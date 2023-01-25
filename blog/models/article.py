from sqlalchemy.orm import relationship
from blog.models.database import db
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="articles")
