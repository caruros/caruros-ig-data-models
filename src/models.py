from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
          
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)

    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    following = db.relationship('Follower', foreign_keys='Follower.follower_id', backref='follower', lazy=True)
    followers = db.relationship('Follower', foreign_keys='Follower.followed_id', backref='followed', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(300), nullable=False)
    caption = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    comments = db.relationship('Comment', backref='post', lazy=True)
    media = db.relationship('Media', backref='post', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "caption": self.caption,
            "user_id": self.user_id,
        }


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "user_id": self.user_id,
            "post_id": self.post_id,
        }


class Follower(db.Model):
    __tablename__ = 'followers'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "follower_id": self.follower_id,
            "followed_id": self.followed_id,
        }


class Media(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(5), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }