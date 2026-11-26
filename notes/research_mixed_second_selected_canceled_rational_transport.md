# Canceled rational maps for the second-selection reference

Exact algebra record, 6 November 2026. All calculations below take
place in \(\mathbb Q(W)\). No parameter value, interval reference,
primitive, root, finite source, or scalar budget is evaluated.

## 1. Original maps and exact cancellation

Use the [original reference curve](research_mixed_second_selected_reference_curve.md)
with \(\alpha=1\), retaining its signs and coordinate meanings:
\[
 (E,A,U,Z,V,B,C)=(e^{-2\pi ie},e^{-2\pi ia},e^{-2\pi iu},
 e^{-2\pi iz},e^{-2\pi iv},e^{-2\pi ib},e^{-2\pi ic}),
 \qquad W=e^{2\pi i\xi}.
 \tag{1}
\]
The exact initial formulas are
\[
 \begin{split}
 E&=(1+W)^2/(5W^2-2W+1),\\
 A&=\{1-(1-EW)(1-E)/W\}/E,\\
 U&=(1-EA)/\{A(1-EA)+(1-A)^3\},\\
 Z&=\{1-A(1-U)^3/(1-AU)\}/U,\\
 V&=(1-UZ)/\{Z(1-UZ)+(1-Z)^3\}.
 \end{split}
 \tag{2}
\]
For \(p=2+\beta\), the remaining maps are
\[
 B_\beta=\{1-Z(1-V)^p/(1-ZV)\}/V,
 \qquad
 C_\beta=(1-VB_\beta)/
       \{B_\beta(1-VB_\beta)+(1-B_\beta)^p\}.
 \tag{3}
\]
The [exact derivation script](../experiments/derive_mixed_second_selected_rational_transport.py)
represents each rational function by coprime integer polynomials,
normalizing the denominator's leading coefficient to be positive.
Every addition, multiplication, division, and power removes the exact
polynomial gcd. The resulting initial \(E,A,U,Z\) agree exactly
with the frozen factored maps `e,z,s,b` in the own-four provider.

## 2. Explicit factor structure

Define the repeated low-degree factors
\[
 \begin{split}
 P_4={}&29W^4-36W^3+38W^2-20W+5,\\
 P_5={}&167W^5-289W^4+294W^3-194W^2+67W-13,\\
 P_6={}&121W^6-191W^5+290W^4-222W^3+141W^2-51W+8,\\
 P_7={}&793W^7-1375W^6+2097W^5-1839W^4
                +1283W^3-597W^2+179W-29,\\
 Q_7={}&985W^7-2449W^6+3885W^5-4085W^4
                +2923W^3-1523W^2+463W-71.
 \end{split}
 \tag{4}
\]
The canceled maps factor over \(\mathbb Z[W]\) as
\[
 \begin{split}
 V&=\frac{(W+1)^{22}P_4}{D_{26}},\\
 B_0&=\frac{N_{20}N_{21}}{(W+1)^{30}P_5P_6},\\
 C_0&=-\frac{(3W-1)(W+1)^{52}P_7Q_7}{D_{33}D_{34}},\\
 B_1&=\frac{N_{56}}{(W+1)^{30}D_{26}},\\
 C_1&=\frac{(3W-1)(W+1)^{82}P_7Q_7}{D_{48}D_{49}}.
 \end{split}
 \tag{5}
\]
Each subscript is the polynomial degree. The same \(D_{26}\)
occurs in \(V\) and \(B_1\). All displayed factors of degree
greater than one are irreducible over \(\mathbb Q\) in the saved
exact factorization. Their full descending integer coefficient lists
are given without rounding in the
[exact rational record](../repro/results/research-mixed-second-selected-rational-transport-exact.json),
under `maps`, the corresponding shape, and `numerator` or
`denominator`. The factors of each indicated degree are unique in
that entry, so this convention identifies every polynomial in (5).

The resulting degrees are:

| Shape | Numerator degree | Denominator degree | Canceled derivative degrees |
|---|---:|---:|---:|
| \(V\) | 26 | 26 | 50 / 52 |
| \(B_0\) | 41 | 41 | 51 / 53 |
| \(C_0\) | 67 | 67 | 132 / 134 |
| \(B_1\) | 56 | 56 | 81 / 83 |
| \(C_1\) | 97 | 97 | 192 / 194 |

The record also includes full coefficients and exact factorizations
of every canceled derivative. For example
\(V'=-4(W+1)^{21}R_{29}/D_{26}^2\), with the derivative numerator's
integer content and \(R_{29}\) specified in that record. Retaining
the recorded content is necessary when implementing the factorization.

## 3. Identity checks and computational cost

The saved calculation checks the four initial-map identities against
the frozen provider, and the six original transfer identities
\[
 \begin{split}
 ZU(1-AU)&=(1-AU)-A(1-U)^3,\\
 V\{Z(1-UZ)+(1-Z)^3\}&=1-UZ,\\
 B_\beta V(1-ZV)&=(1-ZV)-Z(1-V)^{2+\beta},\\
 C_\beta\{B_\beta(1-VB_\beta)+(1-B_\beta)^{2+\beta}\}
                      &=1-VB_\beta,\qquad\beta=0,1.
 \end{split}
 \tag{6}
\]
Each equality is checked by a zero integer-polynomial cross product.
Every factor list is multiplied back to its polynomial, and every
saved derivative is checked against the cross-multiplied quotient
rule. Thus the saved coefficients are tied to (2)--(3), rather than
fitted to sample values.

The calculation took approximately 0.266 seconds in the current
workspace, including factorization and derivative checks. It performed
238 rational normalizations and removed 56 nonconstant polynomial gcds;
the largest intermediate numerator or denominator degree was 284.
All six frozen input bindings were rechecked after completion.

The symbolic script SHA256 is
`71d5fd6d67229b69aaea53cc9e1c540ceb01a68e7fb0d126d2f8d63e8651470a`.
The exact result SHA256 is
`7db105fdc67e0331bebc69d29d33c11cfaff6432f0366344932c96966887bc43`.
Both earlier inconclusive reference diagnostics remain unchanged.

## 4. Scope of a later interval evaluator

Equations (5) give a new arithmetic route to the same reference
curve. They do not yet establish denominator separation or useful
interval widths on the inherited auxiliary box. A later evaluator
must still retain every original regularity condition and necessary
reference filter, including the zero-lift and suffix conditions.
Cancellation of a polynomial factor does not authorize admitting a
point where an original critical equation is undefined.

In particular a direct Horner evaluation of a high-degree polynomial
may still lose accuracy through cancellation. One exact possible
evaluation method is to shift each integer polynomial to the common
dyadic complex midpoint \(W_0\):
\[
 P(W_0+\delta)=\sum_{j=0}^{d}q_j\delta^j,
 \qquad q_j=\sum_{k=j}^{d}p_k\binom{k}{j}W_0^{k-j}.
 \tag{7}
\]
If \(W_0\) has dyadic rational real and imaginary parts, all
\(q_j\) are exact Gaussian rationals. Conversion of these exact
coefficients to outward balls followed by interval Horner evaluation
is rigorous; the same identity applies to derivative polynomials.
This is an algebraic option for a separately reviewed evaluator, not
an evaluated interval claim. No new reference or flow calculation is
performed by the present record.
