#!/bin/bash

nodename="node1"
rpcport="8547"
httpport="8008"
ethport="30304"

while getopts ":n:r:h:e:" opt; do
  case ${opt} in
    n ) nodename=$OPTARG
      ;;
    r ) rpcport=$OPTARG
      ;;
    h ) httpport=$OPTARG
      ;;
    e ) ethport=$OPTARG
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
nohup geth --datadir $nodename --networkid 1234 --mine --port $ethport --miner.etherbase="0x5D16922C9D065226f030851521033366c58f6fCb" --authrpc.port $rpcport --http.api personal,eth,net,web3,admin,txpool --http --http.addr "0.0.0.0" --http.port $httpport &> /dev/null
