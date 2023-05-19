import numpy as np
import pickle as pkl
import pandas as pd

with open('responses.pkl', 'rb') as f:
    data = pkl.load(f)
    
names = data['Names']
ages = data['Ages']
responses = data['Responses']

df = pd.DataFrame(data)

# In the responses matrix, each index contains a vector of length 33 which contains
# all the flattened vectors for each response

print(df)
