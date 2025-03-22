#! /bin/bash

python3 -m venv /tmp/steg-venv
source /tmp/steg-venv/bin/activate

pip install -r ./requirements.txt

python3 decode.py 