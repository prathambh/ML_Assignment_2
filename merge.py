import nbformat
from nbformat.v4 import new_notebook, new_code_cell

def merge_notebooks(notebook_paths):
    merged_notebook = new_notebook()
    
    for notebook_path in notebook_paths:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                merged_notebook.cells.append(new_code_cell(cell.source))
            else:
                merged_notebook.cells.append(cell)
    
    return merged_notebook

notebook_paths = ['C_1.ipynb', 'C_3.ipynb', 'C_5.ipynb']
merged_notebook = merge_notebooks(notebook_paths)

# Write the merged notebook to a file
output_file = 'merged_notebook.ipynb'
with open(output_file, 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)
