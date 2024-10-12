from sql_exeuctor import execute_sql_file 
from sql_exeuctor import app, db

@app.route('/individual-result')
def individual_result():
    execute_sql_file('bincom_test.sql')
    return "Database updated!"


# Route to test the server
@app.route('/')
def home():
    return "Hello, Flask is running!"

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)