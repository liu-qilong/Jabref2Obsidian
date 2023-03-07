import os
import shutil
from jabref2obsidian import cite

def export_group_pages(node: dict, name: str, source_name: str = "None", export_folder: str = 'output/Groups/'):
    """
    Export a group's information, including a roadmap (of its source- and sub- groups) and its literature entries, into a markdown file under a folder of its name. Then recursively generating subfolders and markdown files for the subgroups in the same manner.

    Parameters
    ----------
    node : dict
        A dictionary containing a group's information including its subgroups and entries.
    name : str
        Name of the group.
    source_name : str, optional
        Name of the source group, by default :code:`"None"`.
    export_folder : str, optional
        Folder path for the output files, by default :code:`'output/Groups/'`.
    """
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
    """
    Export a list of notes for the literature entries in markdown format to a specified folder.

    Parameters:
    -----------
    entries : List[dict]
        A list of dictionaries, where each dictionary represents a single literature entries.
        Each dictionary should contain the following keys:

        - :code:`'title' : str` : The title of the note.
        - :code:`'groups' : str (optional)` : A comma-separated list of groups to which the note belongs.
        - :code:`'author' : str (optional)` : The author of the note.
        - :code:`'editor' : str (optional)` : The editor of the note.
        - :code:`'file' : str (optional)` : The path to the file associated with the note.
        - :code:`'ID' : str` : A unique identifier for the note.
        - :code:`'comment' : str (optional)` : A comment or literature review associated with the note.

    export_folder : str, optional
        The path to the folder where the markdown files will be exported.
        Defaults to :code:`'output/Notes'`.
    asset_folder : str, optional
        The path to the folder where the associated files are located.
        Defaults to :code:`'/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/'`.

    Note
    ----
    This function creates a new folder at the specified `export_folder` path, if it does not already exist.

    If the folder already exists, its contents will be deleted before creating new files.
    Each note is exported as a markdown file in the specified :code:`export_folder`.

    The markdown file includes various sections, such as title, asset, citation key, and literature review, depending on the keys present in the dictionary entry.

    Any associated files are linked in the asset section, and citation information is also included. If any errors occur during the export process, the function prints an error message and continues with the next note.
    """
    # create notes folder
    if os.path.exists(export_folder):
        shutil.rmtree(export_folder)
        print("removed legacy {} folder".format(export_folder))
        
    os.mkdir(export_folder)

    # create markdown files for notes
    for entry in entries:
        try:
            md_path = os.path.join(
                export_folder,  "{}.md".format(entry['title'])
                )

            with open(md_path, 'w') as file:
                # title section
                file.write("### {}\n".format(entry['title']))
                if 'groups' in entry.keys():
                    group_str = entry['groups'].replace(", ", "]]. [[")
                    file.write("$\infty$ [[{}]]\n".format(group_str))

                if 'author' in entry.keys():
                    file.write("{}\n\n".format(entry['author']))

                if 'editor' in entry.keys():
                     file.write("Editors: {}\n\n".format(entry['editor']))

                # asset section
                file.write("---\n")
                file.write("#### Entry Type _{}_\n\n".format(entry['ENTRYTYPE']))
                file.write("> {}\n".format("{}\n".format(cite.gen_citation_full(entry))))

                if 'file' in entry.keys():
                    file_path = "file:/{}".format(os.path.join(asset_folder, entry['file'][1:-4])).replace(" ", "%20")
                    file.write("- Open [local file]({})^[only available on desktop] or search it in [Apple Books](ibooks://search).\n".format(file_path))

                if 'url' in entry.keys():
                    file.write("- URL: {}\n".format(entry['url']))

                if 'doi' in entry.keys():
                    file.write("- DOI: `{}`\n".format(entry['doi']))

                file.write("- Citation key\n")
                file.write("  ```\n")
                file.write("  {}\n".format(entry['ID']))
                file.write("  ```\n")

                file.write("- Citation text^[The citation text presented here is only for adding brief literature citations referenced to this note in another Obsidian note, not for formal academic papers.]\n")
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