# imports
# matplotlib inline
import novosparc

import os
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib.pyplot as plt
import altair as alt
from scipy.spatial.distance import cdist, squareform, pdist
from scipy.stats import ks_2samp
from scipy.stats import pearsonr

import random
random.seed(0)

pl_genes = ['sna', 'ken', 'eve']


# Reading expression data to scanpy AnnData (cells x genes)
data_dir = './novosparc/novosparc/datasets/drosophila_scRNAseq/'
data_path = os.path.join(data_dir, 'dge_normalized.txt')
dataset = sc.read(data_path).T
gene_names = dataset.var.index.tolist()

num_cells, num_genes = dataset.shape # 1297 cells x 8924 genes

print('number of cells: %d' % num_cells)
print('number of genes: %d' % num_genes)

# preprocess
# sc.pp.normalize_per_cell(dataset)
# sc.pp.log1p(dataset)

# optional: subset cells
num_cells = 1000
sc.pp.subsample(dataset, n_obs=num_cells)


dge_rep = None # a representation of cells gene expression
sc.pp.highly_variable_genes(dataset)
is_var_gene = dataset.var['highly_variable']
var_genes = list(is_var_gene.index[is_var_gene])

# alternative 1: variable expressed genes representation
dge_rep = dataset.to_df()[var_genes]

# alternative 2: pca representation
sc.pp.pca(dataset)
# dge_rep = pd.DataFrame(dataset.obsm['X_pca'])



atlas_dir = './novosparc/novosparc/datasets/bdtnp/'
target_space_path = os.path.join(atlas_dir, 'geometry.txt')
locations = pd.read_csv(target_space_path, sep=' ')
num_locations = 3039
locations_apriori = locations[:num_locations][['xcoord', 'zcoord']].values


tissue_path = './novosparc/novosparc/datasets/tissue_example.png'
locations_from_image = novosparc.gm.create_target_space_from_image(tissue_path)

locations_from_image = locations_from_image[np.random.choice(locations_from_image.shape[0], num_locations), :]

locations_circle = novosparc.gm.construct_circle(num_locations=num_locations)


tit_size = 15
dpi = 100
fig, ax = plt.subplots(1,3, figsize=(12,3), dpi=dpi)

ax[0].scatter(locations_apriori[:, 0], locations_apriori[:, 1], s=3)
ax[1].scatter(locations_from_image[:, 0], locations_from_image[:, 1], s=3)
ax[2].scatter(locations_circle[:, 0], locations_circle[:, 1], s=3)

ax[0].set_title('Target space available apriori', size=tit_size)
ax[1].set_title('Prior shape without exact locations', size=tit_size)
ax[2].set_title('No prior knowledge of target space', size=tit_size)

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')

plt.tight_layout()
plt.show()


# construct tissue object
tissue = novosparc.cm.Tissue(dataset=dataset, locations=locations_from_image)


num_neighbors_s = num_neighbors_t = 5

# tissue.setup_reconstruction(num_neighbors_s=num_neighbors_s, num_neighbors_t=num_neighbors_t)

# alternative: since we don't have the atlas assumption, we can also setup only the smooth costs.
tissue.setup_smooth_costs(dge_rep=dge_rep, num_neighbors_s=num_neighbors_s, num_neighbors_t=num_neighbors_t)


tissue.reconstruct(alpha_linear=0, epsilon=5e-3)


# reconstructed expression of individual genes
sdge = tissue.sdge
dataset_reconst = sc.AnnData(pd.DataFrame(sdge.T, columns=gene_names))
dataset_reconst.obsm['spatial'] = locations_from_image

novosparc.pl.embedding(dataset_reconst, pl_genes)


# reading reference atlas
locations = locations_apriori
atlas_dir = './novosparc/novosparc/datasets/bdtnp/'
atlas_path = os.path.join(atlas_dir, 'dge.txt')
atlas = sc.read(atlas_path)
atlas_genes = atlas.var.index.tolist()
atlas.obsm['spatial'] = locations

novosparc.pl.embedding(atlas, pl_genes)


# Tip: visualizing loc-loc expression distances vs their physical distances
novosparc.pl.plot_exp_loc_dists(atlas.X, locations)


# Tip: one can test how "spatially informative" are the marker genes. 
# one measure indicating how localized is the expression is Moran's I

mI, pvals = novosparc.an.get_moran_pvals(atlas.X, locations)
df = pd.DataFrame({'moransI': mI, 'pval': pvals}, index=atlas_genes)

gene_max_mI = df['moransI'].idxmax()
gene_min_mI = df['moransI'].idxmin()

title = ['%s, Morans`I=%.02f' % (gene_max_mI, df.loc[gene_max_mI]['moransI']), 
         '%s, Morans`I=%.02f' % (gene_min_mI, df.loc[gene_min_mI]['moransI'])]

novosparc.pl.embedding(atlas, [gene_max_mI, gene_min_mI], title=title)

print('Mean MoransI: %.02f' % df['moransI'].mean())


# construct Tissue object
tissue = novosparc.cm.Tissue(dataset=dataset, locations=locations)


# params for smooth cost
num_neighbors_s = num_neighbors_t = 5

# params for linear cost
markers = list(set(atlas_genes).intersection(gene_names))
atlas_matrix = atlas.to_df()[markers].values
markers_idx = pd.DataFrame({'markers_idx': np.arange(num_genes)}, index=gene_names)
markers_to_use = np.concatenate(markers_idx.loc[markers].values)

# alternative 1: setup both assumptions 
tissue.setup_reconstruction(atlas_matrix=atlas_matrix, 
                            markers_to_use=markers_to_use, 
                            num_neighbors_s=num_neighbors_s, 
                            num_neighbors_t=num_neighbors_t)

# alternative 2: handling each assumption separately
#tissue.setup_smooth_costs(dge_rep=dge_rep)
#tissue.setup_linear_cost(markers_to_use, atlas_matrix)

# compute optimal transport of cells to locations
alpha_linear = 0.8
epsilon = 5e-3
tissue.reconstruct(alpha_linear=alpha_linear, epsilon=epsilon)



# configure locations probability values
rdist = novosparc.gm.prob_dist_from_center(locations)
atlas.obs['Alternative location marginals'] = rdist

novosparc.pl.embedding(atlas, ['Alternative location marginals'])
# tissue.reconstruct(alpha_linear=alpha_linear, epsilon=epsilon, p_locations=rdist)


# reconstructed expression of individual genes
sdge = tissue.sdge
dataset_reconst = sc.AnnData(pd.DataFrame(sdge.T, columns=gene_names))
dataset_reconst.obsm['spatial'] = locations

title = ['%s, corr=%.02f' % (g, pearsonr(dataset_reconst[:,g].X.flatten(), atlas[:,g].X.flatten())[0] ) for g in pl_genes]
novosparc.pl.embedding(dataset_reconst, pl_genes, title=title)


# # cross-validation and self-consistency analysis
# repeats = 3 #10
# num_markerss = [40]
# alpha_linears = np.arange(0.7, 0.9, 0.1) # np.arange(0.5, 1.0001, 0.1)


# df_corr_atlas, df_corr_repeats = novosparc.an.correlation_random_markers(tissue, with_atlas=True, with_repeats=True,
#                              alpha_linears=alpha_linears, epsilons=[epsilon], num_markerss=num_markerss, repeats=repeats)

# base = alt.Chart().mark_boxplot().encode(x=alt.X('alpha_linear:Q', axis=alt.Axis(values=alpha_linears), scale=alt.Scale(zero=False)),
#                                         y=alt.Y('Pearson correlation:Q', scale=alt.Scale(zero=False)),
#                                         color=alt.value('blue'), opacity=alt.value(0.5))

# pl_atlas = base.properties(data=df_corr_atlas, title='Correlation with atlas')
# pl_repeats = base.properties(data=df_corr_repeats, title='Correlation with repeats')

# alt.hconcat(pl_atlas, pl_repeats).configure_axis(grid=False, labelFontSize=15, titleFontSize=20)



# probability of individual cells belonging to each location
gw = tissue.gw
ngw = (gw.T / gw.sum(1)).T
cell_idx = [1, 12]
cell_prb_cols = ['cell %d' % i for i in cell_idx]
dataset_reconst.obs = pd.DataFrame(ngw.T[:, cell_idx], columns=cell_prb_cols)

title=['Cell %d, entropy=%.02f' % (i, novosparc.an.get_cell_entropy(ngw[i,:])) for i in cell_idx]
novosparc.pl.embedding(dataset_reconst, cell_prb_cols, title=title)


# comparing distributions of entropy for transporting a cell to locations
ent_T, ent_T_unif, ent_T_rproj, ent_T_shuf = novosparc.pl.plot_transport_entropy_dist(tissue)

print(ks_2samp(ent_T, ent_T_rproj))
print(ks_2samp(ent_T, ent_T_shuf))


# Looking for spatially informative genes according to reconstruction in highly variable genes

cyc_genes = [g for g in gene_names if g.startswith('Cyc')]
atlas_genes = list(atlas.var_names)
mI_genes = cyc_genes + atlas_genes

tissue.calculate_spatially_informative_genes(mI_genes)
genes_with_scores = tissue.spatially_informative_genes

genes_with_scores.index = genes_with_scores['genes']

gene_groups = {'Atlas': atlas_genes, 'Cell-cycle': cyc_genes}
novosparc.pl.plot_morans_dists(genes_with_scores, gene_groups)

gene_max_mI = genes_with_scores['genes'].iloc[0]
gene_min_mI = genes_with_scores['genes'].iloc[-1]

title = ['%s, Morans`I=%.02f' % (gene_max_mI, genes_with_scores.loc[gene_max_mI]['mI']), 
         '%s, Morans`I=%.02f' % (gene_min_mI, genes_with_scores.loc[gene_min_mI]['mI'])]

novosparc.pl.embedding(dataset_reconst, [gene_max_mI, gene_min_mI], title=title)

print('Mean Morans I for cell-cycle genes: %.02f' % genes_with_scores.loc[cyc_genes]['mI'].mean())
print('Mean Morans I for atlas genes: %.02f' % genes_with_scores.loc[atlas_genes]['mI'].mean())

# plot spatial expression archtypes
num_clusters = 10
atlas_indices = pd.DataFrame(np.arange(num_genes), index=gene_names)[0].loc[atlas_genes].values
archetypes, clusters, gene_corrs = novosparc.rc.find_spatial_archetypes(num_clusters, sdge[atlas_indices,:])

arch_cols = ['archetype %d'% i for i in np.arange(num_clusters)]
dataset_reconst.obs = pd.DataFrame(index=dataset_reconst.obs.index)
df = pd.DataFrame(archetypes.T, columns=arch_cols)
dataset_reconst.obs = pd.concat((dataset_reconst.obs, df), 1)

novosparc.pl.embedding(dataset_reconst, arch_cols)







