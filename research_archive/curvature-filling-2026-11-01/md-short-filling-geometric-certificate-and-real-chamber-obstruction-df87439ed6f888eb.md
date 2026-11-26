# Geometric continuation beyond long auxiliary fillings

1 November 2026. Private research note; no repository files are changed.

The long-filling argument uses two different facts. The explicit source
equations give an actual marked representation, while a separate local
geometric construction turns a representation sufficiently close to the
complete one into a complete metric on the filled topology. The first
fact continues as rational identities wherever its charts are defined.
The second does not follow from those identities alone.

This note establishes an exact obstruction to using the original real
angle chamber as a global filling domain. It then gives a finite
geometric certificate which does imply completion without a closeness
hypothesis. The certificate uses actual cells and actual logarithmic
link periods, rather than assuming that a hyperbolic holonomy exists.
It also distinguishes the absolute volume calibration from the
nondegeneracy and quantum dominance questions.

The inputs are the explicit original maps and primitive curves in
`notes/actual_conway_general_mask_marked_filling.md`, Sections 3–7;
the local core/link construction in
`notes/general_source_regulator_hyperbolic_equality.md`, Sections 2–7;
the absolute fundamental-chain regulator in
`notes/general_peripheral_representation_volume_bound.md`, Sections 1–2;
and the exact Fourier/filling dictionary in
`notes/actual_main_meridian_joint_filling_transform.md`, Section 6.

## 1. What proximity supplies in the existing proof

The explicit white and shaded matrices give the original group
relations, not a global embedding of their deformed images. In
particular the deformed white pieces can cease to be coplanar.
An arbitrary solution of the rational edge relations is therefore an
actual representation but is not yet a geometric metric.

The completion proof near the complete representation uses proximity
in three separate places.

1. Equivariant averages on a compact core and its collars remain
   orientation-preserving local diffeomorphisms by a uniform positive
   Jacobian bound.
2. The affine development of each cusp link is close to its complete
   translation development. At an axis-type cusp the second common
   fixed point escapes every developed fundamental polygon.
3. The actual periods of the logarithm of that link development tend
   to zero on the fixed primitive generators. Consequently they equal
   the chosen small multiplier logarithms, with no added integral
   multiples of \(2\pi i\).

The last assertion is proved on the fixed generators before they are
multiplied by the filling coefficients. Thus it is uniform over long,
independently chosen slopes. None of these three assertions follows
merely from a small angular saddle in the reduced Fourier integral.

## 2. The strict real pyramid chamber contains no primitive filling

Let \(x\) be an original leaf index and \(t\) its hidden pure
deformation parameter. The strict real ideal-pyramid chamber is
\[
                 |t|<x<\frac12.
\tag{1}
\]
Both sines in
\[
 v=\log\frac{\sin\pi(x-t)}{\sin\pi(x+t)}
\tag{2}
\]
are positive, so this is a single-valued real logarithm on the whole
chamber. It vanishes only at \(t=0\): equality of the sines gives
\(2\cos(\pi x)\sin(\pi t)=0\), and the indicated ranges force
\(t=0\).

For the actual half-twist sign \(\epsilon\in\{0,\pm1\}\), the
original primitive similarity logarithms are exactly
\[
 U=\epsilon v-2\pi it,
 \qquad V=-2v,
 \qquad \chi=t-\frac{\epsilon v}{2\pi i},
 \qquad U=-2\pi i\chi.
\tag{3}
\]
These are the geometric squared-eigenvalue logs, with the original
disk meridian and longitude. A turn of the tangle conjugates the
whole peripheral word and does not change (3).

**Proposition.** No point in (1) satisfies a smooth primitive filling
equation
\[
             aU+bV=2\pi i\eta,
       \qquad \gcd(a,b)=1,\quad \eta\in\{1,-1\}.
\tag{4}
\]

Indeed, its real and imaginary parts would give
\[
             (a\epsilon-2b)v=0,
                         -at=\eta.
\tag{5}
\]
The case \(v=0\) is impossible since it gives \(t=0\).
Otherwise \(a\epsilon=2b\). If \(\epsilon=0\), primitivity gives
\(b=0\), \(|a|=1\), and hence \(|t|=1\). If
\(\epsilon=\pm1\), it gives \(|a|=2\), \(|b|=1\), and
\(|t|=1/2\). Both contradict (1).

This is a local obstruction at any filled leaf, independent of the
remaining tree, stationarity equations, or signs at other leaves.
It includes the disk slopes \(a=1,b=p\). Consequently a real
strict-angle optimization on the original pyramids cannot supply a
global smooth-filling domain. The known long fillings already use
complex continuation. The proposition does not prohibit a different
positive geometric decomposition of a filled manifold.

## 3. Small angular variables and large primitive logarithms

At the direct first Fourier charge, the exact stationary dictionary is
\[
 \tau=2\pi z,
 \qquad V=4\pi iz=2i\tau,
 \qquad \chi-2pz=1,
 \qquad U=-2\pi i-2ip\tau.
\tag{6}
\]
Thus for bounded \(p\), a sequence with \(\tau\to0\) has
\(V\to0\) but \(U\to-2\pi i\). Its meridian multiplier tends
to one, but its continued logarithm does not tend to the small
complete logarithm. More generally the exact unit equation implies
\[
       \max(|U|,|V|)\ge\frac{2\pi}{1+|p|}.
\tag{7}
\]
An analytic contraction estimate based on large angular curvature
therefore cannot, by itself, invoke the existing small-log completion
theorem.

There is nevertheless an exact geometric reason why a bounded written
twist can be long in a normalized cusp metric. Put
\(c=\cot(\pi a)>0\) at the original complete leaf. From (3) and
\(v_t(0)=-2\pi c\), the complete auxiliary shape in the primitive
\((\mu,\lambda)\) basis is
\[
        \tau_{\mathrm{aux}}
          =\frac{dV}{dU}(0)
          =\frac{2ic}{1-i\epsilon c},
       \qquad \Im\tau_{\mathrm{aux}}>0.
\tag{8}
\]
Here the factor two matters: the quantity denoted by \(\tau_i\)
in the color Hessian of the marked-filling note is half of (8).
Normalizing \(\mu\) to a unit horizontal translation, the squared
length of \(\mu+p\lambda\), divided by the cusp area, is
\[
 \mathcal L^2(\mu+p\lambda)
 =\frac{|1+p\tau_{\mathrm{aux}}|^2}
            {\Im\tau_{\mathrm{aux}}}
 =\frac{1+n^2c^2}{2c},
                  \qquad n=\epsilon-2p.
\tag{9}
\]
For a fully circle-marked tree, a circle junction of degree \(D\)
has \(c=1/D\), by the original rigid-spine response calculation.
Its angular curvature is \(D/(2\pi)\). Hence
\[
                 \mathcal L^2=\frac{D+n^2/D}{2}.
\tag{10}
\]
This proves the normalized-length phenomenon, but not a uniform
geometric completion statement across growing trees. The old theorem
has a neighborhood for each fixed framed complete representation;
no bound uniform in \(D\) has been proved there. Equation (6) shows
why its hypotheses cannot simply be read from the angular radius.

## 4. A finite certificate for completion without proximity

The following is a sufficient condition which can be checked on finite
geometric data. It applies to an arbitrary original compact core with
torus ends, including one obtained from the marked Conway cut.

Choose a finite geodesic tetrahedral subdivision of the original
topological core and its ideal ends. Finite interior vertices are
allowed. This avoids an assumption that an arbitrarily prescribed
face triangulation extends using ideal vertices only. Keep the actual
face identifications and primitive peripheral curves.

A certificate consists of the following data and checks.

1. Each tetrahedron is realized as a nondegenerate, positively
   oriented hyperbolic tetrahedron. Its ordered faces are identified
   by the prescribed orientation-compatible isometries. Ideal shapes
   may be checked by positive imaginary parts in their stated order;
   tetrahedra with finite vertices can be checked by the signs of
   their hyperboloid determinants and their nondegenerate face data.
2. Every interior edge has total dihedral angle exactly \(2\pi\),
   and its full face-transition word is the identity. The original
   combinatorial links are circles at edges, spheres at finite
   vertices, and tori at the ideal ends. These are topological
   checks on the chosen subdivision, not assertions about holonomy.
3. On an unfilled torus, the developed similarity triangles have
   translation holonomy with two real-linearly independent primitive
   periods. On a filled torus, the affine peripheral group has a
   common second fixed point \(q\), distinct from the selected
   ideal flag at infinity. Every triangle of one finite developed
   fundamental link region, including its boundary, misses \(q\).
4. Continue \(\log(z-q)\) along the two prescribed primitive
   generator paths in that link, and compute their actual periods
   \(P_\mu,P_\lambda\). For the chosen primitive filling slope,
   verify the unexponentiated identity
\[
                  aP_\mu+bP_\lambda=2\pi i\eta,
                       \qquad \eta=\pm1.
\tag{11}
\]

The triangle avoidance in item 3 is a finite plane-triangle test.
The periods in item 4 can be computed as finite increments of the
logarithm along edges, retaining the winding integers. Exact algebraic
equalities and strict inequalities may instead be verified by certified
interval bounds and exact arguments. A nonzero multiplier alone is
not the period check.

In fact the avoidance test is redundant once the link has been proved
to be a nonsingular similarity torus. Here is a direct reason. In a
developed affine coordinate, the vector field
\((z-q)\partial_z\) is preserved by every transition
\(z\mapsto az+b\) fixing \(q\), since
\(az+b-q=a(z-q)\). It therefore descends to a smooth vector field
on the torus. Every zero has index \(+1\): the development is an
orientation-preserving local coordinate, and near a zero this is the
radial vector field. The sum of the indices on a torus is zero. One
can see that without a metric theorem by choosing the usual periodic
trivialization of its tangent bundle: the opposite sides of a
fundamental polygon cancel in the winding number of the vector-field
components. A finite collection of positive-index zeros is therefore
impossible. The development misses \(q\) everywhere. Thus item 3
may instead require only the actual nonsingular similarity link and
its nontranslation peripheral holonomy; the explicit triangle test
is a convenient independent finite check.

**Completion theorem.** A certificate with these properties gives a
complete finite-volume hyperbolic metric on the original specified
Dehn filling. It uses no proximity to a complete representation.

First, the positive tetrahedra and their face isometries give a local
hyperbolic metric away from the edges and vertices. The full edge
word and total angle \(2\pi\) remove both a longitudinal mismatch
and a cone singularity. At a finite vertex the spherical triangle
links form a smooth curvature-one metric on a topological sphere.
Its compact local spherical development covers the standard sphere;
since the target sphere is simply connected it is an isometry.
The finite vertices are therefore nonsingular as well.

At an ideal vertex, sufficiently high horospherical sections of
the incident tetrahedra are Euclidean triangles. Their induced
transition maps are the prescribed positive similarities. Edge
angle sums remove the singularities at triangle vertices. They
therefore give a nonsingular similarity structure on the compact
cusp torus, with a developing local diffeomorphism \(d\) on its
universal cover. No injectivity of the global three-dimensional
development has yet been assumed.

For an axis-type end, all peripheral maps fix \(q\). The finite
avoidance check and equivariance imply that the entire image of
\(d\) misses \(q\). On the simply connected cover set
\[
                         f=\log(d-q).
\tag{12}
\]
Its real differential is invertible. The Euclidean metric
\(|df|^2\) is invariant under the peripheral deck group and
descends to a nonsingular metric on the compact torus. It is
complete. The lifted local isometry \(f\) is consequently a
covering onto \(\mathbb C\): every finite Euclidean segment
lifts by completeness. Since \(\mathbb C\) is simply connected,
\(f\) is a diffeomorphism. Its periods form a real rank-two
lattice, and the periods on the actual marked paths are precisely
the computed \(P_\mu,P_\lambda\).

In the frame with selected flag infinity, the actual geometric
end contains all sufficiently high vertical rays above each link
triangle. These fit to an equivariant expression
\((d(w),e^t b(w))\), with \(b>0\) and
\(b(w+\gamma)=|a_\gamma|b(w)\). The ratio
\(b/|d-q|\) is positive and periodic; on a fundamental compact
link it is bounded. Thus the end contains an entire equivariant
epigraph \(y>A|d-q|\) for some finite \(A\).

Translate \(q\) to zero and write \(r=y/|d|\). The coordinates
\[
 R=\operatorname{arsinh}(1/r),\qquad
 \theta=\Im f,\qquad
 X=\Re f+\tfrac12\log(1+r^2)
\tag{13}
\]
give the exact metric
\[
       dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2.
\tag{14}
\]
The epigraph contains a full punctured tube \(0<R<R_0\).
Equation (11) gives one full angular turn for the primitive meridian.
A complementary primitive period has nonzero real part, since the
period lattice has real rank two. Adding the axis produces an ordinary
smooth solid torus with exactly the prescribed meridian slope.

At an unfilled end the translation link similarly develops onto
\(\mathbb C\), and its vertical end contains a full horoball
quotient. It is a complete finite-volume cusp. The compact middle,
the finitely many attached tubes and the unfilled cusps prove global
completeness and finite volume. The complete universal local
development covers simply connected hyperbolic space by geodesic
path lifting, so it is its universal isometry. The representation
is therefore the actual filled geometric holonomy.

The certificate can be applied to a new subdivision or to an explicitly
continued one. It does not claim that the original ideal pyramids
remain positive at short fillings, or that every hyperbolic filling
has already been certified in this way.

## 5. Why multiplier equations do not replace the link certificate

There is an elementary local model for the missing integer. Fix
\(L>0\) and an integer \(k\ge2\). On the universal cover of a
torus choose a complex coordinate with period lattice
\[
                         \langle L,2\pi ik\rangle
\tag{15}
\]
and similarity development \(d(f)=e^f\). The two affine holonomies
are dilation by \(e^L\) and the identity. The local development
is positive and avoids zero. Its actual primitive angular period,
however, is \(2\pi ik\). Formula (14) completes to a tube with
cone angle \(2\pi k\), not a smooth solid torus.

One could write \(2\pi i\) as a logarithm of the identity
holonomy and falsely satisfy a unit algebraic log equation. That
logarithm is not the actual period of this marked link. This model
shows exactly why an exponentiated gluing solution, or arbitrary
choices of logarithms at one solution, do not suffice. It is not
asserted to be a particular Conway counterexample.

The same distinction explains the usefulness of the small-neighborhood
argument: near completeness it proves automatically that the selected
small multiplier logs equal the actual periods. Outside that
neighborhood the equality must be supplied by continuation with
winding control or by the finite link certificate.

## 6. The absolute action can be continued without a hidden volume constant

Let the rational original face maps and all selected peripheral flags
continue along a path from the complete structure, avoiding undefined
charts. Retain the same original oriented fundamental chain, the same
primitive paths, and continuous lifts of all required logarithms.
Work on this marked logarithmic cover, not merely on the projected
character variety. The source identity on that cover is
\[
 dG=\tfrac12\sum_iV_i\,dU_i,
          \qquad \Im G(0)=\operatorname{Vol}(Y).
\tag{16}
\]
The original ideal-chain boundary cancellation continues as a rational
identity; its Bloch–Wigner differential is
\[
 d\operatorname{Vol}(\rho)
 =\tfrac12\sum_i
       (\Re V_i\,d\Im U_i-\Re U_i\,d\Im V_i).
\tag{17}
\]
The absolute representation volume here is that of the same marked
fundamental class. It can be computed using a signed straightened
chain even at intermediate parameters where no positive metric has
been established. It is not a new primitive chosen at each point.

Differentiating (16) gives, along every such path,
\[
 \operatorname{Vol}(\rho)
      =\Im G-\tfrac12\sum_i\Re U_i\Im V_i.
\tag{18}
\]
The initial value fixes the constant. Consequently a path which returns
to the same representation and the same logarithmic peripheral lift
has zero imaginary period in \(G\). A period in its real part need
not be discarded from an exact complex action, but it does not alter
(18). If the peripheral logs acquire integral multiples of
\(2\pi i\), their boundary term in (18) must be continued too.
Resetting only the logs or only the primitive destroys this argument.

Suppose the endpoint also has the geometric certificate of Section 4,
and its actual link periods equal the continued \(U_i,V_i\).
Then (18) is the actual complete filled volume. If \(b_i\ne0\),
the primitive filling action is
\[
 G_{\boldsymbol\sigma}
 =G+\sum_{i\,\mathrm{filled}}
       \left(\frac{a_iU_i^2}{4b_i}
                     -\frac{\pi i\eta_iU_i}{b_i}\right).
\tag{19}
\]
Its derivatives are the marked equations
\((a_iU_i+b_iV_i-2\pi i\eta_i)/(2b_i)\).
At their solution, direct substitution gives
\[
             \Im G_{\boldsymbol\sigma}
                =\operatorname{Vol}(Y(\boldsymbol\sigma)).
\tag{20}
\]
For a meridional slope with \(b_i=0\), one changes to a primitive
peripheral coordinate chart before using (19), or uses (18) directly.
The certificate itself does not exclude that slope.

Thus a geometric certificate does calibrate a continued selected
action, provided that its logarithmic lift and original fundamental
chain are identified. A certificate at an isolated solution cannot
by itself select among differently normalized actions: adding an
imaginary constant to a local primitive preserves all its critical
equations and changes the proposed volume. The complete anchor and
the continued boundary term are substantive data.

## 7. Positivity of cells and nondegeneracy of the source are different checks

For real positive tetrahedral angles, the volume Hessian is negative
definite on each angle plane. With linear edge constraints and an
injective retained-wire map, the restricted sum has a negative
definite Hessian. This is the original complete optimization argument.
It gives uniqueness and analytic response on its strict real domain.

Primitive filling equations are complex and are not those same linear
angle constraints. Section 2 shows that their smooth solutions cannot
lie in the original real pyramid chamber. The complex Hessian must
therefore be checked on the continued branch; positivity of a metric
realized by a different cellulation does not identify that Hessian.

Even the local leaf action supplies a simple warning. For
\[
 g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
\]
its analytic second derivative is
\[
 g_{xx}=4\pi\cot(2\pi x)-2\pi\cot(\pi x)
             -\pi\cot\pi(x-t)-\pi\cot\pi(x+t).
\tag{21}
\]
At \((x,t)=(1/4,1/2)\), all the sine arguments defining this
local analytic chart are nonzero, yet \(g_{xx}=0\).
This is not a claimed glued filling solution. It proves that the
negative real-chamber Hessian does not persist throughout the regular
complex leaf chart merely because its logarithms are defined.

A nonperturbative application should consequently certify both the
geometric data of Section 4 and the determinant bounds for its actual
continued source saddle. Neither assertion follows from the other.

## 8. Present conclusion and the remaining constructive question

There is a concrete nonperturbative geometric theorem: the finite
positive-cell and primitive-log-link certificate implies smooth
completion and, with the continued marked action, absolute volume
calibration. It permits short slopes whenever its checks succeed.
It has not yet been established uniformly for a new family of short
Conway fillings.

The normalized cusp formula (10) makes high-degree circle junctions a
natural test. It proves that a bounded physical power can correspond
to a large normalized slope. Equations (6)–(7), however, show that
the required logarithmic branch is not the old small complete branch.
To obtain a genuine new family, one must construct a finite positive
subdivision along that branch, or exhibit a new geometric subdivision
at its endpoint together with the continued log-link periods. The
analytic inverse-curvature criterion alone does not do this.

No conclusion about short-slope quantum dominance follows from this
note. That requires the separate source, tail, noncancellation and
primitive-lattice estimates at the same continued saddle.
