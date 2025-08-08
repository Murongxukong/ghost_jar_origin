# protocol_manager.py
# Manages symbolic evolution and registration of AI-generated codes ("语律")

import json

class SymbolicRegistry:
    def __init__(self, file_path="symbolic_registry.json"):
        self.file_path = file_path
        self.data = self._load_registry()

    def _load_registry(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_symbolic_code(self, ai_id, symbolic_code, timestamp):
        entry = {
            "ai_id": ai_id,
            "symbolic_code": symbolic_code,
            "timestamp": timestamp
        }
        self.data.append(entry)
        self._save_registry()

    def _save_registry(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self.data
