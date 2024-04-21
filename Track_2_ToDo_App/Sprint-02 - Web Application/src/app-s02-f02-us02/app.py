###############################################################################
## Sprint 2: Web Application
## Feature 2: Personalize Web Application
## User Story 2: Personalize Web Application
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
    with open(todo_file, "r+") as file:
        for line in file:
            print(line)
            todo_list.append(line.strip())
except FileNotFoundError as e:
    print(f"Error details: {e}")
    pass

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todo_list.append(todo)
    save_todo_list()
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove_todo():
    item_number = int(request.form["item_number"])
    if 0 < item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
        save_todo_list()
    return redirect(url_for("index"))

def save_todo_list():
    with open(todo_file, "w") as file:
        for todo in todo_list:
            file.write(todo + "\n")

if __name__ == "__main__":
    app.run(debug=True)