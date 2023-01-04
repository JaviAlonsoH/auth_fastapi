### This version has FastAPI and Django working on the same server. 

- API runs at `localhost:8000/api/`
- Django Admin Authentification part runs at `localhost:8000/app/login`

### Characteristics

- Created a kind of microservices architecture to handle routers and database operations. Calls to MongoDB (*a free created cluster for this project*) are async operations.

- Django Admin part works fine; you can either register a user and login with that user, then access a homepage where Django recognises the user. This part is handled with PostgreSQL, wich is configured in the *settings.py* file and so in the docker configuration so running Docker-Compose can have PostgreSQL running too.

- API tested only for a GET request using **FastAPI - Jinja2** templates for responses. So I added a template for the visualization of the data but it has no more functionality. 


## MongoDB insert

[Link to the MongoDB Insert files](https://github.com/JaviAlonsoH/auth_fastapi/tree/develop/mongodb_insert)

MongoDB insert is done by a Jupyter Notebook with python. 

1. First create connection with MongoDB
2. Import the .csv data and create a DataFrame with **Pandas** 
3. Data preview
4. Data cleaning (*only NaN's, not a full cleaning*)
5. Convert DataFrame to python dictionary and insert to MongoDB collection with an *insert_many* operation.

