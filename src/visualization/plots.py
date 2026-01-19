import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(rfm_df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=rfm_df, x='Recency', y='Monetary', hue='Cluster', palette='Set2', s=100)
    plt.title('RFM Clusters')
    plt.show()