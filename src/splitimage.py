from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
            
        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes