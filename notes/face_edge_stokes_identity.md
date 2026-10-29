# The edge part of face/edge duality

Research note, 25 October 2026. This is an independent algebraic argument
for globally branched, oriented ideal face pairings. It does not use a
quantum-invariant theorem. Its conclusion concerns all **edge rows**;
the row for a specified peripheral curve requires a separate argument.

## 1. Statement and conventions

Let a triangulation have N ordered tetrahedra with signs epsilon_j. Face
gluings preserve the induced order of their three vertices. Let X_i be
the N by 2N incidence matrix for the face opposite vertex i, and put

    D = X_0-X_1+X_2,     R = X_2-X_3,
    E = diag(epsilon_j), script-A = [D;R],
    S = script-A^(-1)[0;E],     r = X_0 S,
    Q_f = -(r+r^T)/2,         P_+ = (E+I)/2.

Assume script-A is invertible. For a global edge e let a_e,b_e,c_e be
the N-component incidence rows for local opposite edge pairs
(01,23), (02,13), (03,12), respectively. Thus an edge can occur twice
in one opposite pair. The literature shape convention gives

    A_e = a_e-c_e, B_e = b_e-c_e     if epsilon_j=+1,
    A_e = a_e-b_e, B_e = c_e-b_e     if epsilon_j=-1,

where this formula is applied column by column. Define

    G = -2Q_f+P_+ = r+r^T+P_+.

**Proposition.** Every edge row satisfies

    A_e = B_e G.                                      (1.1)

There is no geometricity assumption, and no restriction to twist knots.

## 2. A face assignment produced by an edge assignment

Assign an arbitrary number lambda_e to each global edge. Its pullbacks
to a tetrahedron are denoted lambda_01,...,lambda_23. On an ordered
face with vertices i<j<k define the single-valued global face assignment

    phi(lambda)_ijk = lambda_jk-lambda_ik.

Its four local values are

    phi_0=lambda_23-lambda_13,
    phi_1=lambda_23-lambda_03,
    phi_2=lambda_13-lambda_03,
    phi_3=lambda_12-lambda_02.

Consequently D phi=0, whereas R phi=b(lambda)-c(lambda). If
B(lambda)=sum_e lambda_e B_e, then columnwise
B(lambda)=epsilon*(b(lambda)-c(lambda)). Therefore

    script-A phi = [0;E B(lambda)^T],
    S B(lambda)^T = phi,
    r B(lambda)^T = lambda_23-lambda_13.               (2.1)

These equalities follow from invertibility and the displayed local
formulas, without a homology assertion.

## 3. The second half is a discrete Stokes identity

Let v be arbitrary, and let x=S v be its global face assignment. Then
D x=0 and R x=E v. On an ordered triangle i<j<k put

    psi(lambda)_ijk = lambda_ik-lambda_ij.

Both x and psi are single-valued on identified faces. Their oriented
face sum cancels in pairs:

    sum_j epsilon_j sum_i (-1)^i x_(j,i) psi_(j,i) = 0. (3.1)

Within one tetrahedron substitute x_1=x_0+x_2. The summand becomes

    (lambda_02+lambda_13-lambda_03-lambda_12)x_0
       -(lambda_01-lambda_02)(x_2-x_3).

Equation (3.1) therefore says

    B(lambda) r v = sum_j (lambda_01-lambda_02)_j v_j.

Since v is arbitrary,

    r^T B(lambda)^T = lambda_01-lambda_02.             (3.2)

Adding (2.1) and (3.2) gives

    (r+r^T) B(lambda)^T = a(lambda)-b(lambda).

Finally P_+ B(lambda)^T adds b-c in a positive tetrahedron and zero in
a negative tetrahedron. The result is A(lambda)^T. Symmetry of G now
gives (1.1).

## 4. A rank consequence

Suppose the face pairings give a manifold with V ideal vertices and m
global edges. Write A_ed,B_ed for all edge rows. Then

    rank B_ed = m-V.                                 (4.1)

Indeed, lambda in ker(B_ed^T) also belongs to ker(A_ed^T) by (1.1).
The two conditions imply a(lambda)=b(lambda)=c(lambda) in every
tetrahedron. These two local equations are equivalent to the existence
of four numbers t_0,t_1,t_2,t_3 such that

    lambda_ij=t_i+t_j.

For example t_0=(lambda_01+lambda_02-lambda_12)/2, with the other
values recovered similarly; the equal opposite-pair sums are exactly
the remaining consistency conditions. The values t at the three
vertices of a face are uniquely determined by that face's three edge
values. They therefore agree under every face gluing, and descend to
one t per global ideal vertex. Conversely such global vertex values
give a=b=c and B_ed^T lambda=0. This parametrization is injective:
on each triangle its three equations t_i+t_j=0 force all three t's
to vanish. Thus the kernel has dimension V, proving (4.1).

For a one-cusped knot triangulation, Euler characteristic gives m=N
and V=1, so B_ed has rank N-1. Its row dependence is the sum of all
edge rows, since a=b=c=2 for the constant global edge assignment.

## 5. What remains for a peripheral curve

The subsequent `preferred_longitude_cochains.md` supplies the independent
preferred-longitude proof left open in this section, including the singular
relation. Its consequence for boundary fibers and exact framing corrections
is proved in `general_boundary_state_and_framing.md`.

This proof establishes neither

    A_l=B_l G

for the preferred longitude l, nor invertibility after adding that row
to N-1 independent edge rows. A boundary Stokes formula identifying the
induced peripheral line with the kernel of H_1(boundary M)->H_1(M)
would address the former. That formula has not been proved here.

The exact diagnostic in
[audit_two_bridge.py](../experiments/audit_two_bridge.py) recomputes
face matrices and all edge/peripheral rows from canonical face pairings
and SnapPy's integral peripheral marking. It is a finite check, not an
independent proof of the numerical canonicalization or a uniform
two-bridge theorem. Its first nine examples find proper compatible
branchings for 4_1, 5_2, 6_3 and 7_6. For 6_2, 7_3, 7_4, 7_5 and 7_7,
all compatible branchings of the supplied canonical face pairing have
singular script-A (16,16,32,24,32 branchings respectively). In those
cases the unconstrained finite search exhausts its tree before the
10,000-candidate cap. These singularities do not obstruct other
triangulations, other coordinate descriptions, or oscillatory state
representations. They do invalidate an argument that assumes the
canonical layered triangulation is automatically proper.

For the four proper examples the exact preferred-longitude row and
rank-N completed B tests also pass. Those peripheral successes are
separate certificates rather than consequences silently inferred from
(1.1).
