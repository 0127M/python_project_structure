# Import Module
import yaml


class Baseclass:
    def __init__(self):

        with open('D:\Python programs\structure_python\project_basic\config\configurations.yaml') as f :
            data = yaml.load(f, Loader=yaml.FullLoader)
        self.params = data


Base = Baseclass()
Base.m1()












    