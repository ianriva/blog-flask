from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'ian r',
        'title': 'blog post 1',
        'content': 'primer comentario',
        'date_posted': '4 de mayo, 2019'
    },
    {
        'author': 'jonny boy',
        'title': 'blog post 2',
        'content': 'primer publicacion',
        'date_posted': '5 de mayo, 2019'
    }


]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
