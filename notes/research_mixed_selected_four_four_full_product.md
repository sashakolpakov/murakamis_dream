# The complete selected first-four/next-four weighted finite product

Research theorem, 6 November 2026.

All five independent boundary comparisons in the selected
first-four/next-four finite reduction are now proved. The whole
type-four cap and its complete neighboring type-four kernel have
a strict exponential gap on the full retained plateau, with the
original outgoing halfweight and affine term. This is a local
two-factor source theorem, not a whole-knot asymptotic.

## 1. Literal weighted product and conclusion

Fix the original coupled critical reference of a mixed open word
with \(m\ge3\), first two types four, and every later type three
or four. Keep the original branches and additive calibration of
[the finite reduction](research_mixed_selected_four_four_finite_reduction.md).
Set
\[
 \begin{gathered}
 H=1/100,\qquad z=y+iH,\qquad b=v+ih_b,\qquad
 y,v\in P=[11/50,9/20],\\
 \mathcal F_4=\Psi+Q_4-g(z)-\tfrac12g(b),\qquad
 M=\Re\mathcal F_4(e_*,s_*;z_*,b_*),\\
 p=g'(s_*+b_*)-\tfrac32g'(b_*),\qquad
 \ell_b(v)=\Re p\,(v-\Re b_*).
 \end{gathered}
 \tag{1}
\]
All starred coordinates belong to the same actual reference. The
outgoing coordinate \(b\) is an own-four leg of the neighboring
ordinary block. It is not that block's next external input; the
latter may be attached when \(m=3\).

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), \(X=e^{-2\pi iz}\), and
\(Y=e^{-2\pi ib}\), the exact finite kernels are
\[
 \begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
             \frac{H_N(w,r^{-i})p_i(X)}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
             \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 \mathcal K_N(w;X,Y)&=
          U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N}.
 \end{split}
 \tag{2}
\]
The outgoing allocation is the separate modulus
\(|d_N(Y)|^{1/2}\). No holomorphic square root is chosen.
The complete selected factor \(d_N(X)X^{-N}\) is retained,
with no division by either Fourier weight. Only the cap depends
on the ordinary color \(w\), whose complete value is \(-2\).

**Theorem 1.** For every \(\tau>0\) and fixed ordinary-color
derivative order \(k\ge0\), a sufficiently small fixed color
disk about \(-2\) and constants \(C_{\tau,k},D_{\tau,k},N_0\)
give, uniformly for \(y,v\in P\), at every integer \(N\ge N_0\),
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|\,|d_N(Y)|^{1/2}
 \le C_{\tau,k}N^{D_{\tau,k}}
       \exp N\{M+\ell_b(v)-1/2000+\tau\}.
 \tag{3}
\]
Both level parities are included. Taking \(\tau<1/4000\)
gives the finite gap \(1/4000\), with a polynomial prefactor.
The estimate includes all indices in both sums (2), the cap's
complete inner endpoint coefficient, every contour current and
every original finite-row endpoint.

## 2. The ten completed scalar comparisons

Use the five cap profiles \(A_0,A_L,A_R,A_-,A_+\)
and four ordinary profiles \(B_0,B_L,B_R,B_1\) of the
finite reduction. Every \(B_j\) includes the same outgoing
rate \(-\Re g(b)/2\). The two selected Fourier alternatives are
\[
 W_1(y)=-\Re g(y+iH)-2\pi H,\qquad W_0(y)=0.
 \tag{4}
\]
They bound the same complete Fourier polynomial in (2); they
are not a decomposition into new finite sources.

The four
[half-row majorants](research_mixed_selected_four_four_half_row_majorant.md)
and two
[left-cap/main majorants](research_mixed_selected_four_four_left_main_majorant.md)
now satisfy
\[
 \mathcal H^{(4)}_{0,\nu}<-1/2000,\qquad
 \mathcal H^{(4)}_{L,\nu}<-1/2000,\qquad
 \mathcal J^{(4)}_\nu<-1/2000,\qquad \nu=0,1.
 \tag{5}
\]
These are reference-only upper bounds after all free real targets
have been eliminated with their original outgoing tangent.
In particular, they prove the same gap for
\((A_0,B_R)\), \((A_L,B_R)\), and \((A_L,B_0)\)
with either alternative (4).

For the ordinary left cut, the
[four-corner reduction](research_mixed_selected_four_left_row_corners.md)
proves
\[
 B_0(y,v)-B_L(y,v)\ge
       \min_{\epsilon,\eta\in\{11/50,9/20\}}D_{\epsilon,\eta}.
 \tag{6}
\]
Its exact trial uses the actual index \(s_*\), not a new
optimizer. The four lower bounds are now all strictly positive.
Thus \(B_L<B_0\) on \(P^2\). Adding any cap profile,
either rate (4), and the unchanged outgoing tangent preserves
this pointwise comparison. No additional quantified left-row gap
is needed.

The common proof of these six upper and four lower signs is the
[ten-test certificate](research_mixed_selected_four_four_scalar_cover.md),
with its
[pending-only continuation](research_mixed_selected_four_four_scalar_continuation.md).
Both stages use the same original rational endpoint maps and
necessary-reference filters on
\[
                 u\in[.217,.234]+i[.027,.045].
 \tag{7}
\]
These filters contain every required actual reference, including
the length-three attached external input. They do not assert that
every retained auxiliary point occurs in a word.

The original primitive is evaluated with its proved
[centered enclosure](research_mixed_centered_primitive_enclosure.md)
on regular convex rectangles. The actual private action uses the
same auxiliary \(u\); only the fixed cap cut uses its canonical
explicit radical. The own-four factorial, outgoing halfweight,
chirps and clipped quadratic gains are unchanged in both stages.
No critical root, finite quantum sum or earlier source certificate
is evaluated by this scalar cover.

The original
[attempt01](../repro/results/research-mixed-selected-four-four-scalar-cover-attempt01.json)
stopped at its 8,000-visit budget with 3,997 terminal leaves and
seven uninspected pending boxes. The
[continuation](../repro/results/research-mixed-selected-four-four-scalar-cover-attempt02.json)
processed only those seven boxes and descendants. It completed
after 2,989 additional visits, adding 80 accepted and 1,418
excluded leaves.

The final partition has 5,495 terminal leaves: 1,534 accepted
and 3,961 necessarily excluded, with no unresolved cell. Their
addresses are prefix-free with exact dyadic mass one, and every
recorded box agrees with its address. The total node count is
\(10989=2\cdot5495-1\); the maximal depth is 20.
The original 3,997 entries are preserved exactly, including their
canonical JSON hash. Every new leaf descends from one of the seven
original pending roots.

A saved-data check verifies all 15,340 rational endpoint signs
and all 39 current input bindings. The six largest upper endpoints
are approximately
\[
 \begin{array}{c|r}
 \text{main half-row, factorial}&-0.001063675273742578\\
 \text{main half-row, forced}&-0.1141845400238992\\
 \text{left half-row, factorial}&-0.03868077504306916\\
 \text{left half-row, forced}&-0.1458154574488182\\
 \text{left main, factorial}&-0.011914956171083107\\
 \text{left main, forced}&-0.018537654826815887 .
 \end{array}
 \tag{8}
\]
The smallest of all saved corner lower endpoints is approximately
\(0.009588270102253226>0\). The exact rational endpoints,
not these displays, establish the signs.
The completed record has SHA256
1a4538b1b2dbe21621d87a88ee4123598d22ceadde0c5c36a5e5bfcfd37bbabf.
Its immutable parent has SHA256
07ed9c2f056f1e5ddc133212c5639a49fe63e1bd43a65773a4b9b28715ef5f4a.
The saved-data check reevaluates no primitive or reference map.

## 3. From the five pairs to the whole finite product

The independent pairs in the finite reduction are
\[
                 (0,L),\quad(0,R),\quad(L,0),\quad(L,L),\quad(L,R).
 \tag{9}
\]
Equation (5) pays the two half-row pairs and the left-cap/main
pair. Equation (6) reduces \((0,L)\) to the proved central
pair \((0,0)\), and \((L,L)\) to \((L,0)\).
The central gap is \(1/500\), so all five pairs have raw
gap at least \(1/2000\), with strict inequalities.

The remaining profiles are accounted for as follows.

| Ordinary profile | Joint control for all five cap profiles |
|---|---|
| Main \(B_0\) | The central theorem pays \(A_0\), (5) pays \(A_L\), and the right cap cut and both aliases are pointwise below \(A_0\). |
| Left row \(B_L\) | Equation (6) reduces each pair to the same cap paired with \(B_0\). |
| Half row \(B_R\) | Equation (5) pays \(A_0,A_L\); the other cap profiles are pointwise below \(A_0\). |
| Last row \(B_1\) | The proved last-row estimate pays every cap profile, retaining the outgoing halfweight. |

Thus all twenty cap/ordinary profile pairs and both alternatives
(4) are controlled. The finite reduction already includes the
original joins, horizontal and vertical aliases, zero-safe physical
tails, half-grid slivers and both level parities. Its positive-height
cap-tail argument retains the reflected factor \(e^{2\pi H i}\);
it does not import a negative-height cap bound.

Let \(\mathcal D_5\) be the five-pair maximum in that reduction.
The proved signs give \(\mathcal D_5<-1/2000\). Its complete
finite bound is
\[
 |\partial_w^k\mathcal K_N|\,|d_N(Y)|^{1/2}
 \le C_{\tau,k}N^{D_{\tau,k}}
   e^{N\{M+\ell_b(v)+\max(-1/500,\mathcal D_5(y,v))+\tau\}}.
 \tag{10}
\]
Equation (3) follows immediately. The color neighborhood,
interpolation errors, factorial estimates and finite contour
tolerances consume one arbitrarily small total \(\tau\).
The outgoing modulus halfweight is independent of \(w\);
Cauchy's formula for the original cap color gives the fixed
derivative assertion without differentiating a square root.

The theorem supplies the complete local weighted estimate at the
stated selected height and plateau targets. It does not alone
estimate every remaining chain factor, every Fourier selection,
nonplateau regions, length two, or arbitrary short fillings.
In particular no global volume theorem or whole-invariant
noncancellation is inferred from this local result.
