// Generate English reference in Chicago format and Chinese reference in GB/T7714-2015 format.
// The authors/editors are presented in short form.
function citation(type_str, cite_str,
                  author_str, title_str, editor_str, edition_str,
                  publisher_str, school_str, address_str,
                  year_str, vol_str, num_str, page_str,
                  container_str) {
    
    // Transform author_str and editor_str to short form
    if (author_str != '') {
        var authors = author_str.split(',')

        if (escape(title_str).indexOf( "%u" ) < 0) {
            if (authors.length == 1) {
                author_short = authors[0]
            } else if (authors.length == 2) {
                author_short = authors.join(' and ')
            } else {
                author_short = authors[0] + ', et al'
            }
        } else {
            if (authors.length == 1) {
                author_short = authors
            } else if (authors.length == 2) {
                author_short = authors.join('和')
            } else {
                author_short = authors[0] + '等'
            }
        }
    } else {
        author_short = ''
    }

    if (editor_str != '') {
        var editors = editor_str.split(',')

        if (escape(title_str).indexOf( "%u" ) < 0) {
            if (editors.length == 1) {
                editor_short = editors[0]
            } else if (editors.length == 2) {
                editor_short = editors.join(' and ')
            } else {
                editor_short = editors[0] + ' et al., edit'
            }
        } else {
            if (editors.length == 1) {
                editor_short = editors
            } else if (authors.length == 2) {
                editor_short = editors.join('和')
            } else {
                editor_short = editors[0] + '等, 编'
            }
        }
    } else {
        editor_short = ''
    }

    // if there is no author_str, use editor_short as author_short
    if (author_str == '') {
        author_short = editor_short
        editor_short = ''
    }

    // If it's English literature, generate correct form of title and publicate information.
    if (escape(title_str).indexOf( "%u" ) < 0) {

        if (type_str == 'article') {
            title_str = '"[[' + title_str + ']]"'
            publicate_str = container_str
        }
        else if (type_str == 'inproceedings') {
            title_str = '"[[' + title_str + ']]"'
            publicate_str = container_str
        }
        else if (type_str == 'inbook') {
            title_str = '"[[' + title_str + ']]"'
            publicate_str = container_str
        }
        else if (type_str == 'incollect') {
            title_str = '"[[' + title_str + ']]"'
            publicate_str = container_str
        }
        else if (type_str == 'book') {
            title_str = '[[' + title_str + ']]'
            publicate_str = publisher_str
        }
        else if (type_str == 'booklet') {
            title_str = '[[' + title_str + ']]'
            publicate_str = ""
        }
        else if (type_str == 'phdthesis') {
            title_str = '[[' + title_str + ']]'
            publicate_str = school_str + 'Ph. D. thesis'
        }
        else if (type_str == 'masterthesis') {
            title_str = '[[' + title_str + ']]'
            publicate_str = school_str + 'Master degree thesis'
        }
        else {
            title_str = '[[' + title_str + ']]'
            publicate_str = container_str + '. ' + publisher_str
        }

        publicate_str = publicate_str + '. ' + year_str + ', '
            + vol_str + '(' + num_str + '): ' + page_str + '.'

        edition_str = 'Edition ' + edition_str

    // If it's Chinese literature, generate correct form of title and publicate information.
    } else{
        if (type_str == 'article') {
            title_str = '[[' + title_str + ']][A]'
            publicate_str = container_str
        }
        else if (type_str == 'inproceedings') {
            title_str = '[[' + title_str + ']][C]'
            publicate_str = container_str
        }
        else if (type_str == 'inbook') {
            title_str = '[[' + title_str + ']][A]'
            publicate_str = container_str
        }
        else if (type_str == 'incollect') {
            title_str = '[[' + title_str + ']][A]'
            publicate_str = container_str
        }
        else if (type_str == 'book') {
            title_str = '[[' + title_str + ']][M]'
            publicate_str = publisher_str
        }
        else if (type_str == 'booklet') {
            title_str = '[[' + title_str + ']][M]'
            publicate_str = container_str
        }
        else if (type_str == 'masterthesis') {
            title_str = '[[' + title_str + ']][D]'
            publicate_str = school_str + '博士论文'
        }
        else if (type_str == 'phdthesis') {
            title_str = '[[' + title_str + ']][D]'
            publicate_str = school_str + '硕士论文'
        }
        else {
            title_str = '[[' + title_str + ']]'
            publicate_str = container_str + '. ' + publisher_str
        }

        publicate_str = address_str + ': ' + publicate_str + '. ' + year_str + ', '
            + vol_str + '(' + num_str + '): ' + page_str + '.'
        edition_str = '第 ' + edition_str + ' 版'
    }

    var cite_str = author_short + ". " + title_str + ". " + editor_short + ". " + edition_str + ". " + publicate_str

    //Tidy up empty information.
    //Empty Edition
    var split_str = cite_str.split("Edition .")
    cite_str = split_str.join(".")

    split_str = cite_str.split("第  版.")
    cite_str = split_str.join(".")

    //Empty address.
    split_str = cite_str.split(" : ")
    cite_str = split_str.join(" ")

    //Empty vol.
    split_str = cite_str.split(", (")
    cite_str = split_str.join("(")

    //Empty num.
    split_str = cite_str.split("()")
    cite_str = split_str.join("")

    // Empty page.
    split_str = cite_str.split(": .")
    cite_str = split_str.join(".")

    // Other empty information.
    while (cite_str.split(" . ").length > 1) {
        split_str = cite_str.split(" . ")
        cite_str = split_str.join(" ")
    }

    // Duplicated and annoying items
    while (cite_str.split("..").length > 1) {
        split_str = cite_str.split("..")
        cite_str = split_str.join(".")
    }

    while (cite_str.split("  ").length > 1) {
        split_str = cite_str.split("  ")
        cite_str = split_str.join(" ")
    }

    return cite_str
}

// module.exports = citation