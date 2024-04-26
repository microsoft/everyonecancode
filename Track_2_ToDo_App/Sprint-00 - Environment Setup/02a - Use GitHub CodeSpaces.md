# Using GitHub CodeSpaces
⏲️ _Est. time to complete: 10 min._ ⏲️

## Here is what you will learn 🎯
You will learn the following:
- What is GitHub Codespaces and how it can benefit your development process.
- How to create and stop GitHub Codespaces.
- How to understand and use the `devcontainer.json` file in a project.
- How to install and use extensions in a Codespace.

## Table Of Contents
- [Introduction to GitHub Codespaces](#introduction-to-github-codespaces)
- [Creating and Stopping a GitHub Codespace](#creating-and-stopping-a-github-codespace)
- [Understanding the `devcontainer.json` file](#understanding-the-devcontainerjson-file)
- [Installing and using extensions in a Codespace](#installing-and-using-extensions-in-a-codespace)

## Introduction to GitHub Codespaces

Welcome to our project! If you're new to programming, don't worry. We're here to guide you through the process. We use something called Codespaces, which is a feature provided by GitHub. You can learn more about it [here](https://github.com/features/codespaces).

GitHub Codespaces is a cloud-based development environment. It's like a virtual coding setup that lives on the internet, not on your personal computer. It allows you to write, run, debug, test, save different versions of your code (commit), and share your code with others (push), all from your web browser. This means you don't need to set up a local development environment on your computer, which can be a complex and time-consuming process, especially for beginners.

Here are some of the advantages of using Codespaces:

- **No setup required**: You don't need to install any software or configure your computer to start coding. Just open a Codespace, and you're ready to go!

- **Consistent environments**: Each Codespace is isolated and consistent. This means you won't run into issues like "it works on my machine but not on yours".

- **Powerful and flexible**: Codespaces are powered by Visual Studio Code and support a wide range of programming languages and tools. You can customize your Codespace with extensions and settings to fit your workflow.

- **Accessible from anywhere**: As long as you have an internet connection, you can access your Codespace from any device, anywhere in the world.

- **Limited free usage**: GitHub provides up to 60 hours of free usage of Codespaces per month. This makes it a cost-effective solution for beginners and small projects.

Now that you know what Codespaces is and why it's useful, let's dive into how to use it in our project!


## Creating and Stopping a GitHub Codespace

Creating a new Codespace is easy, when you know where to look:

1. Navigate to the main page of the GitHub repository for which you want to create a Codespace.
2. Click on the green "Code" button on the top right and switch from the local to the Codespaces tab.
3. Click on the plus symbol. GitHub will now create a new Codespace and open it in a new browser window. It might take a few minutes to load but just like that you're done!

![Create Codespaces](../content-images/Sprint%2000/github/CreateCodespaces.png)

To stop a Codespace, follow these steps:

1. Go back to the main page of the GitHub repository (the tab should still be open in your web browser) 
2. Click on the three dots in the top right corner of the Codespace window.
3. Select "Stop Codespace". Your Codespace will now be stopped and closed. You can reopen it later by returning to your repository and selecting the same Codespace from the list.

![Stop Codespaces](../content-images/Sprint%2000/github/StopCodespaces.png)

If you do not explicitly stop a codespace, it will continue to run until it times out from inactivity. Closing a codespace does not stop the Codespace.

## Understanding the `devcontainer.json` file

In our project, you'll find a file named `devcontainer.json` which is located in the.devontainer folder. This file is automatically detected by GitHub and like a recipe for Codespaces. It tells Codespaces how to set up the environment for our project. Let's break down what each part means:

```json
{
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "postCreateCommand": "python3 -m pip install -r Application/requirements.txt",
  "customizations": {
    "codespaces": {
      "openFiles": ["Application/README.md"]
    },
    "vscode": {
      "extensions": [
        "ms-toolsai.jupyter",
        "ms-python.python",
        "github.copilot"
      ]
    }
  }
}
```

- `"image": "mcr.microsoft.com/devcontainers/universal:2"`: This line tells Codespaces to use a specific Docker image. Docker images are like blueprints for creating containers, which are isolated environments where you can run your code. 

    In this case, we're using the `mcr.microsoft.com/devcontainers/universal:2` image. This is a universal image provided by Microsoft that includes a wide range of development tools. It's designed to support many different types of projects, making it a great starting point for most Codespaces.

    This image includes tools for several programming languages, databases, and utilities. It also includes the Visual Studio Code Server, which allows you to use Visual Studio Code's interface in your web browser.

    By using this image, we ensure that everyone working on the project has the same tools available, regardless of their local machine. 

- `"postCreateCommand": "python3 -m pip install -r Application/requirements.txt"`: After the base Docker image is set up, this command runs. It's like adding the specific ingredients for our project. 

    This command is a standard way to install Python packages. Here's what each part of the command does:

    - `python3`: This is the version of Python we're using. Python 3 is the current and most widely used version of Python.

    - `-m pip`: This tells Python to use the `pip` tool. `pip` is like a handyman that can fetch and install Python packages for you. These packages are ready-made pieces of code that you can use in your project.

    - `install`: This is the task we're giving to `pip`. It's like saying, "Hey pip, please install something for me."

    - `-r Application/requirements.txt`: The `-r` option tells `pip` to look in a specific file for a list of packages to install. In this case, the file is `Application/requirements.txt`. This file is like a shopping list of all the Python packages that our project needs.

    By running this command, we make sure that all the necessary Python packages are installed in the Codespace. This is like setting up all the tools and materials before starting a DIY project.

## Installing and using extensions in a Codespace

The `devcontainer.json` file also allows us to customize our Codespaces environment. We have two types of customizations:

- `"codespaces"`: These customizations apply when we're using Codespaces. `"openFiles": ["README.md"]` means that the `README.md` file that you saw on the main page will automatically pop up when you start the Codespace. It's like walking into a room and finding a welcome note on the table.

- `"vscode": {"extensions": ["ms-toolsai.jupyter", "ms-python.python", "github.copilot"]}`: This part tells Visual Studio Code to automatically add three helpers, called extensions, when the Codespace is created:

  - `ms-toolsai.jupyter`: This is like a digital notebook where you can write and run code, and also add notes, images, or even equations. It's very popular in data science because you can see your data and your code side by side. The Jupyter extension lets you use these notebooks right inside Visual Studio Code.

  - `ms-python.python`: This is a helper for writing Python code. It adds features like code suggestions, checks your code for mistakes, and even formats your code to make it look neat and consistent. 

  - `github.copilot`: This is an AI-powered extension that assists you in writing code. It suggests code as you type based on patterns in publicly available code. It's like having a co-pilot that helps you navigate and improve your code. After activating it with the code provided by us, you can chat with it by using the speech bubble icon on the left side.


By including these extensions in our `devcontainer.json` file, we make sure they are automatically added in the Codespace. This means you don't have to add them yourself, and everyone working on the project has the same setup.

We hope this helps you understand how our project is set up in Codespaces. Happy coding!


[🔼 Sprint 0 - Home](readme.md) | [Next Sprint ▶](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/README.md)
