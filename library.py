import os
import json

# Parameters
name = "Alei Eleonora"
names = name.split()
token = "T8a9MRZlbA2SW8SPpkyAmrB4qGUSPpl7Ru73WS44"
year1 = 2000
year2 = 2025
citations = ""
# citations = '2018JQSRT.217...86V'
getweb = True
wtable = True
wdoi = True
wbib = False
wlinks = True
wcolor = False
# font = '"Century Gothic", Verdana, Arial, Helvetica'
font = 'Palatino, Garamond, "Times New Roman", Times'
fontsz = 10
rdir = ""

# Get tables from ADS
# https://github.com/adsabs/adsabs-dev-api (search API)
if len(name) == 0:
    names = ["", ""]
if getweb:
    txt = names[0]
    if len(names) > 1:
        txt = "%s,+%s" % (txt, names[1])
    if len(names) > 2:
        txt = "%s+%s" % (txt, names[2])
    query = 'curl -s -H "Authorization: Bearer %s"' % token
    if len(citations) > 0:
        query = (
            '%s "https://api.adsabs.harvard.edu/v1/search/query?q=citations(bibcode%%3A%s)'
            % (query, citations)
        )
    else:
        query = '%s "https://api.adsabs.harvard.edu/v1/search/query?q=author:%%22%s' % (
            query,
            txt,
        )
    # Endelse
    query = (
        "%s&rows=2000&fl=author,title,pub,volume,issue,page,year,doi,bibcode,citation_count,alternate_bibcode&sort=date+desc"
        % query
    )
    cmd = '%s&fq=property:refereed" > library_ref.json' % query
    os.system(cmd)
    cmd = '%s&fq=property:notrefereed" > library_nonref.json' % query
    os.system(cmd)
# End getting files

# See if there is a list of bibcodes to skip
if os.path.exists("library_%s_skip.txt" % names[0]):
    fr = open("library_%s_skip.txt" % names[0], "r")
    bibskip = [line.rstrip() for line in fr.readlines()]
    fr.close()
else:
    bibskip = []

# Iterate across types
html = []
nfirst = 0
htable = []
nref = 0
nnonref = 0

# HTML structure
html = []
html.append("<!DOCTYPE html>")
html.append('<html lang="en">')
html.append("<head>")
html.append('    <meta charset="UTF-8">')
html.append(
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
)
html.append("    <title>Publications - Eleonora Alei</title>")
html.append(
    '    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">'
)
html.append('    <link href="css/custom.css" rel="stylesheet">')

html.append(
    '    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">'
)
html.append("</head>")
html.append("<body>")

# Add your navbar here
html.append('<header class="fixed-header">')
html.append(
    '    <nav class="navbar navbar-expand-lg navbar-light bg-light   main-navbar">'
)
html.append('        <div class="container">')
html.append(
    '            <a class="navbar-brand   main-navbar-brand" href="index.html">Eleonora Alei</a>'
)
html.append(
    '                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">'
)
html.append('<span class="navbar-toggler-icon"></span>')
html.append('<span class="navbar-toggler-icon"></span>')
html.append('<span class="navbar-toggler-icon"></span>')
html.append('<span class="navbar-toggler-icon"></span>')
html.append("            </button>")
html.append(
    '            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">'
)
html.append('                <ul class="navbar-nav main-navbar-nav">')
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link" href="index.html#about">About</a></li>'
)
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link" href="index.html#experience">Experience</a></li>'
)
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link" href="index.html#research-highlights">Research</a></li>'
)
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link" href="index.html#skills-interests">Skills</a></li>'
)
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link active" href="publications.html">Publications</a></li>'
)
html.append(
    '                    <li class="nav-item"><a class="nav-link main-nav-link"  href="cv.html">CV</a></li>'
)
html.append("                </ul>")
html.append(" <button id='dark-mode-toggle' class='btn btn-secondary ms-3'>")
html.append("                        <i class='fas fa-adjust'></i>")
html.append("                    </button>")
html.append("            </div>")
html.append("        </div>")
html.append("    </nav>")
html.append("</header>")

html.append('<main class="container mt-5">')
html.append('    <section id="publications" class="mt-5 pt-5">')
html.append('        <div class="section-header">')
html.append('            <h2><i class="fas fa-book-open"></i>Publications</h2>')
html.append("        </div>")

# Iterate across types
for itype in range(2):
    if itype == 0:
        html.append('        <h3 class="mb-4">Refereed Publications</h3>')
        with open("library_ref.json") as f:
            pubs = json.load(f)
    else:
        html.append(
            '        <br><br><h3 class="mb-4">Proceedings, Circulars and Conference Contributions</h3>'
        )
        with open("library_nonref.json") as f:
            pubs = json.load(f)

    html.append('        <div class="list-group">')

    # Iterate across all publications
    for i in range(pubs["response"]["numFound"]):
        paper = pubs["response"]["docs"][i]
        year = int(paper["year"])
        if year1 > 0 and year < year1:
            continue
        if year2 > 0 and year > year2:
            continue
        if paper["bibcode"] in bibskip:
            continue
        if itype == 0:
            nref += 1
        else:
            nnonref += 1

        auth = paper["author"][0].split(",")
        if itype == 0 and auth[0] == names[0]:
            nfirst += 1
        htable.append(paper["citation_count"])

        html.append('            <div class="list-group-item">')

        # Authors
        if len(paper["author"]) > 20:
            if auth[0] == names[0]:
                authors_text = f'<b>{paper["author"][0]}</b> et al.'
            elif len(name) > 1:
                authors_text = (
                    f'{paper["author"][0]} et al. (<b>{names[0]}, {names[1]}</b>)'
                )
            else:
                authors_text = f'{paper["author"][0]} et al.'
        else:
            authors_text = ""
            for j in range(len(paper["author"])):
                if j > 0:
                    authors_text += "; "
                auth = paper["author"][j].split(",")
                if auth[0] == names[0]:
                    authors_text += f'<b>{paper["author"][j]}</b>'
                else:
                    authors_text += paper["author"][j]

        html.append(f'                <p class="mb-1">{authors_text}</p>')

        # Title and Journal info
        html.append(
            f'                <p class="paper-title mb-1">{paper["title"][0]}</p>'
        )

        journal_info = f'{paper["pub"]}'
        if "volume" in paper:
            journal_info += f', Vol:{paper["volume"]}'
        if "issue" in paper:
            journal_info += f'-{paper["issue"]}'
        if "page" in paper:
            journal_info += f' pp{paper["page"][0]}'
        if "doi" in paper and wdoi:
            journal_info += f', doi:{paper["doi"][0]}'
        journal_info += f" (<b>{year}</b>)"
        html.append(f'                <p class="mb-1">{journal_info}</p>')

        # Links
        if wlinks:
            html.append('                <div class="mt-2">')
            html.append(
                f'                    <a href="https://ui.adsabs.harvard.edu/abs/{paper["bibcode"]}" class="btn btn-sm btn-primary me-2">ADS</a>'
            )
            if "doi" in paper:
                html.append(
                    f'                    <a href="https://doi.org/{paper["doi"][0]}" class="btn btn-sm btn-secondary me-2">Journal</a>'
                )
            if "alternate_bibcode" in paper:
                html.append(
                    f'                    <a href="https://ui.adsabs.harvard.edu/link_gateway/{paper["bibcode"]}/EPRINT_HTML" class="btn btn-sm btn-info">arXiv</a>'
                )
            html.append("                </div>")

        html.append("            </div>")

    html.append("        </div>")

html.append("    </section>")
html.append("</main>")

# Compute statistics
htable.sort(reverse=True)
hindex = 0
ncit = 0
for i in range(len(htable)):
    if htable[i] >= i:
        hindex += 1
    ncit += htable[i]

# Add summary table
if wtable:
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 4,
        '        <div class="card mb-5">',
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 5,
        '            <div class="card-body">',
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 6,
        '                <h3 class="card-title">Publication Summary</h3>',
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 7,
        '                <div class="table-responsive">',
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 8,
        '                    <table class="table table-hover publications-table">',
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 9,
        "                        <thead>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 10,
        "                            <tr>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 11,
        "                                <th>Publications</th>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 12,
        "                                <th>Refereed</th>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 13,
        "                                <th>Refereed First Author</th>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 14,
        "                                <th>Citations</th>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 15,
        "                                <th>h-index</th>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 16,
        "                            </tr>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 17,
        "                        </thead>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 18,
        "                        <tbody>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 19,
        f"                            <tr>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 20,
        f"                                <td>{nref+nnonref}</td>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 21,
        f"                                <td>{nref}</td>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 22,
        f"                                <td>{nfirst}</td>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 23,
        f"                                <td>{ncit}</td>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 24,
        f"                                <td>{hindex}</td>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 25,
        "                            </tr>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 26,
        "                        </tbody>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 27,
        "                    </table>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 28,
        "                </div>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 29,
        "            </div>",
    )
    html.insert(
        html.index('    <section id="publications" class="mt-5 pt-5">') + 30,
        "        </div>",
    )

html.append('<footer class="text-center py-3 mt-5">')
html.append("    <p>&copy; 2025 Eleonora Alei. All rights reserved.</p>")
html.append("</footer>")

html.append(
    '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'
)
html.append('<script src="js/custom.js"></script>')
html.append("</body>")
html.append("</html>")

# Write the HTML file
with open(f"{rdir}publications.html", "w") as fw:
    for line in html:
        fw.write(f"{line}\n")
