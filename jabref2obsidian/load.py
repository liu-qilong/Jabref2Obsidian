import re
import bibtexparser

def load_bib(bib_path: str) -> bibtexparser.bibdatabase.BibDatabase:
    """
    Load a BibTeX file and parse it using :code:`bibtexparser`.

    Parameters
    ----------
    bib_path : str
        The file path to the BibTeX file.

    Returns
    -------
    bibtexparser.bibdatabase.BibDatabase
        A :code:`BibDatabase` object containing the parsed BibTeX data.
    """
    with open(bib_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # replace unwanted symbol in title string
    for entry in bib_database.entries:
        entry['title'] = entry['title'].replace('/', '_').replace('{', '').replace('}', '')

    return bib_database


def parse_group_tree(tree_str: str) -> tuple:
    """
    Parses a string representing a tree of groups and returns a dictionary of
    groups for fast access and a root node for the group tree.

    Parameters
    ----------
    tree_str : str
        The string representation of the group tree.

        Attention
        ---
        Such text is extracted from the :code:`BibDatabase` object's first :code:`comment` entry, in alignment with the JabRef's data saving scheme: ::

            tree_str = bib_database.comments[1]
            group_dict, tree_root = load.parse_group_tree(tree_str)

    Returns
    -------
    tuple
        A tuple containing a dictionary of groups for fast access and a root
        node for the group tree.
    """
    # extract group level and name and combined as an order list
    lines = re.split('\n', tree_str)
    group_list = []

    for line in lines:
        if 'Group' in line:
            level = int(line[0])
            if level == 0:
                group_list.append({
                    'level': level,
                    'name': 'Root',
                    'node': {'entries': []},
                    })
                
            else:
                name = re.search(r"(?<=Group:)[^\\;]+", line).group()  # at current stage only english group names are supported
                group_list.append({
                    'level': level, 
                    'name': name,
                    'node': {'entries': []},
                    })

    # prepare a dictionary of all groups for fast accessing via group name
    group_dict = {}

    for group in group_list:
        group_dict[group['name']] = group['node']

    # parse the group tree
    for idx_current in range(len(group_list)):
        # search backward for the 1st higher level node as current node's source node
        for idx_previous in range(idx_current, -1, -1):
            if group_list[idx_previous]['level'] < group_list[idx_current]['level']:
                source_node = group_list[idx_previous]['node']
                current_node = group_list[idx_current]['node']
                current_name = group_list[idx_current]['name']
                source_node[current_name] = current_node
                break
    
    tree_root = group_list[0]['node']

    return group_dict, tree_root


def attach_entries_to_group(entries: list, group_dict: dict):
    """
    Attaches a list of entries to the corresponding groups in a dictionary of
    groups.

    Parameters
    ----------
    entries : list
        A list of entries to be attached to the groups.
    group_dict : dict
        A dictionary of groups to which the entries will be attached.

    Examples
    --------
    ::

        # load bib file
        bib_database = load.load_bib(bib_path)

        # parse the group tree
        # P.S. the group dictionary is for fast accessing of the group tree nodes
        tree_str = bib_database.comments[1]
        group_dict, tree_root = load.parse_group_tree(tree_str)

        # attach the loaded entries to the corresponding nodes
        load.attach_entries_to_group(bib_database.entries, group_dict)
    """
    for entry in entries:
        # if the entry has groups attr, attach it to the corresponding groups
        if 'groups' in entry.keys():
            groups = re.split(', ', entry['groups'])

            for group in groups:
                group_dict[group]['entries'].append(entry)

        # if the entry doesn't have groups attr, attach it to the root group
        else:
            group_dict['Root']['entries'].append(entry)


