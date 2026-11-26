# Explicit conditions for extending the ordinary endpoint packet

Research deduction, 5 November 2026. Frozen source records and manuscripts
are unchanged. This note extends the actual complete-boundary coefficient
to a specified complex-index rectangle. Its whole finite source is
controlled by an explicit critical-point enclosure and three outward
scalar inequalities, without a source-row cover. A second deduction explains how an
open-source contour estimate would supply the whole ordinary-boundary
strip bound without a separate outside-angle cover for each word.

## 1. The specified source and the proposed parameter domain

Use the canonical factorial \(G_N\), Newton polynomials \(e_l(w)\),
and the exact finite continuation from
[the full-index boundary theorem](research_complete_boundary_full_index_interval.md):
\[
 \mathcal C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^l2\sin(\pi j/N).
 \tag{1}
\]
At \(e=j/N\), the terms \(l>j\) vanish exactly and
\(\mathcal C_N(j/N,w)=\delta_j b_{j,N}(w)\). Thus (1) retains
the whole ordinary endpoint polynomial and both level parities.
In particular it is not an arbitrary interpolation of its samples.

Let \(J'(z)=\Log(2\sin\pi z)\), with the original branch continued
from \(0<z<1\). At \(w=-2\), define
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 u_c(e)&=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2},
 \qquad S(e)=F(e,u_c(e)).
 \end{split}
 \tag{2}
\]
The roots and logarithms must be the continued original branches;
the equation required below is \(F_u(e,u_c)=0\), not only its
exponentiation. The existing theorem proves the packet on an
unspecified neighborhood of every compact real index interval.
It does not, by itself, cover the following rectangle:
\[
 \mathcal E=[33/100,47/100]+i[-9/100,2/25].
 \tag{3}
\]
Write \(h=\Im e\), \(h_+=\max(h,0)\), \(h_-=\max(-h,0)\), and
put
\[
                 a=1/20,\qquad b(e)=\Re e-1/100.
 \tag{4}
\]
These cuts will be moved by \(O(N^{-1})\) to half-grid cuts only
when applying the exact residue formula.

## 2. All real-row tails reduce to three comparisons

For \(0\le x\le1\), use the zero-safe original row upper exponent
proved in [the complex-index theorem](research_complete_boundary_complex_index.md):
\[
 \begin{split}
 \mathcal V(x)&=2\int_0^x\log(2|\cos\pi t|)\,dt-2J(x),\\
 R(e,x)&=\mathcal V(x)-J(x)-\Re J_{\rm side}(e-x)-\pi xh .
 \end{split}
 \tag{5}
\]
Here the side primitive is the reflected reciprocal-factorial
primitive. Its real upper extension includes zeros and the negative
real axis. The original terms in (1), including every fixed ordinary
derivative at \(w=-2\), are bounded by \(N^C e^{NR(e,l/N)}\).

**Lemma 1.** Uniformly for \(e\in\mathcal E\),
\[
 \begin{array}{ll}
 R(e,x)\le\Re F(e,a),&0\le x\le a,\\
 R(e,x)\le\Re F(e,b(e)),&b(e)\le x\le1/2,\\
 R(e,x)\le-\Re J(e)+2\pi h_-+\dfrac{\pi}{2}h_+,
                                      &1/2\le x\le1 .
 \end{array}
 \tag{6}
\]

*Proof.* For \(0<x<1/2\), away from a possible zero,
\[
 \partial_xR(e,x)=
 \log\frac{|\sin\pi(e-x)|\cos^2(\pi x)}{\sin^3(\pi x)}
                  -\pi h .
 \tag{7}
\]
This holds on both sides of the reflected cut. At an intervening
real zero, integrate on its two sides and use continuity.

On \(0<x\le1/20\), one has
\(\Re(e-x)\in[.28,.47]\), so
\(|\sin\pi(e-x)|>1/2\), \(\cos^2\pi x>1/4\),
\(\sin\pi x<1/6\), and \(e^{-\pi h}>1/2\).
The ratio after exponentiating (7) is therefore greater than
\(27/2\). This proves the first line.

For \(x\ge b(e)\ge.32>.3\), that ratio is at most
\[
 e^{.09\pi}\cosh(.09\pi)
       \frac{\cos^2(.3\pi)}{\sin^3(.3\pi)}
             <\frac75\frac23=\frac{14}{15}<1.
\]
Indeed the trigonometric quotient is less than \(2/3\) by the
exact pentagon values. Also \(e^{.18\pi}<9/5\): use
\(.18\pi<4/7<\log(9/5)\), where the second inequality follows
from \(\log(1+t)>2t/(2+t)\) at \(t=4/5\).
This proves the second line. At both cuts \(x<\Re e\), so the
upper exponent is exactly \(\Re F(e,x)\).

For the last line, put \(v=1-x\in[0,1/2]\). Reflection gives
\[
 R(e,1-v)=2J(1/2-v)+3J(v)-\Re J(e+v)
                       +\pi|h|-\pi(1-v)h .
\]
The first two terms are nonpositive. Moreover
\(-\Re J(e+v)\le-\Re J(e)\). To see this, while
\(\Re(e+v)\le1/2\), the horizontal derivative
\(\log|2\sin\pi(e+v)|\) is positive, because
\(\Re(e+v)\ge.33>1/6\). Above \(1/2\),
\(\Re J(e+v)\ge J(\Re(e+v))\ge0\), whereas
\(\Re J(e)\le J(\Re e)<0\). The vertical comparison follows
directly from the sign of \(\Arg\sin\pi(x+it)\) on the two
half-strips. Finally
\(\pi|h|-\pi(1-v)h\le2\pi h_-+(\pi/2)h_+\).
All endpoint statements follow by continuity. \(\square\)

## 3. Complex-index aliases need no separate parameter cover

On the rectangle \(a\le\Re u\le b(e)\), every relevant real part
\(\Re u,\Re(e-u),\Re(1/2-u)\) lies strictly between zero and
\(1/2\). Consequently, at all finite heights,
\[
 -\Re F_{uu}(e,u)
 =\pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(e-u)\}>0.
 \tag{8}
\]
This statement remains valid for complex \(e\).

**Lemma 2.** For \(a\le x\le b(e)\) and \(y\ge0\),
\[
 \Re F(e,x-iy)-2\pi y
 \le \Re F(e,x+iy)-2\pi(1/2-\Re e)y.
 \tag{9}
\]
Also \(y\mapsto\Re F(e,x+iy)\) is strictly convex.

*Proof.* The terms \(-2J(1/2-u)-3J(u)\) have conjugate real
parts at \(x\pm iy\). The exact difference is
\[
 \Re F(e,x-iy)-\Re F(e,x+iy)
 =2\pi y\Re e+
       \int_{-y}^{y}\Im J'(e-x+it)\,dt.
\]
Since \(0<\Re(e-x)<1/2\), the sine in the integral has positive
real part. Its argument lies in \((-\pi/2,\pi/2)\).
The integral is at most \(\pi y\), which proves (9).
The Cauchy--Riemann equations and (8) give strict vertical
convexity. \(\square\)

Thus, if the upper horizontal segment passes through \(u_c(e)\),
it has its unique maximum there. Every upper vertical side has
maximum at one of its two endpoints. The lower alias is controlled
by the corresponding upper side or segment through (9). The upper
alias has its usual factor \(e^{-2\pi Ny}\). No reflection identity
requiring real \(e\) has been used.

## 4. A concrete packet-extension criterion

**Theorem 3.** Let \(\mathcal K\subset\mathcal E\) be compact.
Suppose the original branch in (2) is holomorphic near
\(\mathcal K\), satisfies \(F_u(e,u_c(e))=0\), and obeys
\[
 a<\Re u_c(e)<b(e),\qquad \Im u_c(e)>0
 \tag{10}
\]
with uniform positive separation from all three boundaries.
Suppose, for some \(\delta>0\), all three quantities
\[
 \begin{split}
 \Re S(e)-\Re F(e,a),\qquad
 \Re S(e)-\Re F(e,b(e)),\\
 \Re S(e)+\Re J(e)-2\pi h_--(\pi/2)h_+
 \end{split}
 \tag{11}
\]
exceed \(\delta\) throughout \(\mathcal K\).
Then the whole function (1) has the joint ordinary-color packet
\[
 \mathcal C_N(e,w)=N^{-3/2}\mathcal A(e,w)
                         e^{N\mathcal S(e,w)}(1+O(N^{-1}))
 \tag{12}
\]
on a fixed neighborhood of \(\mathcal K\times\{-2\}\).
The phase and nonzero amplitude are precisely those of
[the full-index theorem, equations (26)--(28)](research_complete_boundary_full_index_interval.md).
The relative error is holomorphic, uniformly with every fixed
joint derivative on smaller neighborhoods.

*Proof.* Lemma 1 and (11) bound all original rows outside the cuts
by a polynomial times \(e^{N(\Re S-\delta)}\), including the
off-grid terms which vanish at physical integer indices.
The retained summand is the exact regular factorial interpolation,
with its nonzero \(N^{-2}\) symbol. Use the full rectangle with
heights \(\pm H(e)\), \(H(e)=\Im u_c(e)\), and half-grid cuts
near (4), with kernel \(1/(1-e^{-2\pi iNu})\).

By (8), the upper horizontal segment has the unique nondegenerate
maximum \(u_c(e)\). Its cut endpoints have a uniform strict gap.
Their lower, real endpoints have the gap (11); vertical convexity
therefore bounds both entire upper vertical sides. Equation (9)
bounds both lower vertical aliases, including their limits at the
real cuts. On the lower horizontal segment it gives the uniform
additional loss \(2\pi(1/2-\Re e)H(e)>0\). The upper horizontal
alias loses \(2\pi H(e)>0\). These are all pieces of the exact
residue identity, not a selection of its formal stationary points.
The half-grid perturbations preserve the fixed gaps.

The remaining upper horizontal integral has a nonzero Gaussian
coefficient and power \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\).
Its first odd correction integrates to zero. This proves (12)
at \(w=-2\), uniformly near the compact parameter set.

For the whole ordinary color, the original Newton product obeys
the zero-safe bound
\[
 |e_l(w)|\le N^C
       \exp N\{\mathcal V(l/N)+C\sqrt{|w+2|}\}
\]
on a fixed small color disk, as proved in the full-index theorem.
It preserves the discarded-row gaps, including the odd exact zero.
On the retained regular contour the exact factorial symbol is
jointly holomorphic, and the critical point, currents and aliases
persist by continuity. This gives (12) on the stated fixed product
neighborhood, then all derivatives by Cauchy's estimate. \(\square\)

**Certified instance.** The whole rectangle \(\mathcal E\) in (3)
satisfies Theorem 3. Its original critical branch obeys
\[
 19/100<\Re u_c<7/25,\qquad
 1/100<\Im u_c<1/10,\qquad a<\Re u_c<b(e),
 \tag{12a}
\]
and the three quantities in (11) exceed \(1/5,1/20,1/5\),
respectively. Thus (12) holds on a fixed open neighborhood of
\(\mathcal E\times\{-2\}\), with its nonzero original amplitude and
all fixed joint ordinary-color and index derivatives. The size of
the additional neighborhood and color disk is not numerically specified.

Here is the finite outward verification. Split \(\mathcal E\) at
\(h=0\), then exhaust the two rectangular binary trees. On each
whole cell evaluate the explicit square root and arctangent in (2).
The discriminant has real part greater than one. The resulting
regular critical image satisfies (12a), and the imaginary part of
the original \(F_u\) lies in \((-\pi,\pi)\). The exact cubic
factorization in the complete-boundary calculation and the regular
original logarithms imply \(e^{F_u}=1\); this interval therefore
fixes its lift as zero.

For clarity, the three scalar gaps are not accepted from samples.
Put
\[
 B(e)=-J'(e-u_c)+i\pi u_c,\qquad
 \kappa_-=-2\pi,\quad\kappa_+=\pi/2 .
 \tag{12b}
\]
Their exact derivatives in \(r=\Re e,h=\Im e\), in the order
of (11), are
\[
 \begin{array}{c|cc}
 &\partial_r&\partial_h\\ \hline
 D_1&\Re(B-F_e(e,a))&-\Im(B-F_e(e,a))\\
 D_2&\Re(B-F_e(e,b)-F_u(e,b))&-\Im(B-F_e(e,b))\\
 D_3&\Re(B+J'(e))&-\Im(B+J'(e))-\kappa_\pm .
 \end{array}
 \tag{12c}
\]
The whole-cell derivative enclosures give each lower bound as its
outward midpoint value minus the two gradient bounds times the
corresponding half-widths. The complete 256-bit check accepts
389 cells in 776 visits. The saved-cell replay recomputes these
inequalities and the original critical image; it cannot refine a
failed saved cell. No numerical row, contour-current or ordinary-color
parameter cover is used.

## 5. How the whole ordinary-boundary strip estimate can be inherited

There is a separate, general source-side reduction. Write
\(\widetilde B_N(x,w)\) for the canonical entire Newton interpolation,
and let
\[
 \mathcal X=\{x:\alpha\le\Re x\le\beta,\ |\Im x|\le H\},
                    \qquad0<\alpha<\beta<1/2.
 \tag{13}
\]
The [canonical boundary theorem](research_free_boundary_cardinal_factorial_comparison.md),
not only agreement in the physical quotient, gives
\[
 |\widetilde B_N(x,-2\cos(s+it))|
 \le C N^A
 e^{N\{\Re b(x,0)-c(1-\cos s)+Bt^2\}}
 \tag{14}
\]
uniformly for \(x\in\mathcal X\), \(|s|\le\pi\), and a fixed thin
strip. Both original normal data and moving reciprocal zeros are
retained.

Suppose an exact open-source representation, with all its currents,
has a retained part
\[
 Z_N^{\rm ret}(u,v)=
 \sum_\ell\int_{\Gamma_\ell}
       a_{\ell,N}(z)\,
       \widetilde B_N(x_L(z),-2\cos u)
       \widetilde B_N(x_R(z),-2\cos v)\,dz,
 \tag{15}
\]
where the two wire indices stay in \(\mathcal X\), the other
factors are independent of \(u,v\), and the contours have bounded
total variation after any explicit polynomial factors are included.
Assume the weighted absolute contour estimate
\[
 \sum_\ell\int_{\Gamma_\ell}|a_{\ell,N}(z)|
  e^{N\{\Re b(x_L(z),0)+\Re b(x_R(z),0)\}}\,|dz|
                         \le C N^A e^{NM}.
 \tag{16}
\]
Assume the discarded original source is separately of ordinary
degree at most \(N-1\), and its supremum over both complete real
boundary periods is at most \(C N^A e^{N(M-\delta)}\).

**Corollary 4.** For some fixed \(c,B,h>0\), the full original
source satisfies
\[
 |Z_N(s+it,r+iq)|
 \le C N^A e^{N\{M-c(1-\cos s)-c(1-\cos r)+B(t^2+q^2)\}}
 \tag{17}
\]
for \(|s|,|r|\le\pi\), \(|t|,|q|\le h\).

*Proof.* Apply (14) inside (15), then (16). For the original
discarded polynomial, Fourier/Chebyshev continuation costs at most
\(N(|t|+|q|)\), with a polynomial prefactor. Choose \(h\le\delta/8\)
and \(c\le\delta/8\). Since the sum of the two angular deficits is
at most four, its strict discarded-source gap absorbs both this
continuation cost and the advertised angular losses. \(\square\)

This is the mechanism used for the successful
[internal \(3,3\) packet](research_internal_pair_three_full_boundary_packet.md),
Section 4, stated without restricting the interior word.
It does not infer (16) from the value of the source at \(u=v=0\):
that value may be small because of cancellation. Nor does it infer
the uniform discarded-boundary hypothesis from a complete-color
gap alone. These two obligations concern the actual source contour.
Once they and its nonzero local packet are proved for a general word,
(17) needs no further outside-angle cover.

## 6. Exact composition and the remaining general-word task

For a word \(W\), put
\(P_{W,N}(z,z')=v(z)^{\mathsf T}A_Wv(z')\), where
\(A_W\) is the literal ordered product of the original \(A_n=JM^n\).
The Frobenius pairing satisfies
\(\phi_N(v(x)v(x)^{\mathsf T})=J\), \(J^2=I\).
Therefore
\[
 P_{UV,N}(z,z')=
 \phi_N^{(x)}\phi_N^{(y)}
  [P_{U,N}(z,x)\,K_N(x,y)\,P_{V,N}(y,z')],
 \qquad K_N(x,y)=v(x)^{\mathsf T}v(y).
 \tag{18}
\]
This is an exact ordinary-polynomial identity, including every
repeated-root normal. It is not an asymptotic multiplication rule.

The [finite-kernel closure theorem](research_finite_two_boundary_kernel_closure.md)
uses precisely a nonzero holomorphic bidisk packet, positive real
boundary curvature, and (17). Its long intervening crossing ensures
that the new charged stationary point remains inside that bidisk
and below the discarded-source gaps. Equation (18) alone gives
neither assertion for adjacent arbitrary short blocks.

The concrete remaining task is thus a general open-word contour
with its endpoint-eliminated action, not a fixed holomorphic insertion
into the cyclic saddle. The endpoint action in (12) occurs at order
\(N\). Theorems 3 and Corollary 4 isolate its parameter-domain and
whole-boundary obligations; they do not establish open-word
noncancellation, arbitrary short-fill stability, or a new knot family.

## 7. Reproduction and scope

The checker binds the original endpoint proofs and their current
records, including the exact prescribed finite continuation. Those
older finite-level comparisons are used only as provenance for their
written source theorems. The new acceptance uses outward complex
arithmetic on every complete parameter cell, with the derivative
formulas (12c) and fixed rational gap thresholds.

    python3 experiments/certify_mixed_endpoint_packet_extension.py --precision 256
    python3 experiments/certify_mixed_endpoint_packet_extension.py --precision 320 --input repro/results/research-mixed-endpoint-packet-extension.json --output repro/results/research-mixed-endpoint-packet-extension-replay.json

The theorem resolves the endpoint-packet domain obligation for any
actual endpoint map whose private index lies in \(\mathcal E\).
It does not prove that a general open word has such a map, or that
its remaining complete contour satisfies the weighted absolute bound
(16) and the discarded-source hypothesis. Those are separate
all-word geometric and source obligations.
