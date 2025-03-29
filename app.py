import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('demand_data.csv')
food_forecast = pd.read_csv('food_forecast.csv')
ride_forecast = pd.read_csv('ride_forecast.csv')

# Title
st.title("🚀 Demand Forecasting for Food Delivery & Ride-Hailing")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Food Orders Forecast
st.subheader("📊 Food Order Demand Forecast")
fig1 = px.line(food_forecast, x='ds', y='yhat', title="Forecasted Food Orders")
st.plotly_chart(fig1)

# Ride Requests Forecast
st.subheader("🚕 Ride Request Demand Forecast")
fig2 = px.line(ride_forecast, x='ds', y='yhat', title="Forecasted Ride Requests")
st.plotly_chart(fig2)

# Recommendations
st.subheader("📌 Recommendations")
st.write("""
- Allocate more delivery partners in high-demand hours.
- Increase surge pricing in peak demand times.
- Consider weather and events for dynamic scheduling.
""")

st.success("✅ Forecasting and visualization complete!")
