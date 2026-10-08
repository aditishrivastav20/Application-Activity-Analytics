import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Application Activity Analytics",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("🔐 Application Activity Analytics Dashboard")

st.write(
    "Monitoring synthetic application activity logs, "
    "performance metrics, and unusual activity."
)

# Load dataset
df = pd.read_csv("activity_logs.csv")

# -------------------------
# BASIC METRICS
# -------------------------

total_events = len(df)
success_events = (df["status"] == "success").sum()
error_events = (df["status"] == "error").sum()
failed_events = (df["status"] == "failed").sum()

error_rate = (error_events / total_events) * 100

st.subheader("📊 Activity Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Events", total_events)
col2.metric("Successful Events", success_events)
col3.metric("Error Events", error_events)
col4.metric("Error Rate", f"{error_rate:.2f}%")

# Failed events
st.metric("Failed Events", failed_events)

# -------------------------
# ACTIVITY LOG TABLE
# -------------------------

st.subheader("📋 Activity Logs")

st.dataframe(
    df,
    use_container_width=True
)

# -------------------------
# EVENTS BY MODULE
# -------------------------

st.subheader("📈 Events by Module")

module_count = df["module"].value_counts()

st.bar_chart(module_count)

# -------------------------
# ERRORS BY MODULE
# -------------------------

st.subheader("⚠️ Errors by Module")

error_module = df[df["status"] == "error"]["module"].value_counts()

st.bar_chart(error_module)

# -------------------------
# AVERAGE DURATION
# -------------------------

st.subheader("⏱️ Average Duration by Module")

avg_duration = df.groupby("module")["duration"].mean()

st.bar_chart(avg_duration)

# -------------------------
# SUSPICIOUS ACTIVITY
# -------------------------

st.subheader("🚨 Suspicious Activity Detection")

threshold = 5

suspicious_modules = error_module[error_module >= threshold]

if len(suspicious_modules) > 0:

    for module, count in suspicious_modules.items():

        st.warning(
            f"{module}: {count} errors detected. "
            "This module crossed the defined alert threshold."
        )

else:

    st.success(
        "No modules crossed the defined alert threshold."
    )

# -------------------------
# SECURITY NOTE
# -------------------------

st.divider()

st.caption(
    "Security Note: This dashboard uses synthetic activity data only. "
    "No real user information or credentials are used."
)
