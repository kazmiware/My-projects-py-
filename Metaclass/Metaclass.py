class Meta(type):
    def __new__(self,cls,base,attr):
        print("Old Attributes:")
        print(attr)
        attr_new={}
        for name,val in attr.items():
            if name=='x':
               attr_new["x_new"]=val-1
            elif name=='y':
                attr_new["y_new"] =val-1
        print("New Attributes:")
        print(attr_new)
        return type(cls,base,attr_new)

class num(metaclass=Meta):
    x=4
    y=9






