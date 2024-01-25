from flask import Flask , render_template
app = Flask("R & K Collection|Kabir Ahmad")

@app.route("/index.html")
def render_index():
    return render_template("index.html")

@app.route("/login.html")
def render_login():
    return render_template("login.html")

@app.route("/Products.html")
def render_products():
    return render_template("Products.html")

app.run(debug=True)