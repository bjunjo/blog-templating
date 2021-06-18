# blog-templating
## Problem: Making a blog website using Jinja and Flask
## Solutions
1. Showing the mainwebsite
```
@app.route('/blog')
def home():
    return render_template("index.html", contents=blog_contents)
    
...

{% for content in contents: %}
  <div class="content">
      <div class="card">
          <h2>{{ content['title'] }}</h2>
          <p class="text">{{ content['subtitle'] }}</p>
          <a href="{{ url_for('show_post', id=content['id']) }}">Read</a>
      </div>
  </div>
{% endfor %}
```
2. Showing blog posts
```
@app.route('/post/<int:id>')
def show_post(id):
    return render_template("post.html", contents=blog_contents, id=id)
...
{% for content in contents: %}
  <div class="content">
      {% if id == content['id']: %}
         <div class="card">
              <h2>{{ content['title'] }}</h2>
              <h4>{{ content['subtitle'] }}</h4>
              <p class="text">{{ content['body'] }}</p>
          </div>
      {% endif %}
</div>
{% endfor %}
```
