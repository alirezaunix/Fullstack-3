from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///post.db')
Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title_des = Column(String, nullable=False)
    post_date = Column(String, nullable=False)
    post_text_1 = Column(String, nullable=False)
    post_text_2 = Column(String, nullable=False)

Base.metadata.create_all(engine)


if __name__=="__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    post1 = Post(title_des="My First Post", post_date="2025-02-07", post_text_1="Hi Guys", post_text_2="Let Me Start")

    post2 = Post(title_des="My Second Post", post_date="2025-05-08",
                post_text_1="Hi Boys", post_text_2="Let Me Finish")

    session.add_all([post1, post2])
    session.commit()
