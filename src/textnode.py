from htmlnode import LeafNode
import re


class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False
    
    def __repr__(self):
        return f"text: {self.text}, text_type: {self.text_type}, url: {self.url}"
    
    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(value=self.text)
        elif self.text_type == "bold":
            return LeafNode(tag="b", value=self.text)
        elif self.text_type == "italic":
            return LeafNode(tag="i", value=self.text)
        elif self.text_type == "code":
            return LeafNode(tag="code", value=self.text)
        elif self.text_type == "link":
            return LeafNode(tag="a", value=self.text, props={"href": self.url})
        elif self.text_type == "image":
            return LeafNode(tag="img", props={"src": self.url, "alt": self.text})
        else:
            raise ValueError(f"Unknown text type: {self.text_type}")
        
    def extract_markdown_text_nodes(self, text):
        images = self.extract_markdown_images(text)
        links = self.extract_markdown_links(text)
        text_nodes = []
        for image in images:
            text = image[0]
            url = image[1]
            text_nodes.append(TextNode(text=text, text_type="image", url=url))
        for link in links:
            text = link[0]
            url = link[1]
            text_nodes.append(TextNode(text=text, text_type="link", url=url))
        return text_nodes
    
class MarkDownExtractor:
    def __init__(self, text=None):
        self.text = text
    
    def extract_markdown_images(self):
        if self.text is None:
            raise ValueError("No text provided")
        return re.findall(r"!\[(.*?)\]\((.*?)\)", self.text)
    
    def extract_markdown_links(self):
        if self.text is None:
            raise ValueError("No text provided")
        return re.findall(r"\[(.*?)\]\((.*?)\)", self.text)
