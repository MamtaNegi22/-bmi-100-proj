from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = None
    try:
        if request.method == "POST":
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            bmi_val = weight * 10000 / (height ** 2)  # height in cm
            bmi = "{:.2f}".format(bmi_val)

            # Category logic
            if bmi_val < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi_val <= 24.9:
                category = "Normal weight"
            elif 25 <= bmi_val <= 29.9:
                category = "Overweight"
            else:
                category = "Obese"
    except Exception:
        bmi = "Invalid input"
        category = None

    return render_template("home.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)