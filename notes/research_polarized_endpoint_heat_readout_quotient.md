# Canonical polarized endpoints and the exact heat-readout quotient

Private written proof, 16 November 2026.

The canonical finite charge polarization and the initialized frozen-contour
polarization need not have the same leading term away from unit charge.
They nevertheless represent exactly the same original scalar after any
signed heat evolution and final unit-charge readout. Their difference
belongs to the precise kernel of all such readouts: the sum of charge
parity sectors odd in at least one coordinate.

For the original same-index kernel network with complete outside data,
the canonical polarization has an explicit complete-action endpoint term
in its contractive charge half-planes. This statement includes all
physical normals and both parities, and does not require a charged
high-sector estimate. The quotient identity explains how that term can
coexist with a geometrically initialized contour representative.

## 1. Original families and charge parity

Fix \(N\ge2\), \(D=N-1\), and \(\eta=(-1)^D\). Retain the original
algebra and closing functional
\[
 P_N(z)=2T_N(z/2)+2,\qquad \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
The distinct double nodes are \(c_a=-2\cos\tau_a\), with
\[
 \tau_a=\pi(D-2a)/N>0,\qquad 0\le a<\lfloor N/2\rfloor.
 \tag{2}
\]
At odd levels the remaining node \(-2\) is simple. The canonical
positive-angle class \(L_N\) has values \(\tau_a\), first normals
\(1/(2\sin\tau_a)\), and odd simple value zero.

Put \(y_v=1-\chi_v\). For a fixed compiled numerator \(F_N\), including
all kernels, spectators and ordinary outside variables, define the
carrier-removed canonical source
\[
 \mathcal F_{\boldsymbol\sigma}(\mathbf n,\mathbf y)
 =\phi_N^{\otimes I}\left[
 F_N\prod_{v\in I}
  \exp_{\mathcal A_N}\!\left(\frac{in_vN}{4\pi}L_N^2\right)
  \exp_{\mathcal A_N}(\sigma_viNy_vL_N)\right].
 \tag{3}
\]
Multiplication by \(\prod_v\exp(\pi i n_vD^2/(4N))\) restores the
literal original carriers. At integer powers and \(\mathbf y=0\),
this is the prescribed original scalar.

Let \(\mathcal G_{\boldsymbol\sigma}(\mathbf n,\mathbf y)\) be a
pattern-adapted contour family with its original polynomial numerator,
removed-row expansion, cuts, and entire table of positive heights fixed
as in its pinned source. It is not redefined during heat transport.
Both exact constructions obey
\[
 R_v\mathcal F_{\boldsymbol\sigma}
   =\mathcal F_{\boldsymbol\sigma^{(v)}},\qquad
 R_v\mathcal G_{\boldsymbol\sigma}
   =\mathcal G_{\boldsymbol\sigma^{(v)}},
 \qquad
 R_v f(\mathbf y)=f(y_1,\ldots,-y_v,\ldots),
 \tag{4}
\]
where \(\boldsymbol\sigma^{(v)}\) flips the indicated sign.
Their sign averages are the same original cosine source
\(\mathcal C(\mathbf n,\mathbf y)\). Thus, with
\[
 E=\prod_{v\in I}\frac{1+R_v}{2},
 \tag{5}
\]
one has the exact identities
\[
 E\mathcal F_{\boldsymbol\sigma}
   =E\mathcal G_{\boldsymbol\sigma}=\mathcal C .
 \tag{6}
\]
These are identities of the full source, before specializing any
ordinary outside variables or taking any asymptotic expansion.

## 2. The maximal kernel of independent heat readouts

Let \(\mathscr H\) consist of entire functions of \(\mathbf y\) satisfying
some bound
\[
 |f(\mathbf y)|\le C(1+|\mathbf y|)^M
                       \exp(A\sum_v|y_v|).
 \tag{7}
\]
Constants here may depend on the fixed level. The original canonical
families and fixed-contour families belong to this class at every fixed
base power. Their actual source bounds give (7), including ordinary
outside derivatives on compact sets.

For independent heat increments \(\boldsymbol\delta\), put
\[
 \mathsf H_{\boldsymbol\delta}
  =\exp\left[-\frac{i}{4\pi N}
                   \sum_v\delta_v\partial_{y_v}^2\right],
 \qquad
 \Lambda_{\boldsymbol\delta}f
                   =(\mathsf H_{\boldsymbol\delta}f)(\mathbf0).
 \tag{8}
\]
The series converges locally uniformly in \(\mathbf y\) and all complex
\(\boldsymbol\delta\). Indeed Cauchy estimates with radii proportional
to the derivative orders bound an order-\(\boldsymbol\nu\) derivative
of (7) by a fixed exponential in \(|\boldsymbol\nu|\) times a polynomial
in \(|\boldsymbol\nu|\), locally uniformly in \(\mathbf y\).
The factorials in the exponential series then give convergence for
every bounded set of heat parameters.

**Theorem 1.** On \(\mathscr H\),
\[
 \bigcap_{\boldsymbol\delta}\ker\Lambda_{\boldsymbol\delta}
     =\ker E
     =\bigoplus_{\varnothing\ne A\subseteq I}\operatorname{im}P_A,
 \qquad
 P_A=\prod_{v\in A}\frac{1-R_v}{2}
                  \prod_{v\notin A}\frac{1+R_v}{2}.
 \tag{9}
\]
For the intersection it suffices to use all independent real heat
parameters in any nonempty open box, or a complex neighborhood.
Using only integer powers is not asserted sufficient.

**Proof.** Every \(\partial_{y_v}^2\) commutes with every reflection,
and evaluation at zero equals evaluation after \(E\). Hence
\(\Lambda_{\boldsymbol\delta}=\Lambda_{\boldsymbol\delta}E\).
This proves one inclusion and heat stability of the kernel.
Conversely, vanishing on a real open box implies vanishing of the
entire heat-readout function. Its derivatives at
\(\boldsymbol\delta=0\) give
\[
 \left.\partial_{\boldsymbol\delta}^{\boldsymbol\alpha}
             \Lambda_{\boldsymbol\delta}f\right|_0
  =\left(-\frac{i}{4\pi N}\right)^{|\boldsymbol\alpha|}
                     \partial_{\mathbf y}^{2\boldsymbol\alpha}f(0).
 \tag{10}
\]
These are exactly all Taylor coefficients of the all-even function
\(Ef\). Thus \(Ef=0\). The commuting reflection projectors sum to
the identity and have disjoint images, proving the last equality.
\(\square\)

For nonzero real increments the same statement is an absolutely
convergent Gaussian identity. In one coordinate,
\[
 \Lambda_\delta f
 =\sqrt{\frac N{|\delta|}}\int_{\mathbb R}
  e^{-\pi Nr^2/|\delta|}
       f\!\left(-e^{-i\,\operatorname{sgn}(\delta)\pi/4}r\right)\,dr.
 \tag{11}
\]
The minus sign accounts for \(y=1-\chi\) and can equally be removed
by \(r\mapsto-r\). Bound (7) justifies tensorization, Fubini and
reflection of a complete integration line. A parity sector odd in
one coordinate integrates to zero. When an increment is zero,
evaluation at that coordinate gives the same conclusion.

Equations (6)--(11), together with the exact heat identities of the
two sources, give for every base power \(\mathbf b\)
\[
 \Lambda_{\boldsymbol\delta}
  \{\mathcal F_{\boldsymbol\sigma}(\mathbf b,\cdot)
                -\mathcal G_{\boldsymbol\sigma}(\mathbf b,\cdot)\}=0,
 \qquad
 \mathcal F_{\boldsymbol\sigma}(\mathbf b+\boldsymbol\delta,0)
  =\mathcal G_{\boldsymbol\sigma}(\mathbf b+\boldsymbol\delta,0).
 \tag{12}
\]
All original outside derivatives and carriers can be restored.
For the frozen contour representative its small-charge initializer
is the actual proved one; (12) does not require reconstructing it
inside the canonical finite charge space.

There are two useful limitations. Membership in the ideal generated
by the \(y_v\) is insufficient: for example a nonzero \(y_v^2\) term
can contribute after heat evolution. The precise kernel is (9).
Also cancellation in (11) uses the entire centered lines. A displaced
or truncated local saddle piece need not annihilate an odd sector;
its compensating pieces must remain in the exact heat integral.

Finally \(E\) is injective on the canonical finite-\(Q\) image of a
fixed full spectral algebra. Its image is the faithful original
cosine observation, and the crossing factors in (3) are algebra
units. Thus a nontrivial repair by (9) generally leaves that finite
image. The contour family is a representative of the same heat-readout
class in the larger entire function space, not a new finite coupon
with silently changed normal data.

## 3. A local complete-kernel estimate with a global physical envelope

For the remaining statements take the original same-index source on
a fixed finite circle tree, with a nonempty selected set \(I\).
Keep all \(e\) edges incident to \(I\), counted once, and fix every
outside endpoint at its complete spectral value \(-2\).
No further uncontracted exterior is included in this assertion.
The selected set need not be connected, and no lower degree or
charged geometric-positivity hypothesis is needed.

Write
\[
 K_N(z,w)=\sum_{a=0}^{D}e_a(z)e_a(w),\qquad
 \mathcal K_N=K_N(-2,-2),\qquad M_\infty=4G/\pi .
 \tag{13}
\]
The pinned local low-edge proof at complete angles gives
\[
 \mathcal K_N
 =\frac14N^{-3/2}e^{NM_\infty}(1+O(N^{-1})).
 \tag{14}
\]
Here is why it applies to the full kernel with the needed derivatives.
The complete index maximum is \(x=1/4\), with second derivative
\(-8\pi\) and density \(1/4\). Retain a small fixed index interval
about this maximum and apply the original holomorphic index-contour
expansion. Outside that interval the real complete low-index action
has a fixed strict gap, including its endpoint limits. The low
Laurent coefficients are nonnegative, so its full real angular
supremum is bounded by its complete value. Polynomial continuation
preserves the gap on a sufficiently small fixed complex angular
polydisk.

The full high radical kernel, with both arguments ordinary, satisfies
the source bound
\[
 |\partial_t^r\partial_u^s K_N^{\rm high}(-2\cos t,-2\cos u)|
 \le m(N-1)D^{r+s}e^{D(|\Im t|+|\Im u|)},\qquad m=\lfloor N/2\rfloor,
 \tag{15}
\]
apart from the possible middle low index, which stays in the low sum.
Shrinking the fixed polydisk makes (15) exponentially smaller than
the complete low-edge term. Thus, on that polydisk,
\[
 K_N(-2\cos t,-2\cos u)
 =N^{-3/2}a(t,u)e^{N\psi(t,u)}(1+O_{\rm hol}(N^{-1})),
 \quad a(0,0)=1/4,\quad\psi(0,0)=M_\infty .
 \tag{16}
\]
All factors are separately even in their angular arguments.

Let \(f_{N,\mathbf n}(\mathbf t)\) be the graph kernel product
multiplied by the carrier-removed Gaussian factors
\(\exp(i n_vNt_v^2/(4\pi))\). For real powers in a fixed bounded box,
(16) implies, uniformly near the origin,
\[
 f_{N,\mathbf n}(0)=\mathcal K_N^e,\qquad
 \frac{f_{N,\mathbf n}(\mathbf t)}{\mathcal K_N^e}
   =a_*(\mathbf t)e^{NW_*(\mathbf t)}
                         (1+O_{\rm hol}(N^{-1})),
 \quad a_*(0)=1,\quad W_*(0)=0,
 \tag{17}
\]
with \(W_*=O(|\mathbf t|^2)\). The amplitudes, actions and errors
are separately even. The ratio in (17) is normalized exactly at
zero; changing its displayed error by \(O(N^{-1})\) achieves this.

There is also a global polynomial physical-jet envelope. At a
physical node \(c_j\),
\[
 0\le e_r(c_j)\le e_r(-2)\quad(r\le j),\qquad e_r(c_j)=0\quad(r>j).
 \tag{18}
\]
The first inequality follows term by term from the positive Newton
product. Consequently every physical kernel value is at most
\(\mathcal K_N\). The pinned full-normal bounds give
\[
 |K_z(c_j,w)|\le N^{11}K_N(c_j,w),\qquad
 |K_{zw}(c_j,c_l)|\le(N^{16}+N^{22})K_N(c_j,c_l),
 \tag{19}
\]
with the stated first-normal bound also valid at outside \(w=-2\).
Leibniz expansion over the fixed graph therefore bounds every mixed
normal needed by the tensor trace by \(CN^A\mathcal K_N^e\).
Real crossing values have modulus one and their normals add only
polynomial cost. Odd simple nodes require only evaluation.
This is a bound for the actual full source, not for a replacement
positive closing.

## 4. The canonical half-grid endpoint term

For \(\sigma=\pm1\), define on \(\sigma\Im y>0\)
\[
 \begin{aligned}
 \mathfrak e_{\sigma,\mathrm{even}}(y)
  &=-i\sigma\{\csc(\pi y)-\pi y\csc(\pi y)\cot(\pi y)\},\\
 \mathfrak e_{\sigma,\mathrm{odd}}(y)
  &= i\sigma\{\cot(\pi y)-\pi y\csc^2(\pi y)\}.
 \end{aligned}
 \tag{20}
\]
Their apparent singularity at zero is removable, but the asymptotic
domain below stays a fixed positive distance inside the half-plane.

**Theorem 2.** Uniformly on compact sets of
\(\{\mathbf y:\sigma_v\Im y_v>0\ \text{for every }v\}\), and for
real powers in a fixed bounded box,
\[
 \boxed{\quad
 \mathcal F_{\boldsymbol\sigma}(\mathbf n,\mathbf y)
 =\mathcal K_N^e
   \left\{\prod_{v\in I}\mathfrak e_{\sigma_v,\operatorname{parity}(N)}
                                      (y_v)+O_{\rm hol}(N^{-1})\right\}.
 \quad}
 \tag{21}
\]
Equivalently its complete-action prefactor is
\(4^{-e}N^{-3e/2}e^{NeM_\infty}\).
The assertion includes every mixed physical normal in (3).

**Proof.** The exact positive-node contribution of a one-variable
spectator \(f\), after inserting the polarized coupon, is
\[
 2\eta e^{\sigma iNy\tau}
   \{\sin\tau\,\partial_\tau+\cos\tau
                         +\sigma iNy\sin\tau\}f(\tau).
 \tag{22}
\]
This follows from \(4\sin^2\tau\,f_z=2\sin\tau\,f_\tau\)
and \(-c=2\cos\tau\). At odd levels add \(f(0)\).
The tensor product of these exact operators is (3).

On the compact charge set let \(\sigma_v\Im y_v\ge b_0>0\).
If at least one physical angle is at least a fixed small
\(\delta>0\), (19) and the coupon exponential bound make its entire
contribution \(O(N^A e^{-Nb_0\delta})\mathcal K_N^e\).
There are only polynomially many physical assignments. This also
handles configurations in which some other coordinates are odd
simple nodes.

For the remaining assignments put \(r_v=N\tau_v\). Formula (17),
its holomorphic derivative bounds, and separate evenness show that
applying the operators in braces in (22) gives their constant-
spectator answer with error bounded by
\[
 \frac{C}{N}(1+\sum_vr_v)^B
            \exp\!\left(\frac C N\sum_vr_v^2\right)
                         \mathcal K_N^e .
 \tag{23}
\]
This elementary bound follows either by Leibniz expansion of (17)
or by differentiating in the \(r_v\): each differentiated phase
has at least its corresponding factor \(r_v/N\), and
\(N\sin(r_v/N)\) supplies at most \(r_v\).
An undifferentiated exponential differs from one by at most its
quadratic bound times that exponential. The holomorphic
\(O(N^{-1})\) remainder and its fixed derivatives have the same
bound. There are only finitely many derivatives in this calculation.

Choose \(\delta\) smaller if necessary so that
\(Cr_v^2/N\le b_0r_v/2\) on this region. Multiplication by the
coupon exponential then makes the sum of (23) at most
\[
 \frac{C'}N\mathcal K_N^e
       \sum_{\mathbf r}(1+\sum_vr_v)^B
                                      e^{-b_0\sum_vr_v/2}
 =O(N^{-1})\mathcal K_N^e .
 \tag{24}
\]
The mesh of each \(r_v\) is the fixed mesh \(2\pi\), with its
appropriate parity offset. Thus the bound is independent of \(N\).
In the constant-spectator part, replacing \(\cos(r/N)\) by one
and \(N\sin(r/N)\) by \(r\) costs at most
\(C(r^2+r^3)/N^2\) before the same exponential weight.
Its sum is \(O(N^{-2})\), also absorbed in (24).
The same argument permits extending the constant-spectator sums
to the whole positive half-grid, with exponential error.

At even levels that half-grid is \(r=(2j+1)\pi\), \(j\ge0\);
at odd levels it is \(r=2j\pi\), \(j\ge1\), together with the
simple evaluation at zero. The convergent sums are
\[
 K_{\sigma,\mathrm{even}}(y)
      =2\sum_{j\ge0}e^{\sigma i(2j+1)\pi y}
      =i\sigma\csc(\pi y),
 \qquad
 K_{\sigma,\mathrm{odd}}(y)
      =1+2\sum_{j\ge1}e^{\sigma i2j\pi y}
      =i\sigma\cot(\pi y).
 \tag{25}
\]
Equation (22) gives
\(\eta(K+yK')\) at even levels and \(K+yK'\) at odd levels,
where \(\eta=-1\) and \(+1\), respectively. These are (20).
All tensor variables factor in the constant-spectator answer,
proving (21). Cauchy estimates on slightly larger compact
half-plane sets give the holomorphic derivative assertion.
\(\square\)

The coefficient is not identically zero. More concretely, for every
\(\beta>0\), at \(y=i\sigma\beta\) it is
\[
 \mathfrak e_{\sigma,\mathrm{even}}
       =(\pi\beta\coth(\pi\beta)-1)\operatorname{csch}(\pi\beta)>0,
 \qquad
 \mathfrak e_{\sigma,\mathrm{odd}}
       =\coth(\pi\beta)-\pi\beta\operatorname{csch}^2(\pi\beta)>0.
 \tag{26}
\]
The inequalities follow by differentiating
\(z\cosh z-\sinh z\) and \(\sinh z\cosh z-z\) for \(z>0\).
Thus on neighborhoods of these actual charge points the canonical
polarized source has precisely the complete action \(eM_\infty\),
for every bounded real power tuple.

## 5. Exact removal and the remaining estimate

Every function in (20) is odd in \(y\). This is consistent with,
but is not a substitute for, the exact parity theorem (9).
The two signs' asymptotics are proved in opposite half-planes;
they must not be added outside their domains to infer a cosine
asymptotic. The original cosine cancellation is instead an exact
identity (6), with all normal data retained.

One may remove the difference
\[
 \mathcal D_{\boldsymbol\sigma}
      =\mathcal F_{\boldsymbol\sigma}-\mathcal G_{\boldsymbol\sigma}
      =\sum_{\varnothing\ne A\subseteq I}P_A\mathcal D_{\boldsymbol\sigma}
 \tag{27}
\]
before estimating a final heat readout. Equations (9)--(12) prove
that this removal has exactly zero effect on the prescribed scalar,
at every level and every signed real power tuple. There is no
unestimated residual boundary term in that identity. In particular
the already initialized frozen-contour family can be used directly
as a representative of the canonical family's heat-readout class.

Subtracting only the first asymptotic term in (21) would not prove
this: it is a local half-plane expression and leaves errors with
the same complete exponential rate. Likewise subtracting a finite
Taylor jet of the angular spectator generally lowers only the
polynomial endpoint order. The exact parity decomposition is the
relevant operation, and it retains the original scalar by (12).

The construction does not provide a new action-relative bound along
an arbitrary heat path. The initialized contour representative still
has its actual fixed growth envelope, shrinking certified domains,
and possible large complementary contributions. A proposed
geometric initializer for the canonical finite-\(Q\) family cannot
ignore (21) whenever its asserted action is strictly below
\(eM_\infty\). Passing to the exact quotient permits the contour
representative; it does not by itself extend its proved coverage
to arbitrary short fillings.

## Direct sources and readback

The complete proof and the following complete source versions are read
before freezing. Only written mathematics, text reads and hashes are
used; no programs, tests or numerical calculations are run.

* [Canonical finite polarization](research_polarized_charge_heat_source.md),
  SHA256 860801dedc3f1093d58c0413f580599512bd2566c00f4a94d0ebf99636343db1:
  all physical jets, trace formula, cosine projection, faithful
  observation and exact carrier-removed heat evolution.
* [Pattern-adapted initialized family](research_pattern_adapted_polarized_heat_initializer.md),
  SHA256 a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694:
  fixed actual source, reflection and sign-average identities,
  entire exponential-type bound, exact Gaussian heat and initializer.
* [Regular low-edge source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_regular_zero_subtree_low_source.md),
  SHA256 06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1:
  holomorphic edge symbol, exact density, strict index maximum and
  polynomial continuation of the discarded low indices.
* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  full ordinary radical Fourier bound and derivative bound (15).
* [Original physical normal envelope](research_charged_source_physical_pressure.md),
  SHA256 1e127c0842c0d6d5727a517cc66c39e73baa2846848c284d257c1ebe49679091:
  all physical first and mixed-normal bounds and their assembly
  with the real crossing factors and complete outside ends.

The finite reconstruction theorem
(research_finite_charge_quantitative_reconstruction.md, 5d13994e8b6d2dc3c54d1fcf15d1f9435efc2d26921046bca14b90d22e75bf23)
already identifies canonical polarization as a projection of the
whole cosine charge function. No claim of novelty is made for
reflection projectors or elementary heat parity. The additions are
the exact comparison with the initialized original contour family,
the maximal readout-kernel statement in its actual growth class,
and the controlled complete-action asymptotic of the canonical
half-grid source.
