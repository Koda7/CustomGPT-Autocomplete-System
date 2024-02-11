# CustomGPT-Autocomplete-System

## Description
This project aims to build a simple autocomplete system. The service provides suggestions to users based on their input query, utilizing a lookup mechanism to suggest the most relevant queries based on their frequency of occurrence.

## Features
- Simple autocomplete functionality using FastAPI.
- Efficient lookup mechanism to suggest relevant queries.
- Input query validation and parameter handling.
- Preprocessing script to prepare data for the autocomplete service.

## Installation
1. Clone this repository to your local machine: 
```
git clone https://github.com/Koda7/CustomGPT-Autocomplete-System.git
```

2. Install the required dependencies:
```
pip3 install fastapi
pip3 install pandas
```

3. Run the preprocessing script to prepare the data:
```
python3 main.py
```

4. Start the FastAPI server:
```
python3 api.py
```

5. Access the autocomplete service by sending GET requests to the endpoint /query with the q parameter representing the query string:

Example: In the URL http://localhost:8000/query?query=how&count=1 -
- Base URL: http://localhost:8000
- Endpoint: /query
- Query parameters:
query=how: This parameter represents the input query string. It is set to "how".
count=1: This parameter specifies the number of autocomplete suggestions to return. It is set to 1.





