import json

# Input/output file names
INPUT_FILE = "public_transport_stops.geojson"
OUTPUT_FILE = "filtered_transport_stops.geojson"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Keep only features that are NOT BUS or SKYBUS
data["features"] = [
    f for f in data["features"]
    if f["properties"]["MODE"].upper() in ("METRO TRAIN")
]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    # indent=2 for readability; remove for smaller file
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Filtered GeoJSON written to {OUTPUT_FILE}")
