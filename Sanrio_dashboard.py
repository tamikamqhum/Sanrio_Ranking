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
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Introduction",
        "Overview of Rankings",
        "Character Performance",
        "Debut and Longevity Analysis",
        "Custom Insights"
    ]
)

# Neon color scheme for black background
neon_colors = ["#FF1493", "#00FFFF", "#32CD32", "#FFFF00"]  # Pink, Cyan, Neon Green, Neon Yellow

# Introduction Page 
if page == "Introduction":
    st.title("🌟 Welcome to the Sanrio Character Dashboard!")
    st.write("""
    This interactive dashboard showcases Sanrio character ranking trends, insights, and performance over the years.
    
    ### How to Use
    - **Overview of Rankings:** Explore character rankings by year.
    - **Character Performance:** See detailed trends for individual characters.
    - **Debut & Longevity Analysis:** Discover how debut years influence rankings.
    - **Custom Insights:** Create custom comparisons across selected characters and years.

    ### About the Data
    The dataset includes:
    - **Rank:** The character's rank for a given year.
    - **Highest Rank:** Best rank achieved.
    - **Lowest Rank:** Worst rank achieved.
    - **Total Times Ranked:** How often the character has appeared in rankings.

    💡 *Fun Fact:* Hello Kitty has consistently remained a fan-favorite since her debut in 1974!
    """)

    # Only display the image on the Introduction page
    st.image(
        "https://admin.sportshackster.com//BlogFiles/Untitled_design_63858880819066.jpg", 
        caption="Sanrio Characters", 
        use_container_width=True
    )


# Overview of Rankings
if page == "Overview of Rankings":
    st.title("📊 Sanrio Character Ranking Overview")

    # 🎯 Year Filter
    year_filter = st.selectbox("🎯 Select Year", sorted(df['Year'].dt.year.unique()))

    # 🎯 Character Filter
    character_filter = st.selectbox("🎯 Filter by Character", sorted(df['Character Name'].unique()))

    # Filter the Data for Selected Year
    filtered_data = df[df['Year'].dt.year == year_filter]

    # Check if filtered_data is not empty
    if filtered_data.empty:
        st.warning("No data available for the selected year.")
    else:
        # 📊 Bar Chart
        bar_chart = px.bar(
            filtered_data,
            x='Character Name',
            y='Rank',
            title=f'📊 Ranking for {year_filter}',
            labels={'Rank': 'Ranking', 'Character Name': 'Character'},
            color_discrete_sequence=neon_colors
        )
        st.plotly_chart(bar_chart)

        # 🔝 Top 10 Characters Table
        top_10 = filtered_data.sort_values('Rank').head(10)
        st.write("### 🔝 Top 10 Characters Summary")
        st.dataframe(top_10[['Character Name', 'Rank', 'Highest Rank', 'Lowest Rank', 'Total Times Ranked']])

        # 📈 KPI Metrics
        st.write("### 📈 Summary Statistics")
        total_unique_characters = df['Character Name'].nunique()
        top_rank_character = df[df['Rank'] == 1]['Character Name'].value_counts().idxmax()

        col1, col2 = st.columns(2)
        col1.metric(label="Total Unique Characters", value=total_unique_characters)
        col2.metric(label="Most Frequent No.1 Character", value=top_rank_character)

        # 📥 Download Filtered Data
        buffer = io.BytesIO()
        filtered_data.to_csv(buffer, index=False)
        st.download_button(
            "📥 Download Filtered Data",
            data=buffer.getvalue(),
            file_name='filtered_sanrio_data.csv',
            mime='text/csv'
        )

# Character Performance
elif page == "Character Performance":
    st.title("📈 Character Trends Over Time")

    # 🎯 Character Selection Filter
    selected_character = st.selectbox("🎯 Select Character", sorted(df['Character Name'].unique()))

    # 📈 Line Chart
    character_data = df[df['Character Name'] == selected_character]
    line_chart = px.line(
        character_data,
        x='Year',
        y='Rank',
        title=f'📈 {selected_character} Performance Over Time',
        color_discrete_sequence=neon_colors
    )
    st.plotly_chart(line_chart)

    # 🔥 Heatmap
    heatmap_data = df.pivot_table(index='Character Name', columns='Year', values='Rank')
    heatmap_fig = px.imshow(
        heatmap_data,
        labels=dict(x="Year", y="Character Name", color="Rank"),
        title="🔥 Rank Heatmap by Year and Character",
        color_continuous_scale=['#FF1493', '#00FFFF', '#32CD32', '#FFFF00']  # Neon gradient
    )
    st.plotly_chart(heatmap_fig)

    # 📊 KPI Metrics
    st.write(f"### 📊 {selected_character}'s Performance Overview")
    highest_rank = character_data['Highest Rank'].min()
    lowest_rank = character_data['Lowest Rank'].max()
    total_times_ranked = character_data['Total Times Ranked'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Rank Achieved", highest_rank)
    col2.metric("Lowest Rank Achieved", lowest_rank)
    col3.metric("Total Times Ranked", total_times_ranked)

# Debut and Longevity Analysis
elif page == "Debut and Longevity Analysis":
    st.title("🔍 Debut and Longevity Analysis")

    # 📊 Histogram
    debut_hist = px.histogram(
        df,
        x='Debut',
        nbins=20,
        title="📊 Distribution of Characters by Debut Year",
        color_discrete_sequence=neon_colors
    )
    st.plotly_chart(debut_hist)

    # 📊 Bar Chart for Total Years Ranked
    total_years_ranked = df.groupby('Character Name')['Total Times Ranked'].sum().reset_index()
    ranked_years_chart = px.bar(
        total_years_ranked,
        x='Character Name',
        y='Total Times Ranked',
        title='📊 Total Years Ranked by Character',
        color_discrete_sequence=neon_colors
    )
    st.plotly_chart(ranked_years_chart)

    # 🔍 Scatter Plot
    scatter_plot = px.scatter(
        df,
        x='Debut',
        y='Total Times Ranked',
        color='Highest Rank',
        title='🔍 Debut Year vs. Total Times Ranked',
        color_discrete_sequence=neon_colors
    )
    st.plotly_chart(scatter_plot)

# Custom Insights
elif page == "Custom Insights":
    st.title("🏅 Deep Dive: Insights and Comparisons")

    # 🎯 Year Filter
    selected_years = st.multiselect(
        "🎯 Select Years",
        sorted(df['Year'].dt.year.unique()),
        default=df['Year'].dt.year.unique()[:5]
    )

    # 🎯 Character Filter
    selected_characters = st.multiselect(
        "🎯 Select Characters",
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
        # 📈 Line Chart
        insight_chart = px.line(
            filtered_insights,
            x='Year',
            y='Rank',
            color='Character Name',
            title='📈 Comparison of Popularity Trends',
            color_discrete_sequence=neon_colors
        )
        st.plotly_chart(insight_chart)

    # 🏅 Key Takeaways
    st.markdown("### 🏅 Key Takeaways")
    consistent_top_rankers = df[df['Rank'] <= 3]['Character Name'].value_counts().head(3)
    st.write("Top 3 Characters with Consistently High Rankings:")
    st.write(consistent_top_rankers)

    # 📥 Download Insights Data
    buffer = io.BytesIO()
    filtered_insights.to_csv(buffer, index=False)
    st.download_button(
        "📥 Download Insights Data",
        data=buffer.getvalue(),
        file_name='custom_insights.csv',
        mime='text/csv'
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Sanrio Character Dashboard - Designed with ❤️ using Streamlit")
