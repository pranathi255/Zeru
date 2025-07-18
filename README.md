# DeFi Wallet Credit Scoring

## Objective
Build a scoring model to assign a score between 0–1000 to Aave V2 wallets based on their transaction history.

## Data Source
- JSON transaction dataset (100K entries)
- Actions: deposit, borrow, repay, redeemunderlying, liquidationcall

## Methodology
- Engineered behavioral features per wallet.
- Designed a scoring heuristic favoring repayments and penalizing risky actions.
- Scores normalized to range 0–1000.

## Run Instructions
```bash
python scripts/score_wallets.py
