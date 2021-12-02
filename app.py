import time
import redis
from flask import Flask
from flask import request

app=Flask(__name__)

cache= redis.Redis(host='redis',port=6379)


@app.route('/',methods=['GET'])


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

