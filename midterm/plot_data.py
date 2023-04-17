import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('output-final.txt', index_col="time", sep=" ")

print(data)
data.plot()
plt.show()