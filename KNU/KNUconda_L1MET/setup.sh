#!/bin/bash
mamba activate deepmeteor-py310

export PROJECT_HOME=${PWD}
export PROJECT_LOG_DIR=${PROJECT_HOME}/logs
export PROJECT_DATA_DIR=/pnfs/knu.ac.kr/data/cms/store/user/jiwoong/deepmet

export PYTHONPATH=${PROJECT_HOME}:${PYTHONPATH}

python --version
which python
declare -p PROJECT_HOME
declare -p PROJECT_LOG_DIR
declare -p PROJECT_DATA_DIR
