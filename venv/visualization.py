import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


wine_data = pd.read_csv('WineQT.csv')


plt.figure(figsize=(10, 6))
sns.histplot(wine_data['alcohol'], bins=20, kde=True, color='blue')
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.show()




