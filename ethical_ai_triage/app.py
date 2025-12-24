import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.triage_decision_tree import assign_priority

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Ethical AI Healthcare Triage",
    layout="wide"
)

st.title("🏥 Ethical AI Healthcare Triage Dashboard")
st.caption("Explainable • Fair • Safety-Critical Decision System")

# -------------------- LOAD DATA --------------------
df = pd.read_csv("data/mock_patient_data.csv")

# Assign priority using rule-based logic
df["priority"] = df.apply(
    lambda x: assign_priority(x["severity"], x["wait_time_min"]),
    axis=1
)

# -------------------- METRICS --------------------
st.subheader("📊 Live ER Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients Today", len(df))
col2.metric("High Priority Patients", (df["priority"] == "High").sum())
col3.metric("Avg Wait Time (min)", round(df["wait_time_min"].mean(), 1))

# -------------------- CRITICAL ALERT --------------------
critical_count = df[df["severity"] == "Critical"].shape[0]
if critical_count > 0:
    st.error(f"🚨 ALERT: {critical_count} CRITICAL patients need immediate attention")
else:
    st.success("✅ No critical patients currently")

# -------------------- PATIENT QUEUE --------------------
st.subheader("🧾 Patient Queue (Triage Order)")

priority_order = {"High": 1, "Medium": 2, "Low": 3}
df["priority_rank"] = df["priority"].map(priority_order)

queue_df = df.sort_values(
    by=["priority_rank", "wait_time_min"],
    ascending=[True, False]
)[[
    "patient_id", "severity", "wait_time_min", "priority"
]]

# -------------------- SINGLE-CELL SEVERITY HIGHLIGHT --------------------
def highlight_severity_cell(row):
    styles = [""] * len(row)
    severity_col_index = row.index.get_loc("severity")

    if row["severity"] == "Critical":
        styles[severity_col_index] = "background-color: #ffcccc; font-weight: bold"  # Red
    elif row["severity"] == "Moderate":
        styles[severity_col_index] = "background-color: #fff2cc"  # Orange
    else:
        styles[severity_col_index] = "background-color: #e6ffe6"  # Green

    return styles

st.dataframe(
    queue_df.style.apply(highlight_severity_cell, axis=1),
    use_container_width=True
)

st.markdown("""
### 🧭 Severity Indicator
- 🔴 **Critical** – Life-threatening condition
- 🟠 **Moderate** – Requires medical attention
- 🟢 **Minor** – Safe to wait
""")

# -------------------- SIDEBAR PATIENT EXPLORER --------------------
st.sidebar.header("🔍 Patient Explorer")
selected_patient = st.sidebar.selectbox(
    "Select Patient ID",
    df["patient_id"]
)

patient = df[df["patient_id"] == selected_patient].iloc[0]

# -------------------- PATIENT DETAILS --------------------
st.subheader("👤 Selected Patient Details")
st.json({
    "Patient ID": patient["patient_id"],
    "Age": patient["age"],
    "Gender": patient["gender"],
    "Severity": patient["severity"],
    "Wait Time (min)": patient["wait_time_min"],
    "Assigned Priority": patient["priority"]
})

# -------------------- DECISION EXPLANATION --------------------
st.subheader("🧠 AI Decision Explanation")

if patient["priority"] == "High":
    st.error("High Priority → Critical condition or long wait time")
elif patient["priority"] == "Medium":
    st.warning("Medium Priority → Stable but requires monitoring")
else:
    st.success("Low Priority → Minor condition, safe to wait")

st.info("ℹ️ Age and gender are intentionally NOT used in decision-making")

# -------------------- CHARTS --------------------
st.subheader("📈 System-Level Insights")
col1, col2 = st.columns(2)

with col1:
    st.write("Severity Distribution")
    fig, ax = plt.subplots()
    df["severity"].value_counts().plot(kind="bar", ax=ax, color=["#ff4d4d", "#ffcc66", "#66ff66"])
    ax.set_ylabel("Number of Patients")
    st.pyplot(fig)

with col2:
    st.write("Priority Distribution")
    fig, ax = plt.subplots()
    df["priority"].value_counts().plot(kind="bar", ax=ax, color=["#ff4d4d", "#ffcc66", "#66ff66"])
    ax.set_ylabel("Number of Patients")
    st.pyplot(fig)

# -------------------- FAIRNESS PANEL --------------------
st.subheader("⚖️ Ethical & Fairness Checks")

fairness_table = df.groupby(["gender", "priority"]).size().unstack().fillna(0)
st.dataframe(fairness_table)

st.success("""
✔ No age-based rules  
✔ No gender-based rules  
✔ Deterministic & explainable  
✔ Same input → same output  
✔ Suitable for safety-critical use
""")

# -------------------- FOOTER --------------------
st.caption("Ethical AI Triage System • Designed for transparency, safety, and fairness")
