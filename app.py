from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    # Returns a string when we enter to the root of the website
    return "Hello, Mundo!!!!!"

@app.route("/page2wow")
def view2():
    # We can return HTML tags and the browser is going to interpret it
    # is ugly but """works"""
    htmlcontent="<h1>Hi I'm a header</h1><p>I'm a paragraph</p>"
    return htmlcontent

@app.route("/2")
def view_template():
    # "There must be a better way!"™, yes using templates
    # we can create HTML files and save it in the templates/ directory
    # so flask can find it
    return render_template("index.html")

@app.route("/3", methods=['POST','GET'])
def pass_arguments():
    my_name = "Isa"
    my_name2 = "Charlotte"
    # get the username GET parameter
    username = request.args.get('username')
    # get the POST name form field
    my_name = request.form.get('name')
    
    print(request.args.get('keys_info'))
    return render_template("three.html", name=my_name, surname="Williams", username=username, name2=my_name2)

@app.route("/list")
def view_list():
    # We have a nested list and we pass it as an argument so we can print it in
    # a nice way, we also can use a dictionary instead
    currencies = [["CHF",100], ["EUR", 200], ["USD",400], ["ARG",997], ["CRC",222], ["PYG", 876]] 
    return render_template("currencies.html", curr_list=currencies)


if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0")