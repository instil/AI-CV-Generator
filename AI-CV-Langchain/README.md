# policy-generator

## Project setup

1. Clone project  
2. Create a virtual environment. This can be done in the likes of PyCharm or via the command line by running `python3 -m venv venv`  
3. Activate the venv by running `source venv/bin/activate`  
4. Ensure your Python interpreter is pointing to your venv folder by checking project settings in your IDE 
5. Run `pip install -r requirements.txt` to install the projects python packages 
6. Set up your AWS credentials if you haven't already -> see [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
7. If running this project regularly then use yawsso to sign in to credentials every morning like [this](https://instil.atlassian.net/wiki/x/f4BLXg)
  
## Modifying projects python packages

Updates to python packages requires updating the projects `requirements.txt` file.  
To do this run `pip freeze > requirements.txt` in the command line and commit the changes using Git.

For more information on how the requirements file works see [here](https://pip.pypa.io/en/latest/user_guide/#requirements-files)

## To generate a policy
1. Run `python main.py`
2. Follow the console instructions. Rego and test files will be output to the current directory