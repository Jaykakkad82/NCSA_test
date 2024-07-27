# ============= Question ====================
# a.	Replace all the vowels in the string “National Center for Supercomputing Applications” by their corresponding order number in alphabetical sequence (a with 1, e with 5, etc).
# b.	Print the resulting string.
# c.	Print the total number of consonants in the given string.

# ==== Logic====
# Assumption: Both upper and lowercase 'A'/ 'a' can be replaced with '1' and so on.
# use ascii values of each character. Use list to replace character in string.
# time complexity: O(n), Space complexity: O(n)


class StringPlayer:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")     # vowel check can be performed in O(1) time
    
    def replace_vowels(self, string):
        result = []             # store in an array as string is immutable
        consonant_count = 0

        for char in string:
            if char.isalpha():
                if char in self.vowels:
                    result.append(str(ord(char.lower()) - 97 + 1))      # use ascii values to find the correct number
                else:
                    # if alphabet not vowel then its a consonant
                    consonant_count += 1
                    result.append(char)
            else:
                result.append(char)
        
        print("Original String: ", string)
        print("Changed String: ", "".join(result))
        print("number of consonants in string: ", consonant_count)
        return "".join(result), consonant_count
    

# test required by the problem statement
worker = StringPlayer()
astring = "National Center for Supercomputing Applications"
outputstring, consonant_count = worker.replace_vowels(astring)
print("==============================")
print("Original String: ", astring)
print("Changed String: ", outputstring)
print("number of consonants in string: ", consonant_count)
        


# We can run a few unit tests to test our implementation of replace_vowels method
import unittest

class TestStringPlayer(unittest.TestCase):
    def setUp(self):
        self.player = StringPlayer()

    def test1_all_vowels(self):
        result_string, consonant_count = self.player.replace_vowels("aeiou")
        self.assertEqual(result_string, "1591521")
        self.assertEqual(consonant_count, 0)

    def test2_mixed(self):
        result_string, consonant_count = self.player.replace_vowels("All is Well")
        self.assertEqual(result_string, "1ll 9s W5ll")
        self.assertEqual(consonant_count, 6)

    def test3_all_consonants(self):
        result_string, consonant_count = self.player.replace_vowels("bcdfg")
        self.assertEqual(result_string, "bcdfg")
        self.assertEqual(consonant_count, 5)

    def test4_empty_string(self):
        result_string, consonant_count = self.player.replace_vowels("")
        self.assertEqual(result_string, "")
        self.assertEqual(consonant_count, 0)

    def test5_no_vowels(self):
        result_string, consonant_count = self.player.replace_vowels("xyz")
        self.assertEqual(result_string, "xyz")
        self.assertEqual(consonant_count, 3)

    def test6_mixed_case(self):
        result_string, consonant_count = self.player.replace_vowels("HeLLo WoRLd")
        self.assertEqual(result_string, "H5LL15 W15RLd")
        self.assertEqual(consonant_count, 7)
    def test7_numbers_special_char(self):
        result_string, consonant_count = self.player.replace_vowels("12345!@#")
        self.assertEqual(result_string, "12345!@#")
        self.assertEqual(consonant_count, 0)



if __name__ == '__main__':
    unittest.main()





