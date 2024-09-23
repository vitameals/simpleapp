import streamlit as st
from read_data import load_and_process_data
from plot_data import plot_scatter

# Main page title
st.title("Simple Streamlit App")

# Option to load and process data
if st.button("Load and Process Data"):
    df = load_and_process_data()
    if df is not None:
        st.write("DataFrame Head:")
        st.write(df.head())
        st.write("Shape of DataFrame:", df.shape)
        st.write("Column Names:", df.columns.tolist())
        
        # Save DataFrame as CSV
        df.to_csv("processed_data.csv", index=False)
        st.success("Data saved as processed_data.csv")

# Option to plot data
if st.button("Plot Data"):
    plot_scatter()
