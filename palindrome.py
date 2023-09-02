class Palindrome:
    def __init__(self, a):
        self.value = a
    def is_true(self):
        if(type(self.value) != str):
            b=str(self.value)[::-1]
            if (str(self.value) == b):
                return "It is a palindrome"
            else:
                return "It is not a palindrome"
        else:
            d=(self.value)[::-1]
            if (self.value == d):
                return "It is a palindrome"
            else:
                return "It is not a palindrome"


checker1=Palindrome(1230321)
print(checker1.is_true())

checker2=Palindrome("1230321 09234 0124210")
print(checker2.is_true())

checker3=Palindrome("abcd5dcba 1230321 09234 0124210")
print(checker3.is_true())
