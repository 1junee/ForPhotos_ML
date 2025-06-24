"""Automatic filter application module."""

from typing import Tuple
from PIL import Image, ImageEnhance, ImageOps
import numpy as np


def analyze_image(path: str) -> Tuple[float, float, float]:
    """Return average H, S, V values for the image."""
    img = Image.open(path).convert("RGB")
    hsv = img.convert("HSV")
    arr = np.array(hsv) / 255.0
    h, s, v = arr[:, :, 0].mean(), arr[:, :, 1].mean(), arr[:, :, 2].mean()
    return h, s, v


def apply_filter(path: str, filter_type: str, output_path: str) -> str:
    """Apply a simple filter and save the result."""
    img = Image.open(path).convert("RGB")
    if filter_type == "bright":
        img = ImageEnhance.Brightness(img).enhance(1.2)
    elif filter_type == "vintage":
        img = ImageOps.colorize(img.convert("L"), "#704214", "#C0A080")
    elif filter_type == "cool":
        r, g, b = img.split()
        b = ImageEnhance.Brightness(b).enhance(1.3)
        img = Image.merge("RGB", (r, g, b))
    img.save(output_path)
    return output_path


def auto_apply_filter(path: str, output_path: str) -> str:
    """Infer mood from colors and apply an appropriate filter."""
    h, s, v = analyze_image(path)
    if v < 0.4:
        filter_type = "bright"
    elif h > 0.6:
        filter_type = "cool"
    else:
        filter_type = "vintage"
    return apply_filter(path, filter_type, output_path)


if __name__ == "__main__":
    import sys
    src = sys.argv[1]
    dst = sys.argv[2]
    print(auto_apply_filter(src, dst))
