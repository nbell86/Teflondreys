from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":  # Checks to see if the incoming request is post, if so app requests the following information
        new_student_id = request.form.get("student-id", "")
        new_student_first_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(first=new_student_first_name, last=new_student_last_name, student_id=new_student_id)
        students.append(new_student)  # The new student is added to the students list

        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)



#  In order for this to run I need to install the Flask package