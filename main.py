import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff


df = pd.read_csv('./olympic-history/athlete_events.csv')
region_df = pd.read_csv('./olympic-history/noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Data Analysis")
# st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
st.sidebar.image('./images/olympics 1.png')
user_menu = st.sidebar.radio(
    'Select An Option',
    ("Medal Tally", "Overall Analysis","Country Analysis","Athlete Analysis")
)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Years", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    else:
        st.title(f"{selected_country} in {selected_year} olympics!")
    st.table(medal_tally)

if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0]
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Events")
        st.title(events)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Sports")
        st.title(sports)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time,x ='Editions', y='region')
    st.title("Nations in Olympics over Time")
    st.plotly_chart(fig)

    
    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time,x ='Editions', y='Event')
    st.title("Events over Time")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x ='Editions', y='Name')
    st.title("Athletes over Time")
    st.plotly_chart(fig)

    st.title("Number of Events over Time")
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns="Year", values="Event", aggfunc="count").fillna(0).astype('int'), annot=True)
    st.pyplot(fig)


    st.title("Most Successful Atheletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")

    selected_sport = st.selectbox('Select a Sport', sport_list)

    x = helper.best_athletes(df, selected_sport)
    st.table(x)


if user_menu == 'Country Analysis':
    st.sidebar.title("Country Analysis")

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country  = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country )
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(f"{selected_country } Medals Over the Years")
    st.plotly_chart(fig)

    st.title(f"{selected_country } in various sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt, annot=True )
    st.pyplot(fig)

    st.title(f"Best athletes of {selected_country}")
    athlete_df = helper.country_athlete_analysis(df, selected_country)
    st.table(athlete_df)


if user_menu ==  'Athlete Analysis':
    athlete_df = df.drop_duplicates(subset=['Name','region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist','Silver Medalist', ' Bronze Medalist'], show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Athletes - Distribution by Age")

    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Sports - Distribution by Age for Gold Medalist")
    st.plotly_chart(fig)


    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

    