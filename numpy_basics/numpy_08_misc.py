import numpy as np

## Load data from a file
## Delimters of np.genfromtxt
# , , ; , \t
file = np.genfromtxt("free_txt_data_heat_index.txt", delimiter="\t")
#print(file.astype("float32"))

## Boolean Masking and Advanced Indexing
boolean_test = file > 30.0
#print(boolean_test)
filtered_data = file[file > 30.0]
print(filtered_data)