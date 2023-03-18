import logging, sys
from dotenv import load_dotenv
from os import path, environ



def getlogger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(filename)s - Line: %(lineno)d - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


basedir = path.abspath(path.join(path.abspath(path.dirname(__file__)), '../'))

configdir = path.join(basedir, 'config')

load_dotenv(path.join(configdir, '.env'))

logger = getlogger("mcq_app", logging.INFO)

dbData = {
    "host" : environ.get("dbHost"),
    "port" : int(environ.get("dbPort")),
    "user" : environ.get("dbUser"),
    "name" : environ.get("dbName"),
    "password" : environ.get("dbPassword")
}
