
import os
import pep8
import unittest
import fnmatch


class Test(unittest.TestCase):

    def test_pep8_conformance_unitests(self):
        """Pep8 conformance test (unitests)

        Runs on the unittest directory.
        """

        print("\r\n")

        # Get the path to current directory
        path = os.path.dirname(os.path.realpath(__file__))

        self.run_check(path)

    def test_pep8_conformance_pygccxml(self):
        """Pep8 conformance test (pygccxml)

        Runs on the pygccxml directory.
        """

        print("\r\n")

        # Get the path to current directory
        path = os.path.dirname(os.path.realpath(__file__))
        path += "/../pygccxml/"

        self.run_check(path)

    def test_pep8_conformance_example(self):
        """Pep8 conformance test (examples)

        Runs on the example file in the docs.
        """

        print("\r\n")

        # Get the path to current directory
        path = os.path.dirname(os.path.realpath(__file__))
        path += "/../docs/examples/"

        # Find all the examples files
        file_paths = []
        for root, dirnames, filenames in os.walk(path):
            for file_path in fnmatch.filter(filenames, '*.py'):
                file_paths.append(os.path.join(root, file_path))

        for path in file_paths:
            self.run_check(path)

    def test_pep8_conformance_setup(self):
        """Pep8 conformance test (setup)

        Runs on the setup.py file
        """

        print("\r\n")

        # Get the path to current directory
        path = os.path.dirname(os.path.realpath(__file__))
        path += "/../setup.py"

        self.run_check(path)

    def run_check(self, path):
        """Common method to run the pep8 test."""

        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(paths=[path])

        if result.total_errors != 0:
            self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings).")


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite


def run_suite():
    unittest.TextTestRunner(verbosity=2).run(create_suite())

if __name__ == "__main__":
    run_suite()
