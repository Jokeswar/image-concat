#!/usr/bin/python3
import json
from pathlib import Path
from glob import glob
from PIL import Image


def main():
    image_name = glob(str(Path("check-concat") / "*"))
    image = Image.open(image_name[0])
    widths, heights = image.size

    with open("config.json") as f:
        images_data = json.loads(f.read())

    x_offset = 0
    for i in range(len(images_data)):
        zone = (x_offset,
                0,
                x_offset + images_data[i]["width"],
                images_data[i]["height"])
        name = str(Path("check-split") / images_data[i]["name"])
        image.crop(zone).save(name)
        x_offset += images_data[i]["width"]


if __name__ == "__main__":
    main()
