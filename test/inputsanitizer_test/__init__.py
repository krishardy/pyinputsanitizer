import unittest

from inputsanitizer import *


class InputTestCase(unittest.TestCase):
    def test__init__(self):
        uut = Input()

    def test_sanitize(self):
        uut = Input(str)
        self.assertEqual(uut.sanitize(""), "")
        self.assertEqual(uut.sanitize("a"), "a")

        uut = Input(str, required=True, default="x")
        self.assertEqual(uut.sanitize(""), "x")
        self.assertEqual(uut.sanitize("a"), "a")

        uut = Input(str, r"^abc$")
        self.assertEqual(uut.sanitize("abc"), "abc")
        self.assertEqual(uut.sanitize(""), None)
        self.assertEqual(uut.sanitize("a"), None)

        uut = Input(str, r"^abc$", default="x")
        self.assertEqual(uut.sanitize("abc"), "abc")
        self.assertEqual(uut.sanitize(""), "x")
        self.assertEqual(uut.sanitize("a"), "x")

        uut = Input(str, r"^abc", default="x",
                precast_parser=lambda s: x + "!")
        self.assertEqual(uut.sanitize("abc"), "abc!")
        self.assertEqual(uut.sanitize(""), "x")
        self.assertEqual(uut.sanitize("a"), "x")

        uut = Input(str, r"^abc$", default="x",
                precast_parser=lambda s: x + "!",
                postcast_parser=lambda s: s + "@")
        self.assertEqual(uut.sanitize("abc"), "abc!@")
        self.assertEqual(uut.sanitize(""), "x")
        self.assertEqual(uut.sanitize("a"), "x")

        uut = Input(str, r"^abc$", default="x",
                precast_parser=lambda s: x + "!",
                postcast_parser=lambda s: s + "@")
        self.assertEqual(uut.sanitize("abc"), "abc!@")
        self.assertEqual(uut.sanitize(""), "x")
        self.assertEqual(uut.sanitize("a"), "x")

class IntInputTestCase(unittest.TestCase):
    def test__init__(self):
        raise unittest.SkipTest()
        self.assertFalse(True)

    def test_sanitize(self):
        raise unittest.SkipTest()
        self.assertFalse(True)


class FloatInput(unittest.TestCase):
    def test__init__(self):
        raise unittest.SkipTest()
        self.assertFalse(True)

    def test_sanitize(self):
        raise unittest.SkipTest()
        self.assertFalse(True)


class MACInput(unittest.TestCase):
    def test__init__(self):
        raise unittest.SkipTest()
        self.assertFalse(True)

    def test_sanitize(self):
        raise unittest.SkipTest()
        self.assertFalse(True)


class ListInput(unittest.TestCase):
    def test__init__(self):
        raise unittest.SkipTest()
        self.assertFalse(True)

    def test_sanitize(self):
        raise unittest.SkipTest()
        self.assertFalse(True)

