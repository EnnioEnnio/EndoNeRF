#!/bin/bash -eux
#SBATCH --job-name=es_endoNeRF
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ennio.strohauer@mattermost
#SBATCH --partition=gpua100 # -p
#SBATCH --cpus-per-task=10 # -c
#SBATCH --mem=50gb
#SBATCH --gpus=1
#SBATCH --time=09:00:00 # 09 hours
#SBATCH --output=job_test_%j.log # %j is job id

cudaenv="endonerf3"
source /dhc/home/ennio.strohauer/conda3/bin/activate
conda activate $cudaenv
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice/renderonly_path_fixidentity_100000/estim
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_HITNet/renderonly_path_fixidentity_100000/estim
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_sharpened_once/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_sharpened_once/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_sharpened_once/renderonly_path_fixidentity_100000/estim
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python eval_rgb.py --gt_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_sharpened_twice/images --mask_dir /dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_sharpened_twice/gt_masks --img_dir /dhc/home/ennio.strohauer/EndoNeRF/logs/cutting_tissues_twice_sharpened_twice/renderonly_path_fixidentity_100000/estim
