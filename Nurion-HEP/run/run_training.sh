#python train_labelByUser.py --epoch 10 --batch 64 -o /x5/cms/jwkim/TORCH_GPU/HEP-CNN/run/result/result_CPLargekernelnorm0_lr_1e-3 --lr 1e-3 --batchPerStep 1 --shuffle True --optimizer adam --model CPlargekernelnorm0 -c config.yaml --lars True
#python train_labelByUser.py --epoch 10 --batch 64 -o /x5/cms/jwkim/TORCH_GPU/HEP-CNN/run/result/result_CPlargekernelnorm0_lr_2e-3 --lr 2e-3 --batchPerStep 1 --shuffle True --optimizer adam --model CPlargekernelnorm0 -c config.yaml --lars True
#python train_labelByUser.py --epoch 10 --batch 64 -o /x5/cms/jwkim/TORCH_GPU/HEP-CNN/run/result/result_CPlargekernelnorm0_lr_5e-3_real --lr 5e-3 --batchPerStep 1 --shuffle True --optimizer adam --model CPlargekernelnorm0 -c config.yaml --lars Ture

python train_labelByUser.py --epoch 100 --batch 128 -o 2021_results_gpu_singlerun/224x224 --lr 2e-3 --shuffle True --optimizer adam --model CPlargekernelnorm0 -c config.yaml

#python train_labelByUser.py --epoch 100 --batch 64 -o 2021_results_gpu_singlerun --lr 8e-3 --shuffle True --optimizer adam --model CPlargekernelnorm0 -c config.yaml
