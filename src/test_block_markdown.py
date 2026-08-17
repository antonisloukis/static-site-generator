import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from main import extract_title


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_extra_blank_lines(self):
        md = """First block


Second block



Third block"""

        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_whitespace(self):
        md = """

    First block    

Second block    

"""

        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First block",
                "Second block",
            ],
        )


if __name__ == "__main__":
    unittest.main()

def test_heading(self):
    self.assertEqual(
        block_to_block_type("### My heading"),
        BlockType.HEADING,
    )

def test_paragraph(self):
    self.assertEqual(
        block_to_block_type("This is just a normal paragraph."),
        BlockType.PARAGRAPH,
    )

def test_code(self):
    self.assertEqual(
        block_to_block_type("```\nprint('hello')\n```"),
        BlockType.CODE,
    )

def test_quote(self):
    self.assertEqual(
        block_to_block_type("> hello\n> world"),
        BlockType.QUOTE,
    )

def test_unordered_list(self):
    self.assertEqual(
        block_to_block_type("- first\n- second\n- third"),
        BlockType.UNORDERED_LIST,
    )

def test_ordered_list(self):
    self.assertEqual(
        block_to_block_type("1. first\n2. second\n3. third"),
        BlockType.ORDERED_LIST,
    )

def test_bad_ordered_list(self):
    self.assertEqual(
        block_to_block_type("1. first\n3. third"),
        BlockType.PARAGRAPH,
    )


def test_extract_title_with_whitespace(self):
    markdown = "#    Hello World    "
    self.assertEqual(extract_title(markdown), "Hello World")


def test_extract_title_with_whitespace(self):
    markdown = "#    Hello World    "
    self.assertEqual(extract_title(markdown), "Hello World")


def test_extract_title_missing(self):
    with self.assertRaises(Exception):
        extract_title("## Not an h1")       