#! SPACY PARCER
    # NER with Custom SpaCy Model
    # Export to JSON for geocoding


import spacy as spc # type: ignore
import json


print("LET'S GO")
nlp = spc.load("C:\\Users\\13065\\Documents\\GitHub\\queering-geographies\\spacy-training\\output\\model-best") #Use this for our TRAINED MODEL

with open("fugue_2021_for-spacy.json", "r", encoding="utf-8") as f: #! CHANGE DIRECTORY!!!!
    blocks = json.load(f)

print("Loaded and Read")

texts = [block["text"] for block in blocks]
docs = nlp.pipe(texts, batch_size=64)
i = 0 # progress tracjker int

output = []

for block, doc in zip(blocks, docs):
    block["entities"] = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    if not block["entities"]: #skip if no entities
        continue
    
    output.append({
        "source": block["source"],
        "page": block["page"],
        "text": block["text"],
        "entities": block["entities"],
    })
    
    if i % 1000 == 0: 
        print(f"     Processed {i} blocks...")
    i += 1

print("Blocks processed, writing to JSON...")
with open("fugue_2021_spacy-processed.json", "w", encoding="utf-8") as f: #! CHANGE DIRECTORY!!!!
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"{len(output)} Rows Total")
print("DONE!")
