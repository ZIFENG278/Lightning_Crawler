#!/usr/bin/env bash


version_match=`python3 -c 'import sys;r=0 if sys.version_info >= (3,7) else 1;print(r)'`
if [ $version_match -ne 0 ]; then
echo 'python version must be >= 3.7'
exit 1
fi

echo "setup a virtual python environment"
python -m venv .venv

source .venv/bin/activate

python3 -m pip install --upgrade pip

pip3 install -r requirements.txt


