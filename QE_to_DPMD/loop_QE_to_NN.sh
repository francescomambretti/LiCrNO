# Written by Francesco Mambretti, 24/1/2023

main_folder=/leonardo_scratch/fast/IscrB_GRANCOCA/LiCrNO/round15/H-_form/get_FES/
#folders=#bias_70_pace_250/run_0 bias_70_pace_250/run_1 bias_90_pace_250/run_0)
folders=(0 1 2 3 4 5) #($(seq 0 6))
min_id=(0 0 0 0 0 0)
max_id=(49 49 49 49 49 49) #(346 685 1194 1631 1851 2036)

echo $folders

cwd=$(pwd)
index=0
for fold in ${folders[*]}; do
#	echo $main_folder ${fold} ${min_id[$index]} ${max_id[$index]}
	#min_id=$(($fold*5+j))
	#max_id=$(($min_id+4))
	#bash QE_to_NN.sh $main_folder run_${folders[$index]} $min_id $max_id
	bash QE_to_NN.sh $main_folder run_${folders[$index]} ${min_id[$index]} ${max_id[$index]}
#	cd ${cwd}
	index=$((index+1))
done
