# An endpoint-window induction step from closed angle rates

Private written proof, 16 November 2026.

The positive physical-row expansion transports an endpoint window to
charges slightly below one. The original supporting-plane comparison
still gives a uniform gap for those charges. Combining the two gives
an actual estimate for the endpoint-window source from uniform upper
bounds on its inserted descendants. The descendants need not have a
positive critical point, a nonzero leading coefficient, or a previously
supplied strict gap.

The quantum hypothesis concerns the whole descendant scalar with its
actual spectator and partial coupons. A bound for an undecorated source
does not satisfy that hypothesis for arbitrary insertions. The result
does not estimate the other physical windows or the paired vertical
currents.

## 1. Original geometry and the closed deleted rates

Fix a finite original circle tree, a nonempty selected set \(S\), and
the edges incident to \(S\), counted once. Each selected vertex has an
original incidence. All outside vertices are complete, with angle
\(t_b=0\) and spectral color \(-2\). Keep fixed signed integer powers
\(n_v\), and suppose the original canonical positive unit-charge
equations have a solution:
\[
 P_{n,v}(t):=\sum_{e\ni v}r_{v,e}-\frac{i n_vt_v}{2}
                 =-\pi i,\qquad v\in S.
 \tag{1}
\]
Write \(t_v^0=s_v^0-iH_v\). The adopted positive-prefix and convex
comparison theorem gives \(H_v>0\).

We use its full ambient closed angle body \(\overline X\), with selected
real angles \(s_v\), incidence angles \(g_{v,e}\), and inequalities
\[
 |s_v|+2|g_{w,e}|\le\pi,\qquad
 |s_w|+2|g_{v,e}|\le\pi,\qquad e=\{v,w\}.
 \tag{2}
\]
The fixed outside angles are zero. There are no filling rows in the
definition of \(X\). Its energy is the original sum of square energies
\(\mathcal E=4\sum_e(E_{\square,P,e}+E_{\square,Q,e})\); the outside
linear work is zero for the present complete boundary data. Let
\(z_0\in X\) be the solution in (1), and put
\[
 \rho_v(z)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 D_0(z)=\mathcal E(z)-\mathcal E(z_0)
                         -d\mathcal E(z_0)(z-z_0).
 \tag{3}
\]
The exact original differential and its ambient boundary gap are
\[
 d\mathcal E(z_0)=-\sum_{v\in S}H_v\,d\rho_v,\qquad
 \rho_v(z_0)=-\pi,\qquad
 \delta_0:=\min_{\partial X}D_0>0.
 \tag{4}
\]
This is the boundary of the full angle body, not of the constrained
unit-charge polytope. Write
\[
 M_G=e_GM_\infty-\mathcal E(z_0)/\pi,\qquad
 M_\infty=4G_{\rm Cat}/\pi,
 \tag{5}
\]
where \(e_G\) is the number of original edges under consideration.
It is the calibrated real action at (1).
Moreover,
\[
                              M_G>0.                       \tag{5a}
\]
Indeed the square energy has the constant boundary value
\(G_{\rm Cat}/2\). Strict convexity along a segment through any interior
point gives a strictly smaller value at that point. Both original
square factors of every positive edge are interior, so that edge's
energy is strictly less than \(4G_{\rm Cat}=\pi M_\infty\).
There is at least one edge, and the complete outside data add no
linear work. Summing proves (5a).

Let \(\varnothing\ne U\subseteq S\), set \(Y=S\setminus U\), and
delete all edges incident to \(U\). Denote their number by \(r_U\).
The remaining graph is \(G_U\); original outside data, powers, and
all surviving vertices are retained.

For \(\mathbf c'\in(0,\infty)^Y\), let
\(\mathcal F_U(\mathbf c')\) be the set of all weak angle assignments
on \(G_U\) satisfying its version of (2) and
\[
 \sum_{\substack{e\ni w\\e\ {\rm survives}}}g_{w,e}
                     -n_ws_w/2=-\pi c'_w,\qquad w\in Y.
 \tag{6}
\]
Always impose \(|s_w|\le\pi\), including isolated surviving selected
vertices. Their empty-incidence row in (6) is not dropped.
This is a compact set when nonempty. Define the closed variational
rate by
\[
 M_U^{\rm cl}(\mathbf c')
   =\max_{z'\in\mathcal F_U(\mathbf c')}
       \left\{(e_G-r_U)M_\infty-\mathcal E_U(z')/\pi\right\}.
 \tag{7}
\]
Here \(\mathcal E_U\) is the same original energy on the surviving
edges. If the fiber is empty, write \(M_U^{\rm cl}=-\infty\) only as
an extended-real convention; no classical critical action is thereby
assigned to that charge. If \(Y=\varnothing\), the fiber consists of
the empty assignment and the rate is zero.
Every weak surviving square has energy at most its boundary value,
so every action maximized in (7) is nonnegative. In the quantum step
below, the fiber will explicitly be required to be nonempty at every
sampled descendant charge.

## 2. A gap on a below-unit charge box

Assume first \(n_v\ne0\) for \(v\in U\), and define
\[
 B_U=\sum_{v\in U}H_v\left(\frac{|n_v|}{2}-1\right),\qquad
 H_Y=\sum_{w\in Y}H_w,\qquad
 \Delta_U(r)=\frac{\delta_0}{\pi}+B_U-rH_Y.
 \tag{8}
\]

**Proposition 1.** For \(0\le r<1\), every
\(\mathbf c'\in[1-r,1]^Y\), and every admitted assignment
\(z'\in\mathcal F_U(\mathbf c')\),
\[
 M_G-\left\{(e_G-r_U)M_\infty-\mathcal E_U(z')/\pi\right\}
 \ge \frac{\delta_0}{\pi}+B_U
                       +\sum_{w\in Y}H_w(c'_w-1)
 \ge\Delta_U(r).
 \tag{9}
\]
Consequently
\[
                  M_U^{\rm cl}(\mathbf c')\le M_G-\Delta_U(r)
 \tag{10}
\]
on every nonempty fiber. In particular, this statement does not
require an interior minimizer of the deleted energy.

*Proof.* Extend \(z'\) to the original weak body by setting
\[
 s_v=\operatorname{sgn}(n_v)\pi\quad(v\in U),\qquad
 g_{a,e}=0\quad\hbox{at both ends of each deleted edge}.
 \tag{11}
\]
Every restored edge satisfies (2). The extension \(\widetilde z\)
lies on \(\partial X\), since a removed vertex has an original
incidence. Its rows are
\[
 \rho_v(\widetilde z)=-\pi|n_v|/2\quad(v\in U),\qquad
 \rho_w(\widetilde z)=-\pi c'_w\quad(w\in Y).
 \tag{12}
\]
Every restored edge has both square factors on their boundary, with
the exact energy \(\pi M_\infty\) per edge. Thus
\[
 \mathcal E(\widetilde z)=\mathcal E_U(z')+r_U\pi M_\infty.
 \tag{13}
\]
The ambient differential (4) gives, without any restriction that the
comparison charges be at least one,
\[
 \boxed{\quad
 M_G-\left\{(e_G-r_U)M_\infty-\mathcal E_U(z')/\pi\right\}
 =\frac{D_0(\widetilde z)}{\pi}
       +B_U+\sum_{w\in Y}H_w(c'_w-1).
 \quad}                                                     \tag{14}
\]
This is precisely the supporting-plane identity at the original
solution. Use \(D_0(\widetilde z)\ge\delta_0\), and then take the
maximum in (7). No continuity of the maximizer, and no positive
deleted solution, is used. \(\square\)

For all sets with \(|n_v|\ge2\) on \(U\), one charge box works
simultaneously. Put
\[
 H_S=\sum_{v\in S}H_v>0,\qquad
 r_0=\min\left\{\frac12,\frac{\delta_0}{4\pi H_S}\right\},
 \qquad \Delta_*=\frac{3\delta_0}{4\pi}.
 \tag{15}
\]
Then \(B_U\ge0\) and \(r_0H_Y\le\delta_0/(4\pi)\), so
\[
 M_U^{\rm cl}(\mathbf c')\le M_G-\Delta_*
             \qquad\bigl(\mathbf c'\in[1-r_0,1]^Y\bigr)
 \tag{16}
\]
whenever the fiber is nonempty. This is uniform over the finitely
many such nonempty removed subsets of the fixed graph.

There is a useful automatic feasibility condition: if every surviving
power has \(|n_w|\ge2\), then every \(\mathbf c'\in(0,1]^Y\) has the
weak assignment
\[
             g_{a,e}=0,\qquad s_w=2\pi c'_w/n_w.
 \tag{16a}
\]
It satisfies (2) and (6), including every isolated survivor. This
does not assert that its energy minimum is interior. In particular,
original components of arbitrary fixed size with all \(|n_v|\ge2\)
satisfy this feasibility condition after every deletion.

If \(U\) includes powers \(1\) or \(-1\), their contribution to
\(B_U\) is \(-H_v/2\). The sufficient budget for this argument is
exactly
\[
 \frac{\delta_0}{\pi}
 +\sum_{\substack{v\in U\\|n_v|\ge2}}
       H_v\left(\frac{|n_v|}{2}-1\right)
 -\frac12\sum_{\substack{v\in U\\|n_v|=1}}H_v
 -rH_Y>0.
 \tag{17}
\]
It is not automatic. Failure of (17) does not assert failure of the
true gap: it says that this particular uniform supporting estimate
does not certify it. The same identity can also be applied to a
removed zero power by choosing either sign in (11); its row is zero
and its contribution to \(B_U\) is \(-H_v\). No blanket conclusion
for such sets is claimed.

## 3. The actual inserted-descendant hypothesis

We now use the original physical-row source of the pinned transport
theorem, at unit charge before evaluation. Fix \(N\ge2\), put
\[
 D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 F_{a,N}(z)=K_N(c_a,z),\quad M_{a,N}=F_{a,N}(-2).
 \tag{18}
\]
The original crossing elements and their unit scalar carriers are
retained. At \(v\in U\), take the actual omitted-row weight
\(\Omega_{v,a_v}\), possibly from a fixed number of shared microscopic
endpoint coupons in the domain of that theorem. Uniformly over its
fixed compact parameter set,
\[
                         |\Omega_{v,a_v}|\le C N^{3/2}.
 \tag{19}
\]
The original support restriction on these weights is always retained.

Let \(A_N(\mathbf z;\nu)\) be a specified joint polynomial spectator
family. It may include partial coupons and other original insertions.
Here \(\nu\) ranges over any specified parameter set on which the
bounds below are uniform. Evaluate its removed variables to obtain
\(A_{N,\mathbf a}\). All original surviving kernels, powers and full
traces remain in
\[
 Z_{G_U,N}^{A_{N,\mathbf a}}
                     (\mathbf n_Y,\mathbf c';\nu).
 \tag{20}
\]
Edges incident to \(U\) are the explicit physical row factors of the
transport theorem; they are not counted again in (20). Extra spectator
factors do not disappear when a vertex is evaluated.

Fix \(0<r<1\) and some \(\varepsilon_*>0\).
The needed descendant hypothesis is:
there is a sequence \(q_N\ge1\), with \(\log q_N=o(N)\), such that
\[
 \left|Z_{G_U,N}^{A_{N,\mathbf a}}
                 (\mathbf n_Y,\mathbf c';\nu)\right|
 \le q_N\exp\{N M_U^{\rm cl}(\mathbf c')\}
 \tag{21}
\]
uniformly for all its retained parameters \(\nu\), all physical
assignments \(0\le a_v\le\min(J,\varepsilon_*N)\) in the original
support, and the descendant charges actually sampled by the folded
row law below that lie in
\[
 c'_w\in (1+N^{-1}\mathbb Z)\cap[1-r,1],\qquad w\in Y.
 \tag{22}
\]
At every such sampled charge, require in addition that
\(\mathcal F_U(\mathbf c')\ne\varnothing\).
More explicitly, with \(A_w=\sum_{v\in U,\ vw\in E}a_v\), the folded
support is the Cartesian product of the grids
\(\{1-j/N:0\le j\le A_w\}\); only its intersection with (22) enters
this hypothesis. All these coefficients have positive probability.
Nonemptiness and (21) on the whole box (22) are a sufficient stronger
formulation. Condition (16a) supplies the nonemptiness part whenever
all surviving powers have absolute value at least two.

No vanishing or zero-rate estimate is imposed or inferred for
empty-fiber descendants. They are not covered by this induction step.

This is only an upper bound, with a uniform subexponential loss. It
contains neither a lower bound nor a nonzero coefficient. It must
include every surviving full normal and every spectator in (20).
An upper bound for the source with \(A_N=1\) alone gives no assertion
about (21) for another \(A_N\). Likewise, a bound known only at
\(\mathbf c'=\mathbf1\) is not the uniform hypothesis (21).

## 4. The endpoint-window induction estimate

Let \(d_v\) be the original degrees,
\[
 d=\max_{v\in S}d_v,\qquad d_U=\sum_{v\in U}d_v,\qquad
 h(\varepsilon)=2\varepsilon
                  \log\left(\frac{\pi e^2}{2\varepsilon}\right).
 \tag{23}
\]
Let \(T_{U,N}^{\varepsilon}\) be the actual omitted-row contribution
with all \(a_v\le\varepsilon N\), including the crossing values,
the original internal \(U\)-edges, the complete outside incidences,
the weights (19), and the joint spectator. No remaining trace is
replaced by a physical supremum norm.

**Theorem 2.** Suppose \(\Delta_U(r)>0\), every sampled fiber is
nonempty as in Section 3, and (21) holds. For every
fixed
\[
 0<\varepsilon\le\varepsilon_*,
 \qquad \varepsilon<\frac12,\qquad d\varepsilon\le r,
 \tag{24}
\]
one has
\[
 \boxed{\quad
 |T_{U,N}^{\varepsilon}|
 \le C' q_N N^{\,d_U+(5/2)|U|}
       \exp\{N[M_G-\Delta_U(r)+d_Uh(\varepsilon)]\}.
 \quad}                                                     \tag{25}
\]
In particular, choose \(\varepsilon\) so small that
\(d_Uh(\varepsilon)\le\Delta_U(r)/4\). Then, for all sufficiently
large \(N\),
\[
 |T_{U,N}^{\varepsilon}|
 \le C' N^{\,d_U+(5/2)|U|}
                      e^{N[M_G-\Delta_U(r)/2]}.
 \tag{26}
\]
The result is an induction step for this actual endpoint window,
conditional only on the specified descendant upper estimates.

*Proof.* The exact row law gives, at each survivor \(w\),
\[
 p_w(z):=\prod_{\substack{v\in U\\vw\in E}}F_{a_v,N}(z),
 \qquad
 p_w\,\mathcal C_{N,1}
      =p_w(-2)\,\mathbb E\mathcal C_{N,1-K_w/N},
 \quad |K_w|\le\sum_{\substack{v\in U\\vw\in E}}a_v.
 \tag{27}
\]
This is an identity of the full physical algebra, not merely of
values. The laws are symmetric. The exact cosine identity
\(\mathcal C_{N,1+u}=\mathcal C_{N,1-u}\), including its normal,
replaces each charge in (27) by
\(1-|K_w|/N\in[1-d\varepsilon,1]\).
Thus every descendant sampled by the finite expectation lies in
(22). No charge exceeds one.

All row coefficient masses, including the internal removed edges
and complete outside factors, have the bound below. Explicitly, their
literal evaluated-edge factor is
\[
 D_U(\mathbf a)=
   \prod_{\substack{vw\in E\\v,w\in U}}K_N(c_{a_v},c_{a_w})
   \prod_{\substack{vb\in E\\v\in U,\ b\notin S}}F_{a_v,N}(-2).
 \tag{27a}
\]
Each such original edge appears once. Positivity of the physical
rows and their complete-color maximum give
\[
 D_U(\mathbf a)\prod_{w\in Y}p_w(-2)
          \le\prod_{v\in U}M_{a_v,N}^{d_v}
          \le N^{d_U}e^{N d_Uh(\varepsilon)}.
 \tag{28}
\]
The expectation has total mass one. Equations (10), (21), and
(27) therefore bound its actual coupled descendant by
\(q_Ne^{N(M_G-\Delta_U(r))}\). The removed crossing values have
modulus one, since the powers are real integers. Multiply by (19)
and sum over at most \(N^{|U|}\) actual physical assignments.
This proves (25). Finally \(\log q_N/N\le\Delta_U(r)/4\) for large
\(N\), which proves (26). \(\square\)

For the entire collection \(|n_v|\ge2\) on \(U\), use \(r_0,\Delta_*\)
from (15). If the nonemptiness condition and (21) hold for that finite
collection, its uniform loss is the maximum of finitely many
subexponential losses. Choose also
\(\varepsilon\le\min_U\varepsilon_{*,U}\) and \(\varepsilon<1/2\),
as required by the individual hypotheses and (24). A single such
\(\varepsilon\) satisfying
\[
 d\varepsilon\le r_0,\qquad
 \left(\sum_{v\in S}d_v\right)h(\varepsilon)\le\Delta_*/4
 \tag{29}
\]
works for every such \(U\), and for their finite sum.

All surviving first and mixed normal channels have already been
retained in (27). If fixed additional parameter derivatives or
outside normal observations are desired, the same argument applies
provided (21) is imposed on the corresponding inserted descendants
and the other differentiated factors have their stated polynomial
bounds. Such derivative bounds are not inferred from an undecorated
scalar estimate.

## 5. Scope and direct sources

The new implication is the derivation of the strict, charge-uniform
descendant margin from the original geometry before applying the
exact row law. No separate strict gap is assumed for a descendant,
and no positive deleted solution is needed to define or compare the
closed rate (7). The ambient extension (11) is a classical comparison;
it is not asserted to be the literal quantum evaluation \(c_{a_v}\).
The latter is handled separately and exactly by (27)--(28).

This does not prove the upper hypothesis (21). It also leaves the
remaining macroscopic physical rows, paired vertical currents, whole
relative contour, and nonzero geometric cycle coefficient unresolved.
Powers \(1\), \(-1\), or zero are covered here only when the explicit
supporting budget is positive, the sampled fibers are nonempty, and
the same inserted-descendant hypothesis is available.

### Why a global zero-rate floor was rejected

Replacing the rate of an empty global fiber by zero does not repair
the general disconnected-descendant problem. For an isolated surviving
vertex with \(n=\pm1\) and \(c'>1/2\), its row forces
\(|s|=2\pi c'>\pi\), so the weak fiber is empty. Nevertheless the
actual unit-charge trace is nonzero and has modulus one. Indeed the
original crossing matrix gives, for \(\mathfrak q=e^{\pi i/N}\),
\(\kappa=\mathfrak q^{D^2/2}\),
\[
 R=\kappa\sum_{j=0}^D(-\mathfrak q)^j e_j,\qquad
 \phi_N(R)=\kappa(-\mathfrak q)^D,\qquad
 \phi_N(R^{-1})=\overline{\phi_N(R)}.
 \tag{30}
\]
Here \(\phi_N(e_j)=\mathbf1_{j=D}\), and the negative crossing is
coefficient conjugation in the real Newton basis.

A disconnected product of this isolated trace with a positive-rate
component has that component's exponential rate, while the global
weak angle fiber is still empty. A zero floor for that global fiber
would lose the positive component's rate. Thus it is not a general
descendant envelope. Arbitrary additional spectators only make such
an inference less available. A componentwise replacement would require
its own geometric comparison; none is inferred from Proposition 1.
The present theorem instead states the nonempty-fiber restriction
explicitly, with the automatic unbounded-size subcase (16a).

The following three complete direct sources were read at these versions,
their directly used statements checked, and hashes verified:

* [Ambient split-current action comparison](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc:
  the full ambient body, exact gradient, strict boundary Bregman
  remainder, saturated extension, deleted-edge energy constant,
  isolated-survivor convention, and identity (20) before its
  above-unit specialization.
* [Positive physical-row charge transport](research_physical_row_charge_transport.md),
  SHA256 d09d5c669848f0389504cea613244570eca18be03f2b608a359773e423e97040:
  the full-normal positive charge law, coefficient mass \(h\),
  shared original graph factors, below-unit reflection, actual
  omitted-row weights, and polynomial counting.
* [Original arbitrary-power source compilation](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f:
  the exact crossing matrix, its conjugate negative crossing,
  and the original Frobenius coefficient extraction used in (30).

Only written mathematics, text reads and hashes were used. No
mathematical program, numerical experiment, test or compilation was
run. Adopted notes and public manuscripts are unchanged.
