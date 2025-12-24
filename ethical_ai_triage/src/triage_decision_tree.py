def assign_priority(severity, wait_time):
    if severity == "Critical":
        return "High"
    elif severity == "Moderate":
        return "High" if wait_time > 30 else "Medium"
    else:
        return "Medium" if wait_time > 60 else "Low"
