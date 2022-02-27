import unittest
from unittest.mock import patch
from dictionary import checkWord, countLetters, getRandomWord

from ui import checkLengthNotFiveAndAlphabets, getUserInput, isWordValidDictionaryWord, printWordRestrictionsError, wordIsEqualToInput

class WordIsEqualToInput_Tests(unittest.TestCase):
    def test_wordIsEqualToInput_wrongInput1(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        expectedWord = "Banks"
        userInput = "Books"
        self.assertFalse(wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_wrongInput2(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        expectedWord = "Banks"
        userInput = "Pitch"
        self.assertFalse(wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_wrongInput3(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        expectedWord = "Banks"
        userInput = "Hello"
        self.assertFalse(wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_wrongInput4(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        expectedWord = "Banks"
        userInput = "Clubs"
        self.assertFalse(wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_correctInput1(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        expectedWord = "Banks"
        userInput = "Banks"
        self.assertTrue(wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput2(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        expectedWord = "abuse"
        userInput = "abuse"
        self.assertTrue(wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput3(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        expectedWord = "Goals"
        userInput = "Goals"
        self.assertTrue(wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput4(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        expectedWord = "about"
        userInput = "about"
        self.assertTrue(wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_caseSensitive(self) -> None:
        """Test wordIsEqualToInput method with correct input - return false"""
        expectedWord = "Banks"
        userInput = "BANKS"
        self.assertFalse(wordIsEqualToInput(expectedWord, userInput))

class IsWordValidDictionaryWord_Tests(unittest.TestCase):
    def test_isWordValidDictionaryWord_wrongInput1(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        userInput = "xyzzz"
        self.assertFalse(isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_wrongInput2(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        userInput = "champ"
        self.assertFalse(isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_wrongInput3(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        userInput = "classy"
        self.assertFalse(isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_wrongInput4(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        userInput = "plants"
        self.assertFalse(isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_correctInput1(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        userInput = "abuse"
        self.assertTrue(isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_correctInput2(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        userInput = "later"
        self.assertTrue(isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_correctInput3(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        userInput = "laugh"
        self.assertTrue(isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_correctInput4(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        userInput = "menus"
        self.assertTrue(isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_caseSensitive(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        userInput = "LAUGH"
        self.assertFalse(isWordValidDictionaryWord(userInput))

class CheckLengthNotFiveAndAlphabets_Tests(unittest.TestCase):
    def test_checkLengthNotFiveAndAlphabets_wrongInput1(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        userInput = "laughs"
        self.assertTrue(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput2(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        userInput = "book"
        self.assertTrue(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput3(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        userInput = "geek"
        self.assertTrue(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput4(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        userInput = "mock"
        self.assertTrue(checkLengthNotFiveAndAlphabets(userInput))
    
    def test_checkLengthNotFiveAndAlphabets_correctInput1(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        userInput = "laugh"
        self.assertFalse(checkLengthNotFiveAndAlphabets(userInput))
    
    def test_checkLengthNotFiveAndAlphabets_correctInput2(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        userInput = "menus"
        self.assertFalse(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_correctInput3(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        userInput = "mercy"
        self.assertFalse(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_correctInput4(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        userInput = "naval"
        self.assertFalse(checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_symbolInput(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input(contains symbols) - return true"""
        userInput = "n@!al"
        self.assertTrue(checkLengthNotFiveAndAlphabets(userInput))

class GetUserInput_Tests(unittest.TestCase):
    @patch('builtins.input', return_value = '')
    def test_getUserInput_blankInput(self, mock_inputs):
        result = getUserInput([])
        self.assertEqual(result, 0)

    @patch('builtins.input', return_value = 'hey')
    def test_getUserInput_lessCharacters(self,mock_inputs):
        with patch("ui.printWordRestrictionsError") as patched_function:
            getUserInput([])
        patched_function.assert_called()

    @patch('builtins.input', return_value = 'Ban!@')
    def test_getUserInput_symbolsInput1(self,mock_inputs):
        with patch("ui.printWordRestrictionsError") as patched_function:
            getUserInput([])
        patched_function.assert_called()

    @patch('builtins.input', return_value = '!@#$%@')
    def test_getUserInput_symbolsInput2(self,mock_inputs):
        with patch("ui.printWordRestrictionsError") as patched_function:
            getUserInput([])
        patched_function.assert_called()

    @patch('builtins.input', return_value = 'henlo')
    def test_getUserInput_invalidWord1(self,mock_inputs):
        with patch("ui.printWordNotInDictionaryError") as patched_function:
            getUserInput([])
        patched_function.assert_called()

    @patch('builtins.input', return_value = 'phone')
    def test_getUserInput_priorInput(self,mock_inputs):
        with patch("ui.printPriorInputError") as patched_function:
            getUserInput(['phone', 'books'])
        patched_function.assert_called()

    @patch('builtins.input', return_value = 'plant')
    def test_getUserInput_validInput1(self, mock_inputs):
        result = getUserInput([])
        self.assertEqual(result, 'plant')

    @patch('builtins.input', return_value = 'abcde')
    def test_getUserInput_invalidWord2(self,mock_inputs):
        with patch("ui.printWordNotInDictionaryError") as patched_function:
            getUserInput([])
        patched_function.assert_called()

    @patch('builtins.input', return_value = 'rebel')
    def test_getUserInput_validInput2(self, mock_inputs):
        result = getUserInput([])
        self.assertEqual(result, 'rebel')

class GetRandomWord_Tests(unittest.TestCase):
    def test_getRandomWord_Positive(self) -> None:
        result = getRandomWord()
        self.assertTrue(len(result) == 5 and result.isalpha())

class CountLetters_Tests(unittest.TestCase):
    def test_countLetters_input1(self)-> None:
        expectedWord = "rebel"
        expectedOutput = { 'r': 1, 'e':2 , 'b': 1, 'l':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input2(self)-> None:
        expectedWord = "scary"
        expectedOutput = { 's': 1, 'c':1 , 'a': 1, 'r':1 , 'y':1}
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input3(self)-> None:
        expectedWord = "shots"
        expectedOutput = { 's': 2, 'h':1 , 'o': 1, 't':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input4(self)-> None:
        expectedWord = "tight"
        expectedOutput = { 't': 2, 'i':1 , 'g': 1, 'h':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input5(self)-> None:
        expectedWord = "seeks"
        expectedOutput = { 's': 2, 'e':2 , 'k': 1}
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input6(self)-> None:
        expectedWord = "rider"
        expectedOutput = { 'r': 2, 'i':1 , 'd': 1, 'e':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input7(self)-> None:
        expectedWord = "puppy"
        expectedOutput = { 'p': 3, 'u':1 , 'y': 1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input8(self)-> None:
        expectedWord = "pools"
        expectedOutput = { 'p': 1, 'o':2 , 'l': 1, 's':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input9(self)-> None:
        expectedWord = "occur"
        expectedOutput = { 'o': 1, 'c':2 , 'u': 1, 'r':1 }
        result = countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

class CheckWord_Tests(unittest.TestCase):
    def test_checkWord_input1(self) -> None:
        userInput = "banks"
        expectedWord = "sonic"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '"" "`')

    def test_checkWord_input2(self) -> None:
        userInput = "occur"
        expectedWord = "sonic"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '``"""')

    def test_checkWord_input3(self) -> None:
        userInput = ""
        expectedWord = ""
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, "")

    def test_checkWord_input4(self) -> None:
        userInput = "ocean"
        expectedWord = "rocky"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '``"""')

    def test_checkWord_input5(self) -> None:
        userInput = "mills"
        expectedWord = "flash"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '""`"`')

    def test_checkWord_input6(self) -> None:
        userInput = "crops"
        expectedWord = "codes"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, ' "`" ')

    def test_checkWord_input7(self) -> None:
        userInput = "chain"
        expectedWord = "chair"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '    "')

    def test_checkWord_input8(self) -> None:
        userInput = "peers"
        expectedWord = "pearl"
        result = checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '  " "')


    
if __name__ == '__main__':
    unittest.main()