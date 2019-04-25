
class stringDemo:
    # length of string
    name = "Vinay Bhosale"
    print(len(name))

    # to find char occurences
    # char = "google"
    # print(char[0])
    # dict = {}
    # for ele in char:
    #     if ele not in dict:
    #         dict[ele] = 1
    #     else:
    #         dict[ele] += 1
    # print(dict)

    # list = []
    # game = "tricketttt"
    # for ele in game:
    #     if ele not in list:
    #         list.append(ele)
    #     else:
    #         list.append('$')
    # print(list)

    # name = "vinay"
    # print(name[3:])

    # checks whether a string ends with ing if yes tghen adds ly or else adds ing
    def add_char_to_string(self, string):
        add_ing_string = "ing"
        add_ly_string = "ly"
        if len(string) > 3:
            new_string_size = len(string) - 3
            new_str = string[new_string_size:]
        for ele in string:
            if new_str != add_ing_string:
                ingstring = string + add_ing_string
                print("Printing new string with ING at end :",ingstring)
            elif new_str == add_ing_string:
                lystring = string + add_ly_string
                print("Print new string with LY at end :",lystring)

        return new_str


    #Functionj takes list of words and returns the longest string lengthwise

    def find_long_string(self):
        list = []
        list_size = int(input("enter the size of list : "))
        for ele in range(0, list_size):
            add_to_list = input("enter the words :")
            list.append(add_to_list)
        print(list)
        # sorted_list = list.sort()
        # print(sorted_list)
        long_string = ""
        length = 0
        for ele in list:
            if length < len(ele):
                length = len(ele)
                long_string = ele
        print("The longest string is :", long_string)
        return ""

    # program converts the given word into upper and lower case
    def upper_lower(self):
        user_input = input("Enter the word :")
        lower_user_input = user_input.lower()
        upper_user_input = user_input.upper()
        print("Upper case :",upper_user_input,"Lower case :",lower_user_input)

    def sort_list_of_words(self):
        list = [ 'red', 'white', 'black', 'red', 'green', 'black' ]
        values = int(input("enter the size of tuple : "))
        new_list = []
        for ele in range(0, values):
            elements = input("Enter the words : ")
            new_list.append(elements)
        new_set = set(new_list)
        print(sorted(new_set))

    def split_string(self):
        name = "VinayVinayVinayVinay"
        #splits the string at the 1st occurence of "n"
        print(name.rsplit('n', 1)[0])
        # splits the string at the 4th occurence of "n"
        print(name.rsplit('n', 4)[0])

    string = "Mumbai has team named as Mumbai Indians"
    new_list = string.split(" ")
    print(new_list)

    # print(string.count("Mumbai"))
    substring = "Mumbai"
    count = 0
    for ele in new_list:
        if substring == ele:
            count += 1
    print(count)
    # def substring_count(self):
    #     count = 0
    #     address = "C2 11 MIDC COLONY midc and mirage miplane"
    #     substring = print(input("enter the substring to check :"))
    #     for ele in address:
    #         if
    #         print(ele)
    #     return count

sd = stringDemo()
# print(sd.add_char_to_string(input("enter the string to check : ")))
# sd.find_long_string()
# sd.upper_lower()
sd.sort_list_of_words()
# sd.split_string()
# sd.substring_count()



