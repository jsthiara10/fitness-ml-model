# fitness-ml-model
# 🏋️‍♂️ Calorie Predictor Web App

A simple but effective fitness web application that calculates your daily calorie needs (TDEE), predicts tomorrow's intake using a linear regression model, and offers actionable insights based on your fitness goal — bulk, cut, or maintain.

Built with Python, Flask, and scikit-learn, this app combines practical machine learning with an interactive frontend.

---

## 🔍 Features

- Step-by-step flow: Enter personal info → Get your daily calorie target → Log your weekly intake
- Predictive modeling: Uses linear regression to forecast tomorrow's calorie intake
- Smart feedback: Personalized tips based on user goals and trends
- Clean multi-page UI with reminders and status indicators
- Fully written in Python and HTML — no JavaScript frameworks required

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, scikit-learn, NumPy
- **Frontend**: HTML, Jinja2 templates (served via Flask)
- **Model**: Linear Regression (for calorie prediction)
- **Deployment**: Google App Engine (GCP)

---

## 🚀 Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/fitness-calorie-predictor.git
cd fitness-calorie-predictor


### 2. Create a virtual environment 

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows


### 3. Install dependencies

pip install -r requirements.txt


### 4. Set environment variables

Create a .env file in the root directory and add:

SECRET_KEY=your-secure-random-secret-key


You can generate a secure key using:

python -c "import secrets; print(secrets.token_hex(16))"

###6. Running Unit Tests

Unit tests are in the tests/ folder and validate key parts of the backend logic

python -m unittest discover tests

You should see:
...
Ran 3 tests in 0.000s
OK

### 7.Project Structure

fitness-calorie-predictor/
├── calorie_predictor.py       # Main Flask app
├── config.py                  # App configuration (secret keys, etc.)
├── templates/
│   ├── index.html             # Personal info input
│   ├── intake.html            # Weekly calorie intake page
│   └── result.html            # Final results page
├── tests/
│   └── test_core.py           # Unit tests
├── .env                       # Local secrets (not tracked)
├── .gitignore
└── requirements.txt

