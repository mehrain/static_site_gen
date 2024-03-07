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
            value = value.replace("'", '"')
            html += f' {key}="{value}"'
        return html