# The literal reflected two-circle source and its two-octahedron geometry

> **Draft topology certificate.** This note had not completed its independent topology audit at snapshot time. Its referenced audit script is not included. It is not an established extension of the proved family indexed by the README.

29 October 2026. The positive original circuit
\[
 E_N=\phi\!\left(\mathscr R(RL_N)\,R^{-1}L_N\right)
       =\|\,\mathscr R(R^{-1}L_N)\,\|_{\rm Newt}^{\,2}       \tag{1}
\]
has a genuine four-component hyperbolic interpretation. The labeled
cut-and-reglue certificate below gives two regular ideal octahedra,
volume \(2v_8\). This is a complete-base calibration, not yet a new
broad family of filled knots. The topology certificate should be
reviewed independently; software recognition is not its proof.

## 1. Exact source diagram and cut-open port table

Let \(C\) be the actual auxiliary three-braid \([2,1,1,2]\), with
its THIRD top and bottom endpoints joined outside on the right.
Its first two top/bottom endpoints stay open. The original pivotal
color-\(N\) evaluation of this circle is precisely \(L_N\), with no
extra trace normalization. Use the literal single crossings \(X_\pm\).
The diagram is the denominator closure of
\[
       \mathscr R(X_+C)\,(X_-C).                         \tag{2}
\]
Thus it is fixed before evaluating any invariant.

Its two auxiliary circles are distinct. Deleting them leaves the
genuine diagram \(\mathscr R(X_+)X_-=X_-^2\), whose braid closure has
two components. There are therefore FOUR components in (2).
In the audit's crossing convention its unmodified planar code is

    [(1,10,2,11),(2,19,3,16),(15,19,10,18),(17,15,18,14),
     (16,3,17,4),(11,4,12,5),(5,8,0,9),(12,7,13,8),
     (6,13,7,14),(9,0,6,1)].

The retained half crossings are 0 and 5; the auxiliary loops run
through crossings 1--4 and 6--9. A simultaneous mirror convention
does not change the absolute invariant or volume conclusion.

Cut along the projection sphere and the two twice-punctured crossing
disks. Keep each half twist as its actual regluing. This produces
two balls \(P_+,P_-\). A crossing-disk cut replaces its local
circle gadget by two shaded triangles with a common circle vertex.
This is reversed by restoring the disk collar and the third-strand
closure defining \(C\).

Label the four main arc segments between the disks cyclically by
\(p_0=Y_+,p_1=Z_+,p_2=Y_-,p_3=Z_-\). The unturned disk sides see
\((p_0,p_1)\), \((p_2,p_3)\). The GENUINE quarter-turn shifts the
second disk's cyclic port order by one, giving
\((p_3,p_0)\), \((p_1,p_2)\). With circle vertices \(X_0,X_1\),
the shaded triangles in either cut ball are consequently

| Face | Vertices |
| --- | --- |
| \(A\) | \(X_0,Y_+,Z_+\) |
| \(B\) | \(X_0,Y_-,Z_-\) |
| \(C\) | \(X_1,Y_+,Z_-\) |
| \(D\) | \(X_1,Y_-,Z_+\) |

Their edges form the octahedral graph, with opposite pairs
\(\{X_0,X_1\},\{Y_+,Y_-\},\{Z_+,Z_-\}\). The four white
complementary regions are
\[
 W_0=(X_0,Y_+,Z_-),\ W_1=(X_0,Y_-,Z_+),\
 W_2=(X_1,Y_+,Z_+),\ W_3=(X_1,Y_-,Z_-).
\]
Without the port shift the disk-side pairs would repeat; it would
be incorrect to replace this actual turn by scalar multiplication.

White gluing is \(W_j^+\to W_j^-\), with identity vertex map.
The odd half twists exchange the upper/lower disk sides, giving

| Source | Target | Vertex map |
| --- | --- | --- |
| \(A^+\) | \(B^-\) | \(X_0\to X_0,\ Y_+\to Y_-,\ Z_+\to Z_-\) |
| \(A^-\) | \(B^+\) | same rule |
| \(C^+\) | \(D^-\) | \(X_1\to X_1,\ Y_+\to Y_-,\ Z_-\to Z_+\) |
| \(C^-\) | \(D^+\) | same rule |

This follows by tracing the two punctures through the single crossing,
not by matching a computed volume. Restoring the white sphere and
these disk collars reverses the cut and gives (2).
The sign of the half twist retains its source disk-framing convention.
Adding a full disk twist changes its preferred filling meridian but
not this unmarked exterior quotient. No new filling-peripheral
identification is inferred from this complete-base certificate.

## 2. Exact positive metric, edge cycles, and four complete cusp tori

Realize each cell as a regular ideal octahedron, for example
\[
 X_0=0,\quad X_1=\infty,\quad
 Y_\pm=\pm1,\quad Z_\pm=\pm i .
\]
Use opposite labeled orientations on the two copies. Every displayed
triangle map is realized by an octahedral symmetry followed by the
appropriate face reflection. In the hyperboloid model take center
\(O=(1,0,0,0)\) and normalized ideal lifts
\((1,\pm e_1),(1,\pm e_2),(1,\pm e_3)\).
An octahedral symmetry fixes \(O\) and maps these lifts EXACTLY;
reflection in a target face fixes its three lifts. Thus all face
maps preserve the canonical horospheres, not just ideal endpoints.

The finite combinatorial checks from this table are:

* The 24 octahedral boundary-edge occurrences form six cycles of
  length four. Their dihedral angles sum to \(4(\pi/2)=2\pi\).
  Matched endpoint horospheres exclude a dilation along an edge.
* The ideal vertex classes are
  \(X_0^\pm\), \(X_1^\pm\), all \(Y_\pm^\pm\), and all \(Z_\pm^\pm\).
  They give the four actual components.
* Their links have respectively \(2,2,4,4\) Euclidean squares.
  Every link edge is paired twice and every link vertex has four
  right-angle sectors. Each link is connected and orientable, with
  Euler characteristic zero, hence a nonsingular torus.

Shrinking compatible horospheres first gives disjoint actual corner
sections and full horoball ends. The remaining core is compact.
The resulting positive curvature-minus-one metric is complete and
finite-volume on the actual complement of (2).

An explicit eight-tetrahedron version makes the check reproducible.
Put \(v=(Y_+,Z_+,Y_-,Z_-)\). The tetrahedra in \(P_+\) are
\((X_1,X_0,v_j,v_{j+1})\), \(j\bmod4\); reverse the last two labels
in \(P_-\). Their shapes are \(i\) in the respective reflected
frames. Internal and external face maps have local permutation
\(0132\). The audit builds these maps from the table, checks all
face pairs and exact rational edge-angle sums, and checks the links.
Thus the volume is \(8D(i)=2v_8\). This link is genuinely hyperbolic,
not merely a JSJ/composite explanation of the observed exponent.

## 3. The original quantum limit and what generalizes

Section 6 of [the Newton-turn theorem](actual_newton_turn_positive_gram.md)
proves the whole-source identity (1) and
\(\lim N^{-1}\log E_N=v_8/\pi\), using the actual finite coefficients,
all-index endpoint bound, and a nonzero high-index lower term.
Both level parities and all composite levels are included.
The original single-cut reduced normalization changes (1) only by
its recorded unit phase; the optional one-cut modified convention
adds \(1/N\), not one factor per component. Therefore
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|\langle L_{\rm ref}\rangle_N|
           =2v_8=\operatorname{Vol}(S^3\setminus L_{\rm ref}). \tag{3}
\]
Here \(L_{\rm ref}\) is the explicit diagram (2), not a census name.

There is an exact reusable non-scalar tangle gluing:
\[
 \phi(f^\sharp\mathscr Rg)
       =\sum_{r=0}^d\overline{\alpha_r(f)}\alpha_r(g).    \tag{4}
\]
It preserves all physical source ports and gives positive entire
reflected circuits. But its quantum separating cut is not
automatically the projection/disk cut of the geometric octahedra.
A general tangle double need not have a verified geodesic separating
surface, and its \(N\)-channel overlap is not a scalar product of
independent local invariants. Two known packet norms alone do not
control the sharp coherent overlap or its geometric critical point.

In a genuinely branched construction with three paired boundary slots,
the original vertex is a SIX-port tensor. Its saturated source has
dimension \((N^3+N)/2\) and the explicit divided-power kernel of
[the six-port source theorem](actual_six_port_divided_power_source_kernel.md).
It cannot be replaced by independent two-port scalar Frobenius
multiplication vertices. The bounded confluent construction controls
its finite normal order, but not its coherent geometric energy.
Thus the present exact base and gluing metric are useful analytic
inputs; they do not prove closure under arbitrary octahedral graphs
or an arbitrary-bridge volume conjecture.

Audit: [actual tangle and exact octahedral face/edge/cusp certificate](../experiments/audit_actual_reflected_two_circle_octahedral_base.py).
Software census names and numerical volumes, when requested in the
audit, are diagnostics only; the written proof is the reversible
disk/projection cut and the exact metric checks above.
