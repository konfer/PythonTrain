#codingL:utf-8

class RoundFloatManual(object):
    
    def __init__(self,val):
        assert isinstance(val,float),"value must be a float"
        self.value=round(val,2)
        
    def __str__(self):
        return "the value %s" %(self.value,)
            
    #__repr__=__str__

p=RoundFloatManual(7.5324534)

#print(repr(p))
print p