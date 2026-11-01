# From the marked tensor contraction to the face coefficient

This reading concerns the finite source identity used in Appendix O.
It checks the passage from the stated local matrices to the global face
coefficient. It does not rederive every entry of the original crossing
matrix, its comparison with Kashaev's definition, or the local Casimir
polynomial. Those are named inputs, not consequences of a coefficient
selection argument.

The inputs read were [the general Morse construction](../../notes/research_matched_sphere_morse_source.md),
[transport of the marked edge](../../notes/research_arbitrary_main_edge_mark_transport.md),
the first four sections of [the homogeneous local polynomial](../../notes/actual_homogeneous_casimir_face_source.md),
and the first three sections of [the normalization calculation](../../notes/actual_complete_augmented_source_normalization.md).
The companion [finite source and filling record](finite-source-and-filling-followup.md)
records the separate checks of the local functional, analytic estimates
and geometric completion.

## The source and its scalar

Write \(R\) for the number of crossing boxes, \(N\) for the root level,
and \(d=N-1\). Contracting each matched pair of triangles gives a
connected four-valent spherical graph with \(R\) vertices, \(2R\)
edges and \(R+2\) faces. Fixing the exterior face potential leaves
\(R+1\) independent face grids. This is the integral cycle lattice
of the graph: face boundaries generate it with their one total-sum
relation. Introducing Morse maxima and minima only subdivides its
edges and does not change this lattice.

The local polynomial \(H_e\) has nonnegative exponents and degree
\(d\). Its matrix adapter is \(N^{-1}H_e/(bc)^{d/2}\), with \(b,c\)
the two middle faces in the fixed local order. The physical endpoint
zeros must be imposed before any modular reduction of head indices.
Otherwise a modular conserved state could have the wrong integer
total. The local adapter proof explicitly retains these zeros.

The four turns have the displayed cup and cap coefficients in their
actual head order. Whole-source conservation first forces the two
heads at the marked cap to sum to \(d\); only then may its ratio to
the ordinary cap be used. If \(u\) is exterior and \(v\) is the
other protected face, that ratio is \(N^{-1}(L_v/L_u)^d\).
The face-boundary turning count is

\[
 M_f-T_f=2\quad(f\ne u),\qquad M_u-T_u=-2,
\]

where \(M_f\) counts middle passages and \(T_f\) counts outside
minus inside turns. Substitution cancels every half power and gives
the full summand

\[
 N^{-R-1}\frac{\prod_eH_e(L)}{\prod_{f\ne u,v}L_f^d}.
\]

Thus the grid count cancels the displayed scalar exactly. No factor
of \(N\) is discarded as a purportedly harmless normalization.

## Why the grid selects one coefficient

Put \(P=\prod_eH_e\). For odd levels the free grids are ordinary
\(N\)-th roots of unity. At even levels they are their specified
cosets. The parity cochain has value one on the strand edges and
zero on the matching edges. Every triangle has two strand edges,
so this cochain is closed; on the sphere it integrates to face
parities. Coherent face lifts therefore give exactly the cosets in
the original matrix calculation.

Every ordinary exponent surviving the grid average is congruent to
\(d\) modulo \(N\) and is therefore at least \(d\). There are \(R\)
such exponents, whereas the total degree of \(P\) is \(Rd\).
They exhaust the degree: all ordinary exponents equal \(d\), and
both protected exponents vanish. The coset multiplier is then one.
This also explains why fixing \(L_u=1\), rather than averaging that
variable, cannot admit another monomial.

Appendix O now states and proves this finite selection proposition for
arbitrary complex coefficients and arbitrary nonzero grid shifts.
The six declarations in [FaceGridSupport.lean](../../formal/VolumeLogic/FaceGridSupport.lean)
formalize the exponent argument. They do not construct the physical
grid or verify the local crossing adapter.

## Moving the mark and keeping the normalization

The generic lift used to move the mark has pivot
\(\widetilde g=(-1)^H K\), which implements the same squared
antipode as \(K\) and specializes literally to \(K^{1-N}\).
Its traces agree on every tensor-generated endomorphism: at positive
real generic \(q\), decomposition into highest-weight summands gives
the same trace on each summand, and rational continuation gives the
identity in the regular generic matrices. The argument specializes
these matrices, not potentially singular decomposition projectors.
The scalar of a cut complete-color strand is compared generically
and then specialized; there is no division by a zero root quantum
dimension.

This proves equality of the full marked readings under the stated
matrix inputs. It does not transport individual central or
noncentral sectors, nor their absolute-value estimates.

The balanced basis changes cancel on internal wires by exact tensor
covariance. Their condition numbers are not external normalization
factors. At the complete meridian, the recorded framing correction
has modulus one; the separate one-cut modified normalization has
the exact factor \(i^{N+3}/N\). The latter has zero exponential rate.
Neither assertion supplies a bound for a moving peripheral germ.

## Boundary of this check

No additional correction was identified in these adapter steps. The
new written grid proposition and finite formal proof expose a step
that was previously compressed into the degree count. The following
remain separate inputs: the actual local Casimir relation and
crossing jets, the comparison with the specified knot invariant,
the uniform analytic remainder bounds, and the primitive completed
hyperbolic metric. This record cannot be used to replace any of them.
