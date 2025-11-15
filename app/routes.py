# Import Flask utilities:
# - render_template: Renders HTML templates.
# - request: Accesses incoming request data (form fields, etc.).
# - redirect: Redirects to another route.
# - url_for: Generates URLs for routes.
# - Blueprint: Organizes routes into modular components.
from flask import render_template, request, redirect, url_for, Blueprint

# Import the database instance and models
from app import db
from app.models import User, Post

# Create a Blueprint named 'main'.
# Blueprints allow you to organize routes and logic into reusable modules.
bp = Blueprint('main', __name__)

# Route for the homepage ('/')
# Handles both GET and POST requests:
# - GET: Displays all users and posts.
# - POST: Adds a new user if the name and email are provided and not already in the database.
@bp.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        bio = request.form.get('bio')   

        if name and email:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                error = "A user with this email already exists."
                print(error)
            else:
                user = User(name=name, email=email, bio=bio)  
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))

    users = User.query.all()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', users=users, posts=posts, error=error)


# Route to add a new post
# Handles POST requests to '/add_post':
# - Creates a new post with the given title, content, and user_id.
# - Saves the post to the database and redirects to the homepage.
@bp.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
    if title and content and user_id:
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('main.index'))