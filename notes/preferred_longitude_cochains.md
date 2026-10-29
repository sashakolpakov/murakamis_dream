# The preferred-longitude identity, including singular charts

Research note, 25 October 2026. The cochain construction audited here
appears in Kambampati,
[Integral face-edge duality for knot triangulations, arXiv:2610.04103v1](https://arxiv.org/abs/2610.04103v1),
Sections 4--6. We reconstruct its local identities and global cancellation.
The cusp intersection identity below has a separate exhaustive local
verification. We do not use that paper's analytic corollaries, integral
cokernel theorems, or any claimed quantum asymptotic as a premise.

This closes the preferred-longitude gap left in `face_edge_stokes_identity.md`.
The extra condition for an ordinary boundary fiber remains distinct.

## 1. The relation already supplied by Fourier reduction

Use the notation S,Q,G from `reduce_singular_faces.py`, with

    G=-2Q+P_+, P_+=diag((epsilon+1)/2),
    L={ (t,s): t in im S, s-Gt in (im S)^perp }.

Here Q is the symmetric ambient extension of the reduced Gaussian.
The dimension of L is N, and L is Lagrangian for the form
t.s'-s.t'. The Fourier regularity theorem applies to every globally
branched knot-exterior triangulation, even when its stacked face matrix
is singular.

Introduce two global face assignments x,y with

    (X_0-X_1+X_2)x=0,
    (X_3-X_2+X_1)y=0,
    (X_2-X_3)x=(X_1-X_0)y.

Set t=E(X_2-X_3)x and s=X_0x+X_3y+P_+t. These assignments parametrize
exactly L. Here is an independent dimension argument that avoids an
assumed Neumann--Zagier rank theorem.

On local face values use the pairing
sum epsilon*(x_0 y_0-x_1 y_1+x_2 y_2-x_3 y_3). It vanishes for two
global face assignments by cancellation across identified faces. The
local constraints give tuples

    x=(a,a+b,b,b-epsilon*t),
    y=(p-epsilon*t,p,p+w,w).

Pairing an original lift of t' with a reversed lift of t gives

    (t')^T X_0 x_t = t^T X_3 y_(t').

In particular t obeys both Fourier support constraints, and the last
identity gives S^T(s-Gt)=0. Thus the image is in L.

The map is injective. In the zero-shape case t=s=0, the face cochains
of Section 2 agree on every occurrence of a global edge. They give an
ideal edge cocycle, which vanishes by `automatic_face_regularity.md`.
Its first and last edge values recover x and -y, hence x=y=0.
There are 4N face unknowns and only 3N equations, so the parameter
space has dimension at least N. Injectivity into the N-dimensional L
forces dimension N and surjectivity.

## 2. Face potentials and a closed dual-spine cochain

On a quotient face with ordered vertices a<b<c define potentials

    phi(a)=0, phi(b)=x_f, phi(c)=x_f-y_f.

Their directed edge differences agree on the two occurrences of a
paired face. For local faces k,l meeting in edge jm define

    q_jm=epsilon*sgn(j,m,k,l)*(h_k(jm)-h_l(jm)),
    h_k(jm)=phi_k(m)-phi_k(j).

These potentials use separate corners of each characteristic triangle,
even though those corners map to the same ideal vertex.

This is independent of the choices of ordering of jm and kl. The
local tuples of Section 1 give

    q_01=q_23=t,
    q_03=q_12=epsilon*(x_0+y_3),
    q_02=q_13=-t-epsilon*(x_0+y_3).

Therefore these are the homogeneous physical shape coordinates for

    (log z,log z',log z'')=(t,s-t,-s),

with prime/double-prime placement determined by epsilon. Edge equations
follow by canceling the h terms around each complete global edge link.

Derive auxiliary local face values f_i as follows. Put f_0=0 and, for
i=1,2,3, let jm be the edge shared by faces 0 and i and set

    f_i=phi_0(j)+phi_0(m)-phi_i(j)-phi_i(m).

Substitution gives

    f=(0, -x_2-x_3, x_0-x_2-x_3+y_3, x_0-2x_3+y_3).

For every pair k,l, not only those involving face 0, one obtains

    phi_k(j)+phi_k(m)-phi_l(j)-phi_l(m)=f_l-f_k.          (2.1)

For a normal cusp arc at vertex j entering face k and leaving face l,
the signed shape contribution is consequently

    h_k(jm)-h_l(jm)
       =[f_l+2phi_l(j)]-[f_k+2phi_k(j)].                 (2.2)

The sign here is the one used by `curve_holonomy`: epsilon times the
sign of the permutation (j,m,k,l). Our code derives f from endpoint
sums and checks all six equations (2.1) and all twenty-four directed
arc equations (2.2), for each tetrahedron sign.

On a directed dual edge crossing from face (T,k) to its partner (U,l),
give the value a=f_(T,k)-f_(U,l). Around a dual two-cell, equation
(2.1) writes its period as a telescoping sum of endpoint potentials.
Paired-face potentials agree, so that period is zero. Thus a is a
closed cochain on the dual spine of the knot exterior.

On a closed normal cusp curve, the phi terms of (2.2) cancel across
successive paired faces. The resulting shape period is exactly its
dual-spine period under a. Pushing each cusp arc through the center of
its truncated tetrahedron gives that same dual-spine path and preserves
its homology class. A preferred longitude is nullhomologous in the
exterior. Its period is therefore zero.

We have proved, for its actual unhalved normal-curve row,

    A_l t-B_l s=0 for every (t,s) in L.                  (2.3)

This proves immediately that

    B_l^T in im S,
    S^T(A_l^T-G B_l^T)=0.                               (2.4)

If the face matrix is invertible, im S=R^N and (2.4) becomes the full
identity A_l=B_l G. No finite-example extrapolation is involved.

## 3. A separate local proof of the peripheral symplectic pairing

For a closed normal cusp curve gamma let h_gamma be its physical
angle-coefficient row. Put

    J_epsilon=blockdiag(epsilon_j*J0),
    J0=[ 0  1 -1; -1  0  1; 1 -1  0 ].

Then, with our cusp orientation and positive-turn convention,

    h_gamma J_epsilon h_eta^T=-2 intersection(gamma,eta).

Here is the finite local identity that proves this formula. List the
24 directed normal arcs of a tetrahedron as (vertex,entry,exit).
Place gamma endpoints at fraction 1/3 and eta endpoints at fraction
2/3 on the ordered sides. Let r_gamma(f) be +1 for its exit face,
-1 for its entry face and zero otherwise. For each common face f,
let i,j be the ranks of the arc vertices in the ordered face. Then

    local algebraic pairing + 2 local intersection
       =sum_f epsilon*(-1)^f*r_gamma(f)*r_eta(f)*K_ij,
    K=[ 1  1 -1; -1 -1  1; 1 -1  1 ].                 (3.1)

All 2*24^2=1152 cases are checked with rational line intersections and
integer arithmetic by `audit_boundary_cochains.py`. Equation (3.1)
is also a direct three-side endpoint calculation; it handles arcs
at different vertices as well as intersecting arcs in one cusp
triangle. On identified faces both endpoint signs reverse, their
product is unchanged, the vertex ranks agree, and epsilon*(-1)^f
reverses. The boundary terms cancel. Summing (3.1) proves the formula.

After eliminating the prime coordinate, the same algebraic pairing is
A_gamma B_eta^T-B_gamma A_eta^T. In particular a meridian m and
longitude l oriented with intersection(m,l)=1 have pairing -2.
The factor two is retained; the longitude row is not divided by two.

## 4. The complete preferred-longitude relation

The full edge block (A_ed|B_ed) has rank N-1. Indeed its left kernel
consists of global edge assignments with equal sums on the three
opposite pairs in every tetrahedron. Such an assignment is locally
lambda_ij=n_i+n_j. A triangle's three edge values uniquely recover
its three vertex values, so the values agree under all gluings.
There is one ideal vertex, hence this kernel is precisely the
one-dimensional space of constant edge assignments.

An edge row can be represented by a small contractible cusp curve
around one endpoint germ of that edge. It has zero intersection with
every peripheral curve. Section 3 therefore proves edge isotropy and
orthogonality to every peripheral row. The longitude row is independent
of the edge rows: pairing a proposed dependence with the meridian
would give zero, whereas its longitude pairing is -2.

Delete one full edge row and append the preferred longitude. The
resulting N by N matrices A,B consequently satisfy

    rank(A|B)=N, AB^T=BA^T.

Section 2 proves L is contained in ker(A|-B). Both spaces have
dimension N, so

    L=ker(A|-B)=im [B^T;A^T],
    im S=im B^T, rank B=dim S=N-2k.                    (4.1)

The image equality follows from the displayed symplectic identity
and rank. This proves nullity doubling and the full constrained
preferred-longitude Gaussian identity independently of a presumed
analytic result.

In particular every proper globally branched knot triangulation has
invertible preferred-longitude B and its exact FAMED matrix identity.
For a singular chart the same statement is a relation on im S, not
an unjustified inverse of B.

## 5. What this does and does not settle for the boundary state

If rank B_ed=dim S-1, adding the longitude increases the B rank. The
allowed shape plane is then independent of longitude holonomy and
one may extract the boundary state by an ordinary linear fiber.
If instead rank B_ed=dim S, the longitude moves that affine plane.
These two cases must be distinguished; (4.1) does not rule out the
second case.

Wong's existing definition makes this distinction in condition (2) of
Definition 1.5 of
[arXiv:2512.23198v1](https://arxiv.org/abs/2512.23198v1).
We do not assume its additional meridian/framing condition or its
analytic theorem. A separate change of peripheral polarization is
needed when the linear fiber represents a framed meridian.

Reproduce the independent audits with

    python3 experiments/audit_boundary_cochains.py

The finite global checks include all fundamental cycles of the cusp
dual graph, the closed dual-spine cochain, its preferred-longitude
period, and equality of the face and completed gluing relations.
The proof above supplies the uniform statement beyond those examples.
