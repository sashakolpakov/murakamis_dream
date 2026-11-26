# The initial four/four pair on the real interval from one half to seven tenths

Private written proof, 10 November 2026. The complete first four/four
pair is controlled on the real interval from one half to seven tenths.
The proof starts with the individual profile bounds established by
the half-face height connection. The original cap and conditional
polynomial, their physical end rows, both Fourier terms, and all
contour corrections are retained. No whole-period conclusion is claimed.

## 1. The finite functions and the required starting bounds

Keep an actual positive three/four word beginning with four and four,
of length at least three, and its original geometric reference.
Write its first two retained coordinates as \(a_0+ic\) and
\(b_0+id\), with the ranges in
[the half-face height connection](research_mixed_initial44_half_face_height_connections.md).
The targets in this note are
\[
 a=x,\quad \frac12\le x\le\frac7{10},\qquad
 b=z+id,\quad z\in[11/50,9/20].
 \tag{1}
\]
The original finite factors are
\[
\begin{split}
 q_N&=e^{-2\pi i/N},\quad P_j=(q_N;q_N)_j,\\
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       H_N(w,q_N^{-i})\frac{(q_NX;q_N)_i}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^3},\\
 K_{\epsilon,N}(w;a,b)&=
       U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-\epsilon N},
       \qquad \epsilon\in\{0,1\},
\end{split}
 \tag{2}
\]
where \(X=e^{-2\pi ia}\) and \(Y=e^{-2\pi ib}\).
Both first Fourier alternatives remain in \(d_N\). The outgoing
allocation is \(|d_N(Y)|^{1/2}\).

Let \(\Lambda(z)\) be the original joint geometric supporting plane.
Set
\[
 \delta_R=\frac{(9/20-a_0)^2}{2500000},\qquad
 \gamma=\delta_R/2>0.
 \tag{3}
\]
The strict reference bound \(a_0<.350\) supplies a uniform positive
lower bound for \(\gamma\).

The five cap profiles mean the actual main contour at private height
\(h_e\), the two real cuts at \(.27,.49\), and the two horizontal
sampling corrections at heights \(-.055,.04\), with their respective
penalties \(.11\pi,.08\pi\). Write their rates as \(A_j(a)\).
They use the full endpoint coefficient \(H_N\).
Let \(\Theta(a,b)\) be the original conditional critical action, and
let \(E(t;a,b)\) be the original physical-row rate.

The starting bounds, all at \(a=1/2\), are the following.

1. Every \(A_j\), paired with \(\Re\Theta\) or with any physical
   rate for \(t\in[0,2/25]\cup[1/2,1]\), and with the outgoing
   halfweight rate \(-\Re g(b)/2\), is at most
   \(\Lambda(z)-\gamma\).
2. At the same private real coordinate, the upper sampling correction
   is below the main cap profile by more than \(1/50\).
3. The constant \(3/5\), paired with the critical action or those
   physical-row rates, has the bound in item 1 with an additional
   reserve \(29/200\).

These are profile bounds before summation. A bound for the absolute
value of a signed cap alone would not be a substitute for them.
Corollary 2 of the half-face height connection proves items 1 and 3,
with the stronger main reserve \(\delta_R\). Its equation (27a)
proves item 2 pointwise at the same private real coordinate.
The present \(\gamma=\delta_R/2\) leaves a common reserve for the
finite source estimates. Thus all three are established starting
bounds for this same coupled reference.

**Theorem.** For every
\(\tau>0\), both level parities and every real ordinary color
\(w\in[-2,2]\),
\[
 |K_{\epsilon,N}(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
       \exp N\{\Lambda(z)-\gamma+\tau\}
 \qquad(\epsilon=0,1)
 \tag{4}
\]
uniformly on (1). Fixed small ordinary-color neighborhoods and
fixed derivatives on smaller neighborhoods have the same conclusion
with a separately reserved arbitrary allowance.

## 2. The critical exponential and the complete cap

At height zero the incoming radius is exactly one. The difference
of squared moduli in equations (11)--(12) of
[the cap transport proof](research_mixed_first_four_cap_lower_right_horizontal.md)
still has its strict positive lower bound at this radius.
Consequently each point of its retained cap contour decreases in
rate as \(x\) increases from one half to seven tenths. This includes
both horizontal sampling corrections and all connecting sides.
The global numerator factorial retains its period multiplier when
\(\Re(a+e)\) crosses one.

The omitted compact lower cap rows also decrease from their values
at one half. The compact upper rows decrease in their private index
to the current cut \(.49\). Their respective proofs in Sections 3--4
of that source allow radius one: the lower numerator comparison is
unchanged, and the upper index derivative is bounded above by
\(-6/5+\log2<0\) before one half and by \(-\log2\) afterwards.
The genuine cap ends have the unchanged ceiling \(3/5\) on the
whole closed incoming disk.

The original action theorem
[across the incoming unit circle](research_mixed_four_conditional_positive_incoming_action.md)
gives
\[
                  \partial_x\Re\Theta(a,b)<0.
 \tag{5}
\]
It applies throughout (1), with the same cubic root and logarithmic
lift. The starting bounds therefore pay the product of the
whole cap with the conditional critical exponential. This alone
does not yet bound \(C_{1,N}\).

## 3. The physical end blocks

For a retained cap point \(e=u+i\eta\), put
\[
 D=|1-X|,\quad N_e=|1-Xe^{-2\pi ie}|,\quad
 N_t=|1-Xe^{-2\pi it}|\le2.
\]
The derivative of its joint rate with an ordinary real row is
\[
                         \log(N_eN_t/D^2).
 \tag{6}
\]
For \(\eta\le0\), equations (14)--(15) of
[the positive-height horizontal proof](research_mixed_selected44_upper_right_complete_pair.md)
give \(2N_e<D^2\) at radius one. Their strict inequalities include
this endpoint; their proof does not require a positive incoming
height. Thus the main cap, lower sampling correction, real cuts,
lower weighted sides and unweighted joins decrease jointly with
every ordinary physical row.

The upper horizontal correction has a decreasing bare cap rate.
The possible increase of any ordinary physical row is less than
\[
 \int_0^{1/5}\log\sec(\pi v)\,dv<\frac3{175}<\frac1{50},
 \tag{7}
\]
by the written tangent bound in equation (16) of that same source.
The extra starting reserve in item 2 pays this increase.

Each upper weighted cap side reduces to its real cut at the current
\(x\). Indeed the exact canonical marginal and its continued
numerator period term, as in equation (17) of the cited proof,
give
\[
 \partial_\eta(\widehat\Psi(e,a)-2\pi\eta)<0
 \qquad(\eta\ge0).
 \tag{8}
\]
Before the numerator wall the negative derivative is bounded below
by \(-2\pi x>-2\pi\); after the wall it is bounded below by
\(\pi(u-x-3/2)\ge-193\pi/100>-2\pi\).
The argument bounds remain valid when the incoming height is zero.
One integrates their continuous rate across the wall, keeping the
exact period multiplier.

For omitted compact cap rows with \(2/25\le e\le.27\), the
trigonometric polynomial proof in Section 3 of
[the complete physical-row comparison](research_mixed_initial44_lower_right_physical_rows.md)
applies with \(4r/(1+r)^2=1\). It proves \(2N_e<D^2\), hence the
same joint decrease. Below \(2/25\), the cap row increases in its
private real index to the current \(2/25\) row. Above \(.49\), it
decreases to the current \(.49\) row. These comparisons retain the
original coherent coefficient; they do not replace its internal
Newton sum by a sum of moduli.

Finally, the constant true-end ceiling \(3/5\) has no \(x\)
derivative. Its joint increase is bounded by (7), or by the weaker
\[
                  \frac15\log2<\frac7{50}<\frac{29}{200}.
 \tag{9}
\]
Thus item 3 pays both genuine cap ends. All physical rows
and both limiting real cuts of the conditional contour now satisfy
the geometric upper bound.

## 4. The complete conditional sum and finite conclusion

Proposition 2 of
[the complete positive-height horizontal proof](research_mixed_selected44_upper_right_complete_pair.md)
applies at height zero. It bounds the entire conditional polynomial
by the maximum of
\[
 \Re\Theta(a,b),\qquad
 \sup_{t\in[0,2/25]\cup[1/2,1]}E(t;a,b).
 \tag{10}
\]
It includes both unweighted connecting sides, all four weighted
sides, both horizontal sampling corrections and all physical rows.
Sections 2--3 pay each of (10) after multiplication by the complete
cap and its outgoing allocation.

On (1), \(\Re g(a)\ge0\), whereas the height is zero. The original
absolute bound for \(d_N\) therefore has exponential rate zero.
Also \(|X^{-\epsilon N}|=1\). This treats both literal Fourier
terms without identifying them as finite functions.

All sources used above are zero safe and uniform through the two
level parities. Half-grid cut displacements cost
\(O(\log N/N)\) in the rate, and the finite row counts and original
residue measures contribute only polynomial factors. Reserving one
total tolerance proves (4).
The exact dependence on \(w\) is polynomial of degree less than
\(N\); the existing Chebyshev continuation and Cauchy estimates give
the stated ordinary-color neighborhoods and derivatives.

The theorem bounds this real horizontal segment only. It does
not cover the real arc from \(7/10\) to the periodic endpoint
neighborhood, nor any further coordinate of the original period.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_selected44_upper_right_complete_pair.md | aee07a0914def14645fe344173883de690a2e0c4591ee65ce7873ce6627515d7 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The proof uses written inequalities and the original finite source
identities. No mathematical numerical evaluation, saved-value
arithmetic, test, import, compilation, or frozen-source edit was used.
The half-face source and this continuation require their separate full
reviews before adoption.
