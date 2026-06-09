"""
utils/data_loader.py
Handles loading and fallback for ANN/SNN result JSON files.
"""

import json
import os
from typing import Dict, Any


# Fallback mock data
DEFAULT_ANN: Dict[str, Any] = {
    "accuracy": 97.5,
    "flops": 1_234_567,
    "energy": 120,
    "inference_time": 12,
    "training_loss": [2.31, 1.85, 1.42, 1.10, 0.85, 0.67, 0.54, 0.44, 0.37, 0.31],
    "model_name": "ANN (MLP)",
    "layers": 4,
    "parameters": 407_050,
    "batch_size": 64,
    "epochs": 10,
}

DEFAULT_SNN: Dict[str, Any] = {
    "accuracy": 96.8,
    "synops": 245_000,
    "energy": 20,
    "inference_time": 7,
    "training_loss": [2.29, 1.90, 1.55, 1.25, 1.01, 0.82, 0.68, 0.57, 0.49, 0.43],
    "model_name": "SNN (Spiking MLP)",
    "layers": 4,
    "parameters": 407_050,
    "batch_size": 64,
    "epochs": 10,
    "timesteps": 25,
    "threshold": 0.5,
    "spike_rate": 0.042,
}


def load_json(path: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
    """Load a JSON file; return fallback dict if missing or malformed."""
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
            # Merge fallback so missing keys never cause KeyErrors
            return {**fallback, **data}
    except (json.JSONDecodeError, OSError):
        pass
    return fallback.copy()


def load_ann_results(base_dir: str = "data") -> Dict[str, Any]:
    return load_json(os.path.join(base_dir, "results_ann.json"), DEFAULT_ANN)


def load_snn_results(base_dir: str = "data") -> Dict[str, Any]:
    return load_json(os.path.join(base_dir, "results_snn.json"), DEFAULT_SNN)
