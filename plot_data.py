import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def plot_scatter():
    # Load the processed data
    df = pd.read_csv("processed_data.csv")
    
    # User input for plotting
    rows_to_plot = st.number_input("Number of rows to plot:", min_value=1, max_value=len(df), value=250)
    
    # User input for selecting columns
    col_a = st.selectbox("Select Column for X-axis", df.columns)
    col_b = st.selectbox("Select Column for Y-axis", df.columns)

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col_a][:rows_to_plot], df[col_b][:rows_to_plot])
    plt.xlabel(col_a)
    plt.ylabel(col_b)
    plt.title(f"Scatter Plot of {col_a} vs {col_b}")
    plt.grid()
    st.pyplot(plt)
