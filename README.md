# Company Financial Analysis Tool

A Python-based financial analysis tool developed to evaluate the financial performance of **Datalex plc**, an Irish technology company specialising in digital retail solutions for the global airline industry.

## About Datalex plc

Datalex is an Irish airline retail technology company headquartered in Dublin. The company develops technology that enables airlines to operate more effectively as digital retailers, including solutions for airline offers, pricing, order management, payments and digital commerce.

Its technology is designed to help airlines increase revenue, improve customer experiences, personalise offers and gain greater control over their digital retail operations. Datalex works with airline brands across international markets.

## About This Project

This project uses Datalex plc as a real-world case study to demonstrate how Python can be applied to financial analysis.

The tool takes selected financial information from Datalex's **2024 Annual Report and Financial Statements** and converts the raw financial data into financial ratios, comparisons and written interpretations.

The financial statements report the figures in **US$ thousands**. The figures used in this project have been converted to **US$ millions** to make the analysis easier to read.

### Data Source

The primary source for the financial data is:

**Datalex plc Annual Report and Financial Statements 2024**

The project uses information from Datalex's financial statements, including revenue, operating loss, net income, assets, liabilities, equity, cash, debt, operating cash flow, capital expenditure and market capitalisation.

## What the Tool Does

The tool takes financial data and automatically calculates a range of financial measures before producing a structured financial report.

### Profitability Analysis

The tool calculates:

* Profit Margin
* Return on Assets (ROA)
* Return on Equity (ROE)

It then interprets whether the company was profitable and how effectively it generated returns from its assets and equity.

### Liquidity Analysis

The tool calculates:

* Current Ratio
* Quick Ratio
* Cash Ratio
* Working Capital

These measures help assess the company's ability to meet its short-term financial obligations.

### Leverage Analysis

The tool calculates:

* Debt-to-Equity Ratio
* Debt-to-Assets Ratio

These measures provide an indication of the company's use of debt and the proportion of its assets financed through debt.

### Efficiency Analysis

The tool calculates:

* Asset Turnover
* Interest Coverage

These measures help assess how efficiently the company uses its assets to generate revenue and whether operating performance is sufficient to cover interest expenses.

### Growth Analysis

The tool compares 2024 with 2023 and calculates:

* Revenue Growth
* Change in Net Income

This allows the user to identify whether the company's financial performance improved or deteriorated year over year.

### Cash Flow Analysis

The tool calculates:

* Cash-to-Debt
* Cash-to-Assets
* Free Cash Flow

It also interprets whether operating cash flow and free cash flow are positive or negative.

### Valuation Analysis

The tool calculates:

* Price-to-Book Ratio

It also identifies situations where a P/E ratio may not be meaningful, such as when a company reports a net loss.

### Automated Financial Interpretation

Rather than simply displaying numbers, the program interprets the results.

For example, it can identify:

* Negative profitability
* Weak or strong liquidity
* High leverage
* Declining revenue
* Negative free cash flow
* Changes in net losses
* Potential financial strengths
* Areas that require monitoring

The tool then produces an overall financial interpretation and a summary of key findings.

## Error Handling

The project includes a `safe_divide()` function to handle situations where a financial ratio would require division by zero.

Instead of allowing the program to crash, the function returns `None`, allowing the report to display the relevant calculation as unavailable.

This makes the tool more robust when working with different companies and financial datasets.

## Why This Tool Can Be Useful

Financial statements contain large amounts of information, but raw financial figures do not always provide an immediate picture of a company's financial position.

A financial analysis tool can help turn financial statement data into information that is easier to interpret.

For businesses, similar tools could be used to:

* Quickly assess financial performance
* Monitor profitability
* Track liquidity
* Identify changes in financial health
* Compare performance across financial years
* Support management decision-making
* Highlight areas requiring further investigation
* Reduce repetitive manual calculations
* Standardise financial analysis

For financial analysts, investors and business managers, automating repetitive calculations can allow more time to be spent on interpreting results and making informed decisions.

## Technologies Used

* Python
* Python functions
* Conditional statements
* Financial calculations
* Error handling
* Financial ratio analysis

## Key Skills Demonstrated

This project demonstrates the application of:

* Financial analysis
* Financial modelling concepts
* Python programming
* Functions
* Conditional logic
* Data handling
* Error handling
* Financial ratio interpretation
* Year-on-year analysis
* Automated reporting

## Current Version

The current version analyses Datalex plc's 2024 financial performance using data from its published annual report.

This is the first version of the tool and is designed as a foundation for a more flexible financial analysis application.

## Future Improvements

Future versions could allow users to:

* Enter financial data directly into the program
* Analyse different companies
* Compare multiple companies
* Analyse several years of financial data
* Automatically import financial data
* Add additional valuation metrics
* Create charts and visualisations
* Generate downloadable financial reports
* Build a simple graphical user interface

## Project Purpose

The purpose of this project is to demonstrate how financial knowledge and programming can be combined to create a practical financial analysis application.

Rather than analysing financial statements manually, the tool demonstrates how Python can automate calculations and transform financial data into a structured financial report.

## Author

**Grace Waithera**

Financial Engineering Graduate | 

Interested in financial analysis, financial modelling, fintech, and climate finance.

