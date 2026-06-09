"""
components/architecture.py
ASCII/HTML architecture pipeline visualization.
"""

import streamlit as st


def _pipeline(title: str, color: str, steps: list, bg: str) -> str:
    step_html = ""
    for i, s in enumerate(steps):
        arrow = "" if i == len(steps) - 1 else f"""
        <div style="text-align:center;color:{color};font-size:1.1rem;line-height:1.2;margin:0;">v</div>
        """
        step_html += f"""
        <div style="
            background: {bg};
            border: 1px solid {color}33;
            border-radius: 10px;
            padding: 10px 16px;
            text-align: center;
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            color: #e2e8f0;
            letter-spacing: .04em;
        ">{s}</div>
        {arrow}
        """
    return f"""
    <div style="
        background: rgba(255,255,255,0.02);
        border: 1px solid {color}22;
        border-radius: 16px;
        padding: 24px 20px;
        height: 100%;
    ">
        <div style="
            font-family:'Orbitron',monospace;
            font-size:0.78rem; font-weight:700;
            color:{color};
            letter-spacing:.1em; text-transform:uppercase;
            text-align:center;
            margin-bottom:20px;
        ">{title}</div>
        {step_html}
    </div>
    """


def render_architecture() -> None:
    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:0.8rem; font-weight:700;
        color:#e2e8f0; letter-spacing:.1em; text-transform:uppercase;
        margin-bottom:18px;
    ">Architecture Pipelines</div>
    """, unsafe_allow_html=True)

    col_ann, col_mid, col_snn = st.columns([5, 1, 5], gap="small")

    ann_steps = [
        "MNIST Input (28x28)",
        "Flatten to 784-dim vector",
        "Dense Layer 1 (512) + ReLU",
        "Dense Layer 2 (256) + ReLU",
        "Dense Layer 3 (128) + ReLU",
        "Output Layer (10) + Softmax",
        "Predicted Digit",
    ]

    snn_steps = [
        "MNIST Input (28x28)",
        "Rate Encoding to Spike Trains",
        "LIF Layer 1 (512 neurons)",
        "LIF Layer 2 (256 neurons)",
        "LIF Layer 3 (128 neurons)",
        "Output Spike Count (10 classes)",
        "Predicted Digit",
    ]

    with col_ann:
        st.markdown(_pipeline("ANN Pipeline", "#00f5ff", ann_steps, "rgba(0,245,255,0.04)"),
                    unsafe_allow_html=True)

    with col_mid:
        st.markdown("""
        <div style="
            display:flex; flex-direction:column; align-items:center;
            justify-content:center; height:100%; padding-top:120px;
        ">
            <div style="font-size:1.4rem; color:#6b7280;">vs</div>
            <div style="
                font-family:'Space Mono',monospace;
                font-size:0.55rem; color:#4b5563;
                writing-mode:vertical-lr;
                text-transform:uppercase; letter-spacing:.1em;
                margin-top:8px;
            ">vs</div>
        </div>
        """, unsafe_allow_html=True)

    with col_snn:
        st.markdown(_pipeline("SNN Pipeline", "#bf5af2", snn_steps, "rgba(191,90,242,0.04)"),
                    unsafe_allow_html=True)
