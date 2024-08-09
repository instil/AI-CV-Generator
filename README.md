## Project setup

1. Clone project  
2. Create a virtual environment. This can be done in the likes of PyCharm or via the command line by running `python3 -m venv venv`  
3. Activate the venv by running `source venv/bin/activate`  
4. Ensure your Python interpreter is pointing to your venv folder by checking project settings in your IDE 
5. Run `pip install -r requirements.txt` to install the projects python packages  
6. Download the model for local use from HuggingFace - [openchat-3.5-1210.Q4_0.gguf](https://huggingface.co/TheBloke/openchat-3.5-1210-GGUF/blob/main/openchat-3.5-1210.Q4_0.gguf)
7. Run the `cv-generator.py` main method  
  
## Modifying projects python packages

Updates to python packages requires updating the projects `requirements.txt` file.  
To do this run `pip freeze > requirements.txt` in the command line and commit the changes using Git.
