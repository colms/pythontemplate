import json
from typing import Any, Dict
from pathlib import Path


def read_json_resource_file(file_name: str) -> Dict[str, Any]:
    absolute_path = Path(__file__).resolve().parent / 'resources' / file_name
    with open(absolute_path) as json_file:
        json_dict = json.load(json_file)
    return json_dict
