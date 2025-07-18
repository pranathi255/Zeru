import json
import os
import pandas as pd
from tqdm import tqdm

INPUT_PATH = "data/user_transactions.json"
OUTPUT_PATH = "wallet_scores.csv"

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found at {path}")
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def engineer_features(data):
    wallets = {}
    for tx in tqdm(data, desc="Processing Transactions"):
        wallet = tx['user']
        action = tx['action']
        if wallet not in wallets:
            wallets[wallet] = {'deposit': 0, 'borrow': 0, 'repay': 0, 'redeemunderlying': 0, 'liquidationcall': 0}
        wallets[wallet][action] += 1
    df = pd.DataFrame.from_dict(wallets, orient='index').reset_index().rename(columns={'index': 'wallet'})
    return df

def assign_scores(df):
    # Very basic scoring model: You can improve this
    df['score'] = (
        df['repay'] * 3 + 
        df['deposit'] * 2 - 
        df['borrow'] * 1 - 
        df['liquidationcall'] * 5
    )
    df['score'] = df['score'].clip(lower=0)
    df['score'] = (df['score'] / df['score'].max()) * 1000
    df['score'] = df['score'].astype(int)
    return df[['wallet', 'score']]

def main():
    data = load_data(INPUT_PATH)
    df_features = engineer_features(data)
    df_scores = assign_scores(df_features)
    df_scores.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Scores saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
