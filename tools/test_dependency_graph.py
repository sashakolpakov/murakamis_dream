#!/usr/bin/env python3
"""Structural controls for explicit article ownership and witnessed imports.

These tests do not validate mathematical proofs or the completeness of the
manually traced inventory. They use temporary article files and write no
repository outputs. Run: python3 -I tools/test_dependency_graph.py
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "dependency_builder", Path(__file__).with_name("build_dependency_graph.py"))
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class ArticleDependencies(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for article in ("a", "b", "c"):
            source = self.root / "papers" / article / "main.tex"
            source.parent.mkdir(parents=True)
            source.write_text(f"Written source for article {article}.\n")
        self.data = {
            "articles": {
                a: {"title": f"Article {a}", "path": f"papers/{a}/main.tex"}
                for a in ("a", "b", "c")
            },
            "article_dependencies": [{
                "from": "a", "to": "b",
                "witnesses": [{
                    "path": ["a_lemma", "adapter", "b_result"],
                    "reason": "Uses the lemma through the recorded adapter."
                }]
            }]
        }
        self.nodes = {
            "a_seed": {"article": "a"},
            "a_lemma": {"article": "a"},
            "adapter": {"article": None},
            "b_result": {"article": "b"},
        }
        self.edges = {
            ("a_seed", "a_lemma"),
            ("a_lemma", "adapter"),
            ("adapter", "b_result"),
        }

    def validate(self, data=None, nodes=None, edges=None):
        return BUILDER.validate_articles(
            self.data if data is None else data,
            self.nodes if nodes is None else nodes,
            self.edges if edges is None else edges,
            root=self.root)

    def test_internal_uses_and_unowned_adapter(self):
        result, hashes = self.validate()
        self.assertEqual(result["article_edges"], [("a", "b")])
        self.assertEqual(result["owned_statements"], 3)
        self.assertEqual(result["unowned_statements"], 1)
        self.assertLess(result["article_topological_order"].index("a"),
                        result["article_topological_order"].index("b"))
        path = "papers/a/main.tex"
        self.assertEqual(hashes[path], hashlib.sha256(
            (self.root / path).read_bytes()).hexdigest())
        self.assertFalse((self.root / "docs").exists())

    def test_stop_at_nearest_owned_result(self):
        self.nodes["c_result"] = {"article": "c"}
        self.edges.add(("b_result", "c_result"))
        self.data["article_dependencies"].append({
            "from": "b", "to": "c",
            "witnesses": [{"path": ["b_result", "c_result"],
                           "reason": "Uses the intervening article's result."}]
        })
        result, _ = self.validate()
        self.assertEqual(result["article_edges"], [("a", "b"), ("b", "c")])

    def test_same_article_edges_need_no_external_declaration(self):
        data = deepcopy(self.data)
        data["article_dependencies"] = []
        nodes = {"first": {"article": "a"}, "second": {"article": "a"}}
        result, _ = self.validate(data, nodes, {("first", "second")})
        self.assertEqual(result["article_edges"], [])

    def test_cycle_appears_only_after_article_contraction(self):
        # The statement graph is a path, so checking it alone cannot find this.
        nodes = {
            "a_seed": {"article": "a"},
            "b_use": {"article": "b"},
            "a_use": {"article": "a"},
        }
        edges = {("a_seed", "b_use"), ("b_use", "a_use")}
        order, _, _ = BUILDER.topological(nodes, edges)
        self.assertEqual(order, ["a_seed", "b_use", "a_use"])
        data = deepcopy(self.data)
        data["article_dependencies"] = [
            {"from": "a", "to": "b", "witnesses": [{
                "path": ["a_seed", "b_use"], "reason": "B uses A's first result."}]},
            {"from": "b", "to": "a", "witnesses": [{
                "path": ["b_use", "a_use"], "reason": "A later uses B's result."}]},
        ]
        with self.assertRaisesRegex(ValueError, "Article dependency cycle"):
            self.validate(data, nodes, edges)

    def test_actual_statement_cycle_is_rejected(self):
        edges = self.edges | {("a_lemma", "a_seed")}
        with self.assertRaisesRegex(ValueError, "Cycle in declared dependencies"):
            self.validate(edges=edges)

    def test_unknown_owner(self):
        self.nodes["a_lemma"]["article"] = "not-an-article"
        with self.assertRaisesRegex(ValueError, "unknown article owner"):
            self.validate()

    def test_missing_owner_must_be_explicit_null(self):
        del self.nodes["adapter"]["article"]
        with self.assertRaisesRegex(ValueError, "explicit article owner or null"):
            self.validate()

    def test_invalid_registry_path(self):
        for path in ("papers/missing/main.tex", "../outside.tex",
                     str(self.root / "papers/a/main.tex")):
            with self.subTest(path=path):
                data = deepcopy(self.data)
                data["articles"]["a"]["path"] = path
                with self.assertRaisesRegex(ValueError, "article source"):
                    self.validate(data=data)

    def test_registry_and_declarations_are_required(self):
        for key in ("articles", "article_dependencies"):
            with self.subTest(key=key):
                data = deepcopy(self.data)
                del data[key]
                with self.assertRaisesRegex(ValueError, "Explicit articles"):
                    self.validate(data=data)

    def test_unknown_import_article(self):
        self.data["article_dependencies"][0]["to"] = "unknown"
        with self.assertRaisesRegex(ValueError, "Unknown article in import"):
            self.validate()

    def test_explicit_article_self_import_rejected(self):
        self.data["article_dependencies"].append({
            "from": "a", "to": "a",
            "witnesses": [{"path": ["a_seed", "a_lemma"],
                           "reason": "This is internal, not an import."}]
        })
        with self.assertRaisesRegex(ValueError, "Article self-import"):
            self.validate()

    def test_missing_import(self):
        self.data["article_dependencies"] = []
        with self.assertRaisesRegex(ValueError, "missing=.*a.*b"):
            self.validate()

    def test_missing_witness(self):
        self.data["article_dependencies"][0]["witnesses"] = []
        with self.assertRaisesRegex(ValueError, "missing article import witness"):
            self.validate()

    def test_witness_requires_reason(self):
        self.data["article_dependencies"][0]["witnesses"][0]["reason"] = " "
        with self.assertRaisesRegex(ValueError, "use explanation"):
            self.validate()

    def test_witness_requires_actual_step(self):
        self.data["article_dependencies"][0]["witnesses"][0]["path"] = [
            "a_lemma", "b_result"]
        with self.assertRaisesRegex(ValueError, "unsupported witness dependency step"):
            self.validate()

    def test_witness_cannot_invent_node(self):
        self.data["article_dependencies"][0]["witnesses"][0]["path"] = [
            "a_lemma", "invented", "b_result"]
        with self.assertRaisesRegex(ValueError, "invalid witness node path"):
            self.validate()

    def test_witness_endpoint_owner_must_match(self):
        self.data["article_dependencies"][0]["from"] = "c"
        with self.assertRaisesRegex(ValueError, "witness endpoint owners disagree"):
            self.validate()

    def test_witness_cannot_skip_intervening_article(self):
        self.nodes["adapter"]["article"] = "c"
        with self.assertRaisesRegex(ValueError, "intervening article"):
            self.validate()

    def test_duplicate_import_rejected(self):
        self.data["article_dependencies"].append(
            deepcopy(self.data["article_dependencies"][0]))
        with self.assertRaisesRegex(ValueError, "Repeated article import"):
            self.validate()


if __name__ == "__main__":
    unittest.main(verbosity=2)
