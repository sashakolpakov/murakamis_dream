# The half-charge observation with a free outside color

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The half-charge observation and its physical normal-defect rows retain
their nonzero packets when the complete outside color is replaced by
a fixed small complex neighborhood. The input is the literal full
Newton kernel. A polynomial interpolation estimate controls it on the
whole observation contour; the local free-edge theorem supplies the
coefficient only near the saddle. Actual first normals control the
omitted physical rows.

All outside derivatives below are derivatives in the ordinary
spectral color, including at the complete color \(-2\). No conclusion
about a global coupled pair coefficient is inferred.

## 1. A whole-contour bound from the actual physical rows

Put
\[
 D=N-1,\qquad J_N=\lfloor(N-1)/2\rfloor,\qquad
 c_a=2\cos((2a+1)\pi/N),\quad 0\le a\le J_N,
\]
and retain the original polynomials
\[
 K_N(w,\zeta)=\sum_{j=0}^{D}e_j(w)e_j(\zeta),\qquad
 L_N(w,\zeta)=\sum_{j=0}^{J_N}e_j(w)e_j(\zeta),\qquad
 F_{a,N}(w)=K_N(c_a,w).
 \tag{1}
\]
Every omitted \(e_j\) is radical, and vanishes at every distinct
physical node. Thus \(L_N(c_a,w)=F_{a,N}(w)\) exactly.

Let \(Q_N\) be the monic distinct-node polynomial:
\[
 Q_N(w)=
 \begin{cases}
 2T_m(w/2),&N=2m,\\
 (w+2)\{U_m(w/2)-U_{m-1}(w/2)\},&N=2m+1.
 \end{cases}
 \tag{2}
\]
Its degree is \(J_N+1\). The exact Chebyshev formulas give
\[
 \|Q_N\|_{[-2,2]}\le4,\qquad
 |Q_N'(c_a)|^{-1}\le2/N.
 \tag{3}
\]
The odd simple node is included in (3).

**Lemma 1.** On each compact subset \(\mathcal W\) of
\(\Re w<2\), for all large \(N\),
\[
 |F_{a,N}(w)|\le |F_{J_N,N}(w)|
       \le C N^A e^{N\Re\Psi(w)}.
 \tag{4}
\]
For every fixed ordinary derivative order \(k\), uniformly for
\(w\in\mathcal W\) and all \(u\in\mathbb C\),
\[
 \left|\partial_\zeta^k L_N(w,\zeta)
                          \big|_{\zeta=-2\cos u}\right|
 \le C_k N^{A+2k+2}
            e^{N\Re\Psi(w)+J_N|\Im u|}.
 \tag{5}
\]
Here \(\Psi(-2\cos t)=\psi(t,0)\) has its original complete constant.

*Proof.* The [actual Riccati recurrence](research_physical_row_riccati_transport.md)
has positive coefficients in its entire ordinary physical range,
including the last row at each parity:
\[
 \rho_{r+1}=1+\frac{c_0-w}{A_r}
               +\frac{C_r}{A_r}(1-\rho_r^{-1}),\qquad
 \rho_1=1+\frac{c_0-w}{A_0},\quad
 A_r>0,\quad C_r\ge0.
 \tag{6}
\]
For large \(N\), \(\Re w<c_0\) on \(\mathcal W\).
If \(\Re\rho>1\), then \(\Re(1-\rho^{-1})>0\). Induction
therefore gives \(\Re\rho_r>1\), and hence \(|\rho_r|>1\),
for the normalized original solution. This proves the first
inequality in (4), without selecting a formal recurrence mode.
The second is the [last-row logarithmic theorem](research_last_physical_row_riccati.md).

The polynomial \(L_N(w,\zeta)\), of degree at most \(J_N\) in
\(\zeta\), is exactly the ordinary interpolant of the values
\(F_{a,N}(w)\). Its cardinal polynomial is
\[
 \ell_a(v)=\frac{Q_N(v)}{(v-c_a)Q_N'(c_a)}.
\]
On the real interval, the mean-value bound and Markov's inequality
give \(\|\ell_a\|_\infty\le C N\), using (3). Consequently
\[
 \|L_N(w,\cdot)\|_{[-2,2]}
                     \le C N^2 |F_{J_N,N}(w)|.
 \tag{7}
\]
The same argument applies to complex coefficients, since the
cardinal polynomials are real. Markov's inequality costs at most
a factor \(C_k N^{2k}\) for \(\partial_\zeta^k\).
For a polynomial \(P\) of degree \(d\), the elementary
Bernstein ellipse bound is
\[
 |P(-2\cos u)|\le \|P\|_{[-2,2]}e^{d|\Im u|}.
 \tag{8}
\]
It follows by applying the maximum principle to the polynomial
in \(z\) obtained from \(z^dP(-z-z^{-1})\); equivalently apply
the exterior maximum principle to the reversed polynomial.
Equations (4), (7), and (8) prove (5). \(\square\)

The original radical Fourier bound and ordinary Markov inequality
also give, for every fixed \(k\),
\[
 \left|\partial_\zeta^k(K_N-L_N)(-2\cos t,-2\cos u)\right|
 \le C_k N^{A_k}
               e^{D(|\Im t|+|\Im u|)}.
 \tag{9}
\]
Indeed every radical \(e_j\) has real interval norm at most
\(\sqrt{N-1}\); apply (8) to its two factors and sum at most \(N\)
terms. This retains the full radical, at both parities.

Choose a fixed neighborhood of the half-charge observation
rectangle \(|\Re t|\le\pi/2,\ |\Im t|\le2/5\). On a sufficiently
small such neighborhood, the
[complete-edge gap](research_internal_pair_complete_edge_gap.md)
and reflection give
\(\Re\psi(t,0)>|\Im t|+\delta_0\), for some \(\delta_0>0\).
The mapped colors form a compact subset of \(\Re w<2\).
Combining (5) and (9) proves the whole-contour estimate
\[
 \left|\partial_\zeta^k K_N(-2\cos t,\zeta)
                          \big|_{\zeta=-2\cos u}\right|
 \le C_kN^{A_k}
                   e^{N\{\Re\psi(t,0)+|\Im u|\}}.
 \tag{10}
\]
Every fixed derivative in the selected variable has the same
exponent and an additional polynomial cost: use Cauchy's formula
on radius \(1/N\) inside a slightly larger compact set. This
estimate comes from the finite polynomial, not from continuation
of a relative complete-end error.

## 2. Original physical tails and their normals

Write \(G_{a,N}(\zeta)=\partial_wK_N(c_a,\zeta)\) at a double
physical node. For every such \(a\), every fixed \(k\), and all
complex \(u\),
\[
 \begin{split}
 |\partial_\zeta^kF_{a,N}(-2\cos u)|
      &\le C_kN^{A_k}F_{a,N}(-2)e^{D|\Im u|},\\
 |\partial_\zeta^kG_{a,N}(-2\cos u)|
      &\le C_kN^{A_k}F_{a,N}(-2)e^{D|\Im u|}.
 \end{split}
 \tag{11}
\]
The first line includes the odd simple node; no original first
normal is assigned to that node.

Here is a proof of the real bounds needed for (11).
Put \(\delta=c_0-\zeta\) and
\(\Delta F_r=F_r-F_{r-1}\). The original row recurrence is
\[
 \Delta F_{r+1}=(C_r/A_r)\Delta F_r+(\delta/A_r)F_r,\qquad
 F_0=1,\quad \Delta F_1=\delta/A_0.
 \tag{12}
\]
It proves that every \(F_r\) has nonnegative coefficients in
\(\delta\). Since \(|c_0-\zeta|\le c_0+2\) on \([-2,2]\),
one obtains \(|F_a(\zeta)|\le F_a(-2)\) throughout that interval.

For the second line, the actual
[first-normal estimate, Lemma 5](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_color_path_normal_bound.md)
gives
\[
 |G_a(\zeta)|\le N^{11}F_a(\zeta)
                    \le N^{11}F_a(-2),\qquad -2\le\zeta\le c_0.
 \tag{13}
\]
It concerns the full original normal. It must not be obtained by
differentiating a physical value asymptotic.
The missing real interval \([c_0,2]\) has length \(O(N^{-2})\).
The affine map of \([-2,c_0]\) to \([-1,1]\) sends its right
endpoint \(2\) to
\[
 1+\frac{2(2-c_0)}{c_0+2}=1+O(N^{-2}).
\]
A polynomial of degree at most \(D\) therefore incurs at most
\(\exp\{D\operatorname{arcosh}(1+O(N^{-2}))\}=O(1)\)
in the Bernstein bound on this small extension. Thus (13), up
to a constant, holds in absolute value on all of \([-2,2]\).
Ordinary Markov inequalities and (8) now prove both lines of
(11), including all fixed outside normals.

For the parity-appropriate midpoint cuts \(T_N\to\pi/2\), the
positive complete rows and the absolute row normalization give
\[
 \max_{\tau_a>T_N}F_{a,N}(-2)
                 \le CN^A e^{N\psi(\pi/2,0)},\qquad
                  \tau_a=\arccos(-c_a/2).
 \tag{14}
\]
Multiplication by the original Gaussian crossing value changes
no physical modulus for real \(n\). Its logarithmic first normal
is \(O_n(N^2)\). Consequently (11)–(14) bound the omitted
source values and their actual selected first normals by
\[
 C_kN^{A_k}
                  e^{N\{\psi(\pi/2,0)+|\Im u|\}}.
 \tag{15}
\]
All constants are uniform in the physical row. The complete
half-charge gap is
\(\psi(\pi/2,0)<M_n-7/80\). Thus (15) retains a fixed gap for a
sufficiently small fixed outside-color neighborhood.

## 3. The free-outside observation packet

Fix an integer \(n\ge3\). Let \(\zeta\) denote the ordinary outside
color. Near \(\zeta=-2\), the even analytic functions
\(\psi(t,u)\) and \(a_e(t,u)\), where \(\zeta=-2\cos u\), descend
to holomorphic functions \(\widehat\psi(t,\zeta)\) and
\(\widehat a_e(t,\zeta)\). This is the
[actual free-edge theorem](research_pair_free_boundary_kernel.md).
Set
\[
 S_n(t;\zeta)=\widehat\psi(t,\zeta)+\frac{int^2}{4\pi}-\frac{it}{2}.
 \tag{16}
\]
The nondegenerate complete half-charge saddle continues uniquely
to \(t_n(\zeta)\) on a fixed disk about \(-2\). Define
\[
 \mathcal S_n(\zeta)=S_n(t_n(\zeta);\zeta),\qquad
 \mathcal A_n(\zeta)=-\partial_t^2S_n(t_n(\zeta);\zeta).
 \tag{17}
\]
At \(\zeta=-2\),
\(\mathcal A_n=(\sec(t_n/2)-in)/(2\pi)\) has positive real part.
All square roots below continue this Gaussian root.

Use the full source and its ordinary distinct-node interpolant:
\[
 \begin{split}
 h_{n,N}(w;\zeta)
  &=e^{inN\arccos(-w/2)^2/(4\pi)}K_N(w,\zeta),\\
 I_{n,N}(\,\cdot\,;\zeta)
  &=\text{its interpolant of degree at most \(J_N\) at all \(c_a\)},\\
 D_{n,N}(w;\zeta)&=(h_{n,N}(w;\zeta)-I_{n,N}(w;\zeta))/Q_N(w),\\
 \mathcal O_{n,N}(w;\zeta)
  &=\sum_a\frac{N e^{inN\tau_a^2/(4\pi)}
                    K_N(c_a,\zeta)}
                   {Q_N'(c_a)(w-c_a)}
    =\frac{NI_{n,N}(w;\zeta)}{Q_N(w)}.
 \end{split}
 \tag{18}
\]
The squared inverse cosine is the original branch holomorphic
on \(\mathbb C\setminus[2,\infty)\), including \(w=-2\).

Put \(\epsilon_N=(-1)^{\lfloor N/2\rfloor}\), and define
\[
 \begin{split}
 b_n^{\rm e}(w;\zeta)
  &=\frac{\sqrt{2\pi}}{\pi i}
   \frac{\sin t_n(\zeta)\,\widehat a_e(t_n(\zeta),\zeta)}
    {(w+2\cos t_n(\zeta))\sqrt{\mathcal A_n(\zeta)}},\\
 b_n^{\rm o}(w;\zeta)
  &=\frac{\sqrt{2\pi}}{\pi}
   \frac{\cos(t_n(\zeta)/2)\,\widehat a_e(t_n(\zeta),\zeta)}
    {(w+2\cos t_n(\zeta))\sqrt{\mathcal A_n(\zeta)}} .
 \end{split}
 \tag{19}
\]

**Theorem 2.** There is \(r_n>0\), independent of \(N\), such
that for \(|\zeta+2|<r_n\), through both level parities,
\[
 \mathcal O_{n,N}(w;\zeta)
  =\epsilon_NN^{-1}b_n^{\rm e/o}(w;\zeta)
              e^{N\mathcal S_n(\zeta)}(1+O(N^{-1})),
                         \qquad w>2.
 \tag{20}
\]
This is uniform over all real \(w>2\). The coefficient is nonzero
and comparable to \(1/(w+1)\). The normalized error is holomorphic
in \(\zeta\), with every fixed ordinary \(\zeta\)-derivative
\(O(N^{-1})\) on a smaller fixed disk. Fixed observation-color
derivatives have the corresponding holomorphic expansion.

*Proof.* Keep the exact angular contours and their orientation from
the [even](research_complete_source_pick_observation.md#5-a-nonzero-half-charge-observation)
and [odd](research_odd_half_charge_observation.md#1-the-full-node-polynomial-and-exact-angular-contour)
source identities, replacing their complete kernel by
\(K_N(-2\cos t,\zeta)\). Their residues are precisely (18);
no interpolation in the selected angle is introduced.
The odd ramified pole at \(t=0\) still contributes
\(\epsilon_N h_{n,N}(-2;\zeta)/(w+2)\), exactly once.

At \(\zeta=-2\), all connectors and all noncritical horizontal
parts have a strict exponential gap. Estimate (10) increases their
upper exponents by at most \(|\Im u|\), while (15) does the same
for the omitted physical rows. If \(|\zeta+2|\) is small, either
local solution of \(-2\cos u=\zeta\) has \(|u|\) small. Thus these
gaps persist uniformly on a fixed ordinary color disk, also
relative to the continuously varying \(\Re\mathcal S_n(\zeta)\).

Near the complete saddle use the genuine two-variable free-edge
packet, valid on one fixed neighborhood. The local contour may
be deformed inside this neighborhood through \(t_n(\zeta)\);
its endpoints stay in the gapped portion, and the observation
pole is uniformly separated. No global contour claim is needed
for this local deformation. The exact folded lower denominators
are \(1+e^{-iNt}\) and \(1-e^{-iNt}\), respectively. Their
nonconstant parts stay exponentially small because the height
is bounded below by a positive constant near the saddle.
The folded scalars and amplitudes are respectively
\(\epsilon_NN\sin t/(\pi i)\) and
\(\epsilon_NN\cos(t/2)/\pi\). Combining the factor
\(N^{-3/2}\widehat a_e\) with the Gaussian factor
\(\sqrt{2\pi/N}/\sqrt{\mathcal A_n}\) gives exactly (19)–(20).

For real \(w>2\), multiplying the rational amplitudes by \(w+1\)
gives a uniformly bounded holomorphic family, bounded away from
zero at the saddle. The physical tails have at most polynomial
loss from \(w-c_a\), uniformly after the same multiplication.
This proves the stated uniformity. Evenness in \(u\) ensures
holomorphy in the ordinary color disk; Cauchy's formula applied
to the normalized error proves its ordinary derivative claims.
In particular an angular derivative vanishing at \(u=0\) has
not been substituted for an ordinary outside normal. \(\square\)

## 4. Uniform physical defects and exterior pair colors

**Theorem 3.** On a smaller fixed disk \(|\zeta+2|<r_n\),
uniformly over every distinct physical node,
\[
 D_{n,N}(c_a;\zeta)
  =-\epsilon_NN^{-2}b_n^{\rm e/o}(c_a;\zeta)
                     e^{N\mathcal S_n(\zeta)}(1+O(N^{-1})).
 \tag{21}
\]
The normalized error has all fixed ordinary outside-color
derivatives \(O(N^{-1})\). The coefficients in (21) are uniformly
bounded above and away from zero, so the actual defect values
are nonzero for all sufficiently large levels.

*Proof.* Use the exact pole cancellation in the
[physical normal-defect packet](research_physical_normal_defect_packet.md).
If \(I^{\rm tail}\) interpolates the omitted source values and
zero on all retained nodes, the omitted Cauchy sum is
\(NI^{\rm tail}/Q_N\). At an outside physical node the exact
identity is
\[
 D_{n,N}(c_a;\zeta)
 =\frac{\partial_wh_{n,N}(c_a;\zeta)
                   -\partial_wI^{\rm tail}_{n,N}(c_a;\zeta)}
                  {Q_N'(c_a)}
                -\frac{\mathcal J_{n,N}(c_a;\zeta)}N.
 \tag{22}
\]
At an inside node it is \(D=-(\mathcal J+\mathcal T)/N\).
The first term in (22), and the inside tail, have a fixed gap
by (15) and the polynomial cardinal differentiation bounds.
Those bounds commute with ordinary outside derivatives.
The odd simple node is inside and uses its ramified residue,
not an original first normal.

The contour packet for \(\mathcal J(c_a;\zeta)\) is uniform
over all \(c_a\in[-2,2]\). Its horizontal Cauchy denominators
are uniformly separated; on the midpoint vertical sides they
cost at most \(O(N)\), already absorbed by the strict gap.
At the perturbed saddle \(c_a+2\cos t_n(\zeta)\) stays uniformly
away from zero. The proof of Theorem 2 therefore gives
\(\mathcal J(c_a;\zeta)=
\epsilon_NN^{-1}b_n^{\rm e/o}(c_a;\zeta)
e^{N\mathcal S_n(\zeta)}(1+O(N^{-1}))\).
Substitute in the exact identities to obtain (21).
Uniform holomorphy and a smaller outside disk give the normalized
derivative conclusion. \(\square\)

There is also a local consequence at each actual unit-charge
positive pair of fixed integer powers \(n,p\ge3\). Let \(t_*\)
be its angle at the power-\(n\) vertex. The independent
[pair-to-half-charge theorem](research_pair_half_charge_action_gap.md)
places \(t_*\) strictly outside the half-charge rectangle and
gives \(\Re S_n(t_*;-2)>\Re\mathcal S_n(-2)\).
These strict inequalities persist for \(t\) near \(t_*\) and
\(\zeta\) near \(-2\). The exact exterior residue formula
therefore yields, with some fixed \(\delta>0\),
\[
 \begin{split}
 D_{n,N}(-2\cos t;\zeta)
 &=\frac{h_{n,N}(-2\cos t;\zeta)}{Q_N(-2\cos t)}
                       (1+O(N^{-1/2}e^{-\delta N}))\\
 &=\epsilon_NN^{-3/2}\chi_{\rm e/o}(t)
      \widehat a_e(t,\zeta)e^{NS_n(t;\zeta)}(1+O(N^{-1})),\\
 \chi_{\rm e}(t)&=1,\qquad
 \chi_{\rm o}(t)=\frac{i}{2\sin(t/2)}.
 \end{split}
 \tag{23}
\]
All fixed ordinary derivatives in both colors are retained,
in the differentiated holomorphic sense.

The original crossing carrier
\(C_{N,n}=\exp\{\pi in(N-1)^2/(4N)\}\) was omitted in (18)
and is restored exactly once in an original trace. At odd
levels the top-degree correction is still present. With
\(\ell_{n,N}(\zeta)=[w^m]I_{n,N}(w;\zeta)\),
\[
 \phi_N[R^nK_N(\,\cdot\,,\zeta)e_m]
     =C_{N,n}(-1)^mN\ell_{n,N}(\zeta),\qquad
 N\ell_{n,N}(\zeta)
     =\lim_{w\to+\infty}w\,\mathcal O_{n,N}(w;\zeta).
 \tag{24}
\]
Thus this endpoint also has the nonzero packet obtained from
(20), with coefficient \(b_{n,\infty}^{\rm o}(\zeta)\).
Formula (24) is the original odd rank-one term, not a missing
physical first normal.

These results provide a free-outside source packet and the
whole-contour and omitted-row estimates needed for composition.
They do not justify replacing a coherent shared-index transform
by its finite-order physical-row expansion. The remaining joint
cycle and its possible cancellations require their own estimate.

## 5. Whole outside-period decay, with a complex strip

The complete half-charge contour also gives an upper bound on the
whole outside period. This assertion concerns the exact observation
and the exact defect values; it does not continue the local relative
expansion (20) to distant outside colors.

**Theorem 4.** For each fixed integer \(n\ge3\) there are
\(c,B,h_*>0\) such that, for every fixed ordinary derivative
order \(k\), some \(C_k,A_k\) satisfy
\[
 \begin{split}
 &(w+1)\left|\partial_\zeta^k
          \mathcal O_{n,N}(w;\zeta)\right|
       +\max_a\left|\partial_\zeta^k
          D_{n,N}(c_a;\zeta)\right|\\
 &\hspace{10mm}\le C_kN^{A_k}
       \exp N\{M_n-c(1-\cos u)+Bv^2\},\\
 &\qquad \zeta=-2\cos(u+iv),\quad
             -\pi\le u\le\pi,\quad |v|\le h_*,\quad w>2.
 \end{split}
 \tag{25}
\]
The constants are independent of the physical row and of the
level parity. The odd top trace in (24), and each of its fixed
ordinary outside derivatives, obeys the same upper exponent.

*Proof.* Keep the complete half-charge rectangle of height \(H_0\).
After the exact folding of its horizontal sides, choose a small
fixed neighborhood of the unique saddle on the lower side.
Its closure lies in the domain of the free-edge theorem. On
this neighborhood the
[whole-period edge estimate](research_pair_free_boundary_kernel.md#7-whole-outside-period-decay-and-a-complex-strip)
gives, including all fixed ordinary outside derivatives,
\[
 |K_N(-2\cos t,-2\cos(u+iv))|
 \le CN^A\exp N\{\Re\psi(t,0)
                    -\kappa(1-\cos u)+B_0v^2\}.
 \tag{26}
\]
The original crossing and the lower sine or cosine denominator
add exactly the terms which turn \(\Re\psi(t,0)\) into
\(\Re S_n(t;-2)\), up to bounded factors. This real part is at
most \(M_n\) on the complete horizontal side. The denominator's
nonconstant term is retained and uniformly bounded there.
Consequently the contribution of this saddle neighborhood has
the upper exponent in (25), with \(c\le\kappa\) and \(B\ge B_0\).
No assumption about the location of a saddle for distant \(u\)
is made.

Every other horizontal piece, each vertical connector, and the
original omitted physical rows have a complete-outside gap.
Let \(\delta>0\) be a common lower bound for that gap, after
removing the small saddle neighborhood. Equations (10) and (15)
bound these pieces, for arbitrary real \(u\), by
\[
 CN^A\exp N\{M_n-\delta+|v|\}.
 \tag{27}
\]
Their ordinary outside derivatives have the same exponent by
(10) and (11). Shrink the strip so that \(|v|\le\delta/4\),
and choose \(c\le\delta/8\). Since \(1-\cos u\le2\),
\[
 M_n-\delta+|v|
 \le M_n-\frac{3\delta}{4}
 < M_n-c(1-\cos u).
 \tag{28}
\]
Thus these full error sectors retain the angular loss as well.
This use of a fixed gap is why no individual angular decay of
every omitted normal row is required.

For the observation, all Cauchy factors have the polynomial
uniform bounds used in Theorem 2, after multiplication by \(w+1\).
For a physical defect row, use its exact inside or outside
identity (22). The saddle Cauchy factors are uniformly bounded
over the entire real physical interval. The midpoint vertical
factors cost only powers of \(N\). Its additional regular
first-normal and tail-interpolant terms satisfy (27) by (11),
(14), and the fixed polynomial collocation bounds. This proves
(25), with every physical row included.

All derivatives here act on the ordinary polynomial color
\(\zeta\). On the saddle neighborhood this is part of (26);
on the complement it follows from the proved polynomial bounds,
including at \(\zeta=\pm2\). In particular no division by
\(\sin u\) or loss of an endpoint normal is used.
Finally multiply the exact finite observation (18) by \(w\) and
let \(w\to+\infty\) in the bound (25). Formula (24) transfers
the result to the original odd top term. The original crossing
carrier has unit modulus. This proves the theorem. \(\square\)

The inequalities in (25) are upper bounds for genuine source
observations, with an independently proved local nonzero packet
from Theorems 2–3. They leave the signed shared-wire closure and
its global cycle coefficient open.
