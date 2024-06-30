from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


# Inheritance from the db.Model class 
class Pet(db.Model): 
   
   # Table name class attribute 
    __tablename__ = 'pets' # database table is named pets 

    # COLUMNS 
 #Class attribute which is a table's primary key 
    id = db.Column(db.Integer, primary_key=True)#
  
  # Class attribute assigned to the db column  
    name = db.Column(db.String)
    species = db.Column(db.String)

# Inheritance from db model class 
class User(db.Model):

    # table name class attribute 
    __tablename__='users'

    # class attribute for db column one of them must have the table's primary key 
  #(this is the primary key i.e id)  id= db.Column(db.Integer,primary_key=True)
    username = db.Column (db.string (80),unique=True # username has a unique string of 80
                          nullable=False, index=True)
    
    email = db.Column(db.String(120),unique=True,) # email has a unique key of 120
    verified=db.Column(db.boolean, default =False) # verified is a boolean that defaults to false if a value is not given 