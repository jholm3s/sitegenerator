import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )
    
    def test_to_html_with_nested_children(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i></span></div>",
        )
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )
    
    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={})
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )
    
    def test_to_html_with_none_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props=None)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )
    
    def test_to_html_with_none_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_none_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_empty_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<><span>child</span></>",
        )
    
    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )
    
    def test_to_html_with_empty_tag_and_children(self):
        parent_node = ParentNode("", [])
        self.assertEqual(
            parent_node.to_html(),
            "<></>",
        )
    
    def test_to_html_with_empty_tag_and_none_children(self):
        parent_node = ParentNode("", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_none_tag_and_empty_children(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    
    
    if __name__ == "__main__":
        unittest.main()