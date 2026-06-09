"""
utils/styles.py
Central CSS / colour tokens for the rsynops dashboard.
"""

# Colour palette
CYAN    = "#00f5ff"
PURPLE  = "#bf5af2"
GREEN   = "#30d158"
ORANGE  = "#ff9f0a"
RED     = "#ff453a"
BG_DARK = "#0a0e1a"
BG_CARD = "rgba(255,255,255,0.04)"
BORDER  = "rgba(0,245,255,0.18)"

PLOTLY_TEMPLATE = "plotly_dark"
PLOTLY_COLORS   = [CYAN, PURPLE, GREEN, ORANGE]

# Global CSS injected via st.markdown
GLOBAL_CSS = """
<style>
/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');

/* Root */
html, body, [data-testid="stAppViewContainer"] {
    background: #0a0e1a !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: rgba(10,14,26,0.95) !important;
    border-right: 1px solid rgba(0,245,255,0.12);
}

/* hide default header */
[data-testid="stHeader"] { display: none; }

/* Metric overrides */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,245,255,0.15);
    border-radius: 12px;
    padding: 16px 20px;
    backdrop-filter: blur(12px);
    transition: border-color .25s, box-shadow .25s;
}
[data-testid="metric-container"]:hover {
    border-color: rgba(0,245,255,0.45);
    box-shadow: 0 0 18px rgba(0,245,255,0.12);
}
[data-testid="metric-container"] label {
    color: #8899aa !important;
    font-size: 0.72rem !important;
    letter-spacing: .08em;
    text-transform: uppercase;
    font-family: 'Space Mono', monospace !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #00f5ff !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 1.6rem !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    font-size: 0.75rem !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #00f5ff22, #bf5af222) !important;
    border: 1px solid rgba(0,245,255,0.4) !important;
    color: #00f5ff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.82rem !important;
    letter-spacing: .06em;
    border-radius: 8px !important;
    padding: 10px 24px !important;
    transition: all .2s !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #00f5ff44, #bf5af244) !important;
    box-shadow: 0 0 20px rgba(0,245,255,0.25) !important;
    transform: translateY(-1px);
}

/* Tabs */
[data-testid="stTabs"] button {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #8899aa !important;
    border-bottom: 2px solid transparent !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #00f5ff !important;
    border-bottom: 2px solid #00f5ff !important;
}

/* Divider */
hr { border-color: rgba(0,245,255,0.1) !important; }

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(0,245,255,0.15) !important;
    border-radius: 10px !important;
}

/* File uploader */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(0,245,255,0.03) !important;
    border: 1px dashed rgba(0,245,255,0.3) !important;
    border-radius: 10px !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0e1a; }
::-webkit-scrollbar-thumb { background: rgba(0,245,255,0.25); border-radius: 3px; }
</style>
"""
