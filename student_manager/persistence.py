import json

CURRENT_VERSION = 1


class JSONPersistence:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save(self, records):
        data = {
            "version": CURRENT_VERSION,
            "students": {
                name: {
                    "age": info["age"],
                    "grades": list(info["grades"]),
                    "courses": list(info["courses"])
                }
                for name, info in records.items()
            }
        }

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            if data.get("version") != CURRENT_VERSION:
                raise ValueError("Unsupported JSON version")

            return {
                name: {
                    "age": info["age"],
                    "grades": set(info["grades"]),
                    "courses": set(info["courses"])
                }
                for name, info in data["students"].items()
            }

        except FileNotFoundError:
            return {}
