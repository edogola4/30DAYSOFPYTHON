# 📘 Day 23

# Setting up Virtual Environments

'''To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv'''

# $ pip install virtualenv

'''
Here's a step-by-step guide to completing the assignment for Day 23: Setting up Virtual Environments:

Steps:
Install virtualenv: Open your terminal (or command prompt for Windows) and install the virtualenv package:

bash
Copy code
pip install virtualenv
Create a Project Directory: Navigate to the directory where you want to create the project folder:

bash
Copy code
mkdir 30DaysOfPython
cd 30DaysOfPython
mkdir flask_project
cd flask_project
Create a Virtual Environment:

For Mac/Linux:
bash
Copy code
virtualenv venv
For Windows:
bash
Copy code
python -m venv venv
Check if the virtual environment is created: List the directory to verify that the venv folder was created:

For Mac/Linux:
bash
Copy code
ls
For Windows:
cmd
Copy code
dir
Activate the Virtual Environment:

For Mac/Linux:
bash
Copy code
source venv/bin/activate
For Windows (PowerShell):
bash
Copy code
venv\Scripts\activate
For Windows (Git Bash):
bash
Copy code
venv/Scripts/activate
Verify Activation: Once activated, your command prompt should look like this:

bash
Copy code
(venv) user@your-pc:/path/to/project$
Install Flask: With the virtual environment activated, install Flask:

bash
Copy code
pip install Flask
Check Installed Packages: After installing Flask, check which packages are installed:

bash
Copy code
pip freeze
The output should look something like this:

bash
Copy code
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
Deactivate the Virtual Environment: Once done, deactivate the virtual environment:

bash
Copy code
deactivate
Add venv to .gitignore: Create a .gitignore file in your project folder and add the following line to ensure that the venv folder is not pushed to GitHub:

bash
Copy code
venv/
Exercise Complete!
You've successfully set up your project directory with a virtual environment and Flask installed. Congratulations! 🎉
'''