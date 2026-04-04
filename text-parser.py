

# following this page https://github.com/pymupdf/PyMuPDF
#! ######################################### STEP 1 ##############################################


import pymupdf as pypdf # type: ignore
import spacy as spc # type: ignore
nlp = spc.load("fr_core_news_lg")

import json
import pathlib as path

# Set up Entity Ruler, rule-based
print("Setting up Entity Ruler...")
patterns = []
with open("'entity_ruler_sorted.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # tokens = line.split(" ") #Split tokens
        tokens = [line] #No Split

        pattern = [{"LOWER": token.lower()} for token in tokens]
        patterns.append({"label": "LOC", "pattern": pattern})

ruler = nlp.add_pipe("entity_ruler", after="ner")
ruler.add_patterns(patterns)
print("Entity Ruler initialized")


# Process PDFs
all_blocks = []
pdf_folder_sub = "pdfs-OCR\\2005" #! CHANGE DIRECTORY!!!!
pdf_folder = path.Path(f"C:\\Users\\13065\\Documents\\GitHub\\queering-geographies\\{pdf_folder_sub}")
for pdf_file in pdf_folder.glob("*.pdf"):
    print(f"Processing {pdf_file.name}...")

    pdf_doc = pypdf.open(pdf_file)
    page_count = pdf_doc.page_count

    for page in pdf_doc: #(x0, y0, x1, y1, text, block_no, block_type)
        blocks = page.get_text("blocks", flags=pypdf.TEXT_PRESERVE_LIGATURES | pypdf.TEXT_PRESERVE_IMAGES)
        for block in blocks:
            if block[0] > 10000: #skip random outliers
                continue
            
            #! skip Images  COMMENT OUT OF FOR FULL SCRIPT
            # if block[6] == 1:
            #     continue
            #! skip Images  COMMENT OUT OF FOR FULL SCRIPT
            
            text_line = block[4]
            if block[6] == 1:
                text_line = ""
            else:
                text_line = text_line.replace("\n", " ")
            
            all_blocks.append({
                "source": pdf_file.name,
                "page": page.number + 1, #human number readable
                "bbox": [round(block[0], -1), round(block[1], -1), round(block[2], -1), round(block[3], -1)], #maybe get rid of this
                "block_no": block[5],
                "block_type": block[6],
                "text": text_line,
                # "entities": [] if block[6] == 1 else [
                #     {"text": ent.text, "label": ent.label_} for ent in nlp(text_line).ents if ent.label_ in ["LOC", "GPE", "ORG"]
                #     ]
            })
            
            print(f"     > pg {page.number + 1}")
        
with open("fugue_2005_for-spacy.json", "w", encoding="utf-8") as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)

print("oh yeah!")



#! For a Specific Page
# specific_page = pdf_doc[39]
# blocks = specific_page.get_text("blocks", flags=pypdf.TEXT_PRESERVE_LIGATURES)
# for block in blocks:
#     print(round(block[0], -1), round(block[1], -1), round(block[2], -1), round(block[3], -1)) #Round the bbox coordinates
#     if block[6] == 1: 
#         print(f"#IMAGE_BLOCK")
#     else:
#         text_line = block[4]
#         text_line_remove_newline = text_line.replace("\n", " ")
#         print(f"{text_line_remove_newline}")