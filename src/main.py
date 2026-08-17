import os
import shutil
import sys

from block_markdown import markdown_to_html_node


def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    copy_directory(source, destination)


def copy_directory(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying {source_path} -> {destination_path}")
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            copy_directory(source_path, destination_path)


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 header found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} to {dest_path} "
        f"using {template_path}"
    )

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html)

    # Fix absolute links/images for GitHub Pages
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)

    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)


def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
    basepath,
):
    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(content_path):
            if entry.endswith(".md"):
                html_filename = entry.replace(".md", ".html")
                html_dest_path = os.path.join(
                    dest_dir_path,
                    html_filename,
                )

                generate_page(
                    content_path,
                    template_path,
                    html_dest_path,
                    basepath,
                )

        else:
            os.makedirs(dest_path, exist_ok=True)

            generate_pages_recursive(
                content_path,
                template_path,
                dest_path,
                basepath,
            )


def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath,
    )


if __name__ == "__main__":
    main()