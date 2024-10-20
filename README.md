#  K-means Clustering Project

## 1. Introduction to the Topic
   ### 1.1 History and Background
   
   The K-means clustering algorithm, introduced by Stuart Lloyd in 1957, is a foundational technique in unsupervised learning. Initially applied in pulse-code modulation, it has become a widely-used tool across various fields due to its simplicity and effectiveness in partitioning data into clusters based on similarity.

   ### 1.2 What is K-Means Algorithm
   K-means is a clustering algorithm that divides data into `k` clusters by assigning each data point to the nearest centroid, forming clusters based on distance. 

   ### 1.3 How K-means Works:
   - **Initialization**: Choose `k` random centroids from the dataset.
   - **Assignment**: Assign each data point to the closest centroid based on Euclidean distance.
   - **Update**: Recalculate the centroids by averaging the points within each cluster.
   - **Repeat**: Steps 2 and 3 are repeated until the centroids no longer change or a specified maximum number of iterations is reached.

   ### 1.4 Applications of K-means
   K-means clustering is widely used in various domains, including:
   - **Customer Segmentation**: Grouping customers based on purchasing behavior.
   - **Image Compression**: Reducing the number of colors in an image by clustering pixel values.
   - **Anomaly Detection**: Identifying unusual patterns in datasets, such as fraud detection.
   - **Market Basket Analysis**: Analyzing customer purchasing trends to group products.

   ### 1.5 Importance of Parallelization
   Parallelizing the K-means algorithm is crucial when dealing with large datasets because:
   - **Enhanced Processing Speed**: Large datasets can be processed faster, allowing for quicker insights.
   - **Real-time Analysis**: Parallelization enables real-time analysis, which is essential for applications requiring immediate decisions.
   - **Cost Efficiency**: Optimizing resource usage helps in reducing computational costs and increasing system efficiency.

## 2. Implementation
   ### 2.1 Sequential Code Complexity Analysis
   - **Time Complexity**: The K-means algorithm's time complexity is \(O(n \times k \times i \times d)\), where `n` is the number of data points, `k` is the number of clusters, `i` is the number of iterations, and `d` is the data dimensionality. 
   - **Space Complexity**: The space complexity is \(O(n + k + d)\), primarily due to the storage required for clusters, centroids, and data points.

   ### 2.2 Parallelization Opportunities
   
   In the K-means algorithm, certain tasks can benefit significantly from parallelization:
   - **Cluster Assignment**: Calculating the distance between data points and centroids is independent for each point, making it ideal for parallel execution.
   - **Centroid Update**: The calculation of new centroids can also be parallelized, especially beneficial when working with high-dimensional data.

   ### 2.3 Output of Sequential Code
   After running the K-means algorithm sequentially, the following performance metrics and cluster information were obtained:

                           ``` 
                           Total time for assign_clusters: 143.5992 seconds
                           Total time for update_centroids: 0.3440 seconds
                           Total time for all iterations: 131.1577 seconds
                           
                           
                           
                           
                           Cluster Descriptions and Centroids:
                           
                           Cluster 'High Income, High Spend': Centroid at [25.46011238 19.99283218]
                           Data Points in Cluster 'High Income, High Spend':
                            [[15 39]
                            [16  6]
                            [17 40]
                            ...
                            [26  8]
                            [18 19]
                            [31 18]]
                           
                           Cluster 'High Income, Low Spend': Centroid at [25.49664812 78.48512465]
                           Data Points in Cluster 'High Income, Low Spend':
                            [[15 81]
                            [16 77]
                            [17 76]
                            ...
                            [31 75]
                            [29 79]
                            [36 88]]
                           
                           Cluster 'Low Income, High Spend': Centroid at [87.5013484  16.78698158]
                           Data Points in Cluster 'Low Income, High Spend':
                            [[70 29]
                            [71 11]
                            [71  9]
                            ...
                            [79 13]
                            [71 15]
                            [78 11]]
                           
                           Cluster 'Low Income, Low Spend': Centroid at [86.32229157 81.82287431]
                           Data Points in Cluster 'Low Income, Low Spend':
                            [[ 69  91]
                            [ 70  77]
                            [ 71  95]
                            ...
                            [ 75  88]
                            [124  81]
                            [ 97  88]]
                           
                           Cluster 'Moderate Income, Moderate Spend': Centroid at [54.87171662 49.08631298]
                           Data Points in Cluster 'Moderate Income, Moderate Spend':
                            [[39 36]
                            [39 61]
                            [40 55]
                            ...
                            [52 59]
                            [65 59]
                            [69 35]]
                           Total time for printing cluster descriptions and centroids: 0.056539058685302734
                           ```

     



   - **Cluster Descriptions and Centroids**:
     - **High Income, High Spend**: Centroid at `[25.46, 19.99]`
       - Data points in this cluster represent customers with high income and high spending habits.
     - **High Income, Low Spend**: Centroid at `[25.50, 78.49]`
       - Data points here indicate customers with high income but low spending.
     - **Low Income, High Spend**: Centroid at `[87.50, 16.79]`
       - Represents customers with low income but high spending tendencies.
     - **Low Income, Low Spend**: Centroid at `[86.32, 81.82]`
       - Comprises customers with both low income and low spending.
     - **Moderate Income, Moderate Spend**: Centroid at `[54.87, 49.09]`
       - Indicates a balanced group with moderate income and spending levels.

This README provides a comprehensive overview of the project, from understanding the basics of K-means and its applications to analyzing the need for parallelization and the output of the sequential implementation.
