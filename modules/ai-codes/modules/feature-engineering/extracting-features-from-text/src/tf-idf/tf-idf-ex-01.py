from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

samples = [
    "the mouse ran away from the house",
    "the house had a tiny little mouse",
    "the cat saw the mouse",
    "the cat finally ate the mouse",
    "the end of the mouse story",
]

vectorizer = CountVectorizer()  # Instance without stop words.
sparse_matrix = vectorizer.fit_transform(samples)
feature_names = vectorizer.get_feature_names_out()

dense_matrix = sparse_matrix.todense()  # Sparse Matrix to Dense Matrix.
total_words_per_sample = dense_matrix.sum(axis=1)  # Sum of Words Per Sample.
tf_values = dense_matrix.astype(float)  # Mapped dense matrix to calculate the TF.

# Iterate over each sample (total_words_per_sample=[[7] [6] [5] [6] [6]])
for index, total_words in enumerate(total_words_per_sample):
    # Divide the current word (tf_values[index]) occurrences
    # by the total number of words in the current sample.
    tf_values[index] /= total_words

tfidftransformer_instance = TfidfTransformer(smooth_idf=True, use_idf=True)  # Instance.
idf_weights = tfidftransformer_instance.fit(sparse_matrix)  # Train & calculate IDF.
tfidf_matrix = tfidftransformer_instance.transform(sparse_matrix)  # Calculate TF-IDF.

tfidf_df = pd.DataFrame(
    tfidf_matrix.todense().round(2),
    index=samples,
    columns=feature_names
)
print(tfidf_df)
