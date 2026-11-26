# A contour-polarized heat family with an actual small-charge initializer

Private written proof, 16 November 2026.

Expand the original finite source by its removed physical-row subsets
before choosing contour heights. Freeze for each subset the heights
used in its small-charge estimate. Splitting only the retained lower
horizontal cosine then gives exact polarized entire families. Their
sign average is the original charged source, and every polarization
has the original unit-charge endpoint. The all-plus family has a
proved nonzero complex initializer and exact signed heat evolution.

These families depend on the prescribed polynomial source and frozen
contours. They are different from the finite Hermite coupons
\(Q_{N,\pm}\). No polarized finite-coupon initializer is inferred.
Nor does the construction supply the angle-label coverage or global
action-relative bounds needed to reach arbitrary unit-charge targets.

## 1. Fixed operators with the original trace normalization

Let \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 \tau_j=\frac{\pi(D-2j)}N,\qquad
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{1}
\]
For an even holomorphic spectator \(A(t)\), write
\[
 g_n[A](t)=\sin t\,A(t)e^{inNt^2/(4\pi)}.
 \tag{2}
\]
The carrier-removed original trace with the full-Hermite cosine
coupon is
\[
 \mathcal L_{n,\chi}[A]
 =\eta\sum_{j=0}^{D}
       \left.\partial_t\{
          g_n[A](t)\cos(N(1-\chi)t)\}\right|_{t=\tau_j}.
 \tag{3}
\]
It equals \(C_{N,n}^{-1}\phi_N(R_n[A]\mathcal C_{N,\chi})\).
The odd simple node is the single value contribution at \(t=0\);
all other terms combine in pairs to give the original first normals.
The same direct formula holds at \(N=2\).

Choose a positive midpoint \(a_N\le\pi\) with
\(e^{iNa_N}=-\eta\). For all sufficiently large \(N\), choose the
largest such midpoint not exceeding \(19/20\), as in the small-charge
proof. The finite number of remaining levels can use \(a_N=\pi\).
Define the literal outer-row operator
\[
 \mathcal O_{n,\chi}[A]
 =\eta\sum_{|\tau_j|\ge a_N}
       \left.\partial_t\{
          g_n[A](t)\cos(N(1-\chi)t)\}\right|_{t=\tau_j}.
 \tag{4}
\]
No value or first normal in this sum is dropped.

For a fixed \(h>0\) and \(\sigma\in\{+,-\}\), set
\[
 \mathcal H_{\sigma,n,\chi}^{h}[A]
 =-\frac{N^2}{\pi i}
   \int_{-a_N-ih}^{a_N-ih}
       g_n[A](t)e^{\sigma iN(1-\chi)t}W_N(t)\,dt,
 \qquad
 \mathcal H_{\cos}^{h}=\frac{\mathcal H_+^{h}+
                                      \mathcal H_-^{h}}2.
 \tag{5}
\]
For a chosen side \(\epsilon\in\{+1,-1\}\), the unchanged cosine
vertical current is
\[
 \mathcal V_{n,\chi}^{h,\epsilon}[A]
 =\frac{\epsilon\eta N^2}{\pi}
   \int_{-h}^{h}
       \frac{g_n[A](\epsilon a_N+iv)
              \cos(N(1-\chi)(\epsilon a_N+iv))}
                 {4\cosh^2(Nv/2)}\,dv.
 \tag{6}
\]
The factor \(\epsilon\) retains the orientation: replacing the
positive side by the negative side changes the unprefactored integral
by a minus sign. The exact retained-trace identity is
\[
 \mathcal L_{n,\chi}
   =\mathcal O_{n,\chi}
       +\mathcal H_{\cos,n,\chi}^{h}
       +\mathcal V_{n,\chi}^{h,\epsilon}.
 \tag{7}
\]
It uses evenness of the spectator and cosine, not charge integrality.
The identity follows from the double-pole residue formula, with the
two horizontal sides combined by reflection. Every contour and its
endpoints in (4)--(7) will be fixed independently of the evolving
power and charge parameters.

## 2. Expand the removed subsets before freezing heights

Fix a finite original same-index graph with selected set \(I\),
\(m=|I|\ge1\), and degrees \(d_v\ge1\) at selected vertices, counting
loop incidences. Retain its original polynomial kernel product
\(F_N(\mathbf t;\mathbf u)\), even in each selected angle. The outside
angles \(u_w\) label spectral variables \(z_w=-2\cos u_w\); their
ordinary polynomial dependence is retained. For the initializer
only, set those outside angles to zero, exactly as in the small-charge
source theorem.

Fix base real powers \(\mathbf b\) and a base charge vector
\[
                 \boldsymbol\xi\in(1/4000,1/2000)^I.
 \tag{8}
\]
For each subset \(S\subseteq I\), set the angles in \(S\) to zero
and take the small critical point of the remaining graph at charges
\(\xi_v\), \(v\notin S\). All original incidences remain, now
including the new complete ends. Let its positive heights be
\(h_v^S\), \(v\notin S\). For \(S=I\) no heights are needed.
Freeze all these numbers. Also freeze
\(\epsilon_v=\operatorname{sgn}b_v\) when \(b_v\ne0\), and
\(\epsilon_v=1\) when \(b_v=0\). Put
\[
              H_* =\max_{S,v\notin S}h_v^S>0.
 \tag{9}
\]
The small-charge estimates give \(H_*<63/20000\). All choices in
(8)--(9) are part of the definition of the family, not parameters
silently adjusted during heat evolution.

For a sign vector \(\boldsymbol\sigma\in\{+,-\}^I\), define
\[
 \mathfrak Z_{N,\boldsymbol\sigma}(\mathbf n,\boldsymbol\chi;\mathbf u)
 =\sum_{S\subseteq I}
    \left[\prod_{v\in S}\mathcal O_{v,n_v,\chi_v}
       \prod_{v\notin S}
       \bigl(\mathcal H_{\sigma_v,n_v,\chi_v}^{h_v^S}
             +\mathcal V_{n_v,\chi_v}^{h_v^S,\epsilon_v}\bigr)
    \right]F_N.
 \tag{10}
\]
These are carrier-removed families. Operators in separate coordinates
commute. The spectator remains even in each not-yet-contracted
coordinate, since the original kernels are even there. Thus (7)
can be applied independently after the outer subsets have been
expanded. It gives the exact identities
\[
 2^{-m}\sum_{\boldsymbol\sigma}\mathfrak Z_{N,\boldsymbol\sigma}
       =\widetilde Z_N(\mathbf n,\boldsymbol\chi;\mathbf u),
 \qquad
 \mathfrak Z_{N,\boldsymbol\sigma}(\mathbf n,\mathbf1;\mathbf u)
       =\widetilde Z_N(\mathbf n,\mathbf1;\mathbf u).
 \tag{11}
\]
For signs belonging to removed vertices the summand in (10) is
independent of that sign; their multiplicity is exactly the one
needed for the first equality. At charge one both horizontal
exponentials equal one, giving the second equality term by term.
Multiplication by \(\prod_v C_{N,n_v}\) restores the original
crossing carriers. At integer powers the endpoint is the prescribed
original scalar, with both parities and all normals retained.

Charge reflection \(\chi_v\mapsto2-\chi_v\) exchanges the sign
\(\sigma_v\), leaving every vertical and removed-row operator
unchanged. The individual families need not be even about charge
one. Away from that endpoint they generally do not factor through
the finite spectral quotient: changing a polynomial representative
or the frozen heights can change (10). No such change is made here.

## 3. Exact heat evolution and the full-source growth bound

Each integrand in (4)--(6) obeys
\[
 \partial_{n_v}
   =-\frac{i}{4\pi N}\partial_{\chi_v}^2
 \tag{12}
\]
when applied to its Gaussian times its cosine or exponential. In
(4), the physical angular derivative commutes with this identity.
All finite sums and fixed compact contour integrals commute with
the parameter derivatives. Consequently (10) is entire in powers
and charges and satisfies (12) in every coordinate. No integration
by parts or missing moving-endpoint term is involved.

For fixed real powers in a bounded box and free boundaries in a
fixed compact set, there are constants \(A,p,C\) such that
\[
 |\mathfrak Z_{N,\boldsymbol\sigma}(\mathbf n,\boldsymbol\chi;\mathbf u)|
 \le A N^p\prod_v(1+|\chi_v|)
 \exp N\left\{C+\sum_v
       \bigl[\pi|\Im\chi_v|+H_*|1-\Re\chi_v|\bigr]\right\}.
 \tag{13}
\]
Every angular argument used in (10) has \(|\Re t|\le\pi\) and
\(|\Im t|\le H_*\). Its charge exponential is therefore bounded by
the corresponding factor in (13); cosine is their mean. Physical
normals add polynomial factors and \(1+|\chi_v|\). The original
Newton polynomial envelopes on this fixed angular compact give
\(N^p e^{CN}\) for the kernels and their fixed mixed normals, as
in the local heat theorem. The horizontal \(W_N\) factors are bounded
at the fixed positive heights; the vertical denominators in (6)
are bounded by one. The finitely many patterns and finite small
levels can be absorbed in the constants. This proves (13), also
with any fixed number of ordinary free-boundary derivatives.

For \(\delta\in\mathbb R\setminus\{0\}\) and
\(v_\delta=e^{-i\operatorname{sgn}(\delta)\pi/4}\), the exact heat
formula is
\[
 \mathfrak Z_N(\mathbf n+\delta\mathbf e_v,\boldsymbol\chi)
 =\sqrt{\frac N{|\delta|}}
   \int_{\mathbb R}e^{-\pi Nr^2/|\delta|}
       \mathfrak Z_N(\mathbf n,
                       \boldsymbol\chi+v_\delta r\mathbf e_v)\,dr.
 \tag{14}
\]
Complete the square on each charge exponential before the compact
angular integrations. It multiplies that integrand by
\(e^{i\delta Nt_v^2/(4\pi)}\). The same identity holds for cosine
and after the physical angular derivatives. Bound (13), with the
Gaussian quadratic decay, justifies Fubini and all derivatives.
It also permits any finite translation of the entire charge line.
Thus (14) retains every original current. It does not rely on an
incorrect finite-dimensional charge-space claim for (10).

## 4. A genuine holomorphic initializer for the all-plus family

Throughout this section the outside angles are specialized to zero,
so their spectral variables equal \(-2\). The initializer below is
not asserted for arbitrary free-boundary values.

Let \(\Phi_{\mathbf b,\boldsymbol\chi}\), its small critical point,
and \(A_\Gamma(\boldsymbol\chi)\ne0\) have exactly the original
normalization in the small-charge theorem, with carriers removed.
If \(e\) is the number of kernel edges in that theorem, then on a
fixed complex neighborhood \(U\) of the base point (8),
\[
 \boxed{\quad
 \mathfrak Z_{N,\mathbf+}(\mathbf b,\boldsymbol\chi)
  =2^m N^{3(m-e)/2} A_\Gamma(\boldsymbol\chi)
       e^{N\Phi_{\mathbf b,\boldsymbol\chi}(\mathbf t^*)}
                      (1+O_{\rm hol}(N^{-1})).\quad}
 \tag{15}
\]
The amplitude is a holomorphic unit after shrinking \(U\), and there
is an expansion to every fixed inverse-power order. Through both
level parities, every other sign vector obeys, on a possibly smaller
\(U\),
\[
 |\mathfrak Z_{N,\boldsymbol\sigma}(\mathbf b,\boldsymbol\chi)|
  \le A N^p
      e^{N(\Re\Phi_{\mathbf b,\boldsymbol\chi}(\mathbf t^*)-\gamma)}
       \quad(\boldsymbol\sigma\ne\mathbf+)
 \tag{16}
\]
for some \(\gamma>0\).

Here is the source estimate, including the role of the frozen heights.
At the real base point, a summand with \(S\ne\varnothing\) uses
precisely the reduced heights required by the original outer-row
proof. Its centered kernel bound retains the losses at every removed
incidence and every mixed physical normal. Replacing a remaining
horizontal cosine by either exponential does not increase its
exponential majorant: at height \(-h\) the plus choice gives charge
\(\chi\), and the minus choice gives the larger decaying charge
\(2-\chi\). Thus the archived outer-row gap applies to that summand.
Likewise every summand with a vertical coordinate has the original
mixed-current gap, with the side factor in (6) retained.

For \(S=\varnothing\) and no vertical coordinate,
\[
 W_N(t)e^{iN(1-\chi)t}
    =\frac{e^{-iN\chi t}}{(1-\eta e^{-iNt})^2},\qquad
 \frac{e^{-iN(1-\chi)t}}{e^{iN(1-\chi)t}}
                         =e^{-2iN(1-\chi)t}.
 \tag{17}
\]
On the fixed lower horizontals at the base point, the second factor
has modulus \(e^{-2N(1-\xi_v)h_v^\varnothing}\). Every height is
positive. Hence any minus sign gives a strict gap, while all plus
signs give exactly the original selected phase and Gaussian density.
The only normalization change is the absence of the cosine's factor
\(1/2\) at each vertex, proving the factor \(2^m\) in (15).

This argument is valid at real nonlattice charges: the exact coupon
identities use the same even entire functions and full Hermite data,
and all quoted estimates use real charge inequalities rather than
integrality of \(N\chi\). Real powers are handled by the canonical
crossing extension in the local heat theorem. Its physical values
have unit modulus and its normals have polynomial cost.

To obtain the complex neighborhood, keep every contour in (10)
fixed. A change \(|\delta\chi_v|\le\varepsilon\) changes each of
the preceding absolute exponential bounds by at most
\(e^{C_1N\varepsilon}\), uniformly over all the compact contour
pieces and physical angles. The physical derivatives add only
polynomial factors; explicitly their coupon bounds are
\(e^{\pi N|\Im\chi|}\) and
\(N|1-\chi|e^{\pi N|\Im\chi|}\). Choose \(\varepsilon\) below
the finitely many strict gap margins divided by the resulting
constants. The continued action changes by \(O(\varepsilon)\),
so the gaps remain uniform relative to it. This is an exponential
estimate, not pointwise continuity in \(N\).

The all-plus saddle moves holomorphically inside the same pole-free
thin rectangle. Its local contour can be displaced through that
saddle, keeping the ends fixed and the connecting pieces in the
existing strict-gap region. The original holomorphic kernel symbols,
sine factors and Gaussian determinant stay nonzero. Their standard
Taylor expansion gives (15) with uniform holomorphic errors and
all fixed orders. The same gap perturbation gives (16).

## 5. What local heat transport now does, and what it does not do

Equations (13)--(15) supply an actual initialized family to which the
quantitative local heat proof applies. Its growth function is now
\(C+\pi|\Im\chi|+H_*|1-\Re\chi|\) in one coordinate. Along a
Gaussian line, its extra linear cost is at most
\((\pi+H_*)|r|\). Replacing the constant \(\pi\) by
\(\pi+H_*\) in that proof's linear tail bound gives the same
sufficient small-step theorem, with its excess constant also replaced
by the supremum of
\(C+\pi|\Im\zeta|+H_*|1-\Re\zeta|-\Re S(\zeta)\)
on the certified initial domain. In particular the characteristic,
new action and density remain
\[
 \chi=\zeta+\frac{i\delta}{2\pi}S'(\zeta),\qquad
 S_\delta=S(\zeta)+\frac{i\delta}{4\pi}S'(\zeta)^2,
 \qquad
 a_\delta=\frac{a(\zeta)}
                {\sqrt{1+i\delta S''(\zeta)/(2\pi)}},
 \tag{18}
\]
with the square root continued from one and with the actual
eroded-domain and tail requirements of that theorem.

The frozen family is not redefined after a step. Rechoosing its
heights would require retaining its exact height-change currents.
Iteration still carries the same initially certified classical
angle labels; the present construction does not prove that they
cover a prescribed arbitrary short filling at unit charge. Nor does
(13) replace the whole-source growth by the geometric action.
The remaining problem is coverage and a certified chain of
action-relative tail bounds for this now initialized family.
It is no longer an internal charge-reflection obstruction, since
the all-plus family is not itself even about charge one.

## Direct sources and versions

The complete final proof and all directly used source implications
were read before freezing, retaining earlier full source readbacks
only at unchanged hashes.

- [Exact complete trace contour](research_exact_complete_trace_contour.md),
  `a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8`:
  double-pole derivative sampling, removed rows and the oriented
  horizontal/vertical identity.
- [Small-charge source](research_small_charge_path_source.md),
  `c6d0ce2a4ecf1412aa3752cb8a94c6933bb47acab5d96d879c6f1b17b2db2a90`:
  reduced small saddles, full same-index graph kernel bounds,
  all mixed-current/removed-row gaps, and the original amplitude.
- [Local charged-source heat propagation](research_charged_source_local_heat_propagation.md),
  `a924922b515aecdedef0c3877d69f0e50da030b9a111220f712a3f6d1bdb926e`:
  real-power and complex-charge proof extensions, finite exponential
  envelopes, quantitative local heat estimate and its domain scope.
- [Entire charged-source heat reduction](research_entire_charged_source_heat_reduction.md),
  `33213425be9cac699860a48b23830399c82cd89bea3140cc776274aafe115fba`:
  canonical crossing carrier, full normal data and Gaussian heat
  normalization. The finite-space assertion there is not imported
  for the contour families (10).
