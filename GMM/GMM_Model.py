#GMM Model
from sklearn.mixture import GaussianMixture

# Create an instance of the GMM class
gmm = GaussianMixture(n_components=3)

# Fit the GMM model to the data
gmm.fit(X)

# Use the GMM model to predict the cluster labels for new data
labels = gmm.predict(X)
# Predict the probabilities of each data point belonging to each cluster
probs = gmm.predict_proba(X)

# Assign each data point to its most likely cluster
labels = probs.argmax(axis=1)

# Get the samples/points in each cluster
samples_in_cluster = [X[labels == i] for i in range(gmm.n_components)]