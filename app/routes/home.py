from flask import Blueprint, redirect, render_template, request, url_for

from app.extensions import db
from app.models import TestValue

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    """Display form and handle new test value submissions."""
    if request.method == 'POST':
        value = request.form.get('value')
        if value:
            db.session.add(TestValue(value=value))
            db.session.commit()
            return redirect(url_for('home.index'))
    values = TestValue.query.all()
    return render_template('index.html', values=values)
