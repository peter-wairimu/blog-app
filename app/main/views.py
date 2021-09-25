from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from .. import db,photos
import markdown2
from ..request import get_quote
from .forms import  UpdateProfile
from ..models import User,Post,Comment,Like

@main.route("/")
def home():
    quotes = get_quote()
    posts = Post.query.all()
    return render_template("index.html",quotes=quotes,user= current_user,posts = posts)



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)






@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.home',uname=uname))


@main.route("/create-blog",methods =['GET','POST'])
@login_required
def create_blog():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash("Post can not be empty",category='error')

        else:
            post = Post(text=text,author =current_user.id)
            db.session.add(post)
            db.session.commit()

            flash('Post has been created successfully',category='success')

            return redirect(url_for('main.home'))
    return render_template('create_blog.html',user = current_user)

@main.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id = id).first()
    if not post:
        flash("Post does not exist",category='error')

    
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfuly',category='success')
    return redirect(url_for('views.home'))
