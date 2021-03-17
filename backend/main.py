from flask import Flask
from elasticsearch import Elasticsearch

es = Elasticsearch(HOST='http://127.0.0.1',PORT=9200)
#
# try:
#     es.indices.create(index="logs")
# except:
#     print('index: logs, already exists ')

# logging.basicConfig(filename='Logs/backend_logs',level=logging.WARNING)
# logging.info("Creating handler")
# root = logging.getLogger()
# hdlr = root.handlers[0]
# json_format = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
# hdlr.setFormatter(json_format)

app = Flask(__name__)