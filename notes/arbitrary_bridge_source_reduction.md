# Eliminating every bridge: an arbitrary plat and its retained source

Research note, 27 October 2026. The general target is every hyperbolic
knot, with no bound on its bridge number. The twist-family calculation
is a diagnostic example. This note replaces its one-variable relator
by a construction for an arbitrary 2k-plat and arbitrary crossing word.
All elimination arguments below are proved for arbitrary k and word
length; the audit is a check of the formulas, not their proof.

The result is a scheme-level reduction, an explicit sourced deformation
complex, and its determinant and dual transport. It does not yet prove
the selected Kashaev period's regulator norm. In particular, a
contraction of the classical deformation complex is not asserted to
be a contraction of the full finite quantum period.

## 1. A general bridge presentation, without a twist-family hypothesis

Fix a 2k-strand plat of a knot K. The upper and lower trivial tangles
each have k bridges. Choose oriented puncture meridians so an adjacent
cap identifies its two meridians as inverses. Work first with the
noncentral trace-tau SL_2 class O_tau. Inversion preserves this class.
Put

    X=O_tau^(2k),        P(H)=H_(2k)...H_1,
    j(B_1,...,B_k)=(B_1,B_1^(-1),...,B_k,B_k^(-1)).       (1.1)

Thus P j=I. At the complete point use tau=2 (or the consistently
marked negative lift). The inverse puncture meridian is an orientation
convention, not a change of the knot's peripheral marking.

For a positive crossing use the already derived actual holonomy map

    h_i(...,A,B,...)=(...,A^(-1) B A,A,...),
    h_i^(-1)(...,A,B,...)=(...,B,B A B^(-1),...).          (1.2)

Both preserve P and commute with simultaneous conjugation. They are
regular mutually inverse maps on the matrix scheme: SL_2 inversion is
the adjugate, so (1.2) introduces no rational denominator.
Let F_beta=h_L ... h_1 be the arbitrary braid word, in actual action
order. Its cap equations are

    (F_beta j(B))_(2i) (F_beta j(B))_(2i-1)=I,
                                     1<=i<=k.          (1.3)

At a solution set A_i=(F_beta j(B))_(2i-1). Then
F_beta j(B)=j(A). This eliminates every upper bridge variable A_i
by just reading an odd endpoint. Van Kampen gives the knot-group
presentation: each trivial-tangle complement is free on its bridge
meridians, the punctured-sphere meridians restrict as (1.1), and their
other restrictions are transported by (1.2). Consequently (1.3),
modulo simultaneous conjugation, is the fixed-trace representation
scheme of that marked knot presentation on the stated open locus.

There is also an elementary scheme-theoretic elimination proof. If
H_0=j(B), H_s=h_s(H_(s-1)) are retained as independent stage variables,
substitution removes H_1,...,H_L in order. Each equation solves for
its target with coefficient I. The inverse map sends each eliminated
H_s to h_s...h_1 j(B). These two maps of coordinate rings are inverse.
This holds over Artin rings and retains nilpotents. It is not a
dimension count or an equality only of reduced solution sets.

In particular, the crossing words do not disappear. They are all
retained in F_beta and the k residual cap equations. Eliminating
transport variables does not change K to an unknot.

## 2. The normal to a cap and the three global dependencies

At a point (A,A^(-1)) write a boundary tangent as (v_o,v_e).
Differentiating H_e H_o gives

    q_A(v_o,v_e)=v_e A+A^(-1)v_o,
    N_A=im(1-Ad_(A^(-1))) subset sl_2.                 (2.1)

The range is precisely the two-dimensional plane N_A. Its kernel
is the cap tangent

    dj_A(v)=(v,-A^(-1)v A^(-1)).                        (2.2)

Indeed q_A dj_A=0, and the explicit splitting

    r_A(n)=(0,n A^(-1))                               (2.3)

is tangent to X and satisfies q_A r_A=I. To see the tangent claim,
N_A is the trace-pairing annihilator of the one-dimensional traceless
centralizer of A; equivalently it is the right-trivialized tangent
space at A^(-1). No choice of a logarithm is involved.

Take the direct sum q of (2.1) and N=direct_sum_i N_(A_i).
Since every pair product is I at the cap point, the derivative of P is

    m_L=dP|_(j(A))=M q,       M(n_1,...,n_k)=sum_i n_i. (2.4)

Here dP already takes values in sl_2 because P=I. These three global
dependencies are essential; treating all cap relations as independent
scalar equations gives the wrong complex.

Let V=T_B O_tau^k, set J_s=dh_s at its actual stage, and define

    D_beta=q J_L ... J_1 dj_B : V -> N,
    a_B(xi)=([xi,B_1],...,[xi,B_k]).                   (2.5)

Equivariance and P preservation prove, for every k and beta,

    D_beta a_B=0,          M D_beta=0.                 (2.6)

We therefore obtain the endpoint complex

    0 -> sl_2 --a_B--> V --D_beta--> N --M--> sl_2 -> 0,
    dimensions:       3,  2k,        2k,       3.       (2.7)

The quotient ker(D_beta)/im(a_B) is exactly the infinitesimal
fixed-trace character deformation of the plat presentation. Both
the upper and the lower bridge tuples generate the represented knot
group. At an irreducible representation a_B is injective. Also M
is surjective: an element trace-orthogonal to every N_(A_i) commutes
with every A_i, so is zero in sl_2. Thus (2.7) is acyclic precisely
when the fixed-trace character is infinitesimally rigid.

This is a 2k by 2k map for arbitrary bridge number, independent of
the number of crossings. No two-bridge reduction is assumed.

## 3. An explicit contraction, including inhomogeneous transport

This step is pure linear algebra over any coefficient ring where
the displayed tangent bundles have been trivialized. It does not
require acyclicity of (2.7).

Retain v in V and all intermediate u_s in T_(H_s) X. The full middle
differential has rows

    e_s=u_s-J_s u_(s-1),   u_0=dj_B v,
    n=q u_L.                                             (3.1)

Write T_(s:r)=J_s...J_r and set T_(s:s+1)=I. The triangular change
of domain coordinates from (v,u_1,...,u_L) to (v,e_1,...,e_L) has
diagonal I and determinant one. Its inverse is

    u_s=T_(s:1) dj_B v
                  +sum_(r=1)^s T_(s:r+1) e_r.            (3.2)

In the target replace the last row by

    n'=n-sum_(r=1)^L q T_(L:r+1) e_r.                    (3.3)

This is another determinant-one triangular change. The middle map
now consists of D_beta and L identity pairs of rank 4k. Since 4k
is even, grouping these blocks introduces no permutation sign.

The two end maps are transported as well. Put m_s=dP|_(H_s).
Product preservation gives m_s J_s=m_(s-1). The last map before
elimination is

    (e_1,...,e_L,n) |-> M n-sum_s m_s e_s.               (3.4)

It kills (3.1), because m_0 dj_B=0. After (3.3) it is just M n',
since M q T_(L:s+1)=m_s. Conjugation maps to (a_B,0,...,0)
in the new domain. This is an explicit chain equivalence of the
entire four-term complexes, not only equality of determinants.

For actual inhomogeneous linear transport

    e_s=b_s,       n=c,

the retained endpoint source is therefore exactly

    c_eff=c-sum_(s=1)^L q T_(L:s+1) b_s,
    D_beta v=c_eff.                                      (3.5)

Its compatibility is M c=sum_s m_s b_s, equivalently M c_eff=0.
No source term has been replaced by zero. If (2.7) is acyclic,
a compatible source has a solution unique modulo conjugation.

The dual source is equally explicit. If a linear functional is

    ell_0(v)+sum_s ell_s(u_s),

its value on a solution becomes

    [ell_0+sum_s ell_s T_(s:1) dj_B](v)
       +sum_(1<=r<=s<=L) ell_s T_(s:r+1) b_r.             (3.6)

The second line is a prescribed affine constant. Omitting it changes
the pointed pairing even when the homogeneous complex is unchanged.
Equivalently, all covectors transform by the inverse transpose of
the displayed changes. This is the source/co-source transport needed
when eliminating every bridge's intermediate strands.

## 4. The normal determinant has a specified volume, not an arbitrary unit

Use the conjugation-invariant residue two-form

    nu=dH_11 wedge dH_12/H_12
       =-dH_11 wedge dH_21/H_21                        (4.1)

on the respective regular charts of O_tau. Inversion pulls nu back
to -nu; that cap sign is retained. Define the volume on N_A by

    nu_N(n_1,n_2)=nu_(A^(-1))(n_1 A^(-1),n_2 A^(-1)).   (4.2)

With this definition (dj_A,r_A) identifies the product cap/normal
volume with nu_A wedge nu_(A^(-1)). A different splitting changes
only an off-diagonal block and has determinant one.

Take product volumes on V and N and the same ordered basis
(diag(1,-1),E_12,E_21) on the two copies of sl_2. At a regular
irreducible representation choose columns V_c completing a_B to
a basis and a right inverse W of M. The sourced endpoint torsion is

    T_plat=vol_V[a_B,V_c]/vol_N[D_beta V_c,W].            (4.3)

It is nonzero, independent of both splittings and invariant under
simultaneous conjugation. Splitting changes add image columns or
multiply numerator and denominator by the same determinant.
Conjugation preserves nu and has determinant one on sl_2.

Equations (3.2)--(3.4) preserve this entire determinant line: each
removed identity pair has torsion one in its identical stage bases.
Thus no factor depending on a meridian, a crossing count or a root
level is silently discarded. This statement is for the explicitly
defined linear complex. It does not identify (4.3) with the original
quantum Gaussian density merely because both are invariant objects.

## 5. Regularity at the complete hyperbolic representation

The geometric input already audited in this repo supplies a positive
complete ideal triangulation (under its recorded Epstein--Penner
input). The polarized gluing argument in
[the rigidity note](geometric_rigidity_and_cyclic_source.md#1-positive-shapes-make-marked-gluing-unramified)
proves that the edge equations together with fixed meridian have
invertible shape Jacobian. Here is the missing direct passage to
the bridge representation tangent; no published character-rigidity
proof is required.

Consider a dual-number deformation of the complete representation
whose noncentral meridian has constant trace 2. Its meridian has a
unique free eigenline reducing to the complete cusp line. This can
be checked in a chart with a unit off-diagonal entry: Cayley--Hamilton
gives (mu-I)^2=0, and its rank-one kernel solves for that line.
Every peripheral element commutes with mu and hence preserves it.
Develop the ideal vertices using the deformed cusp line. The
nondegenerate complete tetrahedra remain nondegenerate over the
dual numbers, so their cross-ratios are defined and satisfy the
same gluing equations. The meridian eigenvalue is still 1.

The invertible marked gluing Jacobian makes every infinitesimal
shape change zero. Conjugate so three vertices of one lifted
tetrahedron agree with the undeformed vertices. Its fourth vertex
agrees because its cross-ratio does. Propagate across adjacent
faces; the connected lifted dual graph then makes every developed
vertex agree. For each group element, the two representations act
identically on three distinct developed points, so they agree in
PGL_2 over the dual numbers. The SL_2 infinitesimal discrepancy is
also zero, since the central lift is discrete in characteristic zero.
Thus the original deformation is simultaneous infinitesimal
conjugation. The negative trace lift gives the same argument with
mu+I and eigenvalue -1.

Consequently (2.7) is acyclic at the complete representation of
every hyperbolic knot for which the recorded positive geometric
triangulation input applies. This has no bridge-number restriction.
It is not an assertion that every other parabolic character is
regular, reduced or isolated.

## 6. The original finite quantum source can be bent into a plat

The actual finite quantum network can be put in this presentation
without defining a new invariant. Use its original crossings,
unrolled weights, zero-framing correction and pivot, and the
explicit turns in
[the duality note](relative_pivotal_duality.md#2-double-duality-fixes-the-actual-pivot-exactly):

    x_dual=x^(-1)Q^(-1),
    J_x v_a=(-x)^a Q^(a(a+1)/2) v_(N-1-a)^*,
    J_x^(-t) J_(x_dual)=g=K^(1-N).                       (6.1)

The already proved matrix snake identities permit an identity
strand to be replaced by a cup followed by its paired cap. Moving
a linear map through a bend uses its literal turned matrix
J_V^(-1) A^t J_W. Repeating these finite matrix substitutions puts
the cut tangle in plat form and preserves its entire contraction.
It retains dual colors, weight lifts and all turn scalars. A same-
color crossing must not be substituted for the turned crossing.

Keep exactly one marked cut. If C_N=F_N(M) I is the original
zero-framed reduced cut, its balanced source is still psi=1 and
phi=(1/N)sum_a, or e=psi phi with Tr(e)=1. Carry this source through
the same bends, rather than close the last cut by an ordinary
pivotal cap. The latter has Tr(g)=0 and loses the invariant.
The resulting pointed plat contraction is exactly F_N(M), hence
F_N(1)=<K>_N. If using the unreduced ADO state, multiply by its
same whole d_N(M); nothing in the re-expression cancels or
evaluates that peripheral germ separately.

This is a finite tensor re-expression of an existing pointed state.
The inhomogeneous b_s in Section 3 are general tangent source data,
not an assertion that the full quantum affine extension has already
been expressed by those classical columns. Deriving that complete
quantum-to-normal source map is still required.

The subsequent [quantum boundary theorem](quantum_bridge_cap_source.md)
now supplies the explicit finite turns, cyclic source corners and
their full meridian half-step transport. A marked defect g^(-1)e
also gives a fully closed pointed plat with the exact reduced
normalization 1/N for every k. Its principal cap equations give
the inverse-meridian relations and original selected flag directly.
This specifies the boundary input to the missing map; it does not
yet construct the full quantum-to-normal period comparison.

## 7. What replaces the one-variable twist residue

Equations (1.3), (2.7), and (3.5) are the replacement for a Riley
polynomial and its 1/(S f') residue. They retain all k bridge
meridians and the three global dependencies. The marked peripheral
words can be carried along the exact representation-scheme
isomorphism in Section 1; eliminating them to the eigenvalue image
produces the corresponding classical A-support, with lift and
saturation conventions still specified. It does not prove a
minimal summed quantum operator has no lost geometric component.

This directly advances the previous repo work: the old
[Markov theorem](pointed_markov_reduction.md) controlled one added
strand of a closed braid; the present contraction removes every
intermediate stage of an arbitrary bridge presentation and gives
the transported source, dual affine constant, and cap-normal
determinant. Unlike the twist calculation, it has no single trace
coordinate, Chebyshev recurrence, or family restriction.

The unresolved theorem remains at the quantum period level: send
the actual pointed affine extension and its selected evaluation to
this regular geometric normal complex and marked regulator action,
with a comparison whose nonzero norm is subexponential across N.
Classical acyclicity solves compatible infinitesimal transport; it
does not by itself prove this comparison or control cancellation
in the selected finite scalar. The volume conjecture is not proved
by the present elimination theorem.

## 8. Existing coverage and independent verification

Plat representation intersections and their volume/torsion forms
already have coverage, for example Dubois's
[2005 paper](https://www.numdam.org/articles/10.5802/aif.2136/)
and [2006 plat-volume paper](https://msp.org/agt/2006/6-1/agt-v6-n1-p13-p.pdf).
Their stated scope is SU(2) regular representation spaces. This
coverage check is not a borrowed proof of our parabolic SL_2 complex,
its normalization, or any quantum-period comparison. The direct
proofs used here are (2.1)--(3.6) and the geometric argument above.
No novelty is claimed for the underlying plat decomposition or
triangular elimination.

[Audit](../experiments/audit_arbitrary_bridge_source.py).
[Results](../experiments/arbitrary_bridge_source_results.json).
