# A uniform packet for the physical normal-defect rows

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The half-charge observation determines the actual interpolation-normal
defect at every physical row, not only at complex geometric colors.
Rows outside the shifted contour require an exact cancellation of two
Cauchy poles. The remaining regular part has a smaller exponential
rate, by the original first-normal bound and polynomial collocation
estimates. This gives one uniform source packet at both parities.

The result concerns the specified complete-end source. It does not
justify applying an exponentially ill-conditioned shared-index
transform to a relative \(O(N^{-1})\) row error.

## 1. Unified notation and statement

For even \(N=2m\), use
\[
 Q_N(w)=2T_m(w/2),\qquad
 \mathcal L_N(w)=\sum_{j=0}^{m-1}e_j(w)e_j(-2).
\]
For odd \(N=2m+1\), use
\[
 Q_N(w)=(w+2)\{U_m(w/2)-U_{m-1}(w/2)\},\qquad
 \mathcal L_N(w)=K_N(w,-2).
\]
In both cases \(Q_N\) is the monic polynomial of all distinct
physical roots \(c_a\), and \(\epsilon_N=(-1)^m\). Set
\[
 \begin{split}
 h_{n,N}(w)&=
   e^{inN\arccos(-w/2)^2/(4\pi)}\mathcal L_N(w),\\
 I_{n,N}&=\text{the ordinary interpolant of \(h_{n,N}(c_a)\)
                       at all distinct physical roots},\\
 D_{n,N}(w)&=\frac{h_{n,N}(w)-I_{n,N}(w)}{Q_N(w)} .
 \end{split}
 \tag{1}
\]
The analytic branch of the squared inverse cosine is the one
fixed on \(\mathbb C\setminus[2,\infty)\). At every double root,
\[
             h'_{n,N}(c_a)-I'_{n,N}(c_a)=Q_N'(c_a)D_{n,N}(c_a)
 \tag{2}
\]
is the actual first-normal difference. At the odd simple root
there is no original first normal; \(D_{n,N}(-2)\) is a value
of the holomorphic function (1). The odd trace uses its separate
top-degree term, as in the
[exact odd trace formula](research_odd_half_charge_observation.md#3-the-original-odd-trace-still-has-its-top-degree-term).

Let \(t_0=a_0-iH_0\) be the half-charge saddle at fixed real
\(n\ge3\), and write
\[
 \begin{split}
 nt_0+2i\operatorname{asinh}\tan(t_0/2)&=\pi,\\
 S_n(t)&=\Psi(t)+int^2/(4\pi)-it/2,\quad
 \mathcal S_n=S_n(t_0),\quad M_n=\Re\mathcal S_n,\\
 A_n&=\{\sec(t_0/2)-in\}/(2\pi),\\
 b_n^{\rm e}(w)&=\frac{\sqrt{2\pi}}{\pi i}
    \frac{\sin t_0\,a_e(t_0,0)}
         {(w+2\cos t_0)\sqrt{A_n}},\\
 b_n^{\rm o}(w)&=\frac{\sqrt{2\pi}}{\pi}
    \frac{\cos(t_0/2)a_e(t_0,0)}
         {(w+2\cos t_0)\sqrt{A_n}}.
 \end{split}
 \tag{3}
\]
These are exactly the coefficients of the proved
[even](research_complete_source_pick_observation.md#5-a-nonzero-half-charge-observation)
and [odd](research_odd_half_charge_observation.md#2-the-half-charge-packet-and-the-exterior-residue)
observations, with their original normalization.

**Theorem 1.** Uniformly over all distinct physical roots, as \(N\)
tends to infinity through its stated parity,
\[
 \boxed{\quad
 D_{n,N}(c_a)
    =-\epsilon_N N^{-2}b_n^{\rm e/o}(c_a)e^{N\mathcal S_n}
                                  (1+O(N^{-1})).
 \quad}
 \tag{4}
\]
The error constant may depend on the fixed crossing time.
Both rational coefficients in (3) are bounded above and away
from zero on the whole real interval \([-2,2]\). Thus all these
defect values are nonzero for sufficiently large levels.

## 2. The source tail, including its actual first normals

Choose the parity-appropriate midpoint cuts \(T_N\to\pi/2\)
used in the observation proofs. Split the nodes into the
inside set \(\tau_a<T_N\) and the outside set \(\tau_a>T_N\),
where \(\tau_a=\arccos(-c_a/2)\).
Let \(I^{\rm tail}_{n,N}\) interpolate \(h_{n,N}(c_a)\) at
the outside nodes and zero at all inside nodes. The omitted
Cauchy sum is exactly
\[
 \mathcal T_{n,N}(w)
     =N\,\frac{I^{\rm tail}_{n,N}(w)}{Q_N(w)}.
 \tag{5}
\]

The positive physical-row recurrence and its endpoint normalization
give, uniformly over the outside nodes,
\[
 |\mathcal L_N(c_a)|\le CN^A e^{N\Psi(\pi/2)}.
 \tag{6}
\]
Indeed the complete values decrease with increasing \(\tau_a\);
the first omitted row lies at \(\pi/2+O(N^{-1})\).
Its absolute logarithmic asymptotic has this rate.

The same exponential bound holds for the actual first derivative
of \(\mathcal L_N\) at the outside nodes. These nodes are double
at both parities. The
[all-color first-normal bound, Lemma 5](research_all_color_path_normal_bound.md#5-the-complete-normal-determinant-at-every-color-assignment)
gives
\[
 |\partial_zK_N(c_a,-2)|\le N^{11}K_N(c_a,-2).
\]
At odd levels \(\mathcal L_N=K_N(\,\cdot\,,-2)\).
At even levels their radical difference has polynomial real
interval norm and polynomial first ordinary derivative, by
the [radical Fourier bound](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials)
and the ordinary Markov inequality. Since every physical
complete value is at least one, that polynomial correction
is absorbed in (6). The crossing's logarithmic derivative
at a double root is \(inN\tau_a/(4\pi\sin\tau_a)=O_n(N^2)\).
Consequently
\[
 \max_{\rm outside}
   \{|h_{n,N}(c_a)|+|h'_{n,N}(c_a)|\}
                    \le CN^A e^{N\Psi(\pi/2)}.
 \tag{7}
\]
This is an estimate of the original first normals, not a
derivative of a value-only asymptotic.

Ordinary collocation on these nodes costs only powers of \(N\).
In fact \(\sigma_a=N/Q_N'(c_a)\) obeys
\[
       2/N\le|\sigma_a|\le2,\qquad
       |c_a-c_b|\ge4/N^2\quad(a\ne b),
 \tag{8}
\]
with the odd simple weight of modulus one included.
The first inequalities follow from the explicit Chebyshev
weights; the second follows from the sine difference formula
for the physical nodes. The cardinal differentiation matrix
has off-diagonal entries
\[
             \frac{Q_N'(c_a)}
                  {Q_N'(c_b)(c_a-c_b)}
\]
and diagonal entries \(\sum_{b\ne a}(c_a-c_b)^{-1}\).
It therefore has infinity norm at most \(CN^4\).
By (7),
\[
 \max_a |(I^{\rm tail}_{n,N})'(c_a)|
                       \le CN^A e^{N\Psi(\pi/2)} .
 \tag{9}
\]
Also \(1/|Q_N'(c_a)|\le2/N\).

## 3. Exact cancellation and a uniform contour packet

Let \(\mathcal J_{n,N}(w)\) be the exact shifted cosine or sine
contour, without its omitted physical rows. At an inside
physical node the interior residue identity gives
\[
 D_{n,N}(c_a)
       =-\frac{\mathcal J_{n,N}(c_a)+\mathcal T_{n,N}(c_a)}{N}.
 \tag{10}
\]
The tail sum has no pole there. Its node gaps (8), weights
bounded by two, and (7) bound it by
\(CN^A e^{N\Psi(\pi/2)}\).

At an outside node use the exterior identity and (5) before
taking the limit:
\[
 D_{n,N}(w)
    =\frac{h_{n,N}(w)-I^{\rm tail}_{n,N}(w)}{Q_N(w)}
                           -\frac{\mathcal J_{n,N}(w)}N .
\]
The numerator vanishes at that node. Hence the exact regular
value is
\[
 D_{n,N}(c_a)
   =\frac{h'_{n,N}(c_a)-(I^{\rm tail}_{n,N})'(c_a)}
                  {Q_N'(c_a)}
                       -\frac{\mathcal J_{n,N}(c_a)}N .
 \tag{11}
\]
Equations (7)–(9) bound the first term by
\(CN^A e^{N\Psi(\pi/2)}\). Thus the same conclusion holds
at every node:
\[
 D_{n,N}(c_a)
       =-\frac{\mathcal J_{n,N}(c_a)}N
                              +O(N^A e^{N\Psi(\pi/2)}).
 \tag{12}
\]

The contour proof of the observation packet is uniform at all
these real evaluation colors. Here is the point requiring care.
On the two horizontal sides, \(-2\cos z\) is a compact curve
disjoint from \([-2,2]\), so the Cauchy denominator is uniformly
bounded away from zero. On each midpoint vertical side,
\[
 |-2\cos\tau_a+2\cos(T_N+iv)|\ge c/N
                  \qquad(|v|\le H_0)
 \tag{13}
\]
for all physical nodes and all sufficiently large levels.
To see this, for \(|v|\ge1/N\) use
\(2|\sin T_N\sinh v|\ge c/N\).
For \(|v|<1/N\), the physical angles are at least \(\pi/N\)
from the midpoint \(T_N\), and \(T_N=\pi/2+O(N^{-1})\).
Their real cosine separation is at least \(c/N\), whereas
the perturbation \(\cos T_N(\cosh v-1)\) is \(O(N^{-3})\).
This proves (13).

Thus near the vertical cut the Cauchy factor costs only a
power of \(N\). The vertical and noncritical horizontal parts
already have a fixed exponential gap. At the saddle itself
\(c_a+2\cos t_0\) is uniformly separated from zero for
\(c_a\in[-2,2]\), because \(\Im\cos t_0\ne0\).
The usual local expansion is consequently uniform over
the full physical interval:
\[
 \mathcal J_{n,N}(c_a)
     =\epsilon_N N^{-1}b_n^{\rm e/o}(c_a)e^{N\mathcal S_n}
                                    (1+O(N^{-1})).
 \tag{14}
\]
The source tail satisfies
\(\Psi(\pi/2)<M_n-7/80\), by the proved half-charge
comparison. Substituting (14) in (12) and absorbing the
polynomially weighted exponential error proves (4).

The odd endpoint \(c_m=-2\) lies in the inside set, so it uses
(10) and its exact ramified residue. No nonexistent odd
physical first normal was used in (7) or (11).

## 4. What can be transported from this estimate

Equation (4) gives a nonzero source coefficient for every actual
physical normal-defect row, with one common exponential phase
and the explicit rational observation profile. It can be used
inside identities that retain the whole original finite source.

It does not license replacing the rows by their leading terms
inside an arbitrary oscillatory shared-index sum. Such a sum
can magnify the \(O(N^{-1})\) row error exponentially relative
to its signed value. The exact Cauchy or reduced-node expression
must be retained until the relevant collective contour has
been controlled. Likewise the odd top-degree trace term remains
the one displayed in the linked odd-level note.

## 5. A fixed complex neighborhood of the retained real interval

The physical-row estimate has a holomorphic extension away from the
spectral endpoint \(2\). This matters for the reduced-node Cauchy
formula: its contour can be kept a fixed distance from the nodes.
The extension still uses the literal low complete-end source in (1).
It does not assert an estimate for the full even off-grid kernel.

**Theorem 2.** Fix real \(n\ge3\) and \(0<\delta<4\). There is
an open neighborhood \(\mathcal U\) of \([-2,2-\delta]\), independent
of the level, on which
\[
 D_{n,N}(w)=-\epsilon_NN^{-2}b_n^{\rm e/o}(w)e^{N\mathcal S_n}
                         (1+O(N^{-1})).
 \tag{15}
\]
The error is uniform on a fixed smaller neighborhood, including
every fixed ordinary spectral derivative in the differentiated
holomorphic sense. In particular the actual defect is nonzero there
for all sufficiently large levels of the stated parity.

*Proof.* Put \(T_\delta=\arccos(-1+\delta/2)<\pi\), and choose
\[
             \max(T_\delta,\pi/2)<T<\pi.
 \tag{16}
\]
Let \(T_{0,N}\to\pi/2\) and \(T_N\to T\) be physical midpoint
cuts of the appropriate parity. Use the original half-charge
contour of height \(H_0\) for \(|\Re t|\le T_{0,N}\). At each
of its two real ends join vertically to a smaller positive height
\(\varepsilon\), then continue at that height to \(\pm T_N\).
Close by the vertical sides at \(\pm T_N\), and use the reflected
upper boundary. This is one closed, symmetric angular contour.
The two vertical joins at \(\pm T_{0,N}\) are retained parts of
the old midpoint sides, not discarded deformation terms.

We choose \(\varepsilon\) small enough to prove a strict gap on
every added piece. The actual complete-end low polynomial satisfies
\[
 \mathcal L_N(-2\cos t)
       =\exp\{N\Psi(t)+O(\log N)\}
 \tag{17}
\]
on compact subsets of \(\Re(-2\cos t)<2\), at both parities.
This is the [even low-kernel theorem](research_even_complete_low_kernel.md#5-consequence-for-the-geometric-exponential-rate)
and the [odd last-row theorem](research_last_physical_row_riccati.md#5-the-actual-complete-end-kernel-at-odd-levels),
with their actual logarithmic normalization. Since \(T<\pi\),
the outer pieces lie in such a compact subset for sufficiently
small \(\varepsilon\).

On the real interval, \(\Psi\) is even and strictly decreasing
on \((0,\pi)\), because
\(\Psi'(a)=-\operatorname{asinh}(\tan(a/2))/\pi<0\).
Write \(g=M_n-\Psi(\pi/2)>7/80\). Uniform continuity on the
fixed outer interval permits \(\varepsilon>0\) so small that
\[
 \Re\Psi(a+ih)+\frac{n|a h|}{2\pi}
           \le \Psi(\pi/2)+g/3<M_n
 \quad
 \left\{\begin{array}{l}
 \pi/2-o(1)\le|a|\le T+o(1),\\
 |h|\le\varepsilon.
 \end{array}\right.
 \tag{18}
\]
The \(o(1)\) allowances here are just the midpoint errors
\(O(N^{-1})\); choose a fixed margin first, then take large \(N\).
The exact cosine or sine denominator has size at most
\(C e^{-N|h|/2}\) after inversion on the horizontal pieces and
on the outer midpoint sides. Thus (18) bounds all these pieces,
even after dropping that favorable exponential factor.
On the two joins at \(\pm T_{0,N}\), the already proved
half-charge connector bounds apply to every height between
\(\varepsilon\) and \(H_0\). Their fixed gap is unchanged.

The image of the fixed limiting symmetric angular boundary under
\(t\mapsto-2\cos t\) encloses \([-2,2-\delta]\) and is
separated from it. Choose \(\mathcal U\) with compact closure
strictly inside that image, separated from the boundary and from
the omitted real physical nodes \(\tau_a>T_N\). Choose these
separations with a positive fixed margin. The midpoint adjustments
then leave \(\mathcal U\) inside every sufficiently large level's
contour, with the same separation bounds. All angular
Cauchy denominators are then uniformly bounded, with their fixed
\(w\)-derivatives. The saddle color \(-2\cos t_0\) lies on
the boundary, so \(b_n^{\rm e/o}\) has no pole or zero on this
smaller neighborhood.

Let \(\mathcal J^{\rm tap}_{n,N}(w)\) be the exact observation
integral on this tapered contour, with the original parity scalar,
and let \(\mathcal T^{\rm tap}_{n,N}(w)\) be its omitted
physical Cauchy sum. Every target color is inside, so the exact
interior residue identity gives
\[
 D_{n,N}(w)=-\frac{
       \mathcal J^{\rm tap}_{n,N}(w)
       +\mathcal T^{\rm tap}_{n,N}(w)}{N}.
 \tag{19}
\]
At the physical nodes this identity is interpreted by its removable
continuation. It retains the odd simple-node residue exactly.
The same positive physical-row monotonicity used in (6), now at
\(T_N\), bounds the omitted sum by
\(N^A e^{N\Psi(T)}\), uniformly on \(\mathcal U\). The
denominators are separated there, and \(\Psi(T)<\Psi(\pi/2)\).

The central horizontal pieces and their nonzero saddle are the
original ones. All added pieces, joins and omitted rows have the
strict gaps just proved. Therefore the local Gaussian computation,
including the two equal angular copies and the parity scalar,
gives
\[
 \mathcal J^{\rm tap}_{n,N}(w)
       =\epsilon_NN^{-1}b_n^{\rm e/o}(w)e^{N\mathcal S_n}
                                      (1+O(N^{-1}))
 \tag{20}
\]
uniformly on \(\mathcal U\). Equations (19)–(20) prove (15).
The functions and normalized remainder are holomorphic; Cauchy's
formula on smaller neighborhoods proves the derivative statement.
No physical value or first normal has been replaced before taking
the exact observation. \(\square\)

Here is an explicit consequence for the even reduced-node transform.
It estimates the whole source, without substituting a finite
asymptotic expansion into an increasing-order divided difference.
Fix \(0<\alpha<1/2\), and choose a fixed positively oriented
contour \(\Gamma\subset\mathcal U\) around the real interval
containing all \(c_a\) with \(a\ge\alpha N\), for large \(N\).
Such a choice is possible by taking
\(0<\delta<2-2\cos(2\pi\alpha)\) in Theorem 2.
The contour can be chosen at a fixed positive distance from this
interval. For \(x\in[\alpha,1/2]\), set
\[
 J(x)=\int_0^x\log(2\sin\pi r)\,dr,\qquad
 V_x(z)=\int_x^{1/2}\log|z-2\cos(2\pi r)|\,dr.
 \tag{21}
\]
Then, uniformly for \(\alpha N\le j<N/2\), the original trace
in the [reduced-node formula](research_complete_source_pick_observation.md#7-complex-colors-and-the-exact-normal-defect)
satisfies
\[
 \left|\phi_N[R^n\mathcal L_Ne_j]\right|
  \le C N^A\exp\!\left\{
      N\left[M_n-2J(j/N)-\min_{z\in\Gamma}V_{j/N}(z)\right]
                  \right\}.
 \tag{22}
\]
Indeed \(|D_{n,N}|\le C N^{-2}e^{NM_n}\) on \(\Gamma\),
while the exact trace has prefactor \(N^2/S_j^2\) and denominator
\(Q_{j,N}\). Uniform midpoint summation on this separated contour
gives
\(\log|Q_{j,N}(z)|=NV_{j/N}(z)+O(1)\), and the original sine
factorial gives \(\log S_j=NJ(j/N)+O(\log N)\). These are
upper bounds applied to the exact contour, proving (22).

The potential in (22) is explicit, but no comparison of its minimum
with the pair's geometric rate is asserted here. In particular,
holomorphic control on a fixed contour does not by itself make the
relative \(O(N^{-1})\) error small after an order-\(N\) divided
difference. The grouped block currents remain part of the original
pair calculation.

The exact vanishing moments give a familiar polynomial-approximation
version of (22), but that version does not reach the pair rate.
Here is a quantitative comparison that fixes its scope. Let
\(N=4k+2\), \(j=k\). Then \(c_j=0\), the retained nodes lie
in \([-2,0]\), and their divided difference has order \(k\).
For a Bernstein ellipse of parameter \(\rho>1\) around this
interval, suppose the whole actual defect obeys
\(\sup|D_{3,N}|\le N^A e^{NM_3}\) there. Standard Chebyshev
truncation gives a degree-\((k-1)\) polynomial with error at most
\(C N^A e^{NM_3}\rho^{-k}\). Explicitly, apply Cauchy's
coefficient estimate to
\(D_{3,N}(-1+(z+z^{-1})/2)\) on \(|z|=\rho\): its
Chebyshev coefficients obey
\(|a_\ell|\le2\sup_{E_\rho}|D_{3,N}|\rho^{-\ell}\), and
summing the geometric tail proves this error bound.
The divided difference annihilates
that polynomial exactly. Since
\[
 \sum_{a=j}^{m-1}\frac{|e_j(c_a)|}{|Q_N'(c_a)|}
        \le e_j(-2),\qquad
 \frac1N\log e_j(-2)\longrightarrow M_\infty/2,
 \tag{23}
\]
the resulting squared-coefficient upper-rate expression is
\[
          E(\rho)=2M_3+M_\infty-\tfrac12\log\rho.
 \tag{24}
\]
The first inequality uses \(0\le e_j(c_a)\le e_j(-2)\),
\(|1/Q_N'(c_a)|\le2/N\), and at most \(N/2\) nodes.
The limit is the original sine-product integral at \(j/N\to1/4\).
Thus this is an upper bound for the actual source, obtained from
the whole analytic remainder. It is not a new estimate independent
of the contour principle in (22).

A flat envelope at rate \(M_3\) cannot be used on an ellipse
containing the half-charge color \(w_0=-2\cos t_0\). To see this,
put \(t_h=t_0-ih\) for small fixed \(h>0\). The exact exterior
defect identity in the
[observation theorem](research_complete_source_pick_observation.md#7-complex-colors-and-the-exact-normal-defect)
and the actual local complete-edge packet give
\[
 \begin{split}
 \Re S_3(t_h)&=M_3+\tfrac12\Re A_3\,h^2+O(h^3)>M_3,\\
 D_{3,N}(-2\cos t_h)&=
       h_{3,N}(-2\cos t_h)/Q_N(-2\cos t_h)
                                  \,(1+O(e^{-c_hN})).
 \end{split}
 \tag{25}
\]
Here \(S_3'(t_0)=0\), \(S_3''(t_0)=-A_3\), and
\(\Re A_3>0\). The interpolation term has rate \(M_3\),
whereas the displayed direct term is nonzero and has the strictly
larger rate. If a fixed ellipse contains \(w_0\) in its interior,
it contains these colors for sufficiently small \(h\). Provided
the ellipse is a domain of holomorphy of the original defect,
the maximum-modulus principle therefore rules out the flat
polynomial-times-\(e^{NM_3}\) boundary bound. An ellipse crossing
the original branch cut is already inadmissible for the same
analytic approximation argument.

The half-charge bounds \(0<\Re t_0<\pi/3\) and
\(0<-\Im t_0<2/5\) place \(w_0\) strictly inside the
\(\rho=3\) ellipse about \([-2,0]\). In fact
\[
 |\Re(w_0+1)|<6/5,\qquad |\Im w_0|<3/4,
 \qquad
 \left(\frac{6/5}{5/3}\right)^2+
 \left(\frac{3/4}{4/3}\right)^2
       =\frac{133569}{160000}<1.
 \tag{26}
\]
These constants require no numerical saddle calculation.
The Taylor series gives
\(37/25<e^{2/5}<1007/675<3/2\); hence
\(\cosh(2/5)<11/10\) and \(\sinh(2/5)<5/12\).
Together with \(\sqrt3<7/4\), these prove (26).
The ellipse has center \(-1\) and semiaxes \(5/3,4/3\).
Consequently any radius justified by this flat envelope has
\(\rho<3\).

Finally the [proved rational source bounds](research_pair_regular_support_cells.md#5-a-termwise-absolute-bound-fails-for-the-actual-short-pair)
give \(M_3>21/20\), \(M_\infty>23/20\), and
\(\log3<6/5\). Therefore every such instance of (24) satisfies
\[
 E(\rho)>\frac{13}{4}-\frac12\log3
              >\frac{53}{20}>\frac{13}{5}>\mathcal M_{3,3},
 \tag{27}
\]
where \(\mathcal M_{3,3}\) is the already proved full pair rate.
Reaching even its coarser upper bound \(13/5\) through (24)
would require \(\log\rho>13/10\), contrary to
\(\log\rho<6/5\). This is an insufficiency of this particular
upper-bound expression, not a lower bound on the original
coefficient. A more effective joint contour must retain the direct
phase in (25), its Cauchy diagonal and the original grouped currents;
the argument does not exclude such a contour.

## 6. Reproduction

Run the [focused checker](../experiments/check_physical_normal_defect_packet.py):

~~~sh
python3 experiments/check_physical_normal_defect_packet.py
~~~

It computes the first normals from the literal Newton products,
including the terms whose values vanish, and compares them with
ordinary collocation at both parities. It also records the
normalized defect at every physical row for several finite levels.
Those ratios check the phase and coefficient; the proof of a
uniform physical-row asymptotic remains Sections 2–3 above.
The fixed-neighborhood extension and the transform bound are proved
in Section 5; no growing-order derivative test is substituted for
that contour proof.
The [saved record](../repro/results/research-physical-normal-defect-packet.json)
separates exact finite identities from convergence diagnostics
and includes the input hashes.

