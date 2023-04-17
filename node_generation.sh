#!/bin/bash

nodename="node1"
rpcport="8547"
httpport="8008"
ethport="30304"
account="0x6d918f4DecDbeCfeD4123dC42b7037D1aEE4D1F9"

while getopts ":n:r:h:e:a:" opt; do
  case ${opt} in
    n ) nodename=$OPTARG
      ;;
    r ) rpcport=$OPTARG
      ;;
    h ) httpport=$OPTARG
      ;;
    e ) ethport=$OPTARG
      ;;
    a ) account=$OPTARG
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
nohup geth --datadir $nodename --nodiscover --networkid 1234 --mine --port $ethport --miner.etherbase="$account" --rpc.enabledeprecatedpersonal --allow-insecure-unlock --authrpc.port $rpcport --http.api personal,eth,net,web3,admin,txpool --http --http.addr "0.0.0.0" --http.port $httpport &> /dev/null
