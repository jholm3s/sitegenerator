import sys
import os
from block_markdown import markdown_to_html_node, extract_title

basepath = sys.argv[1] if len(sys.argv) > 1 else '.'

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using template {template_path}")

    source_md = open(from_path, "r").read()
    template_md = open(template_path, "r").read()

    source_HTML_string = markdown_to_html_node(source_md).to_html()
    source_title = extract_title(source_md)

    template_md = template_md.replace("{{ Title }}", source_title)
    template_md = template_md.replace("{{ Content }}", source_HTML_string)
    template_md = template_md.replace('href="/', 'href="/{basepath}')
    template_md = template_md.replace('src="/', 'src="/{basepath}')



    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_md)