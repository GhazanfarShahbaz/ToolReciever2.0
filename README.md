# Tool Reciever 2.0

# Description
A python script that takes arguments and then runs a corresponding command by connecting and requesting to the server.

## Usage
To run the script, execute the receiver.py file. It accepts the following command-line arguments:
```
-df or --default: Filter events by default options: today, weekly, month, or year.
-dgm or --dgmail: Get a list of default email snippets.
-diagnostics or --diagnostics: Show endpoint diagnostics.
-gl or --getlogs: Get today's logs.
-w or --weather: Get today's weather.
```

# Set Up 
Start by installing all of the requirements from the requirements.txt file 
```bash
python3 -m pip install -r requirements.txt
```
After that using the .env_sample file, create a .env file and fill it out with the values.
Setting up is then done!

## Example
```bash
python3 receiver.py -df today -w
```
This will filter events by today and get today's weather.