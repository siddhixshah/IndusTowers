import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Indus Towers | Equity Research Report",
    page_icon="🗼",
    layout="wide",
)

# --- CUSTOM STYLING (The "Pro" Look) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; }
    h1, h2, h3 { color: #1e3a8a; }
    .report-box { padding: 20px; border-radius: 10px; background-color: #ffffff; border-left: 5px solid #1e3a8a; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: EXECUTIVE SUMMARY ---
with st.sidebar:
    st.image("https://www.industowers.com/wp-content/uploads/2023/07/Indus-Towers-Logo.png", width=200)
    st.title("NSE: INDUSTOWER")
    st.markdown("---")
    st.metric(label="Current Price (Feb '26)", value="₹477.35", delta="2.4%")
    st.metric(label="Rating", value="OUTPERFORM")
    st.metric(label="Target Price", value="₹560.00")
    st.markdown("---")
    st.info("**Thesis:** 5G densification is shifting the model from 'volume' to 'value' as loading charges drive margin expansion.")

# --- HEADER ---
st.title("🗼 Indus Towers: The 5G Infrastructure Toll-Gate")
st.caption("Institutional Equity Research | February 2026 Update")

# --- TOP ROW: CORE STATS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Tenancy Ratio", "1.62x", "Rising")
col2.metric("Market Cap", "₹1.28L Cr", "Large Cap")
col3.metric("Div. Yield", "6.1%", "Est.")
col4.metric("EV/EBITDA", "7.2x", "Undervalued")

st.markdown("---")

# --- SECTION 1: BUSINESS ARCHITECTURE ---
st.header("1. Business Model & Purpose")
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="report-box">
    <h4>What the company does</h4>
    India’s largest telecom tower infrastructure provider. It operates a "Neutral Host" model, 
    offering passive infrastructure (towers, power, space) to <b>Airtel, Jio, and Vi</b>.
    <ul>
        <li><b>Mental Model:</b> Telecom Landlord.</li>
        <li><b>Inventory:</b> ~260,000 Towers | ~420,000 Co-locations.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="report-box">
    <h4>Why it exists</h4>
    Telcos avoid duplicating massive Capex. By sharing towers:
    <ul>
        <li>Operators reduce Capex by 30-40%.</li>
        <li>Data growth requires massive capacity (24GB+/user).</li>
        <li>5G requires <b>Densification</b> (Signals travel shorter distances).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 2: TOWER ECONOMICS (Unit Level) ---
st.header("2. Unit Economics: The Power of Tenancy")

# Data for the Visual
tenancy_data = pd.DataFrame({
    'Tenancy': [1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
    'EBITDA_Margin': [22, 35, 48, 55, 62, 70]
})

fig = go.Figure()
fig.add_trace(go.Scatter(x=tenancy_data['Tenancy'], y=tenancy_data['EBITDA_Margin'], 
                         mode='lines+markers', name='EBITDA Margin %', line=dict(color='#1e3a8a', width=4)))
fig.update_layout(title="The Convexity of Returns (Margin vs. Tenancy)", xaxis_title="Tenancy Ratio", yaxis_title="EBITDA Margin %")

st.plotly_chart(fig, use_container_width=True)



st.markdown("""
- **1st Tenant:** Cost recovery phase. High depreciation and land lease.
- **2nd Tenant:** Strong profitability. Incremental revenue has ~90% margin.
- **3rd Tenant:** Pure Alpha. The tower becomes a massive FCF engine.
- **Strategic Insight:** Growth now occurs via **Equipment Loading** (upgrading 4G to 5G) which provides rent increases with zero extra land cost.
""")

# --- SECTION 3: GROWTH & DEBATE ---
st.header("3. Strategic Outlook")
t1, t2 = st.tabs(["Growth Drivers", "The Bear Case / Key Debate"])

with t1:
    st.markdown("""
    * **5G Rollout:** Equipment loading charges are the primary revenue driver for FY26.
    * **Vi De-risking:** Government AGR relief has stabilized receivables.
    * **Energy Arbitrage:** Transitioning to **Solar + Lithium-ion** is fixing the 'diesel leakage' problem.
    """)

with t2:
    st.markdown("""
    * **The Debate:** Will Small Cells replace Macro Towers?
    * **Analyst View:** Macro towers remain the 'backbone'; small cells are 'capillaries.' They are complementary, not substitutes.
    * **Risk:** Customer concentration (Airtel/Jio/Vi represent ~100% of revenue).
    """)

# --- SECTION 4: VALUATION THINKING ---
st.header("4. Valuation Framework")
st.markdown("""
<div class="report-box" style="border-left: 5px solid #10b981;">
<h4>How the Street is pricing Indus in 2026:</h4>
<ul>
    <li><b>Utility Lens:</b> Trading like a bond proxy. With receivables stable, the expected 6%+ yield makes it a "Safe Haven."</li>
    <li><b>Re-rating Potential:</b> Currently at 7x EV/EBITDA. Global peers (American Tower) trade at 15x+. As "Receivable Risk" vanishes, the multiple should expand to 9-10x.</li>
    <li><b>Value Trap vs. Multibagger:</b> If Tenancy crosses 1.8x, it's a multibagger. If active sharing becomes mandated by the regulator, it's a value trap.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- TRACKING CHECKLIST ---
st.subheader("📋 Analyst Tracking Checklist")
st.checkbox("Tenancy Ratio moving toward 1.7x", value=True)
st.checkbox("Monthly Receivable collection from Vi at 100%", value=True)
st.checkbox("Energy Margin improvement (Reduction in diesel costs)")
st.checkbox("New Tower Guidance (Target: 15k-20k p.a.)")

st.markdown("---")
st.caption("Disclaimer: This report is for educational purposes and reflects a simulated analysis as of February 2026.")
