from textnode import TextNode, MarkDownExtractor

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

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        pass      
    '''

Check if the text_type of the node is text_type_text. If it's not, append the node to new_nodes and continue to the next iteration.

If the text_type of the node is text_type_text, create a MarkDownExtractor object with the text of the node.

Call the extract_markdown_images method of the MarkDownExtractor object to get a list of all images in the text. Each image is represented as a tuple containing the alt text and the URL of the image.

If there are no images in the text, append the node to new_nodes and continue to the next iteration.

If there are images in the text, iterate over each image in the list of images.

For each image, split the text of the node into two parts: the part before the image and the part including and after the image. You can use the str.split method with the markdown syntax of the image as the delimiter and 1 as the maximum number of splits.

Create a new TextNode with the part of the text before the image and append it to new_nodes.

Create a new TextNode with the alt text of the image, the URL of the image, and text_type set to text_type_image, and append it to new_nodes.

Update the text of the node to be the part of the text after the image.

After processing all images, if there's any text left in the node, create a new TextNode with this remaining text and append it to new_nodes.

After processing all nodes in old_nodes, return new_nodes.
    '''
    
    
        


