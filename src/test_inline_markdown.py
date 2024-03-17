import unittest
from textnode import *
from inline_markdown import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_text_nodes(self):
        old_nodes = [
            TextNode(text="This is normal text.", text_type="text"),
            TextNode(text="**This is bold text.**", text_type="text"),
            TextNode(text="*This is italic text.*", text_type="text"),
            TextNode(text="`This is code.`", text_type="text"),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")
        new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
        new_nodes = split_nodes_delimiter(new_nodes, "`", "code")

        expected_nodes = [
            TextNode(text="This is normal text.", text_type="text"),
            TextNode(text="", text_type="text"),
            TextNode(text="This is bold text.", text_type="bold"),
            TextNode(text="", text_type="text"),
            TextNode(text="", text_type="text"),
            TextNode(text="This is italic text.", text_type="italic"),
            TextNode(text="", text_type="text"),
            TextNode(text="", text_type="text"),
            TextNode(text="This is code.", text_type="code"),
            TextNode(text="", text_type="text"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_non_text_nodes(self):
        old_nodes = [
            TextNode(text="This is normal text.", text_type="text"),
            TextNode(text="This is bold text.", text_type="bold"),
            123,  # Some non-TextNode object
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")

        expected_nodes = [
            TextNode(text="This is normal text.", text_type="text"),
            TextNode(text="This is bold text.", text_type="bold"),
            123,
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_invalid_text_type(self):
        old_nodes = [
            TextNode(text="This is normal text.", text_type="text"),
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", "invalid")



def test_split_nodes_image_no_image(self):
    node = TextNode("This is a text without an image.", text_type_text)
    new_nodes = split_nodes_image([node])
    self.assertEqual(new_nodes, [node])

def test_split_nodes_link_no_link(self):
    node = TextNode("This is a text without a link.", text_type_text)
    new_nodes = split_nodes_link([node])
    self.assertEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()