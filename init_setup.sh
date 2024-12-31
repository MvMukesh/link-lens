echo [$(date)]:"START"
echo [$(date)]:"Creating conda env using Python 3.9"
conda create --prefix ./linkLens_env python=3.9 -y

echo [$(date)]:"Activating env"
source activate ./linkLens_env

echo [$(date)]:"Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"END"
