# Written by Francesco Mambretti, 24/1/2023

main_folder=/leonardo_scratch/fast/IscrB_GRANCOCA/LiCrNO/round15/unbias_9NH_9NH2/
folders=(run_0 run_1)

cwd=$(pwd)

for index in ${!folders[*]}; do
	cp raw_to_set.sh $main_folder/${folders[$index]}
	cd $main_folder/${folders[$index]}
	sh raw_to_set.sh
        mkdir rawfiles/
	mv *raw rawfiles/
	mv set.000/ rawfiles/
	cd ${cwd}
done
