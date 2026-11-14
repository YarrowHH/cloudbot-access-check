import json
from pathlib import Path
value = json.loads(Path("src/message.json").read_text())
assert value == {"message": "CloudBot acceptance passed"}, "Unexpected candidate"
print("Bounded JSON candidate verified")
