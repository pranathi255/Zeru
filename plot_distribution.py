import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load wallet scores
df = pd.read_csv("data/wallet_scores.csv")

# Bin the scores
bins = range(0, 1100, 100)
df['score_range'] = pd.cut(df['score'], bins)

# Plot distribution
plot = sns.countplot(data=df, x='score_range')
plt.xticks(rotation=45)
plt.title("Wallet Score Distribution")

# Save plot
plt.tight_layout()
plt.savefig("score_distribution.png")
