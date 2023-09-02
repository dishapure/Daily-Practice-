def booooooooooopictures():
    actress = "rani mukharjee"
    merijaan = "kiara"
    try:
        assert actress != "rani mukharjee"
        assert merijaan == "kiara"
    except AssertionError as e:
        if actress ==  "rani mukharjee":
            print("bhai apan to error to dega na kya is ko actress banayi")
        else:
            print("tere ki yeh kya hai")
        if merijaan == "kiara":
            print("ha yeh sahi hai")
        else:
            print("tere ki yeh kya hai")
        print(f"Caught the AssertionError: {e}")

booooooooooopictures()
