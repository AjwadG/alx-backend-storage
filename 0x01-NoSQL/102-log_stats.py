#!/usr/bin/env python3
""" 102-log_stats """
from pymongo import MongoClient


def main():
    """ main function """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    get = logs_collection.count_documents({'method': 'GET'})
    post = logs_collection.count_documents({'method': 'POST'})
    put = logs_collection.count_documents({'method': 'PUT'})
    patch = logs_collection.count_documents({'method': 'PATCH'})
    delete = logs_collection.count_documents({'method': 'DELETE'})
    st = logs_collection.count_documents({'method': 'GET', 'path': '/status'})

    print('{} logs'.format(logs_collection.count_documents({})))
    print('Methods:')
    print('\tmethod GET: {}'.format(get))
    print('\tmethod POST: {}'.format(post))
    print('\tmethod PUT: {}'.format(put))
    print('\tmethod PATCH: {}'.format(patch))
    print('\tmethod DELETE: {}'.format(delete))
    print('{} status check'.format(st))

    IPs = logs_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "total": {"$sum": 1}
            }
        }, {
            "$sort": {
                "total": -1
            }
        }, {
            "$limit": 10
        }
    ])
    print('IPs:')
    for ip in IPs:
        print('\t{}: {}'.format(ip.get('_id'), ip.get('total')))


if __name__ == "__main__":
    main()
