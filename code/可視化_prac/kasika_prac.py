# 可視化
#%%
import seaborn as sns
import matplotlib.pyplot as plt
#%%
# library & dataset
df = sns.load_dataset('iris')

# Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='scatter')
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='hex')
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde')

plt.show()
# %%
print(sns.get_dataset_names())
# %%
print("githubわからん！難しい！")
# %%
