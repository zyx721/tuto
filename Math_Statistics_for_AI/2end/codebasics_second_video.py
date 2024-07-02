import pandas as pd
import seaborn as sn

df = pd.read_csv("heights.csv")

print(df.height.describe())

sn.histplot(df['height'], kde=True).set(
    title='Height Distribution with KDE',
    xlabel='Height',
    ylabel='Frequency'
)

# plt.show()
mean = df.height.mean()
std = df.height.std()
m1 = mean - 3*std
m2 = mean + 3*std
print(df[(df.height > m2) | (df.height < m1)])
df_clean = df[(df.height < m2) & (df.height > m1)]
print(df_clean.shape)
print(df.shape)
df['zscore'] = (df.height - df.height.mean())/df.height.std()

df = df[(df.zscore > -3) & (df.zscore < 3)]
print(df.shape)