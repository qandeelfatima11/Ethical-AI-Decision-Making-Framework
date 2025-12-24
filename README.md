# Ethical AI Healthcare Triage System

An explainable, fairness-aware, rule-based Agentic AI system designed for healthcare triage scenarios.  
The system prioritizes patients in an emergency room setting while ensuring transparency, ethical compliance, and human-centered decision support.

---

## 📌 Project Overview

This project demonstrates an **Ethical Decision-Making Framework** for an Agentic AI deployed in a **healthcare triage scenario**.

The system:
- Simulates patient arrivals in an emergency room
- Assigns triage priority using transparent, rule-based logic
- Avoids sensitive attributes such as age and gender in decision-making
- Provides intuitive, clinician-friendly visualizations
- Enables ethical evaluation through fairness checks

---

## 🎯 Key Objectives

- Design an ethical decision-making framework for sensitive AI applications
- Balance efficiency and fairness in healthcare triage
- Provide full explainability of AI decisions
- Prevent automation bias through careful UI design
- Demonstrate ethical AI principles in practice

---

## 🧠 Ethical Decision Logic

The triage decision tree follows these rules:

- **Critical severity** → High priority
- **Moderate severity**
  - Wait time > 30 minutes → High priority
  - Else → Medium priority
- **Minor severity**
  - Wait time > 60 minutes → Medium priority
  - Else → Low priority

### Ethical Safeguards
- ❌ No age-based decision rules
- ❌ No gender-based decision rules
- ✔ Fully deterministic logic
- ✔ Same input → same output
- ✔ Transparent and explainable

---

## 🎨 Visual Design Philosophy

- **Red color is used only for medical severity**, not AI priority
- Single-cell highlighting avoids automation bias
- Patient queue mimics real hospital triage dashboards
- Clear legends and explanations support clinician trust

---

## 📊 Features

- Live patient queue with triage ordering
- Severity-based visual indicators
- Individual patient explanation view
- System-level analytics (charts)
- Fairness analysis by gender
- Ethical compliance panel
- Deployable Streamlit application

---

### 1️⃣ Install dependencies

```bash
pip install streamlit pandas matplotlib

