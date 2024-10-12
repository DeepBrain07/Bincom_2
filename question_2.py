from flask import Flask
from sqlalchemy import create_engine, MetaData, Table, text
# from sql_executor import execute_sql_file 

app = Flask(__name__)

# Connection string to your remote MySQL database
DATABASE_URL = "mysql+mysqlconnector://sql8737280:xznZBqaPzD@sql8.freemysqlhosting.net:3306/sql8737280"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Load the table metadata
metadata = MetaData()
metadata.reflect(bind=engine)

def execute_sql_file():
    # Connect to the database
    connection = engine.connect()
    
    try:
        # Example: Access the table if it exists
        example_table = metadata.tables.get("agentname")
        
        if example_table is not None:
            # Print the structure of the table
            print(example_table.columns)
            
            # Use `text()` for raw SQL queries
            # polling unit result
            query = text("SELECT polling_unit_uniqueid, party_score FROM announced_pu_results")
            result = connection.execute(query)
            result_list = []
            for row in result:
                result_list.append(row)
            # lga
            query2 = text("SELECT lga_id, lga_name FROM lga")
            result2 = connection.execute(query2)
            result2_list = []
            for row in result2:
                result2_list.append(row)
            # polling unit 
            query3 = text("SELECT unique_id, lga_id FROM polling_unit")
            result3 = connection.execute(query3)
            result3_list = []
            for row in result3:
                result3_list.append(row)
            dict = {}
            # Fetch and print the results
            for i in range(len(result_list)):
                res_id = result_list[i][0]
                for j in range(len(result2_list)):
                    # print(row2[0], "========")
                    if str(result2_list[j][0]) == str(res_id):
                        lga_id = result2_list[i][1]
                        if pol_name in list(dict.keys()):
                            dict[pol_name] += int(result_list[i][1])
                        else: 
                            dict[pol_name] = int(result_list[i][1])
            return(dict)
        else:
            print("Table 'agentname' not found in the database.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the connection after all operations are complete
        connection.close()

# Call the function to execute the SQL file

@app.route('/lga-result')
def individual_result():
    data = execute_sql_file()
    page = ""
    for d in data.keys():
        page += f"{d} ============================== {data[d]} \n\n"
    return page if page else "No results found."  


# Route to test the server
@app.route('/')
def home():
    return "Hello, Flask is running!"

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)