# Horizontal concavity and index barriers at the second selection

Research deduction, 6 November 2026. The main/main phase for a selected
second retained coordinate is strictly concave on its original horizontal
product, for both alternatives of the full Fourier weight. Its maximizing
indices lie in smaller intervals on which stronger pair estimates apply.
These statements do not assert a negative central defect or control the
other finite-current profiles. No source, root, or numerical cover is
evaluated; the new polynomial identity below uses exact rational algebra.

## 1. Original variables and both Fourier alternatives

Use the actual reference and source of the
[second-selection reduction](research_mixed_second_selected_plateau_reduction.md),
with a fixed positive mixed three/four word of length \(m\ge4\),
\((\epsilon_1,\epsilon_2,\epsilon_3)=(\alpha,1,\beta)\),
and position 1 unselected. Put
\[
 a=r_1,\qquad u=s_2,\qquad z=r_2,\qquad v=s_3,\qquad b=r_3,
 \qquad \alpha,\beta\in\{0,1\}.
 \tag{1}
\]
The symbols on the right specify the roles of the target variables; stars
denote their original coupled reference values. Both \(u_*,v_*\) are
ordinary indices, also when \(m=4\). Fix all heights at their actual
values except \(\Im z=H\), where \(0\le H\le7/500\). The bounds needed
below are
\[
 \begin{gathered}
 -.102<h_u<-.001,\qquad -.078<h_a<.021,\\
 (h_v,h_b)\in
 \begin{cases}
 (-.065,.068)^2,&\beta=0,\\
 (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{2}
\]
The height enclosure for \(a\) contains both actual attached types;
its type-four lower endpoint uses the proved coupled attached-height
bound. The ordinary real references satisfy
\(u_{*,R}\in(.24,.36)\), and
\(v_{*,R}\in(.267,.433)\) or \((.24,.36)\) according to \(\beta\).
No private endpoint is used in an ordinary image theorem.

Write \(V(s,w)=g(s+w)-g(s)-g(w)\), retaining the original primitive and
logarithmic lifts. Up to the two original affine boundary subtractions
and a real constant, the two objectives are
\[
 \begin{split}
 F_\nu={}&V(u,a)+V(u,z)+V(v,z)+V(v,b)
       -g(u)-\beta g(v)-\nu g(z)\\
 &-\frac\alpha2g(a)-\frac\beta2g(b)+2\pi iau+2\pi izv,
 \qquad \nu\in\{0,1\}.
 \end{split}
 \tag{3}
\]
Here \(\nu=1\) is the factorial alternative, with the additional
constant \(-2\pi H\); \(\nu=0\) is the forced alternative.
The affine subtractions are exactly those in the
[central-budget proof](research_mixed_second_selected_central_budget.md),
not independently chosen tangents. Their presence does not affect any
Hessian or either index marginal below.

The original real product, in the order \((a,u,z,v,b)\), is
\[
 K=P\times[1/8,1/2]\times P\times[\ell_\beta,1/2]\times P,
 \qquad P=[.22,.45],\quad \ell_0=.15,\quad\ell_1=.125.
 \tag{4}
\]

## 2. Uniform strict concavity on the original product

**Proposition 1.** At the fixed heights above, both objectives satisfy
\[
 -\Re F_\nu''\succ
 \mu\operatorname{diag}(1,1,2,1,1),
 \qquad \mu=\frac1{1250000},\qquad x\in K.
 \tag{5}
\]
For \(\nu=1\), the Hessian also contains the additional nonnegative
entry \(\pi\Re\cot(\pi z)\) in its \(z\) diagonal relative to \(\nu=0\).

*Proof.* The bare ordinary phase is
\[
 Q_\epsilon(s;a,b)=V(s,a)+V(s,b)-\epsilon g(s)+2\pi ias.
 \tag{6}
\]
On \([.15,.49]+i[-.108,.068]\) for the index and
\(P+i[-.12,.12]\) for the two outer arguments, the
[whole-pair Hessian proof](research_mixed_horizontal_zero_mode_support.md),
equations (8)--(10), gives \(-\Re Q_\epsilon''\succ\mu I_3\).
The [half-index extension](research_mixed_half_index_contour.md) supplies
the same bound through the closed upper face \(\Re s=1/2\).

For own type four the additional interval \([.125,.15]\) follows
from the Schur calculation in Section 2 of the
[smaller-cut proof](research_mixed_four_left_cut_extension.md), with both
outer coefficients set to one. To make this application explicit, write
\(q=\Re\cot\pi s\), \(p_j=\Re\cot\pi a_j\),
\(C_j=\Re\cot\pi(s+a_j)\), and \(D_j=p_j-C_j\).
The cited scalar bounds give
\[
 q>21/20,\quad D_j>9/70,\qquad
 C_j+C_j^2/D_j\le0\ \ (C_j\le0),\qquad
 C_j+C_j^2/D_j<187/120\ \ (C_j>0).
 \tag{7}
\]
The original argument for (7) requires only an outer coefficient at
least one, so it applies to the bare phase (6). Its index Schur
complement exceeds \(3(21/20)-2(187/120)=1/30\).
The determinant exceeds \((1/30)(9/70)^2\), while the trace is less
than \(40/3\). Consequently
\[
 -\Re Q_1''\succ\frac{729\pi}{58800000}I_3
                    \succ\frac1{40000}I_3\succ\mu I_3.
 \tag{8}
\]
All these domains contain (2)--(4).

For the forced phase, add the bounds for \(Q_1(u;a,z)\) and
\(Q_\beta(v;z,b)\). The shared coordinate \(z\) is counted twice,
which gives (5). The remaining negative node terms in (3) have
nonnegative negative real Hessian, because
\(g''(w)=\pi\cot\pi w-\pi i\) and the real parts in question
are at most \(1/2\). The two chirps have zero real horizontal
Hessian. Adding \(-g(z)\) proves the factorial assertion. \(\square\)

One cannot justify the original product by simply declaring each of
the four unweighted \(-\Re V''\) positive on the entire own-four
index interval. The extra own-four factorial is essential to the
small-index proof. Equivalently it can be divided equally between
the two adjacent pairs, as in the central-budget proof's convex
potentials. Proposition 1 supplies a common quantitative reserve;
its small value alone is not a useful selected-gap estimate.

## 3. The left own-four index is greater than .22

**Proposition 2.** Every maximizer of either objective on (4) satisfies
\(u_R>11/50\).

*Proof.* At \(u_R=11/50\), let
\[
 U=e^{-2\pi iu},\quad A=e^{-2\pi ia},\quad Z_H=e^{-2\pi iz},
 \qquad r=|U|,\quad T=|A|^{-1},\quad R=|Z_H|.
 \tag{9}
\]
The original chirp is retained in the exact identity
\[
 e^{2\partial_{u_R}\Re F_\nu}
   =\frac{|A^{-1}-U|^2|1-UZ_H|^2}{|1-U|^6}.
 \tag{10}
\]
Here \(1/2<r<1\), \(T>17/20\), and \(R\ge1\).
Indeed \(.204\pi<2/3<\log2\), proving the first lower bound.
For the second, \(h_a<.021\) and
\(.042\pi<3/20\), together with \(e^x<1/(1-x)\) for
\(0<x<1\), give \(e^{.042\pi}<20/17\).

Both summed real arguments lie in \([.44,.67]\), so their
doubled-angle cosines are less than \(-12/25\); also
\(\cos(.44\pi)>9/50\). The sine cubic witnesses at
\(314/625<.16\pi\) and \(471/2500<.06\pi\), respectively,
are recorded in the next-four endpoint deduction below. In particular,
one does not use the stronger, false bound \(-1/2\) at the upper
summed endpoint \(.67\). Equation (10) is strictly greater than
\[
 \frac{(r^2+\frac{102}{125}r+\frac{289}{400})
             (1+r^2+\frac{24}{25}r)}
      {(1+r^2-\frac9{25}r)^3}.
 \tag{11}
\]
Numerator minus denominator is the exact polynomial
\[
 P(r)=-r^6+\frac{27}{25}r^5-\frac{1493}{625}r^4
       +\frac{62229}{15625}r^3-\frac{44147}{50000}r^2
       +\frac{3237}{1250}r-\frac{111}{400}.
 \tag{12}
\]
For \(r=(1+t)/2\), write
\(P((1+t)/2)=\sum_{j=0}^6 b_j\binom6j t^j(1-t)^{6-j}\).
The exact coefficient vector is
\[
 (b_0,\ldots,b_6)=
 \left(\frac{581611}{500000},\frac{4401979}{3000000},
 \frac{4508591}{2500000},\frac{10839169}{5000000},
 \frac{12712359}{5000000},\frac{4327463}{1500000},
 \frac{387877}{125000}\right).
 \tag{13}
\]
Every coefficient is positive. Thus (11) exceeds one throughout
\(r\in[1/2,1]\), proving a positive marginal on the entire face.
By Proposition 1 that marginal decreases with \(u_R\), with all
other real variables fixed. It is therefore positive for every
\(u_R\le.22\) in the original interval. An admissible increase
of \(u_R\) excludes that entire region from a maximum.
The extra Fourier term is independent of \(u\), so this proves
both alternatives. \(\square\)

## 4. The right index barriers and the restricted convex domain

**Proposition 3.** Every maximizer of either objective satisfies
\[
 v_R>\begin{cases}1/5,&\beta=0,\\11/50,&\beta=1.\end{cases}
 \tag{14}
\]

For \(\beta=0\), this is precisely the index-marginal argument in
Proposition 4 of the
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md),
with its variables \((s,z,b)\) mapped to \((v,z,b)\) here.
It uses only the ordinary derivative and the actual heights of its
index and outgoing leg, not any cap derivative. At \(v_R=.2\),
put \(r=|e^{-2\pi iv}|\), \(R=|Z_H|\), and
\(r_b=|e^{-2\pi ib}|\). Then
\(1/2<r<8/5\), \(r_b>1/2\), and \(1\le R<11/10\).
Including the incoming chirp gives the lower bound
\[
 e^{2\partial_{v_R}\Re F_\nu}>
 \frac{N_1(r)N_2(r)}{D(r)^2},\quad
 N_1=r^2+\frac{10r}{11}+\frac{100}{121},\quad
 N_2=\frac{r^2}{4}+\frac r2+1,\quad D=r^2-\frac{3r}{5}+1.
 \tag{15}
\]
The cited two concave quadratics \(N_1-3D/2\) and
\(N_2-2D/3\) are positive at both endpoints of \([1/2,8/5]\).
Thus the marginal is positive at the cut. Proposition 1 extends
that sign down to the original lower endpoint \(.15\).

For \(\beta=1\), apply Lemma 1 of the
[next-four endpoint deduction](research_mixed_first_four_next_four_endpoint_budget.md),
again with \((s,z,b)=(v,z,b)\). Its derivative is independent
of a cap and of every term added to the present ordinary phase.
At \(v_R=.22\), its lower bound is
\[
 e^{2\partial_{v_R}\Re F_\nu}>
 \frac{\{(91/100)^2+r^2+(24/25)(91/100)r\}
       \{1+(13/25)^2r^2+(24/25)(13/25)r\}}
      {(1+r^2-(9/25)r)^3}>1,
 \quad 13/25<r<1.
 \tag{16}
\]
The same actual negative type-four heights give
\(|e^{-2\pi ib}|>13/25\) and \(R^{-1}>91/100\).
For completeness, numerator minus denominator in (16), written in
the degree-six Bernstein basis at \(r=13/25+(12/25)t\), has
coefficient vector
\[
 \frac1{244140625000}
 (194930869745,221659107435,241725065149,250490096231,
       239542984425,194584871875,90328203125).
 \tag{17}
\]
These are the existing exact coefficients, not a repeated numerical
certificate. Their positivity gives the face sign. Proposition 1
extends it to every \(v_R\le.22\) in the original interval.
This proves (14).

Consequently both maxima are unchanged if (4) is replaced by the
closed convex product
\[
 K'=P\times[.22,.5]\times P\times[q_\beta,.5]\times P,
 \qquad q_0=.2,\quad q_1=.22.
 \tag{18}
\]
The actual real reference lies strictly inside its two index
intervals. No restriction on the three retained real targets is
introduced, and no boundary face of (18) is asserted to be active.

## 5. Stronger pair costs on the justified domain

The restricted product supports useful nonuniform estimates beyond
the small common constant in (5). Write
\(a_w=\Re\cot\pi w\). The pair inequalities in Section 2 of
the [next-three left-cut majorant](research_mixed_selected_cap_left_main_majorant.md)
and the [next-four left-cut majorant](research_mixed_selected_four_four_left_main_majorant.md)
give
\[
 -\pi^{-1}\Re V(s,w)''\succeq\operatorname{diag}(0,a_w/2).
 \tag{19}
\]
For \(s=u\), or \(s=v\) with \(\beta=1\), use the latter
lemma on \([.22,.5]\times P\) with absolute heights at most
\(.102\). For \(s=v\) with \(\beta=0\), use the former on
\([.2,.5]\times P\) with absolute heights at most \(.068\).
Every pair in (3) satisfies its indicated hypotheses, including the
attached incoming height and the selected height.

Adding the four inequalities and the unchanged node terms yields,
in the order \((a,u,z,v,b)\),
\[
 -\pi^{-1}\Re F_\nu''\succeq
 \operatorname{diag}\left(
 \frac{1+\alpha}{2}a_a,\ a_u,\ (1+\nu)a_z,
                    \beta a_v,\ \frac{1+\beta}{2}a_b\right).
 \tag{20}
\]
In particular the selected direction has curvature greater than
\(3\pi(1+\nu)/20\), since \(a_z>3/20\) on
\(P+i[0,.014]\). The outer directions retain their original
allocation. The zero possible index entries in (20) do not negate
the independent strict bound (5).

There are stronger costs on downward index displacements. Because
the heights stay fixed, when \(u_R\le u_{*,R}<.36\) the two
type-four pair remainders each give \(39/160\), while
\(a_u\ge\Re\cot\pi u_*>2/5\). Thus the \(u\) diagonal
in (20) can be replaced by at least \(71/80\) on that region.
For \(v_R\le v_{*,R}\), the corresponding replacement is
\[
 \begin{cases}
 2/5,&\beta=0,\\71/80,&\beta=1.
 \end{cases}
 \tag{21}
\]
For \(\beta=0\), the stronger fixed-height version permits
\(2\min\{\Re\cot\pi v_*,15/53\}\) in place of \(2/5\).
These are joint matrix lower bounds, so they preserve arbitrary
motions in the other coordinates; the equal-height condition is
essential when using the reference cotangent.

The connecting segments from the actual real reference to targets
in (18) remain in that convex product at the stated final heights.
Therefore the costs may be integrated in a centered majorant or
used in the central-budget proof's pair conjugates. No direction
of the unknown optimizing displacement is presumed: (21) applies
only on its stated side of the reference, while (19)--(20) remain
valid on the other side. The fixed-reference vertical cost, the
coupled boundary tangents, and the signs of the resulting scalar
tests still have to be controlled. This is a main/main deduction,
not a full finite-source selected bound.
