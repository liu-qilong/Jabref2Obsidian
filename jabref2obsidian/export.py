import os
import shutil
from jabref2obsidian import cite

def export_group_pages(node: dict, name: str, source_name: str = "None", export_folder: str = 'output/Groups/'):
    # create group folder
    if os.path.exists(export_folder):
        shutil.rmtree(export_folder)
        print("removed legacy {} folder".format(export_folder))
        
    os.mkdir(export_folder)

    # create group's markdown page
    md_path = os.path.join(export_folder, '{}.md'.format(name))
            
    with open(md_path, 'w') as file:
        # title section
        file.write("# {}\n".format(name))

        # roadmap section
        file.write("---\n")
        file.write("#### Roadmap\n\n")

        if name is not None:
            file.write("Source group\n")
            file.write("[[{}]]\n".format(source_name))

        file.write("Subgroups \n\n")

        for subgroup in node.keys():
            if subgroup != "entries":
                file.write("- [[{}]]\n".format(subgroup))

        # entries section
        file.write("---\n")
        file.write("#### Entries\n\n")
        file.write("| Type | Entry |\n")
        file.write("| --- | --- |\n")
        
        for entry in node['entries']:
            try:
                file.write("| {} | {} |\n".format(
                entry['ENTRYTYPE'],
                cite.gen_citation(entry),
                ))
            except:
                print("entry information miss:")
                print(entry)

    # recurse to the subgroups
    for subgroup in node.keys():
        if subgroup != "entries":
            sub_folder = os.path.join(export_folder, subgroup)
            export_group_pages(node[subgroup], subgroup, name, sub_folder)


def export_note_pages(entries: list, export_folder: str = 'output/Notes', asset_folder: str = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/'):
    # create notes folder
    if os.path.exists(export_folder):
        shutil.rmtree(export_folder)
        print("removed legacy {} folder".format(export_folder))
        
    os.mkdir(export_folder)

    # create markdown files for notes
    for entry in entries:
        try:
            md_path = os.path.join(export_folder, "{}.md".format(entry['title']))
            
            with open(md_path, 'w') as file:
                # title section
                file.write("### {}\n".format(entry['title']))
                if 'groups' in entry.keys():
                    group_str = entry['groups'].replace(", ", "]]. [[")
                    file.write("$\infty$ [[{}]]\n".format(group_str))

                if 'author' in entry.keys():
                    file.write("{}\n".format(entry['author']))
                if 'editor' in entry.keys():
                     file.write("Editors: {}\n".format(entry['editor']))

                # asset section
                file.write("---\n")
                file.write("#### Asset\n\n")
                file.write("> {}\n".format("{}\n".format(cite.gen_citation_full(entry))))
                
                if 'file' in entry.keys():
                    file_path = "file:/{}".format(os.path.join(asset_folder, entry['file'][1:-4])).replace(" ", "%20")
                    file.write("- Open [local file]({})^[only available on desktop] or search it in [Apple Books](ibooks://search).\n".format(file_path))

                file.write("- Citation key\n")
                file.write("  ```\n")
                file.write("  {}\n".format(entry['ID']))
                file.write("  ```\n")

                file.write("Citation text^[The citation text presented here is only for adding brief literature citations referenced to this note in another Obsidian note, not for formal academic papers.]\n")
                file.write("  ```\n")
                file.write("  {}\n".format(cite.gen_citation(entry)))
                file.write("  ```\n")

                # literature review section
                if 'comment' in entry.keys():
                    file.write("---\n")
                    file.write("#### Literature Review\n\n")
                    file.write("{}\n\n".format(entry['comment']))

        except:
            print("entry information miss:")
            print(entry)