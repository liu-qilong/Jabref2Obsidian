import os
from jabref2obsidian import load
from jabref2obsidian import export

def j2o(
    bib_path: str = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib',
    export_folder: str = '../output/',
    asset_folder: str = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/',
    ):
    """
    Export entries from a BibTeX file to Obsidian, creating Markdown notes for each entry and group.

    Note
    ----
    This function exports BibTeX entries to Obsidian-compatible Markdown notes. The Markdown notes include the title, author, and editor information of each entry. If available, the group information of each entry is included as a tag. If there is a file attachment, a link to the file is provided in the note. Citation information is also included, along with citation text for the literature review section of the note.

    At the same time, the groups information added with JabRef, including a roadmap (of its source- and sub- groups) and its literature entries will be outputted to markdown files, organised in the folder structure according to the hierarchy of the groups.

    Parameters
    ----------
    bib_path : str, optional
        The path of the BibTeX file, by default :code:`'/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib'`
    export_folder : str, optional
        The folder path where the generated Markdown files will be saved, by default :code:`'../output/Notes'`
    asset_folder : str, optional
        The folder path where the attachment files are saved, by default :code:`'/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/'`
        
    Example
    ---
    ::

        from jabref2obsidian import convert
        convert.j2o(
            bib_path='/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib',
            export_folder='../output/',
            asset_folder='/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/',
            )
    """

    # load bib file
    bib_database = load.load_bib(bib_path)

    # parse the group tree
    # P.S. the group dictionary is for fast accessing of the group tree nodes
    tree_str = bib_database.comments[1]
    group_dict, tree_root = load.parse_group_tree(tree_str)

    # attach the loaded entries to the corresponding nodes
    load.attach_entries_to_group(bib_database.entries, group_dict)

    # export group pages
    export.export_group_pages(node=tree_root, name='Root', export_folder=os.path.join(export_folder, 'Groups'))

    # export note pages
    export.export_note_pages(bib_database.entries, export_folder=os.path.join(export_folder, 'Notes'), asset_folder=asset_folder)