import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode(
            "This is text with a `code block` word.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word.", TextType.TEXT),
            ],
        )

    def test_bold(self):
        node = TextNode(
            "This is **bold** text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_italic(self):
        node = TextNode(
            "This is _italic_ text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "_",
            TextType.ITALIC,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_non_text_node(self):
        node = TextNode("already bold", TextType.BOLD)

        new_nodes = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(new_nodes, [node])

    def test_unmatched_delimiter(self):
        node = TextNode(
            "This is `broken",
            TextType.TEXT,
        )

        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE,
            )


if __name__ == "__main__":
    unittest.main()

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual(
        [("image", "https://i.imgur.com/zjjcJKZ.png")],
        matches,
    )

def test_extract_multiple_images(self):
    matches = extract_markdown_images(
        "![rick roll](https://i.imgur.com/aKaOqIh.gif) "
        "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
    self.assertListEqual(
        [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ],
        matches,
    )

def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) "
        "and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual(
        [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ],
        matches,
    )

def test_links_do_not_extract_images(self):
    matches = extract_markdown_links(
        "![image](https://example.com/image.png)"
    )
    self.assertListEqual([], matches)

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
        "and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

    new_nodes = split_nodes_image([node])

    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode(
                "image",
                TextType.IMAGE,
                "https://i.imgur.com/zjjcJKZ.png",
            ),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image",
                TextType.IMAGE,
                "https://i.imgur.com/3elNhQu.png",
            ),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) "
        "and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )

    new_nodes = split_nodes_link([node])

    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode(
                "to boot dev",
                TextType.LINK,
                "https://www.boot.dev",
            ),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube",
                TextType.LINK,
                "https://www.youtube.com/@bootdotdev",
            ),
        ],
        new_nodes,
    )

def test_text_to_textnodes(self):
    text = (
        "This is **text** with an _italic_ word and a `code block` "
        "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
        "and a [link](https://boot.dev)"
    )

    nodes = text_to_textnodes(text)

    self.assertEqual(
        nodes,
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image",
                TextType.IMAGE,
                "https://i.imgur.com/fJRm4Vk.jpeg",
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode(
                "link",
                TextType.LINK,
                "https://boot.dev",
            ),
        ],
    )

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

