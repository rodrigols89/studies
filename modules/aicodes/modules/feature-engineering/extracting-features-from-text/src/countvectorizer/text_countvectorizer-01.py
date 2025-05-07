from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

pd.options.display.max_colwidth = 200

cat_in_the_hat_docs = [
  "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library)",
  "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
  "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
  "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
  "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)" 
]

df = pd.DataFrame(cat_in_the_hat_docs, columns=["Text"])

vectorizer = CountVectorizer() # Instance.
df_vectorized = vectorizer.fit_transform(df['Text'])

print("Sparse Matrix type:", type(df_vectorized))
print("Shape:", df_vectorized.shape)

print("Sparse Matrix:", df_vectorized)

print("Unique words:", vectorizer.get_feature_names_out())

print("Dense Matrix:\n", df_vectorized.toarray())
print("Dense Matrix:\n", df_vectorized.todense())
