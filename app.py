import streamlit as st
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title="OneDigital | Agentic Commerce Accelerator", layout="wide", page_icon="🚀")

# Title and Strategic Context
st.title("🚀 Agentic Commerce Optimizer")
st.markdown("""
    *Objective:* Bridge the gap between human-centric retail and agent-driven ecosystems. 
    This prototype identifies high-priority SKUs and optimizes them for AI Agent discoverability.
""")

# --- PHASE 1: PRODUCT PERFORMANCE (The 'Why') ---
st.header("📊 1. Product Performance Audit")
# Mock data representing Bunnings/Wesfarmers Group categories
data = {
    "Product ID": ["BUN-001", "BUN-002", "BUN-003", "BUN-004", "BUN-005"],
    "Product Name": [
        "Ryobi 18V ONE+ Lithium-Ion Battery",
        "Matador Conquest 4 Burner BBQ",
        "Ozito 1500W Corded Lawn Mower",
        "Kaboodle Kitchen Cabinet 600mm",
        "Dulux Wash&Wear Low Sheen White 4L"
    ],
    "Current Description": [
        "High capacity battery for Ryobi tools.",
        "4 burner gas BBQ with side burner and hood.",
        "Electric mower for small to medium lawns.",
        "Standard kitchen cabinet carcass.",
        "Interior paint with wash and wear technology."
    ],
    "Conversion Rate (%)": [12.5, 8.2, 14.1, 5.5, 9.8],
}

df = pd.DataFrame(data)

# Interactive filtering for the PM to identify 'at-risk' products
st.sidebar.header("Optimization Filters")
threshold = st.sidebar.slider("Conversion Threshold (%)", 0.0, 15.0, 10.0)
filtered_df = df[df["Conversion Rate (%)"] < threshold]

st.write(f"### SKUs Requiring Optimization (Conversion < {threshold}%)")
st.dataframe(filtered_df, use_container_width=True)

# --- PHASE 2: AGENTIC SEO PROMPT GEN (The 'How') ---
st.divider()
st.header("🤖 2. Agentic SEO Suggestion Engine")
if not filtered_df.empty:
    selected_product = st.selectbox("Select SKU to optimize for AI Agents:", filtered_df["Product Name"])
    current_desc = filtered_df[filtered_df["Product Name"] == selected_product]["Current Description"].values[0]
    
    # This creates a structured prompt for Claude/Azure OpenAI
    agentic_prompt = f"""
    SYSTEM: You are an Agentic Commerce Specialist at Wesfarmers OneDigital.
    TASK: Rewrite the following product description to be "Machine-Readable" for AI Shopping Agents.
    Focus on: Structured attributes, technical specs, and compatibility constraints.
    
    PRODUCT: {selected_product}
    HUMAN DESCRIPTION: {current_desc}
    """
    
    st.info("Copy the prompt below into Claude to generate 'Agent-Ready' content:")
    st.text_area("Agentic Prompt:", value=agentic_prompt, height=200)
else:
    st.warning("All products are performing above the threshold.")

# --- PHASE 3: DATA INGESTION (The 'Scale') ---
st.divider()
st.header("🔍 3. Raw HTML Ingestion (Bunnings MVP)")
st.write("Simulating the extraction of unstructured web data into a clean RAG (Retrieval-Augmented Generation) pipeline.")

raw_html = st.text_area("Paste Bunnings 'View Source' HTML here:", height=150, placeholder="<html>...</html>")

if raw_html:
    # Logic to simulate detection of Wesfarmers brands
    if "Ryobi" in raw_html or "Bunnings" in raw_html:
        st.success("✅ Valid Wesfarmers Ecosystem Data Detected")
        st.info("Agent Insight: Detected 15+ potential structured attributes. Ready for MCP (Model Context Protocol) mapping.")
    else:
        st.warning("Data received. Searching for product markers...")

# Footer
st.divider()
st.caption("Developed by SSEretail | Agentic Commerce Product Manager Portfolio 2026")
