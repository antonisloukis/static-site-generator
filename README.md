# Static Site Generator

A static site generator built from scratch in **Python**.

The project converts Markdown content into HTML pages using a reusable HTML template and recursively generates a complete static website.

## Features

- Converts Markdown into HTML
- Supports headings, paragraphs, lists, quotes, code blocks, links, and images
- Extracts page titles from Markdown
- Uses reusable HTML templates
- Recursively generates multiple pages
- Copies static assets such as CSS and images
- Supports configurable base paths
- Deployable with GitHub Pages

## Project Structure

```text
static-site-generator/
├── content/          # Markdown content
├── docs/             # Generated website
├── src/              # Python source code
├── static/           # CSS and images
├── build.sh          # Production build script
├── main.sh           # Local development script
├── template.html     # HTML page template
└── test.sh           # Test runner
```

## Run Locally

Clone the repository and enter the project directory:

```bash
git clone https://github.com/antonisloukis/static-site-generator.git
cd static-site-generator
```

Run the generator:

```bash
./main.sh
```

Then open the generated site using a local HTTP server.

## Build for Production

```bash
./build.sh
```

The generated website will be written to the `docs/` directory for deployment with GitHub Pages.

## Testing

Run the test suite with:

```bash
./test.sh
```

## Built With

- Python
- HTML
- CSS
- Markdown
- GitHub Pages

## What I Learned

This project helped me practice:

- Recursive directory traversal
- Object-oriented programming
- Parsing and transforming Markdown
- File and directory manipulation
- HTML generation
- Unit testing
- Static site architecture
- GitHub Pages deployment

## Acknowledgements

Built as part of the [Boot.dev](https://www.boot.dev/) Backend Developer curriculum.
