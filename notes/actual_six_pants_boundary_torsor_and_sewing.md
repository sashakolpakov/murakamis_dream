# The actual six-pants boundary: topology, a pointed finite frame and sewing

29 October 2026. The four-octahedron geometric block has six pants
boundaries, but its actual quantum boundary cannot be replaced by six
independent complete-color trivalent states or by the positive closed
theta scalar. This note gives three concrete results toward the open
kernel: the boundary incidence and genus of every connected NC Morse
graph; an explicit nondegenerate marked Frobenius frame on every
surviving joint source cell, with at most eight coordinates; and an
exact original-source counterexample to independent three-axis marked
pairings. The remaining geometric-cut identification and conditioning
questions are stated separately.

## 1. The boundary slopes and actual incidence

At a retained crossing disk, its three-punctured-sphere boundary has
the slopes

    (belt longitude, first main meridian, second main meridian). (1)

The first boundary circle follows the crossing disk boundary, while
the two others are the small circles cut from that disk around its
intersections with the physical main strands. Thus (1) is a literal
topological path statement. These are not three meridian-polarized
color-N punctures. The original mixed circle realizes precisely the
longitude-polarized operator L_l(Omega), as proved with all physical
ports retained in the
[circle source theorem](actual_crossing_circle_source_and_filling.md).

There is a sharp parity check on the distinction. At even N the
unrolled H weights of V_N^tensor3 are odd, so its integer-H invariant
space is zero. Nevertheless the actual even marked theta source is
nonzero for N>=4. Assigning Inv(V_N^tensor3) independently to each
geometric pants would therefore lose the original source. This does
not disprove a boundary theory in the correct polarization.

Let Gamma be a CONNECTED graph in the actual ordered NC Morse class:
2b trivalent vertices, b black and b white, and E=3b edge slots. Use
its literal noncrossing cup and cap matchings, with a retained circle
on every edge slot. Cut the projection sphere and all crossing disks,
and then glue ONLY the white projection faces. Before the final
shaded pairings there are 2E boundary pants, naturally indexed by
the halfedges (v,e) of Gamma.

The exact adjacency of their rank-one cusp annuli is as follows.

* Each graph edge e joins the two pants (v,e),(w,e) by the annulus
  at its retained crossing-circle cusp.
* At a graph vertex v, the three original cup or cap arcs join its
  three incident pants pairwise, giving a triangle of three main-arc
  cusp annuli.

Hence this adjacency graph is the Fisher expansion T(Gamma): replace
each trivalent vertex by a triangle and retain the original matching
edges between those triangles. It is connected, cubic, with

    number of pants=2E, number of annuli=3E,
    genus of the connected truncated boundary=E+1=3b+1. (2)

For a direct proof of the genus, the pants contribute Euler
characteristic -2E, and the annuli zero. Their specified connected
gluing is an oriented closed boundary surface, so 2-2g=-2E.
The same count follows from the projection cut: its connected
bowtie skeleton has 3E ideal vertices, 6E edges and 2E shaded faces,
hence E+2 white faces. Gluing the two projection balls along those
white disks is a handlebody with E+1 handles. This is also a direct
topological construction of the boundary surface in (2). Reducible
diagram faces can be read as boundary walks after taking a regular
neighborhood; no convex geometric realization is asserted for an
arbitrary such graph.

For the theta graph, T(Gamma) is the triangular prism and g=4.
This is precisely the six-pants geometric block in
[the actual theta angle certificate](actual_marked_theta_link_and_angle_geometry.md).
For b>1 the true open white-glued object has one connected boundary
of genus 3b+1. It is not b independent copies of that genus-four
block. To obtain T(Gamma), the cusp annuli between vertex triples
must be rewired according to the original Gamma. Gluing geodesic
pants in an arbitrary collection of blocks is a valid geometric
operation, but it does not by itself implement this original annulus
and white-face wiring. That topological identification requires its
own explicit cut certificate.

## 2. A canonical finite actual marked frame on every regular cell

Use the saturated six-head source S_N, its three disjoint pair
Casimirs A_1,A_2,A_3, and the actual nested cup v=p_16 p_23 p_45.
For a folded triple j=(a,b,c) let E_j be the FULL regular joint
cluster projector, not a value-only projector. Restrict now to
a+b+c>=d=N-1. The
[proved regular-cube theorem](actual_trivalent_all_channel_positive_scalar_and_regular_cubes.md)
gives the actual source cell

    S_j=R_r v_j, v_j=E_j v,
    R_r=C[eta_1,...,eta_r]/(eta_1^2,...,eta_r^2),
    dim S_j=2^r<=8.                                 (3)

There is one eta_i for each PAIRED axis, and it is chosen as the
ACTUAL complete-circle sector on that axis. On an odd simple axis
the corresponding circle is the scalar N. Thus eta_i is the full
first-normal nilpotent, with its original coefficient, rather than
an arbitrarily normalized formal coordinate.

Let lambda be the original unrestricted physical marked co-source,
including the two other ordinary caps. Define actual boundary
moments by

    m_I=lambda(eta_I v_j), eta_I=product_(i in I)eta_i,
    tau_j=m_all=Z_N(a,b,c)/N^(3-r)>0.                (4)

The last equality is the
[all-channel marked source evaluation](actual_trivalent_all_channel_marked_contraction.md).
All moments in (4), including the lower ones, are finite original
physical contractions with full cluster projectors and the same
marked row. None is declared small or omitted.

The pointed boundary multiplication pairing is

    B_j(fv_j,gv_j)=lambda(fg v_j),
    F_(I,J)=0 if I intersects J,
    F_(I,J)=m_(I union J) otherwise.                 (5)

It is NONDEGENERATE. More precisely let C_(I,J)=1 if I=J^c and zero
otherwise. Multiplication by the following explicitly known unit
q_j of R_r gives

    q_j(eta)=sum_I (m_(I^c)/tau_j)eta_I, q_j(0)=1,
    lambda(fv_j)=tau_j[eta_all](q_j f),
    F=tau_j C M_(q_j),
    det F=det(C) tau_j^(2^r)!=0.                    (6)

Indeed the coefficient identity is checked on each monomial, and
M_(q_j) is unitriangular in increasing degree. Equivalently every
nonzero ideal of the regular cube contains its top monomial, whose
actual marked value is (4). There is no arbitrary maximal-minor
denominator or implicit choice of Smith frame in (6).

This gives an exact algebraic sewing kernel on the WHOLE source
cell: in the monomial frame v_I=eta_I v_j it is

    I_j=sum_(I,J)(F^(-1))_(I,J) v_I tensor v_J.       (7)

For example inserting (7) into two boundary linear functionals
reproduces their contraction through the pairing (5). Because B_j
is nondegenerate, all linear exteriors on S_j can be represented
this way. This is an all-exterior statement on this ACTUAL finite
source cell. It does not assert that the geometric mapping class
of a pants seam acts by the pairing (5) without further typing.

## 3. Explicit positive Gram and its unproved cost

The same moments give a positive Gram without frame inversion. Put
n_j=q_j-1 and use the FINITE binomial polynomial

    q_j^(-1/2)=sum_(k=0)^r binom(-1/2,k)n_j^k,
    w_I=q_j^(-1/2)eta_I v_j.                        (8)

Nilpotence makes this exact; there is no analytic square-root branch.
Then

    B_j(w_I,w_J)=tau_j delta_(I,J^c),
    I_j=(1/tau_j)sum_I w_I tensor w_(I^c).           (9)

Define the conjugate-linear reflection J_j by J_j(w_I)=w_(I^c),
and conjugate its coefficients. The explicit Hermitian form

    H_j(u,v)=B_j(J_j u,v)/tau_j                      (10)

makes the w_I an orthonormal basis. Thus it is positive definite
on the actual complete source cell. J_j is a constructed boundary
reflection; it has not been identified with a physical mirror or
with the original ribbon duality.

Its actual source and dual costs are also explicit. Write
q_j^(1/2)=sum_I a_I eta_I and K_j=sum_I|a_I|^2. Then

    ||v_j||_(H_j)^2=K_j,
    ||lambda|S_j||_(H_j^(-1))^2=tau_j^2 K_j.        (11)

The first equality uses v_j=q_j^(-1/2)q_j^(1/2)v_j.
For the second, lambda(w_I)=tau_j a_(I^c). These identities display
exactly what a Cauchy estimate would cost. Bounded coordinate count
does NOT prove K_j is polynomial or subexponential. The lower
moments m_I/tau_j can carry amplification, and transitions between
different pairings can mix cells. A quantitative bound for those
actual moments and for genuine recoupling matrices remains required.

The source cells outside a+b+c>=d are NOT discarded. Their full
marked source need not be killed by the three-circle observed
quotient, as shown by the
[marked radical obstruction](actual_three_belt_saturated_source_and_marked_metric.md).
They remain additional packets in any full open boundary construction.
Equations (3)--(11) concern precisely the regular surviving cells.

## 4. A rigorous original-source obstruction to independent axes

The actual marked pairing (5) need not be a product of three
two-dimensional axis pairings. There is already an exact counterexample
at N=4 and a=b=c=1. Reduce its ORIGINAL physical matrices in the
cyclotomic field Q(q), q^4=-1, by the homomorphism

    q -> 762 modulo the prime 1009.

This image has exact order eight. All physical and projector
denominators are nonzero in this reduction. In mask order
empty,1,2,12,3,13,23,123 the actual normalized marked moments are

    (m_I/tau) mod1009=(571,201,201,0,201,0,0,1).      (12)

These are RESIDUES, not complex values or floating-point fits.
The flattening of this three-axis moment tensor has the minor

    det [[m_empty/tau,m_23/tau],
         [m_1/tau,m_123/tau]]=571!=0 mod1009.        (13)

Thus the original moment tensor is not decomposable over C: an
identically zero cyclotomic minor would reduce to zero. Rank-one
flattening is invariant under independent invertible changes on
each axis, so such changes cannot make it a tensor product either.
Equivalently the unit in (6) has q_1=q_2=0 but q_12=201 in this
reduction, violating q_12=q_1q_2.

This is a finite exact nonfactorization proof for the prescribed
original marked data. It does not rule out a correlated Gram like
(10), a larger faithful angle embedding, or a different physical
cut. It rules out replacing this actual three-axis marked boundary
pairing by three independent scalar pants norms.

## 5. Original sewing uses one synchronized normal

The [exact NC Morse source reduction](actual_nc_morse_graph_first_normal_source_reduction.md)
gives the appropriate all-width algebraic boundary packet in a
chosen regular generic lift. For fixed labels it retains the entire
ordinary magnetic tensor network Xi_Gamma(t), all source coefficients
s_v(t), the root h0_j,gamma_j,omega_j, and the SAME parameter t
at every boundary. If epsilon^2=0, it is equivalently a tensor
network over C[epsilon]/epsilon^2 with one common epsilon:

    B_v(epsilon)=B_v(0)+epsilon B_v'(0),
    Z_Gamma=(1/nu_N)[epsilon]
       {C_Gamma product_v s_v(epsilon) Xi_Gamma(epsilon)},
    nu_N=2N(-1)^N/(q-q^(-1)).                       (14)

Here the original marked cap must be GLOBALLY exposed/top-level in
the Morse diagram, or its pointed tensor must be genuinely transported
to that cut. A bare local marked row at an arbitrarily nested white
cap is not covered by (14). The original theta mark on16 is exposed,
so none of the local marked moments in sections2--4 is affected.

Every matrix entry and derivative here is explicit in the original
regular W,pi and cups. Only ONE first-normal insertion occurs in
each term of (14), summed over its possible positions. Assigning
independent epsilon_v and extracting one normal from each local
block gives a different source. For example two disjoint theta
sources with just one marked arc have an extra ordinary zero
dimension and vanish, whereas the product of their two independently
marked positive values is nonzero. The missing normalization is
not repaired by a scalar factor on each block.

For a sole unsaturated marked-white vertex the retained term is
s_v'(0)Xi_Gamma(0); at all saturated vertices the term is
product_v s_v(0) Xi_Gamma'(0). These alternatives are genuine full
source identities, not a selection of a preferred geometric saddle.
The source theorem also proves nontriangle deletion at the marked
vertex through the entire generic physical cut, rather than by
assuming the unrestricted mark is an ordinary invariant.

The nondegenerate kernel (7), the topology (2), the longitude
polarization (1), and the synchronized normal (14) give concrete
necessary data for a proposed geometric six-pants sewing map. What
is NOT yet proved is that arbitrary pants identifications are
represented by the canonical algebraic sewing (7), with the actual
annulus/meridian markings and controlled positive energy. A valid
identification must retain the unsupported packets, realize the
Fisher cusp incidence, transport the original single mark, and
control the correlated boundary Gram and recouplings. No closed
theta scalar can replace these checks.

The [focused exact audit](../experiments/audit_actual_six_pants_boundary_torsor_and_sewing.py)
uses full physical cluster projectors, nilpotent circle matrices,
nested cups and unrestricted marked row at six levels N=3,...,8.
It checks all four regular-block sizes, the actual Frobenius determinant,
finite square-root congruence, and the exact residue certificate
(12),(13). It separately checks the connected Fisher boundaries of
the genuine theta, dipole and corrected cube source diagrams.
The finite algebraic proofs above establish the general regular-cell
claims; no polynomial conditioning or general graph volume is inferred.

The root independently read the topology, actual Frobenius determinant,
finite square-root construction, exact source/dual costs, cyclotomic
nonfactorization inference and synchronized-normal scope and reported
analytical PASS. The exact residue arithmetic was separately replayed
by the focused physical audit. These are internal checks, not external
peer review.
