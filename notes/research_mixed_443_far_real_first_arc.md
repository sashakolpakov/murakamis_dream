# The last real first-coordinate arc with a real second coordinate

Private written proof, 11 November 2026. For an actual word beginning
with \(443\), this note bounds the complete three-factor product when
the first coordinate lies in \([7/8,1]\) and the second lies in
\([1/2,18/25]\). It includes the closed first endpoint and both Fourier
choices at each coordinate.

The comparison uses two complete positive upper bounds and an already
calibrated real-cut profile. The real-cut profile is used as a comparison
rate; it is not a lower bound for a quantum sum.

Author-frozen after full proof and direct-source readback. Independent
full proof/direct-source review is required before adoption. No frozen
source or public document is changed.

## 1. The source and the comparison rate

Fix the actual reference of a positive three/four word of length at
least four beginning with \(443\). Use the original reference, endpoint
coefficient, primitive \(g\), affine action \(\Lambda_{123}\), and
ordinary-color convention in
[the complete core-pair theorem](research_mixed_443_core_first_complete_right_pair.md).
In particular,
\[
 P=[11/50,9/20],\qquad z=b+ic_3,\quad b\in P,\qquad
 -13/200\le c_3\le17/250.
\]
The reference, including its private heights, stays fixed.

Put \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), \(p_j(V)=(rV;r)_j\),
and retain the literal finite functions
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}H_N(w,r^{-i})\,p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
               X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon}.
\end{split}
\]
Here \(H_N\) is the complete original endpoint polynomial.
The polynomial \(d_N\) of degree less than \(N\) satisfies
\(d_N(r^j)=P_j^{-1}\). It is used as a polynomial also away from
these nodes.

Our first and second coordinates are real:
\[
 7/8\le a\le1,\qquad 1/2\le q\le18/25,\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iq},\quad Z=e^{-2\pi iz}.
\]
For \(\nu,\mu\in\{0,1\}\), let
\[
 \mathcal J_{\nu,\mu,N}
  =U_N(w,X)d_N(X)X^{-\nu N}C_{1,N}(X,Y)
                      d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z).       \tag{1}
\]
There is no outgoing halfweight because the third letter is three.

**Theorem.** There is a fixed ordinary-color disk about \(-2\) on
which, at both level parities,
\[
 |\mathcal J_{\nu,\mu,N}|
       \le C N^A e^{N\{\Lambda_{123}(z)-1/200\}}.            \tag{2}
\]
The estimate is uniform over the displayed first, second and third
coordinate ranges and both Fourier choices. It holds for every real
ordinary color \(w\in[-2,2]\), and for fixed color derivatives on
smaller fixed disks. Integration on any oriented subinterval with
the original density \(+N\,da\) preserves this exponential rate.

The first interval \([1/2,7/8)\), the other first-contour pieces and
the later second interval are not conclusions of this theorem.

Write
\[
 J(t)=\int_0^t\log(2|\sin\pi v|)\,dv,
 \qquad J(0)=J(1/2)=J(1)=0,
\]
extended continuously and periodically. For real \(a,q\), the
physical first-kernel rate is
\[
 E_1(t;a,q)=I_a(t)+I_q(t)-3J(t),\qquad
 I_x(t)=\int_0^t\log|1-e^{-2\pi i(x+v)}|\,dv .
\]
Define its real half-input left-cut rate by
\[
                      L(q)=E_1(1/8;1/2,q).               \tag{3}
\]
The reference cap's original main profile at that same first input is
\[
 A_0=\max_{27/100\le u\le49/100}
                     \Re\Psi(u+ih_e,1/2),                \tag{4}
\]
where \(h_e\) and \(\Psi\) retain their original values and constants.

## 2. What the complete core-pair proof already calibrates

Sections 3 and 7 of the core-pair proof compare (3) with the entire
third-factor envelope, before estimating any finite sum. Let \(R(q,z)\)
denote that envelope. More explicitly, it is the maximum of:

* the actual third-height main rate on its prewall interval;
* its lower and upper sampling rates, with penalties
  \(2\pi(13/200)\) and \(2\pi/5\);
* the original half-face third real-left, half and last rates.

Its private lower and upper heights are \(-13/200\) and \(1/5\).
The prewall interval is
\([1/8,\min(r_0,1-q-\varepsilon)]\), with \(r_0<1/2\) sufficiently
close to one half and then \(\varepsilon>0\) sufficiently small.
Both constants are fixed before \(N\). The limiting wall and the
short collars have an arbitrarily small fixed allowance.

The source proof establishes the two implications we need:
\[
 A_0+L(q)+R(q,z)\le \Lambda_{123}(z),                       \tag{5}
\]
and, for every prescribed \(\tau>0\),
\[
 |C_{0,N}(Y,Z)|
       \le C_\tau N^{B_\tau}e^{N\{R(q,z)+\tau\}}.           \tag{6}
\]
To see the precise scope of (5), its first real-left carrier is
exactly (3), and it pairs with every third horizontal by the
joint derivative comparison in that source's equation (11).
Its pairings with the fixed third left, half and last carriers use
the separate nonincrease of \(L(q)\). The complete cap is constant
during this second-coordinate motion; its particular profile (4)
is one of the calibrated alternatives. At the initial half face
the comparison has a positive surplus. Dropping that surplus gives
(5).

Equation (6) includes the two unweighted joins and all four weighted
vertical halves. The third wall rate is at most its actual-height
main rate on this interval; the condition \(q\le18/25\) ensures
\(b+1-q\ge1/2\), which is used in this comparison. Every postwall
middle row decreases from its wall value. The low rows and the
entire high block reduce to the three fixed physical carriers.
The original finite residue formula and the zero-safe product
bounds therefore give (6) through both true endpoints and both
parities. No first conditional factor is divided out to obtain it.
These are the profile and finite-source implications in the written
proof, not consequences inferred from its final product bound.

## 3. A lower bound for the calibrated comparison rate

The cap trial proved in Section 3 of
[the selected-second real-first-arc note](research_mixed_complete44_second_selected_real_first_arc.md)
gives
\[
                            A_0>181/200.                 \tag{7}
\]
That argument uses only the original endpoint branch and the
actual cap height \( -.051<h_e<-.019\). Its trial point is
\(e=2/5+ih_e\). It makes no assumption about the second coordinate,
so it applies unchanged to (4).

We next bound all three terms in (3). The inequality
\(2\sin\pi t<2\pi t\) on \(0<t\le1/8\) gives
\[
 -J(1/8)>
      \frac18\{1-\log(\pi/4)\}>\frac{31}{200}.             \tag{8}
\]
For the last strict inequality use \(\pi<22/7\) and
\(\log(14/11)>6/25\). The latter follows from the first term
\(2(3/25)=6/25\) of the positive series
\(\log x=2\operatorname{artanh}((x-1)/(x+1))\).

On the same interval, \(2\cos\pi t>9/5\). For example,
\(\pi/8<2/5\) and \(\cos u>1-u^2/2\) give the stronger
bound \(2\cos(\pi/8)>46/25\). Thus
\[
 I_{1/2}(1/8)>\frac18\log(9/5)>\frac1{14},                 \tag{9}
\]
using \(\log(9/5)>2(2/7)=4/7\).

For \(q\in[1/2,18/25]\) and \(0\le v\le1/8\), the angle
\(q+v\) lies in \([1/2,169/200]\). Hence
\[
 |1-e^{-2\pi i(q+v)}|
       \ge2\sin(31\pi/200)>2\sin(3\pi/20)>4/5.
\]
For a direct witness to the final inequality, \(3\pi/20>15/32\),
and
\(\sin(15/32)\ge15/32-(15/32)^3/6>2/5\).
Consequently
\[
 I_q(1/8)>-\frac18\log(5/4)>-\frac1{32},                   \tag{10}
\]
since \(\log(1+u)<u\).

Combining (8)--(10) proves uniformly
\[
                   L(q)>\frac{93}{200}+\frac1{14}
                                      -\frac1{32}.       \tag{11}
\]
These are lower bounds for the explicitly defined real functions
(3)--(4). They assert no lower bound for a coherent quantum sum.

## 4. Complete positive bounds at the last first arc

Section 3 of
[the far-right physical envelope](research_mixed_initial44_far_right_physical_envelope.md)
bounds every original cap row, retaining the coherent endpoint
coefficient within each row. Its resulting bound is
\[
 \sup_{w\in[-2,2]}|U_N(w,e^{-2\pi ia})|
       \le C_\tau N^{B_\tau}e^{N(223/240+\tau)}
                  \qquad(7/8\le a\le1).                 \tag{12}
\]
Its separate finite-end estimates apply on the entire closed unit
disk; its other rows use the zero-safe sine-product estimate.
Thus (12) includes \(a=1\), all numerator zeros, all cap indices,
and both parities.

Sections 2--3 of
[the far-real second-arc proof](research_mixed_complete44_second_far_real_arc.md)
supply an independent conditional estimate:
\[
 |C_{1,N}(e^{-2\pi ia},W)|
       \le C_\tau N^{B_\tau}e^{N(7/15+\tau)}
              \quad(7/8\le a\le1,\ |W|\le1).              \tag{13}
\]
Its proof splits at \(j/N=1-a\). Below that point the quotient
\(|p_j(e^{-2\pi ia})|/|P_j|\) has the binary-entropy bound
proved there; above it its continuous quotient rate is nonpositive.
The remaining factor is covered by the complete disk norm.
The incoming monomial has modulus one. This proves (13) for all
indices through \(N-1\), without requiring a physical root or
discarding the rows beyond a terminating index. It applies to
\(W=Y\) in our real second interval.

Both original Fourier polynomials have zero upper exponential rate
on the required real arcs. On compact subintervals of \((1/2,1)\)
this follows from the absolute Fourier bound
\(\max\{-J(x),0\}=0\). The same statement includes \(x=1\):
Section 5 of the far-real second-arc proof uses the exact Newton
formula for \(d_N\) and the uniform endpoint modulus estimate to
give an arbitrarily small exponential allowance there. Thus
\[
 |d_N(X)|+|d_N(Y)|\le C_\tau N^{B_\tau}e^{N\tau}.            \tag{14}
\]
Both monomials in (1) have modulus one. Equations (12)--(14)
give the complete first cap, first kernel and both diagonal factors
a combined upper rate
\[
                     \frac{223}{240}+\frac7{15}
                                      =\frac{67}{48},    \tag{15}
\]
with any prescribed total allowance.

The comparison with (7) and (11) is strictly favorable:
\[
 A_0+L(q)-\frac{67}{48}
   >\frac{181}{200}+\frac{93}{200}+\frac1{14}
                       -\frac1{32}-\frac{67}{48}
    =\frac{241}{16800}>\frac1{100}.                       \tag{16}
\]
This is the additional reserve which pays for replacing the cap
and first conditional factor by their positive bounds.

## 5. Assembly, color continuation and scope

Multiply (6) by (12)--(14). By (5) and (16), the complete product
(1), for every real ordinary color, has upper rate less than
\(\Lambda_{123}(z)-1/100\), with an arbitrarily small prescribed
total allowance. The contours, collars and regularizers used in
(6) are fixed before \(N\); all finite counts and densities have
only polynomial cost.

The exact degree in \(w\) is less than \(N\). The elementary
Chebyshev estimate in
[the polynomial continuation proof](research_mixed_horizontal_complex_extension.md),
Section 1, extends the real-color bound to a fixed disk about
\(-2\) with any prescribed small exponential cost. Here the
other factors in (1) are color-independent constant multipliers.
The argument applies to the whole polynomial and does not divide
by such a multiplier, including at its zeros. Cauchy's formula
gives every fixed derivative on a smaller disk.

Choose all finite-source and color allowances with total less
than \(1/200\). Equation (2) follows. The extra factor \(N\)
from an oriented first-coordinate integral changes only the
polynomial prefactor.

This theorem pays the closed far first arc only. In particular,
it does not apply the existing unit-incoming critical-branch
theorem to \(q>1/2\): that theorem's outgoing half-plane hypothesis
does not cover this domain. A bound on the intervening first arc
\([1/2,7/8]\) still requires a separate proof.

## Direct source versions

| Direct source | Used implication | SHA-256 |
|---|---|---|
| research_mixed_443_core_first_complete_right_pair.md | Sections 3, 7 and 8: real-left/profile calibration and complete third-source envelope on the real second interval | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_complete44_second_selected_real_first_arc.md | Section 3: original cap trial \(A_0>181/200\), independent of the second coordinate | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_initial44_far_right_physical_envelope.md | Section 3: complete cap bound \(223/240\), including both true ends and every real color | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_complete44_second_far_real_arc.md | Sections 2--3 and 5: complete conditional bound \(7/15\) on the far incoming unit arc, and the endpoint bound for the whole Fourier polynomial | 922a114d355f134aae94065d2c8996ac26d670f6dd5439f20285c7c7b627dd2e |
| research_mixed_fourier_weight_continuation.md | Section 5: absolute full Fourier bound on compact real arcs | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | Section 1: elementary polynomial continuation from the real color interval | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The author read the complete proof and every directly used source
implication and checked all six bindings. The profile calibration in
(5) was checked before finite summation; it was not extracted from
the product bound in the core-pair theorem. Independent full proof and
direct-source review remain required. No mathematical numerical
evaluation, saved-value arithmetic, test, import, compilation or
frozen-source edit was used.

