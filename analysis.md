
---

### ✅ Step 5: Create analysis.md with Insights

Example:

```markdown
# Score Analysis

## Score Distribution
- 0-100: 13% wallets — risky, high liquidation
- 900-1000: 8% wallets — excellent behavior

## Graph:
(Use matplotlib/seaborn)

## Observations:
- Wallets with more repayments and fewer liquidations had high scores.
- Many wallets had minimal or only borrowing behavior — these scored lower.
## Score Distribution

![Score Distribution](score_distribution.png)

The chart above shows how the scores are distributed across different ranges. We observe:

- Majority of wallets fall in the 600–800 range, suggesting responsible usage.
- A noticeable number of wallets are in the 0–200 range, likely due to risky or bot-like behavior.
- Very few wallets are in the 900+ range, showing truly ideal behavior.

This distribution helps in defining thresholds for low, medium, and high credit risk.
