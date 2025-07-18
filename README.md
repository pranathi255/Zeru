# DeFi Wallet Credit Scoring using Aave V2 Data

This project assigns credit scores (0–1000) to DeFi wallets based on historical behavior using Aave V2 transaction data.

---

## Goal

To identify responsible vs. risky wallets by analyzing their behavior: depositing, borrowing, repaying, or being liquidated.

---

## Project Structure

defi-credit-score/
│
├── data/
│ └── user_transactions.json
├── scripts/
│ └── score_wallets.py
├── output/
│ └── wallet_scores.csv
├── README.md
└── analysis.md

yaml
Copy
Edit

---

## Features Engineered

- `n_deposit`, `n_borrow`, `n_repay`, `n_liquidation`
- `total_deposit`, `total_borrow`, `total_repay`
- `repay_borrow_ratio` — How much was repaid vs. borrowed
- `deposit_borrow_ratio` — Safety buffer via deposits

---

## Scoring Logic

We apply a heuristic formula:

score = (
+ 4 * repay_borrow_ratio
+ 3 * deposit_borrow_ratio
+ 0.1 * n_repay
- 2 * n_liquidation
)

yaml
Copy
Edit

The score is then scaled to 0–1000 using MinMaxScaler.

---

## How to Run

Install dependencies:

```bash
pip install pandas scikit-learn
Run the scoring script:

bash
Copy
Edit
python scripts/score_wallets.py
Output file will be saved to output/wallet_scores.csv.
