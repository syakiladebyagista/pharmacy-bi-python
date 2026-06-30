import pandas as pd
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# dataset dari Power BI
df = dataset.copy()


# Agregasi per obat
cluster_data = df.groupby('Medicine').agg({
    'Stock_Level':'mean',
    'Units_Sold':'sum',
    'Expiry_Days_Remaining':'mean'
}).reset_index()


# Feature
X = cluster_data[['Stock_Level',
                  'Units_Sold',
                  'Expiry_Days_Remaining']]


# Standardisasi
scaler = StandardScaler()


X_scaled = scaler.fit_transform(X)


# KMeans
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)


cluster_data['Cluster'] = kmeans.fit_predict(X_scaled)


# Scatter Plot
plt.figure(figsize=(9,6))


plt.scatter(
    cluster_data['Stock_Level'],
    cluster_data['Units_Sold'],
    c=cluster_data['Cluster'],
    s=120
)
# Nama obat
for i in range(len(cluster_data)):
    plt.text(
        cluster_data['Stock_Level'][i],
        cluster_data['Units_Sold'][i],
        cluster_data['Medicine'][i],
        fontsize=8
    )
plt.xlabel("Average Stock Level")
plt.ylabel("Total Units Sold")
plt.title("Inventory Clustering Analysis")


plt.grid(True)
plt.tight_layout()
plt.show()
