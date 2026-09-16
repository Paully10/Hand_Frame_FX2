"""
Render every effect in hand_frame_fx onto one image so you can pick your looks.

Usage:
    python3 make_contact_sheet.py                # synthetic demo scene
    python3 make_contact_sheet.py cam            # grab one webcam frame (best!)
    python3 make_contact_sheet.py path/to/pic.jpg  # your own photo

Writes effects_contact_sheet.png next to this file.
"""

import os
import sys
import cv2
import numpy as np

from handy_eff import EFFECTS, apply_effect

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "effects_contact_sheet.png")


def demo_scene(w=640, h=480):
    """A tonally rich synthetic scene (shaded sphere on a gradient) so
    luminance-based looks like chrome/thermal actually have something to show."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t = (xx / w * 0.6 + yy / h * 0.4)[..., None]
    bg = np.array([110, 85, 65]) * (1 - t) + np.array([205, 185, 235]) * t
    img = bg.astype(np.uint8)

    cx, cy, r = w * 0.5, h * 0.55, min(w, h) * 0.33
    inside = ((xx - cx) ** 2 + (yy - cy) ** 2) < r ** 2
    lx, ly = cx - r * 0.45, cy - r * 0.5          # light from upper-left
    shade = np.clip(1.0 - np.sqrt((xx - lx) ** 2 + (yy - ly) ** 2) / (r * 1.7), 0, 1)
    for c, k in enumerate((0.92, 0.96, 1.0)):     # subtle cool tint on the subject
        ch = img[..., c].astype(np.float32)
        ch[inside] = (shade * 255 * k)[inside]
        img[..., c] = np.clip(ch, 0, 255).astype(np.uint8)
    return cv2.GaussianBlur(img, (0, 0), 0.6)


def get_source(arg):
    if arg == "cam":
        cap = cv2.VideoCapture(0)
        frame = None
        for _ in range(10):                        # warm up / let exposure settle
            ok, f = cap.read()
            if ok:
                frame = f
        cap.release()
        if frame is not None:
            return cv2.flip(frame, 1)
        print("Webcam unavailable — falling back to the demo scene.")
    elif arg:
        img = cv2.imread(arg)
        if img is not None:
            return img
        print(f"Could not read '{arg}' — falling back to the demo scene.")
    return demo_scene()


def label(tile, text):
    cv2.rectangle(tile, (0, 0), (tile.shape[1], 34), (0, 0, 0), -1)
    cv2.putText(tile, text, (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2, cv2.LINE_AA)
    return tile


def main():
    src = get_source(sys.argv[1] if len(sys.argv) > 1 else None)
    tw, th = 420, int(420 * src.shape[0] / src.shape[1])
    src = cv2.resize(src, (tw, th))

    tiles = [label(src.copy(), "original")]
    for name, fn in EFFECTS:
        tiles.append(label(apply_effect(fn, src.copy()), name))

    ncols = len(tiles)                             # single row for easy comparison
    pad = 6
    grid = np.full(((th + pad) * 1 - pad, (tw + pad) * ncols - pad, 3), 20, np.uint8)
    for i, tile in enumerate(tiles):
        x = i * (tw + pad)
        grid[0:th, x:x + tw] = tile

    cv2.imwrite(OUT, grid)
    print(f"Wrote {OUT}  ({ncols} tiles: original + {len(EFFECTS)} effects)")


if __name__ == "__main__":
    main()
