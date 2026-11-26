# Positive-pole recovery with actual inner profiles and retained outer collars

Private written proof, 16 November 2026.

The selected-parameter positive-pole presentation can be inserted
into finite-chain projected recovery on all four selected kernel
coordinates. Every auxiliary ordinary quotient then has the proved
joint first-turn bound and the original inner \(V_n\) color profile.
The outer turn still acts on each quotient coupled to the complete
received state. Its two collar packets remain supplied data.

The additional implication is this source-specific assembly and
its explicit lower-factor right side. The finite-chain rank
argument itself is the earlier projected-recovery argument.
Neither generic projected rank nor the inner color profile is
used to assert an outer-collar bound.

## 1. Inputs and the exact lower-factor source

Use the original full algebra and operators
\[
 \mathcal A_N=\mathbb C[C]/(P_N),\qquad
 P_N(C)=2T_N(C/2)+2,\quad q=e^{\pi i/N},\quad s=q-q^{-1},
\]
\[
 \kappa=q^{(N-1)^2/2},\quad
 V_n=\kappa^nTR^{-n}T,\qquad D_n=V_nCV_{-n},
 \qquad J=TCT,\qquad U_\tau=V_\tau,\quad \tau=\pm1 .
 \tag{1}
\]
All canonical representatives have degree at most \(N-1\).
All multiplication in this algebra includes the original first
spectral normals at double roots. Half steps below are performed
on ordinary polynomials before canonical reduction.

Fix \(r\ge1\), a selected index \(i\), and an integer \(n\).
Let \(f_j(C)=K_N(w_j,C)\), with independent parameters
\(w_j=2\cosh(\alpha_j/N)\) in fixed bounded complex microscopic
sets. With the ordinary divided-difference operators of the
positive-pole source, put
\[
 Z_j=(f_j,\mathcal Df_j,\mathcal Sf_j,
                    \mathcal S\mathcal Df_j,p,1)^t,\qquad p=P_N,
\]
\[
 g=\bigotimes_{j\ne i}Z_j,\qquad
 P_0=\operatorname{can}
       (f_i g,(\mathcal Df_i)g,(\mathcal Sf_i)g,
                            (\mathcal S\mathcal Df_i)g)^t .
 \tag{2}
\]
The \(4\cdot6^{r-1}\) coordinates in \(P_0\) are unknown
selected coordinates. The other \(2\cdot6^{r-1}\) coordinates
\((pg,g)^t\) are prescribed actual lower-factor columns.
The empty tensor is \(1\).

The positive-pole theorem supplies an exact equation
\[
       [w_i d_N(C)I-\mathcal B_i(C,J,D_1)]P_0=S_i,
 \tag{3}
\]
where \(d_N\) is monic, nonzero, independent of all endpoint
parameters, and has fixed degree. Every root of \(d_N\) satisfies
\[
                         |C-2|\le B_rN^{-2}.
 \tag{4}
\]
The ordered polynomial matrix \(\mathcal B_i\) is independent
of \(w_i\) and \(P_N(w_i)\); its other endpoint dependence is
retained. It has bounded degree and word length.

There is a useful exact description of \(S_i\). Write
\[
 \gamma_i=-\frac{P_N(w_i)}{N^4s^2},\qquad
 r_i(C)=\frac{\gamma_i}{C-c_0},\qquad c_0=q+q^{-1}.
\]
Choose the clearing in (3) to clear each of the four ordinary
source coefficients, as in its construction, and define
\[
 b_1(C)=d_N(C)\mathcal D\frac1{C-c_0},\qquad
 b_2(C)=d_N(C)\mathcal S\frac1{C-c_0}.
 \tag{5}
\]
These are polynomials with rational \(q\)-coefficients, fixed
degrees, and polynomial level cost. Then
\[
 \boxed{\quad
       S_i=-4s^2\gamma_i
         \operatorname{can}(0,b_1g,b_2g,0)^t .
 \quad}                                                       \tag{6}
\]
In particular the selected kernel has been removed from this
right side. The lower-factor tensor and its shared colors have
not been separated.

To verify (6), the ordinary right side before reduction is
\[
 -s^2d_N\big(r_i p g,\,
       (\mathcal Dr_i)(4-p)g,\,
       (\mathcal Sr_i)(4-p)g,\,
       (\mathcal S\mathcal Dr_i)p g\big)^t .                    \tag{7}
\]
All four coefficients multiplying \(p\) or \(4-p\) are
polynomials after clearing. Thus the first and fourth components
vanish in the full quotient and the middle two reduce to (6).
This uses both aliases \(\mathcal Dp=0,\ \mathcal Sp=4-p\)
before reduction. It does not replace those aliases by a
homogeneous equation.

The cleared equation is only a necessary equation for the actual
source. In particular clearing can kill the nonzero endpoint
radical \(p/(C-c_0)\). The ordinary definitions in (2), the
pre-clearing source (7), all actual endpoint data, and the
prescribed \((pg,g)\) columns remain part of the source
specification. They are not recovered by inverting \(d_N\).

## 2. Every finite inner quotient has its actual source budget

Fix a nonnegative integer \(k\). Componentwise ordinary division
of the canonical polynomials gives
\[
       P_j=d_NP_{j+1}+R_j,\qquad
       \deg_C R_j<\deg d_N,\qquad 0\le j<k.
 \tag{8}
\]
If \(d_N\) is constant, use the corresponding scalar divisions
and zero remainders. Every identity (8) is ordinary before
turning; no nonunit is inverted in \(\mathcal A_N\).

**Inner-budget assertion.** For each fixed \(k\), all components
of \(P_j\), \(0\le j\le k\), satisfy, uniformly on bounded
complex microscopic parameter sets,
\[
       \|P_j\|_{[-2,2]}\le N^{O(1)},\qquad
                         \|TP_j\|_{[-2,2]}\le e^{o(N)}.
 \tag{9}
\]
Let \(c_a=2\cos((2a+1)\pi/N)\) and
\(\mathcal J_n(u)=\int_0^u L_n(v)\,dv\) be the original
terminal prefix profile, with \(\mathcal I_n=\mathcal J_n(1/2)\).
For every component, its actual value and angular first normal
obey
\[
 |(V_nP_j)(c_a)|+
 \left|\left.\partial_u(V_nP_j)
           (2\cos(2\pi u+\pi/N))\right|_{u=a/N}\right|
          \le \exp\{N\mathcal J_n(a/N)+o(N)\}.
 \tag{10}
\]
The \(o(N)\) is uniform for
\(0\le a\le\lfloor(N-1)/2\rfloor\) and all the stated
parameter sets. At the odd simple spectral node
only its value is required. Also
\[
                   \|V_nP_j\|_{[-2,2]}
                       \le \exp\{N\mathcal I_n+o(N)\}.          \tag{11}
\]
Fixed parameter derivatives retain these rates.

These conclusions are direct applications of the positive-division
theorem to the actual, ungauged six-state tensor coordinates in
(2). Factor \(d_N\) over the complex numbers and carry out its
fixed number of ordinary divided differences; repeat for the
fixed chain length \(k\). Every factor satisfies (4), and that
theorem is uniform through collisions and arbitrary complex
root configurations in the microscopic disk. No analytic choice
of root labels is needed: ordinary quotient by the monic
polynomial \(d_N\) is uniquely defined.

The coefficients of every \(R_j\) in a fixed monomial basis
are bounded by a polynomial in \(N\). For clarity, successive
division by roots \(a_1,\ldots,a_d\) gives the Newton remainder
\[
       R_j(C)=\sum_{\ell=1}^d
           Q_{\ell-1}(a_\ell)
                    \prod_{b<\ell}(C-a_b),                    \tag{12}
\]
where \(Q_{\ell}\) are the successive ordinary quotients of
\(P_j\). The polynomial real-norm bounds for these quotients
and the microscopic evaluation bound give polynomial
coefficients in (12), including coincident roots. This avoids
any separation assumption or confluent interpolation inverse.
Such coefficients can have degree growing with \(N\) in the
endpoint parameters. They stay actual source data.

Equations (9)--(11) are estimates before any additional coupling
and outer turn. In particular they are not estimates of the
outer packets defined next.

## 3. Literal coupling and the projected chain

Retain the external-state hypotheses of projected recovery.
Namely \(y\) is the complete received full-step state,
independent of all the endpoint parameters in (2), with an
exact rational companion \(Ey=M(v)y\), \(E:v\mapsto q^2v\).
Its finite shifts and inverse are taken on the stated
coefficient chart, and its source/recovery coordinates are
included. For the microscopic conditioning assertion below,
retain the bounded-degree rational coefficient presentation
and independent parameter/source-symbol specialization of
projected recovery as well. Any additional parameter relations
must be handled in that presentation, not ignored after
choosing a formal minor. Additional shared spectators remain
inside the same linear operation.

Let \(\mathfrak F\) denote, in order, the original \(V_n\)
on the inner coordinates, coupling to \(y\), full even/odd
descent, and the original \(U_\tau\). The packets include all
shifted and reflected coordinates required by the full-step
interface. In particular
\[
        X_j=\mathfrak F(P_j),\qquad
        Y_j=\mathfrak F(R_j)                                  \tag{13}
\]
contain the actual source \(U_\tau[(V_nP_j)y_\nu]\), with
canonical multiplication and original scalar carriers.

The exact connection construction, with one common clearing
independent of the selected \(w_i\), gives finite-band operators
\(\mathcal A,\mathcal L,\mathcal H\) such that
\[
 \mathcal A=a(D_\tau)I,\qquad a\ne0,
\]
\[
       (w_i\mathcal L-\mathcal H)X_0
                             =\mathcal A\mathfrak F(S_i),
 \qquad
       \mathcal L X_{j+1}
                             =\mathcal A X_j-\mathcal A Y_j .
 \tag{14}
\]
The identities defining \(\mathcal L,\mathcal H\) hold on
arbitrary canonical inner vectors, so the same operators
apply at every quotient level. No rational inverse of
\(\mathcal L\) is asserted.
The external clearing \(a\) need not have only positive-endpoint
roots. It is multiplied into the rows, never used as the
ordinary divisor in (8). The positive-pole statement concerns
that inner divisor \(d_N\).

The precise two supplied source classes in (14) are:

* the lower-factor tensor (6), still coupled to the entire
  received state and passed through both original turns;
* the remainders \(R_j\), which replace the selected inner
  block by fixed-degree polynomial coupons, with their
  actual endpoint-dependent scalar coefficients.

In contrast to the earlier two-state construction, the first
class need not be described by fixed-index physical terminal
rows. Half-step coordinates can sample even half-grid colors.
Those sampled values and normals retain their actual dependence
on the endpoint parameters; no bounded-degree physical-row
formula is presumed for them.

## 4. Full-normal projected recovery and its exact rate scope

Choose the same finite formal interior window as in projected
recovery, on an orbit
\[
       v_j=\zeta q^{\delta+2j},\qquad \zeta\ne\pm1.
 \tag{15}
\]
All \(X_j\) use the same component set and support interval.
Include every output row whose shift range meets that support.
Supply the complete exterior collar of every \(X_j\), on
both sides, as well as all source and remainder packets.
The prescribed \((pg,g)\) sector is moved to the right side
before testing any kernel. If it is stored in the same array,
its actual definition rows are retained; it is not counted
as an additional homogeneous selected sector.

Let \(\mathcal V\) be the finite space of the unknown interior
value-and-first-normal packets and put \(d_I=\dim\mathcal V\).
Take \(k=d_I\) divisions. Then the augmented matrix
\(\mathsf M\) of (14) recovers the projection \(\Pi X=X_0\):
\[
                         \ker\mathsf M\subseteq\ker\Pi .
 \tag{16}
\]
This holds over the formal coefficient field under the same
external-companion assumptions as the earlier theorem.

Here is the argument, to specify its use with four coordinates.
Replace each ordinary operator \(L\) by the jet operator
\[
                    L^{\rm jet}=
                  \begin{pmatrix}L&0\\L_u&L\end{pmatrix}.       \tag{17}
\]
The scalar \(\mathcal A=a(D_\tau)I\) is injective on finite
support: its nonzero extreme acts on the first nonzero
component row, using the complete exterior output rows.
The original extremes of \(D_\tau\) are units on (15).
This proves value injectivity and then normal injectivity.

In a homogeneous test of (14), suppose \(X_0\ne0\).
Take its highest Laurent coefficient \(w_i^m x_0\) at
\(w_i=\infty\). The first row yields
\(\mathcal L^{\rm jet}x_0=0\). Extract the coefficient
of \(w_i^m\) from every auxiliary recovery row. It gives
\[
       \mathcal L^{\rm jet}x_{j+1}
                     =\mathcal A^{\rm jet}x_j,\qquad j<d_I.
 \tag{18}
\]
Higher Laurent coefficients of auxiliary packets do not
affect this extraction. If the \(d_I+1\) vectors in (18)
were dependent, a dependence of smallest last index,
followed by \(\mathcal L^{\rm jet}\) and injectivity of
\(\mathcal A^{\rm jet}\), would give an earlier dependence.
Thus they would be independent in \(\mathcal V\), a
contradiction. This proves (16). It does not prove uniqueness
of every auxiliary quotient packet.

The bounded-degree row-span certificate and microscopic
specialization of projected recovery now apply. The
unknown matrix coefficients involve only the bounded-degree
rational coefficient data, ordinary endpoint variables and
the symbols \(P_N(w_j)\) for unselected factors. The selected
\(P_N(w_i)\), all even-half-grid evaluations, all remainder
coefficients, and all actual source functions remain on the
right side. None is promoted to a bounded-degree coefficient.

In particular, on each rational physical center/residue
specialization and compact microscopic parameter chart where
the first nonzero denominator coefficient of that certificate
is a unit, there are \(C,K\) such that
\[
 \boxed{\quad
 \|X_0\|_I\le CN^K
  \left(
    \|\text{lower-factor packets from (6)}\|
       +\sum_{j<d_I}\|Y_j\|
       +\sum_{j=0}^{d_I}\|X_j\|_{\partial I}
       +\|\text{other retained forcing}\|
  \right).
 \quad}                                                       \tag{19}
\]
All norms refer to the complete finite value-and-normal
packets required by the rows, including fixed shifts of
the exterior collar \(\partial I\). Scalar clearings are
included in the polynomial cost on that chart.
No full-column minor for all auxiliary unknowns is required.
Identified parameters or a particular parameter-zero locus
need their own valid specialization or holomorphic-family
recovery; the unit-chart assertion alone does not supply it.

Thus if the actual right-side packet classes in (19) have
uniform rates \(\beta_{\rm lower},\beta_{\rm rem},
\beta_{\rm collar},\beta_{\rm other}\), the recovered packet
has rate at most their maximum. This is a conditional
consequence with explicit original-source data.

The new automatic information is (9)--(11) for every
pre-outer quotient. The still-required collar estimate is
for the literal packets
\[
 \left.
 U_\tau\operatorname{can}\big[(V_nP_j)y_\nu\big]
           \right|_{\partial I},
 \qquad 0\le j\le d_I,                                       \tag{20}
\]
together with their first normals, reflected coordinates,
and shared-source entries. These are not values of
\(V_nP_j\) at the inner color. Neither (10) nor (11)
is a bound for (20). The lower-factor and remainder
classes in (19) also require their actual composed bounds,
even when an induction is intended to provide them.

Consequently the negative-endpoint ordinary divisions are
removed from the recovery chain, and their former uncontrolled
inner rate is replaced by the proved profile (10). The
remaining step is an outer composed-collar estimate, or a
source-preserving projection that eliminates those collars,
at the required parent-action scale. No such estimate is
asserted here. The original closing functional may be
applied after these exact identities, with all shared
colors retained; it does not turn the inner profile into
a closed-source upper or lower bound.

## 5. Coverage and direct sources

The finite-chain injectivity and bounded-degree specialization
are inherited from projected recovery. The added assembly
uses the full selected four-coordinate positive-pole row,
the explicit lower-factor reduction (6), and the positive
division theorem to give actual inner budgets for every
auxiliary packet. It retains the exterior data that those
theorems do not control.

The following complete sources were freshly read at these
pins, and every directly used implication was checked:

* [Positive-pole selected-parameter module](research_positive_pole_parameter_leading_product_module.md),
  SHA256 d1e68bf6cc47282d089c01509e33d0eec046f03a6df1bb81848bea08778ca540.
* [Finite-chain projected recovery](research_multikernel_parameter_leading_projected_recovery.md),
  SHA256 04ff3a2fe980009d527214407b20709b9c962a5935314cf2666619f03447034d.
* [Positive division and actual inner profiles](research_positive_endpoint_quotient_source_bounds.md),
  SHA256 cd773c98ee07750f5ccdae4b95d9e76042a1a1e7cc7f59f4f1d6a9dedf3eb766.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build,
or compilation was run. Frozen notes and public manuscripts
are unchanged.
