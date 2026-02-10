from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    student = None

    if request.method == "POST":
        student = {
            "name": request.form.get("name"),
            "id": request.form.get("id"),
            "department": request.form.get("department"),
            "university": request.form.get("university"),
            "level": request.form.get("level")
        }

    return render_template("home.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)