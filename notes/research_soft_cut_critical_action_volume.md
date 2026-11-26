# Every regular soft-cut critical action has its representation volume

Private written proof, 18 November 2026.

The regular principal critical scheme of the actual binomial-cut
state is already identified in S. This note calibrates every one
of its boundary-parabolic critical actions, with the integer
Fourier correction made before taking its imaginary part.
The result applies to competing representations, not only the
complete geometric one. Copies of the same projective holonomy
have the same exponential rate and are not separated by this result.

The complete proof directs are S, Q, C and G, pinned below.
The general crossing-chain and logarithmic regulator arguments
are already present in C and Q. Their extension beyond faithful
representations is also explicit in the earlier coverage note
actual_wall_critical_regulator.md, Section 5. The new adapter here
is the soft-cut entropy and its integral characters.

## 1. The actual principal action and its lattice

Fix the literal finite braid of an oriented hyperbolic knot \(K\),
with all signs, tail pivots, writhe compensation and reduced
normalization retained. Work at the physical root
\[
 h=2\pi i/N,\qquad c_0=2\pi i,\qquad M=1.
 \tag{1}
\]
Use independent integral coordinates \(k_i\) on the incidence and
occupation lattice of its finite array, and unwrapped logarithms
\(\zeta_i=h k_i\). Integral affine offsets, if used in choosing
coordinates, remain part of these original integer occupations.
They are not discarded by taking cyclic residues.

Write \(\nu=\log M\) for the meridian logarithm. Q supplies the
actual leading action
\[
 S_0(\zeta,\nu)=G_0(\zeta,\nu)
                     +\sum_j\epsilon_j\operatorname{Li}_2(z_j),
 \tag{2}
\]
where the shapes are monomials with modulus-one constants.
The polynomial \(G_0\) is a real quadratic form plus a purely
imaginary linear form and a real constant. It includes the
Cartan, pivot, original framing and \(\operatorname{Li}_2(1)\)
terms; it is not an unspecified primitive of the gluing equations.
The logarithms and dilogarithms are continued compatibly.

Let \(u\) be the cut logarithmic occupation, an integral affine
linear function of the \(\zeta_i\). S proves that the soft action is
\[
 S_{\rm soft}=S_0+g(u),\qquad
 g(u)=c_0[-(u/c_0)\log(u/c_0)
                 -(1-u/c_0)\log(1-u/c_0)-\log2].
 \tag{3}
\]
Its distinguished local sheet near \(u=c_0/2\) has
\[
                       g(c_0/2)=g'(c_0/2)=0.
 \tag{4}
\]
The finite mean is \((N-1)/2\), not \(N/2\); all its finite
shifts and normal corrections remain in the exact source of S.
Equation (3) is its principal coefficient action.

In this note a regular critical point means a point in S's
localized canonical graph, with the internal and soft cut rows
imposed. S proves, as an equality of ideals, that these rows
are the full braid fixed-point rows together with
\[
                              u=c_0/2.
 \tag{5}
\]
This uses the conserved full ordered \(K,E,F\) coproduct and
the stated unit chart. It is not inferred from a peripheral
eigenvalue equation alone. After a common classical momentum
gauge the cut is \(A=-1,p=1\), with noncentral parabolic meridian.
The corresponding projective representation is denoted \(\rho\).

## 2. The Fourier correction preserves every finite summand

At an exponentiated critical point, on its compatible logarithmic
lift, write
\[
             \partial_{\zeta_i}S_{\rm soft}=c_0 n_i,
             \qquad n_i\in\mathbb Z.
 \tag{6}
\]
The integers are locally constant on a continued critical chart.
Define the corrected action
\[
        S_{\rm corr}=S_{\rm soft}-c_0\sum_i n_i\zeta_i.
 \tag{7}
\]
At every original finite lattice state,
\[
 \exp((S_{\rm corr}-S_{\rm soft})/h)
                 =\exp(-2\pi i\sum_i n_i k_i)=1.
 \tag{8}
\]
Thus (7) is a permitted Fourier character of the same discrete
source, with no new coefficient or endpoint factor. It does not
specify a contour or select the charge of a contributing saddle.
On an integral affine parametrization, its integer offsets give
the same identity, including their retained level dependence.

The entropy sheets can be checked explicitly. If the two logarithms
in (3) change by \(c_0j_0,c_0j_1\), respectively, then
\[
 \Delta g=-c_0(j_0-j_1)u-c_0^2j_1,\qquad j_0,j_1\in\mathbb Z.
 \tag{9}
\]
For the actual cut occupation \(u=ha\), \(c_0=Nh\), its exponential
multiplier is
\[
 \exp(\Delta g/h)
 =\exp[-2\pi i((j_0-j_1)a+Nj_1)]=1.
 \tag{10}
\]
At (5),
\[
 \Delta g=-\tfrac12c_0^2(j_0+j_1)\in\mathbb R,\qquad
 \Delta g'=-c_0(j_0-j_1).
 \tag{11}
\]
The derivative change is absorbed in (6). These are genuine
integer characters, not arbitrary complex shifts of the action.
The real constant in (9) is retained.

## 3. Calibration of the imaginary critical value

Let \(\beta=\sum_j\epsilon_j[z_j]\) be the actual signed
five-shape crossing sum. For compatible branches Q proves
\[
 D(\beta)=\operatorname{Im}S_0
 -\sum_i\operatorname{Re}\zeta_i\,
                     \operatorname{Im}\partial_{\zeta_i}S_0
 -\operatorname{Re}\nu\,
                     \operatorname{Im}\partial_\nu S_0.
 \tag{12}
\]
This identity is algebraic in the logarithmic differential data:
\(\operatorname{Im}\operatorname{Li}_2(z)
 =D(z)-\log|z|\operatorname{Im}\log(1-z)\), while the imaginary
part of a real quadratic polynomial with imaginary linear part
is the real-coordinate pairing with its imaginary gradient.
Compatible dilogarithm monodromy contributes its integer logarithms
and a real constant, so the same identity persists.

On the distinguished entropy sheet, (4)--(5) imply that
\(\operatorname{Im}g=0\) and that every internal derivative of
\(g\) vanishes. Since \(\operatorname{Re}\nu=0\) at \(M=1\),
substitution of (6)--(7) into (12) gives
\[
                         \operatorname{Im}S_{\rm corr}=D(\beta).
 \tag{13}
\]
For another entropy sheet, (11) gives a real value of \(g\)
at the same point. Its internal derivative changes by the
integer covector already corrected in (7). Also
\(\operatorname{Re}u=0\); hence the pairing of that derivative
with the real internal coordinates is zero. Any retained affine
offset in \(u\) is purely imaginary and has the same property.
Thus (13) holds on every compatible entropy sheet.

There is no freely adjustable imaginary constant in (13).
The original Gaussian/framing constants in Q and the normalized
binomial constant in (3) have already fixed it. The preferred
longitude and its inverse eigenflag are the ones in Q; their
spin signs have not been recentered.

The same conclusion holds for the other complete central lift
when carried with the full source conventions. One can either
apply (12) with \(\operatorname{Re}\log M=0\), or twist a
determinant-one representation by the knot's meridian sign
character. Then \(x\) and each \(K_j\) change sign together,
so \(A_j=x/K_j\), transfer ratios and \(x^2\) do not change.
The crossing Bloch sum is unchanged. This is a comparison
of retained classical lifts, not a deletion of quantum signs.

If the full ADO normalization is used, its exact factor remains
\[
 d_N(M)=i^{N+3}\frac{M^{N-1}}{1+M^2+\cdots+M^{2N-2}}.
 \tag{14}
\]
At \(M=1\) it is \(i^{N+3}/N\), and at \(M=-1\) it is
\(i^{N+3}(-1)^{N-1}/N\). These phases and powers must be kept,
and their contribution to the scaled logarithmic modulus is
\(-(2\pi/N)\log N\), tending to zero.
No off-root normal or generic-meridian gauge is discarded.

## 4. The crossing regulator is the competing representation volume

C states its final comparison for complete faithful holonomy.
Its chain proof applies to every representation obtained above.
Here are the ingredients needed to check that extension.

At \(M=1\), the noncentral meridians are unipotent projectively.
Their fixed flags and the actual Hurwitz words supply exactly
C's region decorations. Its determinant identities, three
five-term boundaries and signed four-tetrahedron crossing balls
use unipotence, not faithfulness of \(\rho\). The paired faces
and original strand closures are the same abstract oriented
relative fundamental cycle, with the degree-one cusp marking
and preferred-writhe shear proved in C.

The abstract group in that construction is the knot group,
independent of whether its image under \(\rho\) is faithful.
Choose free auxiliary vertex flags generically. If developed
vertices are forced to repeat, use the normalized alternating
configuration complex: that tetrahedron is zero, and its
repeated-vertex faces cancel in pairs. The five-term map
therefore still identifies the signed crossing sum with the
\(\rho\)-developed fundamental chain. Equivalently one can
subdivide and add generic free interior vertex types; their
stars are balls and change no fundamental regulator.
Continuity \(D(0)=D(1)=D(\infty)=0\) gives the same value for
any normalized degenerate developed tetrahedra.

The longitude commutes with the nonidentity unipotent meridian.
Its projective centralizer consists of the unipotents fixing
that flag, so the peripheral image is boundary-parabolic.
The regulated idealized chain is consequently the signed
representation-volume normalization used in C and G. We obtain
\[
                 D(\beta)=\operatorname{Vol}_{S^3\setminus K}(\rho).
 \tag{15}
\]
A trivial meridian would force a trivial knot representation by
normal generation and give volume zero, but it is outside the
noncentral unit midpoint chart used here.

Combining (13) and (15) proves the actual-source calibration
\[
 \boxed{\displaystyle
   \operatorname{Im}S_{\rm corr}
          =\operatorname{Vol}_{S^3\setminus K}(\rho),\qquad
   \frac{2\pi}{N}\log|e^{S_{\rm corr}/h}|
          =\operatorname{Vol}_{S^3\setminus K}(\rho).}
 \tag{16}
\]
The second equality evaluates the exponential of the principal
action. It is not an asymptotic assertion about the sum (1) in S.

## 5. What the actual filled-group gap now compares

Fix a hyperbolic marked core and any earlier fixed short partial
filling that is already part of that core, in G's scope. Fill the
remaining designated cusps along sufficiently long primitive slopes
\(\sigma_i=(a_i,b_i)\), and suppose the resulting physical exterior
is the knot exterior under consideration. Use a literal braid of
that actual filled knot in S, rather than an unfilled-parent source
equipped only with peripheral eigenvalue equations.

Every regular midpoint critical point of this full braid already
gives a representation of its actual knot group, hence of the
actual filled group. Its remaining main cusp is boundary-parabolic
by Section 4. G therefore applies directly. For every such point
whose underlying projective representation is not conjugate to the
oriented filled geometric holonomy,
\[
 \operatorname{Im}S_{\rm corr}
 \le \operatorname{Vol}(M(\sigma))
       -\min\left\{\frac{\delta}{2},
                         \frac{3c_1}{\ell_{\max}^2}\right\},
 \qquad \ell_{\max}=\max_i\sqrt{a_i^2+b_i^2}.
 \tag{17}
\]
G's positive constants depend only on the fixed core and certificate.
This is a uniform comparison of the regular principal critical
rates of these actual full-word presentations. It needs no matching
of a quantum Fourier label to a centered geometric slope charge:
G uses the full filled-group relations of the representation.

In contrast, a critical configuration of an unreduced parent
partial-filling expression has not been shown by this argument to
satisfy those full matrix relations. Applying (17) to such an
expression still requires that source-to-group map and its action
normalization. The equality of its final invariant with a knot
invariant does not identify the separate critical configurations.

## 6. Equal-rate aliases and remaining source boundaries

Different compatible logarithm or entropy sheets, central lifts,
regular framing points, or retained flag descriptions of the same
projective representation all have the same value in (16).
Their corrected actions can have different real parts. The associated
oscillatory phases, multiplicities and cycle coefficients have not
been added or shown nonzero. In particular (17) does not separate
copies of the geometric holonomy or prevent cancellation among them.

The original compact source cycle of S is retained. Neither its
nonstationary boundary contributions, its nonunit/support-wall
strata, escaping decorations nor its centralizer relative current
is controlled by (16)--(17). No integral upper bound, geometric
intersection number, scalar lower bound or new volume-conjecture
filling case is inferred.

## Complete proof-source pins

* S: notes/research_soft_binomial_cut_stationary_source.md, SHA256
  667cb1eb70b770552de05e6f95f518016852b2c0aecdc874c3dff167fccb3d8b.
* Q: notes/quantum_longitude_and_regulator_action.md, SHA256
  e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7.
* C: notes/crossing_fundamental_cycle.md, SHA256
  0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f.
* G: notes/research_long_filled_group_representation_volume_gap.md, SHA256
  977d61c32e9610dc5e3bd1750b50614c88473f28683ca5dcea5f23a8a88becc0.

All four complete texts were read in the author sequence and their
used implications checked. The general nonfaithful chain comparison
already has the coverage described above; no novelty is claimed for
it. The binomial character adapter and its application to the new
principal critical scheme are explicit here. Only written mathematics
and text/hash operations were used; frozen and public files are unchanged.
