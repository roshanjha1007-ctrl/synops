# synops - ANN vs SNN MNIST Dashboard

> Energy-Efficient MNIST Classification

A production-quality **Streamlit** dashboard that benchmarks Artificial Neural Networks (ANN) against Spiking Neural Networks (SNN) on the MNIST handwritten-digit dataset, with a focus on **energy consumption**, inference latency, and computational cost.

---

## Quick Start

```bash
# 1. Clone / unzip the project
cd rsynops

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run app.py
```

---

## Project Structure

```
rsynops/
|-- app.py                    # Main Streamlit entry point
|-- requirements.txt
|-- README.md
|
|-- data/
|   |-- results_ann.json      # ANN benchmark results
|   `-- results_snn.json      # SNN benchmark results
|
|-- components/
|   |-- __init__.py
|   |-- hero.py               # Glassmorphism hero banner
|   |-- metrics_panel.py      # Side-by-side metric cards
|   |-- kpi_cards.py          # Top KPI summary strip
|   |-- charts.py             # All Plotly chart factories
|   |-- architecture.py       # Pipeline architecture viz
|   |-- upload_panel.py       # Image upload + inference UI
|   |-- results_table.py      # Comparison DataFrame table
|   `-- conclusion.py         # Insights / conclusion block
|
`-- utils/
    |-- __init__.py
    |-- data_loader.py        # JSON loader with fallback mocks
    |-- inference.py          # ANN / SNN inference hooks
    `-- styles.py             # Global CSS + colour tokens
```

---

## Connecting Real Models

Edit **`utils/inference.py`**:

```python
def run_ann_inference(image) -> Dict[str, Any]:
    # TODO: load your trained ANN, run forward pass
    ...

def run_snn_inference(image) -> Dict[str, Any]:
    # TODO: load your SNN (snnTorch / Brian2), run spike sim
    ...
```

Both functions receive a **PIL Image** and must return the dict shape shown in the docstring.

---

## Data Format

**`data/results_ann.json`**
```json
{
  "accuracy": 97.5,
  "flops": 1234567,
  "energy": 120,
  "inference_time": 12,
  "training_loss": [2.31, 1.85, ...]
}
```

**`data/results_snn.json`**
```json
{
  "accuracy": 96.8,
  "synops": 245000,
  "energy": 20,
  "inference_time": 7,
  "training_loss": [2.29, 1.90, ...]
}
```

The dashboard **never crashes** - if JSON files are missing or malformed, mock data is used automatically.

---

## Tech Stack

| Layer | Library |
|-------|---------|
| UI Framework | Streamlit |
| Charts | Plotly |
| Data | Pandas, NumPy |
| Image | Pillow |
| Styling | Custom CSS (Glassmorphism, Orbitron font) |

---

## Team synops 
