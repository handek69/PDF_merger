__author__ = "Kaushik Hande"
__version__ = "1.0"

from PyPDF2 import PdfFileMerger

import os
included_extensions = ['pdf']
pdfs = [fn for fn in os.listdir()
              if any(fn.endswith(ext) for ext in included_extensions)]
cwd = os.path.split(os.getcwd())

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_"+cwd[1]+".pdf")
merger.close()
