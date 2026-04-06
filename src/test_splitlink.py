import unittest

from splitlink import split_nodes_link
from textnode import TextNode, TextType

class TestSplitLink(unittest.TestCase):
    def test_split_link_no_links(self):
        text = "This is text with no links"
        new_text = split_nodes_link([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [TextNode(text, TextType.TEXT)])
    
    def test_split_link_one_link(self):
        text = "This is text with a [link](https://www.example.com)"
        new_text = split_nodes_link([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
        ])
    
    def test_split_link_multiple_links(self):
        text = "This is text with a [link1](https://www.example.com) and another [link2](https://www.google.com)"
        new_text = split_nodes_link([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "https://www.example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "https://www.google.com"),
        ])
    
    def test_split_link_links_with_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.example.com)"
        new_text = split_nodes_link([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
        ])
    
    def test_split_link_links_with_images_and_links(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.example.com)"
        new_text = split_nodes_link([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
        ])
    
if __name__ == '__main__':
    unittest.main()