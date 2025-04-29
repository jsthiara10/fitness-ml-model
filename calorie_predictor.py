from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")  # Use env var or fallback

# --- Testable Functions ---

def calculate_bmr(weight, height, age, gender):
    return 10 * weight + 6.25 * height - 5 * age + (5 if gender == "M" else -161)

def calculate_tdee(bmr, activity):
    activity_multipliers = {
        'sedentary': 1.2, 'light': 1.375, 'moderate': 1.55, 'active': 1.725
    }
    return bmr * activity_multipliers.get(activity, 1.2)

# --- Flask Routes ---

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip().title()
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = int(request.form["age"])
        gender = request.form["gender"]
        activity = request.form["activity"]
        goal = request.form["goal"]

        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity)

        if goal == "bulk":
            tdee += 300
        elif goal == "cut":
            tdee -= 300

        protein_min = round(weight * 1.6)
        protein_max = round(weight * 2.2)

        calories = [int(request.form[day.lower()]) for day in
                    ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]

        X = np.array(range(7)).reshape(-1, 1)
        y = np.array(calories)
        model = LinearRegression().fit(X, y)
        predicted = int(model.predict(np.array([[7]]))[0])

        leeway = tdee * 0.05
        low = tdee - leeway
        high = tdee + leeway

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        feedback = []
        for i in range(7):
            status = "✅ On target"
            if calories[i] < low:
                status = "⬇️ Under target"
            elif calories[i] > high:
                status = "⬆️ Over target"
            feedback.append((days[i], calories[i], status))

        tips = {
            "bulk": [
                "Focus on calorie-dense foods: salmon, peanut butter, avocado, nuts, olive oil.",
                "Aim for consistent protein: chicken, beef, eggs, Greek yogurt.",
                "Don’t stress perfection, just stay consistent!"
            ],
            "cut": [
                "Prioritize protein to stay full — lean meats, shakes.",
                "Drink lots of water.",
                "Try intermittent fasting or ‘banking calories’ early in the day."
            ],
            "maintain": [
                "Slight overages are fine — just stay active.",
                "You can balance out by moving more or spreading out calories.",
                "Consistency over perfection!"
            ]
        }

        return render_template("result.html", name=name, tdee=int(tdee),
                               protein_range=f"{protein_min}-{protein_max}",
                               prediction=predicted, feedback=feedback,
                               tips=tips.get(goal, []))

    return render_template("index.html")

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True)
