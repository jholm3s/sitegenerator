from enum import Enum

from parentnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from texttotextnode import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

class BlockType(Enum):
    PARAGRAPH           = 'paragraph'
    HEADING             = 'heading'
    CODE                = 'code'
    QUOTE               = 'quote'
    ULIST               = 'unordered_list'
    OLIST               = 'ordered_list'

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if (
        len(block) > 0
        and block[0] == "#"
    ):
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
            else:
                break
        if 1 <= heading_level <= 6 and len(block) > heading_level and block[heading_level] == " ":
            return BlockType.HEADING

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.ULIST

    ordered = True
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            ordered = False
            break
    if ordered:
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        block_list.append(block_node)
    return ParentNode("div", block_list)



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        block_list = block.split("\n")
        text = " ".join(block_list)
        return ParentNode("p", text_to_children(text))
    if block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        content = block[level + 1 :]
        return ParentNode(f"h{level}", text_to_children(content))
    if block_type == BlockType.CODE:
        content = block[3:-3].lstrip("\n")
        raw_node = TextNode(content, TextType.TEXT)
        raw_html = text_node_to_html_node(raw_node)
        code_node = ParentNode("code", [raw_html])
        return ParentNode("pre", [code_node])
    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        content = " ".join(line.lstrip("> ").strip() for line in lines)
        return ParentNode("blockquote", text_to_children(content))
    if block_type == BlockType.ULIST:
        lines = block.split("\n")
        list_items = []
        for line in lines:
            content = line[2:]
            list_items.append(ParentNode("li", text_to_children(content)))
        return ParentNode("ul", list_items)
    if block_type == BlockType.OLIST:
        lines = block.split("\n")
        list_items = []
        for line in lines:
            content = line.split(". ", 1)[1]
            list_items.append(ParentNode("li", text_to_children(content)))
        return ParentNode("ol", list_items)
    raise ValueError("Invalid block type")


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            clean_title = line[1:].strip()
            if clean_title.startswith("#") is False:
                return clean_title
    raise Exception("No title found in markdown")


