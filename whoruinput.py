import numpy as np
import pickle as pkl
import pandas as pd
from itertools import combinations

with open('responses.pkl', 'rb') as f:
    data = pkl.load(f)
    
names = data['Names']
ages = data['Ages']
responses = data['Responses']

df = pd.DataFrame(data)
df.reset_index(drop=True, inplace=True)

# In the responses matrix, each index contains a vector of length 33 which contains
# all the flattened vectors for each response

print(df)

# Use the itertools library to get every possible combination of 5 
# entries in the datafram using index values 
index_list = df.index.tolist()

groups_of_five_indexes = list(combinations(index_list, 5))

# Define a method to caculate the sum of dots products for 5 vectors 
def sum_of_dot_product(vectors):
    sum = 0

    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j:
                sum += np.dot(vectors[i], vectors[j])

    # / 2 avoids double counting
    return sum / 2 

# Return find the group of 5 people with minimum min_current_overlap_sum 
# Define initial set of vectors with minimum min_current_overlap_sum, 
# a high min_current_overlap_sum threshold, and the minimum min_current_overlap_sum df indexes
vectors = []
min_current_overlap_sum = 10000000000
min_current_overlap_indexes = []

# Loop through each collection of 5 indicies, finding the 
# sum of dot product for each
for indexes in groups_of_five_indexes:

    # Finds the response vectors corresponding to the 5 indexes
    for index in indexes:
        vectors.append(df['Responses'].iloc[index])
    
    # Find the sum of the 5 response vectors
    sum = sum_of_dot_product(vectors)

    # If the sum is smaller than the min current overlap sum,
    # update its value and the min current overlap indexes
    # with the corresponding indexes
    if sum < min_current_overlap_sum:
        min_current_overlap_sum = sum
        min_current_overlap_indexes = indexes 

# Find the names of the 5 people with the most different responses
names = []
for index in min_current_overlap_indexes:
    names.append(df['Names'].iloc[index])

print(names)

    
