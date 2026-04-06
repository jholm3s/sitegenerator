import unittest

from textnode import TextNode, TextType
from splitdelim import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("This is text with no code block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])
    
    def test_split_nodes_delimiter_unmatched_delimiter(self):
        node = TextNode("This is text with an unmatched `code block", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Invalid syntax: unmatched delimiter")
    
    def test_split_nodes_delimiter_non_text_node(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])
    
    
    def test_split_nodes_delimiter_only_delimiter(self):
        node = TextNode("`", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Invalid syntax: unmatched delimiter")
    
    def test_split_nodes_delimiter_delimiter_at_end(self):
        node = TextNode("This is a code block at the end`", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Invalid syntax: unmatched delimiter")
    
    def test_split_nodes_delimiter_delimiter_only_in_middle(self):
        node = TextNode("This is a `code block` in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT),
        ])
    
    def test_split_nodes_delimiter_delimiter_with_whitespace(self):
        node = TextNode("This is a ` code block ` with whitespace", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode(" code block ", TextType.CODE),
            TextNode(" with whitespace", TextType.TEXT),
        ])
    
    def test_split_nodes_delimiter_delimiter_with_unicode(self):
        node = TextNode("This is a `コードブロック` with unicode", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("コードブロック", TextType.CODE),
            TextNode(" with unicode", TextType.TEXT),
        ])

    
if __name__ == '__main__':
    unittest.main()