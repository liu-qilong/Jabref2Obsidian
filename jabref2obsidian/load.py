import re
import bibtexparser

def load_bib(bib_path: str):
    with open(bib_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database


def parse_group_tree(tree_str: str) -> dict:
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
    for entry in entries:
        # if the entry has groups attr, attach it to the corresponding groups
        if 'groups' in entry.keys():
            groups = re.split(', ', entry['groups'])

            for group in groups:
                group_dict[group]['entries'].append(entry)

        # if the entry doesn't have groups attr, attach it to the root group
        else:
            group_dict['Root']['entries'].append(entry)


