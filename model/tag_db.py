from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# 基础类
Base = declarative_base()

class Tag(Base):
  __tablename__ = 'tags'

  id = Column(Integer, primary_key = True)
  name = Column(String(255))
  color = Column(String(80))
