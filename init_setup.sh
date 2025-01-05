echo [$(date)]:"START"
echo [$(date)]:"Creating conda env using Python 3.9"
conda create --prefix ./env python=3.9 -y

echo [$(date)]:"Activating env"
source activate ./env

echo [$(date)]:"Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"END"
