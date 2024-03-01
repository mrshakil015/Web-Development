from flask import Flask, render_template, redirect, url_for, request, jsonify
import pymysql

app = Flask(__name__)
app.secret_key = '6Lck7P8mAAAAABJdGubIiMM8u8e9lHuSE_KglmTC'
mysql = pymysql.connect(host='localhost', user='root', password='', db='dynamic_form')

@app.route('/', methods=['POST', 'GET'])
def index():
    data_dict ={}
    if request.method == 'POST':
        data_dict =entrydata()
        return render_template('viewform.html')
    return render_template('entryform.html')

@app.route('/viewform')
def viewform():
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM data_table")
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return jsonify(data=data)

def entrydata():
    data = {}
    studentname = request.form['studentname']
    institute = request.form['institute']
    designation = request.form['designation']
    course = request.form['course']
    image_file = request.files['image']
    imagename = image_file.filename
    print("Image: ",image_file.filename)
    if image_file:
        image_file.save('static/' + imagename)

    data = {'studentname': studentname, 'institute': institute, 'designation': designation, 'course': course, 'imagename': imagename}
    print(data['studentname'])

    cursor = mysql.cursor()
    query = "INSERT INTO data_table (studentname, institute, designation, course, imagename) VALUES(%s,%s,%s,%s,%s)"
    values = (studentname, institute, designation, course, imagename)
    cursor.execute(query, values)
    mysql.commit()
    
    return data


if __name__ == '__main__':
    app.run(debug=True, port=8080)