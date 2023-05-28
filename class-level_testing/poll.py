## Sample Class to Test
class AnonymousPoll:
    """ Collect anonymous responses to a poll question. """

    def __init__(self, query):
        """ Store a query, and prepare to store the responses """
        self.query = query
        self.answers = []

    def display_question(self):
        """ display the poll question """
        print(self.query)

    def save_response(self, new_answer):
        """ save a single answer to the survey """
        self.answers.append(new_answer)

    def display_results(self):
        """ display all answers that were saved """
        print("\n Survey Results:\n")
        for answer in self.answers:
            print(f" - {answer}")

