from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
import datetime

app = Flask(__name__)
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('jinja.html')


@app.route('/')
def time():
    timezones = ["EST", "CST", "MST", "PST"]
    selected_timezone = request.args.get("select")
    time = datetime.datetime.now()
    if selected_timezone == "CST":
        time = time + datetime.timedelta(hours=-1)
    elif selected_timezone == "MST":
        time = time + datetime.timedelta(hours=-2)
    elif selected_timezone == "PST":
        time = time + datetime.timedelta(hours=-3)

    return template.render(
        time=time.time(),
        timezones=timezones,
        selected_timezone=selected_timezone
    )

# return "Hello World"
# return
# hello = app.route("/")(hello)

# s = "<html><h1>"

if __name__ == "__main__":
    app.run(debug=True)
