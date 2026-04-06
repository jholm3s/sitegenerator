import unittest

from splitimage import split_nodes_image
from textnode import TextNode, TextType

class TestSplitImage(unittest.TestCase):
    def test_split_image_no_images(self):
        text = "This is text with no images"
        new_text = split_nodes_image([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [TextNode(text, TextType.TEXT)])
    
    def test_split_image_one_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"        
        new_text = split_nodes_image([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ])
    
    def test_split_image_multiple_images(self):
        text = "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/fJRm4Vk.jpeg)"
        new_text = split_nodes_image([TextNode(text, TextType.TEXT)])
        self.assertEqual(new_text, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ])

    
if __name__ == '__main__':
    unittest.main()