from flask import Blueprint, render_template
from flask_login import login_required ,current_user

main = Blueprint('main',__name__)

#route is used to  bind url to functions
@main.route('/')
def index():
	return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
	#use current_user object for the user
	return render_template('profile.html',name=current_user.name)

	
