# The selected first four/four central profiles on the early interval

Private written proof, 10 November 2026. The two central selected
profiles for an actual first four/four pair keep their original gap
when the first real coordinate extends from the plateau to one tenth.
The extra private factorial supplies the required curvature down to
the original cut \(1/8\). The proof holds the outgoing coordinate
fixed; it does not assert a new joint Hessian in that coordinate.

Only the two literal main horizontal currents are bounded here.
Their complementary finite contours and rows remain separate.

## 1. Actual reference and statement

Fix an actual positive three/four word of length at least three whose
first two types are four. Retain the coupled reference and original
phase from the [next-four central theorem](research_mixed_first_four_next_four_central_gap.md).
The actual private and outgoing heights obey
\[
 h_e\in[-.051,-.019],\qquad h_s,h_b\in[-.108,-.001].
\tag{1}
\]
The enlarged written height intervals contain the sharper actual
intervals of that theorem; the reference is not released from its
coupled equations. Set
\[
 \begin{gathered}
 H=1/100,\qquad a=x+iH,\quad b=y+ih_b,\qquad
 x\in[1/10,11/50],\quad y\in P=[11/50,9/20],\\
 e=u+ih_e,\quad u\in[.27,.49],\qquad
 s=v+ih_s,\quad v\in[1/8,1/2].
 \end{gathered}
\tag{2}
\]
The original allocated phase is
\[
\begin{split}
 \mathcal F_4(e,s;a,b)={}&S(e)+g(e+a)+g(s+a)+g(s+b)
 -3g(s)-3g(a)-\tfrac32g(b)-g(e)\\
 &-\frac{i\pi}{2}(e-e^2)+2\pi ias.
\end{split}
\tag{3}
\]
All primitive branches and additive constants are unchanged. Put
\[
 M=\Re\mathcal F_4(e_*,s_*;a_*,b_*),\qquad
 p=(\mathcal F_4)_b(e_*,s_*;a_*,b_*),\qquad
 \ell_b(y)=\Re p\,(y-\Re b_*).
\tag{4}
\]

**Theorem 1.** Throughout (1)--(2), with the actual reference as
specified, both central selected alternatives satisfy
\[
 \Re\mathcal F_4-2\pi H<M+\ell_b(y)-1/500,
 \qquad
 \Re\mathcal F_4+\Re g(a)<M+\ell_b(y)-1/500.
\tag{5}
\]
The private intervals, outgoing allocation and fixed heights in
this statement are the original ones. In particular this is not
a comparison along a height-changing early taper.

## 2. Joint concavity with the outgoing coordinate fixed

Write
\[
 A=\Re\cot\pi a,\quad U=\Re\cot\pi s,\quad
 C=\Re\cot\pi(s+a),\quad C_b=\Re\cot\pi(s+b).
\]
The cap Schur calculation in Section 2 of the
[selected four/three early theorem](research_mixed_selected_four_three_early_central.md)
uses only the cap heights and \(|\Im a|<.07\).
It therefore applies at the smaller height \(H=1/100\): the
negative real cap Hessian is positive, and its outgoing Schur
complement, after division by \(\pi\), is strictly greater than
\(A\). The same source gives
\[
 A>\frac{13}{20}p_0,\qquad p_0=\cot\pi x>0.
\tag{6}
\]

For \(u_0=\cot\pi v>0\), the exact cotangent ratio and (1) give
\[
 U>u_0/2\qquad(v<1/2).
\tag{7}
\]
Here the lowest allowed real index is \(1/8\). To verify its
height guard without evaluation, use
\[
 \sinh(27\pi/250)<\sinh(17/50)
 \le\frac{17/50}{1-(17/50)^2/6}
 =\frac{5100}{14711}<\frac9{25}<\frac38<\sin(\pi/8).
\tag{8}
\]
The geometric series bounds the positive sinh series, because every
successive ratio after its first term is at most \(t^2/6\).
The last inequality follows from
\(\sin^2(\pi/8)=(2-\sqrt2)/4>9/64\), using
\(\sqrt2<23/16\). For all \(v\in[1/8,1/2]\),
\(\sin\pi v\ge\sin(\pi/8)\). Thus the exact ratio
\([1+\sinh^2(\pi h_s)/\sin^2(\pi v)]^{-1}\)
is greater than one half, proving (7).

Decompose (3), with the same allocated cap \(\Xi_1\), as
\[
 \Xi_1(e,a)+V(s,a)-g(s)-g(a)/2+2\pi ias
                         +V(s,b)-g(b)/2,
 \qquad V(s,a)=g(s+a)-g(s)-g(a).
\tag{9}
\]
After eliminating the cap-private direction, the negative real
Hessian of the first group in (9), divided by \(\pi\),
strictly dominates
\[
 \begin{pmatrix}2U-C&-C\\-C&\tfrac52 A-C\end{pmatrix}.
\tag{10}
\]
If \(C\le0\), this matrix is positive definite; at \(v=1/2\),
one has \(U=0\) but \(C<0\). If \(C>0\), use
\[
 C\le\frac{u_0p_0-1}{u_0+p_0},\qquad
 \frac1{2U}+\frac1{(5/2)A}
 <\frac1{u_0}+\frac8{13p_0}
 <\frac{u_0+p_0}{u_0p_0-1}.
\tag{11}
\]
For the last inequality its positive-denominator numerator is
\((5/13)u_0^2p_0+p_0+(8/13)u_0>0\).
This is exactly the inverse criterion for (10).

Since \(b\) is fixed, the remaining pair \(V(s,b)\) adds only
the \(v,v\) entry \(U-C_b\) to this real Hessian. That entry
is positive on the whole interval, including the newly used
portion below \(.15\). If \(C_b\le0\), the assertion is
immediate, also at \(v=1/2\). If \(C_b>0\), put
\(p_b=\cot\pi y<4/3\). The real cotangent addition formula
gives
\[
 C_b\le\frac{u_0p_b-1}{u_0+p_b}<u_0/2<U.
\tag{12}
\]
Indeed \(u_0^2-p_bu_0+2>0\), since its discriminant is
\(p_b^2-8<0\). For the coarse bound \(p_b<4/3\),
use \(.22\pi>33/50\) and
\(\tan t>t+t^3/3\): at \(t=33/50\) the latter polynomial
is \(283437/375000>3/4\). The tangent bound follows by
integrating \(\tan' t=1+\tan^2t>1+t^2\).
No two-variable pair estimate with a freely varying \(b\) has
been used in (12). Consequently (3) is strictly jointly concave
in the real variables \((u,v,x)\), for every fixed \(b\) in (2).

## 3. The first-coordinate derivative at the old left face

Fix \(b\), put \(x=11/50\), and maximize (3) over its original
private rectangle. The pointwise exclusions in Propositions 1--2 of
the [selected optimizer theorem](research_mixed_selected_boundary_optimizer_bounds.md)
give, for every such maximizer,
\[
                         u<2/5,\qquad v<11/25.
\tag{13}
\]
Those exclusions hold at every fixed outgoing point: decreasing the
corresponding private coordinate is their strict improvement. Their
height range includes the present \(H\), and the ordinary own type
is four as required there.

As in the early four/three theorem, exact differentiation, including
the incoming chirp, gives
\[
 \partial_x\Re\mathcal F_4=\log\frac{N_eN_s}{D^3},\qquad
 \begin{cases}
 N_e=|1-rR e^{-2\pi i(u+x)}|,&R=e^{2\pi h_e}>18/25,\\
 N_s=|q-r e^{-2\pi i(v+x)}|,&q=e^{-2\pi h_s}>1,\\
 D=|1-r e^{-2\pi ix}|,&1<r=e^{2\pi H}<43/40.
 \end{cases}
\tag{14}
\]
At these maximizers, \(u+x\in[.49,.62)\) and
\(v+x\in[.345,.66)\). The written cosine bounds from the
early four/three theorem and the strict inclusion of the latter
interval in \((1/3,2/3)\) yield
\[
 \cos2\pi(u+x)<-18/25,\qquad
 \cos2\pi(v+x)<-1/2,\qquad
 \cos2\pi x>14/75.
\tag{15}
\]
It follows that
\[
 \frac{N_e^2}{r}>\frac1r+\frac{324}{625}r+\frac{648}{625}
 >\frac{40}{43}+\frac{972}{625}>\frac{12}{5}>\frac94,
 \qquad
 \frac{N_s^2}{r}>\frac{q^2}{r}+r+q\ge3q>3.
\tag{16}
\]
On the other hand, \(r+1/r\) increases for \(r\ge1\), so
\[
 \frac{D^2}{r}<r+\frac1r-\frac{28}{75}
 \le\frac{3449}{1720}-\frac{28}{75}<\frac{49}{30}.
\tag{17}
\]
The last comparison is the integer inequality
\(517350<517720\). Hence
\[
 \frac{D^6}{r^2}<\left(\frac{49}{30}\right)^3\frac{43}{40}
 <\frac{387}{80}<\frac{27}{4}<\frac{N_e^2N_s^2}{r^2}.
\tag{18}
\]
Here \((49/30)^3<9/2\) is the same rational bound used in
the early four/three proof. Thus every private maximizer on the
old left face has strictly positive derivative in \(x\).

## 4. Supporting tangent and literal main currents

For fixed \(b\), choose such a maximizer \((u_b,v_b)\) at
\(x_0=.22\). Private first-order optimality gives
\(f_u(u-u_b)+f_v(v-v_b)\le0\), where
\(f=\Re\mathcal F_4\), even if that maximizer lies on a
private boundary. Joint concavity from Section 2 and positivity
from (18) then give
\[
 f(u,v,x)\le f(u_b,v_b,x_0)+f_x(x-x_0)
                           \le f(u_b,v_b,x_0),
                     \qquad .1\le x\le.22.
\tag{19}
\]
The original next-four central theorem bounds the factorial
alternative on the old face by \(M+\ell_b(y)-1/500\).
Subtracting the same constant \(2\pi H\) in (19) proves
the first inequality in (5). The original scalar comparison
\[
 -\Re g(x+ih)-2\pi h>3/40
                    \quad(.1\le x\le.22,\ 0\le h\le7/500)
\tag{20}
\]
from the [Fourier branch theorem](research_mixed_selected_minimum_flow_obstruction.md)
makes the forced alternative smaller than the factorial one.
This proves Theorem 1 without a separate forced Hessian or a
moving branch of maximizing points.

Let \(U_N^{\rm hor}(w,X)\), \(C_{1,N}^{\rm hor}(X,Y)\)
be the two literal zero-mode main currents defined in the
[next-four finite reduction](research_mixed_selected_four_four_finite_reduction.md).
They retain the original \(+N\) coefficients, half-grid cuts and
complete endpoint coefficient. Set \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi ib}\). For every \(\tau>0\), every fixed
ordinary-color derivative order \(k\), and both level parities,
\[
\begin{split}
 &\left|\partial_w^k\{
 U_N^{\rm hor}(w,X)C_{1,N}^{\rm hor}(X,Y)d_N(X)X^{-N}\}\right|
                  |d_N(Y)|^{1/2}\\
 &\hspace{12mm}\le C_{\tau,k}N^{A_{\tau,k}}
       \exp N\{M+\ell_b(y)-1/500+\tau\}.
\end{split}
\tag{21}
\]
This holds on a sufficiently small fixed ordinary-color disk about
\(-2\), uniformly on (2). The outgoing halfweight in (21) is
its original modulus allocation, not a chosen holomorphic square
root.

Indeed all factorial arguments of these particular currents stay
in compact original regular strips: the shifted real intervals
are \(e+a\in[.37,.71]\), \(s+a\in[.225,.72]\), and
\(s+b\in[.345,.95]\). The complete endpoint coefficient
has its original neighborhood upper bound. The complete selected
Fourier factor has upper rate
\(\max\{-\Re g(a)-2\pi H,0\}\), and the unchanged
outgoing allocation has upper rate \(-\Re g(b)/2\), since
the actual \(h_b<0\). These are precisely the phases in (5).
Compact integration, the two original \(N\) densities, symbols
and half-grid displacements consume a polynomial and one arbitrary
total tolerance. Shrinking the existing ordinary-color disk absorbs
its phase variation; Cauchy's formula on a smaller disk gives the
fixed derivatives. No factor is divided out at a finite zero.

No other cap profile, ordinary real row, alias or joining current
is bounded by (21). A complete selected early pair, a whole-word
comparison and a short-partial-filling theorem remain outside
this note.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_three_early_central.md | d9e2797fac0599cdca302ecd22312926b28765f487c8f0d95629d31d28c22405 |
| research_mixed_selected_boundary_optimizer_bounds.md | 13fa176cf8f50054bc2c47e479f85daf0ecb9b22a68d316689ad752f8ca2b603 |
| research_mixed_first_four_next_four_central_gap.md | 0acb83fa492a0ce6b2c10f1ddeb21480d2c94dfeb10055e925e51f5ae34d4c99 |
| research_mixed_selected_four_four_finite_reduction.md | d018c6ad4dd78e6a6c7ac649f0d5d8443b649f1f01d9c6acde586697da1da4e5 |
| research_mixed_selected_minimum_flow_obstruction.md | 52c6bf13beb1a98b69c2f834223f017dcb2acb27b406cf5cb270947ef2d14963 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The complete written proof and directly used source implications were
read. No new mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.
