import os
from flask import Blueprint, render_template, redirect, url_for, current_app
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app import db
from app.models.user import User
from app.forms import RegistrationForm, LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)

        filename = 'default.jpg'
        if form.profile_pic.data:
            filename = secure_filename(form.profile_pic.data.filename)
            form.profile_pic.data.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        user = User(username=username, password=password, profile_pic=filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


