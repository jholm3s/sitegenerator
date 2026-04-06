import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'container'})
    
    def test_props_to_html(self):
        node = HTMLNode(props={'class': 'container', 'id': 'main'})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')
        
        node_empty = HTMLNode()
        self.assertEqual(node_empty.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'class': 'container'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})")

    def test_repr_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=None, props=None)")

    def test_repr_with_children(self):
        child = HTMLNode(tag='span', value='Child', children=[], props={'class': 'child'})
        node = HTMLNode(tag='div', value='Hello', children=[child], props={'class': 'container'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[HTMLNode(tag=span, value=Child, children=[], props={'class': 'child'})], props={'class': 'container'})")

    def test_repr_with_props_none(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props=None)
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props=None)")
    
    def test_repr_with_props_empty(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={})")
    
    def test_repr_with_props_special_characters(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'data-info': 'This is a "special" value'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'data-info': 'This is a \"special\" value'})")
    
    def test_repr_with_props_unicode(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'data-info': 'こんにちは'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'data-info': 'こんにちは'})")
    
    def test_repr_with_props_emoji(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'data-info': '😀'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'data-info': '😀'})")
    
    if __name__ == "__main__":
        unittest.main()