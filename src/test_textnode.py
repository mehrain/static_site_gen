import unittest
from textnode import TextNode
from textnode import MarkDownExtractor




class TestTextNodeEquality(unittest.TestCase):
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
        
class TestTextNodeRepresentation(unittest.TestCase):
    def setUp(self):
        self.node1 = TextNode(text_type="text", text="Hello")
        self.node2 = TextNode(text_type="bold", text="Hello")
        self.node3 = TextNode(text_type="italic", text="Hello")
        self.node4 = TextNode(text_type="code", text="Hello")
        self.node5 = TextNode(text_type="link", text="Hello", url="http://example.com")
        self.node6 = TextNode(text_type="image", text="Hello", url="http://example.com/image.png")
        self.node7 = TextNode(text_type="unknown", text="Hello")

    def test_text_node_representation(self):
        expected_repr1 = "text: Hello, text_type: text"
        expected_repr2 = "text: Hello, text_type: bold"
        expected_repr3 = "text: Hello, text_type: italic"
        expected_repr4 = "text: Hello, text_type: code"
        expected_repr5 = "text: Hello, text_type: link, url: http://example.com"
        expected_repr6 = "text: Hello, text_type: image, url: http://example.com/image.png"
        expected_repr7 = "text: Hello, text_type: unknown"

        self.assertEqual(repr(self.node1), expected_repr1)
        self.assertEqual(repr(self.node2), expected_repr2)
        self.assertEqual(repr(self.node3), expected_repr3)
        self.assertEqual(repr(self.node4), expected_repr4)
        self.assertEqual(repr(self.node5), expected_repr5)
        self.assertEqual(repr(self.node6), expected_repr6)
        self.assertEqual(repr(self.node7), expected_repr7)

class TestTextNodeToHtmlNode(unittest.TestCase):
    def setUp(self):
        self.node1 = TextNode(text_type="text", text="Hello")
        self.node2 = TextNode(text_type="bold", text="Hello")
        self.node3 = TextNode(text_type="italic", text="Hello")
        self.node4 = TextNode(text_type="code", text="Hello")
        self.node5 = TextNode(text_type="link", text="Hello", url="http://example.com")
        self.node6 = TextNode(text_type="image", text="Hello", url="http://example.com/image.png")
        self.node7 = TextNode(text_type="unknown", text="Hello")

    def test_text_node_to_html_node(self):
        self.assertEqual(self.node1.text_node_to_html_node().to_html(), 'Hello')
        self.assertEqual(self.node2.text_node_to_html_node().to_html(), '<b>Hello</b>')
        self.assertEqual(self.node3.text_node_to_html_node().to_html(), '<i>Hello</i>')
        self.assertEqual(self.node4.text_node_to_html_node().to_html(), '<code>Hello</code>')
        self.assertEqual(self.node5.text_node_to_html_node().to_html(), '<a href="http://example.com">Hello</a>')
        self.assertEqual(self.node6.text_node_to_html_node().to_html(), '<img src="http://example.com/image.png" alt="Hello">')
        with self.assertRaises(ValueError):
            self.node7.text_node_to_html_node()


class TestMarkDownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        extractor = MarkDownExtractor("This is text with an image ![alt text](https://www.example.com/image.jpg)")
        expected = [("alt text", "https://www.example.com/image.jpg")]
        self.assertEqual(extractor.extract_markdown_images(), expected)

    def test_extract_markdown_links(self):
        extractor = MarkDownExtractor("This is text with a [link](https://www.example.com)")
        expected = [("link", "https://www.example.com")]
        self.assertEqual(extractor.extract_markdown_links(), expected)

    def test_no_text(self):
        extractor = MarkDownExtractor()
        with self.assertRaises(ValueError):
            extractor.extract_markdown_images()
        with self.assertRaises(ValueError):
            extractor.extract_markdown_links()

if __name__ == "__main__":
    unittest.main()

