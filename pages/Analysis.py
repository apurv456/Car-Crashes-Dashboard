import streamlit as st
import seaborn as sns
import plotly.express as px

df = sns.load_dataset("car_crashes")

st.title("Explore the Insights Here👇")

st.sidebar.header("Filter Options")

#states filter
states = st.sidebar.multiselect(
    "Select States",
    options=df["abbrev"].unique(),
    default=df["abbrev"].unique()
)


#accident filter
accident_range = st.sidebar.slider(
    "Select Range of Total Accidents",
    int(df["total"].min()),
    int(df["total"].max()),
    (int(df["total"].min()), int(df["total"].max()))
)

#Applying filter
filtered_df = df[
    (df["abbrev"].isin(states)) &
    (df["total"] >= accident_range[0]) &
    (df["total"] <= accident_range[1])
]

#show dataset
st.header("Dataset")
st.dataframe(filtered_df)


#Total Car Crashes by State
st.header("Total Car Crashes by State")
fig = px.bar(filtered_df, x="abbrev", y="total", color_discrete_sequence=["darkturquoise"],
    labels={"abbrev": "State", "total": "Total Crashes"})
st.plotly_chart(fig)
st.subheader("Conclusion")
st.info("""This bar chart shows significant variation in total car crashes across states. 
        Some states record noticeably higher crash counts, 
        indicating a greater need for targeted road safety measures and stricter traffic enforcement.""")


#top10 states by insurance premium
st.header("Top 10 States by Insurance Premium")
top10 = df.sort_values('ins_premium', ascending=False).head(10)
fig = px.bar(top10, x='abbrev', y ='ins_premium', color_discrete_sequence=["darkturquoise"],
             labels = {'abbrev':'State','ins_premium':'Insurance Premium'})
st.plotly_chart(fig)
st.subheader("Conclusion")
st.info("""The chart highlights the top 10 states with the highest insurance premiums. 
        Higher premiums may reflect increased accident risk, higher claim frequencies, 
        or greater repair and healthcare costs in these states.""")


#percentage of speeding accidents
st.header("Percentage of Speeding Accidents")
fig = px.pie(filtered_df, values='speeding', names='abbrev',
             color_discrete_sequence=px.colors.sequential.Darkmint)
fig.update_traces(textposition='inside')
st.plotly_chart(fig)
st.subheader("Conclusion")
st.info("""The pie chart illustrates the proportion of speeding-related accidents across states. 
        It reveals that speeding is a major contributing factor to accidents in several states,
         emphasizing the importance of speed regulation and awareness campaigns.""")


#Speeding VS Alcohol Accidents
st.header("Speeding VS Alcohol Accidents")
fig = px.scatter(filtered_df, x='speeding',
                 y='alcohol',
                 color='abbrev',
                 size='total',
                 color_discrete_sequence=px.colors.sequential.Darkmint,
                 labels={'speeding':'Speeding Accidents', 'alcohol':'Alcohol'})
st.plotly_chart(fig)
st.subheader("Conclusion")
st.info("""The scatter plot shows a positive relationship between speeding and alcohol-related accidents.
         States with higher speeding incidents also tend to report more alcohol-related crashes, 
        suggesting overlapping risk behaviors.""")


#Distribution of Total Car Crashes
st.header("Distribution of Total Car Crashes")
fig = px.histogram(
    filtered_df, x="total",
    color_discrete_sequence=["darkturquoise"],
    labels={"total": "Total Crashes"}
)
st.plotly_chart(fig)
st.subheader("Conclusion")
st.info("""The histogram shows that most states fall within a moderate range of total crashes, 
        while a few states experience exceptionally high crash counts. 
        This indicates uneven accident distribution across the country.""")


st.markdown("""
<hr>
<p style="text-align:center">
Car Crash Dataset Analysis - Done by Apurv
</p>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stApp {
        background-color: LightSeaGreen;
    }
    [data-testid="stSidebar"] {
        background-color: teal;
    }
    </style>
    """,
    unsafe_allow_html=True
)