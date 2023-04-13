#!/bin/bash

nodename="node1"
port="8546"

while getopts ":n:p:" opt; do
  case ${opt} in
    n ) nodename=$OPTARG
      ;;
    p ) port=$OPTARG
      ;;
    \? ) echo "Invalid option: $OPTARG" 1>&2
         exit 1
      ;;
    : ) echo "Invalid option: $OPTARG requires an argument" 1>&2
         exit 1
      ;;
  esac
done

nohup geth --datadir $nodename init genesis.json &> /dev/null
nohup geth --datadir $nodename --networkid 1234 --mine --miner.etherbase="0x5D16922C9D065226f030851521033366c58f6fCb" --authrpc.port $port --http.api personal,eth,net,web33,admin,txpool --http --http.addr "0.0.0.0" --rpc.enabledeprecatedpersonal &> /dev/null
