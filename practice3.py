def name():
    raise Exception()
    
try:
    name()
except Exception:
    print("Dd")
except:
    print("bye")
finally:
    print("Good")