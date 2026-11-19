# ComfyUI Sadstag Nodes

A collection of custom utility nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

---

## Nodes Included

### GPU Total VRAM
Detects total GPU VRAM and compares it against a defined threshold. Ideal for branching workflows, adaptive batch sizing, or dynamic model/precision selection based on available system hardware.

- **Category**: `utils/system`
- **Inputs**:
  - `threshold_gb_1` (*FLOAT*, default: `24.0`, min: `0.0`, max: `384.0`, step: `8`): First threshold in GB.
  - `threshold_gb_2` (*FLOAT*, default: `32.0`, min: `0.0`, max: `384.0`, step: `8`): Second threshold in GB.
  - `threshold_gb_3` (*FLOAT*, default: `48.0`, min: `0.0`, max: `384.0`, step: `8`): Third threshold in GB.
- **Outputs**:
  - `vram_gb` (*INT*): Total detected GPU VRAM rounded to the nearest integer (e.g. `12`, `16`, `24`).
  - `vram_gb_exact` (*FLOAT*): Total detected GPU VRAM in GB rounded to 2 decimal places (e.g. `11.76`).
  - `at_least_threshold_1` (*BOOLEAN*): `True` if total VRAM >= `threshold_gb_1`.
  - `at_least_threshold_2` (*BOOLEAN*): `True` if total VRAM >= `threshold_gb_2`.
  - `at_least_threshold_3` (*BOOLEAN*): `True` if total VRAM >= `threshold_gb_3`.

---

## Installation

### Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/sadstag/comfyui-sadstag-nodes.git
   ```
3. Restart ComfyUI.

> [!NOTE]
> **No extra dependencies required!** This node uses built-in ComfyUI and PyTorch utilities.

---

## Usage
- Double-click anywhere on the ComfyUI canvas and search for **`GPU Total VRAM`**.
- Or right-click: **Add Node** &rarr; **`utils`** &rarr; **`system`** &rarr; **`GPU Total VRAM`**.

---

## License
MIT License
