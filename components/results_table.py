"""
components/results_table.py
Professional comparison table rendered with Pandas + Streamlit.
"""

import streamlit as st
import pandas as pd
from typing import Dict, Any


def render_results_table(ann: Dict[str, Any], snn: Dict[str, Any]) -> None:
    energy_saved = round((1 - snn["energy"] / ann["energy"]) * 100, 1)
    speed_diff   = round(ann["inference_time"] - snn["inference_time"], 1)

    df = pd.DataFrame([
        {
            "Model":              "ANN (MLP)",
            "Accuracy":           f"{ann['accuracy']}%",
            "Energy (mJ)":        f"{ann['energy']} mJ",
            "Inference Time":     f"{ann['inference_time']} ms",
            "Comp. Cost":         f"{ann['flops']:,} FLOPs",
            "Layers":             ann.get("layers", "-"),
            "Parameters":         f"{ann.get('parameters', 0):,}",
        },
        {
            "Model":              "SNN (Spiking MLP)",
            "Accuracy":           f"{snn['accuracy']}%",
            "Energy (mJ)":        f"{snn['energy']} mJ",
            "Inference Time":     f"{snn['inference_time']} ms",
            "Comp. Cost":         f"{snn['synops']:,} SynOps",
            "Layers":             snn.get("layers", "-"),
            "Parameters":         f"{snn.get('parameters', 0):,}",
        },
        {
            "Model":              "Advantage (SNN)",
            "Accuracy":           f"-{round(ann['accuracy']-snn['accuracy'],1)}%",
            "Energy (mJ)":        f"Down {energy_saved}%",
            "Inference Time":     f"Down {speed_diff} ms",
            "Comp. Cost":         f"Down {round((1-snn['synops']/ann['flops'])*100,1)}%",
            "Layers":             "-",
            "Parameters":         "-",
        },
    ])

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )
