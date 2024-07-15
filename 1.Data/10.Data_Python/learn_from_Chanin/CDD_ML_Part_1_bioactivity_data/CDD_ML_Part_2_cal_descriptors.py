
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
     

#Load bioactivity data
df = pd.read_csv('./bioactivity_data.csv')

#Calculate Lipinski descriptors

# Inspired by: https://codeocean.com/explore/capsules?query=tag:data-curation

def lipinski(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem) 
        moldata.append(mol)
       
    baseData= np.arange(1,1)
    i=0  
    for mol in moldata:        
       
        desc_MolWt = Descriptors.MolWt(mol)
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_NumHDonors = Lipinski.NumHDonors(mol)
        desc_NumHAcceptors = Lipinski.NumHAcceptors(mol)
           
        row = np.array([desc_MolWt,
                        desc_MolLogP,
                        desc_NumHDonors,
                        desc_NumHAcceptors])   
    
        if(i==0):
            baseData=row
        else:
            baseData=np.vstack([baseData, row])
        i=i+1      
    
    columnNames=["MW","LogP","NumHDonors","NumHAcceptors"]   
    descriptors = pd.DataFrame(data=baseData,columns=columnNames)
    
    return descriptors
     
df_lipinski = lipinski(df.canonical_smiles)
print(df_lipinski)
print(df)


df_combined = pd.concat([df,df_lipinski], axis=1)

print(df_combined)



# https://github.com/chaninlab/estrogen-receptor-alpha-qsar/blob/master/02_ER_alpha_RO5.ipynb

print('--------\n')

import numpy as np

def pIC50(input):
    pIC50 = []

    for i in input['standard_value_norm']:
        molar = i*(10**-9) # Converts nM to M
        pIC50.append(-np.log10(molar))

    input['pIC50'] = pIC50
    x = input.drop('standard_value_norm', 1)
        
    return x



x=df_combined.standard_value.describe()
print(df_combined)

print('-------df_combined.standard_value.describe():-\n')
print(x)


def norm_value(input):
    norm = []

    for i in input['standard_value']:
        if i > 100000000:
          i = 100000000
        norm.append(i)

    input['standard_value_norm'] = norm
    x = input.drop('standard_value', 1)
        
    return x




df_norm = norm_value(df_combined)

print('-------df_norm:-\n')
print(norm_value(df_combined))



y=df_norm.standard_value_norm.describe()
print('-------df_norm.standard_value_norm.describe():-\n')
print(y)

df_final = pIC50(df_norm)
print('-------df_final = pIC50(df_norm):-\n')
print(df_final)


df_final.pIC50.describe()
z=df_final.pIC50.describe()
print('-------df_final.pIC50.describe():-\n')
print(z)



df_2class = df_final[df_final.bioactivity_class != 'intermediate']
print('-------df_2class = df_final[df_final.bioactivity_class != :-\n')
print(df_2class)



import seaborn as sns
sns.set(style='ticks')
import matplotlib.pyplot as plt

plt.figure(figsize=(5.5, 5.5))

sns.countplot(x='bioactivity_class', data=df_2class, edgecolor='black')

plt.xlabel('Bioactivity class', fontsize=14, fontweight='bold')
plt.ylabel('Frequency', fontsize=14, fontweight='bold')

plt.savefig('plot_bioactivity_class.pdf')

