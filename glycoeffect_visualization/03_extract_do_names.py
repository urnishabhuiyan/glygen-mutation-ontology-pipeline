#%%
"""
This script is used to map the do names to the corresponding doids using the HumanDO.tsv 
file downloaded from Disease Ontology. 
"""

import pandas as pd

#Load mapping file
mapping_df = pd.read_csv('HumanDO.tsv', sep='\t')
df = pd.read_csv("concat_data.csv")

#Pull just DOID
mapping_df['id_int'] = mapping_df['id'].str.replace('DOID:', '').astype(int)

#Create column with DO names
do_mapping = dict(zip(mapping_df['id_int'], mapping_df['subClassOf']))

#Map do_name to do_id in df 
df['do_name'] = df['do_id'].map(do_mapping)

#Save output 
df.to_csv('diseaseIDName.csv', index=False)
