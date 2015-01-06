#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from modules import csv_io
from modules import json_io
from db.MyDB import MyDB

def to_foramt(data, date):
    new_data = []
    for i in range(1, len(data)):
        row = data[i]
        if row[-1][:10].replace('-', '') == date:
            geom = "ST_GeomFromText('POINT(%s %s)', 4326)" % \
                                    (row[4].decode('utf-8'), row[5].decode('utf-8'))
            new_data.append([row[0].decode('utf-8'), geom, row[6].decode('utf-8')])

    return new_data

if __name__=='__main__':
    
    config = json_io.read_json('config.json')
    db_config = config[u'database']
    mydb = MyDB( db_config[u'dbtype'], db_config[u'host'], db_config[u'dbname'], \
            db_config[u'username'], db_config[u'password'], db_config[u'encoding'], None)

    table_name = config[u'table']

    for root, _, files in os.walk(config[u'data'][u'folder_path']):
        for f in files:
            if f != '.DS_Store':
                dataset = csv_io.read_csv(root+f)
                data = to_foramt(dataset, f[11:19])
                for item in data:
                    mydb.insert(table_name, ['siteid', 'geom', 'rainfall10min'], item)
    mydb.close()
                

