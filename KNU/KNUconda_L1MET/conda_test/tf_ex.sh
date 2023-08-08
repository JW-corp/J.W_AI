#!/bin/bash



ls /u/user/jiwoong/anaconda3/etc/profile.d/conda.sh
export PATH=~/anaconda3/bin:$PATH
source /u/user/jiwoong/anaconda3/etc/profile.d/conda.sh

echo "#1 START conda-setup"
conda-env -h
conda-env create -f environment.yml
conda activate l1metml


echo "#2 CHECKING  GPU status"
nvidia-smi


