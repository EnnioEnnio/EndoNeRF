#!/bin/bash -eux
#SBATCH --job-name=es_endoNeRF_eval2
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ennio.strohauer@mattermost
#SBATCH --partition=gpupro # -p
#SBATCH --cpus-per-task=10 # -c
#SBATCH --mem=50gb
#SBATCH --gpus=1
#SBATCH --time=09:00:00 # 09 hours
#SBATCH --output=job_test_%j.log # %j is job id

cudaenv="endonerf3"
source /dhc/home/ennio.strohauer/conda3/bin/activate
conda activate $cudaenv
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet_m1/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet_m1/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_HITNet_StereoNet/renderonly_path_fixidentity_100000/estim
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet_m2/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet_m2/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_HITNet_HITNetXL/renderonly_path_fixidentity_100000/estim