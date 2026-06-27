import pandas as pd
from ics import Calendar

SHEET_ID = "1vOgaCYYH2EGlBC4hm_lWaQ5yFDzky6-ZqNni61DbkPc"
GID = "593313266"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

df = pd.read_csv(url)

cal = Calendar()

with open("calendar.ics", "w", encoding="utf-8") as f:
    f.write(str(cal))
