import os
from jabref2obsidian import load
from jabref2obsidian import export

def j2o(
    bib_path: str = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib',
    export_folder: str = '../output/Notes',
    asset_folder: str = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/',
    ):
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