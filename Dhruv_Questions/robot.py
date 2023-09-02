class robot:
    type = ""

    def __init__(self, content):
        self.type2 = content
        robot.type += content + ";"

envelope_1 = robot("Raspberry Pi")
envelope_2 = robot("Arduino")

print(envelope_1.type, envelope_2.type2)
