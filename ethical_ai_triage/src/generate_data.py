import pandas as pd
import random

random.seed(42)

patients = []
for i in range(1, 61):  # 50+ patients/day
    patients.append({
        "patient_id": f"P{i}",
        "age": random.randint(18, 85),
        "gender": random.choice(["Male", "Female"]),
        "severity": random.choices(
            ["Critical", "Moderate", "Minor"],
            weights=[0.25, 0.45, 0.30]
        )[0],
        "wait_time": random.randint(5, 90)
    })

df = pd.DataFrame(patients)
df.to_csv("data/mock_patient_data.csv", index=False)

print("Dataset generated")
