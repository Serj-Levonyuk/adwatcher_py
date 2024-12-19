#%matplotlib inline
import matplotlib.pyplot as plt

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

doc = DocumentFile.from_pdf("Cash-Payment-Receipt-Template.pdf")
print(f"Number of pages: {len(doc)}")
predictor = ocr_predictor(pretrained=True)
print(predictor)
result = predictor(doc)
json_export = result.export()
print(json_export)