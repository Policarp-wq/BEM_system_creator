import os
import re

project_dir = r'C:\Users\Policarp\Desktop\russian-travel-main'
imports = r'C:\Users\Policarp\Desktop\russian-travel-main\pages\index.css'

# Won't for modifiers i.e. class="lang lang_selected"
def extract_class(line):
    word = 'class='
    match = re.search(r'class=\"[a-z_-]+\"', line)
    if match is not None:
        return match.group()[len(word) + 1:-1]


# Won't for modifiers i.e. class="lang lang_selected"
def create_css_file(class_name):
    split = class_name.split('__')
    block = split[0]
    element = ''
    if len(split) > 1:
        element = split[1]
    add = 'blocks'
    block_path = os.path.join(project_dir, add, block)
    block_css = os.path.join(block_path, block + '.css')
    element_path = os.path.join(block_path, '__' + element)
    element_css = os.path.join(element_path, class_name + '.css')

    imp = open(imports, 'a')
    if not os.path.exists(block_path):
        os.makedirs(block_path)
    if not os.path.exists(block_css):
        f = open(block_css, 'x')
        f.write(f'.{block} ' + '{\n\n}\n\n' + '''@media screen and (min-width: 1280px) {
}
@media screen and (max-width: 1024px) {
}
@media screen and (max-width: 768px) {
}
@media screen and (max-width: 320px) {
}
        ''')
        f.close()
        imp.write(f'@import url({'..' + block_css[len(project_dir):]});\n'.replace('\\', '/'))

    if len(element) > 0 and not os.path.exists(element_path):
        os.makedirs(element_path)
    if len(element) > 0 and not os.path.exists(element_css):
        f = open(element_css, 'x')
        f.write(f'.{class_name} ' + '{\n\n}\n\n' + '''@media screen and (min-width: 1280px) {
}
@media screen and (max-width: 1024px) {
}
@media screen and (max-width: 768px) {
}
@media screen and (max-width: 320px) {
}
        ''')
        f.close()
        imp.write(f'@import url({'..' + element_css[len(project_dir):]});\n'.replace('\\', '/'))
    imp.close()
def main():
    exist = set()
    classes = []

    with open(os.path.join(project_dir, 'index.html'), 'r', encoding='utf-8') as index:
        for line in index.readlines():
            name = extract_class(line)
            if name is not None and name not in exist:
                exist.add(name)
                classes.append(name)

    for cl in classes:
        create_css_file(cl)


if __name__ == '__main__':
    main()
