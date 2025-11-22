# AdmitWise

[Live Demo](https://job-placement-prediction-ml-model-007.streamlit.app/)

**AdmitWise** is a machine-learning-powered Streamlit application that predicts whether a candidate will get placed in a job (or admitted) based on academic performance and other features. It simplifies decision-making for students and HR teams by providing a data-driven placement (or admission) prediction.

---

## About the Project

AdmitWise is designed to help stakeholders (students, HR professionals, academic advisors) make **informed predictions** about job placement or admission outcomes. Rather than relying on gut-feel or superficial screening, users can input real academic performance and background features to get a probability-based prediction.

---

## How It Works

1. The user provides inputs for key features like SSC percentage, HSC percentage, degree percentage, MBA percentage, work experience, specialization, gender, and more.
2. These inputs are one-hot encoded (for categorical features) to match the model’s training format.
3. A **Logistic Regression** model (trained offline) is loaded using Pickle.
4. The model outputs a **binary prediction**: “Placed” or “Not Placed”.
5. The result is shown on the Streamlit web app in a user-friendly way.

---

## Features

- Input via **Streamlit UI** with number inputs and dropdowns  
- One-hot encoding of categorical variables to match training data  
- Real-time prediction of placement status  
- Lightweight and easy to use for non-technical users  
- Easy to extend: you can retrain the model with new data or add new features  

---

## Tech Stack

| Component | Technology / Library |
|---|---|
| Frontend / Web | Streamlit |
| Model | Logistic Regression |
| ML Framework | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Model Persistence | Pickle |
| Visualization (optional / during development) | Matplotlib, Seaborn |
| Environment | Python |

---

## Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/admitwise.git
   cd admitwise
