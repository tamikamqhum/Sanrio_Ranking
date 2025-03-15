
# The Sanrio Index 

**The Sanrio Index** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

# ![Sanrio Characters](https://shoplineimg.com/5cc813ba527c4b0001a31e32/674e6a94d11b16000ae62529/1080x.webp?source_format=jpg)



## Dataset Content
The dataset **SanrioRank** comprises information about the rankings of various Sanrio characters over the years. This dataset consists of 410 rows and 10 columns. Each row in the dataset represents a character's ranking in a specific year, and the columns provide additional context about the character's performance and background.

The dataset includes the following columns:

1. **Year:** The year when the ranking was recorded.

2. **Rank:** The character's rank for that particular year.

3. **Character Name:** The name of the character.

4. **Unique Characters:** A unique identifier for characters, accounting for name variations.

5. **Debut:** The year the character made its first appearance.

6. **First Year Ranked:** The first year the character appeared in the top 10 rankings.

7. **Latest Year Ranked:** The most recent year the character was ranked in the top 10.

8. **Total Times Ranked:** The total number of times the character has been in the top 10 rankings.

9. **Highest Rank:** The best rank the character has achieved.

10. **Lowest Rank:** The lowest rank the character has achieved.

This dataset is valuable for analyzing trends, popularity shifts, and historical performance of Sanrio characters over nearly four decades. It can be used for data visualization, trend analysis, and generating insights into the factors that influence a character's popularity.


## Business Requirements
Understanding character popularity is essential for Sanrio's marketing, merchandising and brand strategy. The analysis aims to: 
1. Identify long-term trends in character popularity 
2. Discover Patterns that correlate with external factors (e.g.media, apppearances and collaborations)
3. Provide insights into how character rankings flactuate over time 


## Hypothesis and Validation 

**Hypotheses:**
* Hello Kitty remains the most popular character overall but may flactuate in ranking
* Media Exposure (e.g. anime, merchandise and collaboration) influences ranking positions 
* New characters introduced in recent years see a temporary spike in popularity but struggle to maintain top positions

**Validation:**
* Time-Series analysis of ranking trends 
* Correlation analysis between media appearances and ranking flactuations 
* Comparisions of older vs. newer characters rank longevity

## Project Plan & Roadmap
1. **Data Collection & Cleaning** 
    - Handling missing values and inconsisitencies 
    - Standardising character names and ranking positions 
2. **Exploratory Data Analysis**
    - Visualising trends in character rankings 
    - Identifying ranking stability and volatility 
3. **Hypothesis Testing** 
    - Correlation Analysis between ranking shifts and external factors
    - Analysing the longevity of character popularity 
4. **Data Visualisation & Insights** 
    - Creating interactive dashboard 
    - Communicating findings for both technical and non-technical audiences 
5. **Machine Learning(Optional)**
    - Trends predictions based on historical data
    - Clustering analysis to group characters based on voting patterns 
6. **Dashboard Development in Streamlit**
    - Interactive UI for data exploration
    - Filters to selectt specific years of characters 
    - AI-generated insights summarising key findings 
7. **Final Documentation & Deployment**
    - Hosting on Streamlit 


## Business Requirements & Data Visualisations Mapping 
| **Business Requirement**              | **Data Visualization**                       |
|---------------------------------------|------------------------------------------------|
| Identify long-term ranking trends      | Line charts & heatmaps                        |
| Determine ranking stability            | Box plots & standard deviation analysis        |
| Analyse new vs. established characters | Bar charts & trend comparisons                |
| Impact of media exposure                | Overlay media release dates on ranking graphs |


## Analysis Techniques Used
* **Time-Series Analysis:** Tracking ranking over time 
* **Statistical Correlation:** Exploring relationships between ranking and external influences 
* **Data Clustering:** Grouping charcters based on ranking similarity 

## Limitations & Alternative Approaches 
* The dataset lacks direct indicators of external factors (anime releases). ***Alternative approach:*** Cross referencing external datasets. 
* Data may not account for regional populairty differences
* Generative AI tools were used to assist with exploratory visualisations and data 

## Ethical considerations
* **Bias Awareness:** The ranking reflect Sanrio's official rsults, but survey biases may exist 
* **Data Privacy:** No personal data is involved, making it ethical for public analysis 
* **Fair Representation:** Analysis ensures no undue preferences is given to specific characters 

## Dashboard Design
**Overview**
- This dashboard is designed to provide insights into Sanrio Character Rankings for both technical and non-technical audiences. It combines interactive filters, visual storytelling and key performance indicators to maximise user engagement and understanding. 

---
**Page 1: Overview of Ranking**
- **Title:** *Sanrio Character Ranking Overview*
- **Widgets:**
    - **Dropdown Filter:** Select a year 
    - **Dropdown Filter:** Filter by character 
    - **Dynamic Bar Chart:** Ranks for the selected year 
    - **Summary Table:** Displays:
        - Character Name 
        - Rank 
        - Highest/lowest rank achieved 
        - Number of times ranked 
    - **KPI Banner:** Key Metrics at the top, including: 
        - Total unique characters 
        - Most Frequent No.1 Character 
        - Average rank improvement over time 
    - **Navigation buttons:** Links to character performance, debut analysis and insight pages. 

**Design Considerations**
- The KPI banner provides immediate insight for non techical analysis 
- Clear Visual separation between key metrics and detailed data ensures readability. 

---
**Page 2: Character Performance**
- **Title:** *Character Trends Over Time*
- **Widget:**
    - **Line Chart:** Tracks Year vs Rank for Individual characters
    - **Dropdown Menu:** Select characters to view their trends 
    - **Heatmap:** Year vs Rank with colour intensity indicating position 
    - **Annotation Feature:** Highlights key insights like major jumps or drops
    - **Character Image Display:** Adds visual context for selected characters 
    - **Navigation buttons:** "Back to Overview" and "Next Page"

**Design Considerations**
- Annotations guide non-technical users by pointing out key insights 
- Including character images improves engagement and storytelling

---
**Page 3: Debut and Longevity Analysis**
- **Title:** *Debut and Popularity Longevity*
- **Widgets:**
    - **Histogram:** Distribution of charcaters by debut year 
    - **Bar Chart:** Total years ranked vs unique characters 
    - **Tooltip-enabled scatter plot:** Debut years vs total time ranked, color coded by highest ranked acheived 
    - **Color coded clusters:** Distinguish long time top performers from rising stars 
    Timeline feature: Tracks key character milestone 

**Design Considerations**
- Colour Coded clusters simplify complex insight for non technical viewers 
- The timeline features adds storytelling to connect data patterns with real word events 

---
**Page 4: Custom Insights**
- **Title:** *Deep Dive: Insights and Comparisons*
- **Widgets:**
    - **Checkout filters:** Select years or characters to compare
    - **Side-by-side plots:** Compare popularity trends across characters or time periods. 
    - **KPI indicators**  Display key takeaways like:
        - Characters with consistent top ranking 
        - Significant drops or improvement 
    - **"Story Mode" Feature:** A guided walkthrough to narrate key insights for less experienced users 
    - **Export Feature:** Allow users to download filtered insights as csv or pdf 

**Design Considerations**
- The "Story Mode" ensures that non-technical audience grasp important insights effectively 
- Export options prrovide flexibility for technical users conducting further analysis

---
**Community Insights Effectively**
- **Visual Hierarchy:** KPIs and key insights are priotised for immediate impact 
- **Color Theory:** Warm color (red, orange) highlight top ranking, while cool tones(blue, purple) represent lower ranks 
- **Interactive Elements:** Filters, tooltips and annotations guide both technical and non technical audiences 
- **Data Dictionary Tab:** Provides clear definitionss for metrics such as percentile, rank shifts and debuts year. 


## Challenges & Solutions 
* **Handling Missing Data:** Used interpolation techniques 
* **Ensuring Accuracy in Trend Analysis:** Cross-checked with multiple sources 
* **Optimizing Dashboard Performance:** Reduced data load times with caching 

## Future Improvements 
1. Integrate sentiment analysis using social media data 
2. Expand dataset with external sources 
3. Enhance AI-generated insights 
4. Project deployment on cloud platform 

## Technologies Used 
| **Technology**           | **Tools/Frameworks**               |
|---------------------------|------------------------------------|
| Programming Language       | Python                             |
| Data Analysis               | Pandas, NumPy                      |
| Data Visualization          | Matplotlib, Seaborn, Plotly        |
| Machine Learning (if applicable) | Scikit-learn                    |
| Web Application             | Streamlit                          |
| Notebook Environment        | Jupyter Notebook                   |

## Main Data Analysis Libraries 
| **Library**          | **Purpose**                            |
|----------------------|----------------------------------------|
| pandas                | Data cleaning & manipulation            |
| matplotlib/seaborn    | Visualization                           |
| scikit-learn          | Clustering & trend analysis             |
| plotly/dash           | Interactive dashboards                  |


## Credits 
**Dataset**
 - This dataset is from Kaggle [SanrioRank](https://www.kaggle.com/datasets/alyahh/sanrio-character-rankings-top-10-19862024) 

**Content:**
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)

**Media**
- The image used were taken from (https://www.sanriogiftgate.com.hk/en/categories/sanrio-mix-characters)
- Dashboard planning 

## Conclusion
This project successfully demonstrates data analytics, visualisations and AI-driven insights to analyse Sanrio Characters Ranking. The interactive dashboards enables both technical and non-technical audiences to explore data-driven findings efficiently.  