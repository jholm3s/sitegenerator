import sys
from textnode import TextNode, TextType
from generate_page import generate_page

import os
import shutil

basepath = sys.argv[1] if len(sys.argv) > 1 else '.'

def copy_static_to_public(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            copy_static_to_public(src_path, dst_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(src_path):
            if item.endswith('.md'):
                dest_path = dest_path.replace('.md', '.html')
                generate_page(src_path, template_path, dest_path)
        else:
            generate_pages_recursive(src_path, template_path, dest_path)




def main():
    
    copy_static_to_public('./static', './docs')
    generate_pages_recursive('./content', 'template.html', basepath)


if __name__ == '__main__':
    main()