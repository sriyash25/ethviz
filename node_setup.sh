#!/bin/bash

while getopts ":n:" opt; do
  case $opt in
    n)
      node_name="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ -z "$node_name" ]; then
  echo "Usage: setup.sh -n node_name"
  exit 1
fi

nohup geth --datadir "$node_name" init genesis.json &> /dev/null
nohup geth --datadir "$node_name" --networkid 1234 --mine --miner.etherbase="0x5D16922C9D065226f030851521033366c58f6fCb" --authrpc.port 8547 --http.api personal,eth,nn
et,web3,admin,txpool --http --http.addr "0.0.0.0" --rpc.enabledeprecatedpersonal &> /dev/null
