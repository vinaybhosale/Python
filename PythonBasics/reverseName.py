class ReverseName:
    def rev_name(self):
        from PythonBasics import readInput
        # data = input ("Enter your first name & last name = ")
        ri = readInput.read()
        data = ri.readUserInput()
        print(data[::-1])

    name = "Vinay"

    size = len(name)
    index = size - 1
    rev_name = ""

    while index > -1:
        reverse_string = name[index]
        rev_name += reverse_string
        index -= 1
    print(rev_name)

obj = ReverseName()
obj.rev_name()


