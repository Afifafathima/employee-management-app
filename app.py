from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Afifa123",
    database="afifadbms2"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        ssn = request.form['ssn']
        department = request.form['department']
        age = request.form['age']
        salary = request.form['salary']
        cursor = db.cursor()
        cursor.execute("INSERT INTO employee (name, ssn, department, age, salary) VALUES (%s, %s, %s, %s, %s)",
                       (name, ssn, department, age, salary))
        db.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['name']
        ssn = request.form['ssn']
        department = request.form['department']
        age = request.form['age']
        salary = request.form['salary']
        cursor.execute("UPDATE employee SET name=%s, ssn=%s, department=%s, age=%s, salary=%s WHERE id=%s",
                       (name, ssn, department, age, salary, id))
        db.commit()
        return redirect('/')
    cursor.execute("SELECT * FROM employee WHERE id=%s", (id,))
    employee = cursor.fetchone()
    return render_template('update.html', employee=employee)

@app.route('/delete/<int:id>')
def delete_employee(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM employee WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
