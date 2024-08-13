from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Department(Base):  # Создаём модель данных департамента
    __tablename__ = 'departments'  # Имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # Колонка с типом Integer
    name = Column(String, nullable=False)  # Колонка с типом String
    divisions = relationship('Division', back_populates="department")  # Связь с таблицей подразделений

class Division(Base):  # Создаём модель данных подразделения
    __tablename__ = 'divisions'  # Имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # Колонка с типом Integer
    name = Column(String, nullable=False)  # Колонка с типом String
    department_id = Column(Integer, ForeignKey('departments.id'))  # Внешний ключ
    department = relationship('Department', back_populates='divisions')  # Связь с таблицей департаментов
    employees = relationship('Employee', back_populates='division')  # Связь с таблицей сотрудников

class Employee(Base):  # Создаём модель данных сотрудника
    __tablename__ = 'employees'  # Имя таблицы

    id =  Column(Integer, primary_key=True, index=True)  # Колонка с типом Integer
    name = Column(String, nullable=False)  # Колонка с типом String
    division_id = Column(Integer, ForeignKey('divisions.id'))  # Внешний ключ
    division = relationship('Division', back_populates='employees')  # Связь с таблицей подразделений

# Создаём движок и локальную сессию
DATABASE_URL = 'sqlite:///./company.db'
engine =  create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для создания таблиц
def create_tables():
    Base.metadata.create_all(bind=engine)

 
