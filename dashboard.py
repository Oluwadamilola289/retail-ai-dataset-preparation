import json
import pandas as pd
import streamlit as st
import time


# Page configuration
st.set_page_config(
    page_title="Retail AI Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load metrics
with open("reports/quality_metrics.json", "r") as file:
    metrics = json.load(file)
# NOW create the sidebar
st.sidebar.title("Retail AI Pipeline")
st.sidebar.success("Pipeline Status")

st.sidebar.write(metrics["status"])
st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")
st.sidebar.write("Author - Oluwadamilola Osho")

st.title("📊 Retail AI Data Quality Dashboard")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows Loaded", metrics["rows_loaded"])

with col2:
    st.metric(
        "Quality Score",
        f'{metrics["quality_score"]}%'
        )
    st.progress(metrics["quality_score"] / 100)

with col3:
    st.metric(
        "Pipeline Status", 
        metrics["status"]
    )

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Duplicates Removed", metrics["duplicates_removed"])

with col5:
    st.metric("Empty Rows Removed", metrics["empty_rows_removed"])

with col6:
    st.metric("Invalid Prices", metrics["invalid_prices"])

st.markdown("---")

st.subheader("Bounding Box Validation")

st.metric(
    "Invalid Bounding Boxes",
    metrics["invalid_bounding_boxes"]
)

if metrics["quality_score"] >= 95:
    st.success("🟢 Healthy Pipeline")

elif metrics["quality_score"] >= 80:
    st.warning("🟡 Review Recommended")

else:
    st.error("🔴 Pipeline Failed Validation")

chart = pd.DataFrame(
    {
        "Issue": [
            "Duplicates",
            "Empty Rows",
            "Invalid Boxes",
            "Invalid Prices",
        ],
        "Count": [
            metrics["duplicates_removed"],
            metrics["empty_rows_removed"],
            metrics["invalid_bounding_boxes"],
            metrics["invalid_prices"],
        ],
    }
)
start = time.time()

# pipeline work

runtime = round(time.time() - start, 2)

st.subheader("Validation Summary")

st.bar_chart(
    chart.set_index("Issue")
)
with open("logs/pipeline.log") as file:
    logs = file.readlines()

with st.expander("View Pipeline Logs"):
    st.code("".join(logs[-20:]))
if st.button("Refresh Dashboard"):
    st.rerun()
with open("reports/validation_report.txt") as file:
    report = file.read()

with st.expander("Validation Report"):
    st.text(report)