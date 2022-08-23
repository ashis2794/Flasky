from flask import Flask, render_template

# creating a flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')
def index():
#    return f"<h1>Hello, Ashish!</h1>"
    firstname = "Ashish"
    message = "This is a <strong>text</strong>."
    names = ["Ashish", "Mike", "Joey"]
    return render_template("index.html", name = firstname, message = message, names = names)

@app.route('/user/<username>')
def user_page(username):
    return render_template('user.html', name=username.title())

# custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500