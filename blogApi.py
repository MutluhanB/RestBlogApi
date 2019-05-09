from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedirectory = os.path.abspath(os.path.dirname(__file__))

#Setting up the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedirectory, "blog_db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#init db
db = SQLAlchemy(app)
#init Marshmallow
ma = Marshmallow(app)

#Blogpost Model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(500))

    def __init__(self,title,text):
        self.title = title
        self.text = text


#Blogpost schema
class BlogpostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "text")

#init schema
blogpost_schema = BlogpostSchema(strict=True)
#this one for multiple products
blogposts_schema = BlogpostSchema(many=True, strict=True)

#Routes

#POST a blogPost
@app.route("/blog", methods=["POST"])
def createPost():
    title = request.json["title"]
    text = request.json["text"]

    newPost = BlogPost(title,text)
    db.session.add(newPost)
    db.session.commit()

    return blogpost_schema.jsonify(newPost)

#GET !single! blogPosts
@app.route("/blog/<id>", methods=["GET"])
def getPost(id):
    post = BlogPost.query.get(id)
    return blogpost_schema.jsonify(post)

#GET !all! blogPosts
@app.route("/blog", methods=["GET"])
def getPosts():
    allPosts = BlogPost.query.all()
    result = blogposts_schema.dump(allPosts)
    return jsonify(result.data)

#UPDATE a blogPost
@app.route("/blog/<id>", methods=["PUT"])
def updatePost(id):

    post = BlogPost.query.get(id)
    title = request.json["title"]
    text = request.json["text"]

    post.title = title
    post.text = text

    db.session.commit()

    return blogpost_schema.jsonify(post)

#DELETE !single! blogPosts
@app.route("/blog/<id>", methods=["DELETE"])
def deletePost(id):
    post = BlogPost.query.get(id)

    db.session.delete(post)
    db.session.commit()

    return blogpost_schema.jsonify(post)


if __name__ == "__main__":
    app.run(port = 5000,debug =True)
