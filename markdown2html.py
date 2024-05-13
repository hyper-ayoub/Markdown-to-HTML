#!/usr/bin/python3

""" doc """

import sys
import os.path


def convert_markdown_to_html(markdown_file, output_file):
    # Check if Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)

    # Write HTML content to output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get input and output file names
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Exit with success status
    sys.exit(0)
