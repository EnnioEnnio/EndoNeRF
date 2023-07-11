#!/bin/bash -eux
#SBATCH --job-name=es_endoNeRF_recon
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
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python endo_pc_reconstruction.py --config_file configs/conf_cutting_tissues_twice_HITNet_StereoNet.txt --n_frames 156 --depth_smoother --depth_smoother_d 28
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python endo_pc_reconstruction.py --config_file configs/conf_cutting_tissues_twice_HITNet_HITNetXL.txt --n_frames 156 --depth_smoother --depth_smoother_d 28