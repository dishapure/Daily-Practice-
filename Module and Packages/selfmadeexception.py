class FakeFaltuError(Exception):
    def __init__(self,a):
        print("choti moti error hai yeh",a)
        

def callkarobhaiexeptionko(a):
    raise FakeFaltuError(a)

callkarobhaiexeptionko("sab badiya hai yaha ha ha ha")

obj  = FakeFaltuError("obj se pass kiya")