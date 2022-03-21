import unittest
from unittest.mock import patch
from dictionary import Dictionary
from statistics import calculateLikelyhood, listToTuple, parseStatisticToTuple, writeInLetterFrequency, writeWordRank
from ui import UI

class WordIsEqualToInput_Tests(unittest.TestCase):
    def test_wordIsEqualToInput_wrongInput1(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "Books"
        self.assertFalse(ui_obj.wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_wrongInput2(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "Pitch"
        self.assertFalse(ui_obj.wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_wrongInput3(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "Hello"
        self.assertFalse(ui_obj.wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_wrongInput4(self) -> None:
        """Test wordIsEqualToInput method with wrong input - return false"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "Clubs"
        self.assertFalse(ui_obj.wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_correctInput1(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "Banks"
        self.assertTrue(ui_obj.wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput2(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        ui_obj = UI()
        expectedWord = "abuse"
        userInput = "abuse"
        self.assertTrue(ui_obj.wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput3(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        ui_obj = UI()
        expectedWord = "Goals"
        userInput = "Goals"
        self.assertTrue(ui_obj.wordIsEqualToInput(expectedWord, userInput))

    def test_wordIsEqualToInput_correctInput4(self) -> None:
        """Test wordIsEqualToInput method with correct input - return true"""
        ui_obj = UI()
        expectedWord = "about"
        userInput = "about"
        self.assertTrue(ui_obj.wordIsEqualToInput(expectedWord, userInput))
    
    def test_wordIsEqualToInput_caseSensitive(self) -> None:
        """Test wordIsEqualToInput method with correct input - return false"""
        ui_obj = UI()
        expectedWord = "Banks"
        userInput = "BANKS"
        self.assertFalse(ui_obj.wordIsEqualToInput(expectedWord, userInput))

class IsWordValidDictionaryWord_Tests(unittest.TestCase):
    def test_isWordValidDictionaryWord_wrongInput1(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        ui_obj = UI()
        userInput = "xyzzz"
        self.assertFalse(ui_obj.isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_wrongInput2(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        ui_obj = UI()
        userInput = "champ"
        self.assertFalse(ui_obj.isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_wrongInput3(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        ui_obj = UI()
        userInput = "classy"
        self.assertFalse(ui_obj.isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_wrongInput4(self) -> None:
        """Test isWordValidDictionaryWord method with wrong input - return false"""
        ui_obj = UI()
        userInput = "plants"
        self.assertFalse(ui_obj.isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_correctInput1(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        ui_obj = UI()
        userInput = "abuse"
        self.assertTrue(ui_obj.isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_correctInput2(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        ui_obj = UI()
        userInput = "later"
        self.assertTrue(ui_obj.isWordValidDictionaryWord(userInput))
    
    def test_isWordValidDictionaryWord_correctInput3(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        ui_obj = UI()
        userInput = "laugh"
        self.assertTrue(ui_obj.isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_correctInput4(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        ui_obj = UI()
        userInput = "menus"
        self.assertTrue(ui_obj.isWordValidDictionaryWord(userInput))

    def test_isWordValidDictionaryWord_caseSensitive(self) -> None:
        """Test isWordValidDictionaryWord method with correct input - return true"""
        ui_obj = UI()
        userInput = "LAUGH"
        self.assertFalse(ui_obj.isWordValidDictionaryWord(userInput))

class CheckLengthNotFiveAndAlphabets_Tests(unittest.TestCase):
    def test_checkLengthNotFiveAndAlphabets_wrongInput1(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        ui_obj = UI()
        userInput = "laughs"
        self.assertTrue(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput2(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        ui_obj = UI()
        userInput = "book"
        self.assertTrue(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput3(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        ui_obj = UI()
        userInput = "geek"
        self.assertTrue(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_wrongInput4(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input - return true"""
        ui_obj = UI()
        userInput = "mock"
        self.assertTrue(ui_obj.checkLengthNotFiveAndAlphabets(userInput))
    
    def test_checkLengthNotFiveAndAlphabets_correctInput1(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        ui_obj = UI()
        userInput = "laugh"
        self.assertFalse(ui_obj.checkLengthNotFiveAndAlphabets(userInput))
    
    def test_checkLengthNotFiveAndAlphabets_correctInput2(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        ui_obj = UI()
        userInput = "menus"
        self.assertFalse(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_correctInput3(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        ui_obj = UI()
        userInput = "mercy"
        self.assertFalse(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_correctInput4(self) -> None:
        """Test checkLengthFiveAndAlphabets function with correct input(length == 5) - return false"""
        ui_obj = UI()
        userInput = "naval"
        self.assertFalse(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

    def test_checkLengthNotFiveAndAlphabets_symbolInput(self) -> None:
        """Test checkLengthFiveAndAlphabets function with wrong input(contains symbols) - return true"""
        ui_obj = UI()
        userInput = "n@!al"
        self.assertTrue(ui_obj.checkLengthNotFiveAndAlphabets(userInput))

class GetUserInput_Tests(unittest.TestCase):
    @patch('builtins.input', return_value = '')
    def test_getUserInput_blankInput(self, mock_inputs):
        ui_obj = UI()
        result = ui_obj.getUserInput([])
        self.assertEqual(result, 0)

    # @patch('builtins.input', return_value = 'hey')
    # def test_getUserInput_lessCharacters(self,mock_inputs):
    #     with patch("ui.printWordRestrictionsError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput([])
    #     patched_function.assert_called()

    # @patch('builtins.input', return_value = 'Ban!@')
    # def test_getUserInput_symbolsInput1(self,mock_inputs):
    #     with patch("ui.printWordRestrictionsError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput([])
    #     patched_function.assert_called()

    # @patch('builtins.input', return_value = '!@#$%@')
    # def test_getUserInput_symbolsInput2(self,mock_inputs):
    #     with patch("ui.printWordRestrictionsError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput([])
    #     patched_function.assert_called()

    # @patch('builtins.input', return_value = 'henlo')
    # def test_getUserInput_invalidWord1(self,mock_inputs):
    #     with patch("ui.printWordNotInDictionaryError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput([])
    #     patched_function.assert_called()

    # @patch('builtins.input', return_value = 'phone')
    # def test_getUserInput_priorInput(self,mock_inputs):
    #     with patch("ui.printPriorInputError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput(['phone', 'books'])
    #     patched_function.assert_called()

    # @patch('builtins.input', return_value = 'plant')
    # def test_getUserInput_validInput1(self, mock_inputs):
    #     ui_obj = UI()
    #     result = ui_obj.getUserInput([])
    #     self.assertEqual(result, 'plant')

    # @patch('builtins.input', return_value = 'abcde')
    # def test_getUserInput_invalidWord2(self,mock_inputs):
    #     with patch("ui.printWordNotInDictionaryError") as patched_function:
    #         ui_obj = UI()
    #         ui_obj.getUserInput([])
    #     patched_function.assert_called()

    @patch('builtins.input', return_value = 'rebel')
    def test_getUserInput_validInput2(self, mock_inputs):
        ui_obj = UI()
        result = ui_obj.getUserInput([])
        self.assertEqual(result, 'rebel')

class GetRandomWord_Tests(unittest.TestCase):
    def test_getRandomWord_Positive(self) -> None:
        dict = Dictionary()
        selectedList = ["books", "marks"]
        result = dict.getRandomWord(selectedList)
        self.assertTrue(len(result) == 5 and result.isalpha())

class CountLetters_Tests(unittest.TestCase):
    def test_countLetters_input1(self)-> None:
        dict = Dictionary()
        expectedWord = "rebel"
        expectedOutput = { 'r': 1, 'e':2 , 'b': 1, 'l':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input2(self)-> None:
        dict = Dictionary()
        expectedWord = "scary"
        expectedOutput = { 's': 1, 'c':1 , 'a': 1, 'r':1 , 'y':1}
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input3(self)-> None:
        dict = Dictionary()
        expectedWord = "shots"
        expectedOutput = { 's': 2, 'h':1 , 'o': 1, 't':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input4(self)-> None:
        dict = Dictionary()
        expectedWord = "tight"
        expectedOutput = { 't': 2, 'i':1 , 'g': 1, 'h':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input5(self)-> None:
        dict = Dictionary()
        expectedWord = "seeks"
        expectedOutput = { 's': 2, 'e':2 , 'k': 1}
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input6(self)-> None:
        dict = Dictionary()
        expectedWord = "rider"
        expectedOutput = { 'r': 2, 'i':1 , 'd': 1, 'e':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input7(self)-> None:
        dict = Dictionary()
        expectedWord = "puppy"
        expectedOutput = { 'p': 3, 'u':1 , 'y': 1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input8(self)-> None:
        dict = Dictionary()
        expectedWord = "pools"
        expectedOutput = { 'p': 1, 'o':2 , 'l': 1, 's':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

    def test_countLetters_input9(self)-> None:
        dict = Dictionary()
        expectedWord = "occur"
        expectedOutput = { 'o': 1, 'c':2 , 'u': 1, 'r':1 }
        result = dict.countLetters(expectedWord)
        self.assertEqual(result, expectedOutput)

class CheckWord_Tests(unittest.TestCase):
    def test_checkWord_input1(self) -> None:
        dict = Dictionary()
        userInput = "banks"
        expectedWord = "sonic"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '"" "`')

    def test_checkWord_input2(self) -> None:
        dict = Dictionary()
        userInput = "occur"
        expectedWord = "sonic"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '``"""')

    def test_checkWord_input3(self) -> None:
        dict = Dictionary()
        userInput = ""
        expectedWord = ""
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, "")

    def test_checkWord_input4(self) -> None:
        dict = Dictionary()
        userInput = "ocean"
        expectedWord = "rocky"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '``"""')

    def test_checkWord_input5(self) -> None:
        dict = Dictionary()
        userInput = "mills"
        expectedWord = "flash"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '""`"`')

    def test_checkWord_input6(self) -> None:
        dict = Dictionary()
        userInput = "crops"
        expectedWord = "codes"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, ' "`" ')

    def test_checkWord_input7(self) -> None:
        dict = Dictionary()
        userInput = "chain"
        expectedWord = "chair"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '    "')

    def test_checkWord_input8(self) -> None:
        dict = Dictionary()
        userInput = "peers"
        expectedWord = "pearl"
        result = dict.checkWord(userInput, expectedWord)
        result = ''.join(result)
        self.assertEqual(result, '  " "')

class CheckWord_Tests(unittest.TestCase):
    def test_listToTuple_function(self)->None:
        result = listToTuple()
        for key in result:
            self.assertTrue(type(result[key]) is tuple) 
    
    def test_checkstats_input1(self)->None:
        result = calculateLikelyhood()
        self.assertEqual(len(result),1379)
    
    def test_writeWordRank_function(self)->None:
        writeWordRank()
        file1 = open('wordRank.csv', 'r')
        words = file1.readlines()
        file1.close()
        self.assertEqual(len(words), 1379)
    
    def test_writeInLetterFrequency_function(self)->None:
        writeInLetterFrequency()
        file1 = open('letterFrequency.csv', 'r')
        lines = file1.readlines()
        file1.close()
        self.assertEqual(len(lines),26)

    def test_parseStatisticToTuple_function(self)->None:
        result = parseStatisticToTuple()
        for key in result:
            self.assertTrue(type(result[key]) is tuple)

if __name__ == '__main__':
    unittest.main()