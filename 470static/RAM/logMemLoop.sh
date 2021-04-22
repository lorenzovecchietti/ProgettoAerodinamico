#/bin/bash
dir=$1
if [ ! -d $dir/logMem.dat ]; then
  totRAM="$(free -m | grep 'Mem:' | awk '{print $2}')"
  totSWAP="$(free -m | grep 'Swap:' | awk '{print $2}')"
  echo -e "RAM:$totRAM\nSWAP:$totSWAP\n" >> $dir/logMem.dat
fi

for i in {1..29}
do
  time="$(date +"%H:%M:%S")"
  nowRAM="$(free -m | grep 'Mem:' | awk '{print $3}')"
  nowSWAP="$(free -m | grep 'Swap:' | awk '{print $3}')"
  echo "$time,$nowRAM,$nowSWAP" >> $dir/logMem.dat
  sleep 2
done
