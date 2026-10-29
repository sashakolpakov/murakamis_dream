# Equivariant peripheral roots and the remaining scalar period

Research note, 25 October 2026. The local projective-frame theorem does
not by itself choose compatible deck roots around a knot. This note
supplies that compatibility and a scalar descent argument. Its inputs
are the directly proved cyclic recoupling and frame identities; no global
quantum-hyperbolic invariance theorem is assumed.

Let W be a compact core of a one-cusped hyperbolic knot complement in
S^3, Gamma=pi_1(W), and P=pi_1(partial W). The same proofs apply to more
cusps with one copy of the peripheral data for each cusp. Let n be odd.
Retain the ordered ideal vertices and all peripheral markings. Work on
the nondegenerate decorated-representation locus described below.

The conclusions concern finite-level algebraic tensors and their scalar
phases. Identification of the selected literature period and its integration
cycle, as well as its compatibility across levels, remains outstanding.

## 1. Root lines on Gamma/P are determined at the peripheral stabilizer

First an elementary groupoid lemma. Let a group Gamma act transitively
on V=Gamma/P. A Gamma-equivariant complex line over V is determined,
up to equivariant isomorphism, by its one-dimensional P-representation
chi on the fiber at v_0=P. The reconstruction is the associated line

    Gamma times_P C_chi -> Gamma/P.

This can be checked by sending [g,z] to g.z in the fiber at gv_0;
the relation [gp,z]=[g,chi(p)z] makes the map well defined and invertible.

An equivariant n-th root line, with an identification of its n-th tensor
power with this line, therefore amounts to a character delta:P->C^*
such that delta^n=chi. Its isomorphism classes form a torsor for

    Hom(P,mu_n).

For P=Z^2 with its marked meridian mu and longitude lambda, write
M=chi(mu), L=chi(lambda). Every pair of roots m^n=M, l^n=L gives
delta(mu^a lambda^b)=m^a l^b, and conversely. Thus the root-line
cover has degree n^2 and deck group mu_n times mu_n. No semisimplicity
of the full peripheral representation is needed: only its invariant line.
At a complete unipotent or signed-unipotent character the same statement
holds. The signs and the n^2 root choices are retained.

These are isomorphism classes of roots of the decorating line. They
do not classify the complete quantum period, its normalization phase,
or its continuous dilogarithm factor.

## 2. An explicit multiplicative root of the projective denominator

Choose an SL(2,C) lift rho of the decorated projective representation
and a peripheral fixed point p_0. Put p_v=rho(r_v)p_0, where r_v in
Gamma is a representative with r_v v_0=v and r_(v_0)=1. In an affine
chart write

    d(g,p)=c_g p+d_g,
    rho(g)(p,1)=d(g,p)(rho(g)p,1).

Choose a chart avoiding zero and infinity on the points in use. For a
fixed representation the orbit is countable, so a complex frame can
avoid the entire orbit. For algebraic families every finite diagram
uses its own common nondegenerate Zariski open chart. We do not assume
one finite open chart avoids every possible group-word denominator.

The matrix multiplication identity gives exactly

    d(gh,p)=d(g,rho(h)p)d(h,p).                         (2.1)

The peripheral character is chi(h)=d(h,p_0), h in P. Choose delta as
in Section 1, and choose a_v with

    a_v^n=d(r_v,p_0),     a_(v_0)=1.

For g in Gamma define h(g,v)=r_(gv)^(-1)g r_v in P and set

    D(g,v)=a_(gv) delta(h(g,v))/a_v.                    (2.2)

Substitution into (2.1) proves

    D(g,v)^n=d(g,p_v),
    D(g_1g_2,v)=D(g_1,g_2v)D(g_2,v).                  (2.3)

For the second identity use
h(g_1g_2,v)=h(g_1,g_2v)h(g_2,v). The intermediate a values cancel.
This constructs the root cocycle; independently taking roots of the
denominators would not prove the second equation.

Changing a_v by zeta_v in mu_n changes D by the coboundary
zeta_(gv)/zeta_v. Changing coset representatives gives an isomorphic
root line. Conversely any such multiplicative D restricts to delta at
v_0, so Section 1 proves that these are all root-line choices modulo
object gauges. Internal root choices are frames, while the two peripheral
characters remain actual data.

For a finite diagram, every r_v is a fixed group word. Its matrix
entries and d(r_v,p_0) are algebraic functions of the decorated
representation; only finitely many n-th roots occur. Thus (2.2) is
algebraic on its nondegenerate root chart. The construction on all
configurations uses compatible charts; this statement does not assert
that the entire quantum period lives on a degree-n^2 cover.

An SL(2) lift exists for the knot group under discussion. The obstruction
is the central two-cocycle obtained from arbitrary lifts of the projective
matrices. Since W is aspherical, its class is in
H^2(W;mu_2)=0: knot-exterior homology is H_1=Z, H_2=0, so the universal
coefficient calculation gives zero. Trivializing that cocycle constructs
a lift. Its two choices differ by a sign character of Gamma. For odd n,
changing rho(g) by epsilon(g) and D(g,v) by the same epsilon(g) preserves
(2.3). Ratios D(g,v_j)/D(g,v_i) are unchanged, so the triangle Weyl
rescalings do not acquire an unrecorded sign from this lift choice.

If peripheral coordinates are squared eigenvalues, their root cover is
equivalent after choosing the lift: if u^n=chi^2, set

    delta=u^((n+1)/2)/chi.

Then delta^n=chi and delta^2=u. The inverse is u=delta^2. This records
the unhalved versus eigenvalue convention without dropping a sign.

## 3. The triangle transports can be made strictly equivariant

The ideal vertices of the universal cover are Gamma/P. Assume the
decorating map has infinite image; this holds on the non-elementary
locus containing the geometric representation. Use configurations with
distinct developing points. For each ordered triangle f=(i,j,k),

    lambda_f=(p_i-p_k)/(p_j-p_k).

Equations (2.3) give compatible Weyl rescalings

    kappa(g,f)=D(g,j)/D(g,i),
    nu(g,f)=D(g,k)/D(g,i).

Choose endpoint roots A_v^n=p_v. Choose a marked spectral root alpha
on one representative of each triangle orbit, and propagate it by

    alpha_(gf)=kappa(g,f)alpha_f.

The action on ordered triangles is free. Indeed P is malnormal in the
hyperbolic knot group: a nontrivial element in two distinct conjugate
maximal peripheral subgroups would be a parabolic fixing two distinct
cusp points in the faithful geometric action, which is impossible.
Thus an element fixing two distinct ideal vertices is the identity.
In particular the propagation is well defined. It uses this property
of the underlying knot group, not faithfulness of the variable rho.

The explicit H K construction in `projective_frame_period_torsor.md`
now yields unnormalized maps S(g,f) with the strict law

    S(g_1g_2,f)=S(g_1,g_2f)S(g_2,f).                   (3.1)

Their determinant roots can also be chosen multiplicatively. For each
free triangle orbit choose f_0, write f=r_f f_0 uniquely, and choose
b_f^n=det(S(r_f,f_0))^(-1), with b_(f_0)=1. Set

    rho(g,f)=b_(gf)/b_f,
    S_hat(g,f)=rho(g,f)S(g,f).

Then det S_hat=1 and (3.1) still holds exactly. Different b choices
are scalar frame gauges. This removes a possible triangle-level
composition anomaly constructively. It does not yet make arbitrary
independent tetrahedron normalizations equivariant.

## 4. The remaining tetrahedral phase is an explicit cocycle

Choose shared face roots xi and the signed Racah matrices R_hat as in
the projective-frame note. They have determinant (-1)^((n-1)/2) and
satisfy the ordered pentagon. For t=(0,1,2,3), define Delta(g,t) by

    R_hat(gt)(S_hat(g,023) tensor S_hat(g,012))
       =Delta(g,t)(S_hat(g,013) tensor S_hat(g,123))R_hat(t).

The previously proved ordered operator comparison and Schur argument
prove that this scalar exists and is nonzero. Determinants give

    Delta(g,t) in A=mu_(n^2).                          (4.1)

Here A is cyclic of order n^2; it is different from the peripheral
deck group mu_n times mu_n. There is no reduction of A to mu_n being
assumed in this note.

Strict composition of S_hat gives

    Delta(gh,t)=Delta(g,ht)Delta(h,t).                  (4.2)

Apply the ordered pentagon before and after g and cancel the common
invertible S maps. Its scalar part gives

    product_(i=0)^4 Delta(g,t_without_i)^((-1)^i)=1.    (4.3)

Literal tensor permutations cause no extra scalar in this calculation;
they occur on both sides of the same pentagon. Thus Delta is simultaneously
a group one-cocycle and a configuration three-cocycle.

## 5. Why relative degree four is the relevant obstruction

Let C_k be the free abelian group on ordered (k+1)-tuples of ideal
vertices whose developing points are distinct, with alternating face
boundary. Its augmented complex is exact. For any finite cycle choose
one vertex whose developing point avoids its finitely many points;
prepending it gives a cone, and boundary(cone)+cone(boundary)=identity.
Infinite image of the decoration supplies that vertex.

For k>=1 the Gamma action on C_k is free by malnormality. Also
C_0=Z[Gamma/P]. With I=ker(C_0->Z), the complex

    ... -> C_3 -> C_2 -> C_1 -> I -> 0

is therefore a free Gamma-resolution. Its invariant cochains in degrees
k>=2 compute H^k(Gamma,P;A). One can see the degree shift directly:
Ext^(k-1)_Gamma(I,A) is computed at C_k; applying Hom and Ext to
0->I->Z[Gamma/P]->Z->0 gives the relative cohomology exact sequence,
using the induced-module identification with P-cohomology.

Both W and its boundary torus are aspherical with these fundamental
groups. Their cellular resolutions identify this relative cohomology
with H^k(W,partial W;A). In particular

    H^4(Gamma,P;A)=0,
    H^3(Gamma,P;A)=A.                                 (5.1)

The first equation follows from the dimension-three relative cellular
complex. The second evaluates a cocycle on the oriented relative
fundamental class. It also follows without a field assumption from
H_3(W,partial W;Z)=Z and H_2(W,partial W;Z)=Z, both free. Thus the
statement holds for composite n as well.

## 6. Scalar descent theorem and its residual period torsor

Equations (4.1)--(4.3), freeness on tetrahedra, and (5.1) imply that
the R_hat matrices admit A-valued corrections making both equivariance
and the ordered pentagon exact. Here is a proof that retains the phase.

Choose t_0 in each free tetrahedron orbit and put

    kappa(g t_0)=Delta(g,t_0)^(-1).

By (4.2), replacing R_hat(t) by kappa(t)R_hat(t) makes the tensors
equivariant. Its pentagon discrepancy is the four-cochain
Omega=delta kappa. Equation (4.3) implies that Omega is Gamma-invariant,
and delta Omega=1. The vanishing H^4 in (5.1) gives an invariant
three-cochain b with delta b=Omega^(-1). Hence

    R_tilde(t)=kappa(t)b(t)R_hat(t)                     (6.1)

is equivariant and satisfies the pentagon exactly. Its determinant
is unchanged because the correction lies in mu_(n^2).

Two such corrections differ by an invariant three-cocycle. Modulo
shared-face scalar gauges, their choices form a torsor for

    H^3(Gamma,P;mu_(n^2))=mu_(n^2).                    (6.2)

This residual value is measured on [W,partial W]. Choosing it is a
global period normalization. Hilbert 90 for a field does not remove it.
All phase corrections have absolute value one at each level; the generic
nonconstant units removed in obtaining R_hat and S_hat remain recorded
in their normalization lines.

This proof is local in the algebraic parameter space. On a common
irreducible root chart every phase in A is locally constant, so the
cochain corrections may be chosen constant on that chart. Every finite
recoupling diagram uses finitely many roots and such equations. We do
not infer a finite degree for the full global period cover from the
degree-n^2 peripheral root-line calculation.

## 7. What this closes, and the remaining comparison

### 7.1 The same descent retains arbitrary generic scalar units

The scalar descent argument itself works for any abelian coefficient
group B with trivial Gamma action. The free relative homology gives
H^4(Gamma,P;B)=0 and H^3(Gamma,P;B)=B. Thus if the unnormalized
intertwiners and Racah maps have scalar discrepancy in F^*, where F
is their common algebraic function field, the same argument corrects
equivariance and pentagon while retaining a residual F^* period torsor.
Here Gamma acts on the configuration labels; the parameter field is
fixed. This is not a theorem for an unspecified semilinear field action.

The hypotheses hold for the unnormalized H K transports and raw
pointed Racah maps above: their cocycle and pentagon are exact, and
the ordered operator comparison makes the discrepancy scalar.
Determinant normalization reduces this particular discrepancy to the
finite phase subgroup considered in Sections 4--6. Before that
normalization all generic units remain functions, including any
peripheral factors. The function-field argument supplies rational
sections generically, not a license to specialize a pole.

This explains the proper treatment of a numerical move multiplier.
Its value at a complete point does not identify its generic cochain,
its residual period class, or the normalization selected by the
literature state. A factor such as 1+M^n must remain in that generic
comparison. No identification of the earlier positive factorial
model with these operator tensors follows from the scalar theorem.
An arbitrary F^* correction can change norms across levels; its exact
period class must be fixed before claiming a volume law.

### 7.2 Scope

The result supplies coherent global deck-root multipliers, strict
triangle transports, and a scalar descent theorem for the local cyclic
recoupling system. It isolates the remaining finite scalar normalization
as a relative fundamental-class period. Tensor contraction with specified
duality pairings is consequently equivariant, and ordered nondegenerate
2--3 recouplings have a common normalization. These assertions are
uniform in the hyperbolic knot group and in every odd level.

This is not yet a construction of the prescribed intrinsic knot state.
The selected vectors, duality and vertex-order conventions, the global
literature period/cycle, and the comparison between finite and continuous
dilogarithm periods still have to be matched. A proof of connectedness
for arbitrary admissible realizations is not supplied by the scalar
cohomology calculation. The volume comparison across levels remains
necessary and cannot be replaced by the finite phase normalization.

The degree-n^2 peripheral cover and global character-cover framework
are already present in Baseilhac--Benedetti,
[Analytic families of quantum hyperbolic invariants](https://arxiv.org/abs/1212.4261v3),
Theorem 1.1 and Section 4. The purpose here is the direct root induction
and relative scalar-obstruction proof within the specified local system,
without assuming that paper's global invariance or asymptotic arguments.
