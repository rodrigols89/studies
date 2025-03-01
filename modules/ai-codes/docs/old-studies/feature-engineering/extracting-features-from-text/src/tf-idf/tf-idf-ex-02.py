from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

samples = [
    "the mouse ran away from the house",
    "the house had a tiny little mouse",
    "the cat saw the mouse",
    "the cat finally ate the mouse",
    "the end of the mouse story",
]

tfidf_vectorizer_instance = TfidfVectorizer(use_idf=True)  # Instance.
tfidf_vectorizer_vectors = tfidf_vectorizer_instance.fit_transform(samples)

tfidf_df = pd.DataFrame(
    tfidf_vectorizer_vectors.todense().round(2),
    index=samples,
    columns=tfidf_vectorizer_instance.get_feature_names_out(),
)
print(tfidf_df)
