# [Multiple-Equity Portfolio Value at Risk (VaR) Calculator](https://valueatriskmethod.streamlit.app/)


## Overview
The Multiple-Equity Portfolio Value at Risk (VaR) Calculator is an interactive, web-based tool designed for financial analysts, portfolio managers, and investment enthusiasts. This application allows users to dynamically assess the risk associated with a portfolio composed of various stocks, providing insights into potential financial exposure under adverse market conditions.

## Features
- **Dynamic Stock Selection**: Users can select up to 10 different stocks to include in their portfolio, specifying the weight of each stock to reflect its proportion in the overall investment strategy.
- **Real-Time Data Fetching**: The calculator integrates with a financial data API to retrieve real-time historical stock prices for the specified date range, ensuring accurate and up-to-date risk assessment.
- **Customizable Risk Metrics**: It supports various risk measurement techniques, including Historical, Variance-Covariance, and Monte Carlo simulations, offering users the flexibility to choose the method that best fits their risk management needs.
- **Interactive Visualizations**: The application provides graphical representations of portfolio returns over time, helping users visualize the performance and risk profile of their investments.
- **Precise Control Over Parameters**: Users can define the initial portfolio value, select the confidence level for risk assessment, and adjust the weight of individual stocks to simulate different investment scenarios.

## Technologies
- **Streamlit**: Used for creating the intuitive and interactive web interface that powers our application.
- **Python**: The backbone of our tool, providing the computational logic and data handling required to calculate Value at Risk.
- **Matplotlib** and **SciPy**: Utilized for generating plots and statistical functions needed to compute VaR.
- **Requests**: Allows the application to communicate with external financial data APIs to fetch necessary stock price data.

## Usage
This tool is particularly useful for:
- **Risk Assessment**: Quickly calculate the potential loss in a given portfolio, aiding in making informed risk management decisions.
- **Investment Strategy Testing**: Experiment with different portfolio configurations to understand how changes in stock selection and weight can affect the risk profile.
- **Educational Purposes**: Serve as a practical example for those learning about financial risk management, portfolio analysis, and related concepts.

## Getting Started
To get started with the Multiple-Equity Portfolio Value at Risk (VaR) Calculator, clone this repository and follow the setup instructions in the README. You will need an API key from [Financial Modeling Prep](https://financialmodelingprep.com/developer/docs/) to fetch stock data.

## Contributing
Contributions are welcome! Whether it's refining the calculations, enhancing the interface, or adding new features, we encourage you to fork this repository and share your ideas through pull requests.

### How to Contribute
1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Clone the Forked Repo**: Clone the forked repository to your local machine.
3. **Create a New Branch**: Create a new branch to make your changes.
4. **Make Your Changes**: Add new features or make improvements to existing ones.
5. **Commit Changes**: Commit your changes with a clear and descriptive commit message.
6. **Push Changes**: Push your changes to your fork on GitHub.
7. **Submit a Pull Request**: Open a pull request from your fork to the main repository.

We appreciate contributions of all kinds, from bug fixes to feature additions, and even updates to documentation. Every bit helps in making this tool more useful and efficient!

## License
This project is open source and available under the [MIT License](LICENSE).

## Support
If you have any questions or run into issues, please file an issue on the GitHub repository, and we will try to address it as soon as possible.

Thank you for trying out the Multiple-Equity Portfolio Value at Risk (VaR) Calculator. We hope it serves as a valuable tool in your financial analysis toolkit!

