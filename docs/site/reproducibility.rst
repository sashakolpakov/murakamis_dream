Reproduction and evidence
=========================

The executable companion separates exact finite certificates from the analytic proof. Run the standard-library verification suite from the repository root:

.. code-block:: sh

   python3 repro/verify.py --output repro/results

The two-leaf certificate covers sixteen slope intervals. The single-leaf attachment certificate covers a square by 55 dyadic rectangles and checks 880 outward-rounded rational inequalities. Their tangent bounds are global by concavity and affine vertex maximization. Candidate numerical optimizers are absent from verification.

The arithmetic encloses pi, sine, logarithms and the integrated Euler sine product by rational series and explicit remainder bounds. The verifier also checks state feasibility and exact domain coverage. Recorded results are compared to fresh output.

Successful finite execution does not by itself prove the complex saddle, topological gluing, or volume identity. Those arguments are in the manuscript. Conversely, a typesetting build is not a proof check. The repository's ``repro/PROOF_INPUTS.md`` identifies the role of each input and the scope of each executable test.

Build the two documentation views after the PDF:

.. code-block:: sh

   python3 tools/build_sphinx.py
   python3 tools/build_book.py
   python3 tools/check_book.py

Sphinx output is in ``docs/sphinx`` and the existing Markdown book remains in ``docs``. Documentation dependencies are pinned in ``repro/requirements-docs.txt``.
