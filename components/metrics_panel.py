"""
components/metrics_panel.py
Side-by-side ANN vs SNN metric cards.
"""

import streamlit as st
from typing import Dict, Any

from utils import lucide_icon


def _card(label: str, value: str, sub: str, color: str, icon: str = "") -> str:
    icon_svg = lucide_icon(icon, 15, color) if icon else ""
    gap = "6px" if icon_svg else "0"
    return f"""
    <div style="
        background: rgba(255,255,255,0.03);
        border: 1px solid {color}33;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 10px;
        transition: all .25s;
        backdrop-filter: blur(10px);
    " onmouseover="this.style.borderColor='{color}88';this.style.boxShadow='0 0 18px {color}22'"
       onmouseout="this.style.borderColor='{color}33';this.style.boxShadow='none'">
        <div style="
            display:inline-flex; align-items:center; gap:{gap};
            font-family:'Space Mono',monospace;
            font-size:0.62rem; color:#8899aa;
            letter-spacing:.1em; text-transform:uppercase;
            margin-bottom:6px;
        ">{icon_svg}<span>{label}</span></div>
        <div style="
            font-family:'Orbitron',monospace;
            font-size:1.45rem; font-weight:700;
            color:{color}; line-height:1;
            margin-bottom:4px;
        ">{value}</div>
        <div style="font-family:'Inter',sans-serif;font-size:0.72rem;color:#6b7280;">{sub}</div>
    </div>
    """


def render_metrics_panel(ann: Dict[str, Any], snn: Dict[str, Any]) -> None:
    """Render side-by-side ANN / SNN metric cards."""

    col_ann, col_snn = st.columns(2, gap="medium")

    with col_ann:
        st.markdown("""
        <div style="
            font-family:'Orbitron',monospace; font-size:0.8rem; font-weight:700;
            color:#00f5ff; letter-spacing:.12em; text-transform:uppercase;
            border-bottom:1px solid rgba(0,245,255,0.2);
            padding-bottom:10px; margin-bottom:14px;
        ">ANN - Artificial Neural Network</div>
        """, unsafe_allow_html=True)

        html = ""
        html += _card("Accuracy",       f"{ann['accuracy']}%",
                      "Test set top-1", "#00f5ff", "target")
        html += _card("FLOPs",          f"{ann['flops']:,}",
                      "Floating-point ops / inference", "#00f5ff", "cpu")
        html += _card("Inference Time", f"{ann['inference_time']} ms",
                      "Single-sample latency", "#00f5ff", "timer")
        html += _card("Energy",         f"{ann['energy']} mJ",
                      "Estimated per inference", "#ff9f0a", "battery")
        st.markdown(html, unsafe_allow_html=True)

    with col_snn:
        st.markdown("""
        <div style="
            font-family:'Orbitron',monospace; font-size:0.8rem; font-weight:700;
            color:#bf5af2; letter-spacing:.12em; text-transform:uppercase;
            border-bottom:1px solid rgba(191,90,242,0.2);
            padding-bottom:10px; margin-bottom:14px;
        ">SNN - Spiking Neural Network</div>
        """, unsafe_allow_html=True)

        html = ""
        html += _card("Accuracy",       f"{snn['accuracy']}%",
                      "Test set top-1", "#bf5af2", "target")
        html += _card("SynOps",         f"{snn['synops']:,}",
                      "Synaptic operations / inference", "#bf5af2", "activity")
        html += _card("Inference Time", f"{snn['inference_time']} ms",
                      "Single-sample latency", "#bf5af2", "timer")
        html += _card("Energy",         f"{snn['energy']} mJ",
                      "Estimated per inference", "#30d158", "battery-charging")
        st.markdown(html, unsafe_allow_html=True)
