# Installation 

`pip install -r requirements.txt`

# Usage

`./concat`

Takes all images found in the folder `uncheck` and combines them into a single pdf file that will be found in the folder
`uncheck-concat`. It will save the name of every image and its position in the pdf in a file called `config.json`

`split.py`

Takes the first pdf found in `check-concat` and splits every page into individual images named according to `config.json`

