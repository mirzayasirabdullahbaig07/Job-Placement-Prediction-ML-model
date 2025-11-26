# 🎓 AdmitWise

An **AI-powered interactive web application** built with **Streamlit** that predicts whether a candidate will get placed in a job (or admitted) based on academic performance and other features.  
The model simplifies decision-making for students, HR teams, and academic advisors by providing **data-driven placement predictions**.

---

## 🚀 Demo  
🔗 [Live Demo on Streamlit](https://job-placement-prediction-ml-model-007.streamlit.app/)  

## 🚀 Video Demo

https://github.com/user-attachments/assets/7c82904a-b4d1-4444-aae5-ed887995955d

---

## 📌 Features  
- Predicts **placement or admission status** instantly.  
- User-friendly **Streamlit UI** with number inputs and dropdowns.  
- One-hot encoding of categorical variables to match the model’s training data.  
- Lightweight and easy to use for non-technical users.  
- Easily extendable: retrain the model with new data or add new features.  
- Shows **binary prediction**: “Placed” or “Not Placed” along with probability.

---

## 🔍 How It Works  
1. The user inputs academic and background features, including:  
   - SSC percentage  
   - HSC percentage  
   - Degree percentage  
   - MBA percentage  
   - Work experience  
   - Specialization  
   - Gender  
   - And more  
2. Inputs are **one-hot encoded** for categorical features.  
3. A **Logistic Regression model** (trained offline) is loaded using Pickle.  
4. The model outputs a **binary prediction**: “Placed” or “Not Placed”.  
5. The result is displayed on the Streamlit app in a clear, user-friendly format.

---

## ⚙️ Tech Stack  

| Component | Technology / Library |
|-----------|--------------------|
| Frontend / Web | Streamlit |
| Model | Logistic Regression |
| ML Framework | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Model Persistence | Pickle |
| Visualization (optional) | Matplotlib, Seaborn |
| Environment | Python 3.9+ |

---

## 📸 Screenshots
### 🏠 Home Page
<img width="1890" height="802" alt="image" src="https://github.com/user-attachments/assets/a91673bf-888f-44b1-a20d-269c8dc1488e" />

### 🧑 Person is placed for job
<img width="1904" height="814" alt="image" src="https://github.com/user-attachments/assets/daa21d60-e59a-4bec-ac61-b4ce35bf9a96" />

### 📄 Person is not placed for job
<img width="1897" height="829" alt="image" src="https://github.com/user-attachments/assets/734e7d56-5de8-4b78-b26e-4764cdb8d718" />

---

## 👨‍💻 Author
**Mirza Yasir Abdullah Baig**  

- 🌐 [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)  
- 💼 [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
- 💻 [GitHub](https://github.com/mirzayasirabdullahbaig07)  

---

## ⚠️ Disclaimer
This project is for **educational purposes only** and should **NOT** be used for real-world business decisions without further validation.  

---

## 📂 Installation & Setup  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/admitwise.git
cd admitwise
