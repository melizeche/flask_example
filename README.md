# flask_example

## steps
 - Install Flask
 - copy the example in app.py
 - create another view
 - return html as string
 - return html as template
 - pass variables to the template

 ## Install flask
 On the terminal:

 `pip install flask`

 ## Copy the example
 https://github.com/pallets/flask

 ## Run the example
 `flask run`
 open the browser in http://localhost:5000/

 ## Make another view
```
@app.route("/page2wow")
def view2():
    htmlcontent="<h1>Hi I'm a header</h1><p>I'm a paragraph</p>"
    return htmlcontent
```