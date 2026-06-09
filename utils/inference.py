"""
utils/inference.py
Placeholder inference hooks for ANN and SNN models.
Replace the body of each function with real model calls when ready.
"""

import random
import time
from typing import Tuple, Dict, Any

import numpy as np


def preprocess_image(image) -> np.ndarray:
    """
    Convert a PIL Image to a normalised 28x28 numpy array.
    Replace with your actual preprocessing pipeline.
    """
    img = image.convert("L").resize((28, 28))
    arr = np.array(img, dtype=np.float32) / 255.0
    return arr.flatten()


def run_ann_inference(image) -> Dict[str, Any]:
    """
    ANN Inference Hook
    TODO: Load your trained ANN model and replace the mock below.

    Expected return shape:
        {
            "digit":          int   - predicted class 0-9
            "confidence":     float - softmax probability of top class
            "inference_time": float - milliseconds
            "energy_est":     float - relative energy units
        }
    """
    _ = preprocess_image(image)          # keep preprocessing wired up
    time.sleep(0.05)                      # simulate latency

    digit = random.randint(0, 9)
    confidence = round(random.uniform(0.88, 0.99), 4)
    inference_time = round(random.uniform(10, 15), 2)
    energy_est = round(random.uniform(110, 130), 2)

    return {
        "digit": digit,
        "confidence": confidence,
        "inference_time": inference_time,
        "energy_est": energy_est,
    }


def run_snn_inference(image) -> Dict[str, Any]:
    """
    SNN Inference Hook
    TODO: Load your trained SNN model (e.g. via snnTorch / Brian2) and
    replace the mock below.

    Expected return shape:
        {
            "digit":          int   - predicted class 0-9
            "confidence":     float - spike-rate confidence score
            "inference_time": float - milliseconds
            "energy_est":     float - relative energy units
            "spike_rate":     float - average spikes per neuron per timestep
        }
    """
    _ = preprocess_image(image)
    time.sleep(0.03)

    digit = random.randint(0, 9)
    confidence = round(random.uniform(0.85, 0.98), 4)
    inference_time = round(random.uniform(5, 9), 2)
    energy_est = round(random.uniform(15, 25), 2)
    spike_rate = round(random.uniform(0.03, 0.06), 4)

    return {
        "digit": digit,
        "confidence": confidence,
        "inference_time": inference_time,
        "energy_est": energy_est,
        "spike_rate": spike_rate,
    }
