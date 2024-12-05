#!/usr/bin/env python
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover(".")
    testrunner = unittest.TextTestRunner()
    testrunner.verbosity = 2
    testrunner.run(tests)
