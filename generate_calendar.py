import pandas as pd
from ics import Calendar

SHEET_ID = "1vOgaCYYH2EGlBC4hm_lWaQ5yFDzky6-ZqNni61DbkPc"
GID = "593313266"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"

df = pd.read_csv(url)

cal = Calendar()

for _, row in df.iterrows():
    try:
        title = str(row.get("Event", "")).strip()
        date = row.get("Date", "")

        if not title or title.lower() == "nan":
            continue

        event = cal.events.add(
            name=title,
            begin=str(pd.to_datetime(date)),
        )

    except:
        continue

with open("calendar.ics", "w", encoding="utf-8") as f:
    f.write(str(cal))

print("calendar.ics generated")
