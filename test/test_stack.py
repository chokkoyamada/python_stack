import unittest
from hamcrest import *
from Stack import Stack

class StackTest(unittest.TestCase):
    def test_hoge(self):
        assert True

    def test_class(self):
        stack = Stack()
        assert stack.isEmpty() == True

        stack.push(1)
        assert stack.isEmpty() == False

        assert stack.size() == 1

        stack.push(2)

        stack.push(4)

        #assert stack.size() == 3
        assert_that(stack.size, equal_to(3))

        assert stack.pop() == 4

        assert stack.size() == 2

        assert stack.top() == 2

        assert stack.size() == 2






