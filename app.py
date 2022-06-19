from flask import Flask, request, jsonify
from flask_pymongo import pymongo
from flask.json import jsonify
import yt
import threading
import time

app = Flask(__name__)

# Set up mongodb client
client = pymongo.MongoClient(host='test_mongodb',
                            port=27017,
                            username='root',
                            password='root')
db = client.yt_videos
data_collection = db.data

if __name__=='__main__':
    app.run(debug=True)


# running db_populate() in background thread to populate mongodb
def db_populate():
    while True:
        result = yt.fetchApiResults()
        for item in result:
            try:
                data_collection.insert_one({
                    "_id":item['video_id'],
                    "video_id": item['video_id'],
                    "title": item['title'],
                    "description": item['description'],
                    "channel_title": item['channel_title'],
                    "published_at": item['published_at']
                    })
            except:
                pass
        time.sleep(10)


threading.Thread(target=db_populate).start()

@app.route('/api', methods=['GET'])
def fetch_paginated_data():
    offset = int(request.args['offset'])
    limit = int(request.args['limit'])
    order = str(request.args['order'])

    starting_id = data_collection.find().sort('published_at', pymongo.DESCENDING)
    last_id = starting_id[offset]['_id']

    if order == "DESCENDING":
        data = data_collection.find({'_id': {'$gte': last_id}}).sort('published_at', pymongo.DESCENDING).limit(limit)
    else:
        data = data_collection.find({'_id': {'$gte': last_id}}).sort('published_at', pymongo.ASCENDING).limit(limit)

    output = []

    for i in data:
        output.append(i)

    return jsonify(output)

@app.route('/api/search', methods=['GET'])
def search():
    key = str(request.args['q'])

    output = []

    data_collection.create_index([("title", pymongo.TEXT)])

    data = data_collection.find({"$text": {"$search": "\""+key+"\""}})

    for i in data:
        output.append(i)

    return jsonify(output)
