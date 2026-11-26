# The original interface between powers three and four

Research calculation, 4 November 2026. Frozen manuscripts are unchanged.

The mixed word requires a different phase domain from the proved
homogeneous-three source class. This note gives its exact crossing
interface, a positive periodic geometric reference with its original
logarithmic periods, and a finite-level obstruction to an exact positive
operator representation. It does not prove a mixed-word source asymptotic.

## 1. The crossing interface is an original finite kernel

Retain the Newton crossing matrix \(M\), reversal \(J\), scalar
\(\kappa=q^{(N-1)^2/2}\), and full half-band cardinal vector \(h\)
from [the traced-vertex calculation](research_traced_three_vertex_endpoint.md).
Put \(A_n=JM^n\), \(Q=q^2\), and
\[
 X=e^{2\pi ix},\quad Y=e^{2\pi iy},\qquad
 c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N).
 \tag{1}
\]
The original one-crossing interface is
\[
 \boxed{\quad
 C_N(x,y):=h(x)^TMh(y)
 =\kappa c_xc_y\sum_{i=0}^{N-1}
 \frac{Y^i(Q^{-1};Q^{-1})_i}
 {(1-XQ^{-i})(Y;Q^{-1})_{i+1}} .\quad}
 \tag{2}
\]
The formula is regular when \(|X|,|Y|<1\); elsewhere apparent
poles are interpreted after multiplication by \(c_xc_y\).
It retains both level parities and all original first normals.

Indeed the exact finite binomial identity in that calculation gives
\[
 h_i(x)=\frac{c_x(-q^{-1})^i}{1-XQ^{-i}},\qquad
 (Mh(y))_i=\kappa c_y(-q)^i
 \frac{Y^i(Q^{-1};Q^{-1})_i}{(Y;Q^{-1})_{i+1}}.
 \tag{3}
\]
Their product proves (2). There is no conjugation. The exact cardinal
identity therefore gives, on any complete horizontal period,
\[
 N\int V_{3,N}(x,z)C_N(z,y)\,dz
       =h(x)^TA_3Mh(y)=V_{4,N}(x,y).
 \tag{4}
\]
The analogous insertion of \(M^r\) changes three to \(3+r\).
For an existing source row \(\ell^TB\), the operation appends
\(A_4=A_3M\) on its right, in this order. Replacing \(A_3\) by a
corner-deleted approximation in (4) would create the additional exact
error \((A_3-\widetilde A_3)M\); its former error bound cannot be
reused without estimating this product.

There is also an exact polynomial transport form with no displayed
moving denominators. For each original row put
\[
 P_j(z)=\sum_{k=0}^jM_{jk}z^k
       =\kappa(-q)^j(-qz;Q)_j,
 \qquad P_{j+1}(z)=-q(1+q^{2j+1}z)P_j(z).
 \tag{4a}
\]
Indeed \(S_j=i^jq^{-j(j+1)/2}(Q;Q)_j\) gives
\(M_{jk}=\kappa(-1)^jq^{j+k^2}{j\brack k}_Q\), so the
finite binomial theorem proves (4a), with \(P_0=\kappa\).
Expanding the original cardinal function into its \(N\) consecutive
frequencies yields
\[
 (Mh(y))_j=\frac{\kappa(-q)^j}{N}
   \sum_{\ell=j}^{N-1}
    e^{2\pi i(\ell-(N-1)/2)y}(Q^{-\ell};Q)_j.
 \tag{4b}
\]
For \(\ell<j\), the product contains \(1-Q^0\) and vanishes
exactly. The frequencies are integral at odd levels and half-integral
at even levels. Formula (4b) supplies exact triangular Fourier data,
not a positive sum or an asymptotic remainder estimate.

Boundary multiplication is a different operation. If \(E\) is an
ordinary two-boundary coefficient matrix, multiplication by a crossing
on its left boundary gives \(M^rE\). Changing its first selected
vertex power gives instead
\[
       A_{n+r}B=(M^r)^TA_nB=JM^rJ\,A_nB.
 \tag{5}
\]
Thus the proved [ordinary boundary-crossing theorem](research_boundary_crossing_packet_preservation.md)
does not perform this power change. It would require the conjugated
turn--crossing--turn operation, for which unrestricted preservation of
concentrated sources is false.

There is a useful warning visible directly in (2). Away from its
factorial ends and denominator divisors, the continuous bulk index
phase, apart from the factor \(-\pi i(x+y)\), is
\[
 f(s;Y)=\mathcal J(s)+\frac{i\pi}{2}(s-s^2)
       +s\Log Y-I_Y(s),\qquad
 e^{f_s}=\frac{Y(1-e^{-2\pi is})}{1-Ye^{-2\pi is}}.
 \tag{6}
\]
For \(Y\ne1\) the last fraction is never one. Consequently this
bulk phase has no stationary point on any regular logarithmic sheet.
The factor \((1-Xe^{-2\pi is})^{-1}\) is an amplitude only on a
contour separated from its divisors. Formula (6) does not bound the
full kernel: it says that endpoint terms, moved poles, or cancellation
must be retained when (2) is used. It cannot be substituted by a
local Gaussian crossing kernel at the old wire center.

## 2. A positive alternating reference with exact periods

Consider a periodic degree-two configuration with powers three and
four alternating. This can be read as two vertices joined by two
edges, counting both incidences. It is a geometric interface reference,
not a claim about the limit of finite complete-ended paths or about a
knot closure. Its original unit-charge equations are
\[
 3t+4i\operatorname{asinh}\{\tan(t/2)\cos(u/2)\}=2\pi,
 \qquad
 4u+4i\operatorname{asinh}\{\tan(u/2)\cos(t/2)\}=2\pi.
 \tag{7}
\]
All returns below are on their right-half-plane principal branches.

**Proposition 1.** Let \(a\) be the unique root in the complex disk
of radius \(10^{-26}\) about
\[
 a_0=.772606299919327105862744779296
             +.357976514994011533180925612135i
 \tag{8}
\]
of
\[
 p(a)=4a^4-6a^3+4a^2-2a+1.
 \tag{9}
\]
Define
\[
 B=\frac{a^2(2a-1)^2}{2(a-1)},\quad b=\sqrt B,
 \quad t=2\arccos a,\quad u=2\arccos b,
 \quad x_{34}=\frac1\pi\arcsin\sqrt{\frac{a^2B}{a^2+B}}.
 \tag{10}
\]
The square roots have positive real part; the inverse trigonometric
branches in (10) have positive real part, with \(t,u\) below and
\(x_{34}\) above the real axis. Thus explicitly
\(a=\cos(t/2)\) and \(b=\cos(u/2)\), not their full-angle
cosines. Then (7) holds with its displayed
logarithmic lift. All eight original shapes of either edge are
strictly positive. In particular,
\[
 \begin{split}
 1.61266&<\Re t<1.61268,& .95522&<-\Im t<.95524,\\
 1.43876&<\Re u<1.43878,& .69705&<-\Im u<.69707,\\
 .18299&<\Re x_{34}<.18301,& .07871&<\Im x_{34}<.07873.
 \end{split}
 \tag{11}
\]

*Proof.* The focused checker proves existence and uniqueness in (8)
by the complex Newton contraction with the fixed inverse \(1/p'(a_0)\).
It encloses the derivative on the entire radius-\(10^{-26}\) square
containing the disk and verifies the strict self-map and contraction
inequalities. The remaining assertions use exact algebra and outward
enclosures on that disk, not a floating-point solution of (7).

Write \(A=a^2\). The exact polynomial identities are
\[
 \begin{split}
 B(1-A)+\frac A2(4a^3-3a+1)&=0,\\
 A(1-B)+B(2B-1)^2
 &=\frac{a^2p(a)(16a^6-24a^5+8a^4-4a^3+8a^2-2a-1)}
                  {2(a-1)^3}.
 \end{split}
 \tag{12}
\]
They imply
\(\sinh^2r_3=-\cos^2(3t/4)\) and
\(\sinh^2r_4=-\cos^2u\), for the two returns in (7).
The sextic factor in (12) and the other quartic roots are not
discarded as if the elimination selected a branch: the root disk
and the following unsquared checks make that selection.
The candidate values
\[
             r_3^*=i(3t-2\pi)/4,
       \qquad r_4^*=i(4u-2\pi)/4
 \tag{13}
\]
have these same squared hyperbolic sines. The enclosures verify that
both actual returns and both candidates have positive real part and
imaginary part strictly between \(-\pi/2\) and zero. The alternatives
\(r=\pm r^*+k\pi i\) therefore force \(r=r^*\). This proves
the unexponentiated equations (7), without resetting a logarithmic
integer or changing a primitive period.

Put \(v=\tan(t/2)\), \(w=\tan(u/2)\), and
\(q_0=\sqrt{1+v^2+w^2}\), with \(\Re q_0>0\).
The same enclosures give
\((\Re q_0)^2>(\Re v)^2+(\Re w)^2\). The
[original positive-edge criterion](research_positive_edge_global_monotonicity.md)
therefore proves positivity of all eight ordered tetrahedra. Formula
(10) is precisely the selected original wire equation, continued in
the positive quadrant. The enclosures also verify its regular
factorial inequalities \(0<\Re x_{34}<1/4\) and
\(\Re x_{34}+\Re(t)/(2\pi),\Re x_{34}+\Re(u)/(2\pi)<1/2\).
Thus no reflected logarithm is used in identifying this reference.
The marking is the original degree-two period (7), with both incident
edges retained; nothing here identifies a periodic graph with a knot.
\(\square\)

This is a substantial change of phase center:
\[
 |x_{34}-x_h|>.035,
 \qquad x_h=1/6+i\log2/(2\pi).
 \tag{14}
\]
It is outside both the proved radius-.005 source disk and the directed
tube in [the retained three-vertex theorem](research_three_vertex_directed_packet.md).
Moreover, write \(\mathfrak b\) for the
[original incidence phase](research_unsummed_network_phase_coercivity.md).
At this reference its actual logarithmic wire derivatives obey
\[
 \begin{split}
 \mathfrak b_x(x_{34},t)&=-\mathfrak b_x(x_{34},u),\\
 .0462<\Re\mathfrak b_x(x_{34},t)&<.0463,
 \qquad .2967<\Im\mathfrak b_x(x_{34},t)<.2969.
 \end{split}
 \tag{15}
\]
For the equality, put \(C=1-2AB/(A+B)\). Direct algebra gives
\((C+2A-1)(C+2B-1)=(1-C)^2\), whereas
\(e^{\mathfrak b_x(x,t)}=(C+\cos t)/(1-C)\).
The original cosine logarithms are regular by the factorial inequalities;
their summed imaginary part lies in \((-\pi,\pi)\), so the sum is
zero, rather than a nonzero multiple of \(2\pi i\). The displayed
enclosures check the individual derivatives. A recentered alternating
phase class must therefore retain opposite nonzero momenta as well
as the new wire center. Merely moving the center of the old
zero-gradient class does not supply it.

## 3. Exact obstruction to positive similarity

For a nonzero scalar multiple of a matrix similar to a positive
Hermitian matrix, the similarity- and scalar-invariant quantity
\[
                 \frac{\operatorname{tr}(B^2)}{(\operatorname{tr}B)^2}
 \tag{16}
\]
is positive real. This holds for every choice of positive metric.
At the original level \(N=3\), direct exact arithmetic gives
\[
 \begin{split}
 \frac{\operatorname{tr}(A_4^2)}{(\operatorname{tr}A_4)^2}
    &=\frac{4854+127i\sqrt3}{6241},\\
 \frac{\operatorname{tr}((A_3A_4)^2)}
      {(\operatorname{tr}(A_3A_4))^2}
    &=\frac{2462214+14347i\sqrt3}{2588881}.
 \end{split}
 \tag{17}
\]
Both denominators are nonzero. Thus neither the single power-four
vertex nor its alternating three-four period admits such an exact
positive similarity at every level. The existing identity
\[
       MA_nM^{-1}=\kappa(M^*M)M^{n-3}
 \tag{18}
\]
cannot turn the additional crossing into a positive factor by another
similarity or scalar normalization in these examples. This rules out
only that exact operator shortcut. It says nothing against a
nonzero asymptotic coefficient, a source-specific estimate, or the
volume conjecture.

## 4. The local mixed angular phase is coercive

The original angular stationary phases can be specified without a
new transcendental root search. For \(n=3,4\), put
\[
 B_n(x,y;\tau)=\mathfrak b(x,\tau)+\mathfrak b(y,\tau)
                 +\frac{in\tau^2}{4\pi}-i\tau.
 \tag{19}
\]
At \((x,y)=(x_{34},x_{34})\), their stationary angles are
respectively \(t,u\) of Proposition 1. The same logarithmic
branches are used. For example, with \(z=e^{i\tau}\), the
power-four exponentiated equation factors exactly as
\[
 \begin{split}
 z^4(1+Xz)(1+Yz)-(X+z)(Y+z)
  =(z^2-1)\{XYz^4+(X+Y)z^3+(1+XY)z^2+(X+Y)z+XY\}.
 \end{split}
 \tag{20}
\]
The selected nontrivial branch, with \(W=z+z^{-1}=2\cos\tau\),
therefore satisfies
\[
           XYW^2+(X+Y)W+1-XY=0.
 \tag{21}
\]
At the reference diagonal it is \(W=1-X^{-1}=2\cos u\).
It is simple: \(2XYW+X+Y=2X^2\ne0\) there. Neither
\(z=1\), \(z=-1\), nor the other root of (21) is substituted
for this lifted branch. The fixed-wire return
\(r_x=\tfrac12[\Log\cos(\pi x-\tau/2)-\Log\cos(\pi x+\tau/2)]\)
equals the corresponding return in (7) at the reference: its squared
hyperbolic sine is the same by (10). Indeed, if
\(k=\sin^2(\pi x)=AB/(A+B)\), then
\(\sinh^2r_x=k(1-A)/(A-k)=B(1-A)/A\).
The same quadrant strips
fix its sign and logarithmic lift. Thus \(B_{n,\tau}=0\) there,
and analytic continuation fixes this equality locally.

Define the actual local critical phases
\(\Xi_n(x,y)=B_n(x,y;\tau_n(x,y))\). This definition specifies
the angular action; it does not assert an asymptotic for \(V_{n,N}\).
Their derivatives at the reference follow from one scalar Schur
complement. With
\(p_\pm=\tan(\pi x_{34}\pm\tau/2)\), write
\[
 \begin{split}
 d&=-\pi(p_++p_-)-2\pi\cot(\pi x_{34}),\\
 e&=(p_--p_+)/2,\\
 f_n&=-(p_++p_-)/(2\pi)+in/(2\pi).
 \end{split}
 \tag{22}
\]
Then \(f_n=B_{n,\tau\tau}\ne0\) and
\[
 \Xi_n''=
 \begin{pmatrix}d-e^2/f_n&-e^2/f_n\\-e^2/f_n&d-e^2/f_n\end{pmatrix},
 \qquad
              -\Re\Xi_3''\succ7I_2,\qquad
              -\Re\Xi_4''\succ9I_2.
 \tag{23}
\]
The checker encloses both eigenvalues, using their exact expressions
\(-\Re d\) and \(-\Re(d-2e^2/f_n)\). All inequalities are
strict and hence persist on some fixed neighborhood of the reference.
Equation (15) gives the two opposite nonzero vertex gradients.
Consequently the sum of these local phases on any alternating cyclic
word, or on an alternating open word with its boundary wires fixed
at \(x_{34}\), is stationary at this constant wire configuration.
Each free wire meets one vertex of each type, so its total negative
real Hessian is bounded below by \(16I\) at that point. Cyclic
length two retains its two parallel incidences. This is an all-length
local phase assertion; it supplies neither a local quantum amplitude
for \(V_4\) nor a complementary-cycle estimate.

## 5. The remaining finite-contour problem

For arbitrary words in \(\{3,4\}\), the exact original problem is
\(v(z)^TA_{n_1}\cdots A_{n_m}v(w)\), with the two ordinary
boundaries and all first normals retained. A possible source induction
would need packets and complementary-period estimates for the two
literal kernels \(V_3,V_4\) on domains containing the actual mixed
critical wires, together with a pair of phase classes whose gradients
match as in (15). The reference above is a necessary test of such
domains, not a proof that all finite mixed paths lie in one of them.

Equation (4) is an alternative exact construction of the missing
power-four kernel. In using it one must bound its full intermediate
Fourier period, the factorial endpoints in (2), and any poles crossed
when its index contour is moved. Equation (6) explains why the old
local three-vertex Gaussian does not provide this crossing step.
Any corner deletion also requires the new error product specified
after (4). The raw canonical bare-edge packet is already known to
fail at the homogeneous-three geometric point, so simply widening
the power-seven angular contour is not a valid substitute.

The full-packet coefficient, complementary mixed cycle, ordinary
boundary decay, and marked action normalization for these interfaces
remain to be established. A long separator can use existing boundary
composition theorems, but does not settle this adjacent \(3,4\)
problem or the finite-exception goal for an arbitrary fixed template.

Run

```sh
python3 experiments/check_three_four_source_interface.py --precision 192
```

The [record](../repro/results/research-three-four-source-interface.json)
checks exact polynomial and matrix identities and the selected
geometric root/branch enclosures. It does not certify a quantum
contour or use numerical dilogarithm calibration.
