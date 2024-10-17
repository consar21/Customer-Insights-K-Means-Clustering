import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Load the customer data
data = pd.read_excel(r'C:\Users\sara\Downloads\Mall_Customers_Extended.xlsx')
X = data[['Annual Income (k$)', 'Spending Score (1-100)']].values

# Number of clusters and maximum iterations
k = 5
max_iters = 100

# Initialize centroids randomly from the data points
def initialize_centroids(X, k):
    indices = np.random.choice(X.shape[0], k, replace=False)
    return X[indices]

# Assign each data point to the nearest centroid
def assign_clusters(X, centroids):
    clusters = np.zeros(X.shape[0])
    for i, point in enumerate(X):
        min_dist = float('inf')
        for j, centroid in enumerate(centroids):
            dist = np.linalg.norm(point - centroid)
            if dist < min_dist:
                min_dist = dist
                clusters[i] = j
    return clusters

# Update centroids based on the mean of assigned data points
def update_centroids(X, clusters, k):
    centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        points = X[clusters == i]
        if len(points) > 0:
            centroids[i] = points.mean(axis=0)
    return centroids

# K-means clustering algorithm with timing accumulation
def kmeans(X, k, max_iters):
    centroids = initialize_centroids(X, k)
    
    # Initialize accumulators for timing
    total_assign_time = 0.0
    total_update_time = 0.0
    total_iteration_time = 0.0
    
    for iteration in range(max_iters):
        iter_start_time = time.time()
        
        # Measure assign_clusters time
        start_time = time.time()
        clusters = assign_clusters(X, centroids)
        assign_time = time.time() - start_time
        total_assign_time += assign_time
        
        # Measure update_centroids time
        start_time = time.time()
        new_centroids = update_centroids(X, clusters, k)
        update_time = time.time() - start_time
        total_update_time += update_time
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
        
        # Measure total iteration time
        iter_time = time.time() - iter_start_time
        total_iteration_time += iter_time
        
    # Print out total times for each section
    print(f"Total time for assign_clusters: {total_assign_time:.4f} seconds")
    print(f"Total time for update_centroids: {total_update_time:.4f} seconds")
    print(f"Total time for all iterations: {total_iteration_time:.4f} seconds")
    print("\n")
    print("\n")

    
    return centroids, clusters

# Run the K-means algorithm and measure total times for critical sections
centroids, clusters = kmeans(X, k, max_iters)

# Define descriptive labels based on the characteristics of clusters
cluster_labels = [
    "High Income, High Spend",
    "High Income, Low Spend",
    "Low Income, High Spend",
    "Low Income, Low Spend",
    "Moderate Income, Moderate Spend"
]


print_start_time = time.time()

print("Cluster Descriptions and Centroids:")
for i, label in enumerate(cluster_labels):
    print(f"\nCluster '{label}': Centroid at {centroids[i]}")
    print(f"Data Points in Cluster '{label}':\n", X[clusters == i])

print_time = time.time() - print_start_time
print(f"Total time for printing cluster descriptions and centroids: {(print_time)}")