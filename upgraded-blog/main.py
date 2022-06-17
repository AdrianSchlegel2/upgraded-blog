from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch API Data
response = requests.get("https://api.npoint.io/9026f703da2055b1ab8b")
data = response.json()


@app.route("/")
def main():
    return render_template("index.html", posts=data, length=len(data))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def post(num):
    num = int(num)
    return render_template("post.html", post_num=num, posts=data)


if __name__ == "__main__":
    app.run(debug=True)