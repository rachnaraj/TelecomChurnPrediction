# Customer Retention - A big shout-out to Satyajit Pattnaik

## 🔴 Detailed Session on EDA:

[Tutorial](https://www.youtube.com/watch?v=baL7OrGWlxs)


## 🔴 What is Customer Churning ?

![Customer Retention](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco1.JPG)

## 🔴 What are the different Churn Scenarios ?

![Churn Scenarios](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco2.JPG)

## 🔴 Decision Cycle of a Subscriber ?

![Decision Cycle](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco3.JPG)

## 🔴 What are the different Churn Segments ?

![Churn Segments](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco4.JPG)

## 🔴 Solution Overview

![Solution](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco5.JPG)


In this repository, we have performed the end to end Exploratory Data Analysis, and idenfitied the characteristics of the customers that are more likely to churn,

### 🟢 For EDA, please refer to : Churn Analysis - EDA.ipynb
### 🟢 For Model Building, please refer to: Churn Analysis - Model Building.ipynb
### 🟢 For Model Deployment, please refer to app.py


### 🔵 Creating the flask API

```
app = Flask("__name__")
```

The loadPage method calls our home.html.
```
@app.route("/")
def loadPage():
	return render_template('home.html', query="")
```

The predict method is our POST method, which is basically called when we pass all the inputs from our front end and click SUBMIT.
```
@app.route("/", methods=['POST'])
def predict():
```
  
The run() method of Flask class runs the application on the local development server.
```
app.run()
```

Deployment using Flask:
	- Flask is a micro web framework written in Python.

	- Flask url binding: build url to specify functions dynamically.
	- [http methods]
		> Post- sent something to server and expecting something
		> get - sending in unencrypted form

To run the program, Go to Anaconda Prompt:
	set FLASK_DEBUG=1 -- if off, then changes won't be reflected if done while the program was running
	python app.py

Below message in Python shell is seen, which indicates that our App is now hosted at http://127.0.0.1:5000/ or localhost:5000
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


HERE'S HOW OUR FRONTEND LOOKS LIKE:

![Customer Retention](https://raw.githubusercontent.com/anirbansarkar823/Telecom_Churn_Predection/TelecomChurnPrediction_Flusk_Deployment/images/Telco6.JPG)





