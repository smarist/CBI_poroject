# type: ignore
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pandas as pd

# Given data
data = [
    {"Name": "DATE", "Sentence": "9 May 1979 INTERVIEWER"},
    {"Name": "LOCATION", "Sentence": "Stanford, CA  McCORDUCK"},
    {"Name": "FORSYTHE", "Sentence": "Same day.  McCORDUCK"},
    {"Name": "FORSYTHE", "Sentence": "Yes.  McCORDUCK"},
    {"Name": "FORSYTHE", "Sentence": "No, I never finished.  But Jack and George got theirs on the 14th of June in 1941, and George's father was a doctor; he ran a health service at the University of Michigan, and so he could come to Providence for either the Ph.D. or a wedding, but probably not twice, so we just arranged to do it the same day.  FORSYTHE"},
    {"Name": "McCORDUCK", "Sentence": "Yes, I was a student at Brown.  FORSYTHE"},
    {"Name": "McCORDUCK", "Sentence": "Well first, the year after we got married, George had the rating -- I forget what -- so he was liable to be called for military duty and he had an appointment here at Stanford and I had an appointment to teach at Vassar so much to everybody's amazement, I went to teach at Vassar and he came here to Stanford.  McCORDUCK"},
    {"Name": "FORSYTHE", "Sentence": "He thought that he would probably only be one quarter here, but actually it was between the Winter and Spring quarter when he was actually called up and they sent him to UCLA to become a meteorologist.  I taught that year at Vassar and toward the end of the year, the woman who was the head of the mathematics department told me to go out to UCLA and look it over and see if I could get a job and if it looked as though it would be a good idea for me to be out there.  She offered me my job back at Vassar with a big raise if I stayed there, but I decided to go out to Los Angeles and went to work for Douglas Aircraft in the aerodynamics division and actually I was put in charge of computing airfoils and pressures on airfoils, and it was a computation that took a week.  McCORDUCK"},
    {"Name": "FORSYTHE", "Sentence": "Desk calculators -- Marchants.  And that was really the first real computation -- I'd come home every night and ask George how to get out of the problems I got into because we were supposed to compute the pressure all along this airfoil.  They had always done it in windtunnels, I guess, and they wanted to get to the state of doing it with a formula and with splines.  And they had one that went quite a ways and then at the very front there was a different one and there you were vertical.  I'd get out these books and try to substitute their formulas and everything would blow up near the nose and nobody gave me any direction. They said \"Well, this is what you're supposed to be able to do\" and they didn't have many mathematicians around.  What Douglas did was to put two groups, one in one part of the company and one in another part of the company and set us both off and then compare our results.  We were on the same problem.  They didn't tell us.  We just discovered it.  McCORDUCK"}
]

# Extract sentences
sentences = [entry["Sentence"] for entry in data]

# Create a DataFrame for visualization
df = pd.DataFrame(data)

# Bag of Words (BoW) embedding
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# K-Means clustering
k = 2  # Number of clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Assign clusters to sentences
clusters = kmeans.labels_

# Add cluster labels to the DataFrame
df['Cluster'] = clusters

# Print the DataFrame with cluster labels
print(df)
