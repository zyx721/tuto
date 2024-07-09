import matplotlib.pyplot as plt
import pandas as np
df = np.read_csv("income.csv")
print(df)
df.plot(x='income($)',y='count')
plt.show()