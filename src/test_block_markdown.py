import unittest

from block_markdown import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node, extract_title
from htmlnode import HTMLNode



class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\nThis is a code block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- This is a list item"), BlockType.ULIST)
        self.assertEqual(block_to_block_type("1. This is a numbered list item"), BlockType.OLIST)
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    

    def test_extract_title(self):
        md = """
# This is a title
This is some text after the title
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")

    
    def test_extract_title_with_two_headers(self):
        md = """
# This is a title
# This is a second title
This is some text after the title(s)
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")
    
    def test_extract_title_with_no_title(self):
        md = """
This is some text without a title
"""
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_with_empty_string(self):
        md = ""
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_extract_title_with_no_headers(self):
        md = """
This is some text without a title
"""
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_extract_title_with_h2_only(self):
        md = """
## This is a title
"""
        with self.assertRaises(Exception):
            extract_title(md)
    

    if __name__ == "__main__":
        unittest.main()