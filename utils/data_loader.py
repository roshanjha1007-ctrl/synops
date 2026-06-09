"""
utils/data_loader.py
Handles loading and fallback for ANN/SNN result JSON files.
"""

import json
import os
from typing import Any, Callable, Dict, Optional


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


def _percent(value: Any) -> Any:
    """Convert fractional accuracies to percentages while preserving percent values."""
    if not isinstance(value, (int, float)):
        return value
    return round(value * 100, 2) if value <= 1 else round(value, 2)


def _ann_from_training_log(data: Dict[str, Any], fallback: Dict[str, Any]) -> Dict[str, Any]:
    """Map ANN training logs into the dashboard schema."""
    result = {**fallback, **data}
    history = data.get("history") or []

    if history:
        result["training_loss"] = [
            row["train_loss"] for row in history if "train_loss" in row
        ]
        val_accs = [row["val_acc"] for row in history if "val_acc" in row]
        if val_accs:
            result["accuracy"] = _percent(data.get("best_val_acc", max(val_accs)))

    if "best_val_acc" in data:
        result["accuracy"] = _percent(data["best_val_acc"])

    if "model" in data:
        result["model_name"] = data["model"]

    return result


def _snn_from_training_log(data: Dict[str, Any], fallback: Dict[str, Any]) -> Dict[str, Any]:
    """Map SNN training logs into the dashboard schema."""
    result = {**fallback, **data}
    logs = data.get("epoch_logs") or []

    if logs:
        result["training_loss"] = [row["loss"] for row in logs if "loss" in row]
        test_accs = [row["test_accuracy"] for row in logs if "test_accuracy" in row]
        if test_accs:
            result["accuracy"] = _percent(data.get("final_test_accuracy", max(test_accs)))

    if "final_test_accuracy" in data:
        result["accuracy"] = _percent(data["final_test_accuracy"])
    if "avg_synops" in data:
        result["synops"] = round(data["avg_synops"], 2)
    if "num_steps" in data:
        result["timesteps"] = data["num_steps"]
    if "hidden_size" in data:
        result["layers"] = f"Input, hidden {data['hidden_size']}, output"
    if "final_train_accuracy" in data:
        result["train_accuracy"] = _percent(data["final_train_accuracy"])

    result["model_name"] = data.get("model_name", "SNN (Spiking MLP)")
    return result


def load_json(
    path: str,
    fallback: Dict[str, Any],
    normalizer: Optional[Callable[[Dict[str, Any], Dict[str, Any]], Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Load a JSON file; return fallback dict if missing or malformed."""
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
            if normalizer:
                return normalizer(data, fallback)
            return {**fallback, **data}
    except (json.JSONDecodeError, OSError):
        pass
    return fallback.copy()


def load_ann_results(base_dir: str = "data") -> Dict[str, Any]:
    return load_json(
        os.path.join(base_dir, "results_ann.json"),
        DEFAULT_ANN,
        _ann_from_training_log,
    )


def load_snn_results(base_dir: str = "data") -> Dict[str, Any]:
    return load_json(
        os.path.join(base_dir, "results_snn.json"),
        DEFAULT_SNN,
        _snn_from_training_log,
    )
