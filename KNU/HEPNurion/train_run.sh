#!/bin/bash

/usr/bin/python3 -m pip install --user virtualenv
echo "***virtualenv Installed...***"

python3 -m virtualenv myvenv
source myvenv/bin/activate
echo "***Installing modules...***"
echo "--------------------------"
pip3 install h5py
echo "***h5py Installed...***"
pip3 install numpy
echo "***numpy Installed...***"
pip3 install PyYAML
echo "***PyYAML Installed...***"
pip3 install torch torchvision torchaudio
echo "***pytorch Installed...***"
pip3 install tqdm
echo "***tqdm Installed...***"
pip3 install scikit-learn
echo "***sklearn Installed...***"
pip3 install pandas
echo "***pandas Installed...***"
echo "--------------------------"

tar -xvf RUN.tar
ls -alh

echo "***Training codes on***"
mkdir models

outpath=`readlink -e models`

echo "***Output directory created***"
echo "--------------------------"
ls -ltr

# PATHAPTHAPTH
cd u/user/lovjxs74/4TOP_ver2/HEP-CNN/run
# PATHPATH

echo "--------------------------"
ls -ltr
echo "***Training...***"
python3 train_labelByUser.py --epoch 5 --batch 64 --lr 1e-4 -o $outpath --model circpad -c config_4top_vs_QCD.yaml
ls -alh

echo "***Finishing...***"

