# The actual ADO threaded character and a separating source projector

Research note, 26 October 2026. This proves an exact, uniform formula for
Chebyshev-threaded interior loops in the specified ADO evaluation. It
retains the odd-thread signs and framing phases and then isolates a
parity-independent even character. A null-homologous loop separates this
character from the complete hyperbolic character for every hyperbolic
knot. Thus identifying fixed central eigenlines is the wrong proposed
comparison in that setting. A source extension can still encode the
period as a distinguished splitting; a precise projector lemma states
what an actual construction would have to provide.

The proof uses the fixed unrolled matrices and elementary exact
sequences, not a published Chebyshev--Frobenius or quantum-trace theorem.
No quantum invariant or state is replaced. The volume conjecture and the
construction of the required geometric source extension remain unproved.

## 1. Fixed evaluation and actual annular threading

Let K be an oriented zero-framed knot, q=exp(pi*i/N), N>=2. Use
the literature color V_alpha and parameters

    x=q^alpha, M=-qx, Y=M^2, U=Y^N=M^(2N).

The pivot is K^(1-N). The core cut evaluation is the one already
fixed in [the ADO note](kashaev_ado_pointing.md). Write F_N^L(M)
for its reduced scalar with an additional framed fundamental-color
link L in the complement; N_N^L=d_N F_N^L is the full period.
The fundamental color W and its exact framed skein relation are
those of [the peripheral-fusion calculation](actual_peripheral_fusion.md).

For a further framed oriented loop gamma disjoint from L and K,
let C_n(gamma) be its annular Chebyshev threading, with

    C_0(X)=2, C_1(X)=X, C_(n+1)(X)=X C_n(X)-C_(n-1)(X).

Products mean framed parallels, and the definition is linear on
the resulting link combinations. It has integer coefficients and
uses no singular Jones--Wenzl projector. Choose the Seifert zero
framing in S^3 as reference, and write f for gamma's framing,
ell=lk(gamma,K), b=lk(gamma,L), the sum over the components of L.

## 2. Integral Weyl modules without divided-factorial denominators

For m>=0 define D_m on u_0,...,u_m by

    H u_j=(m-2j)u_j, K u_j=q^(m-2j)u_j,
    E u_j=[m-j+1]u_(j-1), F u_j=[j+1]u_(j+1).

These formulas have no factorial denominators. The identity
[j+1][m-j]-[j][m-j+1]=[m-2j] checks the commutator, and the
H and K relations follow directly from the weights. At the specified
root E^N=F^N=0: every product of N consecutive quantum integers
contains a multiple of N. They are therefore actual weight modules
for the same restricted unrolled quantum group, even when m>=N.
Only the auxiliary loop's color is changed here; the core color
and its reduced or full normalization stay fixed.

For every m>=1 there is the exact sequence

    0 -> D_(m+1) -> W tensor D_m -> D_(m-1) -> 0. (2.1)

Here are explicit maps, valid before and after root specialization:

    i(v_j)=q^(-j)w_0 tensor u_j+w_1 tensor u_(j-1),
    pi(w_0 tensor u_j)=t_(j-1),
    pi(w_1 tensor u_j)=-q^(-j-1)t_j,

where missing endpoint vectors are zero. They preserve H and K.
Substitution in Delta E=E tensor K+1 tensor E and
Delta F=F tensor 1+K^(-1) tensor F verifies E and F using
[j+1]=q[j]+q^(-j) and q[j+1]-[j]=q^(j+1).
The map i is injective, pi is surjective, and pi*i=0. Their
dimensions give exactness. All these assertions use unit matrix
entries and do not divide by [N]. Also W tensor D_0=D_1.

Consequently in the Grothendieck group of these actual modules,

    [D_m]=U_m([W]/2),
    C_n([W])=[D_n]-[D_(n-2)], n>=2.              (2.2)

This follows recursively from (2.1); it is not a generic-q
semisimplicity argument specialized through a pole.

## 3. Root subquotients, including their pivots and twists

At m=N there is the additional exact sequence

    0 -> D_(N-2) -> D_N -> C_(+N) direct-sum C_(-N) ->0, (3.1)

where C_h is the one-dimensional module with H=h, K=q^h, E=F=0.
The submodule map is u_a -> [a+1]v_(a+1), 0<=a<N-1. These
coefficients are nonzero. The quotient consists of the two endpoint
weights +N and -N. The endpoint transitions to the quotient vanish
because [N]=0. This checks every generator and proves (3.1).

Combining (2.2) and (3.1),

    C_N([W])=[C_(+N)]+[C_(-N)].                 (3.2)

For delta_N=(-1)^(N-1), both one-dimensional colors have

    dim_q(C_(+/-N))=delta_N,
    theta(C_(+/-N))=delta_N*i^N.                 (3.3)

Indeed their pivot is q^((1-N)h), their crossing is q^(h^2/2),
and closing that crossing gives the twist
q^(h^2/2+(1-N)h). These are exactly (3.3) at h=+/-N.
No framing phase is omitted.

The polynomial identity C_(2N)(X)=C_N(X)^2-2 and tensoring
one-dimensional colors then give

    C_(2N)([W])=[C_(+2N)]+[C_(-2N)].             (3.4)

These latter colors have pivot one, twist one, and trivial double
braiding with W. Their double braiding with V_alpha is the scalar
x^(+/-2N)=M^(+/-2N). This is the even character used below. It
does not silently replace the odd-thread data (3.3).

## 4. Why these Grothendieck identities compute the actual knot period

The closed auxiliary-component evaluation is additive in a short
exact sequence of colors. A direct proof uses a braid with the core
cut and a basis adapted to the auxiliary submodule. The finite R,
its inverse and the pivot preserve the filtration on each colored
strand, with the strand positions exchanged at a crossing. A state
can move only down the filtration along the underlying auxiliary
component. Closing its trace forces it to return to its initial
filtration piece; therefore every contributing state stays in one
graded piece around that entire component. Summing those pieces
gives exactly the two subquotient-colored evaluations. Separate
closed components are treated independently. This is filtered
linear algebra on the literal cut contraction, not an assumption
about additivity of a modified trace on the core.

Naturality of R and the tensor-product crossing identities proved
in the peripheral note identify tensor colors with framed
parallels. Thus (3.2)--(3.4) apply to the stated annular threadings
for arbitrary gamma, including knotted gamma and diagrams with
auxiliary self-crossings.

For C_h, h=+/-N, the ratio between the two possible crossings
with a core strand is the scalar monodromy q^(hH)=x^(+/-N).
With a W strand it is -1. Unlinking the auxiliary component by
crossing changes therefore records only its linking numbers.
Its remaining one-dimensional knot evaluation is its pivotal
dimension times its framing twist. This last statement can also
be checked directly: on a one-component braid with B strands and
writhe w, the zero-framing value is g^(B-w)=g, since g=+/-1
and B-w is odd. Its self-crossing scalar cancels against the twist.

We obtain the exact whole-germ formulas

    F_N^(L union C_N(gamma))
       =delta_N*(delta_N*i^N)^f*(-1)^b
                         *(x^(N ell)+x^(-N ell))*F_N^L,

    F_N^(L union C_(2N)(gamma))
       =(U^ell+U^(-ell))*F_N^L.                 (4.1)

In the first line x^N=delta_N*M^N, so its multiplier can also
be written delta_N^(ell+1)*(delta_N*i^N)^f*(-1)^b times
M^(N ell)+M^(-N ell). In the second line every auxiliary framing
and W-linking phase cancels exactly. The same equations hold for
the full period N_N^L, retaining the entire modified dimension.

For the boundary meridian ell=1 and f=b=0, the first equation
is C_N(M+M^(-1))=M^N+M^(-N). For the preferred parallel ell=0,
it is 2delta_N, agreeing with the full ADO character
T^N=(-1)^(N-1). These provide independent checks of both signs.

No universal Chebyshev homomorphism at degree 2N, or an unproved
identification of its source skein parameter, is asserted. Equation
(4.1) is the specific evaluation identity proved here, including
the actual fourth-root phases at degree N.

## 5. The marked ramified fibre has the trivial even character

The even eigenvalues in (4.1) are the squared-trace coordinates
of the abelian character with meridian

    rho_U^ab(mu)=diag(U^(1/2),U^(-1/2)):
    (tr rho_U^ab(gamma))^2-2=U^ell+U^(-ell).      (5.1)

The square-root sign is irrelevant to this coordinate. At U=1
the value is two for every gamma. This includes the whole marked
fibre of [ramified Weyl descent](ramified_weyl_fibre.md): in its
coordinate z=(U-1)/(U+1), U^ell+U^(-ell) is even with constant
term two. It multiplies both a_0 and b_0 by two. No extra odd
coefficient changes the complete normal functional.

In particular a null-homologous gamma has ell=0, and its even
threading acts by exactly two on the entire meromorphic family,
not just at the complete point. This also survives the canonical
polar subtraction and its affine source equation: each part is
multiplied by the same constant two.

This does not require K_N to be nonzero. The ordinary anchor
(a_0)_1/(Q-1)=1 makes the actual marked fibre nonzero at every
level. Nor does (5.1) contradict a hyperbolic semiclassical critical
point: the threading degree 2N grows with the level. Fixed small
observables and fixed root-central characters are different data.

## 6. A null-homologous geometric separator for every hyperbolic knot

Let rho_hyp be the complete holonomy. Two conjugates of a cusp
meridian have distinct fixed points: otherwise the meridian
conjugates, which generate the knot group, would all preserve one
point, contradicting the non-elementary complete holonomy.
After conjugation and harmless SL_2 signs, write them as

    p=[1 1;0 1], q=[1 0;s 1], s!=0.

A direct multiplication gives

    tr[p^a,q]=2+a^2*s^2,
    (tr[p^a,q])^2-4=a^2*s^2*(a^2*s^2+4).        (6.1)

The choices a=1 and a=2 cannot both make the second expression
zero when s!=0. Thus one of the two commutator words gamma has

    lk(gamma,K)=0,
    g_gamma(rho_hyp):=(tr rho_hyp(gamma))^2-2 !=2. (6.2)

Represent the word by an embedded loop and choose its framing.
The even threading formula is independent of that framing. The
squared trace is independent of the lift to SL_2. The witness
is uniform; no alternatingness or knot table is used.

The positive ideal triangulation represents this same complete
holonomy, so g_gamma-2 is a unit in its local geometric character
ring. This is a precise interior-character distinction not detected
by the common parabolic peripheral values alone.

## 7. What a fixed-central-character comparison can and cannot identify

Suppose a proposed geometric root realization identifies the even
threaded observable C_(2N)(gamma) with the scalar
g_gamma(rho)=(tr rho(gamma))^2-2. This is explicit comparison data;
no published quantum-trace Frobenius theorem is being assumed to
establish it here. At the hyperbolic point, (6.2) and the actual
evaluation (5.1) give distinct eigenvalues.

Any intertwiner preserving this observable between the actual
evaluation fibre and that fixed geometric central-character fibre
must be zero: its matrix Phi satisfies

    (g_gamma(rho_hyp)-2)*Phi=0.

The same holds locally because the difference is a unit. A scalar
Hilbert-90 frame change or finite faithfully flat cover cannot
change these scalar eigenvalues. In particular a direct equality
of these two *fixed central eigenlines* cannot be the missing
state comparison.

This is not an obstruction to a source extension, a comparison
only after the correct relative pushforward, or a varying-centre
realization with a hyperbolic semiclassical saddle. Such a second
realization need not have the fixed hyperbolic root character.
It also does not show that the entire cyclic module of an actual
operator lacks geometric factors: its selected evaluation is a
particular quotient, and the distinction matters.

## 8. A separating observable can select the source period exactly

There is a useful positive consequence for the extension approach.
Over a difference field (F,sigma), take a specified source system

    sigma(w)=A_aug*w, A_aug=[ C  b;0 1 ].

Suppose it carries an actual difference endomorphism

    X_gamma=[ G  d_gamma;0 2 ],
    sigma(X_gamma)*A_aug=A_aug*X_gamma,            (8.1)

and 2I-G is invertible. Its unique eigenvector of eigenvalue two
whose source coordinate is one is

    w=(v,1), v=(2I-G)^(-1)*d_gamma.              (8.2)

This vector is automatically horizontal. Applying sigma to its
eigenvalue equation and using (8.1) shows that both sigma(w) and
A_aug*w are eigenvectors of sigma(X_gamma) with eigenvalue two
and last coordinate one. Invertibility gives uniqueness, hence
sigma(w)=A_aug*w. This proves the source equation, without a
monodromy computation or a root-rank hypothesis.

Equivalently the eigenline projector is

    P_2=[0  (2I-G)^(-1)d_gamma;0 1], P_2^2=P_2.

It preserves the difference structure by (8.1). If G=g_gamma I
is a fixed geometric central character, the separator (6.2)
makes the inverse a regular scalar near the complete point.
Its denominator supplies no growing-level volume exponent.
Any such exponent must remain in the actual source coefficient
d_gamma and its selected period pairing.

The even threading theorem supplies the eigenvalue two for the
actual null-homologous observable. The geometric triangulation
supplies a classical separator with g_gamma!=2. What is still
missing is construction of an actual relative gluing/source system
with the endomorphism (8.1), its off-diagonal coefficient, and the
marked normal functional. Neither block can be chosen to force
the desired value. The lemma is a criterion for that construction,
not a proof that it has already been achieved.

Specializing a generic nonsplit source extension to a split
root-level extension causes no contradiction: its distinguished
splitting (8.2) can still carry large periods. Splitting and the
norm of the specified splitting are separate statements.

If a specified generic source class is nonsplit, a separating
endomorphism of the form (8.1) cannot exist over that generic
difference field: (8.2) would split it. It cannot arise after a
finite sigma-stable algebraic cover either, by the normalized-trace
descent proved in [the affine note](affine_quantum_a_period.md).
The actual threaded observables have degree 2N and depend on the
level. Their root-level existence supplies no such fixed generic
endomorphism. This retains the distinction between an algebraic
evaluation at each level and a fixed-degree presentation across
all levels.

## 9. Literature coverage and what has not been imported

The common skein/gluing framework is already covered by
[Garoufalidis--Yu, A quantum trace map for 3-manifolds](https://arxiv.org/abs/2403.12424)
and [Panitch--Park, 3d Quantum Trace Map](https://arxiv.org/abs/2403.12850).
The later [Chen--Kricker, On 3d Quantum Trace Maps](https://arxiv.org/abs/2606.13268)
advertises partial comparison of these constructions. Their abstracts
and the scope of the quantum-gluing definition were consulted for
coverage. No global trace-map, equivalence, Frobenius-compatibility,
or knot-state-comparison proof from these works is a premise here.
In particular no phase identification between their quantum
parameters and the actual ADO parameters is inferred by citation.

Chebyshev threading and root-of-unity representation theory have
existing coverage; no novelty is claimed for that framework or
for the elementary spectral projector. The results here are the
independent, normalization-matched evaluation identities, the
uniform geometric separator, and the resulting precise source
comparison criterion for this fixed knot period.

## 10. Independent diagnostics

[The audit](../experiments/audit_ado_threaded_shadow.py) constructs
the actual modules and R matrices. It checks 52 integral Weyl
sequences and 11 root subquotient sequences through level 18.
At levels 2,3,4,5 it checks 192 heterogeneous R-trace cases,
including positive/negative linking, an extra fundamental strand,
both threading degrees, and all three framing signs. Sixteen
actual knotted auxiliary traces test the closed-component
additivity through nontrivial positive and negative knot braids.
The commutator witness and the separating source projector are
also checked symbolically. The
[results](../experiments/ado_threaded_shadow_results.json) support
the uniform algebraic proofs and establish no volume asymptotic.
