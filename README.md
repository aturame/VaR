This project calculates and visualizes Value at Risk (VaR) using historical financial data.

Features
Accepts CSV and Excel files

Handles missing data and ensures correct data types

Calculates daily percentage returns and log-normal returns

Computes historical VaR across multiple confidence levels (90% to 99.9%)

Displays a histogram of losses using statistically-derived bin sizes

Prints the worst-case observed loss

How to Use
Run the script and input the path to your dataset file when prompted.
The dataset must contain at least the following two columns: Date and Open.

Outputs
Histogram plot of daily losses

Value at Risk figures at confidence levels between 90% and 99.9%

Worst-case loss based on historical data

Requirements
This script requires the following Python libraries:

numpy

pandas

matplotlib

scipy (optional, for future extensions)

Notes
This script uses the historical method (non-parametric) to compute VaR.
It can be extended to include Expected Shortfall (CVaR), parametric methods, or portfolio-level risk.
