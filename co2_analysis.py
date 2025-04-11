# # 🌍 CO₂ Emissions Exploratory Data Analysis
# This notebook analyzes CO₂ emissions data from Our World in Data.

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: seaborn style
sns.set(style="whitegrid")


# In[ ]:


# Load dataset
df = pd.read_csv("owid-co2-data.csv")

# Display the first few rows
df.head()


# In[ ]:


# Filter data for 2020
df_2020 = df[df["year"] == 2020]
top10 = df_2020.sort_values(by="co2", ascending=False).head(10)
top10[["country", "co2"]]


# In[ ]:


# Bar plot for top 10 CO₂ emitting countries
plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x="co2", y="country", palette="Reds_r")
plt.title("Top 10 CO₂ Emitting Countries in 2020")
plt.xlabel("CO₂ Emissions (million tonnes)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()


# In[ ]:


# Trend comparison for India, China, USA (2000–2020)
countries = ["India", "China", "United States"]
df_trend = df[df["country"].isin(countries) & (df["year"] >= 2000)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_trend, x="year", y="co2", hue="country")
plt.title("CO₂ Emissions (2000–2020)")
plt.ylabel("CO₂ Emissions (million tonnes)")
plt.xlabel("Year")
plt.tight_layout()
plt.show()


# In[ ]:


# Correlation heatmap (optional bonus)
df_corr = df[["co2", "gdp", "population", "energy_per_capita"]].dropna()

plt.figure(figsize=(8, 6))
sns.heatmap(df_corr.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between CO₂, GDP, Population, and Energy")
plt.show()
