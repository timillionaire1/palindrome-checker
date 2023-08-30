class Palindrome:
    def __init__(self, a):
        self.value= a
    def is_true(self):
        b=self.value[::-1]
        if (self.value == b ):
            return "It is a palindrome"
        else:
            return "It is not a palindrome"

checker1=Palindrome("titi")
print(checker1.is_true())

checker1=Palindrome("refer")
print(checker1.is_true())
