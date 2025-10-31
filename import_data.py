import pandas as pd
class Initiation:
    def __init__(self):
        pass
    def import_my_data(self):
        print("Please enter your data path")
        path=input()
        data=pd.read_csv(path)
        return data
