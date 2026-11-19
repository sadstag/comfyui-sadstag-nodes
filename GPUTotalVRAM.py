import comfy.model_management as mm


class GPUTotalVRAM:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "threshold_gb_1": (
                    "FLOAT",
                    {"default": 24.0, "min": 0.0, "max": 384.0, "step": 8},
                ),
                "threshold_gb_2": (
                    "FLOAT",
                    {"default": 32.0, "min": 0.0, "max": 384.0, "step": 8},
                ),
                "threshold_gb_3": (
                    "FLOAT",
                    {"default": 48.0, "min": 0.0, "max": 384.0, "step": 8},
                ),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "BOOLEAN", "BOOLEAN", "BOOLEAN")
    RETURN_NAMES = (
        "vram_gb",
        "vram_gb_exact",
        "at_least_threshold_1",
        "at_least_threshold_2",
        "at_least_threshold_3",
    )
    FUNCTION = "run"
    CATEGORY = "sadstag"

    def run(self, threshold_gb_1, threshold_gb_2, threshold_gb_3):
        dev = mm.get_torch_device()
        if dev.type == "cpu":
            total = 0.0
        else:
            total = mm.get_total_memory(dev) / (1024**3)
        return (
            int(round(total)),
            round(total, 2),
            total >= threshold_gb_1,
            total >= threshold_gb_2,
            total >= threshold_gb_3,
        )


NODE_CLASS_MAPPINGS = {"GPUTotalVRAM": GPUTotalVRAM}
NODE_DISPLAY_NAME_MAPPINGS = {"GPUTotalVRAM": "GPU Total VRAM"}
