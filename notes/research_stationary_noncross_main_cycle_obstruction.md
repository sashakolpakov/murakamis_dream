# Every positive-value non-CROSS sharp maximum has an elementary odd MAIN cycle

31 October 2026. **Internally reviewed source/combinatorial theorem.** Root and geometry completed full independent analytical and original-source scope reviews, PASS. This uses the reviewed
full-fiber activation and stationary classification. It does not construct
a representation or prove an absolute exponential phase gap. No cap collar
is used.

## 1. Exact hypotheses inherited from the original maximum

Work with the actual certified simple-white marked plat and its original
ordinary face targets \(1\), protected pair \(u,v\), and triangle pairing across
MATCHING edges. Every MAIN edge has two incident triangles belonging to
different ports. Let \(q\) and the common positive ordinary weights \(L\) be the
data supplied by [finite-multiplier and stationary classification](research_full_fiber_sharp_stationary_classification.md).
In particular every ordinary incidence is positive, the supported
port/ordinary-face graph is connected, and each port is one of:

* strict CROSS at \(\delta=0\), whose incidence character is constant;
* strict Green, with one negative half and overloaded ordinary middle \(o\),
  \(q_{e,o}>1/2\), and

  \[
   L_o-L_p=\frac{L_x+L_y}{\sin^2(\pi\delta)},\qquad 0<\delta<\tfrac12;
   \tag{1}
  \]

* a residual cap, with the two protected faces as one outer and the
  parent middle; its two ordinary incidences are outer \(a\) and overloaded
  middle \(o\), with

  \[
   q_{e,a}=\nu,\quad q_{e,o}=1-\nu,\quad 0<\nu<\tfrac12,\qquad L_o=L_a.
   \tag{2}
  \]

For a Green, the literal source character on its negative half is \(1\) at
its overloaded middle and \(0\) at its outers; its other half has character \(0\).
For a cap, the two supported ordinary characters differ by \(1\). This is the
exact alternating monomer character, up to a constant row gauge. These
statements are unchanged by original RIGHT reflection or outer exchange.
No globally coherent signs are assumed.

Here is a direct source derivation of the character table. In the
[exact full-interval source](research_original_one_sided_four_state_transfer.md),
write \(\alpha_r=c_r-\sigma\) and retain every unused prefix and suffix
factor. On a strict LEFT straddling window the prefix is positive and
the lower-half suffix has sign \((-1)^{M-j}\). The
[positive word expansion](research_positive_eta_word_transfer.md) makes
the coefficients of \(K_{i,j}\) nonnegative for every sufficiently large
level at a fixed strict spectrum. Thus, after retaining the common raw
sign and omitted-half scalar, the varying sign is \((-1)^j\). The
original middle monomial is \(c^{d-j}\), so this is exactly the character
\(c\mapsto-c\), up to a degree-independent row sign. The common scalar
is not divided out; at a sampled zero the source is zero. At the complete
endpoint the same unused factors and tail coefficients are nonnegative,
up to the common raw sign, giving the constant CROSS character. Literal
row reflection gives RIGHT. The [flat-cap formula](research_flat_cap_no_local_exponential_angular_gap.md)
gives the remaining character directly, including its raw sign at both
parities. No geometric collar is needed for this table.

A supported four-cycle \(e-f-e'-g-e\) has sign sum

\[
 \varepsilon_{e,f}+\varepsilon_{e',f}
 +\varepsilon_{e',g}+\varepsilon_{e,g}\quad\text{in }\mathbf F_2.
 \tag{3}
\]

It is odd precisely when the two ports' edge differences on \(f,g\) differ.
The test retains actual incidences and is invariant under all row gauges
and common face signs.

## 2. Every strict Green gives an odd MAIN four-cycle

At a strict Green choose an ordinary outer \(a\). Such an outer exists:
the two protected faces form a MAIN pair, whereas the two outers form a
MATCHING pair. Write \(o\) for the overloaded middle of the negative half.
Both endpoints of the MAIN edge \(oa\) are ordinary. Equation (1) gives

\[
 L_o>L_p+L_x+L_y\ge L_a.\tag{4}
\]

Thus \(L_o>L_a\) also when the other outer or parent is protected. The
original edge \(oa\) has a second triangle at a different port \(e'\).
The chosen Green has edge-character difference \(1\).

We show that the second triangle has edge-character difference \(0\).
A positive Green half or a CROSS half has that difference \(0\). If it is a
negative Green half with difference \(1\), its overloaded middle must be \(o\)
or \(a\): a MAIN edge joins a port middle to an outer. The two possibilities
are impossible:

* overload at \(o\) would put two distinct loads greater than \(1/2\) on the same
  original demand-one face;
* overload at \(a\) would require \(L_a>L_o\) by its own version of (4).

If the second triangle belongs to a residual cap and has both ordinary
endpoints \(o,a\), it is the cap's ordinary output edge. Equation (2) would
require \(L_o=L_a\), also impossible. These exhaust the classified ports.
Thus the actual radial four-cycle \(e-o-e'-a-e\) is odd.

The conclusion needs only (1), the exact sign table, original MAIN typing
and face demands. It does not use a Green collar or representation volume.

## 3. Residual caps also give an odd MAIN four-cycle at positive value

At a cap \(e\) let \(o,a\) be its ordinary output pair. They have equal positive
weights and opposite incidence characters. Their MAIN edge has its other
triangle at \(e'\). A noncap triangle cannot have opposite characters on this
edge: a negative Green would require one of the equal weights to exceed
the other strictly, while positive and CROSS halves have equal characters.
Therefore the cycle is odd unless \(e'\) is itself a cap on the same pair.

The latter case is incompatible with a positive-value maximum. Both caps
have all their supply on the same two ordinary faces. The second cap
cannot overload \(o\), since \(e\) already supplies more than \(1/2\) there; it must
overload \(a\). Write the two parameters as \(\nu\) and \(\nu'\). Face demands imply

\[
 1-\nu+\nu'\le1,\qquad \nu+1-\nu'\le1,
\]

so \(\nu'=\nu\) and both demands are saturated by these two rows. Ordinary
incidence positivity excludes every other port from both faces. The two
cap ports have no other ordinary incidence. They and the two faces form
a whole connected component of the supported graph. Connectedness then
forces the entire source to consist of these two caps, whose sharp
entropy is zero. This contradicts the positive-value hypothesis, in
particular a global maximum at or above \(\Phi_D>0\).

There is an independent literal sphere check of the exceptional geometry.
After locally naming the protected pair \(u,v\), the first cap triangles are
\((u,v,a)\) and \((u,o,a)\), paired across \(ua\). If the other triangle on \(oa\) is
another cap output, its protected vertex must be \(v\). Its input must then be
\((u,v,o)\): choosing ordinary outer \(a\) would repeat the first input triangle.
The four triangles are exactly the boundary of a tetrahedron on \(u,v,o,a\).
Every edge is already incident to two of them, so connectedness of the
triangulated sphere leaves no other triangle. This is not a claim that
the tetrahedral source cannot exist; its all-cap action is simply zero.

Thus every residual cap at the positive-value data in §1 has its own
explicit odd MAIN four-cycle as well.

## 4. Consequence and exact remaining limitation

At every unrestricted global maximum, or competing strict-NC maximum
of value at least \(\Phi_D\) under the stationary theorem's hypotheses, each
non-CROSS port has an elementary odd supported four-cycle. In particular
there is no common solution

\[
 \varepsilon_{e,f}=\gamma_f+\kappa_e
\]

unless every port is complete CROSS. In the restricted non-CROSS problem,
this statement requires at least one middle load strictly greater than
\(1/2\); it makes no assertion about a seam-only constrained maximum.
A phase-coherent maximum therefore
belongs entirely to the original complete endpoint problem. Its value is
at most \(\Phi_D\), and the endpoint unique-max theorem identifies equality
when that comparison is used. A competing non-CROSS maximum of high value
is necessarily phase-inconsistent.

An odd cycle alone is NOT an absolute upper bound for the oscillatory
source. On regular windows the reviewed cycle-packing theorem subtracts
an explicit local phase loss from a positive envelope; comparing that
result to \(\Phi_D\) remains necessary. Residual flat caps do not automatically
satisfy a regular-window exponential angular gap. The [exact flat-cap calculation](research_flat_cap_no_local_exponential_angular_gap.md) exhibits this limitation. No full invariant or volume theorem is inferred.

Dependencies are the [full-fiber boundary reduction](research_full_fiber_sharp_boundary_activation.md),
[stationary classification](research_full_fiber_sharp_stationary_classification.md),
[exact source expansion](research_original_one_sided_four_state_transfer.md), and
[original MAIN/MATCHING dictionary](general_augmented_plat_matching_geometry.md).
The [flat-cap companion](research_flat_cap_no_local_exponential_angular_gap.md) retains its exact raw coefficient and phase.
Root proposed the general Green argument. Root and geometry reviewed this complete written proof; geometry and cluster also independently checked the local original-edge cases. These are internal analytical reviews, not external peer review. No numerical audit is needed or claimed.
