# Customer Segmentation using K-Means Clustering

## Overview

This project applies K-Means clustering to segment customers based on their age, annual income, and spending score. The goal is to identify distinct customer groups that can help businesses make better marketing decisions.

---

## Dataset

The dataset used is the Mall Customer Segmentation dataset, which includes:

* Age
* Annual Income (k$)
* Spending Score (1–100)

The CustomerID column was removed as it does not contribute to clustering.

---

## Approach

1. **Data Preprocessing**

   * Selected relevant numerical features
   * Applied feature scaling using StandardScaler to normalize data

2. **Choosing Optimal Clusters**

   * Used the Elbow Method to determine the optimal number of clusters (K = 4)

3. **Model Training**

   * Applied K-Means clustering with K = 4

4. **Visualization**

   * Plotted clusters using Income vs Spending Score
   * Highlighted centroids for each cluster

---

## Results & Insights

The model identified four distinct customer segments:

* **Cluster 0:** Young customers with low income but high spending
* **Cluster 1:** High-income customers with low spending (potential targets)
* **Cluster 2:** Mid-income, average spending customers
* **Cluster 3:** Older, high-income customers with very low spending

These insights can help businesses:

* Target high-income low-spending customers with promotions
* Retain high-spending younger customers
* Design personalized marketing strategies

---

## Key Learnings

* Importance of feature scaling in distance-based algorithms
* How to determine optimal K using the Elbow Method
* Translating clustering results into meaningful business insights

---

## Future Improvements

* Use Silhouette Score for better validation
* Try other clustering algorithms like DBSCAN
* Build an interactive dashboard using Streamlit

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Output Example

<img width="613" height="463" alt="image" src="https://github.com/user-attachments/assets/e6e515bf-64ae-4079-af4b-30c8ef2d1135" />


---

## Conclusion

K-Means clustering is a simple yet powerful technique for customer segmentation. This project demonstrates how raw data can be transformed into actionable insights.
