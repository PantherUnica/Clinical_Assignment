import unittest

from eval import judge
from eval.multibook.build_questions import on_topic
from eval.run_multibook import book_coverage, fact_hit, model_tag, usage_cost


class RetrievalScoring(unittest.TestCase):
    passages = [
        {"book_id": "plumbs", "page": 10, "page_end": 11},
        {"book_id": "merck", "page": 5, "page_end": 5},
    ]

    def test_book_coverage(self):
        self.assertEqual(book_coverage(["plumbs", "bsava"], self.passages), 0.5)
        self.assertEqual(book_coverage(["plumbs", "merck"], self.passages), 1.0)
        self.assertIsNone(book_coverage([], self.passages))

    def test_fact_hit_needs_same_book_and_page_in_range(self):
        self.assertTrue(fact_hit({"book_id": "plumbs", "pdf_page": 11}, self.passages))
        self.assertFalse(fact_hit({"book_id": "plumbs", "pdf_page": 12}, self.passages))
        self.assertFalse(fact_hit({"book_id": "bsava", "pdf_page": 5}, self.passages))

    def test_on_topic_any_group_all_keywords(self):
        groups = [["meloxicam", "cats"], ["fomepizole"]]
        self.assertTrue(on_topic("Meloxicam dose in CATS", groups))
        self.assertTrue(on_topic("give fomepizole", groups))
        self.assertFalse(on_topic("meloxicam in dogs", groups))


class CostAndNames(unittest.TestCase):
    def test_usage_cost_uses_price_table(self):
        usage = [{"model": "gpt-4o-mini", "input_tokens": 1_000_000, "output_tokens": 1_000_000}]
        self.assertAlmostEqual(usage_cost(usage), 0.15 + 0.60)

    def test_usage_cost_unknown_model_is_none(self):
        self.assertIsNone(usage_cost([{"model": "mystery", "input_tokens": 1, "output_tokens": 1}]))

    def test_model_tag_is_filename_safe(self):
        self.assertEqual(model_tag("ollama:qwen2.5:7b"), "ollama_qwen2.5_7b")


class JudgeParsing(unittest.TestCase):
    def test_fact_recall_counts_partial_as_half(self):
        out = judge.normalise({"facts": [{"n": 1, "verdict": "present"}, {"n": 2, "verdict": "partial"},
                                         {"n": 3, "verdict": "contradicted"}]}, 3)
        self.assertAlmostEqual(out["fact_recall"], 0.5)
        self.assertEqual(out["contradicted"], 1)

    def test_missing_fact_entries_count_as_missing(self):
        out = judge.normalise({"facts": [{"n": 1, "verdict": "present"}]}, 2)
        self.assertAlmostEqual(out["fact_recall"], 0.5)

    def test_unanswerable_has_no_recall(self):
        self.assertIsNone(judge.normalise({"facts": [], "refused": True}, 0)["fact_recall"])

    def test_error_passthrough(self):
        self.assertIsNone(judge.normalise({"error": "bad json"}, 2)["fact_recall"])

    def test_prompt_never_names_the_answering_model(self):
        q = {"question": "Q?", "type": "two_book", "expected_behaviour": "x", "conflict": None,
             "key_facts": [{"fact": "f1"}]}
        prompt = judge.build_prompt(q, "answer text", ["Book A, p. 1"])
        self.assertNotIn("gpt", prompt.lower())


if __name__ == "__main__":
    unittest.main()
