"""
app.py — rsynops dashboard
ANN vs SNN Energy-Efficient MNIST Classification
Run: streamlit run app.py
"""

import streamlit as st

# ── Page config (must be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="rsynops · ANN vs SNN",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Internal imports ──────────────────────────────────────────────────────────
from utils import load_ann_results, load_snn_results, GLOBAL_CSS
from components import (
    render_hero,
    render_metrics_panel,
    render_kpi_cards,
    render_architecture,
    render_upload_panel,
    render_results_table,
    render_conclusion,
    accuracy_bar,
    energy_bar,
    inference_time_bar,
    training_loss_line,
    flops_synops_bar,
    radar_chart,
)

# ── Inject global CSS ─────────────────────────────────────────────────────────
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Load data (never crashes — falls back to mock) ───────────────────────────
ann = load_ann_results("data")
snn = load_snn_results("data")


# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px;">
        <div style="
            font-family:'Orbitron',monospace;
            font-size:1.25rem; font-weight:900;
            background: linear-gradient(90deg, #00f5ff, #bf5af2);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent;
            background-clip:text;
            margin-bottom:4px;
        ">rsynops</div>
        <div style="
            font-family:'Space Mono',monospace;
            font-size:0.6rem; color:#4b5563;
            letter-spacing:.1em; text-transform:uppercase;
        ">ANN vs SNN · MNIST</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        options=[
            "🏠  Project Overview",
            "🔮  Live Predictions",
            "⬡  ANN Metrics",
            "⚡  SNN Metrics",
            "📊  Comparison Charts",
        ],
        label_visibility="collapsed",
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # Quick stats in sidebar
    st.markdown("""
    <div style="font-family:'Space Mono',monospace;font-size:0.62rem;
                color:#4b5563;text-transform:uppercase;letter-spacing:.1em;
                margin-bottom:10px;">Quick Stats</div>
    """, unsafe_allow_html=True)

    energy_saved = round((1 - snn["energy"] / ann["energy"]) * 100, 1)

    def _sidebar_stat(label, value, color):
        st.markdown(f"""
        <div style="
            display:flex; justify-content:space-between; align-items:center;
            padding:7px 0; border-bottom:1px solid rgba(255,255,255,0.04);
        ">
            <span style="font-family:'Inter',sans-serif;font-size:0.73rem;color:#6b7280;">{label}</span>
            <span style="font-family:'Orbitron',monospace;font-size:0.78rem;color:{color};font-weight:700;">{value}</span>
        </div>
        """, unsafe_allow_html=True)

    _sidebar_stat("ANN Accuracy",   f"{ann['accuracy']}%",    "#00f5ff")
    _sidebar_stat("SNN Accuracy",   f"{snn['accuracy']}%",    "#bf5af2")
    _sidebar_stat("Energy Saved",   f"{energy_saved}%",       "#30d158")
    _sidebar_stat("ANN Energy",     f"{ann['energy']} mJ",    "#ff9f0a")
    _sidebar_stat("SNN Energy",     f"{snn['energy']} mJ",    "#30d158")
    _sidebar_stat("ANN FLOPs",      f"{ann['flops']//1000}K", "#00f5ff")
    _sidebar_stat("SNN SynOps",     f"{snn['synops']//1000}K","#bf5af2")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Space Mono',monospace;font-size:0.58rem;
                color:#374151;text-align:center;line-height:1.8;">
        Team rsynops · Hackathon 2025<br>
        <span style="color:#00f5ff22;">⬡</span> Built with Streamlit + Plotly
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════════════════

# ── 1. Project Overview ───────────────────────────────────────────────────────
if "Overview" in page:
    render_hero()

    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                color:#e2e8f0;letter-spacing:.1em;text-transform:uppercase;
                margin-bottom:14px;">◈ KPI Summary</div>
    """, unsafe_allow_html=True)
    render_kpi_cards(ann, snn)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                color:#e2e8f0;letter-spacing:.1em;text-transform:uppercase;
                margin-bottom:14px;">◈ Model Comparison</div>
    """, unsafe_allow_html=True)
    render_metrics_panel(ann, snn)

    st.markdown("<br>", unsafe_allow_html=True)
    render_architecture()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                color:#e2e8f0;letter-spacing:.1em;text-transform:uppercase;
                margin-bottom:14px;">◈ Results Table</div>
    """, unsafe_allow_html=True)
    render_results_table(ann, snn)

    st.markdown("<br>", unsafe_allow_html=True)
    render_conclusion(ann, snn)


# ── 2. Live Predictions ───────────────────────────────────────────────────────
elif "Predictions" in page:
    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700;
        background: linear-gradient(90deg,#00f5ff,#bf5af2);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-clip:text; margin-bottom:6px;
    ">Live Predictions</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;color:#4b5563;
                margin-bottom:24px;">Upload a handwritten digit and run both models.</div>
    """, unsafe_allow_html=True)

    render_upload_panel()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background:rgba(255,159,10,0.06); border:1px solid rgba(255,159,10,0.2);
        border-radius:12px; padding:14px 18px;
        font-family:'Space Mono',monospace; font-size:0.72rem; color:#ff9f0a;
        line-height:1.7;
    ">
        ⚠️  <strong>Note:</strong> Inference results shown here are <em>placeholder mocks</em>.
        Connect real trained models by editing <code>utils/inference.py</code> →
        <code>run_ann_inference()</code> and <code>run_snn_inference()</code>.
    </div>
    """, unsafe_allow_html=True)


# ── 3. ANN Metrics ────────────────────────────────────────────────────────────
elif "ANN" in page:
    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700;
        color:#00f5ff; margin-bottom:6px;
    ">ANN Metrics</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;color:#4b5563;
                margin-bottom:24px;">Artificial Neural Network — detailed performance breakdown.</div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1: st.metric("Accuracy",       f"{ann['accuracy']}%")
    with c2: st.metric("FLOPs",          f"{ann['flops']:,}")
    with c3: st.metric("Inference Time", f"{ann['inference_time']} ms")
    with c4: st.metric("Energy",         f"{ann['energy']} mJ")

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="medium")
    with col_a:
        st.plotly_chart(accuracy_bar(ann, snn), use_container_width=True)
    with col_b:
        st.plotly_chart(energy_bar(ann, snn),   use_container_width=True)

    st.plotly_chart(training_loss_line(ann, snn), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                color:#e2e8f0;letter-spacing:.1em;text-transform:uppercase;
                margin-bottom:14px;">◈ Full Metrics</div>
    """, unsafe_allow_html=True)
    render_results_table(ann, snn)


# ── 4. SNN Metrics ────────────────────────────────────────────────────────────
elif "SNN" in page:
    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700;
        color:#bf5af2; margin-bottom:6px;
    ">SNN Metrics</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;color:#4b5563;
                margin-bottom:24px;">Spiking Neural Network — neuromorphic performance breakdown.</div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1: st.metric("Accuracy",       f"{snn['accuracy']}%")
    with c2: st.metric("SynOps",         f"{snn['synops']:,}")
    with c3: st.metric("Inference Time", f"{snn['inference_time']} ms")
    with c4: st.metric("Energy",         f"{snn['energy']} mJ")

    if snn.get("timesteps"):
        c5, c6, _ = st.columns([1, 1, 2], gap="small")
        with c5: st.metric("Timesteps",  snn["timesteps"])
        with c6: st.metric("Spike Rate", f"{snn.get('spike_rate', 0):.4f}")

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="medium")
    with col_a:
        st.plotly_chart(accuracy_bar(ann, snn),      use_container_width=True)
    with col_b:
        st.plotly_chart(flops_synops_bar(ann, snn),  use_container_width=True)

    st.plotly_chart(training_loss_line(ann, snn), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                color:#e2e8f0;letter-spacing:.1em;text-transform:uppercase;
                margin-bottom:14px;">◈ Full Metrics</div>
    """, unsafe_allow_html=True)
    render_results_table(ann, snn)

    st.markdown("<br>", unsafe_allow_html=True)
    render_conclusion(ann, snn)


# ── 5. Comparison Charts ──────────────────────────────────────────────────────
elif "Charts" in page:
    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700;
        background: linear-gradient(90deg,#00f5ff,#bf5af2);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-clip:text; margin-bottom:6px;
    ">Comparison Charts</div>
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;color:#4b5563;
                margin-bottom:24px;">Interactive Plotly visualisations — ANN vs SNN.</div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Accuracy", "Energy", "Inference Time",
        "Training Loss", "FLOPs vs SynOps", "Radar",
    ])

    with tab1:
        st.plotly_chart(accuracy_bar(ann, snn),       use_container_width=True)
    with tab2:
        st.plotly_chart(energy_bar(ann, snn),          use_container_width=True)
    with tab3:
        st.plotly_chart(inference_time_bar(ann, snn),  use_container_width=True)
    with tab4:
        st.plotly_chart(training_loss_line(ann, snn),  use_container_width=True)
    with tab5:
        st.plotly_chart(flops_synops_bar(ann, snn),    use_container_width=True)
    with tab6:
        st.plotly_chart(radar_chart(ann, snn),         use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    render_conclusion(ann, snn)
