# toucan_analytics
To analyze the customer data and create a table for frequent mode of transaction by individual customer, a bar graph for the amount spent on each mode of transaction for all the customers, a bar graph for the number of customers who paid EMI on time and the customers who haven't paid and a pie chart by grouping based on the various expenses by all the customers.

## Getting Started

### Dependencies
* python
* pip
* venv
* django
* ubuntu
* streamlit
* matplotlib
* pandas

## Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/Pythontp/toucan_analytics.git
$ cd toucan_analytics
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ python3 -m venv env_name
$ source env_name/bin/activate
```
Then install the dependencies:
```sh
(env)$ pip install python
(env)$ pip install django
(env)$ pip install streamlit
(env)$ pip install matplotlib
(env)$ pip install pandas
```

Note: The (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

To run the django app:
```sh
$ python manage.py runserver
```
A webpage will be opened displaying the table, graphs and pie chart.
