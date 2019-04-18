from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def home():
  return render_template("home.html")
  
 @app.route("/Salvador")
 def salvador():
  return "Hello, Salvador"
 
 if _name_ == "_main_":
  app.run(debug=True)
  We made two new changes
 
