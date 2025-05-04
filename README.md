# 🎓 SGPA Estimator - REVA University

This Streamlit app helps students estimate their **semester GPA (SGPA)** using internal assessment (IA) and semester-end exam (SEE) marks. It also provides **target-based suggestions** if the student wants to achieve a specific SGPA.

---

## 📦 Features

- Subject-wise GPA estimation
- Handles both **Theory** and **Lab** subjects
- Uses **credit-weighted average** for accurate SGPA
- Supports **partial mark entry** (IA-1 only or no SEE yet)
- Suggests **marks required** in remaining components (IA/SEE) to meet your target SGPA

---

## 🚀 How to Run

1. **Clone this repo** or download the script:
   ```bash
   git clone https://github.com/chiraghontec/sgpa-estimator
   cd sgpa-estimator
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run gpa_estimator.py
   ```

---

## 📝 How to Use

1. Enter the **number of subjects** you have this semester.
2. For each subject:
   - Enter the name, type (**Theory/Lab**), and number of credits.
   - Enter the marks obtained in IA-1, IA-2 (out of 50 each), and SEE (out of 100). Leave fields blank if not attempted yet.
3. Set your **Target SGPA** (e.g., 8.5).
4. Click **"Estimate SGPA"** to:
   - Get your **current SGPA** (based on entered marks).
   - See **required marks** in upcoming IA/SEE to achieve your goal.

---

## 📘 Calculation Rules (as per REVA University)

- **Theory subjects**:
  - IA1 + IA2 + Assignments: 50 marks total (converted to 25)
  - SEE: 100 marks (converted to 50)

- **Labs**:
  - Internal: 35 marks (converted to 35)
  - SEE: 100 marks (converted to 65)

---

## 🛠 Future Improvements

- Save sessions for multiple semesters
- GPA to percentage mapping toggle
- Export results to PDF

---

## 🤝 Contributing

Feel free to fork, improve, and submit PRs.

---

## 📄 License

This project is under the [MIT License](LICENSE).
