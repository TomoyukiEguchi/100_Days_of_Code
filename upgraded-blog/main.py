from flask import Flask, render_template
import requests


posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()

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


@app.route('/contact')
def get_contact_page():

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)