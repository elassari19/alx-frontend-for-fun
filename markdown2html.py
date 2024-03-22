#!/usr/bin/python3
""" should convert a Markdown file to HTML """

import argparse
import pathlib
import re


def convert_md_to_html(input_file, output_file):
    ''' convert to HTML file '''
    with open(input_file, encoding='utf-8') as f:
        md_file_content = f.readlines()

    content = []
    for line in md_file_content:
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            heading_level = len(match.group(1))
            heading_content = match.group(2)
            content.append(f'<h{heading_level}>{heading_content}</h{heading_level}>\n')
        else:
            content.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    convert_md_to_html(args.input_file, args.output_file)
