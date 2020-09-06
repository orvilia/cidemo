# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Mr Saurabh Dubey !! CONGRATULATIONS !!!!'

app.run(host='0.0.0.0', port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
