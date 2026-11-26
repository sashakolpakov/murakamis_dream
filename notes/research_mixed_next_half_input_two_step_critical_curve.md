# The original two-step half-input critical curve

Private source and phase deduction, 9 November 2026. The complete
two-step conditional polynomial has a different stationary problem
from the geometric four-block local contribution. Its exponentiated
equations admit an explicit rational parameterization, with the
original half-input sheet selected before clearing denominators.

For a following type three there is a concrete diagonal base:
its reduced real phase has one nondegenerate maximum, at a shared
coordinate strictly between \(39/100\) and \(2/5\). This lies
outside the previous closed outgoing region, but the new complete
lower-unit-arc theorem supplies its full finite source. Positivity
then gives an actual lower bound for the whole physical two-step
diagonal at both parities. It does not give a full diagonal
asymptotic or a comparison at the ordinary complex output.
No mathematical numerical evaluation, saved-value
arithmetic, import, compilation, or frozen-source edit is used.

## 1. The complete source and its original phase

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
C_{\beta,N}(Y,W)=
 \sum_{j=0}^D\frac{Y^{-j}(rY;r)_j(rW;r)_j}{P_j^{2+\beta}},
 \qquad\beta=0,1.
\]
The exact source is the one in
[Fourier propagation, (7)](research_mixed_next_attachment_fourier_propagation.md):
\[
\begin{split}
C^{(2)}_{0\beta,N}(r^b,W)
 &=N\operatorname{CT}_Y
       [C_{0,N}(r^b,Y)C_{\beta,N}(Y,W)]\\
 &=\sum_{a=0}^D C_{0,N}(r^b,r^a)C_{\beta,N}(r^a,W).
\end{split}                                                     \tag{1}
\]
All rows and support zeros remain in this identity. The intermediate
band is \([-D,D]\), so no nonzero multiple of \(N\) survives.
There is no old-four weight on this cycle, including when
\(\beta=1\). At \(b=M=\lceil N/2\rceil\) the incoming coordinate
is \(1/2\) at even levels and \(1/2+1/(2N)\) at odd levels.
The phase below is the limiting half-input phase; it does not
erase the latter finite shift.

Use the original primitive and its original strip lift:
\[
g(v)=\frac{\operatorname{Li}_2(e^{-2\pi iv})-\pi^2/6}{2\pi i},
\qquad g'(v)=\log(1-e^{-2\pi iv}),\qquad 0<\Re v<1.
                                                               \tag{2}
\]
For clarity include the external factorials in the conditional
phase:
\[
\Phi_\beta(s;a,z)=g(s+a)+g(s+z)-(2+\beta)g(s)
                     -g(a)-g(z)+2\pi ias.                       \tag{3}
\]
The complete outgoing amplitude source uses precisely
\(\Phi_0\), with the original additive constant.
The two-step phase at limiting half input is
\[
\Omega_\beta(\xi,y,\eta;z)
   =\Phi_0(\xi;1/2,y)+\Phi_\beta(\eta;y,z).                       \tag{4}
\]
At this point (4) is a phase of the literal source (1), not a
claim that its complete cycle is represented by one saddle.

Its three original stationary equations are
\[
\begin{split}
0&=g'(\xi+1/2)+g'(\xi+y)-2g'(\xi)+\pi i,\\
0&=g'(\xi+y)+g'(\eta+y)-2g'(y)+2\pi i\eta,\\
0&=g'(\eta+y)+g'(\eta+z)-(2+\beta)g'(\eta)+2\pi iy.
\end{split}                                                     \tag{5}
\]
No derivative of an external normalization is omitted in the
middle equation.

## 2. Exact rational elimination and the selected half sheet

Set
\[
X=e^{-2\pi i\xi},\quad Y=e^{-2\pi iy},\quad
T=e^{-2\pi i\eta},\quad W=e^{-2\pi iz}.
\]
Exponentiating (5) gives exactly
\[
\begin{split}
(1+X)(1-XY)&=-(1-X)^2,\\
(1-XY)(1-TY)&=T(1-Y)^2,\\
(1-TY)(1-TW)&=Y(1-T)^{2+\beta}.
\end{split}                                                     \tag{6}
\]
Define
\[
A(X)=X^2-X+2,\qquad D(X)=X^3-X^2+2X-4.
\]
At any solution in the original regular strips, (6) yields
\[
\boxed{\quad
Y=\frac{A}{X(X+1)},\qquad
T=\frac{X^2(X+1)}D,\qquad
1-XY=-\frac{(X-1)^2}{X+1},\quad
1-TY=-\frac4D,\quad1-T=-\frac{2A}D .
\quad}                                                         \tag{7}
\]
Consequently the two output maps are
\[
\boxed{\begin{split}
W_0(X)&=\frac{X(X+1)D+A^3}{X^3(X+1)^2},\\
W_1(X)&=\frac{X(X+1)D^2-2A^4}{D X^3(X+1)^2}.
\end{split}}                                                    \tag{8}
\]
For example \(1-Y=2(X-1)/[X(X+1)]\); substituting this and
the first formula in (7) into the middle equation of (6)
gives the formula for \(T\). The last equation then gives (8).
Thus the displayed phases, rather than a changed Fourier
carrier, fix all signs in these rational maps.

The algebra is applied only where the original exponentials
are nonzero and every factorial argument is in a regular strip.
In particular \(X\ne0,\pm1\), \(A\ne0\), and \(D\ne0\).
Before division, the middle equation gives
\(DT=X^2(X+1)\). Its finite exponential \(T\) therefore
proves \(D\ne0\).
The identities in (7) retain the nonzero factors \(1-XY\),
\(1-TY\), and \(1-T\); the last equation of (6) then retains
\(1-TW\ne0\). A rational preimage in (8) alone is not an
original stationary point: it must also admit the required
strip arguments and all three zero logarithmic lifts in (5).

There is a particularly concrete guard on the first root.
The [half-input phase theorem, Lemma 1](research_mixed_next_attachment_excess_harmonic_disks.md)
defines a holomorphic original root \(\xi=s_{\rm h}(y)\) for
every \(0<\Re y<1/2\), without any restriction on \(\Im y\).
It is the root with
\[
0<\Re\xi<1/2,\qquad \Re\cot(\pi\xi)>0.
                                                               \tag{9}
\]
In exponential coordinates this sheet is exactly
\[
\mathcal X=\{X:\Im X<0,\ |X-1|^2>2\},
\qquad Y\in\{\Im Y<0\}.                                         \tag{10}
\]
Indeed
\[
\Re\!\left(i\frac{1+X}{1-X}\right)
       =\frac{-2\Im X}{|1-X|^2},\qquad
\Im\!\left(\frac{A}{X(X+1)}\right)
       =\frac{2\Im X\,(|X-1|^2-2)}
                    {|X|^2|X+1|^2}.                            \tag{11}
\]
The selected cotangent root in (9) is unique for every lower
half-plane \(Y\), by that theorem. Conversely, an \(X\) in
(10) gives such a \(Y\), solves the same exponentiated first
equation, and has the required right-half-plane cotangent.
It is therefore that root, with its already calibrated zero
lift. In particular the first rational map in (7) is one-to-one
from \(\mathcal X\) onto the lower half-plane. Its derivative
\[
Y'(X)=-2/X^2+4/(X+1)^2
                                                               \tag{12}
\]
does not vanish there: its zeros \(1\pm\sqrt2\) are real.
These assertions select the first index. They do not select
a root of either full output equation (8).

## 3. The actual four-block reference is not this saddle

At an eligible ordinary four-block reference write
\(y_*=t_3\), \(\eta_*=s_4\), \(z_*=t_4\), and retain its
third incoming coordinate \(t_2\) and third index \(s_3\).
The complete local four-block source has reduced phase
\[
P_{343}(-2,y)+\psi_\beta(y,z),
\]
whereas the replacement half-input problem has phase
\[
\mathcal S_{\rm h}(y)+\psi_\beta(y,z),\qquad
\mathcal S_{\rm h}(y)=\Phi_0(s_{\rm h}(y);1/2,y).
                                                               \tag{13}
\]
Stationary differentiation of the original sources gives at
the actual four-block point
\[
\partial_y[\mathcal S_{\rm h}(y)+\psi_\beta(y,z_*)]_{y=y_*}
   =g'(y_*+s_{\rm h}(y_*))-g'(y_*+s_3)\ne0.                     \tag{14}
\]
Here the geometric four-block derivative has already canceled;
no independent choice of its reference has been made.

For the nonzero assertion, equality in (14), followed by
exponentiation in the regular strips, would give
\(s_{\rm h}(y_*)=s_3\). Their real-part difference has modulus
less than one, so the possible integer difference is zero.
Subtracting the original third-index equation from the
half-input equation then gives, with
\(X=e^{-2\pi i s_3}\) and \(Y_2=e^{-2\pi i t_2}\),
\[
                 -Y_2\frac{1+X}{1-Y_2X}=1,
                    \qquad Y_2=-1.                            \tag{15}
\]
But the original typed chamber has \(0<\Re t_2<9/20\).
This contradicts \(e^{-2\pi i t_2}=-1\).
This is the source-matched nonstationarity argument of the
half-input phase theorem; it applies at both fourth types.
Thus an old geometric saddle cannot be reused in (1).

## 4. A uniquely located type-three diagonal phase base

Take \(\beta=0\) and \(z=1/2\), so \(W=-1\).
For real \(0<y<1/2\), the original primitive has
\[
g(v)=J(v)+\frac{i\pi}{2}(v-v^2),\qquad
J(\overline v)=\overline{J(v)}
\]
on the regular strip. Equation (3) becomes
\[
\Phi_0(\xi;a,z)
 =J(\xi+a)+J(\xi+z)-2J(\xi)-J(a)-J(z)
                                    +i\pi\xi(a-z).              \tag{16}
\]
Therefore the reverse conditional index
\(\eta=\overline{s_{\rm h}(y)}\) has the original zero lift
and satisfies
\[
\Phi_0(\eta;y,1/2)=\overline{\mathcal S_{\rm h}(y)}.
\]
Eliminating these two nondegenerate index roots reduces (4)
on this real interval to
\[
                         2\Re\mathcal S_{\rm h}(y).              \tag{17}
\]

Write \(X=x+iv\) on the selected sheet, with \(v<0\).
The condition \(|Y|=1\), together with (10), is equivalent to
\[
-1<x<0,\qquad
|X|^2=\frac{2x^2-x+1}{1+x},\qquad
v=-\sqrt{\frac{(1-x)(x^2+1)}{1+x}}.                              \tag{18}
\]
To verify it, expand \(|A|^2=|X|^2|X+1|^2\).
It gives \(|X|^2(1+x)=2x^2-x+1\), and hence the stated
formula for \(v^2\). Positivity first gives \(-1<x<1\).
Then \(|X-1|^2=2(1-x)/(1+x)>2\) gives \(x<0\).
Conversely (18) satisfies both conditions.
As \(x\) runs from \(-1\) to zero, \(Y\) runs once along the
lower unit semicircle from \(1\) to \(-1\). This follows
also from injectivity and (12); the angular derivative is
nonzero. Thus \(y\) increases strictly from zero to \(1/2\).

The exact stationary derivative in (13), using (7), has real part
\[
\Re\mathcal S_{\rm h}'(y)
 =\log\left|\frac{1-XY}{1-Y}\right|
 =\log\left|\frac{X(X-1)}2\right|.
                                                               \tag{19}
\]
On (18),
\[
\left|\frac{X(X-1)}2\right|^2
 =\frac{(1-x)(2x^2-x+1)}{2(1+x)^2}
 =1-\frac{p(x)}{2(1+x)^2},
\quad p(x)=2x^3-x^2+6x+1.                                      \tag{20}
\]
Since \(p'(x)=6x^2-2x+6>0\), \(p(-1)<0<p(0)\),
there is a unique zero \(x_0\in(-1,0)\). Equations
(19)--(20) show strict increase of (17) before it and strict
decrease afterward. The second derivative there is strictly
negative, since \(dx/dy>0\) and \(p'(x_0)>0\).

There is an entirely rational location witness:
\[
p(-5/31)=-64/29791<0,\qquad
p(-4/25)=97/15625>0.
                                                               \tag{21}
\]
At the root, (20) gives
\(|X|^2=2(1+x)/(1-x)\). Substituting this and
\(p(x)=0\) into the real part of \(Y\) simplifies it to
\[
\Re Y=\frac{x(5-x)}{2(3x+1)}.
\]
This expression increases on the interval in (21), because
the numerator of its derivative, after the positive denominator
is removed, is \((1-x)(3x+5)>0\). Hence
\[
                         -\frac{25}{31}<\Re Y<
                                      -\frac{258}{325}.          \tag{22}
\]
For the upper angular endpoint, \(5>(69/31)^2\) gives
\[
-25/31>-(1+\sqrt5)/4=\cos(4\pi/5).
\]
For the lower angular endpoint, use \(\pi>25/8\) and the
alternating cosine series:
\[
\begin{split}
\cos(11\pi/50)&<\cos(11/16)\\
&\le1-\frac{(11/16)^2}{2}+\frac{(11/16)^4}{24}
 =\frac{1215793}{1572864}
 <\frac{25}{32}<\frac{258}{325}.
\end{split}                                                     \tag{23}
\]
All angles in this comparison lie in \((0,\pi)\).
Since \(Y=e^{-2\pi iy}\), (22)--(23) prove
\[
\boxed{\qquad 39/100<y_0<2/5.\qquad}                             \tag{24}
\]

This is a nondegenerate critical point of the full holomorphic
phase (4). The two conditional index derivatives are nonzero
by the simple selected half root and its conjugate. Eliminating
them leaves the strictly negative second derivative of (17).
The full three-variable Hessian is therefore nonsingular.
Every argument in (2)--(5) is in a compact regular strip at
this point. The implicit function theorem supplies one
holomorphic original-log critical branch near \(z=1/2\).
Its exponential representation is \(W_0(X)\) in (8), and
\(W_0'(X_0)\ne0\). Indeed a zero derivative in that rational
curve would give a nonzero null vector of the just proved
invertible Hessian, while \(d\xi/dX=-1/(2\pi iX)\ne0\).
This calibrates one local phase sheet, without selecting a
continued cycle at the actual ordinary output reference.

## 5. A complete physical diagonal lower bound

At both parities, the exact physical Gram matrix
\[
K_{ab}=C_{0,N}(r^a,r^b)
\]
is Hermitian positive. Thus the complete source has the identity
\[
\boxed{\quad
C^{(2)}_{00,N}(r^M,r^M)=(K^2)_{MM}
                     =\sum_{a=0}^D|C_{M,N}(r^a)|^2>0 .
\quad}                                                         \tag{25}
\]
Here \(C_{M,N}(Y)=C_{0,N}(r^M,Y)\), and no crossing scalar
has been removed from the definition (1). At even levels
both diagonal arguments are exactly \(-1\); at odd levels
they remain \(r^M\).

The previous complete outgoing amplitude theorem was uniform on
a neighborhood of the closed set
\[
4/5\le|Y|\le8/7,\qquad
3\pi/5\le-\arg Y\le39\pi/50.                                    \tag{26}
\]
Its original-action identification includes
\(3/10\le\Re y\le39/100\), \(-3/100\le\Im y\le1/50\).
The base point (24) lies strictly outside that closed set;
its unspecified neighborhood did not supply a proved inclusion.
The independent central conditional rectangles do reach
\(\Re y=2/5\), but their incoming coordinate is restricted to
the central rectangles, and does not include the first
incoming coordinate \(1/2\) here. Those statements therefore
did not by themselves license the first complete factor near
(24).

The [complete lower-unit-arc theorem](research_outgoing_packet_lower_unit_arc.md)
now does license it. Choose a sufficiently small fixed
\(\epsilon>0\) so that
\([y_0-\epsilon,y_0+\epsilon]\subset(1/4,1/2)\).
On a fixed complex neighborhood of this interval its exact
formula, including the sine factorial, has original action
\[
\mathcal S(a,y)=J(a)-\int_a^1\log h(v,e^{-2\pi iy})\,dv .
                                                               \tag{27}
\]
At \(a=1/2\) it equals \(\mathcal S_{\rm h}(y)\). Indeed both
are holomorphic near the real arc and match on its overlap
with the original outgoing theorem; the whole-strip phase
theorem fixes the continuation of the latter.
The source supplies a nonzero holomorphic symbol
\(\mathcal B(a,Y)\) there, and the original sine-product
normalization yields
\[
C_{M,N}(e^{-2\pi iy})
 =N^{-1/2}a_{{\rm par}}(y)
     e^{N\mathcal S_{\rm h}(y)}(1+O_{\rm hol}(N^{-1})),
                                                               \tag{28}
\]
where
\[
\begin{split}
a_{{\rm par}}(y)
 &=\sqrt2\,\mathcal B(1/2,e^{-2\pi iy})
       \exp\{\delta_N\partial_a\mathcal S(1/2,y)\},\\
\delta_N&=M-N/2=
\begin{cases}0,&N\ {\rm even},\\1/2,&N\ {\rm odd}.\end{cases}
\end{split}                                                     \tag{29}
\]
Both symbols are nonzero. Equation (29) retains the exact
odd shift of the physical input; it is not the shift for
the different row \(M-1\).

Put \(e_0=\Re\mathcal S_{\rm h}(y_0)\) and
\(d_0=-\partial_y^2\Re\mathcal S_{\rm h}(y_0)>0\).
Define the literal node block
\[
\mathcal A_N=\{0\le a\le D:|a/N-y_0|\le\epsilon\}.
\]
The strict local maximum in Section 4 and the full relative
estimate (28) give the positive discrete Gaussian expansion
\[
\boxed{\quad
\sum_{a\in\mathcal A_N}|C_{M,N}(r^a)|^2
 =N^{-1/2}|a_{\rm par}(y_0)|^2
        \sqrt{\frac{\pi}{d_0}}\,
       e^{2Ne_0}\{1+O(N^{-1/2})\}.
\quad}                                                         \tag{30}
\]
For completeness, in the rescaled coordinate
\(x=\sqrt N(a/N-y_0)\) the squared modulus in (28) is
\[
N^{-1}e^{2Ne_0}
       \bigl(|a_{\rm par}(y_0)|^2+O(N^{-1/2}|x|+N^{-1})\bigr)
       e^{-d_0x^2+O(N^{-1/2}|x|^3)} .
\]
Shrink \(\epsilon\) once so that the cubic remainder is
absorbed by a fixed negative quadratic. A smaller rescaled
window and its Gaussian tail give an integrable polynomial
Gaussian majorant; Taylor's theorem then gives the stated
relative \(O(N^{-1/2})\) error. The rescaled mesh is
\(N^{-1/2}\), with an arbitrary fractional center, and its
Gaussian sum tends uniformly to
\(\sqrt N\int_{\mathbb R}e^{-d_0x^2}\,dx\).
The usual first-derivative Riemann-sum estimate suffices for
the stated error. No internal signed remainder has been
discarded: (28) was retained inside the nonnegative summands.

Since (25) is a sum of nonnegative terms, (30) proves for
some fixed \(c_*>0\) and all sufficiently large \(N\), at
both parities,
\[
\boxed{\quad
C^{(2)}_{00,N}(r^M,r^M)
        \ge c_*N^{-1/2}e^{2N\Re\mathcal S_{\rm h}(y_0)}.
\quad}                                                         \tag{31}
\]
This is a lower bound for the complete actual finite diagonal.
It needs no upper estimate on the excluded nodes.

The exact rational curve (8), the local phase branch at (24),
and the full positive lower bound (31) are distinct useful
inputs. Completing the proposed coherent propagation requires
selection and continuation of a joint saddle toward the actual
ordinary \(W\), and estimates for every competing region and
endpoint of (1). For \(\beta=1\), even (25) is unavailable:
the exact additional diagonal \(P_j^{-1}\) is complex.
No propagated half-input action anchor, four-block remainder
gap, or closing theorem follows from the current calculation.

## Frozen source bindings

- Literal two-step source, physical stops, and exact Fourier scalar:
  07704e4c973619426b5f6d3090a2b5a49b55ec58a6f4d7afc1827f0c761c3b82.
- Whole-strip half-input phase, selected sheet and nonstationarity:
  623ebfda0574d46a7e10e851d27a9fd48a8910543691a58a8d819a882878be47.
- Original finite outgoing amplitude and its precise complex domain:
  1620ac15a7fb61021729aeb3831b85dc6c716f140787f9984ecc29bd3be61840.
- Exact Hermitian feature Gram identity and the type-four weight:
  be5dc00fde7c062f7b6ad0e7b8859b2e9dd5d564f16bce0aea75de9dba12cb6e.
- Actual four-block local source and original action allocation:
  c62f1cca0fbfe5bfe619824ca3fc3ce70af50176b623b82004848bf59a24f8ca.
- Independent central conditional products and their source scope:
  e5d03fb37a0f5746aabc0e87727fbae897f4badbe843953147f103fad6f92c2b.
- Complete finite source on every compact lower unit arc:
  ec77eea9959e496b98c52274d249c056af6c3a656a5bb4fad0534c70efefdca8.

