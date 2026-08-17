from enum import Enum

from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []

    for block in raw_blocks:
        block = block.strip()

        if block != "":
            blocks.append(block)

    return blocks

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    # Heading: 1-6 # characters followed by a space
    if block.startswith("#"):
        parts = block.split(" ", 1)
        if len(parts) == 2:
            hashes = parts[0]
            if 1 <= len(hashes) <= 6 and all(char == "#" for char in hashes):
                return BlockType.HEADING

    # Code block: starts and ends with ```
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    # Quote: every line starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: must start at 1 and increase
    is_ordered = True

    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            is_ordered = False
            break

    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            children.append(
                ParentNode("p", text_to_children(text))
            )

        elif block_type == BlockType.HEADING:
            level = 0

            for char in block:
                if char == "#":
                    level += 1
                else:
                    break

            text = block[level + 1:]

            children.append(
                ParentNode(
                    f"h{level}",
                    text_to_children(text),
                )
            )

        elif block_type == BlockType.CODE:
            text = block[4:-3]

            code_node = LeafNode(
                "code",
                text,
            )

            children.append(
                ParentNode(
                    "pre",
                    [code_node],
                )
            )

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []

            for line in lines:
                cleaned_lines.append(
                    line.lstrip(">").strip()
                )

            text = " ".join(cleaned_lines)

            children.append(
                ParentNode(
                    "blockquote",
                    text_to_children(text),
                )
            )

        elif block_type == BlockType.UNORDERED_LIST:
            items = []

            for line in block.split("\n"):
                text = line[2:]

                items.append(
                    ParentNode(
                        "li",
                        text_to_children(text),
                    )
                )

            children.append(
                ParentNode(
                    "ul",
                    items,
                )
            )

        elif block_type == BlockType.ORDERED_LIST:
            items = []

            for line in block.split("\n"):
                parts = line.split(". ", 1)
                text = parts[1]

                items.append(
                    ParentNode(
                        "li",
                        text_to_children(text),
                    )
                )

            children.append(
                ParentNode(
                    "ol",
                    items,
                )
            )

    return ParentNode("div", children)