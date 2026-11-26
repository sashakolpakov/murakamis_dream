# The independent Fourier endpoint disk is too large for the old source domain

The fixed [saved-domain test](research_mixed_fourier_boundary_saved_domain_protocol.md)
disproves
\[
                         \beta_K(D_4)\subset K_3.
\]
Here \(D_4\) is the entire independent type-four input disk, and
\[
 K_3=\{|b-(.35-.01i)|\le.083\}
      \cap\{-.072\le\Im b\le.068,\quad \Re b-3\Im b\le.608\}.
\]
This is a limitation of the proposed source-domain substitution.
It does not exclude the actual last coordinate of a geometric word.

The single execution processed all 512 saved boundary arcs and all
three prescribed half-plane tests on each arc. Of the 1536 tests,
1378 establish containment of their whole saved rectangle, 118
establish violation throughout their whole boundary arc, and 40
are inconclusive. The violations consist of 81 lower-imaginary
failures and 37 oblique failures. There is no upper-imaginary
violation. All 20 original source bindings matched before and
afterward. No analytic function was evaluated.

Two exact witnesses suffice. Parametrize the original boundary by
\[
 q(\theta)=.30-.052i+.064e^{2\pi i\theta}.
\]
For every \(\theta\in[107/512,108/512]\), the saved enclosure gives
\[
 \Im\beta_K(q(\theta))+\frac9{125}
       \le-\frac{383031797}{1073741824000}<0.
\]
For every \(\theta\in[153/512,154/512]\), it gives
\[
 \frac{76}{125}
 -\Re\beta_K(q(\theta))+3\Im\beta_K(q(\theta))
       \le-\frac{21287719}{33554432000}<0.
\]
These are upper bounds for the relevant margins, not negative lower
bounds from wide rectangles. They therefore certify actual violations.
Both retain the original uncertainty in the algebraic parameter \(K\).

The output is
[the saved-domain result](../repro/results/research-mixed-fourier-boundary-k3-saved-domain.json),
SHA256
04e00eb7d04878b1f4d8092a7271786c8363a83a1efebf1a9e1284148be8c219.
The frozen checker hash is
597178f93ea3e0ee8dce0aaea1a7a2c5c16cac15b91aac284c325360e8814677,
and the frozen protocol hash is
83b4204f10f723f310633ce9ce19aaae48f07cde1458661914c0ec9c9ccbb4ac.
The output was created exclusively and has not been rerun or replaced.

The already proved inclusion in the disk of radius \(0.082\) remains
valid. The failed implication is that this disk inclusion also enforces
the three additional linear constraints. A right-boundary proof must
retain the correlation between the last ordinary vertex and
\(\beta_K\), or establish source estimates on an appropriate different
domain. Increasing the accuracy of this same independent-disk test
cannot establish the false inclusion.
