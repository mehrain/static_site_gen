from htmlnode import LeafNode

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

