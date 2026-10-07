# A Company Financial Analysis Tool takes a company's financial information
# and uses it to calculate important financial measures, then presents
# the results in an easy-to-understand way.

# ---------------------------------------------------------
# IRISH COMPANY FINANCIAL ANALYSIS TOOL
# Company: Datalex plc
# Financial Year: 2024
# ---------------------------------------------------------

company_name = "Datalex plc"
financial_year = 2024


# ---------------------------------------------------------
# REPORT HEADER
# ---------------------------------------------------------

print("=" * 60)
print("COMPANY FINANCIAL ANALYSIS REPORT")
print("=" * 60)
print("Company:", company_name)
print("Financial Year:", financial_year)
print("=" * 60)


# ---------------------------------------------------------
# FINANCIAL DATA
# ---------------------------------------------------------

# Financial data in USD millions

revenue = 27.481
revenue_2023 = 28.895
operating_loss = -7.479
net_income = -10.226
net_income_2023 = -6.6

# Balance sheet data in USD millions

total_assets = 18.286
current_assets = 14.350
current_liabilities = 13.152
total_equity = 0.138
cash = 6.370
total_debt = 0.704

# Other financial data

inventory = 0
interest_expense = 2.7
market_cap = 114.02
operating_cash_flow = -5.090
capital_expenditure = 1.313


# ---------------------------------------------------------
# ERROR HANDLING
# ---------------------------------------------------------

def safe_divide(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator


# ---------------------------------------------------------
# FINANCIAL DATA DISPLAY
# ---------------------------------------------------------

print()
print("FINANCIAL DATA")
print("-" * 60)

print("Revenue:              $", revenue, "million")
print("Operating Loss:       $", operating_loss, "million")
print("Net Income:           $", net_income, "million")
print("Total Assets:         $", total_assets, "million")
print("Current Assets:       $", current_assets, "million")
print("Current Liabilities:  $", current_liabilities, "million")
print("Total Equity:         $", total_equity, "million")
print("Cash:                 $", cash, "million")
print("Total Debt:           $", total_debt, "million")


# ---------------------------------------------------------
# PROFITABILITY CALCULATIONS
# ---------------------------------------------------------

def calculate_profit_margin(net_income, revenue):
    result = safe_divide(net_income, revenue)
    if result is None:
        return None
    return result * 100


def calculate_roa(net_income, total_assets):
    result = safe_divide(net_income, total_assets)
    if result is None:
        return None
    return result * 100


def calculate_roe(net_income, total_equity):
    result = safe_divide(net_income, total_equity)
    if result is None:
        return None
    return result * 100


profit_margin = calculate_profit_margin(net_income, revenue)
roa = calculate_roa(net_income, total_assets)
roe = calculate_roe(net_income, total_equity)


# ---------------------------------------------------------
# LIQUIDITY CALCULATIONS
# ---------------------------------------------------------

def calculate_current_ratio(current_assets, current_liabilities):
    result = safe_divide(current_assets, current_liabilities)
    if result is None:
        return None
    return result


def calculate_quick_ratio(current_assets, inventory, current_liabilities):
    result = safe_divide(current_assets - inventory, current_liabilities)
    if result is None:
        return None
    return result


def calculate_cash_ratio(cash, current_liabilities):
    result = safe_divide(cash, current_liabilities)
    if result is None:
        return None
    return result


current_ratio = calculate_current_ratio(
    current_assets,
    current_liabilities
)

quick_ratio = calculate_quick_ratio(
    current_assets,
    inventory,
    current_liabilities
)

cash_ratio = calculate_cash_ratio(
    cash,
    current_liabilities
)


# ---------------------------------------------------------
# LEVERAGE CALCULATIONS
# ---------------------------------------------------------

def calculate_debt_to_equity(total_debt, total_equity):
    result = safe_divide(total_debt, total_equity)
    if result is None:
        return None
    return result


def calculate_debt_to_assets(total_debt, total_assets):
    result = safe_divide(total_debt, total_assets)
    if result is None:
        return None
    return result * 100


debt_to_equity = calculate_debt_to_equity(
    total_debt,
    total_equity
)

debt_to_assets = calculate_debt_to_assets(
    total_debt,
    total_assets
)


# ---------------------------------------------------------
# EFFICIENCY CALCULATIONS
# ---------------------------------------------------------

def calculate_asset_turnover(revenue, total_assets):
    result = safe_divide(revenue, total_assets)
    if result is None:
        return None
    return result


def calculate_interest_coverage(operating_loss, interest_expense):
    result = safe_divide(operating_loss, interest_expense)
    if result is None:
        return None
    return result


asset_turnover = calculate_asset_turnover(
    revenue,
    total_assets
)

interest_coverage = calculate_interest_coverage(
    operating_loss,
    interest_expense
)


# ---------------------------------------------------------
# GROWTH CALCULATIONS
# ---------------------------------------------------------

def calculate_revenue_growth(revenue, revenue_2023):
    result = safe_divide(revenue - revenue_2023, revenue_2023)
    if result is None:
        return None
    return result * 100


def calculate_net_income_change(net_income, net_income_2023):
    return net_income - net_income_2023


revenue_growth = calculate_revenue_growth(
    revenue,
    revenue_2023
)

net_income_change = calculate_net_income_change(
    net_income,
    net_income_2023
)


# ---------------------------------------------------------
# CASH FLOW CALCULATIONS
# ---------------------------------------------------------

def calculate_cash_to_debt(cash, total_debt):
    result = safe_divide(cash, total_debt)
    if result is None:
        return None
    return result


def calculate_cash_to_assets(cash, total_assets):
    result = safe_divide(cash, total_assets)
    if result is None:
        return None
    return result * 100


def calculate_free_cash_flow(operating_cash_flow, capital_expenditure):
    return operating_cash_flow - capital_expenditure


cash_to_debt = calculate_cash_to_debt(
    cash,
    total_debt
)

cash_to_assets = calculate_cash_to_assets(
    cash,
    total_assets
)

free_cash_flow = calculate_free_cash_flow(
    operating_cash_flow,
    capital_expenditure
)


# ---------------------------------------------------------
# WORKING CAPITAL
# ---------------------------------------------------------

def calculate_working_capital(current_assets, current_liabilities):
    return current_assets - current_liabilities


working_capital = calculate_working_capital(
    current_assets,
    current_liabilities
)


# ---------------------------------------------------------
# VALUATION
# ---------------------------------------------------------

def calculate_price_to_book(market_cap, total_equity):
    result = safe_divide(market_cap, total_equity)
    if result is None:
        return None
    return result


price_to_book = calculate_price_to_book(
    market_cap,
    total_equity
)


# ---------------------------------------------------------
# KEY FINANCIAL RATIOS
# ---------------------------------------------------------

print()
print("=" * 60)
print("KEY FINANCIAL RATIOS")
print("=" * 60)

if profit_margin is not None:
    print("Profit Margin:       ", round(profit_margin, 2), "%")
else:
    print("Profit Margin:       Not available")

if roa is not None:
    print("Return on Assets:    ", round(roa, 2), "%")
else:
    print("Return on Assets:    Not available")

if roe is not None:
    print("Return on Equity:    ", round(roe, 2), "%")
else:
    print("Return on Equity:    Not available")

if current_ratio is not None:
    print("Current Ratio:       ", round(current_ratio, 2))
else:
    print("Current Ratio:       Not available")

if quick_ratio is not None:
    print("Quick Ratio:         ", round(quick_ratio, 2))
else:
    print("Quick Ratio:         Not available")

if debt_to_assets is not None:
    print("Debt-to-Assets:      ", round(debt_to_assets, 2), "%")
else:
    print("Debt-to-Assets:      Not available")

if debt_to_equity is not None:
    print("Debt-to-Equity:      ", round(debt_to_equity, 2))
else:
    print("Debt-to-Equity:      Not available")

if asset_turnover is not None:
    print("Asset Turnover:      ", round(asset_turnover, 2))
else:
    print("Asset Turnover:      Not available")

if interest_coverage is not None:
    print("Interest Coverage:   ", round(interest_coverage, 2))
else:
    print("Interest Coverage:   Not available")

if cash_ratio is not None:
    print("Cash Ratio:          ", round(cash_ratio, 2))
else:
    print("Cash Ratio:          Not available")

if price_to_book is not None:
    print("P/B Ratio:           ", round(price_to_book, 2))
else:
    print("P/B Ratio:           Not available")


# ---------------------------------------------------------
# PROFITABILITY ANALYSIS
# ---------------------------------------------------------

print()
print("PROFITABILITY ANALYSIS")
print("-" * 60)

if profit_margin is not None and profit_margin < 0:
    print("The company was not profitable in 2024.")

if roa is not None and roa < 0:
    print("Return on assets was negative, indicating that the company")
    print("was not generating a profit from its asset base.")

if roe is not None and roe < 0:
    print("Return on equity was negative.")
    print("This figure is strongly affected by the company's very low equity.")


# ---------------------------------------------------------
# LIQUIDITY ANALYSIS
# ---------------------------------------------------------

print()
print("LIQUIDITY ANALYSIS")
print("-" * 60)

if current_ratio is not None and current_ratio >= 1:
    print("Current assets were sufficient to cover current liabilities.")
else:
    print("Current assets were lower than current liabilities.")

if quick_ratio is not None and quick_ratio >= 1:
    print("Quick assets were sufficient to cover current liabilities.")
else:
    print("Quick assets were not sufficient to cover current liabilities.")

if cash_ratio is not None and cash_ratio < 1:
    print("Cash alone was not sufficient to cover current liabilities.")
else:
    print("Cash was sufficient to cover current liabilities.")


# ---------------------------------------------------------
# LEVERAGE ANALYSIS
# ---------------------------------------------------------

print()
print("LEVERAGE ANALYSIS")
print("-" * 60)

if debt_to_assets is not None and debt_to_assets < 50:
    print("Debt represented a relatively small proportion of total assets.")
else:
    print("A significant proportion of total assets was financed by debt.")

if debt_to_equity is not None and debt_to_equity > 2:
    print("Debt-to-equity was high.")
    print("However, this ratio is strongly affected by the company's")
    print("very low level of equity.")


# ---------------------------------------------------------
# CASH FLOW ANALYSIS
# ---------------------------------------------------------

print()
print("CASH FLOW ANALYSIS")
print("-" * 60)

if operating_cash_flow < 0:
    print("Operating cash flow was negative.")
else:
    print("Operating cash flow was positive.")

if free_cash_flow < 0:
    print("Free cash flow was negative.")
    print("Operating cash flow was not enough to cover capital expenditure.")
else:
    print("Free cash flow was positive.")


# ---------------------------------------------------------
# GROWTH ANALYSIS
# ---------------------------------------------------------

print()
print("GROWTH ANALYSIS")
print("-" * 60)

if revenue_growth is not None and revenue_growth < 0:
    print("Revenue declined compared with 2023.")
else:
    print("Revenue increased compared with 2023.")

if net_income_change < 0:
    print("The company's net loss increased compared with 2023.")
else:
    print("The company's net result improved compared with 2023.")


# ---------------------------------------------------------
# EFFICIENCY ANALYSIS
# ---------------------------------------------------------

print()
print("EFFICIENCY ANALYSIS")
print("-" * 60)

if asset_turnover is not None and asset_turnover > 1:
    print("The company generated more than $1 of revenue")
    print("for every $1 invested in assets.")
else:
    print("The company generated less than $1 of revenue")
    print("for every $1 invested in assets.")


# ---------------------------------------------------------
# VALUATION ANALYSIS
# ---------------------------------------------------------

print()
print("VALUATION ANALYSIS")
print("-" * 60)

if net_income <= 0:
    print("P/E Ratio: Not meaningful because the company")
    print("reported a net loss.")

if price_to_book is not None:
    print("P/B Ratio:", round(price_to_book, 2))
else:
    print("P/B Ratio: Not available")

if price_to_book is not None and price_to_book > 3:
    print("The P/B ratio was very high.")
    print("This figure is strongly affected by the company's")
    print("very low book equity.")


# ---------------------------------------------------------
# WORKING CAPITAL ANALYSIS
# ---------------------------------------------------------

print()
print("WORKING CAPITAL ANALYSIS")
print("-" * 60)

print("Working Capital: $", round(working_capital, 3), "million")

if working_capital > 0:
    print("The company had positive working capital.")
else:
    print("The company had negative working capital.")


# ---------------------------------------------------------
# YEAR-ON-YEAR COMPARISON
# ---------------------------------------------------------

print()
print("YEAR-ON-YEAR COMPARISON")
print("-" * 60)

print("Revenue 2024:          $", round(revenue, 3), "million")
print("Revenue 2023:          $", round(revenue_2023, 3), "million")
print("Revenue Change:        ", round(revenue_growth, 2), "%")

print()

print("Net Income 2024:       $", round(net_income, 3), "million")
print("Net Income 2023:       $", round(net_income_2023, 3), "million")
print("Change in Net Income:  $", round(net_income_change, 3), "million")


# ---------------------------------------------------------
# OVERALL FINANCIAL INTERPRETATION
# ---------------------------------------------------------

print()
print("=" * 60)
print("OVERALL FINANCIAL INTERPRETATION")
print("=" * 60)

print("Datalex reported a challenging financial performance in 2024.")

if revenue_growth is not None and revenue_growth < 0:
    print("- Revenue declined compared with 2023.")

if net_income_change < 0:
    print("- The company's net loss increased compared with 2023.")

if free_cash_flow < 0:
    print("- Free cash flow was negative, indicating pressure on cash generation.")

if current_ratio is not None and current_ratio >= 1:
    print("- Current assets were slightly higher than current liabilities.")

if debt_to_assets is not None and debt_to_assets < 50:
    print("- Debt represented a relatively small proportion of total assets.")

print()
print("Overall, profitability and cash generation were the main")
print("financial weaknesses identified by the analysis.")


# ---------------------------------------------------------
# KEY FINDINGS
# ---------------------------------------------------------

print()
print("=" * 60)
print("KEY FINDINGS")
print("=" * 60)

if profit_margin is not None and profit_margin < 0:
    print("- The company was not profitable in 2024.")

if revenue_growth is not None and revenue_growth < 0:
    print("- Revenue declined compared with 2023.")

if free_cash_flow < 0:
    print("- Free cash flow was negative.")

if current_ratio is not None and current_ratio >= 1:
    print("- Current assets were higher than current liabilities.")

if debt_to_assets is not None and debt_to_assets < 50:
    print("- Debt represented less than half of total assets.")

print("=" * 60)


# ---------------------------------------------------------
# FINANCIAL SUMMARY
# ---------------------------------------------------------

print()
print("=" * 60)
print("FINANCIAL SUMMARY")
print("=" * 60)

print()
print("STRENGTHS")
print("-" * 60)

if current_ratio is not None and current_ratio >= 1:
    print("- Current assets were sufficient to cover current liabilities.")

if debt_to_assets is not None and debt_to_assets < 50:
    print("- Debt represented a relatively small proportion of total assets.")

if cash_to_debt is not None and cash_to_debt > 1:
    print("- Cash was significantly higher than total debt.")


print()
print("AREAS TO MONITOR")
print("-" * 60)

if current_ratio >= 1 and current_ratio < 1.5:
    print("- The current ratio was only slightly above 1.")

if cash_ratio is not None and cash_ratio < 1:
    print("- Cash alone was not sufficient to cover current liabilities.")

if revenue_growth is not None and revenue_growth < 0:
    print("- Revenue declined compared with the previous year.")


print()
print("FINANCIAL WEAKNESSES")
print("-" * 60)

if profit_margin is not None and profit_margin < 0:
    print("- The company reported a negative profit margin.")

if free_cash_flow < 0:
    print("- Free cash flow was negative.")

if net_income_change < 0:
    print("- The company's net loss increased compared with the previous year.")

if interest_coverage is not None and interest_coverage < 0:
    print("- Operating earnings were insufficient to cover interest expense.")

print()
print("=" * 60)
