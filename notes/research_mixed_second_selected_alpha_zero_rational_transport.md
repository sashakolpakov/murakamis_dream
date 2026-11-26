# Canceled second-selection maps with a type-three first endpoint

Exact algebra deduction, 6 November 2026. This extends the rational
reference data to first flag \(\alpha=0\), while the second block
still has type four and the third flag is \(\beta=0\) or \(1\).
All calculations take place in \(\mathbb Q(W)\). No parameter,
interval reference, transcendental primitive, root, finite source,
or selected-rate budget is evaluated.

## 1. Original endpoint and ordinary equations

Keep the variables and signs of the
[original reference curve](research_mixed_second_selected_reference_curve.md):
\[
 W=e^{2\pi i\xi},\qquad
 (E,A,U,Z,V,B,C)=
 (e^{-2\pi ie},e^{-2\pi ia},e^{-2\pi iu},
  e^{-2\pi iz},e^{-2\pi iv},e^{-2\pi ib},e^{-2\pi ic}).
 \tag{1}
\]
The actual roles remain \((a,u,z,v,b)=(r_1,s_2,r_2,s_3,r_3)\);
\(c=s_4\) is the next external leg. For the first endpoint
of type three, its original equations give
\[
 \begin{split}
 E&=\frac{(1+W)^2}{5W^2-2W+1},\\
 A&=\frac{1-(1-EW)/W}{E},\\
 U&=\frac{1-EA}{A(1-EA)+(1-A)^2}.
 \end{split}
 \tag{2}
\]
The absence of the factor \(1-E\) in the second line, and
the square in the third, are the changes from first type four.
The following ordinary block still has its own cubic factorial:
\[
 Z=\frac{1-A(1-U)^3/(1-AU)}{U},\qquad
 V=\frac{1-UZ}{Z(1-UZ)+(1-Z)^3}.
 \tag{3}
\]
For \(p=2+\beta\), its next transfer is
\[
 B_\beta=\frac{1-Z(1-V)^p/(1-ZV)}{V},\qquad
 C_\beta=\frac{1-VB_\beta}
                  {B_\beta(1-VB_\beta)+(1-B_\beta)^p}.
 \tag{4}
\]
The first endpoint type does not change either exponent in (3).
All original chirps and logarithmic lifts enter through the source
identities underlying (2)--(4); a later converse still requires
the reference theorem's regularity and zero-lift conditions.

## 2. Fully canceled factorizations

Define
\[
 \begin{split}
 D_2&=5W^2-2W+1,&
 P_2&=7W^2-6W+3,\\
 P_3&=17W^3-7W^2+7W-1,&
 R_2&=2W^2-W+1,\\
 P_5&=169W^5-279W^4+314W^3-174W^2+77W-11,\\
 P_6&=407W^6-512W^5+575W^4-344W^3+165W^2-40W+5.
 \end{split}
 \tag{5}
\]
The exact reduced maps are
\[
 \begin{split}
 E&=(1+W)^2/D_2,\\
 A&=(3W-1)R_2/\{W(1+W)^2\},\\
 U&=(1-W)(1+W)^4/(P_2P_3),\\
 Z&=P_5P_6/\{(1+W)^6P_2P_3\},\\
 V&=-\frac{(3W-1)(1+W)^{16}R_2}{D_9D_{10}},\\
 B_0&=\frac{N_{30}}{(1+W)^{22}D_8},\qquad
 C_0=\frac{(1+W)^{38}P_5P_6}{D_{24}D_{25}},\\
 B_1&=\frac{N_{20}N_{21}}{(1+W)^{22}D_9D_{10}},\qquad
 C_1=-\frac{(1+W)^{60}P_5P_6}{D_{35}D_{36}}.
 \end{split}
 \tag{6}
\]
Here subscripts identify degrees, not vertex indices. The higher-degree
polynomials are the unique factors of the indicated degrees in the
corresponding numerator or denominator of the
[exact alpha-zero record](../repro/results/research-mixed-second-selected-alpha-zero-rational-transport-exact.json).
Its complete descending integer coefficient lists define them without
rounding. The \(D_9,D_{10}\) factors in \(V\) and \(B_1\)
are identical. For convenience,
\[
 D_8=2861W^8-5976W^7+8396W^6-7336W^5+4974W^4
                         -2280W^3+780W^2-152W+13.
 \tag{7}
\]
All signs and integer contents are retained in (6).
These symbols refer only to the present alpha-zero record; they do
not identify similarly numbered factors in the alpha-one record.

The resulting degrees are:

| Shape | Numerator / denominator | Canceled derivative numerator / denominator |
|---|---:|---:|
| \(E\) | \(2/2\) | \(2/4\) |
| \(A\) | \(3/3\) | \(3/5\) |
| \(U\) | \(5/5\) | \(8/10\) |
| \(Z\) | \(11/11\) | \(15/17\) |
| \(V\) | \(19/19\) | \(36/38\) |
| \(B_0\) | \(30/30\) | \(37/39\) |
| \(C_0\) | \(49/49\) | \(96/98\) |
| \(B_1\) | \(41/41\) | \(59/61\) |
| \(C_1\) | \(71/71\) | \(140/142\) |

## 3. Exact checks and source bindings

The [new derivation script](../experiments/derive_mixed_second_selected_alpha_zero_rational_transport.py)
verifies the hash of the frozen alpha-one algebra implementation
before loading its Rational, factorization and derivative routines.
It never calls the old main program or its frozen-map reader.
Every operation removes the exact polynomial gcd; no parameter is
substituted for \(W\).

Besides the solved transfer cross products, the record checks the
original equations
\[
 \begin{gathered}
 (1+W)^2(1-EW)=E(1-W)^3,\qquad W(1-EA)=1-EW,\\
 (1-EA)(1-UA)=U(1-A)^2,\\
 (1-AU)(1-UZ)=A(1-U)^3,\qquad
 (1-UZ)(1-VZ)=V(1-Z)^3,\\
 (1-ZV)(1-VB_\beta)=Z(1-V)^{2+\beta},\qquad
 (1-VB_\beta)(1-C_\beta B_\beta)
                         =C_\beta(1-B_\beta)^{2+\beta}.
 \end{gathered}
 \tag{8}
\]
All are zero polynomial cross-product checks. The initial \(A,U\)
are also checked against the independently written alpha-zero formulas
in (4) of [rational critical transport](research_mixed_rational_critical_transport.md).
There are 19 recorded identity checks. For each of the nine maps,
the canceled derivative is independently cross-multiplied against
the quotient rule, and all four numerator/denominator factor lists
for the map and derivative are multiplied back to their exact
polynomials.

The single algebra-only calculation completed in approximately
0.409 seconds. It used 428 rational normalizations, removed
83 nonconstant polynomial gcds, and reached precancellation degree
208. Across the map and derivative factorizations there are 28 distinct
nonconstant integer polynomials, with maximum degree 81 and degree
sum 522. Their exact midpoint-shift multiplication bound is
\[
             \sum_P\frac{\deg P(\deg P+1)}2=10954.
 \tag{9}
\]
These counts describe exact algebra and a possible later evaluator;
no interval evaluation is implied.

The frozen script SHA-256 is
40c8782a72f1e6fef56239447c4da69bbbb1a59b36648dc756e9940b82fa5272.
The exact result SHA-256 is
9a9e3018aeced570e4cf0f9bba32d703f3c08e39a0282a09e2532d59b705df5e.
Its four before/after bindings include the new script itself and:

| Input | SHA-256 |
|---|---|
| Original reference-curve proof | 4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5 |
| Original rational-transport proof | 0cba78ed20d7e98d65414b61a96412a8ee6f3e43b766d7d10f9900ea36a96635 |
| Reused exact rational implementation | 71d5fd6d67229b69aaea53cc9e1c540ceb01a68e7fb0d126d2f8d63e8651470a |

The original alpha-one script, proof and result were not changed.
Its exact result still has hash
7db105fdc67e0331bebc69d29d33c11cfaff6432f0366344932c96966887bc43.

## 4. What a later reference evaluation must retain

The first-three endpoint has its own original parameter rectangle
\[
                \xi\in(.218,.242)+i(.049,.077).
 \tag{10}
\]
Its private and attached coordinate ranges are those of the type-three
row of the original endpoint theorem, not the type-four row used by
the alpha-one provider. The second block is still ordinary type four,
and both final choices of \(\beta\) in (4) are required.
The original reference theorem specifies the corresponding typed
suffix alternatives and pair sums.

A later interval evaluator may use the exact-shift method on these
new coefficients, but must bind this record and its new factor counts.
It must restore every original endpoint and transfer denominator,
the original logarithmic branch conditions, and the necessary reference
filters before admitting a point. Algebraic cancellation does not
justify enlarging the geometric reference set. There is no alpha-zero
reference cover or selected scalar-sign conclusion in this record.
