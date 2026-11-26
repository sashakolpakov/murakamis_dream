# Relative holonomy deformation at a supplied marked cone metric

Private written geometry, 16 November 2026.

A supplied complete hyperbolic cone metric with embedded tube and
cusp ends can be deformed with its actual nearby peripheral periods.
The compact part is constructed by an equivariant hyperboloid
average. On each end the developing map is prescribed explicitly,
using the full original period basis. Interpolation takes place
only on compact collars.

The analogous compact-core averaging argument near a complete
cusped base is already proved in
[the general source-regulator completion theorem](general_source_regulator_hyperbolic_equality.md),
Sections 2--5. The extension here starts with nonzero cone-core
lengths and possibly noninjective global development. It retains
the non-small full periods of a supplied cone metric instead of
recovering small logarithms from a complete cusp.

This theorem requires a supplied marked metric. It neither
constructs a corner limit nor assumes that an algebraically regular
corner is already such a metric. No representation rigidity or
positive ideal subdivision is used.

Two additional relative statements are proved below. Developments
that are close in one supplied marked atlas, have the same
representation, and have compatible canonical ends give marked
isometric metrics. The constructed family's total volume is real
analytic. Together these give a conditional one-parameter action
calibration from an accumulating sequence of original positive
metrics. They do not infer metric closeness from holonomy closeness.

## 1. The supplied metric and the admissible representations

Let \(Y\) be the interior of a compact oriented three-manifold with
finitely many torus ends, with its fixed original marking. Put
\(\Gamma=\pi_1(Y)\). At a chosen set \(F\) of ends retain the
primitive basis \((\mu_v,\lambda_v)\), the integer \(p_v\), and
the primitive filling slope
\[
                         \alpha_v=\mu_v+p_v\lambda_v .
 \tag{1}
\]
Suppose a complete finite-volume hyperbolic cone metric \(g_0\)
has been supplied on this filled topology. Its singularities,
if any, are exactly the disjoint selected core curves. Its
restriction to \(Y\), with these cores deleted, is a smooth
oriented hyperbolic metric. Each selected end contains an actual
embedded punctured cone tube
\[
 g_0=dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2,
                         \qquad 0<R<R_v^0 ,
 \tag{2}
\]
whose original marked period vectors, expressed as \(X+i\theta\),
are
\[
 P_{\alpha_v,0}=-2\pi i\chi_{v,0},\qquad
 P_{\lambda_v,0}=V_{v,0}=2H_{v,0}+2is_{v,0},
 \quad 0<\chi_{v,0}\le1,\quad H_{v,0}>0.
 \tag{3}
\]
The other ends are complete rank-two translation cusps. Fix their
actual primitive bases and their complete translation frames.
All chosen end neighborhoods are disjoint.

Let
\[
              \operatorname{dev}_0:\widetilde Y\longrightarrow
              \mathbb H^3,\qquad
              \rho_0:\Gamma\longrightarrow\operatorname{PSL}(2,\mathbb C)
 \tag{4}
\]
be the actual developing map and holonomy on the original unfilled
exterior. The map \(\operatorname{dev}_0\) is an oriented local
diffeomorphism. Global injectivity, faithfulness of \(\rho_0\),
and descent of \(\rho_0\) to a filled group are not assumed.

Consider actual nearby representations \(\rho_t\) of this same
\(\Gamma\), continuous in their finite generator matrices. They
may form a real-analytic family, or the admissible real restriction
of a complex-analytic family. At selected ends require the
following data and identities:

* The peripheral images commute and have the common ordered pair
  of fixed points continued from (4). The longitude is loxodromic
  in this ordering.
* Their similarity multipliers have the specified full logarithms
  \(U_v(t),V_v(t)\), continuous from the actual base values, and
  \[
  U_v(t)+p_vV_v(t)=-2\pi i\chi_v(t),\qquad
  V_v(t)=2H_v(t)+2is_v(t),\qquad
          0<\chi_v(t)\le1,\quad H_v(t)>0 .
  \tag{5}
  \]
* At each unfilled end the peripheral image stays parabolic with
  its common flag and with a real-linearly independent pair of
  translation periods, continued from the fixed complete pair.

The flags and periods are actual peripheral data of \(\rho_t\).
The relation in (5) is a full-period identity, not merely its
exponential. If the family is given in original carrier notation,
one keeps \(n_v=\eta_v-2p_v\); neither \(p_v\) nor the carrier
is changed by this construction.

**Theorem 1.** For every sufficiently small admissible \(t\)
there is an oriented complete finite-volume hyperbolic cone
metric \(g_t\) on the same marked filled topology. On \(Y\)
its developing holonomy is exactly \(\rho_t\). The selected core
at \(v\) has cone angle \(2\pi\chi_v(t)\), length \(2H_v(t)\),
and meridian exactly \(\alpha_v\). All unfilled ends remain
complete cusps with the prescribed translation periods.

On a fixed smaller neighborhood of every end, \(g_t\) is the
explicit tube or cusp model below. On every compact part of
\(Y\), its coefficients tend to those of \(g_0\) in every
fixed smooth derivative order as the representation and end
data tend to their base values. If the data are real analytic
in \(t\), the constructed metric is real analytic in \(t\)
on each compact part, while smooth in its spatial variables.

The theorem asserts existence of a nearby metric for the supplied
admissible representations. It makes no existence assertion for
such representations and no uniqueness assertion for the metric.

## 2. Averaging on the original compact core

Choose disjoint smaller ends and a compact core with slightly
larger compact collars. Cover this compact set by finitely many
relatively compact coordinate balls that lift injectively to
\(\widetilde Y\). Choose a smooth partition of unity subordinate
to those balls. For each ball choose one lift. Its lifted
partition functions and their translates are denoted
\(\eta_{i,\gamma}\), \(\gamma\in\Gamma\), so
\[
 \sum_{i,\gamma}\eta_{i,\gamma}(x)=1,\qquad
 \eta_{i,\gamma}(\delta x)
                =\eta_{i,\delta^{-1}\gamma}(x).
 \tag{6}
\]
The sums are locally finite. On a fixed finite compact family
of lifts covering the core and collars, only finitely many
words \(\gamma\) occur.

Use the future unit hyperboloid model of \(\mathbb H^3\), with
Lorentz product \(\langle\, ,\,\rangle\). Define
\[
 Y_t(x)=\sum_{i,\gamma}\eta_{i,\gamma}(x)\,
              \rho_t(\gamma)\operatorname{dev}_0(\gamma^{-1}x),
 \qquad
 E_t(x)=\frac{Y_t(x)}{\sqrt{-\langle Y_t(x),Y_t(x)\rangle}} .
 \tag{7}
\]
Every term in the convex sum is future unit timelike, so its
sum is future timelike and the normalization is defined. The
Lorentz action is the actual action of \(\operatorname{PSL}(2,\mathbb C)\);
no choice of signs of lifts to \(\operatorname{SL}(2,\mathbb C)\)
is required.

Reindexing \(\gamma=\delta\beta\) in (7) proves
\[
                              E_t(\delta x)=\rho_t(\delta)E_t(x).
 \tag{8}
\]
At \(t=0\) equivariance of \(\operatorname{dev}_0\) gives
\[
 \rho_0(\gamma)\operatorname{dev}_0(\gamma^{-1}x)
                         =\operatorname{dev}_0(x)
 \tag{9}
\]
for every summand. Thus \(E_0=\operatorname{dev}_0\), even
when the latter is not globally injective.

On the finite compact family of lifts, (7) and all its fixed-order
spatial derivatives converge to (9). They involve only finitely
many representation matrices and fixed smooth functions. The
derivative of \(\operatorname{dev}_0\) is invertible there.
After shrinking the parameter neighborhood once, \(E_t\) is
therefore an orientation-preserving local diffeomorphism over
the whole core and collars. Equation (8) propagates this
property to all their lifts.

## 3. Prescribing the selected tube ends

The base selected tube itself supplies its coordinates; no
ideal-cell chart is used. On the universal cover of its torus
write \(x,y\in\mathbb R\) for the original basis
\((\alpha_v,\lambda_v)\). Then
\[
                    X+i\theta=x(-2\pi i\chi_{v,0})+yV_{v,0}.
 \tag{10}
\]
The determinant of this ordered real period pair is
\(4\pi\chi_{v,0}H_{v,0}>0\). Normalize its two fixed points
to \(0,\infty\), with the original selected flag at infinity.
The explicit developing map of (2) is
\[
 \mathcal D(R,w)=
       \bigl(e^w\tanh R,\ e^{\Re w}\operatorname{sech}R\bigr)
            \in\mathbb C\times(0,\infty),\qquad w=X+i\theta .
 \tag{11}
\]
Substitution in the upper-half-space metric
\(y_{\rm hyp}^{-2}(|dz|^2+dy_{\rm hyp}^2)\) gives exactly (2).
Replacing \(w\) by \(w+P\) acts on the target by
\[
                       (z,y_{\rm hyp})\longmapsto
                         (e^Pz,e^{\Re P}y_{\rm hyp}).
 \tag{12}
\]

Since \(H_{v,0}>0\), the longitude has distinct fixed points.
They continue regularly for nearby representations. Choose a
nearby Möbius frame \(A_v(t)\), equal to the base frame at zero,
sending \(0,\infty\) to this ordered pair. It can be chosen
real analytically for analytic data, by using nonvanishing local
eigenvector coordinates and a fixed third-point normalization.
Every peripheral transformation commutes with the loxodromic
longitude, hence fixes its two flags individually. In this frame
its multiplier is the prescribed exponential of \(U_v(t)\)
or \(V_v(t)\).

Define on this universal end
\[
 w_t(x,y)=x(-2\pi i\chi_v(t))+yV_v(t),\qquad
 F_{v,t}(R,x,y)=A_v(t)\mathcal D(R,w_t(x,y)).
 \tag{13}
\]
Its exact equivariance under the two original generators is
\[
 F_{v,t}(R,x+1,y)=\rho_t(\alpha_v)F_{v,t}(R,x,y),\qquad
 F_{v,t}(R,x,y+1)=\rho_t(\lambda_v)F_{v,t}(R,x,y).
 \tag{14}
\]
The real-linear map \((x,y)\mapsto w_t\) has determinant
\(4\pi\chi_v(t)H_v(t)>0\), so (13) is an oriented local
diffeomorphism for every \(R>0\). It agrees with the supplied
developing map at zero, in these actual tube coordinates.

There is no hidden peripheral-injectivity assumption. If an
element of the torus group is trivial in \(\Gamma\), its
image under \(\rho_t\) is the identity. Equations (12)--(14)
then make (13) invariant under it. Thus (13) descends from the
universal torus cover to the component of the lifted end in
\(\widetilde Y\). Its peripheral equivariance makes propagation
to all other components by \(\rho_t\) independent of the
chosen coset representative.

For sufficiently small \(t\), (13) is close to the base map
with all fixed-order derivatives on any compact tube annulus
and a fixed fundamental period parallelogram. Uniform estimates
are needed only on such annuli, not as \(R\downarrow0\).
Deeper in the end (13) is kept exactly.

Adding \(R=0\) to the quotient of (13) gives the original marked
solid torus. The vector for \(\alpha_v\) has zero real part
and angular period exactly \(-2\pi\chi_v(t)\); the vector for
\(\lambda_v\) has real part \(2H_v(t)>0\). Because (1) is
primitive and the change from \((\mu_v,\lambda_v)\) has
determinant one, this fills exactly the prescribed meridian.
No multiple turn or slope change can be inferred from, or
hidden in, an exponentiated equation.

## 4. Prescribing the complete cusp ends

On a chosen complete base cusp use its actual coordinate
\[
                    (w,h)\in\mathbb C\times[h_0,\infty),
 \qquad
 \operatorname{dev}_0(w,h)=A_b(0)(w,e^h),
 \tag{15}
\]
with translations by the original independent periods
\(\ell_{1,0},\ell_{2,0}\). Choose a nearby frame \(A_b(t)\)
sending infinity to the moving common parabolic flag. That
flag is regular near the supplied nontrivial parabolic
generator. In this frame let the actual periods be
\(\ell_1(t),\ell_2(t)\). Define the real-linear map \(L_b(t)\)
by
\[
                  L_b(t)\ell_{k,0}=\ell_k(t),\qquad k=1,2.
 \tag{16}
\]
It is close to the identity and has positive determinant.
The exact end map is
\[
                       F_{b,t}(w,h)=A_b(t)(L_b(t)w,e^h).
 \tag{17}
\]
It is equivariant for the original peripheral group and an
oriented local diffeomorphism at every height. Its pullback
metric is
\[
                         dh^2+e^{-2h}|L_b(t)\,dw|^2.
 \tag{18}
\]
Thus the quotient is an actual complete finite-volume cusp
with the prescribed marked translation lattice. It agrees
with the base map at zero and is close on compact collars.
As in Section 3, equivariance defines it on all lifted end
components without a coset ambiguity.

## 5. Relative interpolation on compact collars

For each selected tube choose
\(0<R_1<R_2<R_v^0\). Define the core average on a neighborhood
of \(R\ge R_1\), and retain (13) on \(R\le R_2\). Choose a
smooth cutoff \(\beta\) equal to one near \(R_1\) and zero
near \(R_2\), constant outside this annulus. It is a function
on the actual base end, and is therefore deck invariant.
On the overlap define
\[
 \widehat D_t(x)=
 \frac{(1-\beta(x))E_t(x)+\beta(x)F_{v,t}(x)}
 {\sqrt{-\langle(1-\beta(x))E_t(x)+\beta(x)F_{v,t}(x),
               (1-\beta(x))E_t(x)+\beta(x)F_{v,t}(x)\rangle}} .
 \tag{19}
\]
The numerator is future timelike. Equivariance of the two
maps and Lorentz invariance make (19) exactly
\(\rho_t\)-equivariant.

Use the same construction on compact complete-cusp collars,
with the cutoff one on the deeper side and the exact map (17)
there. The collars are disjoint. At \(t=0\) both maps in
every interpolation equal \(\operatorname{dev}_0\), so their
interpolation is exactly \(\operatorname{dev}_0\). On their
finitely many compact lifted fundamental pieces, the interpolated
maps are close in \(C^1\). One further restriction of the
parameter neighborhood makes all derivatives invertible with
positive orientation. The cutoff is constant near each end
of the annulus, so the maps fit smoothly.

The result is a global equivariant oriented local diffeomorphism
\[
              D_t:\widetilde Y\longrightarrow\mathbb H^3,\qquad
                         D_t(\gamma x)=\rho_t(\gamma)D_t(x),
 \tag{20}
\]
equal to the exact prescribed end maps sufficiently far into
each end. Pull back the hyperbolic metric. Equivariance
descends it to a smooth hyperbolic metric on \(Y\), with
holonomy exactly \(\rho_t\): an isometry is determined by
its action on the nonempty open image of any local chart.
No discreteness or freeness of the deformed holonomy action
was assumed.

## 6. Completion, marking, and scope

Attach the axes in the exact model portions (13). Their metric
completion has angle \(2\pi\chi_v(t)\), core length \(2H_v(t)\),
and the original meridian and longitudinal screw period.
The underlying topological end and its attachment collar
were never moved or reglued. Hence this is the same marked
filled topology, with disjoint actual tube ends.

The compact part has finite volume. Each bounded-radius tube
has finite volume by the volume density
\(\cosh R\sinh R\,dR\,dX\,d\theta\), and (18) gives finite
volume at every complete cusp. The completed metric is
complete: its filled truncated part is compact and each
remaining cusp has infinite length in its depth coordinate.
This proves Theorem 1.

For a parameter at which every selected \(\chi_v(t)=1\),
the metric is smooth on the selected cores. The unfilled
representation then kills each original filled meridian and
is the holonomy of the constructed complete smooth hyperbolic
metric. At nonintegral cone angles no descent to the filled
fundamental group is claimed; the developing holonomy in
(20) is that of the unfilled exterior.

The full periods in (5) are built into the new end maps,
including their winding integers. This is why the argument
works near a supplied positive-length cone metric without
returning to the complete cusp or resetting logarithms.
It also makes clear its remaining premise in the corner
problem: a marked complete cone metric with these actual end
models must first be obtained at the corner. Convergence of
representation matrices or regularity of the primitive
equations alone is not that premise.

No ideal-cell replacement, quantum-source transport, or
nonzero asymptotic coefficient is supplied by this geometric
deformation.

## 7. Local comparison in one marked atlas

Here compatibility of ends has a precise meaning. The two structures
are expressed on the same marked \(Y\), with the same selected
full period bases and the same complete cusp bases. In their
canonical end coordinates there are specified marked isometries
between sufficiently deep model ends, with equivariant lifts that
identify their developing maps. On compact end collars these
identifications are close to the base identification in \(C^1\).
One may first use them to identify the end coordinates. After this
normalization the two developing maps agree on all sufficiently
deep ends.

This normalization does not assume a new isometry of the compact
core. A near-identity identification of a compact product collar
extends to a diffeomorphism that is the identity on a smaller core:
in a fixed lifted product coordinate its displacement is small and
periodic, and multiplying that displacement by a fixed collar cutoff
gives a map with derivative close to the identity. Its straight
displacement interpolation is an isotopy. On the deeper end keep the
specified model isometry exactly. Canonical tube identifications
extend over the core circle and canonical cusp identifications over
the complete tail. Thus the normalization preserves the original
marking. This is a hypothesis about identified actual end models,
not a conclusion from equality of their exponential eigenvalues.

**Lemma 2 (relative local comparison).** Suppose \(D^{(1)}\) and
\(D^{(2)}\) are oriented developing maps on \(\widetilde Y\), both
equivariant for the same actual representation \(\rho\). Suppose
their canonical ends are compatible as above. After the end
normalization, assume that both maps are sufficiently close in
\(C^1\) to \(\operatorname{dev}_0\) on the same finite compact
lifted atlas covering the core and transition collars. Then there
is a marked diffeomorphism \(f:Y\to Y\), isotopic to the identity,
whose equivariant lift satisfies
\[
                      D^{(1)}\circ\widetilde f=D^{(2)}.
 \tag{21}
\]
It extends to the completed cone metrics, is the specified model
isometry on each sufficiently deep end, and is an actual isometry
from the second metric to the first. In the normalized end
coordinates it is the identity there. The near-identity solution
of (21) is unique within the local inverse neighborhoods used
in the proof.

*Proof.* Fix an auxiliary smooth metric on \(Y\). On the compact
core and transition collars choose finitely many nested coordinate
balls in which \(\operatorname{dev}_0\) is injective. By shrinking
the smaller balls and taking a finite minimum, there are uniform
source and target margins for their inverse charts. The inverse
function theorem and \(C^1\) closeness preserve smaller such margins
for \(D^{(1)}\).

Consequently, at each lifted point \(x\) in these compact pieces
there is a unique solution \(x'\), within one fixed small
auxiliary distance of \(x\), to
\[
                           D^{(1)}(x')=D^{(2)}(x).
 \tag{22}
\]
The target lies in the inverse-chart image because both maps are
close to \(\operatorname{dev}_0\). These inverse solutions are
smooth and close to the identity in \(C^1\). On overlaps the two
candidate solutions belong to a common smaller injectivity
neighborhood of \(D^{(1)}\), so they coincide. This constructs
\(\widetilde f\) on the compact lifted atlas.

The auxiliary metric lifted from \(Y\) is deck invariant.
Equivariance of the two developments shows that
\(\gamma\widetilde f(x)\) solves (22) at \(\gamma x\), and it
lies in the corresponding near-identity neighborhood. Uniqueness
therefore gives
\[
                    \widetilde f(\gamma x)=\gamma\widetilde f(x).
 \tag{23}
\]
No injectivity of either global developing map is used. On an
overlap with the normalized deep ends, \(x'=x\) solves (22);
uniqueness makes the compact construction equal to the identity
there. Extend it by the identity throughout those ends.

The descended map \(f\) is a local diffeomorphism and is uniformly
\(C^1\)-close to the identity on a compact set, with identity
outside that set. To verify the global assertion explicitly, let
\(X(x)=\log_x f(x)\) in the auxiliary metric's uniform small
normal neighborhoods on this compact set, and put
\[
                            f_s(x)=\exp_x(sX(x)),\qquad 0\le s\le1.
 \tag{24}
\]
Take \(X=0\) on the ends. If the original closeness is small
enough, every \(f_s\) is an orientation-preserving local
diffeomorphism, is proper, and equals the identity off a compact
set. A proper local diffeomorphism is a covering: a fiber is
discrete and compact, hence finite, and finitely many inverse
charts together with properness give a common evenly covered
neighborhood. Its image is both open and closed, so it is
surjective on each connected component. A point sufficiently
deep in an end has one preimage, because the image of the
compact support is compact. Thus its covering degree is one.
If a component has no end, the homotopy (24) has degree one
on that compact oriented component and gives the same conclusion.
Hence every \(f_s\) is a diffeomorphism, and (24) is an isotopy.

Equation (21) now gives
\(f^*((D^{(1)})^*g_{\mathbb H^3})=(D^{(2)})^*g_{\mathbb H^3}\).
The exact model identifications extend this isometry across all
selected axes and through the complete cusp tails. Undoing the
initial end-coordinate normalization proves the stated marked
comparison. \(\square\)

The same holonomy without the marked-atlas closeness and compatible
ends is not a hypothesis of this lemma and does not imply its
conclusion.

## 8. Analytic volume and conditional action calibration

**Proposition 3.** For a real-analytic family in Theorem 1,
the total completed volume of the constructed metric is real
analytic in the parameter germ.

*Proof.* Truncate each selected model at a fixed small radius
\(\overline R_v>0\) and each complete model at a fixed log-height
\(\overline h_b\), inside the portions on which the developing
maps are exact. These choices define a fixed compact manifold
with boundary \(K\), independent of the parameter. If
\[
           A_b(t)=\operatorname{Im}
                  \bigl(\overline{\ell_1(t)}\,\ell_2(t)\bigr)>0
 \tag{25}
\]
is the area of the positively oriented actual cusp period
parallelogram, then
\[
 \begin{split}
 \operatorname{Vol}(g_t)
   ={}&\int_K d\operatorname{vol}_{g_t}
       +\sum_{v\in F}2\pi\chi_v(t)H_v(t)
                                      \sinh^2\overline R_v\\
     &+\frac12\sum_{b\notin F}A_b(t)e^{-2\overline h_b}.
 \end{split}
 \tag{26}
\]
Indeed the selected period parallelogram in the \(X,\theta\)
plane has area \(4\pi\chi_vH_v\), and
\(\int_0^{\overline R_v}\sinh R\cosh R\,dR
=\sinh^2\overline R_v/2\).
The cusp density in (18) integrates as
\(A_b\int_{\overline h_b}^{\infty}e^{-2h}\,dh\).
These are exact end volumes, including the full cone periods.

The end terms in (26) are real analytic. On \(K\), formulas
(7), (13), (17), and (19) use finitely many real-analytic
parameter functions and fixed smooth spatial functions. Their
normalizing denominators and the determinant of the metric are
uniformly nonzero at the base. After complexifying the real
parameter locally, the same branches have a common parameter
neighborhood on this compact set, with uniform bounds. Thus
the compact volume density has a uniformly convergent local
parameter power series, and integration over \(K\) is real
analytic. This proves the proposition. The analytic germ of
these formulas is what is used if the admissible cone-angle
set has a boundary at \(\chi_v=1\). \(\square\)

**Corollary 4 (conditional one-parameter calibration).** Let
\(\rho_t\) be a real-analytic one-parameter original branch
through \(t=0\), with the full periods and ends of Theorem 1.
Suppose the marked base cone metric required there has been
supplied. Let \(\mathcal V_{\rm src}(t)\) be the real-analytic
germ of the original marked source action, for example the
already calibrated \(2\pi\operatorname{Re}F(t)\), with its
continued logarithms and absolute normalization retained.

Assume there are distinct \(t_j\ne0\) tending to zero and original
positive metrics \(g_j^{\rm pos}\) at those parameters such that:

* Their holonomy is the same actual \(\rho_{t_j}\), with the
  same full peripheral periods and compatible canonical ends.
* Under supplied original markings, their developing maps
  converge to \(\operatorname{dev}_0\) in \(C^1\) on the finite
  compact lifted atlas of Lemma 2.
* Their already proved positive calibration is
  \(\operatorname{Vol}(g_j^{\rm pos})
                  =\mathcal V_{\rm src}(t_j)\).

Then the metrics constructed in Theorem 1 satisfy
\[
                        \operatorname{Vol}(g_t)
                                      =\mathcal V_{\rm src}(t)
 \tag{27}
\]
for every sufficiently small admissible parameter in this
one-parameter germ.

*Proof.* The constructed developments also converge to
\(\operatorname{dev}_0\) in this same marked atlas. Lemma 2
therefore identifies \(g_{t_j}\) and \(g_j^{\rm pos}\) by actual
marked isometries for all sufficiently large \(j\). In
particular their volumes agree; this step uses more than
equality of holonomy. By Proposition 3,
\(\operatorname{Vol}(g_t)-\mathcal V_{\rm src}(t)\) is real
analytic at zero and vanishes on a sequence of distinct points
accumulating there. The one-variable analytic identity theorem
proves (27). \(\square\)

For a regular original face chart, action analyticity in this
corollary requires that its shapes avoid \(0,1,\infty\) and that
the original logarithmic lifts continue on the chosen germ;
it is not an assertion about an action with reset logarithms.
An accumulating sequence alone would not give the analogous
conclusion for a general multiparameter family.

This corollary does not supply the base metric, the marked-atlas
convergence, or the positive calibration it assumes. In
particular algebraic convergence of representation matrices is
not substituted for its second bullet. It adds neither a
positive ideal subdivision beyond the wall nor any assertion
about the selected quantum coefficient.

## Direct sources and author readback

- [Earlier complete-cusp-base deformation](general_source_regulator_hyperbolic_equality.md):
  Sections 2--5, equivariant hyperboloid averaging and compact
  relative interpolation; read in full. SHA256
  2e86cdb646af4cb348081d0e76a698c109af98286904dfe66664954a043ed8ac.
- [Original tube completion](actual_all_circle_geometric_completion.md):
  Sections 3--5, actual end model, primitive period convention
  and cone-axis completion. Its prior complete read was retained,
  with the used formulas reread. SHA256
  cc58cc7c7a133eb69295d9a447aa39568a3656a2a18a2bd8335eecda314efae9.
- [Uniform original end models](research_regular_corner_uniform_end_tubes.md):
  the exact supplied end geometry available in the regular
  one-square application, with its explicit limitation at the
  compact middle. Read in full. SHA256
  904cc289bb829e4a737064e412fc18adb5e95818cc6590219643a7e373460e81.

Only written mathematics and source-text/hash inspection are used.
No mathematical code, numerical computation, tests or compilation
were run. The entire final proof was reread by the author; all three
complete direct-source reads were completed or retained at their
unchanged versions, their used implications reread, and all three
hashes checked. Independent peer/root review is required before
adoption.
