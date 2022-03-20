## What does this script do?
The script will run in background and will generate notification with the provided message after certain interval of time.


## Modules used - **time** and **plyer**
**Note:** 
1. `time` is a built-in module.
2. you need to do `pip install plyer` to use plyer and notification.

## Important function used:
#### 1. sleep() function from time module.
#### 2. notification.notify() function from plyer module. In this method, we provide few things namely - 
- title: provided title will be shown as title of the notification.
- message: provided message will be shown as message of the notification.
- timeout: the notification will automatically removed after provided timeout duration.

## How to use it?
- Just run the `.exe` file it will automatically create reminder with specified time.
- Also you can manually run `main.py` file using `python main.py`.

## How to use it in background?
- Use `pythonw main.py` command.
