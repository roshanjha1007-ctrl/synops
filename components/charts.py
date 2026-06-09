"""
components/charts.py
Reusable Plotly chart factory functions.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import Dict, Any, List

from utils.styles import PLOTLY_TEMPLATE, CYAN, PURPLE, GREEN, ORANGE

# Shared layout defaults
_LAYOUT = dict(
    template=PLOTLY_TEMPLATE,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Space Mono, monospace", color="#8899aa", size=11),
    margin=dict(l=10, r=10, t=40, b=10),
    legend=dict(
        bgcolor="rgba(10,14,26,0.6)",
        bordercolor="rgba(0,245,255,0.15)",
        borderwidth=1,
    ),
)


def _apply(fig: go.Figure, title: str = "") -> go.Figure:
    kw = dict(**_LAYOUT)
    if title:
        kw["title"] = dict(
            text=title,
            font=dict(family="Orbitron, monospace", color="#e2e8f0", size=14),
            x=0.02, xanchor="left",
        )
    fig.update_layout(**kw)
    fig.update_xaxes(gridcolor="rgba(255,255,255,0.05)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(255,255,255,0.05)", zeroline=False)
    return fig


# Individual charts

def accuracy_bar(ann: Dict, snn: Dict) -> go.Figure:
    fig = go.Figure([
        go.Bar(name="ANN", x=["Accuracy (%)"], y=[ann["accuracy"]],
               marker=dict(color=CYAN, opacity=0.85,
                           line=dict(color=CYAN, width=1.5)),
               text=[f"{ann['accuracy']}%"], textposition="outside",
               textfont=dict(color=CYAN, family="Orbitron, monospace")),
        go.Bar(name="SNN", x=["Accuracy (%)"], y=[snn["accuracy"]],
               marker=dict(color=PURPLE, opacity=0.85,
                           line=dict(color=PURPLE, width=1.5)),
               text=[f"{snn['accuracy']}%"], textposition="outside",
               textfont=dict(color=PURPLE, family="Orbitron, monospace")),
    ])
    fig.update_layout(barmode="group", yaxis_range=[90, 100])
    return _apply(fig, "Accuracy Comparison")


def energy_bar(ann: Dict, snn: Dict) -> go.Figure:
    categories = ["Energy (mJ)"]
    fig = go.Figure([
        go.Bar(name="ANN", x=categories, y=[ann["energy"]],
               marker=dict(color=ORANGE, opacity=0.85,
                           line=dict(color=ORANGE, width=1.5)),
               text=[f"{ann['energy']} mJ"], textposition="outside",
               textfont=dict(color=ORANGE, family="Orbitron, monospace")),
        go.Bar(name="SNN", x=categories, y=[snn["energy"]],
               marker=dict(color=GREEN, opacity=0.85,
                           line=dict(color=GREEN, width=1.5)),
               text=[f"{snn['energy']} mJ"], textposition="outside",
               textfont=dict(color=GREEN, family="Orbitron, monospace")),
    ])
    fig.update_layout(barmode="group")
    return _apply(fig, "Energy Consumption (mJ)")


def inference_time_bar(ann: Dict, snn: Dict) -> go.Figure:
    fig = go.Figure([
        go.Bar(name="ANN", x=["Inference Time (ms)"], y=[ann["inference_time"]],
               marker=dict(color=CYAN, opacity=0.8,
                           line=dict(color=CYAN, width=1.5)),
               text=[f"{ann['inference_time']} ms"], textposition="outside",
               textfont=dict(color=CYAN, family="Orbitron, monospace")),
        go.Bar(name="SNN", x=["Inference Time (ms)"], y=[snn["inference_time"]],
               marker=dict(color=PURPLE, opacity=0.8,
                           line=dict(color=PURPLE, width=1.5)),
               text=[f"{snn['inference_time']} ms"], textposition="outside",
               textfont=dict(color=PURPLE, family="Orbitron, monospace")),
    ])
    fig.update_layout(barmode="group")
    return _apply(fig, "Inference Time (ms)")


def training_loss_line(ann: Dict, snn: Dict) -> go.Figure:
    epochs = list(range(1, len(ann["training_loss"]) + 1))
    fig = go.Figure([
        go.Scatter(x=epochs, y=ann["training_loss"], name="ANN Loss",
                   line=dict(color=CYAN, width=2.5),
                   mode="lines+markers",
                   marker=dict(size=5, color=CYAN)),
        go.Scatter(x=epochs, y=snn["training_loss"], name="SNN Loss",
                   line=dict(color=PURPLE, width=2.5, dash="dot"),
                   mode="lines+markers",
                   marker=dict(size=5, color=PURPLE)),
    ])
    fig.update_xaxes(title_text="Epoch", title_font=dict(color="#8899aa"))
    fig.update_yaxes(title_text="Loss",  title_font=dict(color="#8899aa"))
    return _apply(fig, "Training Loss Curve")


def flops_synops_bar(ann: Dict, snn: Dict) -> go.Figure:
    fig = go.Figure([
        go.Bar(name="ANN FLOPs", x=["Computational Ops"], y=[ann["flops"]],
               marker=dict(color=CYAN, opacity=0.85,
                           line=dict(color=CYAN, width=1.5))),
        go.Bar(name="SNN SynOps", x=["Computational Ops"], y=[snn["synops"]],
               marker=dict(color=PURPLE, opacity=0.85,
                           line=dict(color=PURPLE, width=1.5))),
    ])
    fig.update_layout(barmode="group")
    fig.update_yaxes(title_text="Operations", title_font=dict(color="#8899aa"))
    return _apply(fig, "FLOPs vs SynOps")


def radar_chart(ann: Dict, snn: Dict) -> go.Figure:
    """Normalised radar of key metrics."""
    categories = ["Accuracy", "Energy Eff.", "Speed", "Comp. Eff.", "Overall"]

    ann_energy_eff = round((1 - ann["energy"] / 150) * 100, 1)
    snn_energy_eff = round((1 - snn["energy"] / 150) * 100, 1)
    ann_speed      = round((1 - ann["inference_time"] / 20) * 100, 1)
    snn_speed      = round((1 - snn["inference_time"] / 20) * 100, 1)
    ann_comp       = round((1 - ann["flops"] / 2_000_000) * 100, 1)
    snn_comp       = round((1 - snn["synops"] / 1_500_000) * 100, 1)

    ann_vals = [ann["accuracy"], ann_energy_eff, ann_speed, ann_comp,
                round(np.mean([ann["accuracy"], ann_energy_eff, ann_speed, ann_comp]), 1)]
    snn_vals = [snn["accuracy"], snn_energy_eff, snn_speed, snn_comp,
                round(np.mean([snn["accuracy"], snn_energy_eff, snn_speed, snn_comp]), 1)]

    fig = go.Figure([
        go.Scatterpolar(r=ann_vals + [ann_vals[0]], theta=categories + [categories[0]],
                        name="ANN", fill="toself",
                        line=dict(color=CYAN, width=2),
                        fillcolor=f"{CYAN}22"),
        go.Scatterpolar(r=snn_vals + [snn_vals[0]], theta=categories + [categories[0]],
                        name="SNN", fill="toself",
                        line=dict(color=PURPLE, width=2),
                        fillcolor=f"{PURPLE}22"),
    ])
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 105],
                            gridcolor="rgba(255,255,255,0.07)",
                            tickfont=dict(color="#8899aa", size=9)),
            angularaxis=dict(gridcolor="rgba(255,255,255,0.07)",
                             tickfont=dict(color="#e2e8f0", size=10)),
        ),
    )
    return _apply(fig, "Performance Radar")
