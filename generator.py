import yaml
import hashlib
from pprint import pprint

def main():

    with open("./checklist.yaml", "r") as stream:
        data = yaml.safe_load(stream)

    with open('templates/index.html') as f:
        index = f.read()

    with open('templates/section.html') as f:
        section_template = f.read()

    with open('templates/checklist-item.html') as f:
        checklist_item_template = f.read()

    image_template = """<img class="img-fluid" src="{{{IMAGE_SRC}}}"/>"""


    sections_html = []
    for section in data:
        section_html = section_template.replace("{{{TITLE}}}", section['title'])
        if section['img'] != "None":
            image_html = image_template.replace("{{{IMAGE_SRC}}}", section['img'])
            section_html = section_html.replace("{{{IMAGE}}}", image_html)
        else:
            section_html = section_html.replace("{{{IMAGE}}}", "")

        checklist_items_html = []
        for checklist_item in section['checklist']:
            checklist_item_html = checklist_item_template.replace("{{{CHECKLIST_ITEM}}}", checklist_item)
            checklist_item_html = checklist_item_html.replace("{{{RANDOM_ID}}}", get_ID(section['title'], checklist_item))
            checklist_items_html.append(checklist_item_html)

        checklist_items_html = "".join(checklist_items_html)
        section_html = section_html.replace("{{{ITEM_WRAPPER}}}", checklist_items_html)
        sections_html.append(section_html)

    sections_html = "".join(sections_html)

    index = index.replace("{{{SECTION_LIST}}}", sections_html)

    with open('index.html', 'w') as f:
        f.write(index)

def get_ID(title, item):
    title = ''.join(filter(str.isalnum, title))
    item = ''.join(filter(str.isalnum, item))
    ID = f"{title}${item}"
    return ID

if __name__ == "__main__":
    main()
