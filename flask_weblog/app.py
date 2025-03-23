from flask import Flask, render_template,request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dbfeeder import Post

engine = create_engine('sqlite:///post.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)

@app.route("/createpost",methods=["GET","POST"])
def createpost():
    if request.method=="POST":
        formlist=list(request.form.values())
        post2 = Post(title_des=formlist[0], post_date=formlist[1],
                post_text_1=formlist[2], post_text_2=formlist[3])
        session.add_all([post2])
        session.commit()
    return render_template("createpost.html")

@app.route("/")
def index():
    posts = session.query(Post).all()
    return render_template("index.html",posts=posts)

if __name__=='__main__':
    app.run(debug=True)
