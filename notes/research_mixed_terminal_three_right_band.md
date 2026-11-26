# A coherent terminal right band with an exact external product

Research deduction, 5 November 2026. The entire physical transform-index
band \(1/2\le i/N\le59/100\) can be transported to its half-period
cut while keeping the middle Newton sum coherent. Its lower and upper
real Newton tails are monotone to the same two cuts. The unaliased
part and real tails are controlled by the completed mixed-face theorem;
two Newton-alias comparisons suffice for the whole finite band.
No contour in the transform index is introduced. In particular the
external product is retained exactly when its argument crosses a sine
divisor; no holomorphic phase is asserted across that divisor.

## 1. The literal source and a zero-safe continuous rate

Use the conventions of
[the terminal Newton reduction](research_mixed_terminal_three_newton_reduction.md).
For physical \(t=i/N\), the original terminal type-three row is
\[
 N\frac{X^{-i}p_i(X)}{P_i^3}
 \sum_{l=0}^{N-1-i}(-q)^{-l}e_l(w)
                         \frac{P_{i+l}}{P_l^2},
 \quad X=e^{-2\pi ia},\quad a=y+iH.
 \tag{1}
\]
All factors, the support \(i+l<N\), the ordinary endpoint color
\(w\), and both level parities are literal. Put
\[
 y\in P=[11/50,9/20],\quad |H|\le3/25,
 \quad 1/2\le t\le59/100,\quad
 I_u=[1/10,2/5],\quad\eta=3/25.
 \tag{2}
\]
For its external product define the continuous logarithmic potential
\[
\begin{split}
 Q_a(t)&=I_a(t)-2\pi Ht,\\
 I_a(t)&=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds.
\end{split}
 \tag{3}
\]
The exact product \(X^{-i}p_i(X)\) has upper rate \(Q_a(t)\),
uniformly on (2), with any prescribed fixed positive tolerance. This
is the zero-safe numerator estimate in
[the high-Newton theorem, Section 3](research_mixed_terminal_three_high_newton.md#3-reducing-the-upper-half-double-sum-to-one-real-variable).
It remains valid when the product is zero. It is never divided out.

Only the Newton coordinate is interpolated. Its exact factor, including
the outer prefactor, is
\[
 \widehat{\mathcal I}_{N,i}(a;u,w)=
 N\frac{X^{-i}p_i(X)}{P_i^3}
 e^{i\pi(N-1)u}\mathcal E_N(u,w)
 \frac{\mathfrak P_N(t+u)}{\mathfrak P_N(u)^2}.
 \tag{4}
\]
Here \(\mathfrak P_N\) and \(\mathcal E_N\) are the exact
factorial and ordinary Newton interpolants in
[joint zero mode, equations (15a)--(15c)](research_mixed_terminal_three_joint_zero_mode.md).
At \(u=l/N\), (4) is exactly the double summand in (1).
On \(I_u+i[-\eta,\eta]\), every interpolated factorial stays
in a fixed regular strip: \(\Re(t+u)\in[.60,.99]\),
\(\Re u\in[.10,.40]\), and
\(\Re(1/2-u)\in[.10,.40]\). The possibly singular external
factor is independent of \(u\).

Write \(g(v)=J(v)+i\pi(v-v^2)/2\) and
\(V_0(u)=-2J(1/2-u)-2J(u)\). A uniform upper phase of (4)
at complete color is
\[
 \widehat R(a;t,u)=Q_a(t)+
 \Re\{V_0(u)+g(t+u)-3g(t)-2g(u)+i\pi u\}.
 \tag{5}
\]
Polynomial prefactors and an arbitrarily small rate tolerance are
understood. Small fixed ordinary-color motion adds the usual uniformly
small perturbation of \(V_0\), independently of \(t\).
Where \(0<\Re(a+t)<1\), (5) equals the real part of the
original full phase \(\mathcal T(a;t,u)\). In particular this
equality holds at the anchor \(t=1/2\). Formula (5), rather
than an extrapolated primitive, is used beyond \(\Re(a+t)=1\).

## 2. Uniform transport on the entire Newton contour

**Lemma 1.** For all targets (2) and every
\(u=z+ih\in I_u+i[-\eta,\eta]\),
\[
 \widehat R(a;t,u)
 \le\Re\mathcal T(a;1/2,u)-\frac{t-1/2}{250}.
 \tag{6}
\]
The same inequality holds after subtracting either Newton-alias
penalty \(2\pi|h|\).

*Proof.* The function (3) is absolutely continuous in \(t\),
including an integrated logarithmic zero. Almost everywhere the exact
derivative of (5) is
\[
 \partial_t\widehat R=
 \log\frac{|R-e^{-2\pi i(y+t)}|
               |1-r e^{-2\pi i(z+t)}|}
              {(2\sin\pi t)^3},\qquad
 R=e^{-2\pi H},\quad r=e^{2\pi h}.
 \tag{7}
\]
This retains both the chirp and the index-height mark. Put
\(R_*=43/20\). The elementary exponential comparison in
[the physical cap extension, equation (7)](research_mixed_physical_three_cap_right_extension.md)
gives \(e^{6\pi/25}<R_*\), so both radii lie inside
\([R_*^{-1},R_*]\). For any real angle, convexity in the
radius and comparison of these two endpoint values give
\[
 |\rho-e^{i\theta}|\le |R_*-e^{i\theta}|,
 \qquad |1-\rho e^{i\theta}|\le|1-R_*e^{i\theta}|
 \quad(R_*^{-1}\le\rho\le R_*).
 \tag{8}
\]

First let \(1/2\le t\le11/20\). The two angle ranges are
\(y+t\in[.72,1]\) and \(z+t\in[.60,.95]\). Their cosine
lower bounds are respectively \(-19/100\) and \(-81/100\).
Indeed \(\sin(.06\pi)<19/100\), while
\(\cos(\pi/5)=(1+\sqrt5)/4<81/100\).
Consequently the squared numerator in (7) is at most
\[
 (1+R_*^2+19R_*/50)(1+R_*^2+81R_*/50)
 =\frac{234539469}{4000000}
 <\left(\frac{769}{100}\frac{249}{250}\right)^2.
 \tag{9}
\]
The same cap-extension sine bound gives
\(2\sin\pi t>987/500\), and
\((987/500)^3>769/100\). Thus the ratio in (7) is strictly
less than \(249/250\).

For \(11/20\le t\le3/5\), the first angle is in
\([.77,1.05]\), where its cosine is positive. The second is
in \([.65,1]\), where its cosine exceeds \(-3/5\).
The latter follows from \(\cos(3\pi/10)=\sin(\pi/5)<3/5\).
The squared numerator is therefore less than
\[
 (1+R_*^2)(1+R_*^2+6R_*/5)
       =\frac{7378969}{160000}<\frac{231}{5}.
 \tag{10}
\]
Also \(2\sin\pi t\ge2\sin(2\pi/5)>19/10\), by
\(\cos(\pi/10)>19/20\). The denominator squared exceeds
\((19/10)^6>47\), and
\(231/235<(249/250)^2\). This again bounds the ratio by
\(249/250\). All displayed comparisons are rational after the
stated elementary sine bounds.

Since \(\log(249/250)<-1/250\), (7) is bounded above by
\(-1/250\) almost everywhere on (2). Integrating this absolutely
continuous inequality proves (6). At a zero in the external product's
continuous rate the derivative is interpreted almost everywhere;
its logarithmic singularity is integrable. The proof does not cross
a branch of a complex logarithm in \(a+t\). The alias penalty
is independent of \(t\), so it is unchanged. \(\square\)

## 3. Every real Newton tail reaches its cut

For real \(u\) in the physical support, \(0\le u<1-t\le1/2\),
the complete-color row rate is
\[
 R(a;t,u)=Q_a(t)-2J(1/2-u)-4J(u)+J(t+u)-3J(t).
 \tag{11}
\]
It is continuous at its real endpoints and equals (5). In its interior,
\[
 \exp(\partial_u R)=
 \frac{\cos^2\pi u\,\sin\pi(t+u)}{2\sin^4\pi u}.
 \tag{12}
\]
For \(0<u\le1/10\), the numerator exceeds \((9/10)^2/2\):
\(\cos(\pi/10)>9/10\), and
\(t+u\in[.5,.69]\) implies \(\sin\pi(t+u)>1/2\).
The denominator is less than \(2/3^4\), since
\(\sin(\pi/10)<1/3\). Thus (12) is greater than one.
For \(2/5\le u<1-t\), its numerator is at most one, while
its denominator exceeds \(2(9/10)^4>1\). Thus (12) is less
than one. These inequalities yield
\[
 \sup_{0\le u\le.1}R(a;t,u)=R(a;t,.1),\qquad
 \sup_{.4\le u\le1-t}R(a;t,u)=R(a;t,.4).
 \tag{13}
\]
The physical support always extends past the upper cut because
\(1-t\ge.41\). No upper-half Newton approximation or deletion
of a vanishing row is used. The original zero-safe whole-color Newton
bound and uniform factorial estimates apply up to the endpoints and
support wall, as in the high/low-Newton theorems. Therefore every
fixed ordinary derivative of these real tails has upper rate bounded
by (13), with an arbitrarily small prescribed tolerance. Restricting
either tail to a subset is allowed because this is a positive-majorant
estimate.

## 4. The exact coherent band and the two remaining alias inputs

Let \(a_*=A+iH\) be an actual terminal reference, and retain its
allocated plane \(B_\nu(a_*;y)\), actual Newton height \(h_u\),
and neighboring halfweight from
[zero-mode completion](research_mixed_terminal_three_zero_mode_completion.md).
The completed flattened transform face at \(t=1/2\) has gap
\(1/2000\) for \(u=z+ih_u\); its real-real corners and mixed
endpoints have the same gap. For all the terms in (1) with
\(1/2\le i/N\le59/100\), split only the Newton sum into its
two real tails and an inward half-grid middle interval approaching
\([.1,.4]\). On that middle interval the exact residue identity
has coefficient \(+N\). The transform coordinate remains a
physical sum, and the literal prefactor \(N\) in (1) is retained.

Deform its constant-mode Newton path to height \(h_u\), including
both joins. Apply (6) first, to bring each point to \(t=1/2\).
On the horizontal line the completed flattened face applies; at a join,
height convexity at this anchor reduces to a completed real corner or
mixed endpoint. Equations (6) and (13) likewise transport both real
tails to the completed anchor corners. Thus these contributions have
a strict finite supporting-plane gap without any new comparison.

For the Newton aliases it is enough to assume
\[
 \Re\mathcal T(y+iH;1/2,z\pm i\eta)-2\pi\eta
        \le B_0(a_*;y)-\delta_A,
 \quad y\in P,\ z\in I_u,
 \tag{14}
\]
for some \(\delta_A>0\). These are restrictions of the two
zero-other-height Newton single aliases in
[the twelve-family criterion](research_mixed_terminal_three_alias_reduction.md).
Transport each horizontal or vertical alias point using (6), preserving
its penalty. Only at \(t=1/2\) use convexity on each sign half
of a vertical alias side; its endpoints are (14) and a completed
real-real corner. The exact half-grid kernels are bounded even at
height zero. No small-height current is omitted.

**Theorem 2.** Assume (14), and put
\(\delta_0=\min(1/2000,\delta_A)\). The literal part of
\(\mathcal V_{0,N}\) with \(1/2\le i/N\le59/100\), including
its entire physical Newton sum, has allocated upper bound
\[
 |\text{allocated }\mathcal V^{\rm band}_{0,N}(y+iH,w)|
 \le \exp\{N(B_\nu(a_*;y)-\delta')\}
 \quad\text{for every }0<\delta'<\delta_0,
 \tag{15}
\]
on a sufficiently small fixed ordinary-color disk and for all
sufficiently large \(N\). Both parities and every fixed ordinary
derivative are included, after shrinking the disk as necessary.

*Proof.* The preceding estimates cover the entire literal support in
(1), with the middle Newton part kept coherent. Use the uniform
zero-safe external product bound and the original one-variable
factorial/Newton interpolation (4). Inward cuts alter limiting contour
rates by \(O(N^{-1})\). The corresponding real-tail slivers have
the same bounds by continuity at their regular cuts. Choose the color
disk and upper-rate tolerances once, and then large \(N\), to
use less than \(\delta_0-\delta'\). Residue factors, at most
\(N\) physical outer rows, and fixed contour lengths are polynomial
costs. Cauchy's formula on a smaller fixed color disk proves the
derivative conclusion. For \(\nu=1\), the actual external height
is negative and the original Fourier halfweight contributes its
favorable convex Bregman remainder, counted once. \(\square\)

This estimate removes a fixed right-hand band once (14) is known.
It does not reach transform indices above \(.59\), nor does it
claim a nonzero packet for this discarded sector. Its source may be
partitioned by the physical transform index before any Newton splitting;
the already controlled full end-index sectors are kept intact. No
bound for an arbitrary partial middle-Newton sum is inferred from the
coherent estimate in (15).
