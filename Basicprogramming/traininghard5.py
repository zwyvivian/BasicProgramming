from collections import OrderedDict

class LstUpdate(OrderedDict):
    def __init__(self,cap):
        super(LstUpdate,self).__init__()
        self.cap=cap

    def __setitem__(self, key, value):
