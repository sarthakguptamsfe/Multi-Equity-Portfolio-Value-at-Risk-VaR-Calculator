import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests

# Step 1: Import necessary libraries
def fetch_stock_data(stock_name, start_date, end_date, API_KEY):
    try:
        response = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{stock_name}?from={start_date}&to={end_date}&apikey={API_KEY}")
        data = response.json()
        if 'historical' not in data or not data['historical']:
            st.error("No data available for the selected dates. Please choose another date range.")
            return None
        else:
            return [day['close'] for day in data['historical']]
    except Exception as e:
        st.error(f"Error fetching stock data: {str(e)}")
        return None

# Step 2: Create a basic Streamlit app layout
st.title("Value at Risk (VaR) Calculator")

# Step 3: Add input fields for stock name, start date, and end date
stock_name = st.text_input("Enter Stock Name:")
start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

# API key (Note: Store API keys securely)
API_KEY = '0uTB4phKEr4dHcB2zJMmVmKUcywpkxDQ'

# Step 5: Calculate basic statistics of the fetched stock data
def calculate_statistics(stock_data):
    returns = np.diff(stock_data) / stock_data[:-1]
    average_return = np.mean(returns)
    std_deviation = np.std(returns)
    return returns, average_return, std_deviation

# Step 6: Data Visualization - Line Plot
def plot_returns(returns):
    plt.figure(figsize=(10, 6))
    plt.plot(returns)
    plt.title("Stock Returns Over Time")
    plt.xlabel("Days")
    plt.ylabel("Returns")
    plt.grid(True)
    return plt

# Step 7: Add dropdown menu for selecting VaR method
var_methods = ["Historical", "Variance-Covariance", "Monte Carlo"]
selected_method = st.selectbox("Select VaR Method:", var_methods)

# Step 8: VaR Calculation for each method
def calculate_var(returns, confidence_level):
    if selected_method == "Historical":
        var = np.percentile(returns, 100 - confidence_level)
    elif selected_method == "Variance-Covariance":
        mean = np.mean(returns)
        sigma = np.sqrt(np.var(returns))
        norm_percentile = np.percentile(np.random.normal(mean, sigma, 10000), 100 - confidence_level)
        var = mean - norm_percentile
    elif selected_method == "Monte Carlo":
        simulations = 10000
        returns_simulations = np.random.choice(returns, (simulations, len(returns)), replace=True)
        sorted_returns = np.sort(returns_simulations, axis=0)
        var = np.mean(sorted_returns[int(simulations * (1 - confidence_level / 100)), :])
    return var

# Step 9: Display VaR based on selected method
if st.button("Calculate VaR"):
    stock_data = fetch_stock_data(stock_name, start_date.isoformat(), end_date.isoformat(), API_KEY)
    if stock_data:
        returns, average_return, std_deviation = calculate_statistics(stock_data)
        st.write("Basic Statistics:")
        st.write(f"Average Return: {average_return:.4f}")
        st.write(f"Standard Deviation: {std_deviation:.4f}")
        
        st.write("Data Visualization:")
        plt = plot_returns(returns)
        st.pyplot(plt)
        
        confidence_level = st.slider("Select Confidence Level:", 1, 99, 95)
        var = calculate_var(returns, confidence_level)
        st.write(f"Value at Risk (VaR) at {confidence_level}% confidence level using {selected_method} method: {var:.2f}")
    else:
        st.write("Failed to fetch stock data. Please check your inputs and try again.")
