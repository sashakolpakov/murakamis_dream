# The transverse Hessian of the actual soft-cut braid phase

Private written proof, 18 November 2026.

Under an actual positive complete ideal gluing certificate, the
geometric critical germ of the literal soft-cut braid phase is
smooth of dimension one. In its independent occupation coordinates
the Hessian has precisely the residual framing direction as kernel.
The common momentum has already been quotiented in passing to those
coordinates; it is not a further variable to remove from the phase.

This applies to every fixed finite braid of a one-cusped hyperbolic
knot exterior supplied with the stated certificate. Existence of
such a positive triangulation for every hyperbolic knot is not
assumed. The result is a local complex Hessian theorem. It does not
compute the residual framing period or any physical cycle coefficient.

The complete proof directs are M (the actual crossing/representation
scheme), S (the soft-cut ideal), R (marked positive gluing rigidity),
and F (the complex-cut and common slit frame), pinned below.
The incidence-coordinate and gradient-scheme adapter is proved here.

## 1. The actual phase and the theorem

Fix a finite braid of the knot with \(c\) crossings, counting both
signs positively. Its closed crossing graph has \(c\) vertices and
\(2c\) oriented wire arcs. Put
\[
 \Lambda=\ker(L:\mathbb Z^{2c}\longrightarrow\mathbb Z^c),
 \tag{1}
\]
where \(L\) has incoming coefficient \(+1\) and outgoing coefficient
\(-1\). Each crossing has two incoming and two outgoing arcs.
Loops are allowed. The graph is connected and has rank \(c-1\);
therefore \(\Lambda\) is free of rank \(m=c+1\).
Choosing a spanning tree makes its chord occupations an integral
basis: the tree occupations are recovered uniquely by leaf
elimination. The cut edge may be a chord, since the oriented knot
is an Euler circuit and that edge is not an undirected bridge.

Use unwrapped logarithmic occupations \(\zeta_e\), so the local
wire space is the linear space
\[
 W=\ker(L:\mathbb C^{2c}\longrightarrow\mathbb C^c).
 \tag{2}
\]
Choose chord coordinates \(z_1,\ldots,z_m\) on \(W\).
Every signed transfer is its original difference of wire positions.
There is no additional independent transfer variable after this
linear matching is imposed.

Keep M's literal signed principal crossing expressions, all original
pivots and framing, and a trace-one complex-binomial cut as in F.
Write \(c_0=2\pi i\), \(u=\zeta_{\rm cut}\), and
\[
 \Phi_\theta=S_0+g_\theta(u)-c_0\sum_{j=1}^m n_jz_j,
 \tag{3}
\]
\[
 g_\theta(u)=c_0\!\left[-t\log t-(1-t)\log(1-t)
                   +t\log\theta+(1-t)\log(1-\theta)\right],
 \qquad t=u/c_0.
 \tag{4}
\]
The logs are the matching sheets near \(\theta=1/2\), with
\(\theta\ne0,1\). The fixed integers \(n_j\) are the actual local
Fourier correction which makes the derivative vanish at the
chosen exponentiated critical point. It changes neither the
finite lattice values nor the Hessian. At \(\theta=1/2\), this
is S's real-binomial cut. F permits nearby complex \(\theta\)
and supplies regular geometric slit frames there. Its exact
cut current and exponential cost remain unchanged.

Suppose the actual exterior has R's marked positive complete ideal
gluing certificate. Fix its complete oriented holonomy, the original
central lift, and the selected peripheral eigenflag, with the
meridian eigenvalue fixed exactly to its complete value.
Take a regular source chart as supplied by S/F and choose the
compatible logarithmic lift in (3).

Then, near the corresponding geometric point \(z_*\),
\[
 \operatorname{Crit}(\Phi_\theta)
      \text{ is smooth of dimension }1,\qquad
 \ker\Phi_\theta''(z_*)=T_{z_*}\operatorname{Crit}(\Phi_\theta).
 \tag{5}
\]
Consequently the \(m\)-variable Hessian has rank \(m-1=c\).
The surviving tangent is the actual \(r\)-framing direction.
The assertions hold on a sufficiently small neighborhood of any
such chosen frame and cut parameter, not uniformly over all braids.

## 2. Crossing momenta and the exact incidence adapter

At one positive crossing, write the input log positions \(a,b\)
and the transfer \(n\); the output log positions are \(b+n,a-n\).
At a negative crossing they are \(b-n,a+n\). These are linear
coordinates on the three-dimensional conservation hyperplane.
M's exact generating identities, in the factorial basis, say
\[
 dS_v=\sum_{\rm out}\pi_{v,e}\,d\zeta_e
                 -\sum_{\rm in}\pi_{v,e}\,d\zeta_e,
 \qquad \pi_{v,e}=\log p_{v,e},
 \tag{6}
\]
on that hyperplane, with the external meridian fixed.
They are precisely the actual canonical crossing graph, for
both signs. In particular M's explicit rational inverse proves
the equality on local Artin algebras, where all chart denominators
remain units. Multiplying every momentum at this crossing by one
common scalar does not change (6).

Conversely (6) determines its four log momenta up to that one
common additive constant. The annihilator of the conservation
hyperplane is the one-dimensional span of its defining linear
form. Thus two coefficient lists in (6) differ exactly by the
same addition to every \(\pi_{v,e}\). This is true over each
local Artin algebra as well. No local momentum equation is lost:
M's three derivative identities recover its three independent
momentum ratios and its regular signed crossing correspondence.

For clarity, one can implement the gluing entirely linearly.
Extend each \(S_v\) holomorphically off its conservation
hyperplane by a fixed linear retraction. Its four partial
derivatives give one choice of the signed momenta in (6);
any other choice adds a vertex constant \(\lambda_v\).
On an arc from one crossing to the next, let
\[
 R_e=\pi_{{\rm out},e}-\pi_{{\rm in},e}
                       +g_\theta'(u)\,1_{e={\rm cut}}.
 \tag{7}
\]
The retained pivotal linear terms can be included in this
coefficient list. Their logarithmic multipliers are fixed
integer turns; they do not alter the following linear argument
or its Hessian. The compatible Fourier correction fixes the
same local additive constants.

More explicitly, extend the integer covector \(n\) from the chord
basis to the wire space by using its coefficients on the chord
edges and zero on the tree edges. Assign each resulting linear
term to one incident crossing. Subtracting it from that local
primitive changes its half-edge log momentum by an integer
multiple of \(c_0\), so it does not change its exponentiated
canonical graph. We use those local log branches in (7).
This realizes the exact corrected derivative in (3), rather
than silently dropping a nonzero lattice covector. The pivotal
integer turns are treated in the same way.

The differential of the total phase, restricted to \(W\), is
the restriction of the covector \(R\). Adding the vertex
constants changes \(R\) by \(-L^t\lambda\). The exact sequence
\[
 0\longrightarrow\mathbb C
   \longrightarrow\mathbb C^c
   \mathop{\longrightarrow}^{L^t}\mathbb C^{2c}
   \longrightarrow W^*\longrightarrow0
 \tag{8}
\]
therefore shows that constrained stationarity is equivalent to
being able to set every \(R_e\) equal to zero by local momentum
rescalings. Its kernel consists of the one global common rescaling.
There is a fixed linear right inverse on \(\operatorname{im}L^t\),
obtained by deleting one vertex row and using the same spanning
tree. Thus all these constructions commute with extension to
local Artin algebras; they are not merely tangent-space arguments.

Exponentiated stationarity gives the same germ after its prescribed
integer correction: near zero, \(e^w-1=w\) times a holomorphic
unit. Local logs of all momenta and chart functions are available
because they are units at the chosen point. Equation (8) proves
an isomorphism of the actual gradient scheme in the \(m=c+1\)
chord variables with the glued canonical-graph scheme modulo
the single common momentum.

This resolves the coordinate count. The enlarged graph keeps
local momenta and their one global scale; the chord phase has
already eliminated that scale. Removing another phase variable
as a “common momentum quotient” would be incorrect.

## 3. The soft cut leaves exactly one framing parameter

On every noncut arc (7) is ordinary momentum matching.
On the cut it is
\[
 \frac{p_{\rm out}}{p_{\rm in}}
       =e^{-g_\theta'(u)}
       =\frac{1-\theta}{\theta}\frac{u}{c_0-u}.
 \tag{9}
\]
S's ordered-coproduct ideal calculation applies to precisely
these internal rows. Closure on the other strands and the
preserved total \(K,E,F\) force the cut \(K,e,f\) to close.
On the stated unit chart this also forces
\(p_{\rm out}=p_{\rm in}\). Hence the ideal of (9) is exactly
\[
                              (u-c_0\theta).
 \tag{10}
\]
F proves the same assertion for the complex probe, without
discarding its finite-source current. Conversely a full braid
fixed point satisfying (10) obeys all these weighted rows.

Quotient the one common momentum by setting the cut momentum
to one. M's explicit formula then puts its selected eigenflag
at \(1=(1,1)^t\), with the exact inverse eigenvalue convention.
Its rational Gauss inverse and Hurwitz identities give an
isomorphism, including on Artin test rings, with the selected-flag
framed knot representation germ. These are actual braid-closure
relations, not only equations for peripheral eigenvalues.

For the one-cusped positive certificate, R identifies the decorated
representation germ modulo simultaneous \(\operatorname{PGL}_2\)
with a smooth one-dimensional germ whose coordinate is the
marked meridian similarity log. Fixing that log exactly to zero
makes this unframed germ a point, also on local Artin algebras.
The fixed eigenvalue condition matters: an unspecified invariant
flag of a parabolic can have an infinitesimal motion, which R
explicitly excludes by retaining the exact eigencharacter.

Complete holonomy is irreducible, and its knot meridians are
noncentral parabolics with nonzero trace in the retained lift.
A projective centralizer element, lifted to a matrix, conjugates
each lifted meridian to itself up to sign. Its nonzero trace forces
the sign to be plus. The meridians generate the group, so this
matrix commutes with the entire irreducible representation and
is scalar: a nonscalar commuting matrix would give a common
invariant eigenline. The projective centralizer is therefore trivial.
M consequently identifies the remaining framed germ
with a smooth open part of the two-dimensional group
\[
                       B_1=\operatorname{Stab}_{\operatorname{PGL}_2}(1).
 \tag{11}
\]
This statement uses both the Artin-scheme comparison and R's
rigidity; no dimension count replaces either.

Its explicit local coordinates are
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 F^{-1}J_1F=\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix},
 \quad A_{\rm cut}=(1+s)^{-1}.
 \tag{12}
\]
On the matching log sheet,
\[
 u=-\Log(1+s),\qquad du=-\frac{ds}{1+s}.
 \tag{13}
\]
Near the midpoint \(s=-2\), this differential is a unit
in the \(s\)-direction. For a nearby complex \(\theta\),
(10) is therefore precisely
\[
                         s=e^{-c_0\theta}-1,
 \tag{14}
\]
leaving the free coordinate \(r\). The derivative remains a
unit and \(s\ne0\) on this neighborhood. Thus the actual
gradient scheme of Section 2 is smooth of dimension one.
The common momentum is distinct from \(r\): the former
diagonally changes the chosen eigenflag coordinate, whereas
the latter conjugates the other holonomies by the stabilizer
of the now fixed noncentral cut meridian.

## 4. Hessian and a transverse holomorphic normal form

The defining ideal in chord coordinates is generated by the
actual marked derivatives of \(\Phi_\theta\). Its Zariski
tangent space is therefore the kernel of the Hessian, before
any reducedness assumption. Section 3 proves that this scheme
is reduced and smooth of dimension one. This proves (5),
including exclusion of further infinitesimal null directions.
The coordinate \(r\) gives its entire tangent, not a presumed
redundant equation.

There is a holomorphic Morse--Bott normal form, if desired
without importing a stationary-phase assertion. Choose local
coordinates \((r,y_1,\ldots,y_{m-1})\) flattening the smooth
critical curve to \(y=0\). Its phase value is constant along
that curve, since the full differential vanishes there.
The Hessian on the normal \(y\)-space is invertible. Taylor's
integral formula gives
\[
 \Phi_\theta(r,y)-\Phi_\theta(r,0)
                   =\tfrac12 y^t A(r,y)y
 \tag{15}
\]
with \(A\) holomorphic, symmetric and invertible near the point.
A constant complex congruence makes \(A\) equal to the identity
at that point. On a smaller neighborhood its convergent matrix
binomial square root is symmetric and holomorphic; setting
\(Y=A(r,y)^{1/2}y\) is an invertible holomorphic coordinate change.
Consequently
\[
              \Phi_\theta=\Phi_\theta(z_*)+
                              \tfrac12\sum_{j=1}^{m-1}Y_j^2.
 \tag{16}
\]
The free coordinate \(r\) remains. Rescaling to normalized
occupation variables or multiplying the phase by the nonzero
physical constant \(1/(2\pi i)\) does not change the corank.
This applies to the full chord/transfer phase used in an
oblique residue presentation; it is not a Hessian of an
additional coherent occupation sum.

## 5. Scope and complete source pins

The conditional “if the old framing kernel has dimension two”
in S is now discharged for the stated positive-certificate
braid source. The related two-framing result for a different
augmented-plat source already appears in its critical-scheme
coverage; it is not used as a substitute for Section 2 here.

The positivity hypothesis concerns the supplied complete
triangulation of the actual exterior. The local braid shapes
need not themselves be positive. No positive triangulation
is asserted for every knot. No real-contour negativity,
finite-\(N\) gauge quotient, nonzero \(r\)-period, physical
intersection number or scalar asymptotic follows from (16).
All original cut, pivot, framing and support currents remain.

* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* S: notes/research_soft_binomial_cut_stationary_source.md, SHA256
  667cb1eb70b770552de05e6f95f518016852b2c0aecdc874c3dff167fccb3d8b.
* R: notes/general_marked_multicusp_gluing_rigidity.md, SHA256
  f882d2c7d1f723590391d3cc03dcd9bba7a12d13c2e006c6dea570e1b4af1b42.
* F: notes/research_literal_factorial_common_slit_frame.md, SHA256
  9764a2b77469c7fad402b9b8e609b304a79083bde18fb139031c06fd93650ca8.

All four complete sources were read nontruncated in the active
author sequence; unchanged complete reads were retained where
applicable, their used implications checked and matching pins
renewed. The incidence adapter and normal-form argument above
are written proofs. No mathematical programs or tests were run,
and frozen/public files are unchanged.
