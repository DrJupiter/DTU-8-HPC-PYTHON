#!bin/bash
#BSUB -q hpc
#BSUB -J specialcourse 
#BSUB -n 4
#BSUB -W 2 
#BSUB -R "select[model == XeonE5_2660v3]"
#BSUB -R "rusage[mem=512MB]"
#BSUB -u s204123@student.dtu.dk
#BSUB -B
#BSUB -N
#BSUB -o %J.out
#BSUB -e %J.out

sleep 60