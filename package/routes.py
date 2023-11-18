from flask import render_template

from package import app
from forms import UserForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    return render_template('registration.html', form=form)
