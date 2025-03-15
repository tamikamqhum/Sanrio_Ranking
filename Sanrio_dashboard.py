# Import Libraries 
import streamlit as st
import pandas as pd
import plotly.express as px
import io # For download feature 

# Load the cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_SanrioRank.csv')
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    return df

df = load_data()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to",[
    "Overview of Rankings",
    "Character Performance",
    "Debut and Longevity Analysis",
    "Custom Insights"
])

# Overview  of Rankings 
if page == "Overview of Rankings":
    st.title("Sanrio Character Ranking Overview")

# Dropdown Filters 
year_filter = st.selectbox("Select Year", sorted(df['Year'].dt.year.unique()))
character_filters = st.selectbox("Filter by Character", sorted(df['Character Name'].unique()))

# Filter the Data for Selected Year
filtered_data = df[df['Year'].dt.year == year_filter]

# Check if filtered_data is not empty (ChatGPT troubleshoot help)
if filtered_data.empty:
    st.warning("No data available for the selected year")
else:
    # Create Bar Chart 
    bar_chart = px.bar(
        filtered_data, 
        x='Character Name',
        y='Rank',
        title=f'Ranking for {year_filter}'
    )
    st.plotly_chart(bar_chart)

# Top 10 table
top_10 = filtered_data.sort_values('Rank').head(10)
st.write("### Top 10 Characters Summary")
st.dataframe(top_10[['Character Name', 'Rank', 'Highest Rank', 'Lowest Rank', 'Total Times Ranked']])

# KPI Metrics 
st.write("### Summary Statistics")
total_unique_characters = df['Character Name'].nunique()
top_rank_characters = df[df['Rank'] == 1]['Character Name'].value_counts().idxmax()
col1, col2 = st.columns(2)
col1.metric(label="Total Unique Characters", value=total_unique_characters)
col2.metric(label="Most Frequent No.1 Character", value=top_rank_characters)

# Download Filtered Data
buffer = io.BytesIO()
filtered_data.to_csv(buffer, index=False)
st.download_button("Download Filtered Data", data=buffer.getvalue(), file_name='filtered_sanrio_data.csv', mime='text/csv')

# Character Peformance
