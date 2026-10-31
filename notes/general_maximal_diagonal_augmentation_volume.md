# Long-twist knot volume from a maximal diagonalization of any simple spherical quadrangulation

31 October 2026. Research theorem assembled from the original-source,
geometric, and analytic proofs cited below. The conclusion concerns actual Kashaev invariants
and actual filled hyperbolic volumes. The diagram is selected by a finite
classical maximization; it is not an arbitrary prescribed diagram.

## 1. Statement and quantifiers

Let \(\mathcal Q\) be any finite connected simple spherical
quadrangulation with \(R\geq2\) faces, each bounded by four distinct
vertices. Its edges will be called MAIN edges. Choose a diagonal in
every quadrilateral, retaining every embedded incidence, to obtain a
triangular cellulation \(\mathcal T\). There are \(2^R\) choices.
The chosen diagonals are matching edges: each pairs its two triangles.

Fix a MAIN edge \(uv\). Give each triangle total angle \(\pi\), each
vertex other than \(u,v\) total angle \(2\pi\), and the two marked
vertices angle zero. Write
\[
 \Phi(\mathcal T;u,v)
 =\frac1{2\pi}\max_{\theta}
       \sum_{t}\mathcal V(\theta_t),\qquad
 \mathcal V(\theta_1,\theta_2,\theta_3)
 =2\sum_{j=1}^3
   \left[\Lambda(\theta_j/2)+
         \Lambda((\pi-\theta_j)/2)\right],                 \tag{1}
\]
where \(\Lambda(x)=-\int_0^x\log|2\sin t|\,dt\).
The maximum is over these closed angle constraints; an empty fiber has
value \(-\infty\). Select any diagonalization \(\mathcal T_*\) attaining
the maximum of (1) over the finite set of choices.

**Theorem.** Every such \(\mathcal T_*\) is simple. It has an explicitly
constructed augmented link \(Y_{\mathcal T_*,\epsilon}\subset S^3\),
with \(R\) labeled crossing disks, whose complement is complete
hyperbolic and whose normalized volume is
\[
 \frac{\operatorname{Vol}(S^3\setminus
                  Y_{\mathcal T_*,\epsilon})}{2\pi}
      =\Phi(\mathcal T_*;u,v).                            \tag{2}
\]
Here \(\epsilon_e\in\{-1,0,1\}\) records the retained half twist at
each disk. There exists a choice of their parities for which the main
link has one component. Fix any such choice, with the signs and disk
framings recorded. Fill the crossing circles with integer coordinates
\(p_e\), so the actual crossing powers are
\(n_e=\epsilon_e-2p_e\), and call the resulting knot
\(K_{\mathcal T_*,\epsilon}(\mathbf p)\).

There is a finite threshold \(T(\mathcal T_*,\epsilon)\) such that for
**every fixed** integer vector \(\mathbf p\) with
\(\min_e|p_e|>T(\mathcal T_*,\epsilon)\), the knot complement is
hyperbolic and
\[
 \boxed{
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log\left|K_N\bigl(K_{\mathcal T_*,\epsilon}
                             (\mathbf p)\bigr)\right|
  =\operatorname{Vol}\!\left(S^3\setminus
       K_{\mathcal T_*,\epsilon}(\mathbf p)\right).}        \tag{3}
\]
\(K_N\) denotes the original, unknot-normalized Kashaev invariant in
the complete-color conventions of the source-normalization theorem.
The twists are independently signed and fixed before \(N\) tends to
infinity. Both parities and composite levels occur in the limit. There
is no restriction on ratios of twist magnitudes. The threshold may
depend on the whole chosen diagram.

Equivalently, choose a diagonalization with maximal actual polyhedron
volume among the simple choices. It is also maximal among all choices:
every nonsimple choice has strictly smaller capacity than some simple
choice. The maximum and the set of maximizing simple charts do not
depend on the MAIN edge used for (1).

## 2. Selection, geometry, and an actual knot source

The [maximal-diagonalization theorem](research_maximal_diagonalization_source_gap.md),
sections 4--5, supplies three conclusions used here:

1. Every \(\mathcal Q\) in the statement has a simple diagonalization.
2. Every nonsimple diagonalization has capacity strictly below some
   simple one. Thus every global maximizer is simple.
3. At each maximizing chart the original closed non-CROSS degree fiber
   has a uniform strict entropy gap below \(\Phi\).

These assertions include \(R=2\) and allow separating triangles. The
combinatorial simplification removes repeated diagonal edges by flips
across digons. The strict capacity comparison uses the final flip into
a simple sphere, where the angle optimizer is positive at every allowed
ordinary corner. It does not assume that a chosen initial chart already
has a hyperbolic realization.

For a simple \(\mathcal T_*\), sections 3--5 of the
[simple-sphere capacity and packing construction](actual_smoothed_source_capacity_blocks.md)
give the unique relative-interior angle optimizer, finite positive
ordinary curvatures, and the labeled convex ideal right-angled
polyhedron \(P_{\mathcal T_*}\). The normalization is exact:
\[
       \Phi=\operatorname{Vol}(P_{\mathcal T_*})/\pi.       \tag{4}
\]
This construction supplies the positive geometric certificate, rather
than making it an extra unverified hypothesis on \(\mathcal Q\).

The [general Morse source realization](research_matched_sphere_morse_source.md)
constructs an actual augmented link from this matched sphere. Its
physical strands use the specified pairing in every four-terminal
disk; they are not the abstract cycles of the cubic graph with its
matching removed. Cutting its projection sphere and crossing disks
gives precisely the two labeled balls whose boundary polyhedron is
\(P_{\mathcal T_*}\). The local shaded maps, including the recorded
half twists, are those of the
[original augmented-link cut and gluing](general_augmented_plat_matching_geometry.md),
sections 1--5. The two copies therefore give the complete hyperbolic
exterior and (2), with the actual disk-framed peripheral paths.

A spanning tree of the graph of untwisted physical main circles selects
odd boxes that merge them to one circle. This proves the existence of a
knot parity pattern. Any integer filling of that fixed parity retains
one main component. The
[positive marked filling argument](general_augmented_plat_long_filling_quantifiers.md)
applies to this actual augmented exterior: its local positive gluing
and primitive disk slopes give all sufficiently long independent signed
fillings. No constant number of heads in a horizontal slice is required
by that geometric argument.

The same general Morse source theorem supplies the exact original
quantum contraction, for every \(N\), in the form
\[
 S_N(\boldsymbol\delta)=
  \left[\prod_{f\ne u,v}L_f^{d}\right]
   \left.\prod_{e=1}^R H_{V_N(-2\cos(2\pi\delta_e))}
             (L_{x_e},L_{b_e},L_{c_e},L_{y_e})
   \right|_{L_u=L_v=0},\qquad d=N-1.                     \tag{5}
\]
It also gives the whole original Fourier/Hermite filling functional,
with its original \(\prod_e\sin(2\pi\delta_e)\), charge weights,
Gaussian \(\pi iN\sum_e n_e\delta_e^2\), and scalar
\(q^{d^2\sum_e n_e/4}(-i)^R\). Thus (5) is a polynomial of the
newly constructed link, not a polynomial transported from a different
diagonalization. Half twists enter this functional through \(n_e\)
once. They are not also inserted in the local \(V_N\) in (5).

## 3. The new non-CROSS gap controls the full numerator

Use the exact CROSS/LEFT/RIGHT decomposition of each original local
polynomial, at its actual parity-dependent cutoffs. Let
\(C_N^{\mathrm{raw}}\) be the all-CROSS coefficient, including its sign
\((-1)^{dR}\), and set
\(E_N=S_N-C_N^{\mathrm{raw}}\). The original normalized degree-flow fiber
has supply one at every port, demand one at every ordinary face, and
zero at \(u,v\). Its closed non-CROSS subset has at least one middle
load at least \(1/2\).

The [sharp Green maximum](research_sharp_green_spectral_maximum.md)
eliminates the real spectra in the local upper functional. On an
overloaded LEFT row \((a,b,c,d)\) with
\(\nu=a+b+d=1-c\leq1/2\), it is
\[
 \overline H=f(a)+f(b)+f(d)-f(\nu),\qquad
 f(t)=-\int_0^t\log\tan(\pi s)\,ds;                     \tag{6}
\]
RIGHT is reflected and CROSS has its complete triangle entropy. The
formulas agree continuously on the seams.

The exact load-preserving diagonal flip raises (6) by at least
\(f(\nu)\). Finite maximality, together with the separate pure-child
and seam arguments, therefore gives
\[
 \max_{\text{closed non-CROSS fiber}}
              \sum_e\overline H(q_e)\leq\Phi-\gamma
       \quad\text{for some }\gamma>0.                    \tag{7}
\]
If the fiber is empty its contribution is absent. Crucially, the flip
comparison in (7) is classical; it asserts no quantum identity between
different diagonals or links.

Apply the [uniform closed coefficient upper theorem](research_global_sharp_coefficient_limsup_majorant.md)
to the original coefficients of \(E_N\), after imposing their shared
face demands. There are only polynomially many incidence arrays for
fixed \(R\). The original finite cutoffs differ from the closed degree
domains by \(O(1/N)\); the proved closed continuity and uniform upper
bound include those boundary arrays, protected zeros, both parities,
and zero sampled factors. Equations (6)--(7) give, for all large \(N\),
\[
       \sup_{\boldsymbol\delta\in\mathbb T^R}|E_N|
                    \leq e^{N(\Phi-\gamma/2)}.            \tag{8}
\]

The remainder is itself a cosine polynomial of degree at most \(d\)
in each spectrum. Polynomial Bernstein bounds therefore give
\[
 |E_N(\mathbf x+i\mathbf y)|
 \leq\exp\{N(\Phi-\gamma/2)
                       +2\pi d\sum_e|y_e|\}.             \tag{9}
\]
Choose a fixed strip sufficiently thin that the last term is less than
\(N\gamma/4\). This gives a strict complex gap everywhere, including
all fixed derivatives on smaller strips. This is the full-numerator
restoration used here. It uses no flat-plat endpoint forest.

## 4. The CROSS packet and spectral gap on this general Morse source

Here the extensions of the older flat-plat notation must be checked;
the finite source construction alone does not give asymptotics.
Sections 1--3 of the
[original coefficient packet proof](general_full_spectral_numerator_geometric_packet.md)
use the following data: the exact coefficient (5) and its primitive
Cauchy measure; the local full-Hermite cofactor interpolation and
relative estimates; a positive simple-white packing with two adjacent
marked vertices; and connectivity of the remaining ordinary vertices.
All are present on the new source. A simple triangulated sphere remains
connected after deleting two vertices. Moreover the protected MAIN
edge cannot also be a matching edge, so no local outer pair consists
of both protected vertices. The allowed local zero specializations
are exactly those in the cofactor proofs.

The angular-complement proof is local on triangles and uses that
connectivity. The face saddle uses the positive finite-face Hessian
after fixing the common scale. Neither proof uses the order of cups,
caps and coupons in a horizontal sweep. Consequently the same
finite functions \(A_N,H_N\), constructed on this new coefficient,
give
\[
 C_N^{\mathrm{raw}}(\boldsymbol\delta)
 =\frac{(-1)^{dR}N^{2R}e^{NA_N(\boldsymbol\delta)}}
        {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
     (1+O(N^{-1}))                                       \tag{10}
\]
on a fixed complex neighborhood of zero. The determinant branch is
continued from the positive face Hessian. All finite anchoring factors
remain in \(A_N\); (10) does not define them by an unknown source value.
Its limiting action satisfies
\[
 A_0(0)=\Phi,\qquad
 A_0''(0)=-2\operatorname{diag}(C_e),\qquad C_e>0.         \tag{11}
\]
It is separately even and real on the real chart. The shared scale
quotient has its original dimension \(R-1\) and measure; no bridge
number occurs in that dimension.

Similarly the [global CROSS spectral-gap proof](actual_global_cross_spectral_gap.md)
uses the local cofactor transfer and prefix bounds, the same complete
radii, and the ordinary angular connectivity. It gives, for each
\(\eta>0\), a strict gap below \(\Phi\) on a fixed complex strip
over \(\max_e|\delta_e|_{\mathbb T}\geq\eta\).
The [general Morse action and packet audit](research_general_morse_cross_action.md)
records these dependency checks separately. In particular we do not
invoke section 4 of the older packet note, whose full restoration had
its own flat-layout hypotheses.

Equations (8)--(11) now restore (10) to the **full** source \(S_N\) on
a sufficiently small fixed complex chart: shrink the chart so its
critical real part stays above the absolute remainder bound. The
amplitude in (10) is a nonzero unit times explicit powers and finite
anchors, so that remainder is exponentially small relative to it.
Adding (9) to the CROSS gap gives the full-source strip gap away from
zero. These are precisely the relative-packet hypothesis H1 and the
global strip-gap hypothesis H2 of the whole-period theorem.

## 5. The entire original period and its filled-volume action

Apply the proof of the
[whole Fourier-period theorem](general_all_cross_long_filling_volume.md)
to \(S_N\). Beyond H1 and H2, it needs only the exact functional already
proved in section 2, separate evenness and period one, the polynomial
degree bound, and the original sine/Gaussian endpoint identities. The
full source has each property. The proof keeps the second-derivative
endpoint currents, bounds the infinite charge tail on whole intervals,
and localizes only finitely many charges. Thus no additional cycle
selection or cancellation assumption is introduced by this application.

For all sufficiently long independently signed fixed \(\mathbf n\),
the original unit-charge orbit has a nonzero leading coefficient at
both level parities. Its limiting phase is the stationary value of
\[
 A_0(\boldsymbol\delta)
       +\pi i\sum_e n_e\delta_e^2
       +2\pi i\sum_e\delta_e.                            \tag{12}
\]
The fixed geometric and analytic thresholds can be enlarged so the
\(O(\sum_e|n_e|^{-2})\) loss from \(\Phi\) is smaller than the fixed
complementary gaps. This is uniform over all sufficiently large minimum
twist magnitudes; the asymptotic error constants may depend on the
fixed vector. Nothing here interchanges the twist and level limits.

To identify (12), use the
[general Morse group/action extension](research_general_morse_cross_action.md)
of the [marked cofactor action](actual_cross_cofactor_marked_action.md).
At a horizontal slice with its actual variable region sequence
\(F_0,\ldots,F_{m(t)}\), the reflection prefixes telescope just as in
the constant-width notation. A cup or cap inserts or deletes an
inverse pair. The same local primitive collar and disk longitude
therefore give the actual link representation and peripheral marking.
The general face-winding computation in the source theorem leaves no
additional spectral-dependent turn term.

In the recorded convention put
\[
 A_\epsilon=A_0+\pi i\sum_e\epsilon_e\delta_e^2,
 \qquad V_e=-4\pi i\delta_e,
 \qquad \partial_{\delta_e}A_\epsilon=U_e.                \tag{13}
\]
The stationary equations of (12) are exactly the primitive smooth
filling equations \(U_e+p_eV_e=-2\pi i\). The complete value (4),
the actual geometric deformation, and the retained longitude boundary
correction in the marked-action proof imply
\[
 2\pi\operatorname{Re}\operatorname{crit}(12)
        =\operatorname{Vol}(S^3\setminus
                          K_{\mathcal T_*,\epsilon}(\mathbf p)).
                                                               \tag{14}
\]
It is the filled volume, not the complete augmented volume in (2).
Finally the [original source normalization](actual_complete_augmented_source_normalization.md)
changes the raw knot contraction only by its recorded unit-modulus
framing character. If the separately defined one-cut modified
convention is used instead, retain its factor \(i^{N+3}/N\); its
logarithmic rate is zero. This proves (3).

## 6. Relation to the prescribed k-bridge target

The result ranges over **every** simple spherical quadrangulation of
arbitrary size, then every maximizing diagonal choice and every fixed
knot parity pattern, with independently long signed twists at every
box. It is not a single twist family or a fixed list of examples. Its
selection condition is a finite classical optimization, with existence
proved above; no quantum gap remains as an extra hypothesis for this
selected class.

It does not prove the same result for each preassigned diagonalization.
Changing a diagonal can change the actual augmented link. Nor does the
general Morse construction preserve a preassigned plat width or prove
a particular minimal bridge number. The
[general prescribed-plat target](general_augmented_plat_long_twist_target.md)
therefore remains open beyond this and the previously certified
subclasses. For that target one still needs a source comparison on the
given diagram, or a topology-preserving way to reach a certified chart.
