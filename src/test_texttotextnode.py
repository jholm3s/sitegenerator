import unittest

from textnode import TextNode, TextType
from texttotextnode import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)
    
    def test_plain_text(self):
        # No markdown at all
        nodes = text_to_textnodes("Just plain text")
        self.assertEqual(nodes, [TextNode("Just plain text", TextType.TEXT)])

    def test_bold_only(self):
        nodes = text_to_textnodes("**bold**")
        self.assertEqual(nodes, [TextNode("bold", TextType.BOLD)])

    def test_multiple_bold(self):
        nodes = text_to_textnodes("**one** and **two**")
        self.assertEqual(nodes, [
            TextNode("one", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
        ])



if __name__ == "__main__":
    unittest.main()
