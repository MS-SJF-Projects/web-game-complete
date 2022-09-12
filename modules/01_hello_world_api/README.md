# Hello world python web API

## Goal

In the first stage we're going to create a python web API with [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) that will return "Hello world" on the "/" page.

## Tutorial

1. Add and install `Flask` python package.

    >To be able to build the API, we first need to get the package of API we'll be using.

    1. Create a `requirements.txt` file in the root of the project folder

        ```sh
        touch requirements.txt
        ```

    2. Add the following content to `requirements.txt`:

        ```txt
        flask
        ```

    3. Install the package

        ```sh
        pip install -r requirements.txt
        ```

2. Create the API

    1. Create an `api.py` in the `src/` folder file with the contents of

        ```sh
        mkdir src
        cd src/
        touch api.py
        ```

        ```python
        from flask import Flask
        
        app = Flask(__name__)


        @app.route('/') # Defines the route the page will be served on
        def home():
            return "hello world"
        ```

3. In the root of the project (one level above `src`) create `app.py`

    ```py
    from src.api import app 

    if __name__ == '__main__':
        app.run(debug=True)
    ```

4. Run the API from the project root folder

    ```sh
    FLASK_DEBUG=1 flask run
    ```

5. Navigate to the url that the API is running at from the output of the previous command. The link will most likely be: <http://localhost:5000/>

### [Return to Main Index](../../README.md)
