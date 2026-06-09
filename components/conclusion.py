"""
components/conclusion.py
Conclusion / insight section for rsynops dashboard.
"""

import streamlit as st
from typing import Dict, Any


def render_conclusion(ann: Dict[str, Any], snn: Dict[str, Any]) -> None:
    energy_saved = round((1 - snn["energy"] / ann["energy"]) * 100, 1)
    acc_diff     = round(ann["accuracy"] - snn["accuracy"], 1)
    speed_diff   = round(ann["inference_time"] - snn["inference_time"], 1)
    comp_red     = round((1 - snn["synops"] / ann["flops"]) * 100, 1)

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg,
            rgba(191,90,242,0.07) 0%,
            rgba(0,245,255,0.05) 50%,
            rgba(48,209,88,0.05) 100%);
        border: 1px solid rgba(191,90,242,0.25);
        border-radius: 20px;
        padding: 40px 36px;
        margin-top: 8px;
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position:absolute; top:-40px; right:-40px;
            width:200px; height:200px;
            background: radial-gradient(circle, rgba(191,90,242,0.12), transparent 70%);
            border-radius:50%; pointer-events:none;
        "></div>

        <div style="
            font-family:'Orbitron',monospace; font-size:0.7rem;
            color:#bf5af2; letter-spacing:.15em; text-transform:uppercase;
            margin-bottom:14px;
        ">Conclusion</div>

        <h2 style="
            font-family:'Orbitron',monospace;
            font-size:clamp(1.1rem,2.5vw,1.6rem);
            font-weight:700;
            color:#e2e8f0;
            line-height:1.4;
            margin-bottom:20px;
            max-width:700px;
        ">
            Spiking Neural Networks achieve
            <span style="color:#bf5af2;">comparable accuracy</span> while
            <span style="color:#30d158;">significantly reducing energy consumption.</span>
        </h2>

        <p style="
            font-family:'Inter',sans-serif;
            font-size:0.95rem; color:#94a3b8;
            line-height:1.8; max-width:740px;
            margin-bottom:28px;
        ">
            Our experiments on MNIST demonstrate that SNNs deliver only a
            <strong style="color:#e2e8f0;">{acc_diff}% accuracy drop</strong> compared to
            conventional ANNs, while consuming <strong style="color:#30d158;">{energy_saved}% less energy</strong>,
            running <strong style="color:#00f5ff;">{speed_diff} ms faster</strong> per inference,
            and reducing synaptic compute by <strong style="color:#bf5af2;">{comp_red}%</strong>.
            For edge and IoT deployments where power budgets are constrained,
            neuromorphic computing via SNNs offers a compelling, sustainable path forward.
        </p>

        <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <div style="
                background:rgba(48,209,88,0.08);
                border:1px solid rgba(48,209,88,0.25);
                border-radius:10px; padding:12px 20px; min-width:130px;
            ">
                <div style="font-family:'Space Mono',monospace;font-size:0.6rem;color:#8899aa;text-transform:uppercase;letter-spacing:.1em;">Energy Saved</div>
                <div style="font-family:'Orbitron',monospace;font-size:1.4rem;font-weight:700;color:#30d158;">{energy_saved}%</div>
            </div>
            <div style="
                background:rgba(0,245,255,0.08);
                border:1px solid rgba(0,245,255,0.25);
                border-radius:10px; padding:12px 20px; min-width:130px;
            ">
                <div style="font-family:'Space Mono',monospace;font-size:0.6rem;color:#8899aa;text-transform:uppercase;letter-spacing:.1em;">Faster Inference</div>
                <div style="font-family:'Orbitron',monospace;font-size:1.4rem;font-weight:700;color:#00f5ff;">{speed_diff} ms</div>
            </div>
            <div style="
                background:rgba(191,90,242,0.08);
                border:1px solid rgba(191,90,242,0.25);
                border-radius:10px; padding:12px 20px; min-width:130px;
            ">
                <div style="font-family:'Space Mono',monospace;font-size:0.6rem;color:#8899aa;text-transform:uppercase;letter-spacing:.1em;">Comp. Reduction</div>
                <div style="font-family:'Orbitron',monospace;font-size:1.4rem;font-weight:700;color:#bf5af2;">{comp_red}%</div>
            </div>
            <div style="
                background:rgba(255,159,10,0.08);
                border:1px solid rgba(255,159,10,0.25);
                border-radius:10px; padding:12px 20px; min-width:130px;
            ">
                <div style="font-family:'Space Mono',monospace;font-size:0.6rem;color:#8899aa;text-transform:uppercase;letter-spacing:.1em;">Acc. Parity</div>
                <div style="font-family:'Orbitron',monospace;font-size:1.4rem;font-weight:700;color:#ff9f0a;">-{acc_diff}%</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
