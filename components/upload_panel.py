"""
components/upload_panel.py
Image upload + live ANN / SNN prediction panel.
"""

import streamlit as st
from PIL import Image
from typing import Dict, Any


def _result_card(model: str, color: str, result: Dict[str, Any]) -> str:
    digit      = result.get("digit", "?")
    conf       = result.get("confidence", 0)
    inf_time   = result.get("inference_time", 0)
    energy     = result.get("energy_est", 0)
    spike_rate = result.get("spike_rate")

    extra = ""
    if spike_rate is not None:
        extra = f"""
        <div style="display:flex;justify-content:space-between;margin-top:6px;">
            <span style="font-size:0.7rem;color:#8899aa;">Spike Rate</span>
            <span style="font-size:0.7rem;color:{color};font-family:'Space Mono',monospace;">{spike_rate:.4f}</span>
        </div>"""

    return f"""
    <div style="
        background: rgba(255,255,255,0.03);
        border: 1px solid {color}44;
        border-radius: 16px;
        padding: 22px 20px;
        text-align: center;
    ">
        <div style="
            font-family:'Orbitron',monospace; font-size:0.7rem;
            color:{color}; letter-spacing:.12em; text-transform:uppercase;
            margin-bottom:14px;
        ">{model}</div>
        <div style="
            font-family:'Orbitron',monospace; font-size:4rem; font-weight:900;
            color:{color}; line-height:1; margin-bottom:6px;
        ">{digit}</div>
        <div style="font-size:0.75rem;color:#8899aa;margin-bottom:16px;">
            Predicted Digit
        </div>
        <div style="
            background:{color}18; border:1px solid {color}33;
            border-radius:8px; padding:8px 14px; margin-bottom:10px;
        ">
            <div style="font-size:0.65rem;color:#8899aa;text-transform:uppercase;letter-spacing:.08em;">Confidence</div>
            <div style="font-family:'Orbitron',monospace;font-size:1.2rem;color:{color};">{conf*100:.1f}%</div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:4px;">
            <span style="font-size:0.7rem;color:#8899aa;">Latency</span>
            <span style="font-size:0.7rem;color:{color};font-family:'Space Mono',monospace;">{inf_time} ms</span>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:6px;">
            <span style="font-size:0.7rem;color:#8899aa;">Energy Est.</span>
            <span style="font-size:0.7rem;color:{color};font-family:'Space Mono',monospace;">{energy} mJ</span>
        </div>
        {extra}
    </div>
    """


def render_upload_panel() -> None:
    from utils.inference import run_ann_inference, run_snn_inference

    st.markdown("""
    <div style="
        font-family:'Orbitron',monospace; font-size:0.8rem; font-weight:700;
        color:#e2e8f0; letter-spacing:.1em; text-transform:uppercase;
        margin-bottom:18px;
    ">Live Prediction - Upload a Digit</div>
    """, unsafe_allow_html=True)

    col_upload, col_preview, col_results = st.columns([3, 2, 4], gap="medium")

    with col_upload:
        uploaded = st.file_uploader(
            "Upload handwritten digit (PNG / JPG)",
            type=["png", "jpg", "jpeg"],
            key="digit_upload",
        )
        run_btn = st.button("Run Inference", use_container_width=True)

    with col_preview:
        if uploaded:
            img = Image.open(uploaded)
            st.image(img, caption="Uploaded digit", use_container_width=True)
        else:
            st.markdown("""
            <div style="
                background: rgba(255,255,255,0.02);
                border: 1px dashed rgba(0,245,255,0.2);
                border-radius: 12px;
                height: 140px;
                display: flex; align-items: center; justify-content: center;
                color: #4b5563;
                font-family: 'Space Mono', monospace;
                font-size: 0.7rem;
            ">No image yet</div>
            """, unsafe_allow_html=True)

    with col_results:
        if run_btn and uploaded:
            img = Image.open(uploaded)
            with st.spinner("Running ANN..."):
                ann_res = run_ann_inference(img)
            with st.spinner("Running SNN..."):
                snn_res = run_snn_inference(img)

            r1, r2 = st.columns(2, gap="small")
            with r1:
                st.markdown(_result_card("ANN", "#00f5ff", ann_res),
                            unsafe_allow_html=True)
            with r2:
                st.markdown(_result_card("SNN", "#bf5af2", snn_res),
                            unsafe_allow_html=True)
        elif run_btn and not uploaded:
            st.warning("Please upload an image first.")
        else:
            st.markdown("""
            <div style="
                background: rgba(255,255,255,0.02);
                border: 1px dashed rgba(191,90,242,0.2);
                border-radius: 12px;
                height: 140px;
                display: flex; align-items: center; justify-content: center;
                color: #4b5563;
                font-family: 'Space Mono', monospace;
                font-size: 0.7rem;
                text-align: center; padding: 20px;
            ">Upload an image and<br>click Run Inference</div>
            """, unsafe_allow_html=True)
