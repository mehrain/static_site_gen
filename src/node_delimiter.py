from textnode import TextNode

def split_nodes_delimiter(old_nodes=None, delimiter=None, text_type=None):
    if old_nodes is None:
        raise ValueError('old_nodes is required as a list of TextNode objects')
    if delimiter is None:
        raise ValueError('delimiter is required, please enter a string')
    if text_type is None:
        raise ValueError('text_type is required, please enter a string')
    
    valid_text_types = [
        "text",
        "bold",
        "italic",
        "code",
        "link",
        "image"
    ]
    
    if text_type not in valid_text_types:
        raise ValueError('Invalid text_type. Please provide one of the valid text_type values.')
    
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != "text":
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if i % 2:
                new_type = text_type
            else:
                new_type = "text"
            new_nodes.append(TextNode(text=text, text_type=new_type))
    return new_nodes
        


