# Variable Definitions

This document provides comprehensive definitions for all variables used in the Forex Trader Behavior Analysis project. Variables are organized by category and include their source, meaning, and relevance to the analysis.

## Table of Contents

- [Dependent Variables](#dependent-variables)
- [Transaction Outcome Variables](#transaction-outcome-variables)
- [Social Feature Variables](#social-feature-variables)
- [Trader-Level Control Variables](#trader-level-control-variables)
- [Transaction-Level Control Variables](#transaction-level-control-variables)
- [Market-Level Control Variables](#market-level-control-variables)
- [Derived Variables](#derived-variables)

## Dependent Variables

### Tij (Transaction Duration)
- **Definition**: Duration of transaction *i* by trader *j* from time of purchase to time of sale, measured in seconds
- **Source**: Derived from trading history data
- **Calculation**: `date_closed - date_open` (in seconds)
- **Relevance**: Primary dependent variable measuring how long traders hold positions

## Transaction Outcome Variables

### Gain
- **Definition**: Indicator for whether transaction *i* was sold with a gain (value of 1) or loss (value of 0)
- **Source**: Platform data, derived from price comparison
- **Calculation**: 1 if `price_closed > price_open` for BUY positions (or `price_closed < price_open` for SELL positions), 0 otherwise
- **Relevance**: Used to determine if a trade was profitable and for calculating disposition effect

### Disposition Effect
- **Definition**: Difference between proportion of gains realized versus losses realized
- **Source**: Derived variable
- **Calculation**: `prop_closed_gains - prop_closed_loss`
- **Relevance**: Measures the tendency to sell winning positions too early and hold losing positions too long

## Social Feature Variables

### Views
- **Definition**: Cumulative number of views originating from registered accounts to trader *j*'s page
- **Source**: Platform data (overview_page_data)
- **Field**: `viewed_no_of_times`
- **Relevance**: Quantifies social visibility and attention received by the trader

### Views_previous
- **Definition**: Number of views at the previous observation point
- **Source**: Derived from platform data
- **Relevance**: Used to calculate changes in social visibility

### Views_change
- **Definition**: Change in trader *j*'s page views between purchase and selling
- **Source**: Derived from platform data
- **Calculation**: `views - first_views` (where first_views is the views at transaction open)
- **Relevance**: Measures growth in social attention during the transaction's lifecycle

### Followers
- **Definition**: Number of copiers of the trading investment pattern of trader *j*
- **Source**: Platform data (compute table)
- **Field**: `followers`
- **Relevance**: Indicates social influence and trust in the trader's strategy

### Prev_followers
- **Definition**: Number of followers at the previous observation point
- **Source**: Derived from platform data
- **Relevance**: Used to track changes in follower count

## Trader-Level Control Variables

### Rank
- **Definition**: Rank of trader *j* at time *t*
- **Source**: Platform data (compute table)
- **Field**: `zulu_rank`
- **Relevance**: Represents the trader's standing in the platform hierarchy

### Rank_change
- **Definition**: Change in trader *j*'s rank between time of purchase and time of selling
- **Source**: Derived from platform data
- **Calculation**: `open_rank - observed_rank`
- **Relevance**: Indicates improvement or deterioration in trader standing during transaction

### Avg_rank_1m
- **Definition**: Average rank of trader *j* over the month preceding the purchase
- **Source**: Derived from platform data
- **Calculation**: Average of all rank values over 30 days prior to observation date
- **Relevance**: Provides context on the trader's recent performance trajectory

### Cohort_min_rank
- **Definition**: Minimum rank amongst ten nearest traders based on rank to trader *j* at purchase
- **Source**: Derived from platform data
- **Calculation**: Minimum rank value from a cohort of 10 traders with ranks closest to the target trader
- **Relevance**: Provides social comparison context for the trader

### Conc_transactions
- **Definition**: Total number of transactions concurrent to transaction *i* purchased by trader *j* at purchase
- **Source**: Derived from trading history data
- **Calculation**: Count of open transactions for the trader at date_observed
- **Relevance**: Indicates portfolio complexity and diversification

### Conc_currencies
- **Definition**: Total number of currencies concurrent to transaction *i* purchased by trader *j* at purchase
- **Source**: Derived from trading history data
- **Calculation**: Count of unique currencies in open transactions for the trader at date_observed
- **Relevance**: Measures currency diversification strategy

### Cum_day
- **Definition**: Cumulative number of days trader *j* is on the platform up to purchase
- **Source**: Platform data (overview_page_data)
- **Calculation**: `weeks * 7` (converted from weeks to days)
- **Relevance**: Proxy for trader experience

### Cum_profit_in_pips
- **Definition**: Cumulative profit made by trader *j* up to purchase in pips
- **Source**: Platform data (overview_page_data)
- **Field**: `profit_in_pips`
- **Relevance**: Measures overall trading success

### Cum_profit
- **Definition**: Cumulative profit made by trader *j* up to purchase in account currency
- **Source**: Platform data (compute table)
- **Field**: `cum_profit`
- **Relevance**: Alternative measure of overall trading success

### Cum_trades
- **Definition**: Cumulative number of transactions by trader *j* up to purchase
- **Source**: Platform data (overview_page_data/compute table)
- **Field**: `trades` or `cum_trades`
- **Relevance**: Indicates trading activity level and experience

### Amount_following
- **Definition**: Total amount of money following trader *j* up to purchase
- **Source**: Platform data (compute table)
- **Field**: `amount_following`
- **Relevance**: Measures financial trust placed in the trader by followers

### Amount_following_new
- **Definition**: New money following the trader since previous observation
- **Source**: Platform data (compute table)
- **Field**: `amount_following_new`
- **Relevance**: Indicates growth in financial trust

### Total_follower_profit
- **Definition**: Total profit of followers of trader *j* up to purchase
- **Source**: Platform data (compute table)
- **Field**: `total_follower_profit`
- **Relevance**: Measures the financial success of the trader's followers

### Gain_days
- **Definition**: Cumulative number of days with gain across all trader *j*'s open transactions up to purchase
- **Source**: Derived/Platform data (compute table)
- **Field**: `cum_gain_days`
- **Relevance**: Measures consistency of profitable performance

### N_open_gain
- **Definition**: Number of open positions with gains
- **Source**: Derived from trading history and exchange rate data
- **Relevance**: Used in calculating disposition effect

### N_open_loss
- **Definition**: Number of open positions with losses
- **Source**: Derived from trading history and exchange rate data
- **Relevance**: Used in calculating disposition effect

### N_closed_gain
- **Definition**: Number of closed positions with gains
- **Source**: Derived from trading history and exchange rate data
- **Relevance**: Used in calculating disposition effect

### N_closed_loss
- **Definition**: Number of closed positions with losses
- **Source**: Derived from trading history and exchange rate data
- **Relevance**: Used in calculating disposition effect

### Prop_closed_gains
- **Definition**: Proportion of gains realized
- **Source**: Derived calculation
- **Calculation**: `n_closed_gain / (n_closed_gain + n_open_gain)` if denominator > 0, else 0
- **Relevance**: Key component in disposition effect calculation

### Prop_closed_loss
- **Definition**: Proportion of losses realized
- **Source**: Derived calculation
- **Calculation**: `n_closed_loss / (n_closed_loss + n_open_loss)` if denominator > 0, else 0
- **Relevance**: Key component in disposition effect calculation

## Transaction-Level Control Variables

### Lots
- **Definition**: Lot size of transaction *i* opened by trader *j*
- **Source**: Platform data (trading_history_data)
- **Field**: `lots`
- **Relevance**: Indicates position size and risk level

### Neg_rate_diff
- **Definition**: Difference between the lowest exchange rate observed during the life of transaction *i* and the exchange rate at time of transaction sale
- **Source**: Derived from exchange rate data
- **Calculation**: `close_rate - lowest_rate`
- **Relevance**: Captures missed profit opportunities and potential regret

### Avg_slippage
- **Definition**: Average difference between transaction *i*'s expected price and the actual price at which the transaction is sold
- **Source**: Platform data (compute table)
- **Field**: `avg_slippage`
- **Relevance**: Measures execution quality and trading costs

### 24hr_avg_rate
- **Definition**: Average currency exchange rate over the last 24 hours prior to transaction *i*'s closing time
- **Source**: Derived from exchange rate data
- **Calculation**: Average of rates over 24 hours before closing
- **Relevance**: Provides recent market context for the transaction

### Fx_rate_idx
- **Definition**: Average currency exchange rate over the transaction *i*'s holding time
- **Source**: Derived from exchange rate data
- **Calculation**: Average of rates between opening and closing times
- **Relevance**: Provides overall market context during the transaction's life

## Market-Level Control Variables

### Log_garch
- **Definition**: GARCH volatility measure of the currency pair
- **Source**: Derived from exchange rate data
- **Calculation**: Log-transformed GARCH volatility estimate
- **Relevance**: Measures market volatility and risk

### Money_flow_idx
- **Definition**: Daily average rate over the last 14 days up to purchase
- **Source**: Derived from exchange rate data
- **Calculation**: 14-day average exchange rate
- **Relevance**: Indicates medium-term market trend

### Bollinger_band
- **Definition**: Three-day average up to purchase of the envelopes based on one standard deviation above and below a simple moving average of the currency exchange rate
- **Source**: Derived from exchange rate data
- **Calculation**: Moving average ± standard deviation
- **Relevance**: Captures market volatility and potential reversal points

### Market_idx
- **Definition**: Deutsche Bank Forex volatility index measuring market overall exchange rates volatility
- **Source**: External market data
- **Relevance**: Provides broad market context for trading decisions

## Derived Variables

### Trade_no
- **Definition**: Sequential counter for trades by a specific trader
- **Source**: Derived from trading history data
- **Calculation**: Incremented counter per trader
- **Relevance**: Used to track trading sequence

### Observation_number
- **Definition**: Sequential counter for observations within a transaction
- **Source**: Derived during analysis
- **Calculation**: Incremented counter per trade
- **Relevance**: Used to track observation sequence
