from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for blog posts
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    if 0 <= post_id < len(posts):
        del posts[post_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
