class Palindrome:
    def __init__(self, a):
        self.value = a
    def is_true(self):
        try:
            #let's validate if the parameter is not a string
            if(type(self.value) != str):
                #let's convert it to a string and reverse the order
                b=str(self.value)[::-1]
                if (str(self.value) == b):
                    return "It is a palindrome"
                else:
                    return "It is not a palindrome"
            #let's validate if the parameter is a string
            else:
                #let's reverse the order
                d=(self.value)[::-1]
                if (self.value == d):
                    return "It is a palindrome"
                else:
                    return "It is not a palindrome"
        except TypeError:
            return ("The data type might be faulty")

#let's try out a integer datatype
checker1=Palindrome(1230321)
print(checker1.is_true())

#let's try out a string datatype
checker2=Palindrome("1230321 09234 0124210")
print(checker2.is_true())

#let's try out another string datatype
checker3=Palindrome("abcd5dcba 1230321 09234 0124210")
print(checker3.is_true())

#let's try out another list datatype
checker4=Palindrome(['timi', 'titi', 'sql'])
print(checker4.is_true())

# #let's try out another dictionary datatype
# checker5=Palindrome({'a':'b'})
# print(checker5.is_true())
