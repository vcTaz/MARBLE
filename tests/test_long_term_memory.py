import unittest
from typing import List
from unittest.mock import patch

from litellm.types.utils import Message
from numpy import ndarray

from marble.memory.long_term_memory import LongTermMemory


def fake_embedding(model: str, input: str) -> List[float]:
    """Keyword embedding so retrieval is deterministic and needs no API."""
    return [
        1.0 if ("cold" in input or "weather" in input) else 0.0,
        1.0 if "sleep" in input else 0.0,
        0.1,
    ]


class TestLongTermMemory(unittest.TestCase):
    def setUp(self) -> None:
        patchers = [
            patch(
                "marble.memory.long_term_memory.text_embedding",
                side_effect=fake_embedding,
            ),
            patch(
                "marble.memory.long_term_memory.model_prompting",
                return_value=[Message(content="summary", role="assistant")],
            ),
        ]
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.memory = LongTermMemory()

    def test_update(self) -> None:
        result_1 = Message(content="It is cold today.", role="assistant")
        self.memory.update(
            key="key", information={"type": "action_response", "result": result_1}
        )
        result_2 = Message(content="I want to sleep.", role="assistant")
        self.memory.update(
            key="key", information={"type": "action_response", "result": result_2}
        )
        self.assertIsInstance(self.memory.storage, list)
        self.assertIsInstance(self.memory.storage[0], tuple)
        self.assertIsInstance(self.memory.storage[0][0], dict)
        self.assertIsInstance(self.memory.storage[0][1], ndarray)

    def test_retrieve_latest(self) -> None:
        result_1 = Message(content="It is cold today.", role="assistant")
        information_1 = {"type": "action_response", "result": result_1}
        self.memory.update(key="key", information=information_1)
        result_2 = Message(content="I want to sleep.", role="assistant")
        information_2 = {"type": "action_response", "result": result_2}
        self.memory.update(key="key", information=information_2)
        true_latest_information = information_2
        latest_information = self.memory.retrieve_latest()
        self.assertIs(latest_information, true_latest_information)

    def test_retrieve_most_relevant(self) -> None:
        result_1 = Message(content="It is cold today.", role="assistant")
        information_1 = {"type": "action_response", "result": result_1}
        self.memory.update(key="key", information=information_1)
        result_2 = Message(content="I want to sleep.", role="assistant")
        information_2 = {"type": "action_response", "result": result_2}
        self.memory.update(key="key", information=information_2)
        true_relevant_information = information_1
        result = Message(content="What's the weather like today?", role="assistant")
        most_relevant_information = self.memory.retrieve_most_relevant(
            information={"type": "action_response", "result": result}
        )
        self.assertIs(most_relevant_information[0], true_relevant_information)

        most_relevant_information = self.memory.retrieve_most_relevant(
            summarize=True, information={"type": "action_response", "result": result}
        )
        self.assertIsInstance(most_relevant_information, Message)

    def test_retrieve_all(self) -> None:
        result_1 = Message(content="It is cold today.", role="assistant")
        information_1 = {"type": "action_response", "result": result_1}
        self.memory.update(key="key", information=information_1)
        result_2 = Message(content="I want to sleep.", role="assistant")
        information_2 = {"type": "action_response", "result": result_2}
        self.memory.update(key="key", information=information_2)
        all_information = self.memory.retrieve_all()
        self.assertIn(information_1, all_information)
        self.assertIn(information_2, all_information)


if __name__ == "__main__":
    unittest.main()
