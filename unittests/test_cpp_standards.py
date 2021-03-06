# Copyright 2014-2016 Insight Software Consortium.
# Distributed under the Boost Software License, Version 1.0.
# See http://www.boost.org/LICENSE_1_0.txt

import unittest
import parser_test_case

from pygccxml import parser


class Test(parser_test_case.parser_test_case_t):

    def test(self):
        """
        Test different compilation standards by setting cflags.

        """

        # Skip this test for gccxml, this is a CastXML feature.
        if "gccxml" in self.config.xml_generator:
            return True

        parser.parse(["cpp_standards.hpp"], self.config)

        self.config.cflags = "-std=c++98"
        parser.parse(["cpp_standards.hpp"], self.config)

        self.config.cflags = "-std=c++03"
        parser.parse(["cpp_standards.hpp"], self.config)

        self.config.cflags = "-std=c++11"
        parser.parse(["cpp_standards.hpp"], self.config)

        # This is broken with llvm 3.6.2 (the one from homebrew)
        # It should work with never llvms but I keep the test disabled
        # See https://llvm.org/bugs/show_bug.cgi?id=24872
        # self.config.cflags = "-std=c++14"
        # parser.parse(["cpp_standards.hpp"], self.config)

        # Same as above
        # self.config.cflags = "-std=c++1z"
        # parser.parse(["cpp_standards.hpp"], self.config)

        # Pass down a flag that does not exist.
        # This should raise an exception.
        self.config.cflags = "-std=c++00"
        self.assertRaises(
            RuntimeError,
            lambda: parser.parse(["cpp_standards.hpp"], self.config))


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite


def run_suite():
    unittest.TextTestRunner(verbosity=2).run(create_suite())

if __name__ == "__main__":
    run_suite()
