
import os
import datetime

import logging 
from logging import Logger
# import logging.config


def createLogger(root: str = None,strtime_name: str = '%Y%m%d%H%M', useFileHander:bool = True, useStreamHandler:bool = True) -> Logger:
    if root == None:
        root = os.path.dirname(os.path.realpath(__file__))
        root = os.path.join(root,'log')
    
    if os.path.exists(root) == False:
        os.mkdir(root)

    log_name_time = datetime.datetime.now().strftime(strtime_name)
    # log_name_time = datetime.datetime.now().strftime()

    # new logging
    # logging.basicConfig(encoding='utf-8')
    logger = logging.getLogger(name=log_name_time + '.log')
    logger.setLevel(logging.DEBUG)

    logger.dir = root
    logger.filename = os.path.join(root, log_name_time + '.log')

    if useFileHander:
        # add file hander
        fh = logging.FileHandler(filename=os.path.join(root, log_name_time + '.log'),encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s',
            # datefmt=strtime
            )
        # formatter = logging.Formatter(
        #     '%(asctime)s - %(levelname)s - %(message)s',
        #     datefmt=strtime)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    if useStreamHandler:
        # add stream hander
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            # datefmt=strtime
            )
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    return logger