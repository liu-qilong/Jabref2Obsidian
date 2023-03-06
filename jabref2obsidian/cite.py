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


def param_assemble(entry: dict) -> list:
    """
    Assembles the parameters from a dictionary of bibtex entry to be passed in :code:`citation` or :code:`citation_full` functions.

    Note
    ---
    :code:`citation` or :code:`citation_full` functions are converted from the :code:`JavaScript` functions I developed before. They can generates brief and full versions of citation text. However, the citation text presented here is only for adding brief literature citations referenced to this note in another Obsidian note, not for formal academic papers.

    Parameters
    ----------
    entry : dict
        A a bibtex entry from which the parameters will be extracted. For example: ::

            import bibtexparser

            bib_path = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib'
            with open(bib_path) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            entry = bib_database.entries[1]
            param_assemble(entry)

    Returns
    -------
    list
        A list of publication parameters extracted from the bibtex entry, in the
        order of ['ENTRYTYPE', 'ID', 'author', 'title', 'editor', 'edition',        'container', 'publisher', 'school', 'address', 'year', 'volume',        'number', 'pages'].
    None

    Examples
    --------
    ::

        entry = {
            'ENTRYTYPE': 'book',
            'ID': 'Book1',
            'author': 'John Smith',
            'title': 'My Book',
            'publisher': 'My Publisher',
            'year': '2021',
        }
        param_list = param_assemble(entry)
        print(param_list)
        ['book', 'Book1', 'John Smith', 'My Book', '', '', '', 'My Publisher', '', '', '2021', '', '', '']
    """
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

    for key in param2key.values():
        if key in entry.keys():
            param_list.append(entry[key])
        else:
            param_list.append('')

    return param_list


def gen_citation(entry: dict) -> str:
    """
    Generates a brief form citation string from a dictionary of bibtex entry.

    Attention
    ---
    The citation text presented here is only for adding brief literature citations referenced to this note in another Obsidian note, not for formal academic papers.

    Parameters
    ----------
    entry : dict
        A a bibtex entry from which the parameters will be extracted. For example: ::

            import bibtexparser

            bib_path = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib'
            with open(bib_path) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            entry = bib_database.entries[1]
            gen_citation(entry)

    Returns
    -------
    str
        A brief form citation string generated from the bibtex entry.
    """
    param_list = param_assemble(entry)
    return citation(*param_list)


def gen_citation_full(entry: dict):
    """
    Generates a full form citation string from a dictionary of bibtex entry.

    Attention
    ---
    The citation text presented here is only for adding brief literature citations referenced to this note in another Obsidian note, not for formal academic papers.

    Parameters
    ----------
    entry : dict
        A a bibtex entry from which the parameters will be extracted. For example: ::

            import bibtexparser

            bib_path = '/Users/kirov/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Knowledge.bib'
            with open(bib_path) as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)

            entry = bib_database.entries[1]
            gen_citation_full(entry)

    Returns
    -------
    str
        A full form citation string generated from the bibtex entry.
    """
    param_list = param_assemble(entry)
    return citation_full(*param_list)