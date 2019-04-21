from flask import Flask, render_template

#This is for flask to know where to look for, ___ is used in python
app = Flask(__name__)

#decorator that allows us to write the function to return the website
@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about") 
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)