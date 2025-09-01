main_folder=/leonardo_scratch/fast/IscrB_GRANCOCA/LiCrNO/round15/
#folders=(bias_100_pace_250/run_0  bias_75_pace_500/run_0 bias_80_pace_250/run_4 bias_80_pace_250/run_5 bias_80_pace_500/run_1 bias_80_pace_500/run_4)
folders=(/NN_form/c_NHNH/from_10NH-8NH2-1NH3)

#min_id=(0 0 0 0) #(0 0 0 0 0 0 0)
#max_id=(49 49 49 49) #(1 29 2 1 1 2 4)

runs=`seq 1 1`

cwd=$(pwd)
index=0
for fold in ${folders[*]}; do
	cd $main_folder/$fold
	#pwd
	#ls
	for run in ${runs[*]};do
		min_id=0 #$((5*${run}))
		max_id=149 #$((5*${run}+4))
		cd run_$run
		ls
		for QE in `seq ${min_id} ${max_id}`; do
			##echo $QE,$run
			#pwd
		#for QE in `seq ${min_id[$index]} ${max_id[$index]}`; do
			cp $cwd/job.sh QE_group_$QE/
			cd QE_group_$QE
			sbatch job.sh
			cd ..
		done
		index=$((index+1))
		cd ..
	done
	cd $cwd
done
