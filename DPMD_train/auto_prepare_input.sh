#Original code by Manyi Yang
#Modified by Francesco Mambretti, 24/01/2023

templateinput='input_template.json'
dirs='1model 2model 3model 4model'

root_dir="from-frozen14"
i=0

for dir in $dirs #do 4 random copies
do
  i=$(($i+1))
  mkdir -p $root_dir/$dir
  seed1=$RANDOM
  seed2=$RANDOM
  seed3=$RANDOM
  cp $templateinput $root_dir/$dir/input.json
  cp frozen_model14.pb $root_dir/$dir/
  sed -i 's/SEED1/'"$seed1"'/' $root_dir/$dir/input.json
  sed -i 's/SEED2/'"$seed2"'/' $root_dir/$dir/input.json
  sed -i 's/SEED3/'"$seed3"'/' $root_dir/$dir/input.json
  cd $root_dir/$dir
	cp ../../sub-a100.sh .
	qsub sub-a100.sh
  cd ../..
done
