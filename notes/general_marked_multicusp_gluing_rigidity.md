# Positive marked gluing is unramified at every cusp simultaneously

30 October 2026. For an actual positive complete ideal triangulation with
c torus cusps, the marked decorated geometric germ is smooth of dimension
c. The small meridian similarity logarithms U_1,...,U_c are local
coordinates. More generally one may prescribe the logarithm of ANY one
nonzero primitive peripheral path on each cusp. In particular the mixed
coordinates consisting of main meridians and auxiliary longitudes are
unramified for an arbitrary marked augmented plat.

This is the multi-cusp geometric statement needed by a future comparison
with the full Casimir plat critical scheme. Its proof extends the repo's
own edge-lattice and polarized-Jacobian arguments; no external rigidity
proof is used. It supplies geometric rigidity, not that source comparison.

## 1. Hypotheses and provenance

Supply an actual marked positive complete ideal gluing certificate in the
sense of
[the general certificate theorem](general_marked_positive_gluing_certificate.md).
There are t positively oriented ideal tetrahedra, all faces are paired,
there are no finite vertices, and the c ideal vertex links are tori.
The quotient is the specified oriented manifold Y, with its actual
primitive peripheral paths. For an augmented plat those paths include
the original crossing-disk meridians and zero-self-linking longitudes,
with every retained half twist fixed in the topology.

Such a certificate is already constructed from each positive labeled
right-angled polyhedron certificate in
[the general matching-graph geometry](general_augmented_plat_matching_geometry.md).
The present theorem does NOT prove existence of a positive certificate
for every abstract matching graph or every hyperbolic augmented diagram.
Hyperbolicity alone should not be silently substituted for this input.

The ingredients previously proved in the repo are:

* The signed edge rows are isotropic and have rank E-V over Q:
  [pointed tetrahedron gluing](pointed_tetrahedron_gluing.md), sections 3--4.
  Its face-cancellation and vertex-sum proofs already cover arbitrary
  closed orientable vertex links, not just knots.
* The normal-curve intersection formula is a sum of local cusp-triangle
  identities: [integral half-longitude](integral_half_longitude.md),
  section 2. That proof is componentwise. Its later KNOT-specific
  divisibility assertion is unnecessary here and is not used.
* Positivity gives transversality to a full real isotropic system by
  polarization: [geometric rigidity](geometric_rigidity_and_cyclic_source.md),
  section 1. Its statement there was written for one cusp.

The missing assembly is the all-cusp rank argument, the exact mixed
peripheral coordinate statement, and the corresponding decorated
representation germ with its Artin-ring marking retained. Those are
proved below. No H2(Y)=0 shortcut is used.

## 2. The all-cusp marked Jacobian is invertible

Use quad coordinates

    u_j=Log z_j, v_j=Log z'_j=-Log(1-z_j),
    z'_j=1/(1-z_j),
    t_j=dv_j/du_j=z_j/(1-z_j).

These are the first two ordered quad parameters in this proof. Since
Im z_j>0,

    Im t_j=Im z_j/|1-z_j|^2>0.                         (1)

This convention differs from using Log z'' as the second coordinate;
that convention has negative imaginary derivative and proves the same
transversality. One must transform the equation rows with the quad order.

Let Omega be the direct sum of the standard alternating forms on the
(u_j,v_j) planes. Write E for the real span of the edge equation rows.
The torus-link Euler count gives E_global=t. The vertex-sum dependence
proof then gives

    dim E=t-c, Omega(E,E)=0.                           (2)

For completeness, a dependence among the edge rows requires the three
opposite-pair sums in every tetrahedron to be equal. Over R this is
exactly an assignment lambda_ab=s_a+s_b to its six edges. Three edge
values on a face determine its three s-values uniquely, so the s-values
descend to the c ideal vertices. The assignment from vertex values to
edge values is injective because the three zero sums on a triangle
force all its vertex values to vanish. Thus there are precisely c
edge-row dependences. Isotropy is the cancellation of the four signed
face forms under the actual orientation-reversing pairings.

A normal peripheral path gives a row in E^perp, well defined modulo E.
For two paths the pairing of these rows is, up to the fixed quad/cusp
orientation sign, TWICE their oriented intersection number. The local
normal-flow proof applies separately to every cusp, and paths on
different cusps have zero intersection. Therefore the 2c rows of
primitive peripheral bases are independent in E^perp/E. Its dimension
is exactly 2c by (2), so they form a real basis of that quotient.
Only this nondegeneracy is needed below; all actual holonomy signs are
retained in the marked path equations themselves.

Choose one nonzero primitive path gamma_i on each cusp. Its class is
nonzero in that cusp's two-dimensional summand, and different chosen
classes pair to zero. Thus E together with these c rows has rank t and
is isotropic. Choose t-c independent edge equations and append the c
actual gamma equations. Their real coefficient matrix is (A B), with

    rank(A B)=t, A B^t=B A^t.                          (3)

The logarithmic shape Jacobian is

    J=A+B diag(t_j).                                  (4)

It is invertible. If Jx=0 then w=(x,diag(t_j)x) lies in the complexified
kernel of (A B). The kernel of a full-rank isotropic t-row system is
itself real Lagrangian, so Omega(w,conjugate(w))=0. But directly

    (i/2) Omega(w,conjugate(w))
                            =sum_j Im(t_j)|x_j|^2,

which is strictly positive for x!=0 by (1). Hence x=0.

All edge equations are affine logarithmic equations on this chart.
Their dependent rows have compatible constants because the complete
point satisfies them. Solving the selected t-c rows therefore solves
all edge equations near that point. The holomorphic implicit-function
theorem applied to (4) proves that the edge-gluing germ is smooth of
dimension c and that the c prescribed peripheral logarithms are local
coordinates. Exponentiating changes the Jacobian only by nonzero
monomial factors. Thus the same algebraic germ is etale over its marked
peripheral multipliers.

## 3. This is the actual decorated representation germ, also infinitesimally

The geometric object includes a common fixed flag for each peripheral
group. Keep its eigenvalue/similarity character, not merely the trace
of an unmarked peripheral matrix. Normalize an ordered triple of
developed ideal vertices. At the complete positive point all required
tetrahedral vertex differences and face-triple determinants are nonzero.
They remain units in a sufficiently small local chart and over every
local Artin algebra with this residue point.

Starting with shape coordinates, develop the first ordered tetrahedron.
Across each face, its ordered triple determines a UNIQUE projective
transformation and hence the next tetrahedron. Around a global edge the
resulting transformation fixes its two distinct ideal endpoints. Its
similarity multiplier is the actual edge shape product. The edge equation
sets that multiplier to one, so this transformation is projectively the
identity. The face generators and these edge relations are the actual
dual two-skeleton presentation of the ideal triangulation. They therefore
construct a representation of pi1(Y). Each developed cusp vertex is fixed
by its actual peripheral subgroup, and its marked similarities have
precisely the path monomials used in section 2.

Conversely, a nearby representation with those peripheral flags develops
every ideal vertex equivariantly from its cusp flag. Cross-ratios of the
four vertices give the shape coordinates. The face transformations
coincide on three distinct flags, and the edge products telescope to one.
Normalizing the same ordered triple makes these constructions inverse.
Every step uses rational expressions with UNIT denominators. The two
constructions therefore remain inverse over local Artin algebras, not
only on complex points. This identifies the positive gluing germ with
the actual decorated representation germ modulo simultaneous PGL2
conjugation. A specified SL2 lift and its central signs are retained on
their local sign cover; they are not reset by the projective construction.

There is an important infinitesimal distinction. For a fixed unipotent
matrix M=[[1,1],[0,1]], a projectively invariant flag (1,e), with e^2=0,
can move: M(1,e)=(1+e)(1,e) modulo e^2. Its eigenvalue changes. Thus an
UNSPECIFIED invariant flag is not the same Artin datum as an eigenflag
with exact eigenvalue one. If the eigenvalue is prescribed to be one,
the first coordinate forces e=0. More generally a noncentral parabolic
matrix with a unit off-diagonal entry has a rank-one nilpotent part,
and its kernel is its unique free eigenline with the exact repeated
eigenvalue. The log equations in section 2 retain this character and
remove that ambiguity when the corresponding log is fixed.

It follows in particular that the marked decorated geometric germ has
no nonzero infinitesimal deformation at fixed values of ALL the chosen
peripheral coordinates. This is a statement about this actual germ;
it does not identify a different source gradient scheme with it.

## 4. The marked cusp derivative is exactly diagonal

Now choose the actual meridians as the c coordinate paths, and denote
their small PROJECTIVE similarity logs by U_i. Let V_i be the small
log of the actual preferred longitude similarity. Send the selected
peripheral flag to infinity using a bounded holomorphic frame. Write

    mu_i(z)=exp(U_i)z+m_i(U),
    lambda_i(z)=exp(V_i)z+l_i(U).

At completeness m_i(0),l_i(0) are the two actual primitive translations;
m_i(0)!=0 and

    tau_i=l_i(0)/m_i(0), Im tau_i>0                     (5)

for the positive oriented basis. Peripheral commutativity gives EXACTLY

    (exp(U_i)-1) l_i(U)=(exp(V_i)-1) m_i(U).           (6)

Since m_i remains a unit, U_i=0 implies V_i=0 on the centered log branch.
Consequently V_i is analytically divisible by U_i. Differentiating (6)
at completeness yields

    dV_i=tau_i dU_i,
    partial V_i/partial U_j=delta_ij tau_i.             (7)

This proves the zero cross-cusp first derivatives without an assumed
potential, symmetry of a Hessian, or a source convention. It also proves
that fixing a main meridian multiplier to one keeps that entire main
peripheral group parabolic nearby, with its longitude multiplier one.
The translation pair remains real-linearly independent near the complete
point, so these main cusp ends remain complete.

The logs here are PROJECTIVE similarity logs. Chosen SL2 eigenvalue logs
are U_i/2,V_i/2 with their original central signs retained. Their ratio
in (7) is still tau_i; no factor of two is introduced by changing both.

## 5. Relative rigidity for arbitrary marked augmented links

Partition the cusps into s main cusps and r auxiliary crossing circles,
with c=s+r. Impose the exact main conditions

    U_main=0.

The resulting decorated geometric germ is smooth of dimension r, with
U_aux as coordinates. Equation (6) gives V_main=0 identically. Equation
(7), or directly the choice gamma=mu on main cusps and gamma=lambda on
auxiliary cusps in section 2, shows that V_aux is ALSO a local coordinate
system. Thus the mixed marked projection

    (U_main,V_aux)

is unramified at the complete point. In particular the germ with all
these values fixed has no nonzero infinitesimal deformation modulo
simultaneous conjugation. This is the precise geometric rigidity needed
for channels recording selected auxiliary longitude eigenvalues.

Every retained half-twist partner is treated with its own ACTUAL
triangulated topology and primitive collar paths. The theorem does not
replace a half twist by a fractional integral change of peripheral basis
on the old link. When a right-angled matching-graph certificate is used,
its explicit primitive cusp translations provide the tau_i in (5), with
their separately calibrated source signs. No framing is deduced from a
source Hessian.

For the full Casimir plat phase, a further theorem must identify its
linearized or Artin-ring critical equations with this decorated germ,
including incidence multipliers, scale quotients and the actual marked
cap. The local character map and this geometric rigidity are inputs to
that theorem. They do not yet prove its magnetic Hessian radical or a
nonzero original-source amplitude. Physical-cycle selection and global
coherent estimates remain separate even after such an identification.

Audit: [actual three-cusp marked gluing](../experiments/audit_general_marked_multicusp_gluing_rigidity.py),
[results](../experiments/general_marked_multicusp_gluing_rigidity_results.json).
It constructs cusp normal curves on an actual doubled-octahedron quotient,
checks edge rank 5 and marked rank 8 for all eight meridian/longitude
choices, and computes the exact diagonal peripheral derivative. The test
curves are explicitly chosen primitive bases of that fixture; they are
not substituted for the original crossing-disk marking of another link.

The gluing theorem does not supply a source critical-scheme comparison or automatic existence of a positive triangulation.

The positive geometric certificate remains a hypothesis of the multicusp theorem.