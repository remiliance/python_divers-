import numpy as np
import pandas as pd

import pprint

famille_panda = [
    [100, 5  , 20, 80], # maman panda
    [50 , 2.5, 10, 40], # bébé panda
    [110, 6  , 22, 80], # papa panda
]
famille_panda_df = pd.DataFrame(famille_panda, index = ['maman', 'bebe', 'papa'],
                                columns = ['pattes', 'poil', 'queue', 'ventre'])
print(famille_panda_df)

all_pattes = famille_panda_df["pattes"].dropna().unique()
print("\n******* : ",all_pattes)

data_subset = famille_panda_df[famille_panda_df.poil == 5.0]
print("\n******* \n",data_subset)

print("\n*****\n")
result = {}
result["100"] = data_subset
print(result)


print(len(famille_panda_df))
