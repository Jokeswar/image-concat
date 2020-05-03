#!/usr/bin/python3
import json
from pathlib import Path
from glob import glob
from PIL import Image


def main():
    image_names = glob(str(Path("uncheck") / "*"))
    images = [Image.open(x) for x in image_names]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    info = []
    for i in range(len(images)):
        image = {}
        aux = Path(image_names[i])
        image["name"] = aux.name
        image["width"] = widths[i]
        image["height"] = heights[i]
        info.append(image)

    with open("config.json", "w") as f:
        data = json.dumps(info)
        f.write(data)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save(Path("uncheck-concat") / "test.jpg")


if __name__ == "__main__":
    main()
