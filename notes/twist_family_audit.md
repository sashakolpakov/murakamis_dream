# Uniform face, angle and quantum-state certificates for the twist families

Research note, 25 October 2026. This note reconstructs the geometric and finite
matrix arguments for the explicit face families used in the literature.
The quantum asymptotic and annihilator arguments are in
`literature_state_volume.md` and `general_annihilator_and_volume.md`.

Source conventions are Ben Aribi–Guéritaud–Piguet-Nakazawa,
*Geometric triangulations and the Teichmüller TQFT volume conjecture for twist
knots*, [arXiv:1903.09480v5](https://arxiv.org/pdf/1903.09480v5), especially
Sections 4, 5 and 8; and the later FAMED definition and integral (4.5) in
[arXiv:2410.10776v2](https://arxiv.org/pdf/2410.10776v2).

We do not use their geometricity or asymptotic theorem as a black box. The
face pairings, the geometry of their angle maximum, and the Gaussian/edge
identity below are explicit. The subsequent
[topological and peripheral audit](twist_topology_and_peripherals.md)
reconstructs their identification with the twist diagrams and independently
certifies the meridian and preferred longitude. Global quantum move
identities remain separate work; this qualification remains part of the
scope of the final triangulation-independent knot theorem.
All semiclassical limits are for each fixed p. The constants and strip gaps
may depend on p; no simultaneous p->infinity, b->0 estimate is asserted.

## 1. The two ordered face families

Let p>=0. There are p+3 tetrahedra T_1,...,T_p,U,V,W and 2p+6 faces

    e_1,...,e_(p+1), f_1,...,f_p, v,r,s,g,u.

Set f_0=e_1. A tuple lists faces opposite the ordered vertices 0,1,2,3.
Pair equal face labels by the order-preserving map on their three vertices.

| Tetrahedron | Odd family | Even family |
| --- | --- | --- |
| T_j | (e_j,e_(j+1),f_j,f_(j-1)) | same |
| U | (r,v,s,g) | same |
| V | (g,s,f_p,u) | (s,g,f_p,u) |
| W | (u,r,v,e_(p+1)) | (u,v,r,e_(p+1)) |

The signs are (+,...,+,-,-,-) in the odd family and
(+,...,+,+,-,-) in the even family. The literature identifies these with
X_(2p+3) and X_(2p+2), respectively. The p=0 even member is the three-tetrahedron
subdivision of the figure-eight decomposition; the p=0 odd member is the
three-tetrahedron 5_2 example.

An edge angle a is attached to 01 and 23, b to 02 and 13, and c to 03 and 12.
Following the face pairings gives the chain weights

    c_(j-1)+2b_j+c_(j+1),   1<=j<p,   c_0=0,

and the following end weights for p>=1:

    s: 2a_U+b_V+c_V+a_W+b_W,
    0: 2a_1+c_1+2a_2+...+2a_p+a_V+c_W.

Odd family:

    p:   c_(p-1)+2b_p+b_U+b_V+a_W,
    p+1: c_p+b_U+2c_U+a_V+c_V+b_W+c_W.

Even family:

    p:   c_(p-1)+2b_p+b_U+2c_U+a_V+b_V+a_W+c_W,
    p+1: c_p+b_U+c_V+b_W.

Each weight is 2pi. Their sum is twice the sum of all tetrahedral angles, so
one edge equation is redundant. The chains above can be checked directly by
crossing each face with the two endpoints of the local edge. Every one of
the 6(p+3) edge occurrences appears once in this list. The same local crossing
rule gives the p=0 matrices recorded in Section 5 below.

The executable face construction in `experiments/twist_family_certificates.py`
does the edge identifications from the vertex maps, rather than using the
listed weights as an input. It also checks the oriented face gluings, one
ideal vertex, and the Euler characteristic zero of its link in finite examples.
For the uniform geometric argument, a connected torus link is the topological
input supplied by this ordered face family; the edge cycles and orientation
can also be followed inductively along the chain.

## 2. A positive angle structure for every p

Angles in the following formulas have their usual radian units. For p>=1 set

    epsilon=pi/[12(p+1)^2].

For j<p take

    (a_j,b_j,c_j)=(epsilon, pi-epsilon(j^2+1), epsilon j^2).

In the odd family take

    (a_p,b_p,c_p)
       =(pi/2-epsilon(p^2+2p-1)/2,
         pi/2-epsilon(p-1)^2/2, epsilon p^2),
    (A,B,C)=(pi/2+epsilon p^2/2, pi/3, pi/6-epsilon p^2/2),
    U=(A,B,C), V=(A,B,C), W=(B,C,A).

In the even family take

    (a_p,b_p,c_p)
       =(3pi/4-epsilon(p^2+2p-1)/2,
         pi/4-epsilon(p-1)^2/2, epsilon p^2),
    (A,B,C)=(pi/4+epsilon p^2/2,
             2pi/3-epsilon p^2/3, pi/12-epsilon p^2/6),
    U=(A,B,C), V=(A,C,B), W=(C,B,A).

All entries are strictly between 0 and pi. Substitution in the preceding
edge weights verifies every balancing equation. For p=0, use (A,B,C)=
(pi/2,pi/3,pi/6) in the odd family and (pi/6,2pi/3,pi/6) in the even family.
The explicit edge-incidence matrices below verify these cases directly.

## 3. The volume maximum is interior: a reconstructed proof

Let Lambda(theta)=-integral_0^theta log(2sin t)dt. The volume of a positively
oriented ideal tetrahedron with angles summing to pi is

    V(a,b,c)=Lambda(a)+Lambda(b)+Lambda(c).

It is continuous on the closed angle simplex, positive in its interior and
zero on its boundary. Its restricted Hessian, in a,b with c=pi-a-b, is

    -[[cot a+cot c, cot c],[cot c,cot b+cot c]].

The diagonal pivots are positive before the minus sign and the determinant
is 1, so this Hessian is negative definite. Thus the sum over tetrahedra is
strictly concave on the positive angle polytope. It has a maximum on its
compact closure, and the explicit positive structure makes that maximum
strictly positive.

### 3.1 The only possible flat tetrahedra at a maximum are taut

A triple (0,b,pi-b) with 0<b<pi gains volume with derivative +infinity along
a segment to any positive angle structure: Lambda'(t)=-log(2sin t), and the
new positive zero angle supplies -a log epsilon. A taut triple (0,0,pi) has
a finite, nonnegative one-sided derivative along that segment; its epsilon
log epsilon terms cancel. All other tetrahedra have finite derivatives or
the same positive divergence. Hence a maximum cannot contain a flat
non-taut tetrahedron. Any zero angle at a maximum belongs to a permutation
of (0,0,pi).

### 3.2 Symmetry reduction preserves a global maximum

In the odd family align the end triples as

    U, V, (c_W,a_W,b_W).

In the even family align them as

    U, (a_V,c_V,b_V), (c_W,b_W,a_W).

In either case the s equation says 2a_U=a_V+c_W. Replace the three aligned
triples by their arithmetic average. Its first coordinate equals a_U. The
other two coordinates preserve their respective sums in the endpoint
constraints. Thus the averaged triples still satisfy all the edge equations.
Concavity and invariance of ideal volume under angle permutation show that
their total volume has not decreased. There is therefore a symmetric global
maximum with aligned triples all equal to (A,B,C).

For p>=1 the reduced odd endpoint constraints are

    c_(p-1)+2b_p+3B=2pi,     c_p+A+3C=pi,

and the reduced even endpoint constraints are

    c_(p-1)+2b_p+A+3C=pi,    c_p+3B=2pi.

In both cases the earlier chain equations remain, and c_0=0. These reductions
follow by substitution in the full edge weights; the redundant 0 equation
then holds automatically.

### 3.3 Odd family

At a symmetric maximum, c_p=pi would imply A=C=0, B=pi, contradicting the
first endpoint constraint. If c_p=0, the convex nonnegative sequence
(0,c_1,...,c_p) is identically zero, because

    c_(j-1)-2c_j+c_(j+1)=2a_j>=0,   j<p.

Then b_p is 0 or pi by Section 3.1. For b_p=0 the endpoint equations give
U=(0,2pi/3,pi/3), forbidden by that section. For b_p=pi all tetrahedra are
taut and the total volume is zero. Both possibilities contradict maximality.
Thus 0<c_p<pi and T_p is positive.

None of A,B,C can be pi: the endpoint equations exclude B=pi and C=pi,
and A=pi would force c_p=0. Hence U,V,W are positive by Section 3.1.
The chain equations first give b_j>0 by forward induction, starting from
b_1=pi-c_2/2>=pi/2. Descending induction then gives b_j<pi: the first step
uses c_p>0, and each following step uses positivity of the next tetrahedron.
By Section 3.1 every chain tetrahedron is positive. For p=1 the chain
inductions are empty and the endpoint argument is unchanged.

For p=0 the reduced condition is A+3C=pi. Its interior contains positive
triples. Its boundary has either a flat non-taut triple or zero total volume,
so its maximum is interior as well.

### 3.4 Even family

The second endpoint equation gives B=(2pi-c_p)/3 in [pi/3,2pi/3]. Thus U is
positive by Section 3.1. The chain forward induction gives b_j>0 for j<p.

If b_(p-1)=pi, the last chain equation forces c_p=0. The first endpoint then
forces b_p=0, and the two endpoint equations give U=(0,2pi/3,pi/3), a
contradiction. Descending induction yields b_j<pi for all j<p, so these
tetrahedra are positive. Convexity of (0,c_1,...,c_p) then gives c_p>0.
For p=1 the same c_p=0 contradiction follows directly from the endpoints.
Thus the only remaining possible flat tetrahedron is

    (a_p,b_p,c_p)=(0,0,pi).

Suppose this occurs. Write r=c_(p-1), or r=0 if p=1. The endpoint equations
give

    U=((pi+r)/2, pi/3, pi/6-r/2),       0<=r<pi/3.

For p>=2 perturb the last two chain triples and U by the following column
increments, multiplied by small t>0:

    T_(p-1): (-1,+1,0),
    T_p:     (+2,0,-2),
    U:       (-1,+2/3,+1/3),

and propagate the same aligned U change to V,W. These preserve every angle
and edge equation. For p=1 omit the first increment. T_p stays flat and
contributes zero volume on the path; all other affected tetrahedra remain
positive. Direct differentiation gives

    exp(-V'(0+))
       = [sin b_(p-1)/sin a_(p-1)]
            sin^2 B sin C / sin^3 A,                       (3.1)

with the bracket absent for p=1. The chain equations and convexity give
a_(p-1) in [pi/6,pi/2], so the bracket is at most 2. Also

    sin^2 B sin C/sin^3 A
       = (3/4) sin(pi/6-r/2)/cos^3(r/2) <=3/8.

For the inequality, its logarithmic derivative in t=r/2 is
-cot(pi/6-t)+3tan t<=0 on [0,pi/6). Therefore (3.1) is at most 3/4<1, or
3/8<1 for p=1. This gives V'(0+)>0, contradicting the maximum. The maximum
is consequently positive in every tetrahedron.

For p=0 the symmetric constraints reduce to B=2pi/3, A+C=pi/3. The strictly
concave symmetric volume is maximized at A=C=pi/6, an interior point.

### 3.5 Why an interior maximum gives a complete hyperbolic metric

Here is the needed direction of the usual Casson–Rivin argument, reconstructed
from its multipliers. At an interior maximum on the full angle polytope,
there are a multiplier lambda_T for each tetrahedron and mu_e for each
global edge such that for opposite local edges e,e' carrying angle theta,

    -log(2sin theta)=lambda_T+mu_e+mu_e'.                    (3.2)

This is ordinary linear algebra: the derivative is orthogonal to the kernel
of the affine constraint matrix. Independence of all constraint rows is not
required.

Realize the unique positive ideal tetrahedron with each prescribed angle
triple. At its ideal vertex v scale the Euclidean cusp triangle by

    exp(lambda_T+sum_(w!=v) mu_(vw)).

Its side opposite the corner along vw then has length

    exp(mu_(va)+mu_(vb)-mu_(ab))/2,

where v,a,b are the vertices of the face containing that side. This follows
from (3.2) and the Euclidean sine rule. The expression depends only on the
three global edges of that face. Hence it matches on paired faces.

All cusp triangles therefore glue isometrically. Around a global edge their
angles sum to 2pi, so the cusp surface has no cone singularities. The face
isometries preserve these horosphere cuts; the possible dilation in the edge
holonomy is consequently 1, while its rotation is 2pi. The tetrahedra glue
to a nonsingular hyperbolic metric. The compact torus cusp section is flat
and gives a complete cusp end. This proves a complete finite-volume metric,
whose volume is the sum of the ideal tetrahedral volumes.

This argument supplies positive complete geometric shapes without relying on
a numerical maximizer or on the source's geometricity theorem.

## 4. The face Gaussian for every p, from elementary elimination

Use the current FAMED spectral variables t_j,t_U,t_V,t_W, and the equations
script-A f+script-B t=0, with script-B's lower block the tetrahedral sign
matrix. The chain face equations give

    f_j=e_1-sum_(k<=j)t_k,
    e_(j+1)=e_j+f_j.

The end equations force f_p=t_U in both parities, hence

    e_1=t_U+sum_k t_k,
    f_j=t_U+sum_(k>j)t_k,
    e_j=j t_U+sum_k min(j,k)t_k.

Odd end solution:

    u=t_U-t_V, s=t_V-t_U, g=t_V-2t_U,
    v=(p+1)t_U+sum_k k t_k+t_W,
    r=(p+2)t_U+sum_k k t_k-t_V+t_W.

Even end solution:

    u=s=t_U-t_V, g=2t_U-t_V,
    r=(p+1)t_U+sum_k k t_k+t_W,
    v=(p+2)t_U+sum_k k t_k-t_V+t_W.

The homogeneous equations have only the zero solution, so script-A is
invertible for every p, including p=0. The same elimination uses only unit
pivots, so its determinant has absolute value 1.

Taking the symmetric part of the selected x_0 face variables gives Q_f:

    (Q_f)_ij=min(i,j),   (Q_f)_(iU)=i,
    (Q_f)_(iV)=(Q_f)_(iW)=0,    1<=i,j<=p,

and the U,V,W block

    odd:  [[p+2,-3/2,1],[-3/2,1,-1/2],[1,-1/2,0]],
    even: [[p+1, 1/2,1],[ 1/2,-1,-1/2],[1,-1/2,0]].

Thus G=-2Q_f+diag((epsilon+1)/2) is explicit. In the chain block
G_ij=-2min(i,j)+delta_ij and G_(iU)=-2i. Its end blocks are

    odd:  [[-2p-4,3,-2],[3,-2,1],[-2,1,0]],
    even: [[-2p-1,-1,-2],[-1,2,1],[-2,1,0]].

## 5. Edge and peripheral matrices, with no assumed inverse formula

At a positive tetrahedron the angles a,b,c correspond to z,z'',z'; at a
negative one they correspond to z,z',z''. Convert the actual edge incidences
accordingly to G_0,G',G'', and set A_edge=G_0-G', B_edge=G''-G'. Direct
substitution of the displayed G in each chain and end row gives

    A_edge=B_edge G.

The preferred-longitude rows used in the source, independently identified
by normal curves and integral boundary certificates in the topological
companion note, are

    odd:  a_l=(...,2,-2,2), b_l=(...,0,2,2),
    even: a_l=(...,-2,4,2), b_l=(...,0,2,0).

They too satisfy a_l=b_l G. Their branch constant is nu_l=2pi. For p>=1,
take edge rows s,0,1,...,p-1,p+1 and this longitude row. In B they read

    s: -v_W,
    0: -v_1+v_W,
    k: 2v_k-v_(k-1)-v_(k+1), 1<=k<p, v_0=0,
    p+1: -v_p+v_U+v_V                 (odd),
          -v_p+v_U+v_V-v_W            (even),
    l: 2v_V+2v_W                      (odd),
       2v_V                            (even).

Their homogeneous kernel is zero, starting with v_W=v_1=0, then the chain,
and finally V,U. Thus B is invertible; unit elimination gives |det B|=2.
The corresponding A satisfies B^(-1)A=G. Solving Bv=e_last gives

    2 B^(-1)e_last=(0,...,0,-1,+1,0).                       (5.1)

The affine boundary coordinate is therefore x=y_V-y_U. At the complete
maximum the aligned U,V triples give exactly the same positive shape,
z_U=z_V, so x=0 and gamma=0. No unknown peripheral constant is needed.

For p=0, explicit choices of the two edge rows and the longitude row give

    A_odd=[[-1,0,1],[-1,1,-1],[2,-2,2]],
    B_odd=[[-1,-1,1],[1,1,0],[0,2,2]],
    A_even=[[0,0,-1],[-2,1,1],[-2,4,2]],
    B_even=[[1,1,-1],[-1,-1,2],[0,2,0]].

They have |det B|=2, the same identity B^(-1)A=G, and the same boundary
vector (-1,+1,0). All p>=0 are thus covered by explicit matrix certificates.

For later exact normalization comparisons, the vector c/pi=B^(-1)(nu/pi)-G1
has chain entries i(2p-i+1), V entry -1, W entry 1, and U entry
p^2+p+2 in the odd family or p^2+p+4 in the even family. Here each edge
branch constant is 2-sum_j G'_ej, in units of pi.

## 6. Comparison with the older published twist-state formulas

The FAMED state has all Phi factors in the numerator. Transform to the older
spectral variables y'_j by

    z_j=-y'_j (chain), z_W=y'_W,
    odd: z_U=y'_U,  z_V=y'_U+x_0,
    even: z_U=-y'_U, z_V=x_0-y'_U,

where z here denotes *spectral integration coordinates*, not complex
tetrahedron shapes, and x=2pi sqrt(hbar)x_0. Inverting the chain factors,
and the U factor in the even case, uses the exact identity

    Phi_b(-y')=zeta_b exp(pi i y'^2)/Phi_b(y'),
    zeta_b=exp(i pi(b^2+b^(-2))/12).

Consequently the exact FAMED integral equals

    C_X zeta_b^r/(2pi sqrt(hbar)) times J_derived(hbar,x_0),

where r=p for odd parity and r=p+1 for even parity, and C_X is the explicit
orientation constant of the chosen published fiber convention. Its absolute
value is 1 in these unimodular face families. No exponential factor of
nonunit modulus has been dropped at the complete point.

The reduced Gaussian on y'_1,...,y'_p,y'_U,y'_W has chain block min(i,j),
chain-U entries -i in the odd case and +i in the even case, and U,W block

    odd:  [[p,1/2],[1/2,0]],
    even: [[p+1,-1/2],[-1/2,0]].

The extra quadratic boundary term is

    odd:  x_0(x_0-y'_U-y'_W),
    even: x_0(y'_U-y'_W-x_0).                              (6.1)

The linear vector, divided by pi, has chain entries -i(2p-i+1), W entry 1,
U entry p^2+p+1 in the odd case and -(p^2+p+3) in the even case, and the
extra boundary term is -pi x_0/sqrt(hbar). These formulas follow by ordinary
quadratic substitution using Sections 4–5.

**A version-specific discrepancy.** In arXiv:1903.09480v5, the even theorem
statement and its concluding state formula print the *odd* boundary quadratic
x_0(x_0-y'_U-y'_W). The preceding derivation explicitly computes the even
expression in (6.1). Our direct face-matrix calculation agrees with that
derivation. The difference depends on the internal variable y'_U, so it is
not an overall scalar peripheral factor. Both expressions agree at x_0=0,
which is why this discrepancy does not change their complete-point volume
limit. The exact generic-boundary definition used here is the later FAMED
integral (4.5), retaining its own published convention. The final journal
version has not been checked for this discrepancy.

## 7. What follows, and what remains to audit

For every member of these explicit ordered face families, Sections 2–5
provide the positive complete geometric and finite matrix certificates
required by the independent state-integral theorem. Thus its published
FAMED state has the hyperbolic volume limit. In the Andersen–Malusà b-shift
algebra acting on its explicitly rescaled spectral variable, it also has a
nonzero annihilator and a primitive minimal operator, by the dimension-count
and moment proof. The classical symbol contains the geometric peripheral
curve with the stated lift and orientation conventions.

At the complete boundary value, the older displayed twist states have the
same limit because their exact ratio to the derived state is a unit-modulus
phase times a power of sqrt(hbar). Therefore no arbitrary recurrence
boundary condition or colored Jones sequence has been used.

The subsequent topological note reconstructs the diagram-to-face-family
construction and independently identifies the peripheral curves. It gives
a three-arc marked-edge-germ certificate for the actual meridian, a
ten-arc auxiliary curve, and an integral boundary certificate for the
preferred longitude. Exact angle-constraint identities show that the
longitude branch correction is zero in both parities. Thus these results
apply to the stated literature realizations of the named twist knots.
The exact global state transformations needed to identify arbitrary
triangulations and the broader alternating-knot extension remain open.

Run `python3 experiments/twist_family_certificates.py` for exact diagnostics
on p=0,...,8 in both parities. They recompute edge classes, link counts,
face matrices, positive angle equations, and the FAMED and peripheral matrix
identities from the face tuples. The proofs above, rather than the finite
sample, establish the displayed algebraic and angle statements for all p.
