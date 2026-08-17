import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("click me", TextType.LINK, "https://example.com")
        node2 = TextNode("click me", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_none_url(self):
        node = TextNode("plain text", TextType.TEXT)
        node2 = TextNode("plain text", TextType.TEXT)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

def test_text_to_html(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_bold_to_html(self):
    node = TextNode("bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.to_html(), "<b>bold text</b>")

def test_italic_to_html(self):
    node = TextNode("italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.to_html(), "<i>italic text</i>")

def test_code_to_html(self):
    node = TextNode("print('hello')", TextType.CODE)
    html_node = text_node_to_html_node(node)

    self.assertEqual(
        html_node.to_html(),
        "<code>print('hello')</code>",
    )

def test_link_to_html(self):
    node = TextNode(
        "Boot.dev",
        TextType.LINK,
        "https://www.boot.dev",
    )
    html_node = text_node_to_html_node(node)

    self.assertEqual(
        html_node.to_html(),
        '<a href="https://www.boot.dev">Boot.dev</a>',
    )

def test_image_to_html(self):
    node = TextNode(
        "Boot.dev logo",
        TextType.IMAGE,
        "https://example.com/image.png",
    )
    html_node = text_node_to_html_node(node)

    self.assertEqual(
        html_node.to_html(),
        '<img src="https://example.com/image.png" alt="Boot.dev logo"></img>',
    )    