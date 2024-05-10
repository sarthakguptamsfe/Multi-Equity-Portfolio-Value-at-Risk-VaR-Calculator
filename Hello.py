import streamlit as st
import numpy as np
import requests
import matplotlib.pyplot as plt
import scipy.stats as stats

st.set_page_config(page_title="Multiple-Equity Portfolio Value at Risk (VaR) Calculator")

# Function to fetch stock data
def fetch_stock_data(stock_name, start_date, end_date, API_KEY):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{stock_name}?from={start_date}&to={end_date}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'historical' not in data or not data['historical']:
            return None, "No data available for the selected dates. Please choose another date range."
        else:
            return [day['close'] for day in data['historical']], None
    except Exception as e:
        return None, f"Error fetching stock data: {str(e)}"



image_url = "https://i.postimg.cc/jd3b7X91/Screenshot-2024-05-10-at-12-33-02-AM.png"
st.image(image_url, use_column_width=True)

API_KEY = '0uTB4phKEr4dHcB2zJMmVmKUcywpkxDQ'  # API key for data fetching

# Input field for initial portfolio value
portfolio_value = st.number_input("Enter Initial Portfolio Value (in USD):", min_value=0.0, value=100000.0, step=1000.0, format="%.2f")

# Input fields for the number of stocks, their names, and weights
n = st.slider("Select number of stocks (up to 10):", 1, 10, 1)
stock_names = []
weights = []

for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(f"Enter Stock Name {i+1}:", key=f"stock_{i}")
    with col2:
        weight = st.number_input(f"Enter Weight for Stock {i+1} (%):", 0.0, 100.0, step=5.0, key=f"weight_{i}")
    stock_names.append(name)
    weights.append(weight)

total_weight = sum(weights)
st.write(f"Total Weight: {total_weight}%")  # Display the total weight dynamically

start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

# Storing data and status across sessions
if 'portfolio_returns' not in st.session_state:
    st.session_state['portfolio_returns'] = np.array([])

# Fetch data button
if st.button("Fetch Data and Calculate Statistics"):
    if total_weight != 100:
        st.error("Total weight must be exactly 100%. Please adjust the weights.")
    else:
        portfolio_returns = np.array([])
        for i in range(n):
            stock_data, message = fetch_stock_data(stock_names[i], start_date.isoformat(), end_date.isoformat(), API_KEY)
            if stock_data:
                returns = np.diff(stock_data) / stock_data[:-1]  # daily returns
                weighted_returns = returns * weights[i] / 100
                portfolio_returns = np.concatenate((portfolio_returns, weighted_returns)) if portfolio_returns.size else weighted_returns
            else:
                st.error(message)
                break
        if portfolio_returns.size:
            st.session_state['portfolio_returns'] = portfolio_returns
            st.success("Data fetched and statistics calculated successfully.")
        else:
            st.error("Failed to fetch data for one or more stocks.")
# Function to plot returns
def plot_returns(returns):
    plt.figure(figsize=(10, 6))
    plt.plot(returns, label='Portfolio Returns', color='#ff4c4c')
    plt.title("Portfolio Returns Over Time")
    plt.xlabel("Days")
    plt.ylabel("Returns")
    plt.grid(True)
    plt.legend()
    plt.show()
    st.pyplot(plt)  # Show the plot in the Streamlit app

# VaR Calculation functions
def calculate_var(returns, confidence_level, method, portfolio_value):
    if method == "Historical":
        var = np.percentile(returns, 100 - confidence_level)
    elif method == "Variance-Covariance":
        mean = np.mean(returns)
        sigma = np.std(returns)
        z_score = -(stats.norm.ppf(1 - confidence_level / 100))
        var = -(mean + z_score * sigma)
    elif method == "Monte Carlo":
        simulations = 10000
        mean = np.mean(returns)
        sigma = np.std(returns)
        simulated_returns = np.random.normal(mean, sigma, simulations)
        var = -(np.percentile(simulated_returns, 100 - confidence_level))

    return var * portfolio_value  # Scale the VaR by the portfolio value

# Selection inputs for VaR calculation
var_methods = ["Historical", "Variance-Covariance", "Monte Carlo"]
selected_method = st.selectbox("Select VaR Method:", var_methods)
confidence_level = st.slider("Select Confidence Level:", 1, 99, 95)

# Button to trigger VaR calculation
if st.button("Calculate VaR"):
    if 'portfolio_returns' in st.session_state and st.session_state['portfolio_returns'].size:
        # Plotting the returns
        plot_returns(st.session_state['portfolio_returns'])

        # Calculating VaR
        var = calculate_var(st.session_state['portfolio_returns'], confidence_level, selected_method, portfolio_value)
        st.write(f"Value at Risk (VaR) at {confidence_level}% confidence level using {selected_method} method: ${var:.2f}")
    else:
        st.error("No portfolio data to calculate VaR. Please fetch data first.")
