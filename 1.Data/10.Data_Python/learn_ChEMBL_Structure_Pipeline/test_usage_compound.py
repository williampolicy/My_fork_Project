#https://github.com/chembl/ChEMBL_Structure_Pipeline

from chembl_structure_pipeline import standardizer

#Standardise a compound (info)

o_molblock = """
  Mrv1810 07121910172D          

  4  3  0  0  0  0            999 V2000
   -2.5038    0.4060    0.0000 C   0  0  3  0  0  0  0  0  0  0  0  0
   -2.5038    1.2310    0.0000 O   0  5  0  0  0  0  0  0  0  0  0  0
   -3.2182   -0.0065    0.0000 N   0  3  0  0  0  0  0  0  0  0  0  0
   -1.7893   -0.0065    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  1  3  1  0  0  0  0
  1  4  1  4  0  0  0
M  CHG  2   2  -1   3   1
M  END
"""

std_molblock = standardizer.standardize_molblock(o_molblock)
print('----#1. Standardise a compound (info) : \n')
print(std_molblock)

#Get the parent compound (info)

#from chembl_structure_pipeline import standardizer

o_molblock = """
  Mrv1810 07121910262D          

  3  1  0  0  0  0            999 V2000
   -5.2331    1.1053    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.5186    1.5178    0.0000 N   0  3  0  0  0  0  0  0  0  0  0  0
   -2.8647    1.5789    0.0000 Cl  0  5  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
M  CHG  2   2   1   3  -1
M  END
"""

parent_molblock, _ = standardizer.get_parent_molblock(o_molblock)


print('----# 2.Get the parent compound (info) : \n')
print(parent_molblock)



#Check a compound (info)

from chembl_structure_pipeline import checker

o_molblock = """ 
  Mrv1810 02151908462D           
 
  4  3  0  0  0  0            999 V2000 
    2.2321    4.4196    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0 
    3.0023    4.7153    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0 
    1.4117    4.5059    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0 
    1.9568    3.6420    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0 
  1  2  1  1  0  0  0 
  1  3  1  0  0  0  0 
  1  4  1  0  0  0  0 
M  END 
"""

issues = checker.check_molblock(o_molblock)
print('----# 3.Check a compound (info) : \n')
print(issues)