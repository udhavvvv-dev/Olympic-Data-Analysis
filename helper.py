import numpy as np 

# Medal tally
        
def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
       ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x

# Overall analysis

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years,country


def data_over_time(df, col):
    nations_over_time = df.drop_duplicates(["Year",col])['Year'].value_counts().reset_index().sort_values('index')
    nations_over_time = nations_over_time.rename(columns={'index':'Editions','Year': col})
    return nations_over_time


def medal_tally(df):
    medal_tally_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally_df = medal_tally_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()

    medal_tally_df['Total']= medal_tally_df['Gold'] + medal_tally_df['Silver'] + medal_tally_df['Bronze']

    medal_tally_df['Gold'] = medal_tally_df['Gold'].astype('int')
    medal_tally_df['Silver'] = medal_tally_df['Silver'].astype('int')
    medal_tally_df['Bronze'] = medal_tally_df['Bronze'].astype('int')
    medal_tally_df['Total'] = medal_tally_df['Total'].astype('int')


    return medal_tally_df



def best_athletes(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != "Overall":
        temp_df = temp_df[temp_df['Sport']== sport]

    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on="index", right_on="Name", how='left')[['index','Name_x','Sport','region']].drop_duplicates("index")
    x.rename(columns={'index':'Name', 'Name_x':'Medals'}, inplace=True)

    return x


# Country Analysis

def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC','Games','Year', 'City','Sport', 'Event','Medal'], inplace=True)

    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return final_df

def country_event_heatmap(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC','Games','Year', 'City','Sport', 'Event','Medal'], inplace=True)

    new_df = temp_df[temp_df['region'] ==  country]
    pt_df = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt_df

def country_athlete_analysis(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == country]

    a = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='index', right_on='Name', how='left')[['index','Name_x','Sport']].drop_duplicates('index')
    a.rename(columns={'index':'Name','Name_x':'Medals'}, inplace=True)
    return a 


#  Athlete analysis

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final

