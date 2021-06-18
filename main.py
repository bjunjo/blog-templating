from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
blog_response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
blog_contents = blog_response.json()

@app.route('/blog')
def home():
    return render_template("index.html", contents=blog_contents)

@app.route('/post/<int:id>')
def show_post(id):
    return render_template("post.html", contents=blog_contents, id=id)

if __name__ == "__main__":
    app.run(debug=True)
