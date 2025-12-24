
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

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install streamlit pandas matplotlib
