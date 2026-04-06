from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if node.type == TextType.TEXT:
            split_parts = node.text.split(delimiter)
            if len(split_parts) % 2 == 0:
                raise Exception("Invalid syntax: unmatched delimiter")
            for i, part in enumerate(split_parts):
                if part:  # Skip empty strings
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes