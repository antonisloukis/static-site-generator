import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Click me",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_none(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_single(self):
        node = HTMLNode(
            "a",
            "Boot.dev",
            None,
            {"href": "https://www.boot.dev"},
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_a(self):
    node = LeafNode(
        "a",
        "Click me!",
        {"href": "https://www.google.com"},
    )
    self.assertEqual(
        node.to_html(),
        '<a href="https://www.google.com">Click me!</a>',
    )

def test_leaf_raw_text(self):
    node = LeafNode(None, "Just plain text")
    self.assertEqual(node.to_html(), "Just plain text")

def test_leaf_no_value(self):
    node = LeafNode("p", None)

    with self.assertRaises(ValueError):
        node.to_html()

def test_parent_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])

    self.assertEqual(
        parent_node.to_html(),
        "<div><span>child</span></div>",
    )

def test_parent_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])

    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_parent_multiple_children(self):
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    self.assertEqual(
        node.to_html(),
        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
    )

def test_parent_no_tag(self):
    node = ParentNode(None, [LeafNode("p", "hello")])

    with self.assertRaises(ValueError):
        node.to_html()

def test_parent_no_children(self):
    node = ParentNode("div", None)

    with self.assertRaises(ValueError):
        node.to_html()        

