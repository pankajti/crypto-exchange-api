import yaml
import os
from io import StringIO
import datetime
import traceback
import tempfile

BINANCE_CONFIG = {}
DB_CONFIG = {}



try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

environment = os.environ['env'] if 'env' in os.environ else 'dev'

for path in user_paths:
    config_path='{}/config/config_{}.yaml'.format(path,environment)
    if( os.path.exists(config_path)):
        break
else:
    config_path='{}/config/config_{}.yaml'.format(path,'dev')



print('found config path at : {} '.format(config_path))

with open(config_path, 'r') as file :
    docs =yaml.load_all(file)
    for doc in docs:
        DB_CONFIG=doc['DB_CONFIG']
        BINANCE_CONFIG=doc['BINANCE_CONFIG']


print(BINANCE_CONFIG)