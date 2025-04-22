from sklearn.linear_model import LinearRegression
import numpy as np

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_gender_input():
    while True:
        gender = input("Enter your gender (M/F): ").upper()
        if gender in ['M', 'F']:
            return gender
        print("Please enter 'M' or 'F'.")

def get_activity_level():
    levels = ['sedentary', 'light', 'moderate', 'active']
    while True:
        level = input("Activity level (sedentary, light, moderate, active): ").lower()
        if level in levels:
            return level
        print(f"Choose from: {', '.join(levels)}")

def get_fitness_goal():
    goals = ['bulk', 'cut', 'maintain']
    while True:
        goal = input("Fitness goal (bulk/cut/maintain): ").lower()
        if goal in goals:
            return goal
        print("Please enter 'bulk', 'cut', or 'maintain'.")

# --- User Input ---
print("Welcome to the Smart Calorie Tracker!\n")

name = input("Enter your name: ").strip().title()
weight = get_float_input("Enter your weight (kg): ")
height = get_float_input("Enter your height (cm): ")
age = get_int_input("Enter your age: ")
gender = get_gender_input()
activity_level = get_activity_level()
goal = get_fitness_goal()

# --- Calorie Needs Calculation ---
if gender == 'M':
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

activity_multipliers = {
    'sedentary': 1.2,
    'light': 1.375,
    'moderate': 1.55,
    'active': 1.725
}

tdee = bmr * activity_multipliers[activity_level]

# Adjust for goal
if goal == 'bulk':
    tdee += 300
elif goal == 'cut':
    tdee -= 300

protein_min = weight * 1.6
protein_max = weight * 2.2

print(f"\n{name}, your goal is to {goal}.")
print(f"Your daily calorie target: {int(tdee)} kcal")
print(f"Your daily protein target: {int(protein_min)}g - {int(protein_max)}g\n")

# --- Weekly Logging ---
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calories_consumed = []

print("Enter your calorie intake for each day:")
for day in weekdays:
    cal = get_int_input(f"{day}: ")
    calories_consumed.append(cal)

# --- Prediction ---
X = np.array(range(7)).reshape(-1, 1)
y = np.array(calories_consumed)

model = LinearRegression()
model.fit(X, y)
predicted = model.predict(np.array([[7]]))[0]

# --- Feedback ---
print(f"\n🔍 Prediction: Tomorrow you might consume around {int(predicted)} kcal.")

leeway = tdee * 0.05  # 5% buffer
low_bound = tdee - leeway
high_bound = tdee + leeway

print("\n📊 Daily Breakdown vs Target:")
for i in range(7):
    day = weekdays[i]
    actual = calories_consumed[i]
    if actual < low_bound:
        status = "⬇️ Under target"
    elif actual > high_bound:
        status = "⬆️ Over target"
    else:
        status = "✅ On target"
    print(f"{day}: {actual} kcal – {status}")

# --- Smart Advice ---
print("\n💡 Smart Suggestions:")

if goal == 'bulk':
    print("- Focus on calorie-dense whole foods like salmon, peanut butter, nuts, olive oil, and avocado.")
    print(f"- Hit at least {int(protein_min)}g of protein per day — think chicken, beef, eggs, Greek yogurt.")
    print("- Don't stress about hitting exact numbers. Aim for consistency over perfection.")

elif goal == 'cut':
    print("- Prioritize protein to stay full — lean meats, egg whites, protein shakes.")
    print("- Drink plenty of water throughout the day.")
    print("- Try intermittent fasting or 'banking calories' (eating lighter earlier to save for later).")
    print("- Stay active, even light movement like walking helps manage hunger and energy.")

elif goal == 'maintain':
    print("- Don’t worry about slight overages — it's normal.")
    print("- If you go over, walk a bit more or spread it over the next few days.")
    print("- Just stay within range on most days and you’ll maintain fine.")

print("\n🚀 Keep going, consistency beats perfection!")
