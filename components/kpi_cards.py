"""
components/kpi_cards.py
Top-level KPI summary strip.
"""

import streamlit as st
from typing import Dict, Any


def render_kpi_cards(ann: Dict[str, Any], snn: Dict[str, Any]) -> None:
    energy_saved = round((1 - snn["energy"] / ann["energy"]) * 100, 1)
    speed_diff   = round(ann["inference_time"] - snn["inference_time"], 1)
    comp_red     = round((1 - snn["synops"] / ann["flops"]) * 100, 1)
    acc_diff     = round(ann["accuracy"] - snn["accuracy"], 1)

    c1, c2, c3, c4, c5 = st.columns(5, gap="small")

    with c1:
        st.metric("ANN Accuracy",  f"{ann['accuracy']}%",
                  delta=None)
    with c2:
        st.metric("SNN Accuracy",  f"{snn['accuracy']}%",
                  delta=f"-{acc_diff}% vs ANN", delta_color="off")
    with c3:
        st.metric("Energy Saved",  f"{energy_saved}%",
                  delta="SNN wins", delta_color="normal")
    with c4:
        st.metric("Speed Gain",    f"{speed_diff} ms faster",
                  delta="SNN faster", delta_color="normal")
    with c5:
        st.metric("Comp. Reduction", f"{comp_red}%",
                  delta="SNN ops", delta_color="normal")
