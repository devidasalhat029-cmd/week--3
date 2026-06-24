from flask import Flask, render_template

app = Flask(__name__)

records = [
    {"id": 1, "field": "Field A", "crop": "Wheat"},
    {"id": 2, "field": "Field B", "crop": "Rice"},
    {"id": 3, "field": "Field C", "crop": "Cotton"},
    {"id": 4, "field": "Field D", "crop": "Soybean"},
    {"id": 5, "field": "Field E", "crop": "Maize"}
]

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/records")
def records_page():
    return render_template("recordd.html")

@app.route("/about")
def about():
    return render_template("about1.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/record/<int:record_id>")
def record(record_id):
    for r in records:
        if r["id"] == record_id:
            return render_template("record.html", record=r)
    return "Record Not Found"

if __name__ == "__main__":
    app.run(debug=True)