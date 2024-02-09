### 💻 Project 
#### Python application for barcode generation

This application was developed during Rocketseat's NLW Experts using Python and Flask and is a barcode generator using the Python Barcode module.
Application developed using Python 3.11.5 during the NLW event hosted by Rocketseat.

### 🚀 Technologies

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Flask](https://pypi.org/project/Flask/)
- [Barcode](https://pypi.org/project/python-barcode/)
Cerberus 1.3.5
Flask 3.0.2
Python-barcode 0.15.1
Pytest 8.0.0

Features:

- Validator and error handler using [Cerberus](https://docs.python-cerberus.org/)
- Unit tests using [pytest](https://docs.pytest.org/en/8.0.x/)

### 🎮 Run application

1. Clone the project
2. Install dependencies
    > `npm install`
3. Run the project
    > `npm run dev`



### How to use?
Create and enable virtualenv
Use the commands in the root of the cloned project.

Create virtual environment:

```pip install virtualenv```

Windows:
```py -m venv .venv```

Unix/macOS
```python3 -m venv .venv```
Enable/Activate virtual environment:
```.\.venv\Scripts\activate.bat```
Download libs (they are only downloaded in the virtual environment):

```pip install -r requirements.txt```
Run project:

```python run.py```
Run tests:

```pytest```
Using the application
Make a POST request at the url `http://localhost:3000/create_tag`

Body Json example:
```
{
     "product_code": "123"
}
```
