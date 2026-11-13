import unittest

from eval import metrics as m

RANKED = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


class RetrievalMetrics(unittest.TestCase):
    def test_first_relevant_rank(self):
        self.assertEqual(m.first_relevant_rank(RANKED, {"c", "h"}), 3)
        self.assertIsNone(m.first_relevant_rank(RANKED, {"z"}))
        self.assertIsNone(m.first_relevant_rank(RANKED, set()))

    def test_recall_at_k_is_hit_rate(self):
        self.assertEqual(m.recall_at_k(RANKED, {"c"}, 3), 1.0)
        self.assertEqual(m.recall_at_k(RANKED, {"c"}, 2), 0.0)
        self.assertEqual(m.recall_at_k(RANKED, {"c", "d"}, 5), 1.0)

    def test_empty_relevant_scores_as_miss(self):
        self.assertEqual(m.recall_at_k(RANKED, set(), 10), 0.0)
        self.assertEqual(m.reciprocal_rank(RANKED, set()), 0.0)
        self.assertEqual(m.precision_at_k(RANKED, set(), 5), 0.0)

    def test_reciprocal_rank(self):
        self.assertEqual(m.reciprocal_rank(RANKED, {"a"}), 1.0)
        self.assertAlmostEqual(m.reciprocal_rank(RANKED, {"d", "b"}), 0.5)
        self.assertAlmostEqual(m.reciprocal_rank(RANKED, {"j"}), 0.1)

    def test_precision_divides_by_k(self):
        self.assertAlmostEqual(m.precision_at_k(RANKED, {"a", "c", "z"}, 5), 2 / 5)
        self.assertAlmostEqual(m.precision_at_k(["a"], {"a"}, 5), 1 / 5)
        with self.assertRaises(ValueError):
            m.precision_at_k(RANKED, {"a"}, 0)


class CitationMetrics(unittest.TestCase):
    def test_chunk_citation_precision(self):
        self.assertAlmostEqual(m.citation_precision(["a", "b"], {"a"}), 0.5)
        self.assertEqual(m.citation_precision(["a", "a"], {"a"}), 1.0)
        self.assertIsNone(m.citation_precision([], {"a"}))

    def test_page_overlap(self):
        self.assertTrue(m.spans_overlap(("B", 10, 12), ("B", 12, 14)))
        self.assertFalse(m.spans_overlap(("B", 10, 11), ("B", 12, 14)))
        self.assertFalse(m.spans_overlap(("A", 10, 12), ("B", 10, 12)))

    def test_page_citation_precision(self):
        relevant = [("B", 10, 11)]
        self.assertAlmostEqual(
            m.page_citation_precision([("B", 11, 12), ("B", 40, 41)], relevant), 0.5
        )
        self.assertIsNone(m.page_citation_precision([], relevant))

    def test_page_citation_hit_ignores_extra_citations(self):
        relevant = [("B", 10, 11)]
        self.assertEqual(m.page_citation_hit([("B", 11, 12), ("B", 40, 41)], relevant), 1.0)
        self.assertEqual(m.page_citation_hit([("B", 40, 41)], relevant), 0.0)
        self.assertIsNone(m.page_citation_hit([], relevant))


class AnswerProxies(unittest.TestCase):
    def test_number_recall(self):
        ref = "0.625-1.25 mg per cat p.o. q24h"
        self.assertAlmostEqual(m.number_recall(ref, "Give 0.625 mg, up to 1.25 mg q24h"), 1.0)
        # ref numbers are {0.625, 1.25, 24} ("q24h" counts); candidate has only 0.625
        self.assertAlmostEqual(m.number_recall(ref, "Give 0.625 mg once daily"), 1 / 3)
        self.assertIsNone(m.number_recall("No numbers here", "anything"))

    def test_term_recall(self):
        self.assertAlmostEqual(m.term_recall("amlodipine hypertension", "amlodipine for cats"), 0.5)
        self.assertIsNone(m.term_recall("the and", "x"))


class Aggregation(unittest.TestCase):
    def test_mean_skips_none(self):
        self.assertEqual(m.mean([1.0, None, 0.0]), (0.5, 2))
        self.assertEqual(m.mean([None]), (None, 0))

    def test_percentile(self):
        self.assertEqual(m.percentile([1.0, 2.0, 3.0], 50), 2.0)
        self.assertIsNone(m.percentile([], 50))
        self.assertEqual(m.percentile([7.0], 95), 7.0)


if __name__ == "__main__":
    unittest.main()
