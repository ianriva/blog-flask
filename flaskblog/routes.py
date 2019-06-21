from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post

posts = [
    {
        'author': 'Ian',
        'title': 'Blog Post 1',
        'content': 'Primer post',
        'date_posted': '20 abril, 2019'
    },
    {
        'author': 'juan vv',
        'title': 'Blog Post 2',
        'content': 'segundo contenido',
        'date_posted': '21 abril, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='Acerca de')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Cuenta creada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registro', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Logeado con exito!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login incorrecto. Verifique usuario y contraseña', 'danger')
    return render_template('login.html', title='Login', form=form)