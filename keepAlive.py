from flask import Flask
import os
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Hi."


def run():
    app.run(debug=False, host="0.0.0.0", port=os.getenv("PORT"))


def start():
    server = Thread(target=run)
    server.start()
