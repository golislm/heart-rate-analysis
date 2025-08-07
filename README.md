# heart-rate-analysis
# 💓 Resting Heart Rate Analysis Using Python

This project explores how **BMI (Body Mass Index)**, **physical activity**, **smoking habits**, and **gender** affect **resting heart rate (Pulse1)** among university students.

---

## 📊 Project Overview

A medical researcher collected data from **91 students**, including:

- Resting heart rate (Pulse1)
- Height & weight
- Smoking status
- Physical activity level
- Gender
- Whether they ran in place for 1 minute (Ran)

The goal is to investigate how different lifestyle and biological factors correlate with heart rate, with a focus on cardiovascular health.

---

## 📁 Dataset

The dataset includes the following columns:

| Feature             | Description                             |
|---------------------|-----------------------------------------|
| `Pulse1`            | Resting heart rate (before any activity) |
| `Pulse2`            | Heart rate after activity                |
| `Ran`               | Whether the participant ran in place     |
| `Smokes`            | Smoking status                           |
| `Gender`            | M or F                                  |
| `Height` / `Weight` | Raw units (inches, pounds)               |
| `Activity`          | Activity level: Slight, Moderate, A lot |
| `BMI`               | Calculated from weight (kg) / height (m²) |

---

## 🔧 Methods & Tools

- **Language**: Python 3
- **Libraries**:  
  `pandas`, `matplotlib`, `seaborn`, `numpy`

- **Analysis steps**:
  - Convert height/weight to metric and compute BMI
  - Visualize distribution of heart rate vs variables
  - Group by smoker/non-smoker, active/inactive, BMI levels
  - Compare means and identify patterns
  - [Optional] Perform statistical testing (e.g., t-test, ANOVA)

---

## 📈 Key Findings

- **Smokers** tend to have **higher resting heart rates** than non-smokers.
- Participants with **low physical activity** ("Slight") generally show **higher Pulse1**.
- **Higher BMI** is moderately associated with increased heart rate.
- Surprisingly, some participants who **did not run** had slightly **higher Pulse1**—possibly due to low fitness or other factors.

---

## 📄 Output Files

- 📘 `analysis.ipynb` → Jupyter Notebook with code & comments  
- 📄 `heart_report.html` → Final exported HTML report with visualizations  
- 📊 `data.csv` → Cleaned version of the dataset

---

## 📌 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-rate-analysis.git
   cd heart-rate-analysis

