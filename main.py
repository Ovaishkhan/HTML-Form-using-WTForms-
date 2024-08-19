from flask import Flask, render_template, request
import requests
import smtplib
from datetime import datetime
app = Flask(__name__)

"""
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["post"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"
"""

"""
@app.route("/form-entry",methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message </h2>"
"""

"""codes from previous code"""

posts = requests.get("https://api.npoint.io/5741df4170e3fae6fa0e").json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent = False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

"""
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.sendmail(
        from_addr="contact",
        to_addrs="ovaishajju0786@gmail.com",
        msg="successs"
    )
"""
if __name__ == "__main__":
    app.run(debug=True)
