## What does this script do?
The script will read the top 5 headlines and its summary from the NEWS API.

## Modules used - **requests**, **json**, **pypiwin32**, and **pickle**.
You need to install win32com by using `pip install pypiwin32`

## Important function used:
#### 1. Speak(), to speak a certain string.
#### 2. Dispatch(), to provide the type of voice.
#### 3. loads(), to convert JSON data into dictionary.

## How to generate the API?
- Goto https://newsapi.org
- Sign up to create a free developer account. 
- Generate your API key by logging in with your account.
- Finally, replace the generated API with `<your_api_key>` in the line-19 of the `main.py` file.

## How to use it?
- Just run the `.exe` file it will fetch data in JSON format from the website.
- Also you can manually run `main.py` file using `python main.py`.