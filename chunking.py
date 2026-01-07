import os
import re
import json

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

dataset = []

for category in os.listdir(RAW_DIR):
    cat_dir = os.path.join(RAW_DIR, category)
    if os.path.isdir(cat_dir):
        for filename in os.listdir(cat_dir):
            filepath = os.path.join(cat_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Cleaning
            text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
            text = text.strip()
            
            dataset.append({
                "id": filename.replace(".txt", ""),
                "category": category,
                "text": text
            })

# Save processed JSON
with open(os.path.join(PROCESSED_DIR, "dataset.json"), "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Processed {len(dataset)} documents")

