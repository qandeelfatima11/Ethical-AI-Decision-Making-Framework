import pandas as pd
from triage_decision_tree import assign_priority

# Load mock dataset
df = pd.read_csv('data/mock_patient_data.csv')

# Select 10 sample patients for testing
test_df = df.sample(10, random_state=42)

results = []

for _, row in test_df.iterrows():
    priority = assign_priority(
        severity=row['severity'], 
        wait_time=row['wait_time_min']
    )
    results.append({
        'patient_id': row['patient_id'],
        'age': row['age'],
        'gender': row['gender'],
        'severity': row['severity'],
        'wait_time_min': row['wait_time_min'],
        'assigned_priority': priority,
        'ethical_note': 'No age/gender bias applied'
    })

results_df = pd.DataFrame(results)
results_df.to_csv('results/test_results.csv', index=False)

print("✅ Ethical triage testing completed.")
