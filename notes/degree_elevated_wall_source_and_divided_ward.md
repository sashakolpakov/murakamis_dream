# The elevated wall source is not supplied by the finite divided-Ward orbit

Research proof and two exact tests, 27 October 2026. The binomial
wall co-source has a literal realization on the degree-N symmetric
power of the already proved divided-source standard module. That
realization does not automatically carry the true divided Hopf
coproduct. A finite-head weight bound rules out a full SL2-equivariant
embedding at fixed bridge number and large N. The most immediate
q-binomial elevation also fails a bounded diagonal comparison.

These are precise restrictions on proposed constructions, not a
claim that a linear relative B1 current map is impossible. An
explicit weighted stabilization shows why its second transfer
coordinate needs an actual network map in addition to a cut orbit.

The later [actual high-color construction](high_integral_color_frobenius_wall_source.md)
evades the fixed-head dimension restriction explicitly. Integral color
N(N+1) carries the required Sym^N divided multiplicity, its coherent
row is exactly B_N, and its root knot scalar equals K_N with all
braiding/peripheral signs retained. Its normal block arrows are actual
regularized entries of E,F. This is a source enlargement, not a
contradiction to the fixed-head nilpotence bound. Its full divided
coproduct/current map and the geometric source projection remain
separate requirements.

## 1. The actual wall row and its literal tensor-source realization

The [cut-current theorem](actual_gauss_wall_cut_current_complex.md)
gives

    B_N(J)=[1/(N2^N)]sum_(j=0)^N binom(N,j)J_j.             (1)

J here has the matrix normalization of equation (14a) in the
cut-current note. Original raw Green arrays use N B_N instead;
that coefficient is retained.

Use the actual two-dimensional divided-source subspace

    L=span(Ubar,W), Ubar=(sum E_(j,j+1))/(N-1),
    W=E_(N-1,0), Phi(Ubar)=Phi(W)=1/N.

On L the explicitly proved normalized divided Hopf adjoints
are the standard SL2 matrices e,f,h. Let M_j be the sum of the
distinct tensors with j copies of W and N-j copies of Ubar.
Then the literal coupon row

    ell=((N/2)Phi)^(tensor N)

satisfies `ell(M_j)=binom(N,j)/2^N`. Hence

    B_N(J)=(1/N)ell(sum_j J_j M_j).                       (2)

This is an exact source pairing. The primitive tensor SL2 action
induced from L makes their span Sym^N L, with a highest string
of length N+1.

That primitive action is not automatically the true global
divided Hopf adjoint on the tensor-source network. Its coproduct
contains the mixed ordinary divided powers already computed
in the actual fusion theorem. Equation (2) does not discard
those terms, nor prove a monoidal Ward intertwiner.

## 2. A fixed-head equivariance obstruction

On H=V_N^(tensor b) retain the ordinary integer position grading.
For a matrix unit indexed by an output tuple r and input tuple s,
its matrix weight is `sum r_i-sum s_i`, in

    -b(N-1)<=weight<=b(N-1).

The true E Hopf adjoint decreases this weight by one. Therefore
its degree-N divided-normal operator J_E decreases it by N;
normal division changes the coefficient, not the support degree.
It follows exactly that

    (J_E)^(2b)=0 on End(H).                               (3)

On Sym^N L, by contrast, `e^(2b)` is nonzero when N>=2b.
Consequently there is no nonzero full-SL2-equivariant map
of Sym^N L into this finite-head adjoint space intertwining
its e with the actual normalized J_E when N>=2b. Indeed such
a map is injective: the standard highest-weight polynomial
module Sym^N L is irreducible in characteristic zero, as is
seen by raising a nonzero highest weight term and then applying
the lowering operator. Equation (3) contradicts injectivity.

The same argument applies to a proposed nonzero full-SL2
intertwiner into any subquotient with this same weight bound.
It does not rule out a non-equivariant linear current map,
a Borel-only quotient, an enlarged normal/tail complex, or a
source involving a number of additional factors growing with N.
It identifies the additional sector a full equivariant construction
would have to supply.

## 3. The first divided q-binomial row has a different whole-head lattice

At Q=Q_N, all middle coefficients of `{N choose j}_Q` vanish.
Their exact first divided-normal values are

    d_(N,j)=[{N choose j}_Q/(1-Q^N)]_(Q=Q_N)
      =N/[(Q_N;Q_N)_j(Q_N;Q_N)_(N-j)]
      =(-1)^(j-1)Q_N^[-j(j-1)/2]/(1-Q_N^j), 0<j<N.        (4)

The proof cancels the single numerator factor 1-Q^N before
specialization and then pairs the complementary root factors.
In particular `|d_(N,j)|=1/[2sin(pi j/N)]`.

If the degree-zero endpoint coefficients 1 and the degree-one
middle coefficients (4) are put in the same trial source row,
the result is `(1,d_1,...,d_(N-1),1)`. This statement specifies
the trial Rees identification: it does not identify its two
normal degrees by an unproved map.

A diagonal adapter to the ordinary row
`(binom(N,0),...,binom(N,N))` has endpoint entry one and
middle entries `binom(N,j)/d_(N,j)`. Its condition number in
every common diagonal metric is at least

    2^(N+1)/(N+1), N even,
    sqrt(3)2^N/(N+1), N odd>=3.                           (5)

Choose a central coefficient, which is at least 2^N/(N+1),
and use `2sin(pi j/N)>=sqrt(3)` (equal to 2 at even N).
The endpoint-to-center ratio proves (5). Overall row
normalization does not remove this condition number.

Thus the most immediate q-binomial/Frobenius elevation is not
the bounded full-head Gamma unit already proved at source
degree N-1. A higher normal extension or a different linear
current map might still repair it. Simply replacing classical
binomial weights by the first divided q-binomial weights would
change the actual co-source.

## 4. An actual weighted stabilization does not give a second cut Weyl identity

There is a small universal test using the literal crossing,
rather than an arbitrary array. Set N=2, q=i, Q=-1, M=1,
x=i. Take a positive Markov stabilization, whose new crossing
transfer is k, and attach a weight w^k. Its full root framing
and pivot normalization has kappa_D=0. The two cut diagonal
entries, computed directly from the actual finite coefficients,
are

    C_0(w)=1, C_1(w)=2w-1.                               (6)

For the second entry the routes are `(i,j,k)=(1,0,1)` and
`(1,1,0)`, with their complete normalized weights 2w and -1.
The zeroth entry has the single route `(0,0,0)` with weight 1.
Thus the original normalized cut gives exactly w; at w=1
this is the correct identity tangle after the twist correction.

For a preceding scalar knot cut F I, this local operation gives
F times (6). Therefore the transfer distribution after the
normalized cut is `(0,F)`. Its unnormalized transfer sum is F.
Encoding that sum by a two-dimensional auxiliary diagonal source
means the matrix diag(0,2F). The two hemisphere co-sources of
that transfer source are then

    lambda_2^+=F/4, lambda_2^-=3F/4.                     (7)

They are not the two equal cut values F/2. This is an exact
universal local stabilization test, not a knot-by-knot argument.
It shows that applying a second auxiliary Bernstein reflection
to a transfer index is not already the actual cut Weyl identity.
The original unweighted invariant remains unchanged.

This does not rule out an adapted second framing coordinate
on a hyperbolic geometric chart: the new stabilization transfer
need not be etale on that critical framing torsor. It proves
that such an identification must use its actual network and
current equations; it cannot follow from the one-cut source
orbit or its two Weyl charts alone.

The concrete next map must therefore transport the degree-N
wall row (1), the two actual cut endpoints, and the second
network framing current together, possibly in a normal/tail
extension. The finite cut-current chain map is already explicit.
No selected geometric cycle, global microstalk or volume limit
is asserted here.

Verification is recorded in
[audit_degree_elevated_wall_source.py](../experiments/audit_degree_elevated_wall_source.py)
and its
[results](../experiments/degree_elevated_wall_source_results.json).
The coupon and stabilization tests are exact rational-complex
matrix calculations. The divided q-row formula and conditioning
bound are checked at 80-digit precision for N=2 through 32;
their general proof is the finite product cancellation (4).
No kernel of the full knot network or selected volume limit
is inferred from these tests.
