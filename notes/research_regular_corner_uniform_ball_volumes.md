# Uniform ball volumes along the original positive cone sequence

Private written geometry, 16 November 2026.

The compact-middle diameter bound and its surviving hyperbolic ball
give a uniform lower volume bound for every small ball centered in
the retained filled core. The comparison needed for this implication
can be proved directly for the actual completed cone metrics. The
essential local fact is that a minimizing path between regular points
cannot pass through a genuine cone axis of angle less than \(2\pi\).

The proof below supplies the polar and cut-locus details rather than
assuming a smooth-manifold comparison theorem at the axes. It does
not construct a metric limit or infer marked geometric continuation.
The preceding compact-middle note remains unchanged.
The comparison is the usual Bishop--Gromov inequality; the point here
is to justify it directly for the supplied original cone metrics
and combine it with their uniform diameter and surviving-ball bounds.

## 1. The actual metric input and the conclusion

Use the supplied positive sequence and all regular one-square
hypotheses of
[the compact-middle theorem](research_regular_corner_compact_middle_bounds.md).
Let \(M_j\) denote the original metric after adding the selected
axes. Its genuine singular locus is a finite disjoint union of closed
geodesic axes whose cone angles are
\[
                     \alpha_{v,j}=2\pi\chi_v^{(j)}\in(0,2\pi).
 \tag{1}
\]
A selected axis with \(\chi_v^{(j)}=1\) is smooth and is included
in the regular locus. Off the genuine axes the sectional curvature
is exactly \(-1\). Near each genuine axis the actual metric is
\[
 dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2,
                       \qquad\theta\pmod{\alpha_{v,j}},
 \tag{2}
\]
with the original longitudinal screw period. Locally one unwraps
that longitudinal period. The uniform end theorem establishes this
model in an actual embedded neighborhood, not only in a development.

The compact-middle theorem supplies compact sets \(C_j\), obtained
by deleting only the open complete-cusp tails, and constants
\[
 \operatorname{diam}_{M_j}C_j\le D_1,\qquad
 B_{M_j}(o_j,r_*)\subset C_j,\qquad
 B_{M_j}(o_j,r_*)\cong B_{\mathbb H^3}(r_*),\qquad r_*>0 .
 \tag{3}
\]
All constants are uniform for sufficiently large \(j\). Set
\[
 V_{\mathbb H}(r)=4\pi\int_0^r\sinh^2t\,dt
                    =\pi(\sinh(2r)-2r),\qquad
 R_*=D_1+r_*,\qquad v_*=V_{\mathbb H}(r_*).
 \tag{4}
\]
Volume means the hyperbolic Riemannian volume off the axes, extended
by zero on the axes. This is also the metric three-dimensional volume:
the local model (2) has volume element
\(\cosh R\sinh R\,dR\,dX\,d\theta\), and the axes have zero volume.

**Theorem 1.** For every point \(p\in C_j\), including points
on the selected axes, and every \(0<\rho\le R_*\),
\[
 \operatorname{Vol}B_{M_j}(p,\rho)
       \ge v_*\,\frac{V_{\mathbb H}(\rho)}
                        {V_{\mathbb H}(R_*)}.
 \tag{5}
\]
For \(\rho\ge R_*\) the lower bound \(v_*\) holds. In particular,
\[
 \operatorname{Vol}B_{M_j}(p,\rho)\ge c_*\rho^3,\qquad
 c_*=\frac{4\pi v_*}{3V_{\mathbb H}(R_*)}>0,
             \quad 0<\rho\le R_*.
 \tag{6}
\]
The balls are balls in the entire completed metric \(M_j\);
their volume is not restricted to \(C_j\).

We prove the comparison used in (5) separately at every level.
It depends only on the local model, the angle bound, and properness.
The constants in (5) come entirely from (3).

## 2. Properness and minimizing paths

Fix one metric \(M=M_j\). Its core \(C_j\) is compact. Each
remaining end is a complete cusp with a compact translation torus
and the metric
\[
                 d\sigma^2+e^{-2\sigma}g_T,\qquad\sigma\ge0.
 \tag{7}
\]
Extend the depth function of one cusp by zero outside that cusp.
It is globally one-Lipschitz: its variation on every rectifiable
path is at most the path length, including crossings of its
boundary torus. Therefore a bounded ball meets that cusp only
at bounded depth. There are finitely many cusps. A closed bounded
ball is consequently a closed subset of the union of \(C_j\)
and finitely many compact cusp collars, and is compact.

The glued metric is a length metric. Properness gives a minimizing
path between every two points: choose paths with lengths decreasing
to their distance, use constant-speed parameterizations on a fixed
interval, and apply compactness to their common bounded image.
The resulting uniformly convergent subsequence has a limit whose
length is at most the limiting lengths, by the definition of length
as the supremum of finite partition sums. It realizes the distance.
Every subsegment of such a path is also minimizing.

The regular part \(M^\circ\) is a smooth hyperbolic manifold.
On it a locally minimizing path is an ordinary smooth geodesic.
The genuine singular axes form a closed set, and they have zero
volume by (2). All bounded balls have finite volume, since they
are compact and the regular and cone charts have locally finite
volume.

## 3. A regular minimizing path cannot cross a genuine axis

At a point of a genuine axis, the local metric is the hyperbolic
cone on the spherical football
\[
 L_\alpha:\quad d\varphi^2+\sin^2\varphi\,d\theta^2,\qquad
       0\le\varphi\le\pi,\quad\theta\pmod\alpha,\quad0<\alpha<2\pi.
 \tag{8}
\]
In polar distance \(\ell\) from that point this is
\[
                         d\ell^2+\sinh^2\ell\,g_{L_\alpha}.
 \tag{9}
\]
This follows directly from (2). In a local unwrapped \(X\) chart,
the change of variables is
\[
 \cosh\ell=\cosh R\cosh X,\qquad
 \sinh\ell\cos\varphi=\cosh R\sinh X,\qquad
 \sinh\ell\sin\varphi=\sinh R.
 \tag{10}
\]
The two poles of (8) are exactly the two axial directions.

**Lemma 2.** Two directions in \(L_\alpha\) have distance
strictly less than \(\pi\), unless they are its two opposite poles.

**Proof.** If neither is a pole, choose their longitude difference
\(\delta\) with \(0\le\delta\le\alpha/2<\pi\). The spherical lune
of width \(\delta\) maps into the football and supplies a path of
length at most
\[
 \arccos\{\cos\varphi\cos\psi+
                       \sin\varphi\sin\psi\cos\delta\}<\pi.
 \tag{11}
\]
The strict inequality holds because
\(\sin\varphi\sin\psi>0\) and \(\cos\delta>-1\): the two
ordinary spherical points are not antipodal. The shorter great
circle arc stays in the lune, which is the intersection of the
two appropriate closed hemispheres. If precisely one direction
is a pole, the meridian distance to the other is strictly between
zero and \(\pi\). Only the opposite poles have distance \(\pi\).
\(\square\)

**Lemma 3.** Every minimizing path whose endpoints are regular
stays in \(M^\circ\).

**Proof.** Suppose a minimizing path has a first point \(a\)
on a genuine axis. The first contact is at positive time, and,
because its other endpoint is regular, is an interior point of
the path. Work in a sufficiently small ball with model (9).
A minimizing segment from the center of this model to a nearby
point is radial: every path has length at least its radial
displacement, and equality requires its link direction to be
constant. Thus the incoming and outgoing short segments have
well-defined directions in \(L_\alpha\). The incoming direction
is not a pole, since the preceding segment contains regular
points.

By Lemma 2 the two directions are separated by a distance less
than \(\pi\). Choose short segments of equal radial length
\(\epsilon\) on each side of \(a\). The hyperbolic sector over
a shortest link path between their directions supplies a path
joining their endpoints shorter than \(2\epsilon\). Explicitly,
if its angle is \(\delta'<\pi\), the joining distance satisfies
\[
 \cosh d=\cosh^2\epsilon-\sinh^2\epsilon\cos\delta'
                              <\cosh(2\epsilon).
 \tag{12}
\]
The path stays inside the same small cone ball. It shortens the
purported minimizer, a contradiction. \(\square\)

This proof allows the outgoing segment to run along the axis.
Such an outgoing pole is still at distance less than \(\pi\)
from the incoming nonpolar direction. No geodesic-through-axis
assumption is hidden in the use of ordinary radial Jacobi fields
below.

## 4. The regular polar domain has full-volume image

Fix a regular center \(p\). For \(u\in S_p^2\), let
\(\gamma_u(t)\) be the ordinary unit-speed geodesic in \(M^\circ\)
as long as it exists there. If its maximal regular lifetime
\(a(u)\) is finite, its unit-speed path is Cauchy and properness
gives a limit. This limit must lie on a genuine axis; at a regular
limit the ordinary geodesic equation extends it.

Define the minimizing cut time by
\[
 c(u)=\sup\{s<a(u):
       d(p,\gamma_u(t))=t\text{ for every }0\le t\le s\},
 \qquad
 \mathcal D=\{tu:u\in S_p^2,\ 0<t<c(u)\}.
 \tag{13}
\]
There is a positive uniform initial interval in (13), by a smooth
normal ball at \(p\). Failure to minimize at one time cannot be
reversed later: a shorter prefix followed by the same suffix is
a shorter path. Therefore (13) is an interval on each ray.

We record the needed cut facts with their proofs.

First, a minimizing segment ending before \(c(u)\) is unique.
Otherwise concatenate a different minimizing prefix with the
original geodesic up to a slightly later minimizing time.
The concatenation is minimizing and stays regular by Lemma 3.
It must be smooth at the joining point, so its terminal velocities
agree. Uniqueness for the smooth geodesic equation makes the
prefixes identical.

Second, a regular point \(q\ne p\) with a unique minimizing
segment is not a cut endpoint. Its segment stays regular by
Lemma 3 and has positive distance from the closed singular locus.
Along this segment the perpendicular Jacobi equation is
\[
                       J''-J=0,\qquad J(0)=0.
 \tag{14}
\]
Its solutions with \(J'(0)=w\) are
\(J(t)=\sinh t\,\mathcal P_t w\), where \(\mathcal P_t\)
is parallel transport. Thus the exponential map has nonsingular
derivative at the corresponding vector \(ru\), \(r=d(p,q)>0\),
and gives a smooth inverse branch near \(q\).

That branch is the unique minimizing branch on a neighborhood.
Indeed, if this failed, choose nearby endpoints and minimizing
paths violating the assertion. Their lengths converge to \(r\).
Properness and the constant-speed compactness argument of Section 2
give a subsequence converging to a minimizing path from \(p\) to
\(q\), hence to the unique given path. Its compact image avoids
the axes, so the nearby paths also remain in a compact regular
neighborhood. Their initial directions converge to \(u\), as is
seen in a fixed small normal ball at \(p\), and their lengths
converge to \(r\). The inverse-function neighborhood of the
exponential map then forces every one of these minimizing paths
to be the specified branch, a contradiction. In particular the
original radial branch continues minimizing a little beyond
\(q\), proving \(r<c(u)\).

It follows that \(\mathcal D\) is open and that
\[
 \exp_p:\mathcal D\longrightarrow
 U_p:=\{q\in M^\circ\setminus\{p\}:
                    q\text{ has a unique minimizing segment from }p\}
 \tag{15}
\]
is a smooth diffeomorphism. The first assertion follows from the
unique-branch neighborhoods just proved; injectivity and
surjectivity follow from the two cut facts and Lemma 3. In
particular the cut-time function is measurable, since
\(\{u:c(u)>t\}\) is open for every \(t>0\).

For completeness, \(U_p\) has full volume. The distance function
\(d(p,\cdot)\) is locally Lipschitz in every regular coordinate
chart. Rademacher's theorem, in its usual Euclidean form that a
locally Lipschitz function is differentiable almost everywhere,
applies in a countable atlas. At a differentiability point \(q\),
first variation along the final short regular part of any
minimizer gives
\[
                    d[d(p,\cdot)]_q(v)=\langle w,v\rangle,
 \tag{16}
\]
where \(w\) is its unit terminal velocity. To see both inequalities,
vary the last endpoint along \(v\), retaining the earlier path;
this gives the upper first-variation inequality for distance.
Use \(-v\) and differentiability for the reverse inequality.
Every minimizer consequently has the same terminal velocity.
The smooth geodesic equation backwards makes them identical.
Thus all differentiability points except \(p\) lie in \(U_p\).
The exceptional set has zero volume, and the axes do also.

This establishes the full-volume polar domain without presuming
a cut-locus theorem for a singular manifold. The analytic tools
used are ordinary compactness of equi-Lipschitz paths, smooth
first variation and geodesic uniqueness, the inverse function
theorem, and the stated almost-everywhere differentiability theorem.

## 5. Volume comparison, including centers on axes

The Jacobi calculation (14) gives the exact polar Jacobian
\(\sinh^2t\) on \(\mathcal D\). By (15), its full-volume image,
and the ordinary change-of-variables theorem,
\[
 \operatorname{Vol}B(p,R)
   =\int_{S_p^2}\int_0^{\min(R,c(u))}\sinh^2t\,dt\,d\omega(u)
   =\int_0^R A_p(t)\sinh^2t\,dt,
 \tag{17}
\]
\[
                  A_p(t)=\operatorname{area}\{u:c(u)>t\}.
 \tag{18}
\]
The choice at a radial endpoint does not affect the integral.
The function \(A_p\) is nonincreasing and lies in \([0,4\pi]\).
Consequently
\[
 \frac{\operatorname{Vol}B(p,R)}{V_{\mathbb H}(R)}
 \quad\hbox{is nonincreasing in }R>0
 \tag{19}
\]
at every regular center. Explicitly, the ratio is the weighted
average of \(A_p(t)/(4\pi)\) on \([0,R]\), with positive weight
\(\sinh^2t\); adding a later interval cannot increase that
average. In particular, for \(0<r<R\),
\[
 \operatorname{Vol}B(p,r)\ge
 \frac{V_{\mathbb H}(r)}{V_{\mathbb H}(R)}
                         \operatorname{Vol}B(p,R).
 \tag{20}
\]

Now let \(p\) be on a genuine axis and take regular \(q_\nu\to p\),
with \(\epsilon_\nu=d(q_\nu,p)\). For \(\epsilon_\nu<r\),
\[
 B(q_\nu,r-\epsilon_\nu)\subset B(p,r),\qquad
 B(p,R)\subset B(q_\nu,R+\epsilon_\nu).
 \tag{21}
\]
Apply (20) at \(q_\nu\) with radii
\(r-\epsilon_\nu\) and \(R+\epsilon_\nu\). It follows that
\[
 \operatorname{Vol}B(p,r)\ge
 \frac{V_{\mathbb H}(r-\epsilon_\nu)}
      {V_{\mathbb H}(R+\epsilon_\nu)}
                         \operatorname{Vol}B(p,R).
 \tag{22}
\]
Letting \(\nu\to\infty\) proves (20) at \(p\). Only the
explicit continuous function \(V_{\mathbb H}\) is taken to a
limit; no assertion about continuity of sphere volumes is needed.
This proves the comparison at every point of \(M\).

The same formula gives the upper bound
\(\operatorname{Vol}B(p,R)\le V_{\mathbb H}(R)\) for a regular
center, since \(A_p\le4\pi\). Ball inclusions as in (21) extend
this upper bound to axis centers also. No smoothness assertion at
the axes is used.

## 6. Uniform noncollapse on the retained filled core

For any \(p\in C_j\), (3) and the triangle inequality give
\[
 B(o_j,r_*)\subset B(p,D_1+r_*)=B(p,R_*),\qquad
                  \operatorname{Vol}B(p,R_*)\ge v_*.
 \tag{23}
\]
Apply (20) with the radii \(\rho,R_*\). This proves (5),
including all singular centers. Larger balls contain the ball
in (23), and \(V_{\mathbb H}(\rho)\ge4\pi\rho^3/3\), proving
the remaining assertions of Theorem 1.

Thus the earlier single surviving ball controls every location
in the uniformly bounded retained core. The conclusion is a
uniform metric volume estimate. It does not assert a uniform
injectivity radius, a limit homeomorphism or developing map,
continuation through a flat-cell wall, or a positive ideal
subdivision at the limit. No implication for the selected quantum
coefficient is drawn.

## Direct source versions and readback

- [Uniform original end tubes](research_regular_corner_uniform_end_tubes.md):
  actual disjoint cone-axis neighborhoods, complete cusp frames,
  and cone angles in \((0,2\pi]\). SHA256
  904cc289bb829e4a737064e412fc18adb5e95818cc6590219643a7e373460e81.
- [Compact middle and surviving ball](research_regular_corner_compact_middle_bounds.md):
  compact \(C_j\), its completed-metric diameter, and the actual
  embedded ball in (3). SHA256
  d899199d51f0999b912baa128c9ea1c33d3193a22e87ecbde46f67da08638494.

Both complete direct source texts were read in this proof sequence.
The volume comparison is proved here for their actual metric,
rather than imported as a singular comparison or convergence theorem.
Only written mathematics and source-text/hash inspection are used;
no mathematical code, numerical computation, tests, or compilation.
The entire final proof was reread by the author and both pinned source
hashes rechecked. Independent peer/root review is required before
adoption.
