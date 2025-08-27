from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 연결 정보
scheme = "mysql+pymysql"
host = "localhost"
user = "root"
password = "!23"
dbname = "test_db"

# 데이터베이스 엔진 생성
connection_string = f"{scheme}://{user}:{password}@{host}/{dbname}"
engine = create_engine(connection_string)

# 데이터베이스 모델 정의
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

# 데이터베이스 및 테이블 생성
def setup_database():
    Base.metadata.create_all(engine)

# 데이터베이스에 연결하고 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    setup_database()
    print("Database and users table created successfully.")