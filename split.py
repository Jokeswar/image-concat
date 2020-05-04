#!/usr/bin/python3
import json
import fitz
from pathlib import Path
from glob import glob
from PIL import Image


def main():
    pdf_name = glob(str(Path("check-concat") / "*"))

    with open("config.json") as f:
        images_data = json.loads(f.read())

    doc = fitz.open(pdf_name[0])
    for i in range(len(doc)):
        pix = doc[i].getPixmap(alpha = False)
        out = str(Path("check-split") / images_data[i]["name"])
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(out, "JPEG")


if __name__ == "__main__":
    main()
