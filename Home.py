import streamlit as st

st.markdown("<h2 style= 'color:black; text-align:center'>Car Crashes Data Analysis Dashboard</h2>",unsafe_allow_html=True)

st.image("car_crash_img.jpg",use_container_width=True)

st.markdown("<p style= 'text-align:center'>This dataset contains information about motor vehicle accidents in different U.S. states. It focuses on factors related to speeding, alcohol involvement, and seatbelt usage, along with insurance losses.</p>", unsafe_allow_html=True)

st.subheader("Dataset Overview")
st.markdown("""
<table>
    <tr>
        <th>Column</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><b>total</b></td>
        <td>Total number of car crash deaths per 100,000 people</td>
    </tr>
    <tr>
        <td><b>speeding</b></td>
        <td>Percentage of crashes involving speeding</td>
    </tr>
    <tr>
        <td><b>alcohol</b></td>
        <td>Percentage of crashes involving alcohol</td>
    </tr>
    <tr>
        <td><b>not_distracted</b></td>
        <td>Percentage of crashes not involving distraction</td>
    </tr>
    <tr>
        <td><b>no_previous</b></td>
        <td>Percentage of drivers with no previous accidents</td>
    </tr>
    <tr>
        <td><b>ins_premium</b></td>
        <td>Average annual insurance premium (USD)</td>
    </tr>
    <tr>
        <td><b>ins_losses</b></td>
        <td>Insurance losses per insured driver (USD)</td>
    </tr>
    <tr>
        <td><b>abbrev</b></td>
        <td>State abbreviation (e.g., CA, TX, NY)</td>
    </tr>
</table>
""", unsafe_allow_html=True)


st.subheader("Key Objectives")
st.markdown("""- Identify states with higher accident rates
- Analyze the impact of alcohol and speeding on crashes
- Study the relationship between insurance premiums and losses
- Practice Exploratory Data Analysis (EDA) and data visualization
- Build interactive dashboards using Plotly""")


st.subheader("Common Visualizations")
st.markdown("""- Bar plots showing total crashes by state  
- Bar plots of the top 10 states by insurance premiums  
- Scatter plots showing the relationship between speeding and alcohol accidents  
- Pie charts showing the percentage of speeding accidents  
- Histogram showing the distribution of total car crashes""")


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
