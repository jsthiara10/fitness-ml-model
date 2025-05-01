# fitness-ml-model
🏋️‍♂️ **Calorie Predictor Web App**

A simple but effective fitness web application that calculates your daily calorie needs (TDEE), predicts tomorrow's intake using a linear regression model, and offers actionable insights based on your fitness goal — bulk, cut, or maintain.

Built with Python, Flask, and scikit-learn, this app combines practical machine learning with an interactive frontend.

---

## 🔍 Features

- **Step-by-step flow**:  
  Enter personal info → Get your daily calorie target → Log your weekly intake
- **Predictive modeling**:  
  Uses linear regression to forecast tomorrow's calorie intake
- **Smart feedback**:  
  Personalized tips based on user goals and trends
- **Clean multi-page UI**:  
  With reminders and status indicators
- **No JavaScript frameworks required**:  
  Fully written in Python and HTML, served via Flask

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
```
### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

### 3. Install dependencies

pip install -r requirements.txt













