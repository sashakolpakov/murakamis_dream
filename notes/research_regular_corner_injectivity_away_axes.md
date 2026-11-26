# Uniform regular charts away from the original cone axes

Private written geometry, 16 November 2026.

The adopted volume lower bound gives a uniform normal injectivity
radius at every bounded distance from the retained core, provided
the center stays a fixed positive distance from the genuine axes.
The proof uses short deck translates in one local universal cover.
It does not assume a complete negatively curved universal cover:
only a specified finite hyperbolic ball in that cover is used.

This supplies regular charts for a later marked-limit argument.
It does not identify a marked geometric limit or continue the
metric across the flat-cell wall.

## 1. The supplied metrics and constants

Retain exactly the supplied positive sequence and regular
one-square hypotheses of
[the uniform ball-volume theorem](research_regular_corner_uniform_ball_volumes.md).
The actual completed metrics are \(M_j\). Their genuine singular
sets \(\Sigma_j\) consist of the selected axes with cone angle
strictly less than \(2\pi\). Axes of angle \(2\pi\) are regular.
Outside \(\Sigma_j\) the curvature is exactly \(-1\).
When \(\Sigma_j\) is empty, its distance is understood as infinity.

The adopted compact-middle theorem gives compact \(C_j\subset M_j\)
and uniform constants
\[
 \operatorname{diam}_{M_j}C_j\le D_1,\qquad
 B(o_j,r_*)\subset C_j,\qquad
 B(o_j,r_*)\cong B_{\mathbb H^3}(r_*),\qquad
 v_*=V_{\mathbb H}(r_*)>0,
 \tag{1}
\]
where
\[
                   V_{\mathbb H}(r)=\pi(\sinh(2r)-2r).
 \tag{2}
\]
The preceding comparison proof also establishes that \(M_j\)
is a proper length space, that minimizing paths exist, and that
regular-to-regular minimizers avoid \(\Sigma_j\). Its comparison
holds at every center, not only at centers in \(C_j\).

Fix constants \(L\ge0\) and \(\delta>0\), and define the buffered
regular region
\[
 \mathcal R_j(L,\delta)=
 \{p\in M_j:d(p,C_j)\le L,\ d(p,\Sigma_j)\ge\delta\}.
 \tag{3}
\]
Put
\[
 B=D_1+L+r_*,\qquad
 R=\min\{\delta/8,\ B/4,\ 1\},\qquad
 v_R=v_*\frac{V_{\mathbb H}(R)}{V_{\mathbb H}(B)},\qquad
 \rho=\frac{R\,v_R}{4V_{\mathbb H}(2R)}.
 \tag{4}
\]
All these constants are positive and independent of \(j\).
Since \(v_*\le V_{\mathbb H}(B)\), we have
\(v_R\le V_{\mathbb H}(R)\) and \(0<\rho<R/4\).

**Theorem 1.** At every \(p\in\mathcal R_j(L,\delta)\), the
ordinary exponential map is defined and injective on the open
tangent ball of radius \(\rho\). Under the radial identification
of this domain with \(B_{\mathbb H^3}(\rho)\), it is a Riemannian
isometry onto \(B_{M_j}(p,\rho)\), and also an isometry for its
intrinsic path metric. In particular the normal injectivity
radius is at least \(\rho\).

The smaller ball \(B_{M_j}(p,\rho/4)\) is isometric to
\(B_{\mathbb H^3}(\rho/4)\) also for the ambient distance between
every pair of its points. Thus it is an actual uniformly sized
regular metric chart.

The conclusion concerns all sufficiently large members of the
supplied sequence. It does not assert regularity at a genuine
axis, and it introduces no new filling or geometric-existence
hypothesis.

## 2. The ball-volume input on the buffered region

Since \(C_j\) is compact, \(d(p,C_j)\) is attained. For
\(p\in\mathcal R_j(L,\delta)\), (1) gives
\[
 d(p,o_j)\le L+D_1,\qquad
 B(o_j,r_*)\subset B(p,B),\qquad
                         \operatorname{Vol}B(p,B)\ge v_*.
 \tag{5}
\]
Apply the adopted volume comparison at \(p\) with radii \(R,B\).
Because \(R\le B/4\),
\[
                         \operatorname{Vol}B(p,R)\ge v_R.
 \tag{6}
\]
This is the only quantitative global input used below.

## 3. A hyperbolic ball in a local universal cover

Fix one \(j\) and one \(p\) as above, and let
\[
                             U=B_{M_j}(p,4R).
 \tag{7}
\]
The closure of \(U\) is compact by properness and stays in the
regular locus, because \(4R\le\delta/2\). The set \(U\) is
connected: a minimizing path from \(p\) to any point in it stays
in \(U\). It is an open smooth hyperbolic manifold.

Let \(\pi:\widetilde U\to U\) be its universal covering, with
the lifted length metric, and choose \(\widetilde p\) over \(p\).
The original hyperbolic charts give a developing map
\[
                            d:\widetilde U\longrightarrow\mathbb H^3.
 \tag{8}
\]
For clarity, this does not require completeness. Continue a local
hyperbolic chart along paths by its transition isometries; continuation
around a contractible loop agrees by subdivision into chart squares
and uniqueness of an isometry on an open set. Simple connectedness
therefore makes (8) single valued. Every covering transformation
\(g\) satisfies
\[
                               d\circ g=h_g\circ d
 \tag{9}
\]
for an isometry \(h_g\) of \(\mathbb H^3\). This follows first
near one point and then on all of the connected cover by the same
uniqueness.

Every geodesic from \(p\) of length less than \(4R\) exists and
remains in \(U\). Indeed its distance from \(p\) is at most its
length; its image lies in a compact regular region, where the
smooth unit-speed geodesic equation extends. Lift these geodesics
to \(\widetilde U\). After choosing an orthonormal frame at
\(\widetilde p\), their exponential map gives
\[
 F:B_{\mathbb H^3}(o,4R)\longrightarrow\widetilde U,\qquad
                         F(o)=\widetilde p .
 \tag{10}
\]
Normalize (8) by this frame, so \(d\circ F\) is the identity.
Thus \(F\) is injective. The constant-curvature Jacobi equation
shows that its pullback metric is the hyperbolic metric:
radial length is unchanged and the perpendicular polar fields
have length \(\sinh t\). In particular \(F\) is a smooth local
isometry onto an open subset.

The image in (10) is exactly the radius-\(4R\) metric ball in
the cover, with radial distances from \(\widetilde p\) unchanged.
Here is the needed argument, which avoids completeness of the
cover. If a path from \(\widetilde p\) has length \(a<4R\),
choose \(b\) with \(a<b<4R\). The image
\(F(\overline B(o,b))\) is compact and embedded. Until the path
leaves this image, its inverse under \(F\) has radial distance
at most the length already traveled, hence at most \(a<b\).
It cannot reach the boundary \(F(\partial B(o,b))\); a first
exit is impossible. The path therefore lies in that image and
its endpoint has hyperbolic radial distance at most its length.
Taking infima over paths proves the assertion. Conversely, each
radial segment in (10) has its prescribed length.

Consequently, for every \(0<a<4R\),
\[
 B_{\widetilde U}(\widetilde p,a)=F(B_{\mathbb H^3}(o,a)),
 \qquad
                 \operatorname{Vol}B_{\widetilde U}(\widetilde p,a)
                                      =V_{\mathbb H}(a).
 \tag{11}
\]
We do not assert global injectivity of the developing map beyond
this local ball.

## 4. A short covering displacement has many distinct translates

Suppose \(g\) is a nonidentity covering transformation with
\[
 d_0=d_{\widetilde U}(\widetilde p,g\widetilde p),\qquad
                              0<d_0<R .
 \tag{12}
\]
The covering action is free: a deck transformation fixing one
point is the identity by uniqueness of lifts. Put
\[
                         K=\lfloor R/d_0\rfloor+1 .
 \tag{13}
\]
For \(0\le k<K\), the triangle inequality and the isometric
covering action give
\[
                    d(\widetilde p,g^k\widetilde p)\le k d_0\le R .
 \tag{14}
\]

**Lemma 2.** The \(K\) transformations \(1,g,\ldots,g^{K-1}\)
are distinct.

**Proof.** A repetition would give \(g^m=1\) for some
\(1\le m<K\). Its orbit of \(\widetilde p\) lies in the
radius-\(R\) ball (11). Develop the orbit to the hyperboloid
model of \(\mathbb H^3\), writing its points as future unit
timelike vectors \(x_0,\ldots,x_{m-1}\). Their sum \(S\) is
future timelike. The normalized point
\[
                       b=\frac{S}{\sqrt{-\langle S,S\rangle}}
 \tag{15}
\]
is fixed by \(h_g\), since \(h_g\) permutes the orbit.
Moreover \(b\) lies in the closed radius-\(R\) ball about
\(o=d(\widetilde p)\). Indeed,
\[
 -\langle S,S\rangle
        =\sum_{k,\ell}\cosh d(x_k,x_\ell)\ge m^2,\qquad
 -\langle o,S\rangle=\sum_k\cosh d(o,x_k)\le m\cosh R .
 \tag{16}
\]
Thus \(\cosh d(o,b)\le\cosh R\).

Let \(\widetilde b=F(b)\). By the triangle inequality,
\[
 d(\widetilde p,g\widetilde b)
 \le d_0+d(\widetilde p,\widetilde b)<2R .
 \tag{17}
\]
Both \(\widetilde b\) and \(g\widetilde b\) lie in the
injectively developed ball (10). Equations (9) and (15)
give the same developed point for them, so
\(g\widetilde b=\widetilde b\). This contradicts freeness.
\(\square\)

For every \(q\in B_{M_j}(p,R)\), take a minimizing segment
from \(p\) to \(q\) and lift it from \(\widetilde p\).
Its endpoint \(\widetilde q\) lies in the radius-\(R\) ball
(11). The \(K\) points
\[
                      \widetilde q,\ g\widetilde q,\ldots,
                                      g^{K-1}\widetilde q
 \tag{18}
\]
are distinct, since a nonidentity deck transformation cannot fix
\(\widetilde q\). All lie in the radius-\(2R\) ball, by (14),
and all project to \(q\).

Integrating the multiplicity of the local isometry \(\pi\) on
this ball therefore gives
\[
 K\,\operatorname{Vol}B_{M_j}(p,R)
       \le \operatorname{Vol}B_{\widetilde U}(\widetilde p,2R)
       = V_{\mathbb H}(2R).
 \tag{19}
\]
This elementary counting formula follows by covering the base
by countably many evenly covered coordinate sets and applying
ordinary change of variables to disjoint measurable pieces.
Every summand is nonnegative, so no convergence interchange is
needed beyond monotone addition.

Combining (6), (13), and (19), and using \(K>R/d_0\), proves
the strict displacement bound
\[
                    d_0>\frac{R\,v_R}{V_{\mathbb H}(2R)}.
 \tag{20}
\]
The argument excludes finite-order repetitions without assuming
that the whole universal cover is complete or globally
nonpositively curved.

## 5. From the displacement bound to actual regular charts

The ordinary exponential map at \(p\) is defined for all vectors
of length less than \(4R\), by Section 3, and has nonsingular
derivative there by the same Jacobi calculation. Suppose two
distinct tangent vectors of lengths less than \(\rho\) have the
same exponential image \(q\). Their two radial paths lie in \(U\).
Lift them from \(\widetilde p\). Their lifted endpoints are
distinct by the injectivity of (10) and have the same projection.
They are related by a nonidentity covering transformation.

Concatenating one projected radial path with the reverse of the
other gives a based loop in \(U\) of length less than \(2\rho\).
Its lift joins \(\widetilde p\) to \(g\widetilde p\), for a
nonidentity deck transformation \(g\). Thus
\[
 0<d_0<2\rho
       =\frac{R\,v_R}{2V_{\mathbb H}(2R)}
       <\frac{R\,v_R}{V_{\mathbb H}(2R)} .
 \tag{21}
\]
Also \(2\rho<R\), so (20) applies and gives a contradiction.
This proves injectivity on the radius-\(\rho\) tangent ball.

Every point of \(B(p,\rho)\) has a minimizing segment from \(p\)
of length less than \(\rho\). The segment lies in the regular
region \(U\), so it is one of these radial geodesics. The
injective exponential chart is therefore onto the actual metric
ball. Its pullback metric is exactly hyperbolic. Hyperbolic balls
are geodesically convex, so the intrinsic path metric of this
ball also agrees with its hyperbolic model.

For the asserted ambient-distance statement, take two points in
\(B(p,\rho/4)\). Their hyperbolic joining geodesic stays there
and has length at most \(\rho/2\). Any potentially shorter
competing path in \(M_j\) stays within distance
\[
                         \rho/4+\rho/2=3\rho/4
 \tag{22}
\]
of \(p\). It therefore lies in the already injective
radius-\(\rho\) chart, where its length cannot beat the
hyperbolic geodesic. Thus the smaller ball preserves all
ambient distances, proving Theorem 1.

## 6. What this supplies for a marked limit

The theorem gives uniform regular charts on any fixed buffer
around \(C_j\) that stays a positive distance from genuine axes.
The singular tubes and complete cusp charts remain those of the
uniform original end theorem. It is therefore no longer necessary
to assume a regular injectivity bound merely from curvature or
algebraic regularity of the old tetrahedral shapes.

Identifying a limit with the original marked topology is a further
task. One must select compatible finite charts, control their
overlap maps and their attachment to the original ends, and prove
that the limiting identifications preserve the prescribed marking.
The old tetrahedra may flatten, so their barycentric maps alone
do not supply an invertible limiting chart atlas. No such limit
identification or subsequent metric continuation is claimed here.
No statement about the original quantum source follows from this
injectivity estimate.

## Direct source versions and readback

- [Uniform ball volumes](research_regular_corner_uniform_ball_volumes.md):
  properness, minimizing paths, and ball-volume comparison at all
  centers. SHA256
  756dac12a3e335b74fddd87f804bb05b44ad3fd40640f3e32e596b98aed78d90.
- [Compact middle](research_regular_corner_compact_middle_bounds.md):
  compact \(C_j\), uniform completed-metric diameter, and the
  surviving actual hyperbolic ball. SHA256
  d899199d51f0999b912baa128c9ea1c33d3193a22e87ecbde46f67da08638494.
- [Uniform original ends](research_regular_corner_uniform_end_tubes.md):
  original cone-axis and cusp charts, regularity hypotheses and
  their precise marking. SHA256
  904cc289bb829e4a737064e412fc18adb5e95818cc6590219643a7e373460e81.

All three complete direct source texts were read in this sequence.
Only written mathematics and source-text/hash inspection are used.
No mathematical code, numerical computation, tests or compilation
were run. The entire final proof was reread by the author and all
three pinned source hashes rechecked. Independent peer/root review
is required before adoption.
