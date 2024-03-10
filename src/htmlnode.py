class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
        
    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
       
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")
        else:
            html = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                html += child.to_html()
            html += f"</{self.tag}>"
            return html
