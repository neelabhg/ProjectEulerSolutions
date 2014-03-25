import unittest
import os
import imp


class TestSolutions(unittest.TestCase):
    """
    Test case for testing the solutions.
    Tests are added dynamically to this class, based on entries in answers.txt.
    """
    pass


def create_test(problem_num, expected_answer):

    # From stackoverflow: "How to import a module given the full path?"
    # http://stackoverflow.com/a/67692/2193410
    package_name = 'problem%d' % problem_num
    module_path = 'problems/%s/solution.py' % package_name
    path = os.path.join(os.path.dirname(__file__), module_path)
    m = imp.load_source(package_name, path)

    def do_test(self):
        self.assertEqual(m.solution(), expected_answer)
    return do_test

if __name__ == '__main__':
    answers = []
    try:
        with open('answers.txt', 'r') as f:
            for line in f:
                if not (line.startswith('#') or line.strip() == ""):
                    answers.append(line.split()[1])
    except (IOError, IndexError) as e:
        print "Error: ", e

    # From stackoverflow: "Python unittest: Generate multiple tests programmatically?"
    # http://stackoverflow.com/a/2799009/2193410
    for problem, answer in enumerate(answers):
        test_method = create_test(problem + 1, int(answer))
        test_method.__name__ = 'test_solution%d' % (problem + 1)
        setattr(TestSolutions, test_method.__name__, test_method)

    unittest.main()
