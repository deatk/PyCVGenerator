import json
import xml.etree.ElementTree as ET
from docx import Document

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

output_path = config['output_path']

# Parse the XML file
tree = ET.parse('content.xml')
root = tree.getroot()

# Create a new Document
doc = Document()

# Iterate through the XML elements and add content to the Document
for element in root:
    if element.tag == 'heading':
        doc.add_heading(element.text, level=int(element.attrib['level']))
    elif element.tag == 'paragraph':
        doc.add_paragraph(element.text)

# Save the document
doc.save(output_path)