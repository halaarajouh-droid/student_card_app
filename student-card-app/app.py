from flask import Flask, render_template, request
import os

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
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port,debug=True)