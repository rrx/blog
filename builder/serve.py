import os
import threading
import time
from importlib import reload

import watchfiles
from flask import Flask, render_template, render_template_string, send_from_directory
from flask_socketio import SocketIO

import builder

FILE_DIRECTORY = os.path.abspath("public")
app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def home():
    return send_from_directory(FILE_DIRECTORY, "index.html")


@app.route("/<path:filename>")
def serve_file(filename):
    options = [
        filename,
        os.path.join(filename, "index.html"),
        filename + ".html",
        os.path.dirname(filename) + ".html",
    ]

    for f in options:
        path = os.path.join(FILE_DIRECTORY, f)
        if os.path.isfile(path):
            return send_from_directory(FILE_DIRECTORY, f)

    return send_from_directory(FILE_DIRECTORY, "404.html")


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(FILE_DIRECTORY, "404.html")


def background_task1():
    for changes in watchfiles.watch(FILE_DIRECTORY):
        print('public', changes)
        try:
            socketio.emit("reload", {})
            print("Triggered reload")
        except:
            import traceback

            traceback.print_exc()

    print("END")


def background_task2():
    os.system("make build")
    for changes in watchfiles.watch("builder", "templates", "static", "content"):
        try:
            print('source', changes)
            # reload(builder)
            # builder.parse_tree(debug=True)
            os.system("make build-debug")
        except:
            import traceback

            traceback.print_exc()
    print("END")


def serve():
    assert os.path.exists(FILE_DIRECTORY)
    assert os.path.exists(os.path.join(FILE_DIRECTORY, "404.html"))
    threading.Thread(target=background_task1).start()
    threading.Thread(target=background_task2).start()
    socketio.run(app, debug=False, allow_unsafe_werkzeug=True)
