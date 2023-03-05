__all__ = ['citation_full']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['citation_full'])
@Js
def PyJsHoisted_citation_full_(type_str, cite_str, author_str, title_str, editor_str, edition_str, container_str, publisher_str, school_str, addres_str, year_str, vol_str, num_str, page_str, this, arguments, var=var):
    var = Scope({'type_str':type_str, 'cite_str':cite_str, 'author_str':author_str, 'title_str':title_str, 'editor_str':editor_str, 'edition_str':edition_str, 'container_str':container_str, 'publisher_str':publisher_str, 'school_str':school_str, 'addres_str':addres_str, 'year_str':year_str, 'vol_str':vol_str, 'num_str':num_str, 'page_str':page_str, 'this':this, 'arguments':arguments}, var)
    var.registers(['addres_str', 'editor_str', 'author_str', 'page_str', 'edition_str', 'year_str', 'authors', 'editors', 'cite_str', 'container_str', 'split_str', 'publisher_str', 'school_str', 'title_str', 'vol_str', 'num_str', 'type_str'])
    if (var.get('author_str')!=Js('')):
        var.put('authors', var.get('author_str').callprop('split', Js(',')))
        if (var.get('escape')(var.get('title_str')).callprop('indexOf', Js('%u'))<Js(0.0)):
            if (var.get('authors').get('length')==Js(1.0)):
                var.put('author_full', var.get('authors').get('0'))
            else:
                if (var.get('authors').get('length')==Js(2.0)):
                    var.put('author_full', var.get('authors').callprop('join', Js(' and ')))
                else:
                    var.put('author_full', var.get('authors').callprop('join', Js(', ')))
        else:
            if (var.get('authors').get('length')==Js(1.0)):
                var.put('author_full', var.get('authors').get('0'))
            else:
                if (var.get('authors').get('length')==Js(2.0)):
                    var.put('author_full', var.get('authors').callprop('join', Js('和')))
                else:
                    var.put('author_full', var.get('authors').callprop('join', Js(', ')))
    else:
        var.put('author_full', Js(''))
    if (var.get('editor_str')!=Js('')):
        var.put('editors', var.get('editor_str').callprop('split', Js(',')))
        if (var.get('escape')(var.get('title_str')).callprop('indexOf', Js('%u'))<Js(0.0)):
            if (var.get('editors').get('length')==Js(1.0)):
                var.put('editor_full', var.get('editors').get('0'))
            else:
                if (var.get('editors').get('length')==Js(2.0)):
                    var.put('editor_full', var.get('editors').callprop('join', Js(' and ')))
                else:
                    var.put('editor_full', (var.get('editors').callprop('join', Js(', '))+Js(', edit')))
        else:
            if (var.get('editors').get('length')==Js(1.0)):
                var.put('editor_full', var.get('editors').get('0'))
            else:
                if (var.get('authors').get('length')==Js(2.0)):
                    var.put('editor_full', var.get('editors').callprop('join', Js('和')))
                else:
                    var.put('editor_full', (var.get('editors').callprop('join', Js(', '))+Js(', 编')))
    else:
        var.put('editor_full', Js(''))
    if (var.get('author_str')==Js('')):
        var.put('author_full', var.get('editor_full'))
        var.put('editor_full', Js(''))
    if (var.get('escape')(var.get('title_str')).callprop('indexOf', Js('%u'))<Js(0.0)):
        if (var.get('type_str')==Js('article')):
            var.put('title_str', ((((Js('"[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]"')))
            var.put('publicate_str', var.get('container_str'))
        else:
            if (var.get('type_str')==Js('inproceedings')):
                var.put('title_str', ((((Js('"[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]"')))
                var.put('publicate_str', var.get('container_str'))
            else:
                if (var.get('type_str')==Js('inbook')):
                    var.put('title_str', ((((Js('"[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]"')))
                    var.put('publicate_str', var.get('container_str'))
                else:
                    if (var.get('type_str')==Js('incollect')):
                        var.put('title_str', ((((Js('"[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]"')))
                        var.put('publicate_str', var.get('container_str'))
                    else:
                        if (var.get('type_str')==Js('book')):
                            var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                            var.put('publicate_str', var.get('publisher_str'))
                        else:
                            if (var.get('type_str')==Js('booklet')):
                                var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                                var.put('publicate_str', Js(''))
                            else:
                                if (var.get('type_str')==Js('phdthesis')):
                                    var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                                    var.put('publicate_str', (var.get('school_str')+Js('Ph. D. thesis')))
                                else:
                                    if (var.get('type_str')==Js('masterthesis')):
                                        var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                                        var.put('publicate_str', (var.get('school_str')+Js('Master degree thesis')))
                                    else:
                                        var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                                        var.put('publicate_str', ((var.get('container_str')+Js('. '))+var.get('publisher_str')))
        var.put('publicate_str', (((((((((var.get('publicate_str')+Js('. '))+var.get('year_str'))+Js(', '))+var.get('vol_str'))+Js('('))+var.get('num_str'))+Js('): '))+var.get('page_str'))+Js('.')))
        var.put('edition_str', (Js('Edition ')+var.get('edition_str')))
    else:
        if (var.get('type_str')==Js('article')):
            var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][A]')))
            var.put('publicate_str', var.get('container_str'))
        else:
            if (var.get('type_str')==Js('inproceedings')):
                var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][C]')))
                var.put('publicate_str', var.get('container_str'))
            else:
                if (var.get('type_str')==Js('inbook')):
                    var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][A]')))
                    var.put('publicate_str', var.get('container_str'))
                else:
                    if (var.get('type_str')==Js('incollect')):
                        var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][A]')))
                        var.put('publicate_str', var.get('container_str'))
                    else:
                        if (var.get('type_str')==Js('book')):
                            var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][M]')))
                            var.put('publicate_str', var.get('publisher_str'))
                        else:
                            if (var.get('type_str')==Js('booklet')):
                                var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][M]')))
                                var.put('publicate_str', var.get('container_str'))
                            else:
                                if (var.get('type_str')==Js('masterthesis')):
                                    var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][D]')))
                                    var.put('publicate_str', (var.get('school_str')+Js('博士论文')))
                                else:
                                    if (var.get('type_str')==Js('phdthesis')):
                                        var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']][D]')))
                                        var.put('publicate_str', (var.get('school_str')+Js('硕士论文')))
                                    else:
                                        var.put('title_str', ((((Js('[[')+var.get('cite_str'))+Js('|'))+var.get('title_str'))+Js(']]')))
                                        var.put('publicate_str', ((var.get('container_str')+Js('. '))+var.get('publisher_str')))
        var.put('publicate_str', (((((((((((var.get('addres_str')+Js(': '))+var.get('publicate_str'))+Js('. '))+var.get('year_str'))+Js(', '))+var.get('vol_str'))+Js('('))+var.get('num_str'))+Js('): '))+var.get('page_str'))+Js('.')))
        var.put('edition_str', ((Js('第 ')+var.get('edition_str'))+Js(' 版')))
    var.put('cite_str', ((((((((var.get('author_full')+Js('. '))+var.get('title_str'))+Js('. '))+var.get('editor_full'))+Js('. '))+var.get('edition_str'))+Js('. '))+var.get('publicate_str')))
    var.put('split_str', var.get('cite_str').callprop('split', Js('Edition .')))
    var.put('cite_str', var.get('split_str').callprop('join', Js('.')))
    var.put('split_str', var.get('cite_str').callprop('split', Js('第  版.')))
    var.put('cite_str', var.get('split_str').callprop('join', Js('.')))
    var.put('split_str', var.get('cite_str').callprop('split', Js(' : ')))
    var.put('cite_str', var.get('split_str').callprop('join', Js(' ')))
    var.put('split_str', var.get('cite_str').callprop('split', Js(', (')))
    var.put('cite_str', var.get('split_str').callprop('join', Js('(')))
    var.put('split_str', var.get('cite_str').callprop('split', Js('()')))
    var.put('cite_str', var.get('split_str').callprop('join', Js('')))
    var.put('split_str', var.get('cite_str').callprop('split', Js(': .')))
    var.put('cite_str', var.get('split_str').callprop('join', Js('.')))
    while (var.get('cite_str').callprop('split', Js(' . ')).get('length')>Js(1.0)):
        var.put('split_str', var.get('cite_str').callprop('split', Js(' . ')))
        var.put('cite_str', var.get('split_str').callprop('join', Js(' ')))
    return var.get('cite_str')
PyJsHoisted_citation_full_.func_name = 'citation_full'
var.put('citation_full', PyJsHoisted_citation_full_)
pass
var.get('module').put('exports', var.get('citation_full'))


# Add lib to the module scope
citation_full = var.to_python()