###############################################################################
## Sprint 02 - Web Application
## Feature 1: Web App Conversion
## User Story 1: Make a Web Application from the basic application code
###############################################################################
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))   # Get the directory of the this file
todo_file = os.path.join(basedir, 'todo_list.txt')     # Create the path to the to-do list file using the directory

todo_list = []

# Load the to-do list from a file
try:
    print("Loading the to-do list from the file")
    with open(todo_file, "r") as file:
        for line in file:
            print(line)
            todo_list.append(line.strip())
except FileNotFoundError as e:
    print(f"Error details: {e}")
    pass

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)