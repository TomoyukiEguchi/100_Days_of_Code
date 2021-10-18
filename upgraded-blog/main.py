from flask import Flask, render_template, request
import smtplib
import requests


posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()

OWN_EMAIL = ""
OWN_PASSWORD = ""

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def get_about_page():

    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def get_contact_page():
    if request.method == "POST":
        data = request.form
        send_email(data["username"], data["email"], data["phone_number"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#     if request.method == "POST":
#         data = request.form
#         print(data["username"])
#         print(data["email"])
#         print(data["phone_number"])
#         print(data["message"])
#         return "<h1>Successfully sent your message</h1>"
#     return render_template("contact.html")
    # username = request.form['username']
    # email = request.form['email']
    # phone = request.form['phone_number']
    # message = request.form['message']
    # return f"{username}, {email}, {phone}, {message}, Successfully sent your message!"

if __name__ == "__main__":
    app.run(debug=True)