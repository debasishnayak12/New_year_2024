from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('show_wish', name=name))
    return render_template("home.html")

@app.route("/wish/<name>")
def show_wish(name):
    return render_template("result.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
