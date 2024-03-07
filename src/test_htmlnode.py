import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node1 = HTMLNode("p", "Hello", None, {"class": "greeting", "id": "greeting1"})
        self.node2 = HTMLNode("p", "Goodbye", None, {"class": "farewell", "id": "farewell1"})

    def test_repr(self):
        expected_repr = "tag: p, value: Hello, children: [], props: {'class': 'greeting', 'id': 'greeting1'}"
        self.assertEqual(repr(self.node1), expected_repr)

    def test_props_to_html(self):
        expected_props_html = ' class="greeting" id="greeting1"'
        self.assertEqual(self.node1.props_to_html(), expected_props_html)

if __name__ == "__main__":
    unittest.main()