class ReverseName:
    def rev_name(self):
        from PyPack import readInput
        # data = input ("Enter your first name & last name = ")
        ri = readInput.read()
        data = ri.readUserInput()
        print(data[::-1])


obj = ReverseName()
obj.rev_name()


