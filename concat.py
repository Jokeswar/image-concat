#!/usr/bin/python3
import json
from pathlib import Path
from glob import glob
from PIL import Image


def main():
    image_names = glob(str(Path("uncheck") / "*"))
    images = [Image.open(x) for x in image_names]
    widths, heights = zip(*(i.size for i in images))

    info = []
    for i in range(len(images)):
        image = {}
        image["name"] = Path(image_names[i]).name
        image["width"] = widths[i]
        image["height"] = heights[i]
        info.append(image)

    with open("config.json", "w") as f:
        data = json.dumps(info)
        f.write(data)

    pdf_path = Path("uncheck-concat") / "test.pdf"
    images[0].save(pdf_path, "PDF", resolution=100.0,
                   save_all=True, append_images=images[1:])


if __name__ == "__main__":
    main()
