class Dict(dict):
    ''''
    Simple dict but also support access as x.y style
    >>> d1=Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    '''
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
            #return 90
        except KeyError:
            raise AttributeError(r"'Dict' object has not attribute '%s'"%key)
    def __setattr__(self,key,value):
        self[key] = value
if __name__ == '__main__':
    import doctest
    doctest.testmod()