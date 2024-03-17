from textnode import *
from htmlnode import *
import re

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

def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        if isinstance(node, TextNode) and node.text_type == "text":
            text = node.text
            prev_end = 0
            for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", text):
                alt_text, image_url = match.groups()
                start, end = match.span()
                if start > prev_end:
                    new_nodes.append(TextNode(text=text[prev_end:start], text_type="text"))
                new_nodes.append(TextNode(text=alt_text, text_type="image", url=image_url))
                prev_end = end
            if prev_end < len(text):
                new_nodes.append(TextNode(text=text[prev_end:], text_type="text"))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        if isinstance(node, TextNode) and node.text_type == "text":
            text = node.text
            prev_end = 0
            for match in re.finditer(r"\[(.*?)\]\((.*?)\)", text):
                link_text, link_url = match.groups()
                start, end = match.span()
                if start > prev_end:
                    new_nodes.append(TextNode(text=text[prev_end:start], text_type="text"))
                new_nodes.append(TextNode(text=link_text, text_type="link", url=link_url))
                prev_end = end
            if prev_end < len(text):
                new_nodes.append(TextNode(text=text[prev_end:], text_type="text"))
        else:
            new_nodes.append(node)
    return new_nodes
