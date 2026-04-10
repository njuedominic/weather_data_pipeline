import os
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

class WeatherRecord(Base):
    __tablename__ = 'kenya_weather'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    humidity = Column(Integer)
    description = Column(String)
    timestamp = Column(BigInteger)

class DBManager:
    def __init__(self):
        db_url = os.getenv("DATABASE_URL")
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def load_data(self, df):
        """Loads a pandas DataFrame into PostgreSQL."""
        try:
            df.to_sql('kenya_weather', self.engine, if_exists='append', index=False)
            print("Successfully loaded data to PostgreSQL.")
        except Exception as e:
            print(f"Database error: {e}")