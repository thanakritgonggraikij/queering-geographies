# Label studio wants plain txt or JSON list with text field.
# This script will extract text, source, and page fields from "fugue_blocks_TEXTONLY.json"

import json
import pathlib as path

#! ######################################### STEP 2 ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################
#! ######################################### YOU CAN SKIP THIS!!!!! ##############################################


# Load Json file to read
input_f = path.Path("C:\\Users\\13065\\Documents\\GitHub\\queering-geographies\\fugue_2011-2016-2021_for_LS_FULL.json") #! CHANGE DIRECTORY!!!!

with open(input_f, "r", encoding="utf-8") as f:
    all_blocks = json.load(f)

# Load entity ruler sorted list and split terms
entity_terms = set()
entity_ruler_file = path.Path("C:\\Users\\13065\\Documents\\GitHub\\queering-geographies\\'entity_ruler_sorted.txt")
with open(entity_ruler_file, "r", encoding="utf-8") as f:
    for line in f:
        rule = line.strip()
        if not rule:
            continue
        for token in rule.split():
            if token:
                entity_terms.add(token.lower())

print(f"Loaded {len(entity_terms)} entity tokens from 'entity_ruler_sorted.txt'")

# Address-like check: digit followed by comma/space then street token
street_tokens = {"rue", "avenue", "boulevard", "boul", "av", "st", "montreal", "montréal", "parc"}

output_f = []
for block in all_blocks:
    text = block.get("text", "")
    if not isinstance(text, str) or not text.strip():
        continue

    text_lower = text.lower()

    # Filter 1: must contain at least one entity ruler token
    if not any(term in text_lower for term in entity_terms):
        continue

    # Filter 2: must contain at least one location keyword (from entity terms or street tokens)
    has_location_keyword = any(tok in text_lower for tok in street_tokens)
    if not has_location_keyword:
        # Also check any entity term looks like a location keyword e.g. rue
        has_location_keyword = any(tok in text_lower for tok in entity_terms if tok in street_tokens)

    if not has_location_keyword:
        continue

    # Filter 3: address-like pattern using digit then next token street keyword
    tokens = [t.strip(".,;:") for t in text_lower.replace("\n", " ").split() if t.strip(".,;:")]
    has_address_like = False
    for i in range(len(tokens) - 1):
        if tokens[i].isdigit() and tokens[i+1] in street_tokens:
            has_address_like = True
            break

    if not has_address_like:
        continue

    if not block.get("entities"):
        continue

    output_f.append({
        "text": text,
        "source": block.get("source"),
        "page": block.get("page"),
        "entities": block.get("entities")
    })

print(f"Writing {len(output_f)} cleaned blocks")
with open("fugue_2011-2016-2021_for_LS_CLEAN.json", "w", encoding="utf-8") as f:
    json.dump(output_f, f, ensure_ascii=False, indent=2)
    

print("Cleaned!")

# THEN start Label Studio