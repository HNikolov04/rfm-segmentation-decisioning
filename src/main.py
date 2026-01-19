from data.download_dataset import ensure_dataset
from data.load_data import load_data
from features.rfm_features import calculate_rfm
from models.rfm_model import kmeans_segmentation
from visualization.plots import plot_clusters

def main():
    dataset_path = ensure_dataset("data")

    df = load_data(dataset_path)

    rfm = calculate_rfm(df)

    rfm_clusters = kmeans_segmentation(rfm)

    plot_clusters(rfm_clusters)

    print(rfm_clusters.head())

if __name__ == "__main__":
    main()