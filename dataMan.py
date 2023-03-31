
import os
import json5 as json
from logging import Logger

class DataManager():
    def __init__(self,
                file: str = None,
                root: str = None,
                logger:Logger = None,
                default=[]
                ):
        self.default = default

        if root == None:
            root = os.path.dirname(os.path.realpath(__file__))
        self.root = root


        if file == None:
            self.file = os.path.join(root,'data.json')
        else:
            self.file = os.path.join(root,file)
        
        self.logger = logger
        if self.logger == None:
            self.logger =  Logger('log')
            self.logger.warn('new logger was made')

        self.data = self.load()
        self.logger.info('init DataManager done')

    def load(self):
        self.logger.info('loading Json data')
        try:
            with open(self.file,'r') as file:
                return json.load(file)
        except:
            self.logger.error('error, while loading json file')
            self.data = self.default
            self.save()
            return self.data

    def save(self):
        with open(self.file,'w') as file:
            file.write(json.dumps(self.data,indent=4))
            self.logger.info(f'saved file {self.file}')