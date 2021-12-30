import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read dataset
data = pd.read_excel("dataset/ghgp_data_2020.xlsx", sheet_name="Direct Emitters", header=0, skiprows=lambda x: x in range(0,3))
# print(data.dtypes)
print(data.columns.values)
# print(data['Address'].values)

plt.scatter(x=data['Latitude'], y=data['Zip Code'], c='r')
plt.show()
