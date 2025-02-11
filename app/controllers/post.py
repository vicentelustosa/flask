from flask import Blueprint, render_template
from flask_login import login_required
from app.models.post import Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
@login_required
def list_posts():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('posts/index.html', posts=posts)
