#!bin/bash
#BSUB -q hpc
#BSUB -J specialcourse 
#BSUB -n 16
#BSUB -W 2 
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "span[hosts=1]"
#BSUB -u s204123@student.dtu.dk
#BSUB -B
#BSUB -N
#BSUB -o %J.out
#BSUB -e %J.out

sleep 60