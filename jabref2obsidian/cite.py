import os
from quickjs import Function
import jabref2obsidian

# convert js citation scripts to python functions
mod_path = os.path.dirname(jabref2obsidian.__file__)

with open(os.path.join(mod_path, 'citation_full.js')) as file:
    js = ''.join(file.readlines())
    citation_full = Function('citation_full', js)

with open(os.path.join(mod_path, 'citation.js')) as file:
    js = ''.join(file.readlines())
    citation = Function('citation', js)


def param_assemble(entry: dict):
    param2key = {
        'type_str': 'ENTRYTYPE', 
        'cite_str': 'ID',
        'author_str': 'author', 
        'title_str': 'title', 
        'editor_str': 'editor', 
        'edition_str': 'edition',
        'container_str': 'container', 
        'publisher_str': 'publisher', 
        'school_str': 'school', 
        'addres_str': 'address',
        'year_str': 'year', 
        'vol_str': 'volume', 
        'num_str': 'number', 
        'page_str': 'pages'
    }
    
    param_list = []

    for param, key in param2key.items():
        if key in entry.keys():
            param_list.append(entry[key])
        else:
            param_list.append('')

    return param_list


def gen_citation(entry: dict):
    param_list = param_assemble(entry)
    return citation(*param_list)


def gen_citation_full(entry: dict):
    param_list = param_assemble(entry)
    return citation_full(*param_list)