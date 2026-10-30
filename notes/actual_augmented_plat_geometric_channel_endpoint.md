# The complete geometric disk character is a folded-channel endpoint

30 October 2026. There is a useful general restriction on the branch
that the arbitrary-plat source must select. At every complete essential
crossing-circle cusp, the ordered product of its two main puncture
meridians has trace -2 in the common-trace lift. The classical symbol
of the original pair Casimir is exactly this ordered trace. Hence the
complete geometric character lies at the ENDPOINT of the folded real
Casimir channels, not at a generic interior channel value.

This is a geometric character and source-symbol statement. It does
not prove that the quantum sum concentrates at that endpoint, that
other channels have a gap, or that the complete geometric period has
nonzero original coefficient. Those remain analytic tasks.

## 1. The actual crossing disk and its parabolic product

Take an augmented plat with the labeled complete geometric certificate
of [the matching-graph construction](general_augmented_plat_matching_geometry.md).
Choose one actual twice-punctured crossing disk. Let A and B be its
two puncture meridians, transported to a common basepoint in their
original order, and put P=BA. The disk's boundary is the peripheral
longitude of the crossing circle, up to the recorded orientation
and central lift. In particular the auxiliary meridian C commutes
with P. Both peripheral generators have nontrivial parabolic complete
holonomy: their translation periods generate the actual cusp lattice.

The two main puncture flags are distinct. Indeed one cut half disk
is the nondegenerate shaded ideal triangle (O,C1,C2), with its two
main punctures at C1 and C2. Restoring its disk pairing retains these
distinct developed flags for the two based meridians. Consequently
A and B are nontrivial parabolics with distinct fixed points.

Use the same trace lift for both meridians, as in the original
common-color source; its complete head trace is -2. A central sign
change of both heads does not change Tr(BA). A nontrivial parabolic
C is conjugate in PSL2 to z -> z+1. A determinant-one matrix
that commutes projectively with C commutes with its trace-two lift:
the alternative sign would change the nonzero trace of that lift.
A determinant-one matrix
commuting with its trace-two lift has the form

    P=[[a,b],[0,a]], a^2=1.

Thus Tr P is either 2 or -2. To choose the sign, conjugate the two
distinct main flags to infinity and zero. Their common negative
trace lifts then have the form

    A=-[[1,s],[0,1]], B=-[[1,0],[t,1]], s t !=0,
    Tr(BA)=2+s t.                                         (1)

Trace 2 would force st=0, contrary to the distinct nontrivial flags.
Therefore

    Tr P=-2,  s t=-4.                                     (2)

This argument uses the actual complete cusp and the nondegenerate
disk triangle. An arbitrary pair of parabolics, or an unmarked
solution of a polynomial relation, would not supply those inputs.
Half twists transport the pair by its original Hurwitz map, which
preserves the ordered product up to conjugacy. Thus (2) is unchanged
by the retained signed half-twist pattern.

## 2. The original quantum character fixes the relevant trace coordinate

The [actual adjacent-character identities](actual_adjacent_twist_character_and_source.md)
give, in the original ordered quantum flag algebra,

    Omega_(12)=tr_q(H_2 H_1).                              (3)

Their principal q=1 symbol is the ordinary ordered trace Tr(BA).
The heads are the actual prefix-based meridians, and the cap/Hurwitz
presentation identifies their classical tuples with the marked plat
representation scheme. Thus (2) imposes c=-2 on this geometric
classical pair character. It is not a relabeling of a Newton output
coordinate as a knot meridian.

The complete-circle source compiler uses the ORIGINAL folded nodes

    c_j=2cos((2j+1)pi/N), 0<=j<=floor((N-1)/2).

Set delta_j=N-1-2j. Then exactly

    c_j=-2cos(pi delta_j/N),
    c_j+2=4sin^2(pi delta_j/(2N)).                         (4)

For any sequence of these real nodes, c_j -> -2 if and only if
j/N -> 1/2. If delta_j=o(N), the exact relation further gives

    c_j+2=(pi delta_j/N)^2[1+O((delta_j/N)^2)].            (5)

At odd N the last node has delta_j=0 and is the simple endpoint.
At even N the last folded node has delta_j=1 and belongs to the
paired repeated-root sector. Their original source weights and
normal terms therefore cannot be replaced by one parity-blind
endpoint evaluation.

Equations (3)--(5) locate the complete GEOMETRIC character within the
compiler's classical channel coordinates. They do not assert that
the other physical wire variables are at endpoints, nor that a
stationary phase analysis of the complete coherent sum is finished.
Complex contour sectors also require their actual source coefficients.

## 3. The marked peripheral cover resolves the trace ramification

Continue the actual preferred crossing-circle longitude from
completeness, with centered projective logarithm V. Keep its selected
square root ell=exp(V/2), so L=ell^2 is the projective multiplier.
In the common head lift the eigenvalues of P are -ell and -ell^-1,
up to the recorded inversion of the preferred longitude. Consequently

    c=Tr P=-(ell+ell^-1)=-2cosh(V/2),
    c+2=-(ell-1)^2/ell=-V^2/4+O(V^4).                    (6)

The square-root cover ell^2=L is etale on the peripheral torus.
The subsequent trace map ell -> -(ell+ell^-1) is ramified at ell=1:
it forgets the sign of V and its first-order deformation there.
These are different maps. A marked longitude branch carries more
first-order information than its trace equation at c=-2.

For the real root nodes in (4), one compatible local logarithmic lift
is V=2pi i delta_j/N; the reciprocal sheet changes its sign. This
matches (6) exactly. It is a coordinate comparison, not an assertion
that this logarithm is the quantum source's selected filling cycle.

The conclusion for the general plat program is concrete: analyze the
complete geometric endpoint on its marked peripheral cover, retaining
both level parities and the original repeated-root source. A strict
interior real saddle in the raw folded channel coordinate cannot
represent (2). The required global source selection is still open.

Audit: [trace, ramification and both-parity endpoint identities](../experiments/audit_actual_augmented_plat_geometric_channel_endpoint.py).
The all-plat statement follows from the labeled disk/cusp argument
and the already proved original quantum character identity, not from
the finite-level examples in the audit.

Two independent analytical reviews and fresh audit replays: PASS.
They checked the actual based disk flags, the peripheral commutation
and common-trace sign, the original ordered Casimir symbol, both
level parities, and the distinction between the etale square-root
cover and the ramified trace map. All 17 endpoint parity checks
passed. These checks establish no quantum concentration or gap.
