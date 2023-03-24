# Olympics Data Analysis 

I will be building an Olympics Data Analysis Web Application using Streamlit. For development, I will be using Python and Pandas. For plotting, I will be using Seaborn and Plotly libraries.
Link: https://u-rex13-olympic-data-analysis-main-nb95ph.streamlit.app/

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
## What is Data Analysis 

file under construction 🚧🚧🚧🏗............
