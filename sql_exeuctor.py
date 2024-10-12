from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://daniel:daniel-07@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def execute_sql_file(sql_file_path):
    # Open and read the .sql file
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    
    # Use SQLAlchemy's engine to execute the script
    with db.engine.connect() as connection:
        for statement in sql_script.split(';'):
            if statement.strip():
                connection.execute(statement)
