#!/usr/bin/python3
'''Markdown to HTML Converter'''

import sys
import os.path
import re
import hashlib

def convert_markdown_to_html(input_file, output_file):
    with open(input_file) as read:
        with open(output_file, 'w') as html:
            in_list = False
            for line in read:
                line = line.replace('**', '<b>').replace('__', '<em>').replace('</b>', '**').replace('</em>', '__')
                line = re.sub(r'\[\[(.+?)\]\]', lambda x: hashlib.md5(x.group(1).encode()).hexdigest(), line)
                line = re.sub(r'\(\(([^Cc]+?)\)\)', lambda x: ''.join(c for c in x.group(1) if c not in 'Cc'), line)

                if line.startswith('#'):
                    level = line.count('#')
                    line = f"<h{level}>{line.strip('#').strip()}</h{level}>\n"
                elif line.lstrip().startswith(('-', '*')):
                    if not in_list:
                        html.write('<ul>\n')
                        in_list = True
                    line = f"<li>{line.strip().lstrip('-*').strip()}</li>\n"
                else:
                    if in_list:
                        html.write('</ul>\n')
                        in_list = False
                    if line.strip():
                        line = f"<p>{line.strip()}</p>\n"
                html.write(line)
            if in_list:
                html.write('</ul>\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not os.path.isfile(input_file):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
