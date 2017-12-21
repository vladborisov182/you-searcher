from flask import redirect, render_template, request, session, url_for
from flask_security import login_required

from app import app, db
from forms import RegisterForm
from models import Role, User
from security import user_datastore


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/index')
@login_required
def main_page():
    return render_template('index.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(username = request.form['username'], email = request.form['email'], password=request.form['password'], active=True)
        role = Role.query.filter(Role.name.contains('user')).first()
        user_datastore.add_role_to_user(user, role)
        db.session.add(user)
        db.session.commit()
            
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    return render_template("login_user.html")
