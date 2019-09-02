from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!!!"

@app.route("/page2wow")
def view2():
    htmlcontent="<h1>Hi I'm a header</h1><p>I'm a paragraph</p>"
    return htmlcontent

@app.route("/2")
def view_template():
    print("Hello world")
    return render_template("index.html")

@app.route("/3")
def pass_arguments():
    my_name = "Marcelo"
    username = request.args.get('username')
    return render_template("three.html", name=my_name, surname="Elizeche", username=username)

