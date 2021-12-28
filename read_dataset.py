import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read dataset
data = pd.read_excel("dataset/ghgp_data_by_year.xlsx", sheet_name="Direct Emitters", header=0, skiprows=lambda x: x in range(0,3))
print(data.dtypes)
print(data.columns.values)
print(data['Address'].values)

