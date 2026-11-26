# Closing three-crossing sources before the small-gradient regime

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The actual three-vertex cap can already be closed against itself, or
against any fixed number of its retained attachments. The resulting
original complete-ended scalar has a nonzero leading asymptotic for
every fixed length \(m\ge6\). Both ordinary outside colors are
complete, equal to \(-2\), and every fixed ordinary derivative at
those colors is retained. The geometric target is the original marked
partial filling with those two ends complete; identifying a knot
invariant remains a separate topological and normalization question.

## 1. A closing criterion on the larger source domain

Set
\[
 \begin{gathered}
 x_h=\frac16+\frac{i\log2}{2\pi},\quad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad K=|k_0|,\quad
 a=\Re k_0,\\
 R=\frac1{200},\quad W=\frac9{1000},\quad
 H_*=\frac{57}{10000},\quad b=\frac9{50},\quad
 A=\frac{29}{20},\quad
 v(t)=\min\{\operatorname{dist}(t,\mathbb Z),3/100\},\\
 \rho=\frac{5-\sqrt{21}}2,\qquad
 Z=\frac{(21/20)\rho}{1-(3/10)\rho},\qquad
 D=2\sqrt{21},\quad \beta=2b,\quad
 C_{\rm cl}=\frac{K(D+\beta)}{2(D-\beta)^2}.
 \end{gathered}
 \tag{1}
\]
Let \(F_N,G_N\) be actual finite half-band functions, with the
period sign \((-1)^{N-1}\) of the original cardinal vector.
Assume nonzero holomorphic packets on a neighborhood of the closed
union \(\mathcal U=\{|z|\le R\}\cup[-W,W]\):
\[
 \begin{split}
 F_N(x_h+z)&=\omega_{F,N}N^{\nu_F}f(z)e^{NS(x_h+z)}(1+O(N^{-1})),\\
 G_N(x_h+z)&=\omega_{G,N}N^{\nu_G}g(z)e^{NT(x_h+z)}(1+O(N^{-1})),\\
 S'(x_h+z)/k_0&=-\sqrt{21}z+h(z),\qquad
 T'(x_h+z)/k_0=-\sqrt{21}z+q(z),\\
 |h(0)|&\le H_F\le H_*,\qquad |q(0)|\le H_G\le H_*,
 \qquad |h'|,|q'|\le b.
 \end{split}
 \tag{2}
\]
The errors and their fixed internal derivatives are uniform on smaller
neighborhoods. The original carriers \(\omega_{F,N},\omega_{G,N}\)
have modulus one. Put \(M_F=\Re S(x_h)\),
\(M_G=\Re T(x_h)\), and \(L=H_F+H_G\).
Require either of the following whole-period bounds:

* **Unequal preparation:** each source has the envelope
  \(M_i+KH_i v(t)-Av(t)^2\), up to a polynomial factor, and
  \(L\le(1+Z)H_*\).
* **Two actual entrance caps:** the product has the bound
  \(M_F+M_G+2B_*-3v(t)^2\), up to a polynomial factor,
  where \(B_*=77/10^6\).

All ordinary parameters, when used below, are evaluated at their
complete colors. Assume the corresponding packets and exponential
envelopes, with order-dependent polynomial factors, for every fixed
ordinary jet there. A global bound on a complex neighborhood of those
outside colors is not required.

**Theorem 1.** Under these hypotheses the exact bilinear closure
\[
 \mathcal C_N=N\int_{x_h-1/2}^{x_h+1/2}F_N(x)G_N(x)\,dx
 \tag{3}
\]
has a nonzero leading asymptotic
\[
 \mathcal C_N=
 \omega_{F,N}\omega_{G,N}N^{\nu_F+\nu_G+1/2}
 \frac{\sqrt{2\pi}\,f(z_c)g(z_c)}
 {\sqrt{-[S''+T''](x_h+z_c)}}
 e^{N\Xi}(1+O(N^{-1})),\qquad
 \Xi=S(x_h+z_c)+T(x_h+z_c).
 \tag{4}
\]
The square root has positive real part. The unique critical point
lies in \(|z_c|<.0013\). Both parities and the differentiated
asymptotic for every fixed ordinary jet at completeness are included.

## 2. The exact central contour and its real annuli

Write \(U(z)=S(x_h+z)+T(x_h+z)\). The critical equation is
\[
 z=\frac{h(z)+q(z)}D,
 \qquad |z_c|\le\frac{L}{D-\beta}
 \le\frac{2H_*}{D-\beta}<r:=\frac{13}{10000}.
 \tag{5}
\]
Its right side has derivative modulus at most \(\beta/D<1\)
and maps the closed radius-\(R\) disk strictly into itself.
The complex contraction theorem therefore gives the unique critical
point there. Throughout the disk and real interval,
\[
 |U''+k_0D|\le\beta K,
 \qquad -\Re U''\ge Da-\beta K>18.
 \tag{6}
\]
All bounds remain strict on slightly smaller open neighborhoods of
the stated compact sets, allowing the required analytic germs.

For \(e_\pm=\pm R\), put \(d_\pm=e_\pm-z_c\).
The two elementary uniform estimates
\[
 \begin{split}
 \Re(k_0D d_\pm^2)-\beta K|d_\pm|^2
 &\ge D(aR^2-2KRr-Kr^2)-\beta K(R+r)^2
   >\frac{33}{500000},\\
 \pm\Re(k_0D d_\pm)-\beta K|d_\pm|
 &\ge D(aR-Kr)-\beta K(R+r)>\frac1{20}
 \end{split}
 \tag{7}
\]
follow by expanding around the real endpoints and using
\(|z_c|<r\). They are checked by outward arithmetic in the
reproduction below. The first deliberately uses an absolute bound
for \(\Re(k_0z_c^2)\); it does not assume a favorable phase
of the critical displacement.

Replace only the central real segment \([-R,R]\) by the two
straight segments \([-R,z_c]\) and \([z_c,R]\).
Their convex hull lies inside the source disk. The finite integrand
is holomorphic there, so the replacement is exact with the same
endpoints. No connector is discarded. On either segment, stationarity
and (6)--(7) give
\[
 \Re U(z_c+s d_\pm)
 \le\Re U(z_c)-\frac{s^2}{2}
       \{\Re(k_0D d_\pm^2)-\beta K|d_\pm|^2\},
 \qquad 0\le s\le1.
 \tag{8}
\]
In particular each real endpoint loses more than \(33/10^6\).
The real parts of \(d_+,d_-\) have opposite signs, while
\(|\Im d_\pm|<r\). Equation (7) puts their directions in
the two opposite Gaussian convergence sectors. Equivalently, scale
\(h,q\) continuously to zero: (5)--(7) hold throughout, so the
two rays cannot leave their sectors and reduce to the positive and
negative real rays. The central integral consequently has the full
Gaussian coefficient in (4), with the original left-to-right
orientation.

Integrating (6) once from \(z_c\) shows
\[
 \Re U'(-R)>0,\qquad \Re U'(R)<0.
 \tag{9}
\]
Indeed the second estimate in (7) bounds their signed margins by
more than \(1/20\). Since \(\Re U''<-18\) on both real
annuli, \(\Re U\) decreases away from the center throughout
\(R\le|t|\le W\). The actual packets in (2) apply there;
their contributions have rate at most \(\Re\Xi-33/10^6\).
Thus the union-domain packet supplies the intermediate real annuli
which were absent from the earlier small-disk closing argument.

## 3. The rest of the full period and the coefficient

Stationarity also retains the absolute action normalization:
\[
 U(z_c)-U(0)=-z_c^2\int_0^1 sU''(s z_c)\,ds,
 \qquad |\Xi-S(x_h)-T(x_h)|\le C_{\rm cl}L^2.
 \tag{10}
\]
This is a bound on the actual critical value; it does not replace
that value by the sum of the center actions.

In the unequal-preparation case, for \(v\ge W\) the loss
\(2Av^2-KLv\) increases with \(v\), and
\[
 2AW^2-K(1+Z)H_*W-C_{\rm cl}(1+Z)^2H_*^2
                                      >\frac1{20000}.
 \tag{11}
\]
The product of the two original full-period envelopes therefore has
this strict gap relative to \(\Re\Xi\) on the entire remaining
period. In the two-entrance case the sharper product envelope gives
\[
 3W^2-2B_*-C_{\rm cl}(2H_*)^2>\frac1{20000}.
 \tag{12}
\]
Again the loss only increases up to the cap \(.03\) and remains
constant beyond it. Equations (8)--(12) exhaust the original period.
In particular no unknown Fourier-boundary term is substituted for an
actual source tail.

The central saddle in (8) is nondegenerate by (6). The holomorphic
amplitudes are nonzero there, and the two rays give the full Gaussian.
The original \(N\,dx\) measure supplies the power
\(N^{\nu_F+\nu_G+1/2}\). The absolute complementary gaps
prevent cancellation of this leading coefficient and prove (4).
For ordinary jets, differentiate (3) before integrating. The assumed
jet envelopes preserve every complementary gap up to polynomial
factors. On the central contour the differentiated local packets give
the derivatives of the stationary phase and coefficient in (4).
This proves a complete-color jet assertion, without inferring an
off-color global envelope. \(\square\)

## 4. Original words of every fixed length at least six

Let \(A_N=JM^3\),
\(\widetilde A_N=A_N-E_{\lfloor N/40\rfloor}\), and use the
original vector \(v(w)\). The
[first-entrance real theorem](research_three_first_entrance_real_extension.md)
gives the actual cap
\[
 F_N^{[3]}(x,w)=v(w)^TA_N^3h(x),\qquad w=-2,
 \quad \nu=-1,\quad \omega_N=C_{N,3}\kappa^2,
 \quad H_0=H_*.
 \tag{13}
\]
It has the packet and ordinary jets required in (2), as well as both
the standard larger-class envelope and its sharper original bound
\[
 |F_N^{[3]}(x_h+t,-2)|
 \le CN^q e^{N[M_0+B_2-(3/2)v(t)^2]},
 \qquad
 B_2=.000066+\frac{(.0113)^2}{4(29/20+3/2)}<B_*.
 \tag{14}
\]
The same exponential bound holds for every fixed ordinary jet.

The [full larger-source induction](research_three_larger_source_propagation.md)
proves that, for every fixed \(j\ge0\),
\[
 F_N^{[3+j]}(x,w)=v(w)^TA_N^3\widetilde A_N^{\,j}h(x)
 \tag{15}
\]
has the same packet domain and power \(N^{-1}\), carrier
\(C_{N,3}\kappa^{2+j}\), and standard whole-period envelope
with \(H_j=Z^jH_*\). For \(j\ge1\), the sum of the bounds
for (13) and (15) is at most \((1+Z)H_*\), so (11) applies.
For \(j=0\), the two original estimates (14) give (12).

At both level parities the exact bilinear cardinal identity and the
symmetry of the two finite matrices give
\[
 \begin{split}
 N\int h(x)h(x)^T\,dx&=I,\qquad
 A_N^T=A_N,\quad \widetilde A_N^T=\widetilde A_N,\\
 N\int F_N^{[3]}(x,w_L)F_N^{[3+j]}(x,w_R)\,dx
 &=v(w_L)^TA_N^3\widetilde A_N^{\,j}A_N^3v(w_R).
 \end{split}
 \tag{16}
\]
The right word is transposed and reversed. No complex conjugation is
used. Its selected-vertex count is \(m=6+j\), its carrier is
\(C_{N,3}^2\kappa^{4+j}=C_{N,3}^2\kappa^{m-2}\), and its
power is \(N^{-3/2}\).

Unrolling the stationary eliminations in (13)--(16) gives a critical
point of the original unsummed chain phase. The initial three-vertex
cap branches, the subsequent disk attachment branches, and the closing
wire \(|z_c|<.0013<R\) all lie in the
[proved geometric sign chamber](research_three_chain_geometric_chamber.md).
That chamber is convex and its negative complex Hessian has positive
definite real part. Integrating the Hessian along a segment shows that
the full complex gradient is injective. The assembled critical point
therefore equals the original geometric point. The
[absolute action calibration](research_three_chain_action_volume_calibration.md)
then gives, without changing the original phase constants,
\[
 \Xi_m(-2,-2)=
 \sum_{v=0}^{m}\psi(t_v,t_{v+1})
 +\sum_{v=1}^{m}\left(\frac{3it_v^2}{4\pi}-it_v\right)
 +(m-2)i\gamma,\quad t_0=t_{m+1}=0,
 \qquad 2\pi\Re\Xi_m(-2,-2)=\operatorname{Vol}(M_m).
 \tag{17}
\]
Here \(\gamma\) is the real constant of that calibration and
\(M_m\) is the original marked partial filling with both outside
ends complete.

For \(j=0\), (16) is already \(v(w_L)^TA_N^6v(w_R)\).
For \(j\ge1\), the
[original L40 corner comparison](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
restores every retained factor. Its rate is at most
\((2m-1)c+M_\infty+27/200\), whereas the actual geometric
rate exceeds the same expression with \(27/200\) replaced by
\(3/25+1/15\). The strict reserve is
\[
                   \frac3{25}+\frac1{15}-\frac{27}{200}
                        =\frac{31}{600}>0.
 \tag{18}
\]
The comparison holds for this mixed word and for all fixed ordinary
boundary jets. It therefore preserves the coefficient in (4).

**Corollary 2.** For each fixed integer \(m\ge6\), at the two
ordinary complete boundary colors \((w_L,w_R)=(-2,-2)\),
\[
 v(w_L)^TA_N^m v(w_R)
  =C_{N,3}^{2}\kappa^{m-2}N^{-3/2}
       a_m(w_L,w_R)e^{N\Xi_m(w_L,w_R)}(1+O(N^{-1})),
 \qquad a_m(-2,-2)\ne0.
 \tag{19}
\]
The differentiated asymptotic holds for every fixed ordinary jet at
these colors. The phase and amplitude denote their local analytic
germs; no uniform outside-color full-period estimate is asserted.
In particular, along all sufficiently large integer levels,
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
 \log|v(-2)^TA_N^m v(-2)|=\operatorname{Vol}(M_m).
 \tag{20}
\]
The starting level may depend on the fixed length. Cases \(m=1,2\)
have separate source theorems; this argument leaves \(m=3,4,5\)
unresolved. It supplies neither a whole-period bound in the ordinary
outside colors nor a knot identification. A Kashaev consequence requires
the original marked component conditions and its exact unit or
polynomial normalization. A cofinite theorem for general fixed
templates requires further short-component and reduction arguments.

## 5. Reproduction

```sh
python3 experiments/check_three_larger_source_closure.py --precision 256
```

The [checker](../experiments/check_three_larger_source_closure.py) and
[record](../repro/results/research-three-larger-source-closure.json)
verify the critical-radius, sector, real-annulus and two global-tail
margins, the original word orientation, length and carrier counts,
and the current source-induction provenance. The contour, source and
volume arguments are the written proofs above, not conclusions from
the scalar checks alone.
