# The selected first four/three central profiles on the early interval

Private written proof, 10 November 2026. At the original selected
height, both central Fourier profiles for an actual first four/three
pair remain below their original geometric plane when the first real
coordinate is extended down to one tenth. The proof locates only the
private maximizers on the old left face. Joint concavity then transfers
that face bound to the entire early interval.

The result also bounds the product of the two literal main horizontal
currents, with the complete selected Fourier factor. It does not
estimate the other cap profiles, real ordinary rows or joining and
alias currents outside those two specified main currents.

## 1. Actual reference and original selected alternatives

Fix an actual positive three/four open word of length at least three
beginning with four and three. Retain the original coupled reference
\((e_*,s_*,a_*,b_*)\), its logarithmic lifts and additive phase
normalization. Write
\[
 \Im e_*=h_e\in[-.051,-.019],\qquad
 \Im s_*=h_s\in[-.065,.068],\qquad
 \Im b_*=h_b\in[-.065,.068].
\tag{1}
\]
These are the actual-reference domains in the
[selected finite-source reduction](research_mixed_selected_four_three_finite_reduction.md).
Take
\[
 H=7/625,\quad a=x+iH,\quad b=y+ih_b,\qquad
 x\in[1/10,11/50],\quad y\in P=[11/50,9/20],
\tag{2}
\]
and use the unchanged private main lines
\[
 e=u+ih_e,\quad .27\le u\le.49,\qquad
 s=v+ih_s,\quad .15\le v\le.5.
\tag{3}
\]
The allocated joint phase is exactly
\[
\begin{split}
 \mathcal F(e,s;a,b)={}&S(e)+g(e+a)+g(s+a)+g(s+b)
  -2g(s)-3g(a)-g(b)-g(e)\\
 &-\frac{i\pi}{2}(e-e^2)+2\pi ias.
\end{split}
\tag{4}
\]
Equivalently it is \(\Xi_1(e,a)+F_{10}(s;a,b)\), with
the original two half allocations. Define
\[
 M=\Re\mathcal F(e_*,s_*;a_*,b_*),\qquad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\qquad
 \ell_b(y)=\Re p\,(y-\Re b_*).
\tag{5}
\]
The two central selected upper profiles are
\[
 f_{\rm fac}=\Re\mathcal F-2\pi H,\qquad
 f_{\rm force}=\Re\mathcal F+\Re g(a).
\tag{6}
\]
They bound the same complete Fourier polynomial with its selected
monomial; they are not separate exact finite sources.

**Theorem 1.** On (1)--(3),
\[
              f_{\rm fac}<M+\ell_b(y)-1/500,
 \qquad       f_{\rm force}<M+\ell_b(y)-1/500.
\tag{7}
\]
Every original private main point is included. The other outer
coordinates and their heights remain fixed as stated; no assertion
about a height-changing early contour is made.

## 2. Joint horizontal concavity at the selected height

We first extend the purely algebraic Hessian proof of the
[positive-private-height first-four/three source](research_mixed_early_four_three_positive_private_central.md)
to (1)--(3). This does not import its finite-source comparison at
the unselected first height.

Put
\[
 A=\Re\cot\pi a>0,\quad E=\Re\cot\pi e>0,
 \quad C_e=\Re\cot\pi(e+a).
\]
The original cap Hessian, divided by \(\pi\) after taking its
negative real part, is
\[
 \begin{pmatrix}K&-C_e\\-C_e&\tfrac32 A-C_e\end{pmatrix},
                       \qquad K>2E+3/4-C_e.
\tag{8}
\]
The inequality is the exact endpoint-curvature consequence from the
[joint early-cap theorem](research_mixed_cap_joint_early_horizontal_concavity.md).
Its product domain includes the positive height \(H<.021\).

Its outgoing Schur complement is strictly greater than \(A\).
Here are the same three elementary cases, with their domains checked
at the selected height. If \(C_e\le0\), use \(K>-C_e\).
If \(0<C_e\le1/4\), then \(u+x<1/2\), hence \(x<.23\)
and \(A>1\); consequently
\[
 K(A/2-C_e)-C_e^2>
          (3/4-C_e)(1/2-C_e)-C_e^2\ge1/16.
\]
If \(C_e>1/4\), the real cotangent comparison implies
\(u+x<.43\), so \(u<.33\), \(x<.16\). The original
elementary bounds give \(E>1/2\), \(A>4/3\),
\(C_e<9/20\), and
\[
 K(A/2-C_e)-C_e^2>
                (7/4-C_e)(2/3-C_e)-C_e^2>19/240.
\tag{9}
\]
The estimates for \(A\) in this argument use only
\(|\Im a|\le.07\), not its sign: their denominators are
\(\cosh(2\pi\Im a)-\cos(2\pi x)\). The bounds for
\(E\) use exactly the unchanged private interval (1), and
\(C_e\le\cot\pi(u+x)\) when \(C_e>0\) holds at either
height sign. Thus every case of (8)--(9) remains licensed.

Let \(U=\Re\cot\pi s\), \(C=\Re\cot\pi(s+a)\), and
\(V(s,a)=g(s+a)-g(s)-g(a)\). After eliminating the cap private
direction, the negative real Hessian of
\(\Xi_1+V(s,a)-g(a)/2+2\pi ias\), divided by \(\pi\),
strictly dominates
\[
                   \begin{pmatrix}U-C&-C\\-C&\tfrac52 A-C\end{pmatrix}.
\tag{10}
\]
The chirp has purely imaginary Hessian. If \(C\le0\), this
matrix is positive definite, including \(v=.5\): at that
endpoint \(U=0\) and \(C<0\).

For \(C>0\), set \(u_0=\cot(\pi v)\),
\(p_0=\cot(\pi x)\). The original modulus estimates give
\[
 U>\tfrac45u_0,\quad A>\tfrac{13}{20}p_0,\quad
 C\le\frac{u_0p_0-1}{u_0+p_0},\quad p_0<10/3.
\tag{11}
\]
Indeed the exact ratio to the real cotangent is
\([1+\sinh^2(\pi h)/\sin^2(\pi t)]^{-1}\).
Use \(|h_s|\le.068\), \(v\ge.15\),
\(|H|<.07\), \(x\ge.1\), and the written bounds
\(\sinh(.068\pi),\sinh(.07\pi)<2/9\),
\(\sin(.15\pi)>4/9\), \(\sin(.1\pi)>4/13\).
These bounds are even in each height; the negative part of (1)
does not change them.

The inverse criterion for (10) now reduces to
\[
 \frac5{4u_0}+\frac8{13p_0}
                    <\frac{u_0+p_0}{u_0p_0-1}.
\tag{12}
\]
Its positive-denominator numerator is
\[
 p_0\{(5/13)u_0^2-(p_0/4)u_0+5/4\}+(8/13)u_0>0:
\]
the bracket is greater than
\((5/13)u_0^2-(5/6)u_0+5/4\), whose discriminant is
\(25/36-25/13<0\). This proves strict positivity.
Finally the independent original half-index Hessian of \(V(s,b)\)
is negative in real part on the displayed \(s,b\) domain.
Adding it proves that (4) has a strictly negative real horizontal
Hessian in \((u,v,x)\), for every fixed \(b\) in (2).
Subtracting the constant \(2\pi H\) and the fixed outgoing
affine term preserves this joint concavity.

## 3. Private maximizers on the old left face

Fix \(y\) and maximize \(\Re\mathcal F\) over the private
rectangle (3), now with \(x=11/50\). The original
[optimizer theorem](research_mixed_selected_boundary_optimizer_bounds.md),
Proposition 1, gives
\[
                              u<2/5.
\tag{13}
\]
Its cap derivative bound is established at the larger height
\(7/500\) and is increasing in the first height at this face.
It therefore applies to \(H=7/625\). The ordinary terms and
either correction (6) are independent of \(e\), so their
addition does not change the exclusion. Only this old plateau face,
not an early optimizer extension, is used here.

We next prove the new exclusion
\[
                              v<12/25.
\tag{14}
\]
The real derivative in that coordinate is
\[
 D_s=\Re\{g'(s+a)+g'(s+b)-2g'(s)+2\pi ia\}.
\tag{15}
\]
For \(v\ge.48\), both summed real parts lie in \((1/2,1)\),
where their real cotangents are negative; the real cotangent of
\(s\) is nonnegative. Thus \(D_s\) decreases with \(v\)
and with \(y\). It suffices to bound it at
\(v=.48\), \(x=y=.22\).

Put \(r=e^{2\pi H}\), \(\rho=e^{2\pi h_s}\),
\(t=e^{2\pi h_b}\). We have
\[
                     r\ge1,\qquad 0<\rho,t<31/20.
\tag{16}
\]
For the upper bound, the positive atanh series gives
\(\log(31/20)>22/51>374/875>17\pi/125\).
Let \(\beta=\cos(.4\pi)<1/3\), and note
\(\cos(.04\pi)>99/100\). The latter follows from
\(\cos q\ge1-q^2/2\) and \(.04\pi<22/175\).
In the first numerator of \(e^{D_s}\), divide by its chirp
factor \(r\) before bounding it. The resulting two squared
numerators and denominator satisfy
\[
 e^{2D_s}<
 \frac{(1+\rho^2+2\rho/3)
       (1+961\rho^2/400+31\rho/30)}
      {(1+\rho^2+99\rho/50)^2}.
\tag{17}
\]
For the first factor use \(r^{-1}\le1\) and the negative
cosine at the summed real part \(.70\); for the second use
\(t\le31/20\). Both squared moduli increase with the relevant
positive radial variable in this negative-cosine range.

The denominator minus numerator in (17), divided by \(\rho\),
is strictly greater than
\[
 -561\rho^3/400+53\rho^2/40+9\rho/5+113/50
 >\rho(9/5-17\rho/20)+113/50>0.
\tag{18}
\]
For the first inequality the discarded coefficient of \(\rho\)
is \(2611/90000>0\). For the second use
\(53/40-561\rho/400\ge-6791/8000>-17/20\).
The last bracket is at least \(193/400>0\), by (16).
Hence \(D_s<0\) for every \(v\ge.48\). Decreasing \(v\)
slightly improves the objective, proving (14), including points
on the equality face.

## 4. Positive first-coordinate derivative at each face maximizer

For \(x=.22\), exact differentiation of (4), with the chirp
retained, gives
\[
 \partial_x\Re\mathcal F=\log\frac{N_eN_s}{D^3},\qquad
 \begin{cases}
 N_e=|1-rR e^{-2\pi i(u+x)}|,&R=e^{2\pi h_e},\\
 N_s=|q-r e^{-2\pi i(v+x)}|,&q=e^{-2\pi h_s},\\
 D=|1-r e^{-2\pi ix}|.&
 \end{cases}
\tag{19}
\]
The actual bounds imply
\[
 R>18/25,\quad q>13/20,\qquad 1\le r<43/40.
\tag{20}
\]
The first two are the original elementary radius guards in the
first-four/three source. For the last,
\(\log(43/40)>6/83>44/625>14\pi/625\).

At every maximizer, (13)--(14) yield
\(u+x\in[.49,.62)\), \(v+x\in[.37,.70)\). Therefore
\[
 \cos2\pi(u+x)<-18/25,\qquad
 \cos2\pi(v+x)<-3/10,\qquad
 \cos2\pi x>14/75.
\tag{21}
\]
For the first guard it suffices that \(\cos(6\pi/25)>18/25\).
Writing \(q_0=6\pi/25\), one has \(3/4<q_0<19/25<4/5\),
so the alternating cosine lower bound gives
\[
 \cos q_0>1-361/1250+27/2048-1/2000>18/25.
\]
Here \(27/2048>1/100>11/1250+1/2000\).
The second guard follows from
\(\cos(2\pi/5)=(\sqrt5-1)/4>3/10\).
The last is the original cubic-sine bound at \(.06\pi\).
Using (20)--(21), put
\[
\begin{split}
 N_e^2&>A=1+324r^2/625+648r/625,\\
 N_s^2&>C=r^2+39r/100+169/400,\\
 D^2&<B=1+r^2-28r/75.
\end{split}
\tag{22}
\]

**Lemma 2.** \(AC-B^3>0\) for \(1\le r\le43/40\).

*Proof.* Set
\(a=324/625\), \(b_1=648/625\), \(c_1=39/100\),
\(d_1=169/400\), \(e_1=28/75\), and \(P=AC-B^3\).
Differentiating its exact polynomial expansion gives
\[
\begin{split}
 P''={}&-30r^4+60e_1r^3+12(a-3-3e_1^2)r^2\\
 &+6(b_1+ac_1+6e_1+e_1^3)r
                      +2(b_1c_1+ad_1-2-3e_1^2).
\end{split}
\tag{23}
\]
It is strictly negative on the interval. Indeed use
\(e_1<3/8\), \(a<21/40\), \(b_1<21/20\),
\(c_1<2/5\), \(d_1<17/40\), and \(r<11/10\).
The four groups on the right side of (23), with the first two
monomials grouped together, are respectively bounded above by
\(-15/2,-29,24,-2\). Their sum is negative.
For the positive group, use
\(e_1^3<3/50\), so its inner parenthesis is below
\(21/20+21/100+9/4+3/50=357/100\).
For the last group, \(b_1c_1+ad_1<1\) suffices.

At \(r=1\), \(AC>9/2\), whereas
\(B=122/75<49/30\) and \((49/30)^3<9/2\).
At the other endpoint the exact values are
\[
 A=678409/250000,\quad C=15979/8000,\quad B=42103/24000,
\]
and their difference is
\[
 P(43/40)=
       \frac{293721878105}{13824000000000}>0.
\tag{24}
\]
Strict concavity and the two positive endpoints prove the lemma.
\(\square\)

Equations (19), (22) and Lemma 2 prove that every private maximizer
on \(x=.22\) has strictly positive first-coordinate derivative.
There is no selection of a new critical phase branch in this test.

## 5. Transport by a supporting tangent, and the actual Fourier bound

For each fixed \(b\), choose a private maximizer \((u_b,v_b)\)
of (4) at \(x_0=.22\). Its first-order optimality on the private
rectangle gives
\[
 f_u(u-u_b)+f_v(v-v_b)\le0
\]
for every private target in (3), where \(f=\Re\mathcal F\)
and these derivatives are evaluated at the maximizer. Joint concavity
from Section 2 supplies its global supporting tangent. Consequently
\[
 f(u,v,x)\le f(u_b,v_b,x_0)+f_x(x-x_0)
                             \le f(u_b,v_b,x_0)
                         \qquad(.1\le x\le x_0),
\tag{25}
\]
by Section 4. This proof also covers a maximizer on an original
private face. It assumes neither an interior maximizer nor a
differentiable branch of maximizing points as \(x\) changes.

The [original selected central gap](research_mixed_first_four_next_three_central_gap.md),
Theorem 1, applies at the old face \(x_0\), for the same actual
reference and every \(y\in P\). It bounds its factorial profile
by \(M+\ell_b(y)-1/500\). Subtracting the constant \(2\pi H\)
from (25) proves the first assertion of (7).

The original scalar branch comparison,
[equation (8)](research_mixed_selected_minimum_flow_obstruction.md),
is
\[
 -\Re g(x+ih)-2\pi h>3/40
       \qquad(.1\le x\le.22,\quad0\le h\le7/500).
\tag{26}
\]
It is a scalar inequality for the same primitive, independently of
the cyclic application in which it was first used. At our height it
implies \(f_{\rm force}<f_{\rm fac}-3/40\). Thus the first
assertion pays the second one as well. No force-specific early
Hessian is needed. This proves Theorem 1.

## 6. Consequence for the two literal main currents

Let \(U_N^{\rm hor}(w,X)\) and \(C_N^{\rm hor}(X,Y)\)
be the actual zero-mode horizontal currents defined in the selected
finite reduction, with their original \(+N\) coefficients and
half-grid cuts tending respectively to \([.27,.49]\) and
\([.15,.5]\). Keep the heights \(h_e,h_s\),
\(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\).
Their exact factorial interpolants remain valid throughout (2):
the real parts of \(e+a,s+a,s+b\) stay in the compact intervals
\([.37,.71],[.25,.72],[.37,.95]\), respectively. All unshifted
arguments likewise stay in their original regular strips. The
complete endpoint coefficient in the cap is kept intact, on its
existing ordinary-color neighborhood.

**Corollary 3.** For every \(\tau>0\), both parities and every
fixed ordinary-color derivative order \(k\) obey
\[
 \left|\partial_w^k\{
 U_N^{\rm hor}(w,X)C_N^{\rm hor}(X,Y)d_N(X)X^{-N}\}\right|
 \le C_{\tau,k}N^{A_{\tau,k}}
              e^{N\{M+\ell_b(y)-1/500+\tau\}}
\tag{27}
\]
on a sufficiently small fixed ordinary-color disk about \(-2\),
uniformly on (2).

*Proof.* The exact current symbols and the complete endpoint
coefficient have the original compact-domain upper bounds in the
finite reduction. Equation (7) bounds their joint main phase.
The [complete Fourier theorem](research_mixed_fourier_weight_continuation.md)
retains the upper rate
\(\max\{-\Re g(a)-2\pi H,0\}\) for the whole
\(d_N(X)X^{-N}\). These are precisely the two alternatives
in (6), and (26) selects their larger bound on the early interval.
Compact integration, both original \(N\) densities, symbol factors
and half-grid displacements cost a polynomial and an arbitrarily
small total tolerance. The complete endpoint coefficient is uniform
on a fixed ordinary-color disk; shrink it as needed to absorb its
phase variation in that same tolerance. Cauchy's formula on a smaller
disk proves the derivative assertion. No pointwise remainder is
replaced by an independent asymptotic source. \(\square\)

This corollary concerns only the displayed product of defined main
currents. The real cap cuts, aliases and true cap ends; the ordinary
real rows, aliases and zero-mode joins; and selected or moving-height
outer boundary pieces remain separate finite-source estimates.
There is no complete selected early-pair, whole-word, closed-knot or
short-partial-filling conclusion here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_boundary_optimizer_bounds.md | 13fa176cf8f50054bc2c47e479f85daf0ecb9b22a68d316689ad752f8ca2b603 |
| research_mixed_selected_four_three_finite_reduction.md | 732d6cbf79894cb1e230e4eefa27762e369d84127d67e9e7c0d66c77901bbd42 |
| research_mixed_first_four_next_three_central_gap.md | 395acbb50020c86e79164d594ef959c546cdb016da6c49276b39331fcdb59e37 |
| research_mixed_early_four_three_positive_private_central.md | b8ffb45bbb9eae0d144b0c2e219207509aa7a119543560b058dfca1734e7c289 |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_selected_minimum_flow_obstruction.md | 52c6bf13beb1a98b69c2f834223f017dcb2acb27b406cf5cb270947ef2d14963 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The complete written proof and directly used source implications were
read. No new mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.
