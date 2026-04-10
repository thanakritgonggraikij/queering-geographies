import json
# import re
import pandas as pd

years = ["webapp_full"] #! CHANGE YEAR!!!!

for year in years:
    #load JSON
    with open(f"fugue_{year}_spacy-processed.json", "r", encoding="utf-8-sig") as f:
        data = json.load(f)
        
    rows = []
    for item in data:
        #Call items
        source = item.get("source", "")
        page = item.get("page", "")
        text = item.get("text", "")
        entities = item.get("entities", [])
        
        #Make New row for every entity
        for entity in entities:
            ent_text = entity.get("text", "")
            ent_label = entity.get("label", "")
            
            # def calculate_location_score(ent_text):
            #     score = 0.0

            #     #! Check for street keywords
            #     street_keywords = ["rue", "av", "boul", "boui", "bld", "pl", "st", "street", "avenue", "boulevard", "place", "est", "nord", "sud", "ouest"] #! CHANGE THIS LIST!!!!
            #     if any(keyword in ent_text.lower() for keyword in street_keywords):
            #         score += 0.30
                
            #     #! Check for keywords from keywords.txt (example list)
            #     with open("keywords.txt", "r", encoding="utf-8-sig") as f:
            #         keywords = [line.strip() for line in f]
            #     if any(keyword in ent_text.lower() for keyword in keywords):
            #         score += 0.20
                
            #     #! Check for city names (example list)
            #     city_names = ["Montréal", "mtl", "Québec", "montreal", "laval", "saint-laurent", "parc"] #! Update List if required!!!!
            #     if any(city in ent_text.lower() for city in [name.lower() for name in city_names]):
            #         score += 0.20
                
            #     #! Check for postal code pattern XXX XXX
            #     if re.match(r"\d{3} \d{3}", ent_text):
            #         score += 0.15
                
            #     #! Check length
            #     if len(ent_text) > 10:
            #         score += 0.15
                
            #     return min(score, 1.0)
            # ent_loc_score = calculate_location_score(ent_text) #! Location Score
            
            rows.append({
                "source": source,
                "page": page,
                "text": text,
                "entity_text": ent_text,
                "entity_label": ent_label,
                # "entity_loc_score": ent_loc_score
            })
            
    #Create DataFrame + Export as CSV
    df = pd.DataFrame(rows)

    #! OUTPUT
    df.to_csv(f"fugue_{year}_spacy-processed.csv", index=False, encoding="utf-8-sig") 
    print(f"CSV created with {len(df)} rows")