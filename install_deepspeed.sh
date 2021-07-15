export PDSH_RCMD_TYPE=ssh



num_nodes=$1

if [ -z $1 ];

then

    num_nodes=$DLWS_NUM_WORKER

fi

hosts="worker-0"

for i in `seq 1 $(( num_nodes - 1 ))`; do

        hosts="${hosts},worker-${i}"

done

echo ${hosts}

pdsh -w ${hosts} sudo pip uninstall -y deepspeed
#pdsh -w ${hosts} cd /home/zheweiyao/DeepSpeed
pdsh -w ${hosts} sudo pip install -e /home/zheweiyao/DeepSpeed/
