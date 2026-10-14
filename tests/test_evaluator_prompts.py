import json
import string
import unittest
from pathlib import Path
from typing import Any, Dict, Iterator, Tuple

PROMPTS_PATH = (
    Path(__file__).resolve().parent.parent
    / "marble"
    / "evaluator"
    / "evaluator_prompts.json"
)


def iter_templates(node: Dict[str, Any], path: str = "") -> Iterator[Tuple[str, str]]:
    for key, value in node.items():
        if isinstance(value, dict):
            yield from iter_templates(value, f"{path}.{key}")
        elif isinstance(value, str):
            yield f"{path}.{key}", value


def placeholder_names(template: str) -> set:
    return {
        field for _, field, _, _ in string.Formatter().parse(template) if field
    }


class TestEvaluatorPrompts(unittest.TestCase):
    def setUp(self) -> None:
        with open(PROMPTS_PATH, encoding="utf-8") as f:
            self.prompts = json.load(f)

    def test_every_template_formats(self) -> None:
        for path, template in iter_templates(self.prompts):
            with self.subTest(prompt=path):
                fields = {name: "X" for name in placeholder_names(template)}
                template.format(**fields)

    def test_rating_prompts_keep_json_example(self) -> None:
        for name in ("Communication", "Planning"):
            with self.subTest(prompt=name):
                template = self.prompts["Graph"][name]["prompt"]
                fields = {field: "X" for field in placeholder_names(template)}
                self.assertIn('{"rating": 4}', template.format(**fields))


if __name__ == "__main__":
    unittest.main()
