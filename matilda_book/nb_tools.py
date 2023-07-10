import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("./*.ipynb", recursive=False)
print(notebooks)

add_tag = 'hide-input'

# Search through each notebook and look for the text, add a tag if necessary
cnt=0
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        if cell['cell_type'] != 'code':
            continue
        cell_tags = cell.get('metadata', {}).get('tags', [])

        if add_tag not in cell_tags:
            cnt+=1
            cell_tags.append(add_tag)
        if len(cell_tags) > 0:
            cell['metadata']['tags'] = cell_tags

    nbf.write(ntbk, ipath)

print(f'{cnt} cells updated.')