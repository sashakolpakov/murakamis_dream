# The integral half-longitude and the marked quantum boundary algebra

Research note, 26 October 2026. This fills the peripheral index-two
step left in [the pointed gluing construction](pointed_tetrahedron_gluing.md).
The preferred longitude has an integral half-class in the saturated
edge quotient. No division by two modulo the root level is used.
Its scalar lift and its identification with the actual quantum state
remain distinct questions.

## 1. Statement with the knot marking retained

Let M be an oriented knot exterior in S^3 with an oriented ideal
triangulation of t tetrahedra. Use the signed integral shape lattice

    Lambda = direct_sum_j Z^2,    Omega_j=epsilon_j [[0,1],[-1,0]],
    e_0=(1,0), e_1=(0,1), e_2=(-1,-1).

The opposite edge types are (01,23), (02,13), (03,12). For a global
edge e its signed incidence vector has j-th block

    beta(e)_j=epsilon_j(a_ej-c_ej,b_ej-c_ej).

Let E be their span. The independently proved integral edge theorem
in the linked note makes E primitive and isotropic of rank t-1.
Consequently

    B=E^perp/E

is a unimodular symplectic lattice of rank two. The integral normal
curve map delta:H_1(boundary M;Z)->B is taken with convention

    Omega(delta gamma,delta eta)=-2 I(gamma,eta).          (1.1)

Fix the actual marked meridian mu and preferred longitude lambda,
oriented so I(mu,lambda)=1. Then

    ell=delta lambda/2 belongs to B,                      (1.2)
    Omega(delta mu,ell)=-1.

The half in (1.2) is unique, and (delta mu,ell) is an integral basis
of B. Thus it is the preferred longitude that is halved, while the
unhalved meridian retains its prescribed marking. The original
normal-curve image has basis (delta mu,2ell) and index two.

The proof below needs only the knot topology and the primitive edge
theorem, not hyperbolicity or positive shapes. The audited positive
triangulation theorem supplies a geometric realization of this
construction for every hyperbolic knot.

## 2. An intersection identity for arbitrary face permutations

Here is a direct check of (1.1) without a global branching.
At tetrahedron corner v let f_0<f_1<f_2 be the other three indices.
For outgoing normal flows r_f satisfying r_f0+r_f1+r_f2=0 put

    d_v(r)=(-1)^v (r_f1 e_type(v,f2)-r_f2 e_type(v,f1)),
    d(r)=sum_v d_v(r).

For example a single normal arc has flow -1 on its entry side and
+1 on its exit side. The formula is its signed shape-exponent
vector, after eliminating e_2=-e_0-e_1. The oriented cusp triangle
has sign tau_v=-epsilon(-1)^v. Two closed normal flows have

    2 I(r,s)=sum_(j,v) tau_v
                (r_f0 s_f1-r_f1 s_f0).                  (2.1)

This is the intersection form of the thickened trivalent cusp
graph: displace the two flows in its oriented ribbons; the local
contribution at a vertex is half the displayed determinant, and
the contributions in an edge strip cancel between its ends.
The determinant is independent of the cyclic base side because
both flows have sum zero. Thus (2.1) holds for integral graph
cycles as well as for embedded curves.

Set J_3=[[0,1,-1],[-1,0,1],[1,-1,0]]. On face f order its three
vertices increasingly and collect their corner flows as r_f,s_f.
Expansion in the eight independent flow coordinates gives

    Omega_epsilon(d(r),d(s))
      +sum_v tau_v (r_f0 s_f1-r_f1 s_f0)
        =sum_f epsilon(-1)^f r_f^T J_3 s_f.             (2.2)

For every face permutation matrix P,

    P^T J_3 P=sign(P) J_3.

Across an oriented face pairing, both outgoing flows reverse,
and the oriented face signs differ by minus the permutation sign.
Hence the right side of (2.2) cancels pairwise under completely
arbitrary face permutations. Summation proves (1.1).

A small normal circle about an endpoint of a global edge has
shape vector plus or minus beta(e): each successive corner
contributes its signed opposite-edge type. It is contractible
in the cusp. This proves both orthogonality to E and that
changing a cusp representative through a vertex changes its
vector only by E. Thus delta is the stated integral homology map.

## 3. The mod-two cochain that forces divisibility

Take v=(u_j,w_j) in E^perp. In one tetrahedron put, modulo two,

    q_0=-w, q_1=u, q_2=w-u,
    b_0=0, b_1=q_0, b_2=q_1, b_3=q_2.                (3.1)

For a local edge ij with complementary faces k,l,

    q_type(ij)=b_k+b_l.                              (3.2)

For instance edge 01 gives b_2+b_3=u+(w-u)=w=-w
modulo two. The other five identities follow from q_0+q_1+q_2=0.

On the dual edge crossing a paired face Tf<->Ug define

    a_v(Tf->Ug)=b_Tf+b_Ug in F_2.                    (3.3)

Around a dual two-cell, (3.2) identifies its coboundary with
the sum of q-values at the corresponding global edge. This
sum is zero by Omega(v,beta(e))=0. Thus a_v is a closed
cochain on the dual spine of M.

An arc at corner i entering face k and leaving face l pairs
with v modulo two as q_type(ij), where j is the remaining
vertex. Equations (3.1)--(3.2) make this b_k+b_l. Summing
along a closed cusp curve and regrouping at face crossings gives

    Omega(v,delta gamma)=a_v(i_*gamma) mod 2.        (3.4)

The preferred longitude is zero in H_1(M;Z), so its push-in
is zero over F_2. Therefore

    Omega(v,delta lambda) is even for every v in E^perp.  (3.5)

On the unimodular lattice B, a vector that pairs evenly with
every vector lies in 2B: the pairing identifies B with B^vee,
and its associated functional is twice an integral functional.
This proves (1.2). The lattice is torsion free, so the half is
unique. Equation (1.1) gives pairing -1 with delta mu, hence
these two vectors form a basis of the rank-two unimodular lattice.

This argument also works for any boundary class nullhomologous
modulo two. For a multi-component link, a component's preferred
longitude can have nonzero image determined by its linking
numbers; the knot statement should not be copied without that
correction.

## 4. Computing the half before specializing the quantum parameter

Choose an integral basis e_1,...,e_(t-1) of E and an integral
normal representative d_lambda of delta lambda. Solve over F_2

    sum_i a_i e_i=d_lambda mod 2,   a_i in {0,1}.

The solution exists by (1.2) and is unique for this basis because
E is primitive. Set

    e_lambda=sum_i a_i e_i,
    v_ell=(d_lambda-e_lambda)/2 in Lambda.            (4.1)

This is an integer vector, belongs to E^perp, and represents ell.
In particular it makes sense before choosing N. Even N causes
no need to invert two in Z/N. Using another correction changes
v_ell by an element of E and does not change ell in B.

An unspecified homological meridian can differ from the actual
marked meridian by k lambda. The theorem uses the supplied
actual meridian; a cellular algorithm that constructs a linking-one
curve does not thereby fix its framing.

## 5. The square root retains an edge character

At q=exp(pi*i/N), Q=q^2, use the full Weyl convention with
lambda_W=-q:

    W(v)W(w)=lambda_W^Omega(v,w) W(v+w),
    W(v)^N=z^v.

Let the edge eigenspace have its specified character W(e)=c(e).
Write the prescribed unhalved longitude as

    Lambda_hat=a_lambda W(d_lambda).

Since e_lambda and v_ell are orthogonal, (4.1) gives on that space

    Lambda_hat=a_lambda c(e_lambda) W(v_ell)^2.       (5.1)

On the square-root cover, choose the specified lift

    eta_lambda^2=a_lambda c(e_lambda),
    T=eta_lambda W(v_ell),   Y=a_mu W(d_mu).

Then, at every level including even and composite levels,

    T^2=Lambda_hat,       T Y=Q Y T.                 (5.2)

Replacing v_ell by v_ell+e changes e_lambda to e_lambda-2e.
Taking eta_lambda to eta_lambda/c(e) cancels W(e) exactly.
The remaining sign choice is a genuine mu_2 torsor, not an
unrecorded numerical normalization.

There is a further even-level condition. The central value is

    T^N=eta_lambda^N z^v_ell,
    (T^N)^2=Lambda_hat^N.                            (5.3)

For even N, replacing T by -T leaves T^N unchanged. Its sign is
already constrained by the edge-character lift; the mu_2 choice
cannot repair an incorrectly matched central longitude. Matching
the actual SL_2 marking therefore still requires this lift.

With unit-normalized centers, the unhalved algebra generated by
Y,T^2 has two sectors for even N, distinguished by Y^(N/2).
The half-longitude T exchanges them because Q^(N/2)=-1. At odd
N the half and unhalved algebras generate the same matrix algebra.

## 6. Relation to the actual ADO convention and the geometric action

The [independently proved actual descent](even_meridian_norm_descent.md)
uses Y=M^2 and sigma(Y)=QY. Equation (5.2) supplies exactly this
boundary algebra with the prescribed meridian. It is an algebra
and marking identification, not a source-module identification.

The full ADO scalar gauge remains

    g(q,Y)=-q^(-1)(QY-1)/(Y-1),
    T_full=g(q,Y) T_reduced.

On the generic central field, telescope the complete product:

    Norm_sigma(g)=(-q^(-1))^N=(-1)^(N-1),
    T_full^N=(-1)^(N-1) T_reduced^N.                 (6.1)

At Y^N=1 this is an identity of the whole retained lattice,
not permission to evaluate separate zero denominators. The
actual full dimension and its meridian germ must still be kept.

Classically the unhalved normal coordinates are (m,l)=(Y,L^2),
while the saturated lattice has coordinates (Y,L). The scalar
lift fixes the sign of L; completeness does not justify replacing
it by +1. The earlier action conversion is now explained by
the integral lattice:

    dS_Q=Log(L) dLog(Y),
    R=S_Q-(1/2)Log(Y)Log(L).                         (6.2)

This is the same regulator action already derived on the actual
crossing's geometric critical branch. It fixes the parameter and
peripheral determinant, but not that branch's contribution to
the selected quantum period.

## 7. What this supplies to the ideal-triangulation comparison

A positive geometric triangulation supplies the marked Bloch lift
and its volume regulator. Primitive edge reduction supplies a
nonzero rank-N geometric boundary block. The theorem here identifies
its saturated lattice using the actual meridian and preferred
longitude, with every scalar lift visible.

The remaining comparison must construct a relative geometric
extension with its source and evaluation functional and identify
them with those of the actual ADO/Verma period. It must then prove
the selected period has the marked Bloch-regulator norm. Module
rank, matching Weyl algebras, and equality of complete classical
Bloch classes alone do not establish either statement. The
candidate projected tetrahedron vector can still vanish.

## 8. Coverage and exact diagnostics

Theorems 4.1 and 5.1 of
[Neumann's integral triangulation paper](https://www.math.columbia.edu/department/neumann/preprints/cspaper.pdf)
already cover the doubled boundary pairing and its mod-two
compatibility with the interior. This is existing structural
coverage, not a novelty claim. Only those statements were checked
for coverage; the explicit face-flow and mod-two potentials above
give our proof independently.

[The exact audit](../experiments/audit_integral_half_longitude.py)
checks (2.2) symbolically at both orientations, its covariance under
all six face permutations, and 192 mod-two arc identities. Its
12 cellular presentations include native knot triangulations,
diagram shadows with finite sphere vertices, and arbitrary local
relabelings. On a basis of all balanced mod-two vectors it checks
that (3.3) is closed and that every cusp graph cycle satisfies
(3.4). Integer cellular boundaries, the half representative and
the saturated/unhalved Smith invariants are verified separately.

At N=2,3,4,5,6,8,9,10,12 it checks the nontrivial edge-character
correction, (5.2), sector exchange, the even central-sign condition,
and the full gauge norm (6.1) at a generic nonsingular center.
The cellular meridian is explicitly a homological meridian of
unspecified framing. These tests do not identify a quantum knot
state or prove the volume limit. Results:
[integral_half_longitude_results.json](../experiments/integral_half_longitude_results.json).

    PYTHONPATH=.venv/lib/python3.14/site-packages python3 experiments/audit_integral_half_longitude.py --regina
