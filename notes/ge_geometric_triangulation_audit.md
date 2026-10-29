# Ge's geometric existence argument: audit and usable conclusion

Audit dated 25 October 2026, explicitly requested by the user. Source:
Huabin Ge, [2609.27635v1](https://arxiv.org/abs/2609.27635v1),
Sections 2--4, PDF pages 4--11. Downloaded PDF: 20 pages; SHA-256
`247c0162c4755990b05557c6ca4d2bfc765a3fe9652b4f70f3288be8f5c97999`.

**Result:** the core argument checks out, conditional on the standard
Epstein--Penner decomposition input. No claim is made here about the
separate geodesic-boundary results or Section 6's additional applications.
Writing provenance is not used as mathematical evidence.

## 1. Critical deductions checked

For a polyhedron with v vertices and f polygonal faces, vertex heights
modulo affine functions have dimension v-4. An n-gonal paired face
imposes at most n-3 conditions. Euler's identity gives

    sum_i(v_i-4) - sum_pairs(n_alpha-3)
       = (1/2) sum_i(f_i-4).

This is positive if any cell is not tetrahedral. Modulo-affine
compatibility preserves face subdivisions. A nonzero height class
subdivides some cell, and the new cells retain paired faces and original
vertices. Refinement terminates: disjoint three-dimensional cells cannot
share four affinely independent vertices.

For Epstein--Penner cells, deck transformations give affine face maps in
Minkowski space. Four affinely independent vertices in a hyperplane
lambda=1 are linearly independent; radial projection therefore gives a
nonflat ideal tetrahedron. The resulting subdivision preserves the
complete metric. These are the dependencies needed for Theorem 1.1.

## 2. Independent exact stress test

[audit_ge_compatible_subdivision.py](../experiments/audit_ge_compatible_subdivision.py)
implements lower-face enumeration and reconstructs face identifications
after every refinement. It uses rational arithmetic throughout.

The test exhausts all 8^3=512 affine pairings of opposite cube faces,
including quarter turns and reflections. It does not assume that a
single generic compatible height produces tetrahedra.

Checks include:

* Constructing the quotient by affine heights independently for every cell.
* Recomputing the face-dependency matrix and its nullspace at each stage.
* Checking the dimension inequality, strict increase of cell count, and
  the finite combinatorial bound.
* Matching every induced face subdivision through the original affine map.
* Verifying that all terminal cells are nondegenerate tetrahedra using
  only the original eight vertices, with exact total volume one.

All 512 systems passed. There were 448 six-tetrahedron outputs and 64
five-tetrahedron outputs, with at most three refinement stages. The test
includes quotient systems that need not be manifolds; this is consistent
with the generality of the affine subdivision statement. The finite tests
support the audit but do not replace its uniform dimension and termination
argument. Results are in
[ge_compatible_subdivision_results.json](../experiments/ge_compatible_subdivision_results.json).

Reproduce with:

    python3 experiments/audit_ge_compatible_subdivision.py

## 3. What we may now use

Under the classical Epstein--Penner theorem, the audited argument supplies
a complete positive geometric ideal triangulation for every finite-volume
cusped hyperbolic manifold. For a hyperbolic knot, its complete holonomy
therefore has a representative

    beta = sum_j [z_j],     Im z_j > 0,
    D(beta) = Vol(M).

The existing regulator-line construction can use this positive
representative. Alternatingness is not needed for this geometric input.
This does not select a quantum state, and is not a volume-conjecture proof.

There is an additional distinction specific to the earlier AK calculations.
Ordering each tetrahedron positively chooses its geometric orientation.
A global branching instead requires compatible edge directions, hence
compatible vertex orders on every glued face. The former does not imply
the latter. Thus this audit does not automatically remove the branching
hypothesis from those tensor calculations.

For the principal torsor approach, geometric subdivision supplies a
positive representative of the intrinsic fundamental-class period. The
remaining target is to identify its quantization with the distinguished
Kashaev period and its literature quantum A-module, retaining normalization
and peripheral factors. The AK comparison remains a separate bridge.

The subsequent [triangulation bridge](triangulation_regulator_bridge.md)
spells out this role in the current affine A-period formulation. It
derives the local quantum central gluing relation and distinguishes
the geometric block from the rational period's V=1 source sector.
The positive triangulation supplies the marked Bloch lift; the
relative quantum source, actual cut-period comparison, and norm
identity remain work to prove.

The subsequent [pointed tetrahedron module theorem](pointed_tetrahedron_gluing.md)
now proves that the geometric root gluing reduction itself is
nonzero: for a knot its saturated boundary module has dimension N
at every level. Exact local shape-order changes make a global
branching unnecessary for that module construction. This does
not supply the full colored Verma tensor presentation or remove
the separate branching/cycle issues in the earlier analytic AK
calculation. The projected generator, actual relative source
comparison and regulator norm remain unproved.

The subsequent [integral half-longitude calculation](integral_half_longitude.md)
also identifies the saturated boundary lattice with the marked
meridian and half of the preferred longitude, integrally before
root specialization. Its quantum commutation rule matches the
actual squared-meridian operator at even and odd levels, with
the scalar longitude lift retained. Thus the geometric existence
theorem has a correctly marked boundary algebra available for
the proposed comparison. It still does not select or compare the
relative quantum source and period.

The subsequent [actual normal-period calculation](actual_geometric_normal_period.md)
uses the positive gluing germ to prove nondegeneracy transverse to
the actual two-dimensional framing torsor. It constructs a nonzero
formal normal block from the original crossing coefficients and
matches its connection to the regulator line by a formal unit.
This is precisely a place where the existence theorem enters the
quantum-A comparison. The actual affine-source extension, selected
relative period and all-level regulator norm still need comparison;
Sections 7--8 there give the source-compatible gauge identities.

The subsequent [Rivin flow formulation](rivin_flow_and_quantum_source.md)
also uses this positive complete point as the interior maximizer
of the full angle domain. Its regularized constrained flow has
an explicit boundary-controlling Bregman function and converges
to that point. An arbitrary ideal triangulation need not have
such an interior point; the geometric input is what supplies it.
The quantum source/cycle lift of this flow remains a separate
comparison, with its actual paired cap now explicitly calibrated.
