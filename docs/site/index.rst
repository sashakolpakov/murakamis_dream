Long-twist volume limits
========================

This is the reading companion to the detailed TeX manuscript **Long-twist volume limits for a compositional class of arborescent knots**. The proof keeps the finite invariant, its one-cut normalization, the ordered ideal-cell geometry, and the complete filling period in the same argument.

:download:`Read the manuscript (PDF) <../../manuscript/build/main.pdf>`

The main theorem concerns a specified grammar of completed four-port tangles. It allows arbitrary finite products and turns, and repeated attachment of one leaf to a completed child. Both children of the cylindrical closing product are completed. Every fixed expression admits a knot pairing; after all auxiliary crossing-circle fillings, independently sufficiently long fixed signed twists satisfy the volume limit through all levels.

.. math::

   \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K(\mathbf p)\rangle_N|
   =\Vol(S^3\setminus K(\mathbf p)).

The knot cusp stays unfilled. The threshold depends on the fixed expression and half-twist pattern, and no claim is made for every arborescent knot.

.. toctree::
   :maxdepth: 2
   :caption: Reading and verification

   mathematics
   manuscript
   reproducibility
   scope
   research

The `Markdown research book <../index.html>`_ provides the longer source-note archive. The `repository <https://github.com/sashakolpakov/murakamis_dream>`_ contains the manuscript, native TikZ figures, exact certificate data, and verification scripts.

The later :doc:`research` companion proves a weighted-tree theorem with arbitrary finite branching and unary chains, while retaining the manuscript's stated scope.
