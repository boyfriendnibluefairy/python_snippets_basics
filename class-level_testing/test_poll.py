import unittest
from poll import AnonymousPoll

class TestAnonymousPoll(unittest.TestCase):
    """ Test cases for AnonymousPoll class """

    def setUp(self):
        """
        The setup() method creates variables and classes that
        can be used by all test cases.
        """
        q = "What computer language did you first learn to write?"
        self.my_poll = AnonymousPoll(q)
        self.answers = ["C","C++","Dart","Python"]

    def test_save_single_answer(self):
        """ Test that one answer is saved properly """
        self.my_poll.save_response(self.answers[0])
        self.assertIn(self.answers[0], self.my_poll.answers)

    def test_save_three_answers(self):
        """ Test class to check if it is able to save 3 responses properly """
        for answer in self.answers:
            self.my_poll.save_response(answer)
        for answer in self.answers:
            self.assertIn(answer,self.answers)

if __name__ == '__main__':
    unittest.main()