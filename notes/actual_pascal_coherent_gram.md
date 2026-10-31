# An explicit coherent Gram for an actual split source

29 October 2026. The finite q-Pascal matrix gives an explicit,
invertible, source-independent local packet transform. Pulling back a
positive factorial metric produces a full-rank NON-DIAGONAL Gram.
For the original figure-eight four-plat split packet its co-source
norm is exactly `sqrt(N)` and its positive energy has the sharp volume
exponent. No unknown knot value defines the transform or its metric.

This is a constructive instance of the proposed special-inner-product
Cauchy inequality. It does not yet transport the three-braid complete
clock decomposition to this split packet or provide a sharp energy
estimate for arbitrary knots. Those distinctions matter after the
[complete clock-sector obstruction](actual_figure_eight_clock_gram_obstruction.md).

## 1. A local all-exterior Pochhammer packet identity

Let `Q` be a primitive Nth root, `N>=2`, `d=N-1`, and let `Y,u` be
arbitrary nonzero variables. Write `F_n=(Q;Q)_n`. For `0<=k<=n<N`
define the actual split-route tensor

    T_(n,k)(Y)=Y^(2k-n) [n choose k]_Q
                    (Q/Y;Q)_k (YQ^(-n);Q)_(n-k).       (1)

These are precisely the surviving finite routes `a=n-k` of the
[original four-plat proof](figure_eight_whole_source_identity.md#4-forced-transfer-elimination-and-its-whole-scalar).
That proof derives them from the original E/F entries, unrolled dual
colors, full Cartan scalar, actual turns and the specified `g E_00`
cut coupon. In particular (1) has no unspecified peripheral scalar.

Set

    C_n(Y)=(-1)^n Q^(-n(n+1)/2)(Q/Y;Q)_n,
    v_k(Y,u)=(-1)^k Q^(k(k-1)/2)(uYQ)^k,
    P_(n,k)=[n choose k]_Q if k<=n, and 0 otherwise.

Then the following is an ENTRYWISE identity of whole Laurent
polynomials, retaining the complete internal-clock fugacity:

    u^k T_(n,k)(Y)=C_n(Y) P_(n,k) v_k(Y,u).            (2)

Proof. Reverse the `n-k` consecutive Pochhammer factors in (1):

    (YQ^(-n);Q)_(n-k)
      =(-Y)^(n-k)Q^[-(n(n+1)-k(k+1))/2]
                         (Q^(k+1)/Y;Q)_(n-k).

Their product with `(Q/Y;Q)_k` is `(Q/Y;Q)_n`. The remaining
monomial is exactly the one in (2). No division by `(Q/Y;Q)_n`
is used; its zero fibers and all meridian jets are retained.

Consequently the whole k-fiber is

    sum_(k=0)^n u^k T_(n,k)(Y)
       =C_n(Y)(uYQ;Q)_n.                            (3)

The finite q-binomial theorem proving (3) follows by inserting the
last factor, using q-Pascal. All Gaussian factorial indices are below
N, so even levels and composite levels cause no exception.

The exterior scope is precise. The `n` boundary port, `Y`, and all
other exterior variables remain open. An ARBITRARY polynomial or
matrix-valued exterior `E_n(Y,u,Z)` may be paired with (3). More
generally (2) is a tensor factorization and preserves arbitrary
external arrays on BOTH the n and k ports when those ports are
retained. If an exterior depends on k, it stays attached to that
port; it cannot be deleted while using (3) with input v. This is
the ordinary typed local-contraction rule, not an assumed independence
of the physical underclock feedback.

The variable u records a literal internal-transfer fugacity. It does
not assert that the clocks or spectator arguments of an arbitrary
original knot are independent. Equation (2), rather than the special
value `u=1`, is the reusable bridge packet identity.
Here Y and u are central coefficient variables. Substituting
noncommuting boundary operators would require its actual ordered
intertwiner; the commutative identity does not authorize that step.

## 2. The universal Pascal transform and its inverse

The matrix P is N by N, triangular with unit diagonal, and depends
only on Q. Its explicit inverse is

    (P^(-1))_(n,k)=(-1)^(n-k) Q^((n-k)(n-k-1)/2)
                                  [n choose k]_Q, k<=n.     (4)

Indeed `[n choose j][j choose k]=[n choose k][n-k choose j-k]`;
the convolution in a product with (4) is `(1;Q)_(n-k)`, hence zero
unless `n=k`. This proves the inverse without a root-zero denominator.

Thus the packet move is not contraction to the unknown K_N and not
replacement by a rank-one co-source. It retains N independent boundary
channels. For any adjoining tensor A, changing packet coordinates
`f -> Pf` changes that tensor to `A P^(-1)`; their contraction is
exactly unchanged. This proves source-independent composition at
arbitrary width wherever the stated packet occurs. It makes no claim
that the transported tensor has small norm for arbitrary A.

Both P and its inverse have explicit finite coefficients. The map may
be exponentially conditioned; that conditioning is part of the
coherent metric, not an omitted norm cost.

### 2.1 These Pascal matrices are actual current operators

On an original balanced physical head write the lowering-generator
convention as

    mathsfF|a>=(1-Q^(a+1))|a+1>, mathsfF|d>=0.

Then `mathsfF^r[n,k]=F_n/F_k` for `n-k=r`. Consequently

    P=p_N(mathsfF), p_N(t)=sum_(r=0)^d t^r/F_r.        (4a)

Its inverse is the opposite finite Euler polynomial, reproducing
(4). This is a literal original nilpotent-current realization, not
an auxiliary matrix with only the same classical symbol.

At completeness let `Ecal|a>=(Q^(-a)-1)|a-1>` and
`U_a=Q^[-a(a+1)/2]`. The actual unitary chirp obeys

    U Ecal U^(-1)=mathsfF^T,
    P^T=U p_N(Ecal) U^(-1).                          (4b)

The same Pascal blocks occur in the ACTUAL two-head Borel fusion,
including every total integer degree. For `0<=T<=2d` set
`I_T={max(0,T-d),...,min(T,d)}`. Index the relative input by
`(a,T-a)` and the physical output by `(u,T-u)`, with `a,u in I_T`.
The proved physical fusion kernel is

    C_T[u,a]=x^(u-a) F_a F_(T-u)/(F_(a-u)F_(T-a)), u<=a,
             0 otherwise.

It factors EXACTLY as

    C_T=D_out,T (P|I_T)^T D_in,T,
    D_out,T[u]=x^u F_u F_(T-u),
    D_in,T[a]=x^(-a)/F_(T-a).                        (4c)

All indices of these factorials lie in `0,...,d`. The principal
interval `P|I_T` has the same explicit inverse (4) restricted to
that interval: every intermediate convolution index stays in it.
There is no omitted high-total-degree wrap, including `T>=N`.
This follows directly by writing
`F_a/(F_(a-u))=[a choose u]_Q F_u` in the actual fusion formula.

Thus (4c) supplies a typed current/physical embedding of the
Pascal move on arbitrary neighboring heads. Its diagonal factors
are compulsory. Nothing here silently identifies an arbitrary
fusion-relative clock with a physical head or with a chosen total
Ward current.

On the actual dual pair with total degree d this also checks the
original turns explicitly. In physical pair coordinates `(u,d-u)`,
write the original cup, ordinary cap and degree-d marked row as

    p_u=N x^(u-d), ell_u=x^(-u)Q^(-u)/N,
    m_u=x^(d-u)/N^2.

Then the SAME fusion block obeys

    C_d e_d=p, ell C_d=e_0^T/N,
    (m C_d)_a=x^(d-a) s_a^2/N^2.                    (4e)

The first is the a=d column of (4c). For the second, root reflection
reduces its a-th entry to `(1;Q)_a`; the marked row instead gives
`(Q;Q)_a`. Thus (4e) retains the full marked density, which is NOT
a corner row on arbitrary tensors. Its familiar further corner
reduction requires the actual invariant exterior Ward relation.
This note does not make that reduction for an arbitrary packet.

Finally `H=N G_0^2`, where `G_0=diag(s_a/sqrt(N))=L^(1/2)` is
the source-fixing physical factorial gauge. Hence (7) below is
exactly `G=N P^*G_0^2P`. If an actual current J commutes with the
nilpotent generator C and `S=p_N(C)`, then for ANY positive H_0,

    ||J||_(S^*H_0S)=||S J S^(-1)||_(H_0)=||J||_(H_0). (4d)

This is the useful current-compatible Gram mechanism. Applying
it to a total two-head current requires the actual typed module
identification and the commutation relation; (4a)--(4c) exhibit
the relevant possibilities, but do not assert that every clock
in a knot is simultaneously that same current.

## 3. The actual figure-eight Gram and controlled co-source

Now take the principal `Q=exp(2pi*i/N)`, put `s_n=|F_n|`, and set
`Y=u=1`. Define `v_k=(-1)^k Q^(k(k+1)/2)`. Equation (3) says

    Pv=F=(F_0,...,F_d)^T,
    C_n(1)=conj(F_n).                               (5)

The second equality is the exact identity
`conj(F_n)=(-1)^nQ^(-n(n+1)/2)F_n`. The original whole-source
calculation therefore gives, with its actual zero framing and all
Cartan/turn factors already accounted for,

    K_(4_1),N=C(1)^T P v=F^*F=sum_n s_n^2.           (6)

This normalization comes from the literal original four-plat source,
not from fitting (6) to a known value. Any separately attached original
modified-dimension germ multiplies both sides unchanged.

Let `H=diag(s_0^2,...,s_d^2)` and define the coherent packet metric

    G=P^* H P,
    G_(k,l)=sum_(n>=max(k,l)) s_n^2
                      conj([n choose k]_Q)[n choose l]_Q.    (7)

G is explicit and positive definite because every s_n is nonzero
and P is invertible. It has rank N, including the n=0 channel.
Its off-diagonal terms retain the q-binomial phases. In particular
it is not the diagonal absolute value of P.

The Riesz vector of the original linear co-source `C^T P` is
`a=P^*F`. Its squared dual norm in (7) is EXACTLY

    a^*G^(-1)a=F^*H^(-1)F=N.                        (8)

The actual packet energy is likewise explicit:

    ||v||_G^2=(Pv)^*H(Pv)=sum_(n=0)^d s_n^4.         (9)

Cauchy--Schwarz in this coherent, full-rank inner product proves
the original-source bound

    |K_(4_1),N|^2<=N sum_(n=0)^d s_n^4.              (10)

This is useful precisely because the co-source norm (8) is polynomial
while the state energy (9) retains the cancellation in each Pascal
fiber. It is not a norm estimate for every possible packet input.

## 4. Exact compatibility with the b-length frame, including length zero

Use the [actual length normalization](actual_length_normalized_star_gram.md)

    D_n=A_n^2=s_n^(1/2)/N^(1/4), b_n=B_n/D_n.

The row n of the coefficient tensor of b_n is the corresponding
Pascal row divided by D_n, with its original monomial phases.
Thus in that typed row frame the exact packet factorization is

    P_b=D^(-1)P, C_b=D C,
    C_b^T P_b v=C^T P v.                            (11)

Transport the positive row metric as well:

    H_b=D^2 H, P_b^*H_bP_b=G.                       (12)

The squared source dual norm remains N, and the energy remains
`sum s_n^4`. These are identities, not an asymptotic cancellation.
In particular `D_0=N^(-1/4)`, `b_0=N^(1/4)`; the row-zero factor
in `P_b` and its inverse factor in `C_b` are compulsory. Omitting
zero-length slots changes the original source.

Other length registers of an exterior are retained with their own
inverse frames, exactly as in the length-normalized star theorem.
Equation (11) normalizes the EXPOSED length n row and does not
identify its coefficient index k with a physical-head length.

## 5. The positive energy has the sharp exponent

For `J(t)=integral_0^t log(2sin(pi x))dx`, the elementary uniform
factorial estimate gives

    log s_n=N J(n/N)+O(log N), uniformly 0<=n<N.

J has its unique global maximum at `t=5/6`, and
`4pi J(5/6)=4Lambda(pi/6)=Vol(4_1)`.
Bounding the N-term positive sum by its maximum and using a nearest
integer to `5N/6` gives

    log(sum_n s_n^4)=N Vol(4_1)/pi+O(log N).          (13)

Thus (10) has exactly the desired sharp upper exponent. The positive
sum (6) separately gives the matching lower exponent. This recovers
the verified figure-eight benchmark by a genuine coherent Gram,
rather than by flattening its original overclock sectors.

The Gram here acts on the explicitly exposed split-transfer packet.
The much larger COMPLETE sectors in the three-braid clock state are
different coordinates, after different contractions. Equality of
their final scalar with (6) does NOT by itself provide an invertible
packet map between them. No diagonal-clock obstruction is evaded by
silently identifying those two spaces.

## 6. Exact composable updates and the remaining general question

If a specified invertible packet operator S acts before the packet,
the energy and Riesz vector on its INPUT coordinates update as

    G -> G_S=S^* G S, a -> a_S=S^*a,
    a_S^*G_S^(-1)a_S=a^*G^(-1)a.                    (14)

For a Gaussian clock chirp `U_ell=diag(Q^(ell*k(k+1)/2))`, this is
unitary congruence: its phases and the spectrum of G are retained.
For a pure coordinate change `v'=Sv`, rather than an inserted
operator, the unchanged pairing instead uses
`G'=(S^(-1))^*G S^(-1)` and `a'=(S^(-1))^*a`.
Likewise (4) permits exact Pascal/inverse-Pascal changes. These are
actual local tensor-coordinate operations with arbitrary retained
exteriors, not changes of the knot invariant.

They do NOT imply that the same simple factorial diagonal H survives
an arbitrary coherent word of such moves. A chirped input generally
has energy `sum s_n^2 |(P U_ell v)_n|^2`, not `sum s_n^4`.
The internal phase must be evaluated or controlled before its modulus
is taken. A known actual example is the Rogers coefficient packet
`J_n(t)=sum_k [n choose k]_t t^(k(k+1))`: it is exactly a Pascal
transform of a unitary Gaussian input, as proved from the original
[five-crossing whole source](five_two_cyclotomic_transform_proof.md).
Its remaining Newton evaluation is coherent; the
[multichannel proof](actual_multichannel_newton_green_transport.md)
already shows why a tame coefficient norm cannot simply be assumed.

The proved general local move is (2)--(4), with exact Gram transport
(11)--(14). A broad sharp theorem still requires (i) an actual
source-preserving decomposition into these packet moves and (ii) a
geometric bound on the resulting coherent energy, including all
spectator feedback and dual metrics. Neither condition is inferred
from the figure-eight benchmark alone.

### 6.1 An exact Pascal/Gaussian alphabet for original braid crossings

For the original SAME-COLOR braid there is a further explicit local
decomposition, at every integer total degree T. It resolves the
crossing into known coherent packet moves rather than assuming such
a decomposition. Use `C_T` from (4c), `I_T` as there, and define

    t_T[a]=x^(-a)/F_a,
    U_T[a',a]=x^(-(a'-a))/F_(a'-a) if a'>=a, else 0,
    D_T[a]=(-1)^(T-a) Q^((T-a)(T-a-1)/2) x^(-2(T-a)).

Then EXACTLY

    U_T=t_T (P|I_T) t_T^(-1),
    R_(+,T)=kappa C_T D_T U_T C_T^(-1),
    R_(-,T)=kappa^(-1) C_T U_T^(-1)D_T^(-1)C_T^(-1). (15)

Here kappa is the original common Cartan entry `R_(00,00)`, with
its given meridian continuation. It has not been reset. At completeness
`|x|=1`, both kappa and every D_T entry have modulus one. The other
diagonals in (4c),(15) retain their explicit factorial magnitudes and
root phases. The inverse of U_T is obtained from (4), so no unknown
diagonalization enters.

Proof with the strict physical support retained. In the actual flat
Borel basis `f^a e_j`, `a,j<N`, the original crossing is right
multiplication by the independently derived coefficient

    a_R=kappa sum_(r+k<N)
        (-1)^k Q^(k(k-1)/2) x^(-r-2k) f^r e_k/F_r.

That formula follows by the actual triangular fusion inversion on
`R(e_0 tensor e_j)=kappa x^(-j)e_j tensor e_0`; its finite Euler
inverse is precisely (4a). For an input `f^a e_j` the r,k term has
`j=k+r modulo N`, with output `f^(a+r)e_k` when `a+r<N`.
Within the SAME total INTEGER degree `T=a+j`, one must have
`j=k+r` as an integer, not `k+r-N`. Thus `a'=a+r`, `k=T-a'`,
and its coefficient is exactly `kappa D_T[a']U_T[a',a]`.
Conversely all the entries specified in (15) satisfy `r+k=j<N`,
so none is extra. Conjugation by the actual C_T proves (15).
In particular high blocks `T>=N` have been retained. No completed
positive-N carry or source-null approximation is used in (15).

Taking the direct sum over T gives the FULL original crossing as
an operator identity, with its literal negative inverse. Therefore
(4c),(15) can be inserted into an arbitrary signed braid of arbitrary
width, with arbitrary adjoining tensors. All ordinary/marked turns,
pivots, framing and peripheral factors stay original. The shared
head indices enforce the actual overlap/feedback of neighboring
total-degree registers; those T labels are not independent clocks.

This is an explicit coherent alphabet of principal Pascal blocks,
their inverses, known factorial diagonals and unitary Gaussians.
For a repeated-generator block its C_T interfaces cancel exactly
before any norm is taken. Neighboring generators generally have
different overlapping degree registers and leave genuine recoupling.
Their remaining positive energy is not estimated by (15) alone.

The fusion/Euler formulas themselves were previously proved in
[the actual Borel theorem](actual_borel_regular_fusion_and_divided_cap_period.md)
and [the original crossing coefficient theorem](actual_crossing_euler_completion_and_weight_source.md).
The use here is their exact integer-degree Pascal factorization,
its explicit coherent metrics and its retained original co-source.
It is not a claim that a generic R factorization is new, nor that
known factorial weights already satisfy the global Rivin constraints.

## 7. The precise overlap compatibility problem

There is a local sufficient metric condition for composing the
alphabet without defining a metric from the unknown terminal word.
Choose a family of positive packet metrics specified by LOCAL typed
data (Q, meridians, retained integer degrees and length ports), before
choosing the braid. It must include the explicit Pascal pullbacks
above, the intended positive factorial/angle row energies, and the
original turn co-sources with their controlled dual norms. For every
elementary THREE-head reassociation, let A be its actual finite
coordinate-change matrix. The required local compatibility is

    N^(-c) G_left <= A^* G_right A <= N^c G_left,       (16)

uniformly in all its admissible integer ports, for one fixed c.
Every diagonal factor in (4c),(15), and every required source adapter,
is included in A or in its explicitly assigned endpoint metric.
This is a finite local matrix inequality; its data do not involve K_N
or a terminal braid product.

If (16) holds, a fixed sequence of L reassociations compares the
state energies by `N^(cL)` and the transported source dual norms by
the same factor. This follows by congruence and inversion of (16),
then induction. Thus its Cauchy budget costs at most `N^(2cL)`.
The estimate tensorizes with untouched exterior heads. A positive
geometric angle-fiber factorization of the assigned row energies,
with the actual integer edge and peripheral constraints, would then
give the desired comparison to its partition function up to a
polynomial. That last identification is an explicit requirement,
not a consequence of (16) alone.

Using exact pullbacks of ONE arbitrary physical metric makes tree
coordinate changes isometric tautologically, but does not establish
that the resulting dense Gram has the stated positive-angle energy.
The problem is to obtain BOTH the controlled local energy model and
the compatible overlaps, with the same retained source. It cannot be
solved by defining G from the unknown completed word.

### The obvious fixed factorial tensor metric fails (16)

This failure can be proved on the ACTUAL fusion reassociation, after
removing its trivial column factorial. Put

    C'=C diag_(a,k)(F_a^(-1)),
    A=(I tensor C')^(-1)(C' tensor I) on three heads.  (17)

This is the genuine change from the first-pair divided-power fusion
coordinates to the second-pair coordinates. All its original turns
are transported by the same matrices; the assertion is a local
all-exterior norm test, not a knot scalar estimate.

At total pair degree d, (4c) and reflection give

    C'_d=V (P^T) V^(-1),
    V_a=x^a(-1)^aQ^(a(a+1)/2), |V_a|=1.             (18)

An input `|0,u,d-u>` is fixed by the first-pair C', because its
first relative divided-power index is zero. Hence

    |<0,a,d-a| A |0,u,d-u>|=|[u choose a]_Q|,
                                           0<=a<=u<=d.     (19)

Now use ANY fixed positive diagonal tensor metric whose last two
head weights have constant complementary product
`h_2(a)h_3(d-a)=constant`. In particular every fixed physical
factorial metric `(L^t)^(tensor 3)` has this property. The input
and output basis vectors in (19) have equal metric norm. Therefore
its induced operator norm satisfies

    ||A|| >= |[u choose a]_Q|.                       (20)

For `N=3k+1`, `u=2k`, `a=k`, the uniform factorial estimate gives

    lim (1/N)log|[2k choose k]_Q|=v_3/pi>0.          (21)

Thus (16) with the SAME fixed factorial tensor metric on both
coordinate systems is false, even after the column factorial has
been removed and even before any unknown braid is present.
Its complementary source property does not imply tame reassociation.

This does not rule out the coherent family sought in (16), an
angle-weighted recoupling rather than a tame one, or a source-specific
smaller invariant packet. It pinpoints the next required estimate:
the overlap of the actual Pascal packets needs its OWN coherent
Gram/angle factorization. Flat or fixed diagonal factorial gluing
cannot silently replace it.

The interface is already an EXACT positive affine-angle weight:
root complementation gives

    |[u choose a]_Q|=N w_N(a,u-a,d-u),
    a+(u-a)+(d-u)=d.                                (22)

Thus its squared matrix coefficient is `N^2 w_N(a,u-a,d-u)^2`.
The test (21) has the regular-angle triple `(k,k,k)`; its exponential
cost is genuine tetrahedral angle energy to be allocated and glued,
not an unexplained norm loss. A coherent global comparison may retain
these weights or change their Gram placement. It must prove their
actual incidence and dual/source compensation rather than omit them.

[Audit](../experiments/audit_actual_pascal_coherent_gram.py): original
mixed E/F four-plat contractions, arbitrary Y/u local packets and
exterior insertions, exact Pascal inverses, full positive Gram/source
normalization, b_0, the sharp positive-energy rate, and both original
signed crossings in every total-degree block with full pivotal words.
The final tests also check the actual three-head reassociation and
its fixed-factorial metric obstruction (19)--(21).
