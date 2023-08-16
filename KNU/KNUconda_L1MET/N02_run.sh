#!/bin/bash

ls /u/user/jiwoong/anaconda3/etc/profile.d/conda.sh
export PATH=~/anaconda3/bin:$PATH
source /u/user/jiwoong/anaconda3/etc/profile.d/conda.sh

echo "#1 START conda-setup"
conda activate deepmeteor-py310


echo "#2 CHECKING  GPU status"
nvidia-smi


echo "#3 CHECKING  setup path"
source setup.sh

echo "---path check--"
pwd
ls -alh

echo "#4 START training"
python train.py config/transformer.yaml 
echo "#5 The END"
ls -alh
