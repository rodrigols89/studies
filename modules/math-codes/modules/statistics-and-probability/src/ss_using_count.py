import pandas as pd

# Create DataFrame
df = pd.DataFrame(
    {
        'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'], # Two teams (A and B).
        'position': ['G', 'G', 'F', 'G', 'F', 'F', 'C', 'C'],
        'assists': [5, 7, 7, 8, 5, 7, 6, 9],
        'rebounds': [11, 8, 10, 6, 6, 9, 6, 10]
    }
)

# view DataFrame
# print(df)

# Apply Stratified Random Sampling.
stratifiedRandomSampling = df.groupby(
    'team',
    group_keys=False
).apply(lambda x: x.sample(2))

print(stratifiedRandomSampling)
