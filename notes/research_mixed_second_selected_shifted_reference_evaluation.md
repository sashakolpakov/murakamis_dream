# Exact polynomial shifts for a bounded reference diagnostic

Research evaluation specification, 6 November 2026. This changes only
the interval arithmetic for the original correlated reference. It uses
the [canceled rational maps](research_mixed_second_selected_canceled_rational_transport.md)
and their saved exact derivatives. No reference or scalar budget is
evaluated by this note. Earlier inconclusive drivers and records remain
unchanged.

## 1. One common dyadic center and exact shifts

Use the prescribed first-type-four auxiliary box
\[
 \xi\in[115337/512000,57677/256000]
     +i[8919/256000,279/8000],\qquad
 a_{18}=001111101111010111,
 \tag{1}
\]
with \(\alpha=1\), considering both \(\beta=0,1\).
As before, obtain a containing complex rectangle \(\mathcal W\)
for \(W=e^{2\pi i\xi}\) at 160 bits. Let \(W_0\) be the
exact midpoint of its two real intervals, and put
\(\mathcal D=\mathcal W-W_0\). Write exactly
\[
                 W_0=(M+iN)/D,\qquad D=2^k,
                    \quad M,N\in\mathbb Z.
 \tag{2}
\]
The stored midpoint dyadics determine the common denominator. This is
an arithmetic center, with no claim that it represents an actual word.

For each integer polynomial \(P(W)=\sum_{j=0}^d p_jW^j\), form
the Gaussian-integer coefficients \(R_j\) of
\[
 D^dP((M+iN+X)/D)=\sum_{j=0}^dR_jX^j.
 \tag{3}
\]
They are computed exactly by Horner's rule: start with \(p_d\),
then multiply the current polynomial by \(M+iN+X\) and add
\(p_{d-e}D^e\) at step \(e=1,\ldots,d\).
Integer multiplication and addition introduce no rounding. Consequently
\[
                 P(W_0+\delta)
                  =\sum_{j=0}^d\frac{R_j}{D^{d-j}}\delta^j.
 \tag{4}
\]
Convert each exact Gaussian-rational coefficient in (4) to an outward
complex ball, then evaluate the polynomial by Horner's rule on
\(\mathcal D\). This contains \(P(W)\) on the whole convex
rectangle \(\mathcal W\). The constant coefficient separately
encloses the exact value \(P(W_0)\).

This procedure avoids subtracting large approximate polynomial terms
at the midpoint. It does not presume that the resulting interval is
narrow or that a denominator is separated from zero.

## 2. Canceled values and derivatives on the full rectangle

Use the exact record's numerator, denominator, and derivative
factorizations for
\[
                    E,A,U,Z,V,B_0,C_0,B_1,C_1.
 \tag{5}
\]
Each distinct integer factor is shifted once by (3). Reuse its full
value and midpoint enclosure in all products. Integer contents, signs,
and factor powers are retained exactly.

For a recorded map \(F=N/D_F\), check that every denominator
factor and the resulting full denominator product exclude zero on
\(\mathcal W\). The direct quotient then encloses \(F\).
Apply the same procedure to the separately canceled exact derivative
\(F'=N_1/D_1\); those coefficients were checked against the
quotient rule in the exact algebra record. After denominator separation,
\[
 \begin{split}
 F(\mathcal W)&\subseteq N(\mathcal W)/D_F(\mathcal W),\\
 F(\mathcal W)&\subseteq F(W_0)+F'(\mathcal W)\mathcal D.
 \end{split}
 \tag{6}
\]
The second inclusion follows by integration along segments in the
convex rectangle. Both expressions use the same \(W_0\).
Intersecting their real and imaginary intervals is therefore a valid
full-rectangle enclosure. An empty intersection is an arithmetic
failure and is reported as inconclusive, never as a word exclusion.
No geometric reference filter is used in (3)--(6).

The shapes in (5) are evaluated independently as rational functions
of the same parameter. Their values and derivatives are not propagated
through widened intermediate transfer boxes. This removes the
particular multiplication of derivative widths encountered in the
preceding centered diagnostic, without asserting a numerical outcome.

## 3. All original denominators, lifts and filters remain

Cancellation does not enlarge the admitted reference set. Before
admitting a reference, retain the regularity conditions in Section 1
of the [original curve theorem](research_mixed_second_selected_reference_curve.md):
all seven shapes, \(W\), the original endpoint quadratic, every
listed \(1-EW,1-E,1-EA,1-UA,1-A\), and the five factors
\(1-PQ,1-QR,1-RT,1-Q,1-R\) for each original transfer must
exclude zero. These tests use the full untruncated shape enclosures.
The remaining original displayed denominators are also nonzero by
the exact identities
\[
 \begin{split}
 A(1-EA)+(1-A)^3&=(1-EA)/U,\\
 Z(1-UZ)+(1-Z)^3&=(1-UZ)/V,\\
 B_\beta(1-VB_\beta)+(1-B_\beta)^{2+\beta}
                       &=(1-VB_\beta)/C_\beta.
 \end{split}
 \tag{7}
\]
Both numerator and denominator on each right side are individually
checked nonzero. The retained-coordinate divisions have checked
denominators \(U(1-AU)\) and \(V(1-ZV)\). These identity-based
checks are the same regularity logic as the preceding reviewed
centered evaluator; they do not divide by a possibly zero canceled
factor. All such checks are recorded.

Only after this transport is complete, decode negative-sign shapes
by \(i\Log X/(2\pi)\), retaining the original lower-half-plane
guards and the same mandatory endpoint, ordinary, pair-sum, and typed
suffix filters. Their code is copied unchanged from the frozen direct
diagnostic. Uncertain comparisons and boundary equalities remain;
both suffix alternatives must be strictly excluded before discarding
their union. Necessary rectangle intersections tighten pointwise
coordinates only, never the polynomial or derivative inputs.

The reference theorem's zero-lift lemma consequently applies to every
admitted point. The proposed stronger height bound for \(z\) remains
open and is not a filter. The exact center, midpoint polynomial values,
and containing rectangles are not independently optimized references.

## 4. Finite cost and the sole proposed run

Across all nine maps and their derivatives, the exact factor record
contains 27 distinct nonconstant integer polynomials. Their largest
degree is 111 and their degree sum is 714. Formula (3) requires at
most
\[
                \sum_P\frac{\deg P(\deg P+1)}2=20962
 \tag{8}
\]
Gaussian-integer multiplications by the common \(M+iN\), plus
integer additions and dyadic shifts. Full interval Horner evaluation
requires at most 714 complex multiplications. Factored products and
their powers add a fixed finite number of outward operations. These
are operation bounds, not elapsed-time promises. Cached polynomial
and rational-map enclosures are reused between the two beta cases.

The new driver reuses only the frozen ball construction, exact endpoint
serialization, interval intersection, geometric filter and dyadic
partition helpers. The original primitive classes, scalar conjugate
functions, old reference implementations, inspect functions and main
programs are disabled. It uses no source root, finite quantum sum,
subdivision, extra box, precision retry or numerical optimizer.

After static review, the permitted diagnostic consists of exactly two
reference cases on (1), at 160 bits. The inherited box is selected and
reconstructed solely from saved complete-cover metadata. An excluded
or inconclusive case is recorded without replacement. No scalar
budget follows automatically, even if a reference is retained.

The result records all exact shifted Gaussian-integer coefficients
(in hexadecimal), their dyadic denominator powers, midpoint data,
full polynomial enclosures, direct and mean-value map enclosures,
derivative and denominator bounds, original regularity checks, decoded
coordinate rectangles, suffix alternatives, reasons, operation counts
and elapsed time. Frozen bindings are checked before repository
imports and after completion. The exact record, the prior failed
drivers/results, the new specification and the new driver are bound.
All sign conclusions concerning the selected source remain open.
