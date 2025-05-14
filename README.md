# Olympics Data Analysis 

Olympics Data Analysis Web Application using Streamlit. For development, I will be using Python and Pandas. For plotting, I will be using Seaborn and Plotly libraries.  

Link: [[https://u-rex13-olympic-data-analysis-main-nb95ph.streamlit.app/](https://olympic-data-analysis-tool.streamlit.app/)
](https://u-rex13-olympic-data-analysis-main-nb95ph.streamlit.app/)
* * *

## Steps To Run This Project:
  1) Fisrt Downlod the zip folder of project and unzip the folder. Open Project file and youll find another zip folder inside name as olympic-history.zip, unzip the folder  
  
  2) Install Python and Visual Studio code using below given link
     - Python Desktop Application: "https://www.python.org/downloads/"  
     - Visual Studion Code IDE: "https://code.visualstudio.com/download"
     
  3) Open the project folder inside the visual studio code
  
  4) Install the below given libery in command prompt or visual studio code terminal
  
  ![image](https://user-images.githubusercontent.com/109918405/226778535-dbe41c3f-3e74-40a2-b34b-2880be567c95.png)
  
  Below are python libery command before run this project you make sure to run all command in terminal   
  
  ```
  pip install streamlit
  ```
  ```
  pip install pandas
  ```
  ```
  pip install plotly 
  ```
  ```
  python -m pip install -U matplotlib
  ```
  ```
  pip install seaborn
  ```
  ```
  pip install requests 
  ```
  
  4) Afte installing the project required python libery we return use termianl to run our project using simple command.
  ```
  streamlit run main.py
  ``` 
  (meaning of the line is "streamlit" is package name that we are used to create this web app and run meaning to "run" this project using streamlit and "app.py" is the python file that i create the frontend of this project if in any other situation it can different if you create by own using other name so it is differnet name python extension file)
  
  5) after you run this line the streamlit create a localhost in your machine and run this web application using browser

  - This is the localhost that streamlit is host our web application
  
  ![image](https://user-images.githubusercontent.com/109918405/226804180-e8defcaf-188d-4b8e-aa97-59edb4472262.png)
 
* * *
## Olympic Data Analysis Web Application Preview 
    Data Analysis is perfomed on four level
    - Overall Analysis
    - Country Analysis
    - Sports Analysis
    - Athlete Analysis
![image](https://user-images.githubusercontent.com/109918405/225989249-7c9bb74f-3f73-4613-9718-09f169e8ed96.png)
![image](https://user-images.githubusercontent.com/109918405/226085447-bb62bc96-cbf4-4526-a124-56c5fcfb6a09.png)
![image](https://user-images.githubusercontent.com/109918405/226085479-c9288d04-e6d3-4f8f-881a-96070198bbd2.png)
![image](https://user-images.githubusercontent.com/109918405/226085488-029948c4-c385-4724-b635-3863fa72eead.png)

* * *
### Medal Tally
- Overall

![image](https://user-images.githubusercontent.com/109918405/226774738-9f3e6037-82d4-41ca-bc94-0c87b738feac.png)  

![image](https://user-images.githubusercontent.com/109918405/226774888-6ce2e7a1-0295-4d76-8954-2c8567f82d88.png)

- Select Specific Years & specific Country // Eg: 2016-South Africa

![image](https://user-images.githubusercontent.com/109918405/226775044-a343aff9-2787-494d-a008-23479be1f82e.png)  

![image](https://user-images.githubusercontent.com/109918405/226775147-795924b7-c0a2-46ff-9b5b-094455e69dd2.png)

* * *

### Overall Analysis

![image](https://user-images.githubusercontent.com/109918405/226775395-4aba42b2-d846-415a-9794-4fc14730c611.png)  

![image](https://user-images.githubusercontent.com/109918405/226775421-02293d6d-f25f-448d-a1f2-0d6cb0eecc96.png)
![image](https://user-images.githubusercontent.com/109918405/226775452-8c65b57a-5814-42ed-ab36-07e9a899acdf.png)
![image](https://user-images.githubusercontent.com/109918405/226775472-dee59be5-3a16-4a2a-ad01-2d389c8768fb.png)
![image](https://user-images.githubusercontent.com/109918405/226775496-d58e942d-3759-418c-be3b-38dc81fb3fae.png)
![image](https://user-images.githubusercontent.com/109918405/226775532-8e3c90c3-5789-4c3f-bd71-78cc76d08f60.png)
  - Most Successful Atheletes: Option Overall or specifc specific sport(eg: Archery)  
  
![image](https://user-images.githubusercontent.com/109918405/226775746-0939992b-ef3b-4c75-9dcf-b117a7f35a87.png)
![image](https://user-images.githubusercontent.com/109918405/226775910-66508be0-8d18-4cd3-82d0-72facd44a030.png)

* * *

### Country Analysis 

![image](https://user-images.githubusercontent.com/109918405/226776362-d29fd628-9003-4719-bf5d-f5b81f147dcf.png)  

![image](https://user-images.githubusercontent.com/109918405/226776410-f33ee3d9-78da-4462-a21d-811ef88201de.png)
![image](https://user-images.githubusercontent.com/109918405/226776441-249f2139-1726-403d-b6db-0dcb3f87187c.png)
![image](https://user-images.githubusercontent.com/109918405/226776475-c4b252f6-161d-4b8c-95d4-5b11e83f5517.png)

* * *

### Athlete Analysis

![image](https://user-images.githubusercontent.com/109918405/226776930-7638239f-96ab-437e-a582-9ee0dd4ce315.png)  

![image](https://user-images.githubusercontent.com/109918405/226776769-e0cd085a-3905-4fd3-bf32-a82b282ae50d.png)
![image](https://user-images.githubusercontent.com/109918405/226776835-5f339e61-18da-4c43-887a-7c4d3fae307a.png)
![image](https://user-images.githubusercontent.com/109918405/226776890-99572798-400b-4320-8d77-48e68df8e426.png)

* * * 

## what is role of each file in this or what it contain
![image](https://user-images.githubusercontent.com/109918405/226804538-ad36e093-ddd1-49a7-be81-2c233e28f179.png)
 
- **"git ignore"** 
- **"main.py"** 
- **"helper.py"**
- **"preprocessor.py"**
- **"requirements.txt"**
- **"__pycache__"**  

![image](https://user-images.githubusercontent.com/109918405/226807122-3bded907-1cd0-490c-b13b-8a5c84503088.png)

- **"images"**  

![image](https://user-images.githubusercontent.com/109918405/226807205-2b6e693d-0208-448e-94f8-d68b40830c5a.png)

- **"Jupyter Notebook files"**  

![image](https://user-images.githubusercontent.com/109918405/226807329-41d9d389-647e-4ee8-9627-dee7857cea17.png)

- **"olympic-history"**  

![image](https://user-images.githubusercontent.com/109918405/226807375-47b955d4-0e65-409f-a402-93dc0f993ac9.png)



   - we have both dataset file but stil you want to explore other dataset you can checkout kaggle website and i gave you this dataset site also
      - Kaggle to find other dataset likes or other things also (https://www.kaggle.com/datasets)
      - TMDB 5000 Movie Dataset that we are using (https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

* * *
### Syopsis using gpt4

## What is Olympic Data Analysis 

This project involves the creation of a web application for analyzing Olympic data using Python. The application allows users to select various data points from Olympic Games, including countries, sports, events, and medal counts, and visualize them in a variety of ways, such as graphs, tables, and maps. The data is obtained from a publicly available Olympic database, and the application uses various Python libraries, such as Pandas, Matplotlib, and Folium, for data analysis and visualization. The project provides a user-friendly interface that allows users to interact with the data and gain insights into Olympic trends and statistics. Overall, this project demonstrates the potential of Python for creating data analysis applications that can be used for various purposes, including sports analysis, business intelligence, and scientific research.

## Architecture & Components

Architecture:
The Olympic data analysis web application project is built using the Python programming language and various Python libraries for data analysis, visualization, and web development. The project's architecture consists of three main components:

Data Preprocessing: The first component of the project is data preprocessing, which involves cleaning and preparing the Olympic dataset for analysis. The project uses the Pandas and Preprocessor libraries for this purpose, which enable data cleaning, transformation, and aggregation. The preprocessing step also involves removing any missing or duplicate data, normalizing the data, and creating new features or variables based on the original data.

Data Visualization: The second component of the project is data visualization, which involves creating interactive visualizations and plots that enable users to explore and analyze the data. The project uses the Matplotlib, Seaborn, and Plotly libraries for this purpose, which provide a range of visualization tools for creating line charts, bar charts, scatter plots, heatmaps, and more.

Web Application: The third component of the project is the web application, which provides a user-friendly interface for users to interact with the data and visualize it. The project uses the Streamlit library for web development, which enables the creation of interactive web applications using Python. The web application component consists of multiple pages that provide various features such as data filtering, sorting, searching, and visualization. The application is deployed on the Streamlit Cloud, a free hosting service for Streamlit applications.

Components:
The components of the Olympic data analysis web application project include:

Data Preprocessing:

Pandas Library
Preprocessor Library
Data Visualization:

Matplotlib Library
Seaborn Library
Plotly Library
Web Application:

Streamlit Library
HTML/CSS/JavaScript
Streamlit Cloud (for deployment)
The project's architecture and components work together to enable users to interactively explore and analyze the vast amount of data associated with the Olympic Games, providing them with a range of tools and insights that may not be immediately apparent from the raw data.


## What is Data visualization

Data visualization is an important aspect of the Olympic data analysis web application project, as it enables users to explore and understand patterns and trends in Olympic history in an intuitive and interactive way. The project uses several popular Python libraries for data visualization, including Matplotlib, Seaborn, and Plotly, each of which provides different tools for creating visualizations that can be embedded within the web application.

The project includes a wide range of visualizations that enable users to explore different aspects of Olympic history, including athlete performance, medal counts, and event participation across different countries and time periods. These visualizations include:

Line charts: These are used to show trends in athlete performance over time, such as the number of medals won by a particular country in different Olympic games.

Bar charts: These are used to compare data across different categories, such as the number of gold, silver, and bronze medals won by different countries.

Scatter plots: These are used to show the relationship between two variables, such as the number of athletes from a particular country and their performance in different events.

Heatmaps: These are used to show the distribution of data across different categories, such as the number of medals won by different countries across different events.

The visualizations in the project are highly interactive, enabling users to filter and explore the data in different ways. For example, users can filter the data by year, country, event, or athlete, or zoom in on specific parts of a chart to explore the data in more detail. The project also includes several advanced visualizations, such as choropleth maps and interactive networks, that enable users to explore the data in even more depth.

Overall, data visualization plays a crucial role in the Olympic data analysis web application project, enabling users to explore and understand patterns and trends in Olympic history in a highly interactive and engaging way.


## Types of data visualization

Line Charts: Line charts are used to show trends over time. In the Olympic data analysis web application project, line charts are used to show trends in athlete performance over time, such as the number of medals won by a particular country in different Olympic games. These charts are useful for identifying patterns and trends in data over time.
![image](https://user-images.githubusercontent.com/109918405/230543654-4a6d5d1d-2e53-4a8b-bd0e-ddb974f7c804.png)

Bar Charts: Bar charts are used to compare data across different categories. In the Olympic data analysis web application project, bar charts are used to compare the number of medals won by different countries or the number of medals won in different events. These charts are useful for comparing data across different categories.
![image](https://user-images.githubusercontent.com/109918405/230543746-50c6058e-c7b9-409b-a295-6ecd5cbed209.png)

Scatter Plots: Scatter plots are used to show the relationship between two variables. In the Olympic data analysis web application project, scatter plots are used to show the relationship between the number of athletes from a particular country and their performance in different events. These plots are useful for identifying correlations and relationships between two variables.
![image](https://user-images.githubusercontent.com/109918405/230543783-52aed48e-843f-47b4-a2bd-33d1d786b391.png)

Heatmaps: Heatmaps are used to show the distribution of data across different categories. In the Olympic data analysis web application project, heatmaps are used to show the number of medals won by different countries across different events. These charts are useful for identifying patterns in data across different categories.
![image](https://user-images.githubusercontent.com/109918405/230543819-6eff5027-4718-4f72-ba7f-851ef749a097.png)

Choropleth Maps: Choropleth maps are used to show data across geographical regions. In the Olympic data analysis web application project, choropleth maps are used to show the number of medals won by different countries across the world. These maps are useful for visualizing data across geographical regions.
![image](https://user-images.githubusercontent.com/109918405/230543867-77196de0-f7cf-477a-8524-c40e652173e4.png)

Interactive Networks: Interactive networks are used to show the relationships between different entities in a network. In the Olympic data analysis web application project, interactive networks are used to show the relationships between different countries based on the number of medals they have won. These networks are useful for visualizing complex relationships between different entities.
![image](https://user-images.githubusercontent.com/109918405/230543920-31b10d69-3d87-44eb-954b-96cfc54fd09e.png)
Overall, the Olympic data analysis web application project uses a wide range of data visualizations to enable users to explore and understand patterns and trends in Olympic history. Each type of visualization is used to highlight different aspects of the data and provide users with a comprehensive view of the data.


## how does this Data visualization work

In your Olympic data analysis web application project, data visualization is used to represent the large and complex Olympic dataset in a visually appealing and easily understandable way. The process of data visualization involves transforming data into charts, graphs, and other visual elements that can be easily interpreted by the user.

The data visualization in your project is done using various Python libraries such as Matplotlib, Seaborn, and Plotly. These libraries allow you to create various types of visualizations such as line charts, bar charts, scatter plots, heatmaps, and more.

The data visualization process starts by pre-processing the raw Olympic dataset using the Pandas library, which involves cleaning and transforming the data into a format that can be used for visualization. The pre-processed data is then passed to the data visualization libraries, which create the desired visualizations based on the data.

The data visualizations in your project are interactive, which means that the user can interact with the visualizations and change the displayed data based on their preferences. For example, the user can filter the data by Olympic year, sport, country, and other criteria to see the data in different ways.

Overall, data visualization is a crucial part of your Olympic data analysis web application project, as it helps users to understand and explore the Olympic dataset more easily and efficiently.


## how the code of flow work in text form Data Prepressing and Data Visualization 

Data Preprocessing:
The project reads in the 120 years of Olympic history dataset from Kaggle using the Pandas library.
The dataset is then cleaned and preprocessed using various Pandas methods, such as dropping null values, renaming columns, and aggregating data.
The preprocessed data is then stored in Pandas data frames for further analysis and visualization.
The Scikit-learn library is used for feature scaling, normalization, and machine learning models.
Data Visualization:
The preprocessed data frames are used to create various types of visualizations using Matplotlib, Seaborn, and Plotly libraries.
The Streamlit library is used to create an interactive web application for users to explore and interact with the visualizations.
The visualizations are organized into different sections, such as medal tally, overall analysis, country analysis, and athlete analysis, which can be accessed by the user through the web application interface.
Overall, the data preprocessing and data visualization aspects of your project are closely integrated, with the preprocessed data being used to generate various types of visualizations that are presented to the user through an interactive web application.

### Blogs to know about core concept of project 
  - https://www.ibm.com/in-en/topics/data-visualization#:~:text=Data%20visualization%20is%20the%20representation,that%20is%20easy%20to%20understand.
  - https://www.tableau.com/learn/articles/data-visualization
  - https://powerbi.microsoft.com/en-us/data-visualization/
  - https://www.javatpoint.com/what-is-data-visualization
  - https://visme.co/blog/best-data-visualizations/
  - https://www.techtarget.com/searchdatamanagement/definition/data-analytics#:~:text=Data%20analytics%20(DA)%20is%20the,of%20specialized%20systems%20and%20software.
  - https://www.investopedia.com/terms/d/data-analytics.asp
  - https://www.simplilearn.com/tutorials/data-analytics-tutorial/what-is-data-analytics
  - https://www.tibco.com/reference-center/what-is-data-analytics
  - https://en.wikipedia.org/wiki/Data_analysis#:~:text=Data%20analysis%2C%20is%20a%20process,test%20hypotheses%2C%20or%20disprove%20theories.
  
