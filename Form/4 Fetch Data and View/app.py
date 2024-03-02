from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='dynamic_form')
# Function to fetch data from MySQL database
def fetch_data_from_mysql():

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data_table")
    data = cursor.fetchall()

    cursor.close()
    connection.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Fetch data from MySQL database
    data = fetch_data_from_mysql()
    if data:
        # Convert data to a list of dictionaries
        keys = ['id','studentname','institute', 'designation', 'course', 'imagename']
        data_list = [dict(zip(keys, row)) for row in data]
        return jsonify(data_list)
    else:
        return jsonify([]) 

if __name__ == '__main__':
    app.run(debug=True)

