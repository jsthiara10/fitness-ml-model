from flask import Flask, render_template, request, redirect, url_for, session
from sklearn.linear_model import LinearRegression
import numpy as np
import os
from dotenv import load_dotenv

# Load secret key from .env
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["name"] = request.form["name"].strip().title()
        session["weight"] = float(request.form["weight"])
        session["height"] = float(request.form["height"])
        session["age"] = int(request.form["age"])
        session["gender"] = request.form["gender"]
        session["activity"] = request.form["activity"]
        session["goal"] = request.form["goal"]

        # Calculate TDEE
        bmr = 10 * session["weight"] + 6.25 * session["height"] - 5 * session["age"] + (
            5 if session["gender"] == "M" else -161)
        activity_multipliers = {'sedentary': 1.2, 'light': 1.375, 'moderate': 1.55, 'active': 1.725}
        tdee = bmr * activity_multipliers[session["activity"]]
        if session["goal"] == "bulk":
            tdee += 300
        elif session["goal"] == "cut":
            tdee -= 300

        session["tdee"] = int(tdee)
        session["protein_min"] = round(session["weight"] * 1.6)
        session["protein_max"] = round(session["weight"] * 2.2)

        return redirect(url_for("intake"))
    return render_template("index.html")


@app.route("/intake", methods=["GET", "POST"])
def intake():
    if request.method == "POST":
        calories = [int(request.form[day.lower()]) for day in
                    ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
        session["calories"] = calories
        return redirect(url_for("result"))

    return render_template("intake.html", tdee=session.get("tdee"))


@app.route("/result")
def result():
    calories = session.get("calories")
    X = np.array(range(7)).reshape(-1, 1)
    y = np.array(calories)
    model = LinearRegression().fit(X, y)
    predicted = int(model.predict(np.array([[7]]))[0])

    leeway = session["tdee"] * 0.05
    low = session["tdee"] - leeway
    high = session["tdee"] + leeway
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    feedback = []
    for i in range(7):
        status = "✅ On target"
        if calories[i] < low:
            status = "⬇️ Under target"
        elif calories[i] > high:
            status = "⬆️ Over target"
        feedback.append((days[i], calories[i], status))

    goal = session["goal"]
    tips = []
    if goal == "bulk":
        tips = [
            "Focus on calorie-dense foods: salmon, peanut butter, avocado, nuts, olive oil.",
            "Aim for consistent protein: chicken, beef, eggs, Greek yogurt.",
            "Don’t stress perfection, just stay consistent!"
        ]
    elif goal == "cut":
        tips = [
            "Prioritize protein to stay full — lean meats, shakes.",
            "Drink lots of water.",
            "Try intermittent fasting or ‘banking calories’ early in the day."
        ]
    else:
        tips = [
            "Slight overages are fine — just stay active.",
            "You can balance out by moving more or spreading out calories.",
            "Consistency over perfection!"
        ]

    return render_template("result.html",
                           name=session["name"],
                           tdee=session["tdee"],
                           protein_range=f"{session['protein_min']}-{session['protein_max']}",
                           prediction=predicted,
                           feedback=feedback,
                           tips=tips)


if __name__ == "__main__":
    app.run(debug=True)
