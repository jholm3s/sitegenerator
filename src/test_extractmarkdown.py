import unittest

from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
    
    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
    
    def test_extract_markdown_images_with_link(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links_with_image_and_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) and another [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.example.com"), ("link", "https://www.google.com")], matches)
    
    def test_extract_markdown_images_with_image_and_link(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_links_with_no_links(self):
        matches = extract_markdown_links(
            "This is text with no links"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_with_no_images(self):
        matches = extract_markdown_images(
            "This is text with no images"
        )
        self.assertListEqual([], matches)
        
   
if __name__ == '__main__':
    unittest.main()