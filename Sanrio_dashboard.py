# Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import io  # For download feature
import numpy as np

# Load the cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_SanrioRank.csv')
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    return df

df = load_data()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Overview of Rankings",
        "Character Performance",
        "Debut and Longevity Analysis",
        "Custom Insights"
    ]
)

# Soft pastel color scheme
custom_colors = ["#FEC8D8", "#FFE5B4", "#B4D8FE", "#E0BBE4"]  # Pink, Yellow, Blue, Purple

# Overview of Rankings
if page == "Overview of Rankings":
    st.title("Sanrio Character Ranking Overview")

    # Dropdown Filters
    year_filter = st.selectbox("Select Year", sorted(df['Year'].dt.year.unique()))
    character_filter = st.selectbox("Filter by Character", sorted(df['Character Name'].unique()))

    # Filter the Data for Selected Year
    filtered_data = df[df['Year'].dt.year == year_filter]

    # Check if filtered_data is not empty
    if filtered_data.empty:
        st.warning("No data available for the selected year.")
    else:
        # Create Bar Chart
        bar_chart = px.bar(
            filtered_data,
            x='Character Name',
            y='Rank',
            title=f'Ranking for {year_filter}',
            labels={'Rank': 'Ranking', 'Character Name': 'Character'},
            color_discrete_sequence=custom_colors
        )
        st.plotly_chart(bar_chart)

        # Top 10 Table
        top_10 = filtered_data.sort_values('Rank').head(10)
        st.write("### Top 10 Characters Summary")
        st.dataframe(top_10[['Character Name', 'Rank', 'Highest Rank', 'Lowest Rank', 'Total Times Ranked']])

        # KPI Metrics
        st.write("### Summary Statistics")
        total_unique_characters = df['Character Name'].nunique()
        top_rank_character = df[df['Rank'] == 1]['Character Name'].value_counts().idxmax()

        col1, col2 = st.columns(2)
        col1.metric(label="Total Unique Characters", value=total_unique_characters)
        col2.metric(label="Most Frequent No.1 Character", value=top_rank_character)

        # Download Filtered Data
        buffer = io.BytesIO()
        filtered_data.to_csv(buffer, index=False)
        st.download_button(
            "Download Filtered Data",
            data=buffer.getvalue(),
            file_name='filtered_sanrio_data.csv',
            mime='text/csv'
        )

# Character Performance
elif page == "Character Performance":
    st.title("Character Trends Over Time")

    # Dropdown for Character Selection
    selected_character = st.selectbox("Select Character", sorted(df['Character Name'].unique()))

    # Line Chart
    character_data = df[df['Character Name'] == selected_character]
    line_chart = px.line(
        character_data,
        x='Year',
        y='Rank',
        title=f'{selected_character} Performance Over Time',
        color_discrete_sequence=custom_colors
    )
    st.plotly_chart(line_chart)

    # Heatmap
    heatmap_data = df.pivot_table(index='Character Name', columns='Year', values='Rank')
    heatmap_fig = px.imshow(
        heatmap_data,
        labels=dict(x="Year", y="Character Name", color="Rank"),
        title="Rank Heatmap by Year and Character",
        color_continuous_scale=['#FEC8D8', '#FFE5B4', '#B4D8FE', '#E0BBE4']  # Pastel gradient
    )
    st.plotly_chart(heatmap_fig)

    # KPI Metrics
    st.write(f"### {selected_character}'s Performance Overview")
    highest_rank = character_data['Highest Rank'].min()
    lowest_rank = character_data['Lowest Rank'].max()
    total_times_ranked = character_data['Total Times Ranked'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Rank Achieved", highest_rank)
    col2.metric("Lowest Rank Achieved", lowest_rank)
    col3.metric("Total Times Ranked", total_times_ranked)

# Debut and Longevity Analysis
elif page == "Debut and Longevity Analysis":
    st.title("Debut and Longevity Analysis")

    # Histogram of Debut Years
    debut_hist = px.histogram(
        df,
        x='Debut',
        nbins=20,
        title="Distribution of Characters by Debut Year",
        color_discrete_sequence=custom_colors
    )
    st.plotly_chart(debut_hist)

    # Bar Chart for Total Years Ranked
    total_years_ranked = df.groupby('Character Name')['Total Times Ranked'].sum().reset_index()
    ranked_years_chart = px.bar(
        total_years_ranked,
        x='Character Name',
        y='Total Times Ranked',
        title='Total Years Ranked by Character',
        color_discrete_sequence=custom_colors
    )
    st.plotly_chart(ranked_years_chart)

    # Scatter Plot for Debut Year vs. Total Times Ranked
    scatter_plot = px.scatter(
        df,
        x='Debut',
        y='Total Times Ranked',
        color='Highest Rank',
        title='Debut Year vs. Total Times Ranked',
        color_discrete_sequence=custom_colors
    )
    st.plotly_chart(scatter_plot)

# Custom Insights
elif page == "Custom Insights":
    st.title("Deep Dive: Insights and Comparisons")

    # Filters for Custom Insights
    selected_years = st.multiselect(
        "Select Years",
        sorted(df['Year'].dt.year.unique()),
        default=df['Year'].dt.year.unique()[:5]
    )
    selected_characters = st.multiselect(
        "Select Characters",
        sorted(df['Character Name'].unique()),
        default=df['Character Name'].head(5)
    )

    # Filter Data for Custom Insights
    filtered_insights = df[
        (df['Year'].dt.year.isin(selected_years)) &
        (df['Character Name'].isin(selected_characters))
    ]

    # Check for empty data
    if filtered_insights.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Generate Insight Chart
        insight_chart = px.line(
            filtered_insights,
            x='Year',
            y='Rank',
            color='Character Name',
            title='Comparison of Popularity Trends',
            color_discrete_sequence=custom_colors
        )
        st.plotly_chart(insight_chart)

    # KPI Indicators
    st.markdown("### Key Takeaways")
    consistent_top_rankers = df[df['Rank'] <= 3]['Character Name'].value_counts().head(3)
    st.write("Characters with consistently high rankings:")
    st.write(consistent_top_rankers)

    # Download Insights Data
    buffer = io.BytesIO()
    filtered_insights.to_csv(buffer, index=False)
    st.download_button(
        "Download Insights Data",
        data=buffer.getvalue(),
        file_name='custom_insights.csv',
        mime='text/csv'
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Sanrio Character Dashboard - Designed with ❤️ using Streamlit")
