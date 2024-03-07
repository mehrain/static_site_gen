import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node1 = TextNode("Hello", "greeting", "http://example.com")
        self.node2 = TextNode("Hello", "greeting", "http://example.com")
        self.node3 = TextNode("Goodbye", "farewell", "http://example2.com")

    def test_eq(self):
        self.assertEqual(self.node1, self.node2)
        self.assertNotEqual(self.node1, self.node3)

    def test_repr(self):
        expected_repr = "text: Hello, text_type: greeting, url: http://example.com"
        self.assertEqual(repr(self.node1), expected_repr)


if __name__ == "__main__":
    unittest.main()