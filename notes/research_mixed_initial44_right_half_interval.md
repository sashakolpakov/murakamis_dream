# The complete first four/four pair up to the right half endpoint

Private written proof, 10 November 2026. The unselected first pair
remains exponentially smaller than its original geometric affine rate
when the first real coordinate moves from \(9/20\) to \(1/2\), at
its actual negative height. The adjacent coordinate stays on its full
plateau at its actual height. The proof transports the physical-row
bounds jointly with the cap, and extends the horizontal concavity
needed for the central integral. Every finite row and contour term is
retained. This does not pay the subsequent right interval or a change
of the first height.

## 1. Reference, literal source and statement

Fix an actual positive three/four open word of length \(m\ge3\)
beginning with four and four. Write its original first retained,
second retained, cap private and ordinary private references as

\[
 a_*=a_0+ic,\quad b_*=b_0+id,\quad
 e_*=u_*+ih_e,\quad s_*=v_*+ih_s.
\]

Use the original primitive
\[
 J'(q)=\operatorname{Log}(2\sin\pi q),\quad J(0)=0,\qquad
 g(q)=J(q)+\frac{i\pi}{2}(q-q^2).
\]
The logarithms continue from the positive real sine chamber.
The original endpoint and ordinary image bounds give

\[
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 -.051<h_e<-.019,\quad -.108\le h_s<0,\quad
 -.102\le d\le-.001.
\tag{1}
\]

The real ordinary reference belongs to the old plateau, as do both
retained real reference coordinates. These bounds refer to the same
coupled reference, including the length-three case. Put

\[
 a=x+ic,\quad b=z+id,\qquad
 9/20\le x\le1/2,\quad z\in P=[11/50,9/20].
\tag{2}
\]

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and

\[
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad
 p_j(X)=(q_NX;q_N)_j,
\]

retain the complete original functions

\[
 U_{1,N}(w,X)=\sum_{i=0}^{N-1}
       H_N(w,q_N^{-i})\frac{p_i(X)}{P_i^2},\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
\]
\[
 K_N(w;a,b)=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X).
\tag{3}
\]

The outside allocation is \(|d_N(Y)|^{1/2}\). No selected first
monomial occurs. The degree-\((N-1)\) polynomial \(d_N\) retains its
original forcing. Let \(L_1\) and \(\phi\) be the original allocated
cap and ordinary phases, respectively. Set

\[
\begin{split}
 \kappa&=1/2500000,\qquad \kappa_R=8\kappa/9,\qquad
 \delta_R=\kappa(9/20-a_0)^2,\\
 \Lambda(z)&=\Re\{L_1(a_*)+\phi(a_*,b_*)\}
            +\Re\partial_b\phi(a_*,b_*)(z-b_0).
\end{split}
\tag{4}
\]

In particular \(\delta_R>\kappa/100>0\). The original stationary
equation is \(L_1'(a_*)+\partial_a\phi(a_*,b_*)=0\).

**Theorem 1.** For every \(\tau>0\), the whole finite pair satisfies

\[
 |K_N(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
 e^{N\{\Lambda(z)-\kappa_R(z-b_0)^2-\delta_R+\tau\}}
\tag{5}
\]

on (2), for both level parities and all real \(w\in[-2,2]\).
The same bound holds on sufficiently small fixed ordinary-color disks
at any prescribed total allowance, with fixed derivatives on smaller
disks. Its horizontal integral, with the original measure and outside
scalar, has the same exponential bound.

## 2. The ordinary main integral retains its supporting plane

The allocated phase is

\[
 F(s;a,b)=g(s+a)+g(s+b)-3g(s)-\tfrac32g(a)
                -\tfrac32g(b)+2\pi ias,
\tag{6}
\]

where \(g''(q)=\pi\cot(\pi q)-\pi i\), on the original lifts.
The [half-index theorem](research_mixed_half_index_contour.md) and
[smaller-cut theorem](research_mixed_four_left_cut_extension.md)
prove \(-\Re F''\succeq2\kappa I\) when both real outer
coordinates lie in \(P\) and \(1/8\le\Re s\le1/2\), at the
stated small heights. We need a nonnegative Hessian on the added strip.

First consider \(V(s,a)=g(s+a)-g(s)-g(a)\), and write

\[
 \cot\pi s=u+iv,\qquad \cot\pi a=p+i\beta.
\]

For \(1/8\le\Re s\le1/2\), \(-.108\le\Im s\le0\),
and (2), one has \(u,p\ge0\), \(v,\beta\ge0\). The exact pair
determinant is

\[
 \det(-\Re V''/\pi)
 =\frac{(u+p)^2-(pv-u\beta)^2}
        {(u+p)^2+(v+\beta)^2}.
\tag{7}
\]

On the added outer strip, \(p<4/25\) and \(\beta<2/5\).
For explicit bounds, \(p\le\tan(\pi/20)<4/25\), using

\[
 \tan t\le t/(1-t^2/2),\qquad t<11/70.
\]

The imaginary cotangent increases with the absolute height on this
strip, because \(1-\cos(2\pi x)\cosh(2\pi c)>0\).
The larger containing range \(|c|\le3/25\) gives

\[
 |\Im\cot\pi a|
 \le\frac{\sinh(6\pi/25)}{\cosh(6\pi/25)+\cos(\pi/10)}
 <\frac25.
\tag{8}
\]

One may prove the last inequality without evaluation: its left side
is at most \(\tanh(3\pi/25)/\cos(\pi/10)\), by

\[
 \cosh t+\cos\theta\ge\cos\theta(\cosh t+1).
\]

Then \(\tanh t<t\), \(\cos(\pi/10)>19/20\), and

\[
 (3\pi/25)(20/19)<264/665<2/5
\]

give (8). The cosine bound follows from

\[
 \cos(\pi/10)>1-\tfrac12(11/35)^2=2329/2450>19/20.
\]

If \(\Re s\ge1/6\), then \(v<1\). In fact the imaginary
cotangent formula gives this as soon as

\[
 \cos(2\pi\Re s)<e^{-2\pi|\Im s|}.
\]

The left side is at most \(1/2\); the right side is greater than
\(1/2\), since \(.216\pi<17/25<\log2\).
For the last comparison use the positive atanh series

\[
 \log2>2/3+2/81=56/81>17/25.
\]

Hence \(|pv-u\beta|<p+u\) whenever \(u+p>0\).
If \(1/8\le\Re s\le1/6\), the elementary bounds in the
half-index and smaller-cut proofs instead give

\[
 u>14/15,\qquad v<3/2.
\tag{9}
\]

Indeed \(\sin(2\pi\Re s)>7/10\),
\(\cosh(.216\pi)<5/4\), and \(\cos(2\pi\Re s)\ge1/2\)
give the first. The imaginary part is largest at \(\Re s=1/8\)
and \(|\Im s|=.108\); the written bounds

\[
 \sinh(.216\pi)<3/4,\quad
 \cosh(.216\pi)>123/100,\quad \sqrt2/2<71/100
\]

give \(v<(3/4)/(13/25)<3/2\). They are precisely the positive
series bounds used in the half-index proof. Thus

\[
 |pv-u\beta|<\tfrac32p+\tfrac25u<u+p,
\]

because \(p/2<2/25<3u/5\). Equation (7), together with the usual
pair diagonal entries, proves \(-\Re V''\succeq0\). To see their
signs directly, if \(C=\Re\cot\pi(s+a)\), then \(C\le0\)
because \(1/2<\Re(s+a)\le1\). The pair matrix has diagonal
\(u-C,p-C\ge0\). At \(s=a=1/2\) in real part it may be
semidefinite. On a strict substrip with \(\Re(s+a)<1\), it is
positive definite.

For \(\Re s\ge3/20\), the old pair theorem makes
\(-\Re V(s,b)''\) positive definite. The remaining terms
\(-g(s),-g(a)/2,-g(b)/2\) have nonnegative negative real
Hessians, and the chirp has zero real Hessian. For
\(1/8\le\Re s\le3/20\), use the smaller-cut proof directly.
Writing \(q=\Re\cot\pi b\), \(C_b=\Re\cot\pi(s+b)\),
its estimates give

\[
 u>21/20,\quad D_b=3q/2-C_b>0,\qquad
 C_b+C_b^2/D_b\le187/120.
\]

The \((s,b)\) Hessian of \(V(s,b)-g(s)-g(b)/2\) therefore has
Schur complement greater than

\[
 2(21/20)-187/120=13/24>0.
\]

Adding the nonnegative \((s,a)\) pair proves the required
\(-\Re F''\succeq0\) on the added strip, also when the private
height runs between its actual value and zero. All denominators used
here are nonzero on any fixed right index cut below \(1/2\).

Let \(s=t+ih_s\) on that fixed main line. Integrate the real Hessian
along the straight segment from \((s_*,a_*,b_*)\) to \((s,a,b)\).
Until the first real outer coordinate reaches \(9/20\), the old
bound is \(2\kappa I\). The fraction of this segment so traversed is

\[
 \theta_0=\frac{9/20-a_0}{x-a_0}\ge\frac23.
\]

The rest has nonnegative negative Hessian. The Taylor integral hence
retains coefficient at least

\[
 2\kappa\int_0^{2/3}(1-t)\,dt=8\kappa/9=\kappa_R.
\]

The private derivative at the original reference is zero. Consequently

\[
 \Re F(t+ih_s;a,b)\le B_R(x,z),
\tag{10}
\]

where

\[
 B_R(x,z)=\Re\phi(a_*,b_*)+
 \Re\phi_a(a_*,b_*)(x-a_0)+\Re\phi_b(a_*,b_*)(z-b_0)
 -\kappa_R\{(x-a_0)^2+(z-b_0)^2\}.
\tag{11}
\]

The discarded private quadratic is favorable. The original primitive,
constant and marginal have not been replaced by those of a new root.

## 3. Joint transport of the physical rows

The [complete cap theorem through one half](research_mixed_cap_upper_target_completion.md)
bounds its five regular profiles and its true ends throughout (2).
Its allocated plane is

\[
 B_L(x)=\Re L_1(a_*)+\Re L_1'(a_*)(x-a_0)
                              -\kappa(x-a_0)^2.
\tag{12}
\]

For a fixed regular cap point \(e\in[.27,.49]+i[-.055,.04]\),
write its bare rate as \(\Re\Psi(e,a)-p_e\), with the original
alias penalty \(p_e\), where
\[
 \Psi(e,a)=S(e)+J(e+a)-J(a)-i\pi ea-g(e)
\]
and \(S(e)\) is the original action of the complete endpoint coefficient.
The five profile sets are the main line at height \(h_e\), the two
real cuts \(.27,.49\), and the horizontal aliases at heights
\(-.055,.04\) with penalties \(.11\pi,.08\pi\).
Include the separate bare true-end ceiling

\[
 A_*=3/5+\log4/100.
\tag{13}
\]

This ceiling is valid here by the true-end calculation in the cap
theorem: it is larger than its displayed negative-height ceiling.
It is still strictly below its bare plane \(B_T>149/200\).
The same outgoing-halfweight convexity in that theorem therefore
pays (13) by (12). Thus this harmless common ceiling may be used at
both the old and new targets.

For the ordinary physical rows use the exact continuous rate

\[
 E(t;a,b)=\int_0^t\log|1-e^{-2\pi i(a+u)}|\,du
       +\int_0^t\log|1-e^{-2\pi i(b+u)}|\,du
                         -3J(t)-2\pi ct.
\tag{14}
\]

Put \(r=e^{2\pi c}<1\), \(D=|1-re^{-2\pi ix}|\),

\[
 N_e=|1-re^{2\pi\Im e}e^{-2\pi i(x+\Re e)}|,
 \qquad N_t=|1-re^{-2\pi i(x+t)}|.
\]

Since \(e^{.08\pi}<4/3\) and \(\cos2\pi x<-19/20\),

\[
 N_e<1+4r/3<D^2.
\tag{15}
\]

The exponential bound follows from \(.08\pi<2/7<\log(4/3)\).
For \(1/8\le t\le1\) and \(9/20\le x\le1/2\),

\[
 1-2x\le t\le1,\qquad
 \cos2\pi(x+t)\ge\cos2\pi x,\qquad N_t\le D.
\tag{16}
\]

The second inequality follows by following the cosine from \(1-x\)
through \(1\) to \(1+x\). It includes every numerator wall.

The first height is negative, and \(\Re g(a)\le0\) until \(x=1/2\).
The whole first Fourier upper rate is therefore \(-\Re g(a)\).
Both alternatives coincide at the half endpoint. The outgoing half
rate remains \(-\Re g(b)/2\). Exact differentiation of the joint
regular-cap and row rate gives

\[
 \partial_x\{\Re\Psi(e,a)-p_e+E(t;a,b)
                  -\Re g(a)-\tfrac12\Re g(b)\}
                   =\log(N_eN_t/D^3)<0.
\tag{17}
\]

The chirp \(-2\pi ct\) has been retained and is independent of
this real displacement. For a true cap end the derivative instead is

\[
 \log(N_t/D^2)\le-\log D<0.
\tag{18}
\]

All regular penalties are constant in \(x\). Hence these inequalities
transport every individual high-row and real-cut profile from \(x=9/20\)
to the whole new interval. No assertion about the monotonicity of a
signed finite sum is being made.

At \(x=9/20\), the complete ordinary support theorem proves its
physical-row comparisons before finite summation. In particular its
left cut \(1/8\), half row, last row and intervening high rows are
below the original allocated ordinary plane. Adding the cap profiles
and cancelling the first marginals gives

\[
 \Lambda(z)-\kappa(z-b_0)^2-2\delta_R
\tag{19}
\]

for every high row \(t\in[1/2,1]\) and the left cut. This uses the
real-rate implications in Section 2 of
[ordinary source assembly](research_mixed_three_row_source_assembly.md),
not a bound on absolute rows inferred from a signed kernel estimate.

By continuity of the integrated physical rates on the compact actual
family, there is a fixed \(0<\varepsilon<1/100\) such that (19),
with \(2\delta_R\) replaced by \(3\delta_R/2\), also holds for
every \(t\in[1/2-2\varepsilon,1/2]\). Indeed the old uniform
reserve is at least \(2\kappa/100\); use less than half the lower
bound \(\kappa/100\) in choosing the collar. The zero-safe rate
continuity includes moving numerator zeros. Choose the new right
index cut \(r_0=1/2-\varepsilon\). Equations (17)--(18) transport
this whole collar and the high interval, with the unchanged gap.

The low physical rows are bounded by the left cut. For \(0<t\le1/8\),
their exact continuous ratio is

\[
 e^{E_t}=\frac{|1-re^{-2\pi i(x+t)}|
                       |1-e^{2\pi d-2\pi i(z+t)}|}
                  {r(2\sin\pi t)^3}>1.
\tag{20}
\]

For the first numerator divided by \(r\), use
\(\cos2\pi(x+t)<0\), giving a value greater than one.
For the second, \(z+t\in[.22,.575]\) has cosine less than
\(1/5\); minimization over its positive radius gives squared
modulus greater than \(24/25\). Finally
\(2\sin(\pi/8)<4/5\). These bounds prove (20) with a uniform
strict reserve. Integration gives \(E(t)\le E(1/8)\), including
the limiting endpoint zero. Thus all low rows also have the
transported real-cut comparison.

## 4. Every central contour correction

Use
\[
 L_N=\lfloor N/8\rfloor+1,\quad K_N=\lceil Nr_0\rceil,\qquad
 \ell_N=(L_N-1/2)/N,\quad u_N=(K_N-1/2)/N.
\]
For all sufficiently large levels these are ordered half-grid cuts
tending to \(1/8,r_0\). Let \(\mathcal R_N\) have those vertical
sides, lower height \(-1/5\), and upper height \(5/4\). The original
interpolation and its exact contour identity are

\[
 \begin{split}
 T_N(s)&=e^{2\pi iNas}
 \frac{\widehat P_N(N(s+a))\widehat P_N(N(s+b))}
 {\widehat P_N(Ns)^3\widehat P_N(Na)\widehat P_N(Nb)},\\
 \sum_{j=L_N}^{K_N-1}
    \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}
 &=\frac{N}{2i}\oint_{\partial\mathcal R_N}^{\rm CCW}
                 \cot(\pi Ns)T_N(s)\,ds .
 \end{split}
\tag{21}
\]

Every real factorial argument lies in a fixed compact subinterval
of \((0,1)\), because \(a+s\) has real part at most \(1-\varepsilon\).
The original factorial theorem permits all these bounded imaginary
heights. The unchanged cotangent residue formula gives zero-mode
density \(+N\), both horizontal aliases and four vertical halves.

Let \(Q_s=F_s\), since allocations do not depend on \(s\).
The elementary original logarithmic argument bounds give, at every
finite private height,

\[
 -33\pi/20<\Im Q_s<131\pi/100.
\tag{22}
\]

For completeness, write \(s=v+iy\), with \(1/8\le v\le r_0\).
The first shifted argument \(x+v>1/2\) is always in the upper
real half of its regular strip. If \(z+v\ge1/2\), the lower
bound divided by \(\pi\) is \(-1+2v-2z\ge-33/20\),
and the upper bound is \(2x\le1\). If \(z+v<1/2\),
they are \(-2+4v\ge-3/2\) and
\(1-2v-2z+2x\le131/100\). These come from

\[
 \pi\min(1-2t,0)\le
 \arg(1-e^{2\pi h-2\pi it})\le
 \pi\max(1-2t,0),
\]

with the original carrier \(2\pi x\), not a reset product argument.

Comparison with the main height \(h_s\in[-.108,0]\), including
the full alias penalties, now yields

\[
\begin{split}
 \Re F(v-i/5)-2\pi/5
       &<\Re F(v+ih_s)-69\pi/500,\\
 \Re F(v+5i/4)-5\pi/2
       &<\Re F(v+ih_s)-2593\pi/10000.
\end{split}
\tag{23}
\]

For the second use
\((33/20)(5/4+27/250)-5/2=-2593/10000\).
Both aliases therefore lie below (11). Multiplying by the complete
allocated cap plane (12) and cancelling marginals gives a rate
at most

\[
 \Lambda(z)-(\kappa+\kappa_R)(x-a_0)^2
                                      -\kappa_R(z-b_0)^2.
\tag{24}
\]

The same bound controls the main current. It is strictly stronger
than the exponent in (5).

On the upper and lower vertical alias halves, (22) gives respectively

\[
 \partial_y(\Re F-2\pi y)<-7\pi/20,
 \qquad \partial_y(\Re F+2\pi y)>69\pi/100.
\tag{25}
\]

Each is bounded by its real cut. The two unweighted joins run from
zero to \(h_s\). Section 2 gives \(\Re F_{ss}<0\) there, so their
real rates are convex in the private height. Their endpoints are
bounded by the main comparison (24) and the real-cut comparisons
in Section 3. This includes the new cut \(r_0\) and its small
half-grid displacement.

The cap is independent of this private height. Its complete profile
envelope can therefore be multiplied into each of the comparisons
just made. All original cap aliases, joins, physical tails and true
ends were retained before this multiplication.

## 5. Finite assembly and exact scope

Partition the original ordinary rows at the half-grid cuts in
Section 4. The low and high blocks are bounded by their complete
zero-safe physical rates from Section 3. The central block has its
literal contour identity (21), and every term was bounded in
Section 4. There are at most \(N\) physical rows. The symbols,
contour lengths and half-grid displacements cost polynomial factors
and one prescribed arbitrarily small rate allowance. Both midpoint
parities, the original last index, and all numerator zeros remain.

The high and cut comparison has rate at most
\(\Lambda-\kappa(z-b_0)^2-3\delta_R/2\); the main comparison
is (24). Both imply (5), since \(\kappa_R<\kappa\),
\(x-a_0\ge9/20-a_0>0\), and \(\kappa+\kappa_R>\kappa\).
The complete Fourier bound supplies precisely the two first halves
and the outgoing half already used. No finite Fourier value or
cap coefficient is divided out.

All cap bounds hold for every real ordinary color. The exact
polynomial has degree less than \(N\) in that color, so the
[polynomial continuation theorem](research_mixed_horizontal_complex_extension.md)
gives fixed disks with arbitrarily small added rate allowance.
Cauchy's formula gives fixed derivatives on smaller disks.
The literal increasing horizontal measure and its external scalar
are unchanged. This proves Theorem 1.

The conclusion is a complete first-pair upper bound on (2), with
an actual neighboring plateau variable. It extends the unselected
first-coordinate horizontal path to \(1/2+ic\). It does not
control the selected path, a height-changing right connector,
the subsequent interval to one, or later coordinate departures.
No whole-word or knot conclusion follows from this estimate alone.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_four_left_cut_extension.md | b8a496417f6c6b619508d2ad644eaef47d7fd4408d412bc28a3e92b09d98b96b |
| research_mixed_cap_upper_target_completion.md | 49292f204a86e08c48c5aa8fd29f98103f38a939bb88d523afdd8be741650c22 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

This proof uses written inequalities and unchanged source statements.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or edit of a frozen source was performed.
