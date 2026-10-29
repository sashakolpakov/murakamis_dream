# The balanced Verma crossing is a coherent-source exponential

Research proof, 27 October 2026. The actual balanced factorial lattice
has a completed highest-weight model whose block shift and divided
F-power are a literal Weyl pair. This note evaluates the universal
crossing on that model. Its root resonance is an exact exponential;
on coherent kernels it gives finite E-semicyclic crossings with
changing source parameters. Their selected one-cut operator is exactly
the original one, including its full meridian normalization.

The Burau transport and the Verma/Alexander root period were already
proved in [the earlier Verma note](frobenius_verma_period.md), and an
F-semicyclic crossing in [the carry-braiding note](semicyclic_carry_braiding.md).
Those are not new conclusions here. The new comparison is the
balanced normal-source/Fock kernel, its evaluated cyclotomic pole,
and its relation to those existing objects. This source base remains
triangular/reducible. It is not the geometric A-curve or a volume proof.

[Independent proof audit](balanced_verma_coherent_braiding_independent_audit.md).

## 1. The actual balanced infinite lattice

Initially q,M are generic, Q=q^2, x=-M/q and rho=q-q^(-1). On a
free basis w_a, a>=0, put

    K w_a=x Q^(-a) w_a,
    Ecal w_a=(M Q^(-a)-M^(-1)) w_(a-1), a>=1,
    Ecal w_0=0,
    F w_a=(1-Q^(a+1)) w_(a+1), Ecal=rho^2 E.

The adjacent-entry subtraction gives
[Ecal,F]=rho(K-K^(-1)); the two weight equations are immediate.
Thus this is a genuine generic quantum-group module. Its root
head 0<=a<N is exactly the original balanced finite color.
The [common-Verma source note](common_verma_two_wall_source.md)
gives its two boundary walls and normal extension; the construction
below can also be checked directly from the displayed matrices.

Remove only the common Cartan scalar q^(H_1 H_2/2) at w_00, retaining
it as the same marked external line as in the original crossing.
The remaining Cartan diagonal on a pair of colors is

    D w_(a,b)=x_2^(-a)x_1^(-b)Q^(ab) w_(a,b).

The uncheck universal crossing is D R_0, with

    R_0=sum_(k>=0) (-1)^k q^(k^2)
                      Ecal_1^k tensor F_2^k/(Q;Q)_k
       =P_Q(q Ecal_1 F_2).                       (1)

The sum terminates on every fixed input. It is regular at every
prescribed q_N=exp(pi*i/N), including on tail blocks. Indeed its
entry from (a,b) to (a-k,b+k), 0<=k<=a, is exactly

    (-1)^k q^(k^2) {b+k choose k}_Q
                    product_(j=a-k+1)^a (M_1 Q^(-j)-M_1^(-1)). (2)

The Gaussian coefficient is a polynomial. This cancellation is
essential before root specialization. In particular the terms
k>=N do not in general vanish in the infinite root module.

## 2. Root blocks, the Weyl pair, and the two integral lattices

Fix q=q_N, write gamma=(-1)^(N+1), kappa_i=M_i-M_i^(-1), and
kappa_(i,N)=M_i^N-M_i^(-N). Split a=rN+a_bar, 0<=a_bar<N.
On the product completion over the block index, let B be the
backward block shift. Periodicity of the literal coefficients gives

    Ecal=Ecal_head tensor I+kappa W tensor B,
    F=F_head tensor I, K=K_head tensor I,
    W=E_(N-1,0),
    Ecal^N=gamma kappa_N B.                       (3)

The divided operator, formed before specializing, is

    T=[F^N/(Q;Q)_N]_root.

Its action from block r to block r+1 is r+1, because
{(r+1)N+a_bar choose N}_Q tends to r+1. Thus [B,T]=I.
In the Fock realization h_a tensor t^r/r!, B=partial_t and T=t.
The coherent kernel is

    theta_s(h_a)=h_a exp(s t),
    B theta_s=s theta_s, T theta_s=partial_s theta_s,
    pi_0 theta_s=I.                              (4)

It embeds the finite source module with
Ecal_s=Ecal_head+kappa s W, F_s=F_head, K_s=K_head.
Formula (4) is a kernel identity: replacing B,T by s,partial_s
as an algebra homomorphism would reverse their commutator.

The earlier unbalanced Verma lattice has Fv_a=v_(a+1).
Generically w_a=v_a/(Q;Q)_a is a diagonal change of basis; on
blocks a>=N it has root poles. The two root modules therefore
have different central powers and cannot be identified by a
regular root-fiber basis change. On each fixed total-position
sector the generic matrices are conjugate, and their diagonal
traces coincide as regular whole functions. This preserves the
earlier graded Verma/Alexander period while retaining the singular
factorial lattice, rather than identifying its two special fibers.

## 3. The whole crossing's resonant exponential

Use log P_Q(Z)=-sum_(m>=1)Z^m/[m(1-Q^m)], with
Z=q Ecal_1 F_2. On each total-position sector all sums terminate.
Since F^N=(1-Q^N)N T+O((1-Q^N)^2), terms m>=N not divisible
by N vanish at the root. For m=jN, j>=2, the numerator has
j vanishing factors and the denominator only one; these vanish
as well. The sole additional logarithm term is m=N:

    -q_N^N Ecal_1^N tensor [F_2^N/(1-Q^N)]_root/N
                       =Ecal_1^N tensor T_2.

The remaining m<N terms are the logarithm of the finite nilpotent
part, since F_head^N=0. Consequently

    R_0,root=exp(gamma kappa_(1,N) B_1 T_2) R_0,<N. (5)

The two factors commute: B_1 commutes with Ecal_1, and T_2
commutes with F_2, as follows also from their generic definitions.
On every fixed total-position sector the exponential terminates.
On the product completion its entries are defined sectorwise.
This is an exact operator evaluation of the whole quantum
factorial's cyclotomic resonance, not an asymptotic truncation.

## 4. Finite coherent crossings and their changing parameters

Before applying D, the exponential in (5) sends the kernel pair
(s_1,s_2) to (s_1,s_2+gamma kappa_(1,N)s_1). The finite part
depends on s_1 but not s_2, so this translation introduces no
derivatives of its coefficients. The Cartan block ratio is

    D_(rN+a,sN+b)/D_(a,b)=x_2^(-Nr)x_1^(-Ns).

It therefore rescales the two coherent parameters. The complete
uncheck parameter map is

    (s_1,s_2) -> (x_2^(-N)s_1,
                 x_1^(-N)(s_2+gamma kappa_(1,N)s_1)).        (6)

The finite matrix from the source to this target is exactly

    R_s=D_head sum_(k=0)^(N-1)
              (-1)^k q_N^(k^2) Ecal_(1,s_1)^k F_(2,head)^k/(Q;Q)_k.
                                                               (7)

Equations (5)--(6) prove that (7) is the restriction of the
regular infinite crossing to its coherent kernels. It intertwines
the genuine root quantum-group actions in those changing fibers.
The marked common Cartan scalar remains the original one.

For equal knot colors put chi=x^N=gamma M^N and
t=M^(-2N)=chi^(-2). After the checked flip the source map is

    L_+(chi)=[[1-chi^(-2),chi^(-1)],[chi^(-1),0]]. (8)

Its inverse is L_-=[[0,chi],[chi,1-chi^2]]. These are exactly
the earlier Frobenius Verma block matrices. Positive and negative
coherent finite crossings are literal inverses with the intermediate
parameters updated. The positive finite matrix is flip times (7).
For the inverse, first flip and apply D_head^(-1), then use the
finite inverse series sum_(k<N)q_N^k Ecal_(1,s_1)^k F_2^k/(Q;Q)_k,
where s_1 is the recovered original source parameter.

The infinite crossing satisfies the braid equation on finite
total-position sectors as a generic polynomial identity. Its
regular root specialization does also. Restricting to the coherent
kernels proves the finite changing-source braid equation with
scalar one. No unrelated normalization root is chosen in this
argument. This agrees with, rather than enlarges without proof,
the semicyclic coherence already established in the older F chart.

## 5. The exact original selected cut, including a boundary blowup

Every L_+ and L_- fixes the line s_j=chi^(1-j)s. On this line
the coherent crossings are endomorphisms of one ordered tensor
module. Their finite coefficients are polynomial in the source
parameters. An Ecal wrap raises integer residue position by N-1
instead of lowering it by one; a term containing r wraps therefore
raises total position by rN relative to the ordinary crossing.
F_head has no wrap. The same statement holds for the inverse
finite series and every braid word, with the parameters transported.

In the original pivotal partial trace over b-1 strands, closed
indices equal their input indices. A positive-degree source term
would then raise the remaining cut index by at least N, impossible
in a space with indices 0,...,N-1. Hence the entire one-cut matrix
is source independent:

    C_beta(M;s_1,...,s_b)=C_beta(M;0,...,0).       (9)

In particular it has exactly the original reduced ADO value and
Kashaev specialization. This is an equality of cut operators;
the prescribed pivot, zero-framing scalar and whole external
d_N(M) line are retained. No extra cyclic invariant is substituted.

There is a useful regular boundary chart. Write mu_j=kappa s_j,
and use Ecal_mu=Ecal_head+mu W in (7). The source map (8) is
linear in mu as well, and all its matrix entries are regular in M.
Thus (9) extends to M=1 with mu fixed, even though s=mu/kappa
is singular there. The central power is

    Ecal_mu^N=gamma u_N(M)mu,
    u_N=kappa_N/kappa, u_N(1)=N.                (10)

This distinguishes the regular mu chart from setting kappa=0
while keeping s finite, which would erase the cyclic source.
Equality of the selected cut continues through this boundary
because it is a polynomial whole identity, not because a singular
coherent kernel was evaluated independently.

## 6. What this does and does not add to the A-torsor route

The actual factorial lattice, divided normal power, coherent source,
and semicyclic crossing now belong to one explicitly compared object.
The source-period exponential in (5) is fixed by the whole function;
its group action has the Weyl/regular-centralizer realization proved
in the common-Verma note. The source independence (9) and exact
normal factor (10) retain the original selected knot value.

The earlier unbalanced Verma trace still supplies the full factor
Delta_K(M^(2N)); its cancellation at completeness is a whole-germ
statement, not permission to drop the Alexander divisor. This note
does not replace the already proved graded trace identity.

The base transport (8) is triangular/reducible holonomy. Even on
the nonzero exceptional mu chart, F^N=0 and all root-center
meridians stay in the same Borel. This does not identify the
source base with the irreducible geometric A-curve. Nor does an
exact coherent kernel prove which geometric stationary period
survives the original contraction or give its archimedean norm.
The global geometric source and regulator comparison remains open.

For literature coverage only, [Baseilhac, 1101.3440](https://arxiv.org/abs/1101.3440)
explicitly treats root quantum-group representations through quantum
coadjoint action and Heisenberg doubles, with odd-order roots in its
stated scope. [Negron, 2311.13797](https://arxiv.org/abs/2311.13797)
states a quantum-Frobenius tensor-category framework at roots of
arbitrary order. These prevent a novelty claim for the broad
representation-theoretic framework. No theorem from either paper
is a proof premise of the finite matrix and kernel identities here.

[Exact audit](../experiments/audit_balanced_verma_coherent_braiding.py)
and [results](../experiments/balanced_verma_coherent_braiding_results.json)
compare the polynomial Gaussian crossing with (5), coherent kernels,
changing-source inverses, and braid equations at even and composite
levels. They support the uniform proofs above, not a volume claim.
