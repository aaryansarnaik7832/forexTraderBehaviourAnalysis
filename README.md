# Forex Trader Behavior Analysis

## Overview

This project analyzes how social factors influence the trading decisions of forex traders, with a particular focus on the disposition effect—the tendency of traders to sell winning positions too early and hold losing positions too long. Using a comprehensive dataset from a social trading platform, the analysis combines transaction-level data, market conditions, and social metrics to understand trader decision-making.

## Key Research Questions

1. How do social features (page views, followers) affect trader holding periods?
2. Does trader status (rank, performance) influence the disposition effect?
3. How do market conditions interact with behavioral biases in trading decisions?
4. What role does trader experience play in mitigating or exacerbating the disposition effect?

## Data Description

The analysis uses four primary data sources:

- **Trading History Data**: 1.6+ million individual transactions with opening/closing times, prices, currencies, and trader IDs
- **Overview Page Data**: Platform metrics including views, followers, cumulative profits, and performance statistics
- **Exchange Rate Data**: Historical forex rates at hourly intervals for all currency pairs
- **Compute Data**: Pre-computed platform metrics including trader rankings, social activity, and derived performance indicators

## Methodology

The analysis follows these steps:

1. **Data Preprocessing**: Cleaning raw transaction data, unifying timestamps, and handling missing values
2. **Feature Engineering**: Creating derived variables like holding duration, concurrent transactions, disposition effect measures
3. **Market Condition Analysis**: Calculating forex volatility metrics and incorporating them into the analysis
4. **Social Feature Integration**: Quantifying social visibility and following patterns
5. **Disposition Effect Calculation**: Measuring the difference between proportion of gains realized versus losses realized

## Key Variables

| Category | Variable | Description |
|----------|----------|-------------|
| **Dependent** | Transaction Duration | Time from purchase to sale |
|  | Disposition Effect | Difference between proportion of gains vs. losses realized |
| **Social** | Views | Cumulative profile views |
|  | Followers | Number of traders copying the strategy |
| **Trader** | Rank | Platform ranking |
|  | Experience | Days on platform, cumulative trades |
|  | Performance | Cumulative profit, win ratio |
| **Transaction** | Lot Size | Position size |
|  | Market Conditions | Exchange rate volatility, trends |

## Key Findings

Our analysis reveals:

1. Traders with higher social visibility (more views/followers) show different patterns in holding periods for winning vs. losing positions
2. The disposition effect varies significantly based on trader experience and platform status
3. Market volatility interacts with behavioral biases in predictable ways
4. Evidence suggests social observation influences risk-taking behavior in trading decisions

## Repository Structure

```
├── data_processing/
│   ├── preprocessing_files.ipynb        # Data cleaning and preparation
│   ├── derived_variables_creation.ipynb # Creating analysis variables
│   ├── import_database.py               # Database import utilities
├── analysis/
│   ├── final_analysis.ipynb             # Main analysis notebook
│   ├── testing.ipynb                    # Exploratory analysis and tests
├── docs/
│   ├── variable_definitions.md          # Detailed variable documentation
├── README.md                           
├── requirements.txt                     
```

## Installation and Usage

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/forex-trader-behavior.git
   cd forex-trader-behavior
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. The notebooks can be run sequentially starting with data preprocessing and ending with final analysis:
   ```
   jupyter notebook data_processing/preprocessing_files.ipynb
   ```

Note: The raw data is not included due to size and privacy considerations. Sample processed datasets are provided for reference.

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- sqlalchemy
- jupyter

## Future Work

Potential extensions to this research include:
- Incorporating text analysis of trader communications
- Building predictive models for disposition effect
- Analyzing network effects among followers
- Time-series analysis of how behavioral biases evolve with experience

## Acknowledgments

This analysis builds on behavioral finance literature, particularly work on the disposition effect by Shefrin and Statman (1985) and social influence in financial markets by Hirshleifer and Teoh (2009). This work was done in collboration with and under the advisorship of Dr. Wael Jabr from the Pennsylvania State University.
