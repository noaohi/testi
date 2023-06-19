import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PEPCK
data_PEPCK = {'Category': ['Control', 'Control', 'Control', 'Starvation', 'Starvation', 'Starvation'],
              'Normalized Gene Expression': [1.290669427, 0.836895583, 0.87243499, 0.86042392, 0.595890659, 0.625516366]}
df_PEPCK = pd.DataFrame(data=data_PEPCK)

print(df_PEPCK)

fig, axes = plt.subplots(1, 2, figsize = (12, 6))
fig_PEPCK = sns.barplot(x='Category', y='Normalized Gene Expression', data=df_PEPCK,
            errorbar = 'sd', edgecolor='black', errcolor='black', errwidth = 1.5,
            color= 'grey', capsize=0.1, ax=axes[0], alpha=0.5)
sns.stripplot(x='Category', y='Normalized Gene Expression', data=df_PEPCK,
              color = 'grey', dodge=True, ax=axes[0], alpha = 0.8)
fig_PEPCK.set_title('PEPCK')
plt.savefig('plot_PEPCK.png')

#G6PC
data_G6PC = {'Category': ['Control', 'Control', 'Control', 'Starvation', 'Starvation'],
              'Normalized Gene Expression': [1.025892537, 0.937492865, 1.036614598, 0.791071288, 1.330418021]}
df_G6PC = pd.DataFrame(data=data_G6PC)

print(df_G6PC)

fig_G6PC = sns.barplot(x='Category', y='Normalized Gene Expression', data=df_G6PC,
            errorbar = 'sd', edgecolor='black', errcolor='black', errwidth = 1.5,
            color = 'grey', capsize=0.1, ax=axes[1], alpha=0.5)
sns.stripplot(x='Category', y='Normalized Gene Expression', data=df_G6PC,
              color = 'grey', dodge=True, ax=axes[1], alpha = 0.8)
fig_G6PC.set_title('G6PC')
plt.savefig('plot_PEPCK_G6PC.png')
