from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dbfeeder import Post

engine = create_engine('sqlite:///post.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)



@app.route("/")
def index():
    posts = session.query(Post).all()
    return render_template("index.html",posts=posts)

if __name__=='__main__':
    app.run(debug=True)
