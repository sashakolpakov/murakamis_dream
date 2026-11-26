# Quantitative local exclusion by the original shift identities

Research note, 6 November 2026.

The original-power
[formal component exclusion](research_original_power_ward_component_exclusion.md)
has a quantitative version. Smooth symbol bounds give an arbitrary
fixed inverse power of \(N\). A uniform analytic bound on a fixed
complex neighborhood gives a fixed exponential loss. The distinction
matters for the original source: its individual factorial packets have
such analytic bounds on regular compacts, but an arbitrary assembled
wrong-transport sector has not thereby acquired them.

No separate summand is assumed to satisfy a Ward identity.

## 1. Exact shift equation and its conjugated principal symbol

Use coordinates in which the original finite shifts have sizes
\(\nu/N\), with \(\nu\) in one fixed finite set \(\mathcal V\).
The coordinates may be complex. A constant linear change from
\(h=2\pi i/N\) absorbs the factors \(2\pi i\) into \(\nu\).
After legitimate denominator clearing an original local identity has
the form
\[
 L_Nu_N(x)=\sum_{\nu\in\mathcal V}
                    a_{\nu,N}(x)u_N(x+\nu/N)=r_N(x).
 \tag{1}
\]
The word and its signed powers are fixed before \(N\) varies. Suppose
the coefficients and a proposed phase \(S\) are defined on the
neighborhoods used below, and
\[
 a_{\nu,N}=a_{\nu,0}+O(N^{-1}),\qquad
 \ell(x)=\sum_{\nu}a_{\nu,0}(x)e^{\nu\cdot dS(x)},
 \qquad |\ell(x)|\ge\delta>0.
 \tag{2}
\]
The errors and derivatives in (2) are uniform to each required order.
Write
\[
 v_N=e^{-NS}u_N,\qquad f_N=e^{-NS}r_N.
 \tag{3}
\]
Then the exact conjugated operator is
\[
 A_Nv=\sum_\nu b_{\nu,N}(x)v(x+\nu/N),\qquad
 b_{\nu,N}=a_{\nu,N}e^{N\{S(x+\nu/N)-S(x)\}}.
 \tag{4}
\]
Taylor's formula gives
\(b_{\nu,N}=a_{\nu,0}e^{\nu\cdot dS}+O(N^{-1})\).
Consequently, with \(R_N=A_N-\ell\),
\[
 v_N=B_Nv_N+\ell^{-1}f_N,\qquad
 B_N=-\ell^{-1}R_N.
 \tag{5}
\]
These are exact identities; only their norm estimates use an
asymptotic expansion.

## 2. Every fixed algebraic order

Let \(K\Subset U\) be fixed nested domains, with all necessary
finite shift segments contained in \(U\). For each fixed \(m\), the
mean-value formula for \(v(x+\nu/N)-v(x)\), Leibniz' rule and (2)
give
\[
 \|B_N^m v\|_{C^0(K)}
       \le C_m N^{-m}\|v\|_{C^m(U)}.
 \tag{6}
\]
One may insert \(m\) fixed intermediate domains between \(K\) and
\(U\); for all sufficiently large \(N\), every composed shift lies
inside the next domain. Iterating (5) therefore proves
\[
 \|v_N\|_{C^0(K)}
 \le C_m N^{-m}\|v_N\|_{C^m(U)}
       +\sum_{j=0}^{m-1}C_{m,j}N^{-j}\|f_N\|_{C^j(U)}.
 \tag{7}
\]
Thus an exact homogeneous Ward identity and bounds
\(\|v_N\|_{C^m(U)}\le C_m' N^b\), with fixed \(b\), imply
\(u_N=O(N^{b-m}e^{N\Re S})\) on \(K\) for every fixed \(m\).
This is a relative estimate at the proposed sector's exponential
scale; it is not yet a fixed improvement of that scale.

A cutoff does not remove the residual term in (7). If \(u_N\) is
the whole original kernel and a cutoff is identically one on a
neighborhood containing all shifts used in the proof, (1) remains
homogeneous there. Otherwise the exact commutator and any physical
endpoint terms belong to \(r_N\). If a putative sector is only one
piece of an exact decomposition, its residual must be bounded or
canceled after assembly; the Ward equation for the total does not
set that residual to zero.

## 3. An analytic estimate with a fixed exponential gain

Suppose now all functions in (1)--(4) are holomorphic on a fixed
complex neighborhood of concentric polydisks
\[
                   D_r\Subset D_R,\qquad \rho=R-r>0,
 \tag{8}
\]
with room for the shifts at their outer boundary. Assume the
coefficient bounds in (2), the phase bounds and \(|\ell|^{-1}\)
are uniform there. Let
\[
 A_N^{\rm amp}=\|v_N\|_{D_R},\qquad E_N=\|f_N\|_{D_R}.
 \tag{9}
\]
Cauchy's estimate and (4) imply a constant \(C>0\), independent of
\(N,s,t\), such that
\[
 \|B_Nv\|_{D_s}
       \le \frac{C}{Nt}\|v\|_{D_{s+t}}
 \tag{10}
\]
whenever \(0<t\le\rho\) and
\(\max_\nu\|\nu\|/N\le t/2\). Increase \(C\) if needed to absorb
the uniform \(O(N^{-1})\|v\|\) term and the fixed value of \(\rho\).
The estimate for the shifted difference follows by integrating its
derivative on the shift segment; that segment remains at least
\(t/2\) from the outer polydisk boundary.

Choose
\[
 M\ge\max\{1,C,2\max_\nu\|\nu\|\},\qquad
 m=\left\lfloor\frac{\rho N}{4M}\right\rfloor,\qquad
 t=\rho/m.
 \tag{11}
\]
For sufficiently large \(N\), (10) has norm at most \(1/4\) at
each of these \(m\) successive domain losses. Iterating (5), and
using \(\|\ell^{-1}\|\le\delta^{-1}\), gives
\[
 \boxed{\quad
 \|e^{-NS}u_N\|_{D_r}
    \le 4^{-m}A_N^{\rm amp}
                  +\frac{4}{3\delta}E_N .
 \quad}
 \tag{12}
\]
In particular, for some \(c>0\),
\[
 A_N^{\rm amp}\le C_0N^b,\quad r_N=0
 \quad\Longrightarrow\quad
 |u_N(x)|\le C_0N^b e^{N\Re S(x)-cN}
                         \quad(x\in D_r).
 \tag{13}
\]
One can take \(c=\rho\log4/(8M)\) once \(N\) is large enough.
An exponentially small residual is retained by the second term of
(12). If the normalized outer bound is instead
\(A_N^{\rm amp}\le C_0N^b e^{\gamma N}\), the gain is only
\(c-\gamma\); positivity of that difference must be checked.

This argument uses a bounded holomorphic amplitude, not a conjectural
all-orders expansion. Cauchy's bounds supply its order-\(m\)
derivatives with factorial growth, and (11) makes the truncation
order proportional to \(N\). More generally an already established
bound \(C^m(m!)^sN^{-m}\) would optimize to a loss of order
\(\exp(-cN^{1/s})\); only \(s=1\) gives a fixed exponential rate.

## 4. Why formal cancellation alone is insufficient

There is an exact elementary shift example. Fix
\(0<\alpha<\pi\), put \(S=0\), and on the real line set
\[
 L_N=T_{1/N}-e^{i\alpha},\qquad
 u_N(x)=e^{-\sqrt N}e^{i\alpha Nx}.
 \tag{14}
\]
Then \(L_Nu_N=0\) exactly, while the proposed phase has nonzero
principal symbol \(1-e^{i\alpha}\). Every fixed derivative of \(u_N\)
is smaller than every fixed inverse power of \(N\), so its formal
symbol is zero to all orders. Nevertheless
\[
                  \frac1N\log|u_N(x)|=-N^{-1/2}\longrightarrow0.
 \tag{15}
\]
There is no fixed exponential gap below \(S=0\). On a complex strip
of width \(r>0\), its normalized supremum grows like
\(\exp(\alpha rN-\sqrt N)\), so it fails the polynomial analytic
bound in (13). This is a model for the logical distinction, not a
claim that this function is an original knot source.

## 5. What the original factorials do and do not supply

On a fixed compact subset of the original regular factorial strip,
[the exact factorial theorem, Section 4](exact_factorial_interpolation_and_complex_contours.md)
proves the holomorphic uniform estimate
\[
 G_N(Nz)=\sqrt{2N\sin\pi z}\,e^{NJ(z)}(1+O(N^{-1})).
 \tag{16}
\]
Keep a slightly larger compact in the same strip, the recorded
branches, and a fixed finite number of factors or reciprocal factors.
After removing their summed phase and their explicit powers of \(N\),
their product is uniformly bounded and holomorphic there. Cauchy's
formula gives analytic, factorial derivative bounds. Thus the local
factorials themselves permit the analytic estimate (12), without a
new optimal-truncation theorem for their Stirling series.

There are also proved assembled local examples: the
[ordinary q-Hahn packet](actual_q_hahn_full_physical_complex_packet.md),
Section 5, has a uniform holomorphic relative packet in its magnetic
variables on smaller strict physical compacts, with its channel kept
at the actual integer values. The
[complete marked-density theorem](actual_augmented_plat_local_marked_density.md)
retains the finite normal coefficients. Their stated domains and
variables cannot be enlarged by this observation.

Two hypotheses remain before applying (12) to a wrong-transport
component of a general short-filled source. First, its **assembled
original kernel germ** must obey the exact Ward equation with a
controlled residual, including original endpoint and localization
terms. Second, after division by the proposed sector exponential it
must have a polynomial analytic bound on a fixed complex neighborhood.
The factorial bounds for separate terms do not prove this bound for
a sum or integral with other phases, moving divisors, or uncontrolled
boundary currents. Holomorphy of a finite polynomial of degree
proportional to \(N\) alone permits exponential growth on that
neighborhood.

Accordingly, (7) is the quantitative smooth counterpart of the formal
exclusion, while (12) is a precise sufficient analytic upgrade.
Neither grants an independent-summand Ward identity or a whole-source
dominance theorem.

### Application audit of the existing assembled packets

The explicit coupon in Section 6 does not lie in the established
q-Hahn packet tube. Its total exponential coordinate is
\(T=e^{-2\pi i\tau}=2\). Every logarithmic lift therefore has
\(\Re\tau\in\mathbb Z\), whereas the
[full physical complex packet](actual_q_hahn_full_physical_complex_packet.md),
Sections 2--5, requires
\(1/2<\Re\tau<1\) on a fixed strict compact. Changing its logarithmic
lift does not repair this mismatch. That theorem also keeps the
channel index at its actual integer values and proves a column
packet in its magnetic variables. The
[complete-circle density](actual_augmented_plat_local_marked_density.md)
retains the source \(R^\epsilon L_N\). Neither is the whole filled
power kernel \(R^n\), and the complete-circle coupon is allowed to
have the additive parameter \(c\ne n/2\).

The completed
[mixed-word plateau packets](research_mixed_full_unselected_plateau.md)
are likewise expressed after contractions, in retained wire variables
and ordinary boundary colors. Their estimates do not assert the six
original head-generator identities for each localized sector in those
variables. One cannot substitute their analytic bounds into (12) while
silently substituting different Ward operators.

Finally, the bare all-pole part of the
[full-\(\Psi\) source](actual_full_psi_scalar_flow_cycle.md), Section 7,
has the regular factorial/dilogarithm bounds, but the original relative
cycle retains ray and cut currents. Those currents belong to the
assembled source or to its residual; the bare product bound does not
bound them.

Thus none of these existing packets supplies a new application of
(12) at the wrong-transport coupon. The missing statement is a
fixed-neighborhood analytic bound for the **whole original head
kernel**, normalized by the proposed phase, together with the exact
localized Ward equation and an exponentially controlled endpoint and
localization residual. This audit does not assert that such a bound
is impossible.

## 6. An explicit mismatch for the actual parabolic coupon

The noncharacteristic condition can be made concrete at the original
coupon used in the
[formal component exclusion](research_original_power_ward_component_exclusion.md).
Let \(A\) be its first meridian, \(P=-I+H\) its pair product, and
\(\operatorname{tr}(HA)=4\). For two transport coefficients \(c,d\), put
\[
 C_c=I+cH,\qquad C_d=I+dH,\qquad
 D=C_cAC_c^{-1}-C_dAC_d^{-1}.
 \tag{17}
\]
Since \(H^2=0\), the rank-one identity gives \(HAH=4H\).
Writing \(B=[H,A]\), one has
\(BH=4H\), \(HB=-4H\), and \(B^2=16I\). The last equality also
follows from \(\operatorname{tr}B=0\) and
\(\operatorname{tr}B^2=32\). Therefore
\[
 D=(c-d)\{B-4(c+d)H\},\qquad
 D^2=16(c-d)^2I,\qquad
 \operatorname{tr}D^2=32(c-d)^2.
 \tag{18}
\]
Its spectral radius is \(4|c-d|\). Since the row-sum operator norm
is at most twice the largest entry modulus,
\[
                     \max_{i,j}|D_{ij}|\ge2|c-d|.
 \tag{19}
\]
This matrix-entry conclusion is valid in every fixed basis; it is
not a bound on the conditioning of a varying head chart.

For the original signed power, \(d=n/2\). The rational coupon has
\(c=17/12\), so \(|c-d|\ge1/12\) for every integer \(n\), and (19)
gives a matrix-entry mismatch at least \(1/6\).

There is a stronger pointwise statement in this coupon's original
Gauss chart. Its actual input matrices, obtained from
\(V=8/19\) and input momentum \(33/5\), are
\[
 A=\begin{pmatrix}-19/8&5/24\\-363/40&3/8\end{pmatrix},
 \qquad
 H=\begin{pmatrix}3/2&-5/6\\27/10&-3/2\end{pmatrix},
 \qquad
 [H,A]=\begin{pmatrix}7&-5/3\\99/5&-7\end{pmatrix}.
 \tag{20}
\]
The first Gauss coordinate of the transported meridian is its
\((1,1)\) entry. At the proposed coefficient it is \(K_c=-9/2\);
the correct signed-power transport gives
\[
 K_d=-\frac{19}{8}+\frac{7n}{2}-\frac{3n^2}{2},\qquad
 K_c-K_d=\frac{12n^2-28n-17}{8}.
 \tag{21}
\]
For \(n\ge3\) the last expression is increasing, with value \(7/8\)
at \(3\); for \(n\le-1\) its minimum is \(23/8\) at \(-1\).
At \(n=0,1,2\) its values are respectively
\(-17/8,-33/8,-25/8\). Hence
\[
                           |K_c-K_d|\ge\frac78
                         \qquad(n\in\mathbb Z).
 \tag{22}
\]
Thus one specified generator mismatch, not just an unspecified
matrix norm, is nonzero at this actual coupon.

For a fixed \(n\), on a regular chart of the original generator
identities, the rational \(K\)-Ward symbol is precisely the
input-output discrepancy in (21), in the convention of Section 2
of the formal note. After choosing such a chart, continuity gives
a fixed smaller complex neighborhood on which its modulus is at
least \(7/16\). If a finite-shift equation is obtained by clearing
denominators, retain its principal multiplier \(d_n\): on a further
regular compact with \(|d_n|\ge\eta_n>0\), the corresponding symbol
has modulus at least \(7\eta_n/16\).

More generally the matrix bound (19) also suffices without the
special coordinates (20). For the actual reconstruction
\(G(k,e,f)=\left(\begin{smallmatrix}k&e\\kf&k^{-1}+ef\end{smallmatrix}\right)\),
write \(r_k=k-k'\), \(r_e=e-e'\), \(r_f=f-f'\). Its lower-row
differences are exactly
\[
 f r_k+k'r_f,\qquad
       -\frac{r_k}{kk'}+f r_e+e'r_f.
 \tag{23}
\]
On a fixed compact where both \(k,k'\) are units and the displayed
coordinates are bounded, (23) bounds the matrix discrepancy by a
fixed constant times \(\max\{|r_k|,|r_e|,|r_f|\}\).
Legitimate denominator clearing retains a positive lower multiplier
bound. This gives some nonzero Ward symbol and, after shrinking
around the chosen point, a scalar bound of the form (2).

No chart radius, denominator bound, coefficient constant or
iteration constant in (10)--(13) is asserted to be uniform as
\(n\) varies. These estimates make the local noncharacteristic
hypothesis explicit for each fixed power. They do not supply the
still-unproved analytic bound or residual control for an assembled
wrong-transport sector.

## 7. An upper contact of the whole-kernel envelope is characteristic

There is a consequence which does not assign a separate Ward equation
to a saddle. Let \(u_N\) be the **whole** holomorphic kernel in a fixed
regular complex chart, satisfying (1). Assume the coefficients have
the uniform analytic bounds of Section 3 on a fixed larger chart.
Define its upper-regularized joint exponential envelope by
\[
 U(x)=\lim_{\varepsilon\downarrow0}\ \limsup_{N\to\infty}\
       \sup_{|y-x|<\varepsilon}N^{-1}\log|u_N(y)|.
 \tag{24}
\]
Use balls contained in the chart and \(\log0=-\infty\). Assume
\(U\) is locally bounded above. At an interior point \(x_0\) with
\(U(x_0)\) finite, suppose it has a first-order upper contact in
**all real and imaginary coordinates**:
\[
 U(x)\le U(x_0)+\Re\sum_jp_j(x_j-x_{0,j})
                          +o(|x-x_0|).
 \tag{25}
\]
In particular this holds at a finite differentiability point, with
the real differential written uniquely as
\(dU(x_0)=\Re\sum_jp_j\,dx_j\). If the equation is inhomogeneous,
define its residual envelope by the same operation and require
\[
 U_r(x_0):=\lim_{\varepsilon\downarrow0}\ \limsup_{N\to\infty}\
       \sup_{|y-x_0|<\varepsilon}N^{-1}\log|r_N(y)|
                  <U(x_0).
 \tag{26}
\]
For the homogeneous equation \(U_r=-\infty\).
Then the original Ward equation satisfies
\[
                \sum_\nu a_{\nu,0}(x_0)e^{\nu\cdot p}=0.
 \tag{27}
\]

**Proof of the envelope facts.** The function \(U\) is upper
semicontinuous: a sufficiently small ball about a nearby point lies
in a fixed chosen ball about \(x\), which bounds its defining
limsup. For any compact \(K\), any continuous \(F\), and any
\(\varepsilon>0\), its definition and a finite subcover give,
for all sufficiently large \(N\),
\[
       \sup_K\{N^{-1}\log|u_N|-F\}
              \le \sup_K(U-F)+\varepsilon.
\]
Indeed at each center \(x\in K\) first choose a small ball on
which the eventual upper bound is \(U(x)+\varepsilon/3\);
shrink it so that \(F\) changes by less than \(\varepsilon/3\).
Choose a finite subcover and take the largest of their finite
thresholds. If \(U(x)=-\infty\), any prescribed finite local
upper bound can be used instead. Balls may extend outside \(K\);
the comparison uses only their centers in \(K\). If
\(\sup_K(U-F)=-\infty\), the conclusion instead means an
arbitrarily prescribed finite upper bound.

For finite \(U(x_0)\), successively smaller balls and the limsup
over arbitrarily large \(N\) give \(N_j\to\infty\), \(x^{(j)}\to x_0\)
with \(N_j^{-1}\log|u_{N_j}(x^{(j)})|\ge U(x_0)-1/j\).
The definition of \(U(x_0)\) supplies the reverse limsup bound.
Thus these values converge to \(U(x_0)\). Pointwise convergence
at \(x_0\) itself is not required.

**Proof of (27).** Put
\(S(x)=U(x_0)+\sum_jp_j(x_j-x_{0,j})\). If the left side of (27)
is nonzero, choose one fixed smaller chart on which its modulus
is bounded below. All coefficient, phase and inverse-symbol
bounds are now fixed. In (10), the coefficient \(O(N^{-1})\)
term is absorbed using the fixed maximum width of that chart.
Thus the constants \(C,M\) can be chosen independently of any
subsequent shrinking radius \(\rho\).

Apply (12) on the polydisks of radii \(\rho/2\) and \(\rho\)
about \(x_0\). For all sufficiently large \(N\), its first factor
is at most \(\exp(-c_0\rho N)\), with a fixed \(c_0>0\);
for example one can use \(c_0=\log4/(16M)\).
The upper contact gives
\[
       e_\rho:=\sup_{D_\rho}(U-\Re S)=o(\rho).
 \tag{28}
\]
Choose a positive fixed \(\rho\) so small that
\(e_\rho<c_0\rho/4\). By (26), shrink it further if necessary
so that the normalized residual on \(D_\rho\) is eventually
bounded by \(\exp(-\eta N)\) for some fixed \(\eta>0\):
use \(\Re S(x_0)=U(x_0)>U_r(x_0)\) and continuity of \(S\).
For this fixed disk, the compact upper estimate bounds the normalized
outer amplitude by \(\exp(N(e_\rho+\varepsilon))\) for all
sufficiently large \(N\), with any prescribed \(\varepsilon>0\).
Choose \(\varepsilon<c_0\rho/4\). Both terms of (12) then have
a fixed negative exponential rate throughout \(D_{\rho/2}\).
The attaining points \(x^{(j)}\) eventually lie in this inner
disk, while \(\Re S(x^{(j)})\to U(x_0)\). This contradicts their
attaining property. \(\square\)

This applies to each original generator identity on its regular
chart. Therefore a finite first-order upper contact of the joint
complex envelope of the whole \(R^n\) kernel lies on the original
Hurwitz graph. In particular it cannot have the wrong coupon's
differential from Section 6. The envelope is defined directly from
the family; its local finite-growth bound, a finite upper contact,
the residual estimate and its absolute geometric normalization are
not supplied by this criterion.

For the whole finite head kernel of a fixed original signed word
at the actual color, local exponential boundedness does follow
directly from the
[literal Euler/Gaussian factorization](actual_euler_gaussian_cauchy_network.md),
Sections 1--2. Put \(F_l=(Q;Q)_l\). The exact full product and
reflection give, for \(0\le l<N\),
\[
 |F_l|\le2^l,\qquad
 |F_l|^{-1}=\frac{|F_{N-1-l}|}{N}
                    \le\frac{2^{N-1-l}}N .
\]
At the actual color \(|x|=1\), the truncated shift matrices have
norm at most one, and the Gaussian diagonal and common Cartan
scalars have modulus one. Every literal transfer or factorial
diagonal therefore has norm at most a polynomial in \(N\)
times \(e^{CN}\). The fixed number of factors and head indices
preserves this bound. The whole kernel has degree \(O(N)\) in
its output head variables and inverse input head variables, so
it has the same type of bound on every fixed compact regular
head chart. This verifies the local upper boundedness in (24).
It does not verify an off-grid Ward equation for an arbitrary
continued-index formula: original finite-head projections,
exceptional rows and any endpoint terms must still be retained
in the chosen equation (1), including its residual.

The complex-coordinate condition is essential. In the example (14),
the actual sharp complex envelope is \(U(x+iy)=-\alpha y\), so
\(p=i\alpha\) and its Ward symbol is indeed
\(e^{i\alpha}-e^{i\alpha}=0\). Its restriction to the real axis
alone would give the incorrect proposed differential \(p=0\).

### What a holomorphic scalar window changes

For a holomorphic \(q\), set \(w_N=e^{-Nq}u_N\) and conjugate
the exact operator to \(L_N^q=e^{-Nq}L_Ne^{Nq}\).
Its principal symbol at a phase differential \(p\) is the
old symbol at \(p+dq\). Transporting the proposed phase from
\(S\) to \(S-q\) leaves the normalized amplitude exactly unchanged:
\[
                       e^{-N(S-q)}w_N=e^{-NS}u_N.
 \tag{29}
\]
A holomorphic Gaussian multiplier therefore does not by itself
supply the missing norm in (12). Keeping \(S\) unchanged instead
changes the Ward symbol. Also no nonconstant holomorphic window
equal to one at an interior point has modulus strictly smaller
on every direction of a surrounding complex neighborhood.
Localization by an integral transform is different; its original
shift identity must retain the translated contour boundaries.
No geometric cycle coefficient or lower bound follows solely
from graph ellipticity.
