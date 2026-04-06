from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_links


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link_text, link_url in links:
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
