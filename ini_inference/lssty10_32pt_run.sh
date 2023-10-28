#!/bin/bash
#SBATCH --job-name=lssty10_32pt
#SBATCH -n 200
#SBATCH -c 1
#SBATCH -p kipac
#SBATCH -t 0-48:00:00
#SBATCH -o jobout%j.out
#SBATCH -e joberr%j.out

#go to the location of the cosmosis environment
#!!change if you put it at a different place
cd $SCRATCH
#activate cosmosis environment
source ./env_cosmosis/bin/activate
source cosmosis-configure
#!!change to location of your cosmosis-standard-library 
export CSL_PATH=$SCRATCH/cosmosis-standard-library

#go to the location of the cosmosis ini_files
#!!change if you cloned it at a difference place
cd tutorial_wlcosmology/ini_inference

srun cosmosis --mpi lssty10_32pt_fullchain_nautilus.ini  
