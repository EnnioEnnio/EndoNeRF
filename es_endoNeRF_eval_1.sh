#!/bin/bash -eux
#SBATCH --job-name=es_endoNeRF_eval1
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
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python run_endonerf.py --config configs/conf_cutting_tissues_twice_HITNet_StereoNet.txt --render_only
/dhc/home/ennio.strohauer/conda3/envs/$cudaenv/bin/python run_endonerf.py --config configs/conf_cutting_tissues_twice_HITNet_HITNetXL.txt --render_only