"""Regression checks for formulas silently falling back to literal TeX."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from check_book import Links
from build_book import Headings, repair_numbered_fragments


class HeadingLinks(unittest.TestCase):
    def test_contents_omit_the_hidden_tex_annotation(self):
        parser = Headings()
        parser.feed('<h2 id="width">Width <math><mi>k</mi>'
                    '<annotation encoding="application/x-tex">k</annotation>'
                    '</math></h2>')
        self.assertEqual(parser.items, [("width", "Width k")])

    def test_numbered_link_is_repaired_only_for_existing_heading(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            target = directory / "proof.html"
            target.write_text('<h2 id="the-proof">2. The proof</h2>')
            source = directory / "index.html"
            source.write_text('<a href="proof.html#2-the-proof">Proof</a>'
                              '<a href="proof.html#3-missing">Missing</a>')
            self.assertEqual(repair_numbered_fragments(directory), 1)
            result = source.read_text()
            self.assertIn('href="proof.html#the-proof"', result)
            self.assertIn('href="proof.html#3-missing"', result)


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc is required")
class FormulaRendering(unittest.TestCase):
    def render(self, source):
        result = subprocess.run(
            ["pandoc", "--from=markdown+tex_math_single_backslash",
             "--to=html5", "--mathml"],
            input=source, text=True, capture_output=True, check=True,
        )
        parser = Links()
        parser.feed(result.stdout)
        return result, parser

    def test_unsupported_font_command_is_detected(self):
        result, parser = self.render(r"$B_{\rm in}^{-1}B_{\rm out}$")
        self.assertIn("Could not convert TeX math", result.stderr)
        self.assertTrue(parser.math_errors)

    def test_supported_formula_has_native_math(self):
        result, parser = self.render(r"$B_{\mathrm{in}}^{-1}B_{\mathrm{out}}$")
        self.assertFalse(result.stderr)
        self.assertIn("<math", result.stdout)
        self.assertFalse(parser.math_errors)

    def test_code_example_is_not_treated_as_formula(self):
        result, parser = self.render("```tex\n$B_{\\rm in}$\n```\n")
        self.assertFalse(result.stderr)
        self.assertFalse(parser.math_errors)

    def test_mathml_error_is_detected(self):
        parser = Links()
        parser.feed('<math><merror><mtext>bad formula</mtext></merror></math>')
        self.assertTrue(parser.math_errors)


if __name__ == "__main__":
    unittest.main()
