import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.leaf1 = LeafNode("p", "Hello", {"class": "greeting", "id": "greeting1"})
        self.leaf2 = LeafNode(None, "Hello", {"class": "greeting", "id": "greeting1"})
        self.leaf3 = LeafNode("p", None, {"class": "greeting", "id": "greeting1"})

    def test_to_html(self):
        self.assertEqual(self.leaf1.to_html(), '<p class="greeting" id="greeting1">Hello</p>')
        self.assertEqual(self.leaf2.to_html(), 'Hello')
        with self.assertRaises(ValueError):
            self.leaf3.to_html()
            
class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.node1 = ParentNode("div", None, [LeafNode("p", "Hello", {"class": "greeting", "id": "greeting1"})], {"class": "container"})
        self.node2 = ParentNode("div", None, [LeafNode("p", "Goodbye", {"class": "farewell", "id": "farewell1"})], {"class": "container"})
        self.node3 = ParentNode(None, None, [LeafNode("p", "Hello", {"class": "greeting", "id": "greeting1"})], {"class": "container"})
        self.node4 = ParentNode("div", None, None, {"class": "container"})

    def test_to_html(self):
        self.assertEqual(self.node1.to_html(), '<div class="container"><p class="greeting" id="greeting1">Hello</p></div>')
        self.assertEqual(self.node2.to_html(), '<div class="container"><p class="farewell" id="farewell1">Goodbye</p></div>')
        with self.assertRaises(ValueError):
            self.node3.to_html()
        with self.assertRaises(ValueError):
            self.node4.to_html()