import pandas as pd

# Load activity logs
df = pd.read_csv("activity_logs.csv")

# ==============================
# BASIC ACTIVITY ANALYSIS
# ==============================

total_events = len(df)

success_events = (df["status"] == "success").sum()
error_events = (df["status"] == "error").sum()
failed_events = (df["status"] == "failed").sum()

error_rate = (error_events / total_events) * 100


# ==============================
# MODULE-WISE ANALYSIS
# ==============================

module_count = df["module"].value_counts()


# ==============================
# ERRORS BY MODULE
# ==============================

error_module = df[df["status"] == "error"]["module"].value_counts()


# ==============================
# AVERAGE DURATION
# ==============================

avg_duration = df.groupby("module")["duration"].mean()


# ==============================
# SUSPICIOUS ACTIVITY DETECTION
# ==============================

threshold = 5

suspicious_modules = error_module[error_module >= threshold]


# ==============================
# DISPLAY RESULTS
# ==============================

print("======================================")
print(" APPLICATION ACTIVITY ANALYTICS")
print("======================================")

print("\n----- BASIC ACTIVITY -----")
print("Total Events:", total_events)
print("Successful Events:", success_events)
print("Error Events:", error_events)
print("Failed Events:", failed_events)
print("Error Rate:", round(error_rate, 2), "%")

print("\n----- EVENTS BY MODULE -----")
print(module_count)

print("\n----- ERRORS BY MODULE -----")
print(error_module)

print("\n----- AVERAGE DURATION BY MODULE -----")
print(avg_duration.round(2))

print("\n----- SUSPICIOUS ACTIVITY -----")

if len(suspicious_modules) > 0:

    print("Modules crossing error threshold:")

    for module, count in suspicious_modules.items():
        print(f"{module}: {count} errors")

else:
    print("No suspicious activity detected.")

print("\n======================================")
print(" Analysis Completed Successfully")
print("======================================")