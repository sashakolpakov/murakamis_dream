# A terminal coherent packet gives a positive Gram on the complete original module

29 October 2026. A sharp packet norm need not be diagonal in complete
Casimir channels, and its defining packet map need not be invertible.
This note constructs a positive Gram on the SAME complete source module
used by the original braid representation. It comes from a specified
two-crossing terminal tangle, independently of the preceding word.
For the original figure-eight prefix its energy has the sharp volume
exponent. The construction extends as a source-exact Cauchy construction
to arbitrary plat width; a sharp bound on its energy for general
prefixes is NOT proved.

## 1. A positive completion of a coherent packet seminorm

Let H be a finite-dimensional state space with fixed Euclidean norm.
Suppose a prescribed boundary row factors as a=1^T T, where
T:H->C^s is an EXPLICIT linear packet map. For any epsilon>0 set

    G_epsilon=T^*T+epsilon I.                              (1)

This is positive definite even if T has a kernel. Its boundary cost is

    a G_epsilon^(-1) a^*<=s.                              (2)

Indeed T(T^*T+epsilon I)^(-1)T^* has eigenvalues
sigma^2/(sigma^2+epsilon)<=1, by singular-value decomposition.
Apply it to the vector of s ones. Thus for every input w,

    |a w|^2<=s [sum_n |T_n w|^2+epsilon ||w||^2].          (3)

The seminorm inequality without epsilon is also exact, by ordinary
Cauchy in C^s. Equation (1) makes it a genuine positive inner product
on the full original state space; it neither discards a channel nor
asserts that the kernel of T is invariant under preceding braids.

Use epsilon_N=exp(-N^2). If ||w_N||^2<=exp(C N log N) for a fixed
word, its added energy is superexponentially small. No unknown knot
value is used to choose epsilon. This completion is useful only when
T is specified from a limited terminal packet and its coherent energy
is independently estimable. Taking T to be the unknown entire closed
period would give no new bound.

## 2. The complete original module and a specified terminal packet

Use N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, F_a=(Q;Q)_a.
All original Ecal,F,K, coproducts, full Cartan factors and sources
are those in the [complete multiplicity theorem](actual_complete_source_multiplicity_module.md).
Let W=(V tensor V)_(degree d), and write I_w:V->V^tensor3 for
its complete intertwiner. Its lowest input column is the explicit map

    D w=I_w|d>=F_123^d H_L(w)/F_d,
    H_L(w)=sum_c (-xQ)^c E_12^c w/F_c tensor |c>.          (4)

This retains all N multiplicities and their full intermediate Jordan
channels. The ordinary cap is the original row ell and the cup is p.
Define the physical final row and terminal operator by

    c_top=ell_12 tensor <d|,
    U_phys=I tensor R_+^2,
    U=R_23^2 on W.                                      (5)

R_+ is the literal original checked crossing INCLUDING its common
Cartan factor. Let Pi_n project the middle physical head to color n,
with the other two heads untouched. Define the N-row packet

    T_n(w)=c_top U_phys Pi_n D w, 0<=n<N.                 (6)

Every object in (4)--(6) is fixed before a preceding braid is supplied.
In particular this does not use a closed knot value to choose a basis.
Summing the physical resolution of identity gives exactly

    sum_n T_n=ell U.                                    (7)

To verify the last equality, the complete intertwiner theorem gives
U_phys I_w=I_(Uw); closing its first two heads gives
(ell tensor I)I_(Uw)=ell(Uw) I_V. Its input/output d entry is (7).
This uses the actual whole source and its Hopf closure, not a
replacement of an arbitrary marked row by an ordinary cap.

For ANY original prefix B the unchanged closed scalar is therefore

    K_N=chi_N ell U Bp=chi_N sum_n T_n(Bp).                (8)

All original external factors remain in chi_N. The specified full
marked closure is justified by the complete invariant-tensor theorem;
arbitrary nonintertwining inserted exteriors retain their own source.

Equations (1)--(3), with s=N, give a positive metric on the prefix cut.
One can put it on the final complete module as well:

    G_final=U^(-*) (T^*T+epsilon_N I) U^(-1).             (9)

It obeys ell G_final^(-1)ell^*<=N. For the actual final state
v=chi_N U Bp its energy is exactly

    v^*G_final v=|chi_N|^2
                   [sum_n |T_n(Bp)|^2+epsilon_N||Bp||^2]. (10)

Thus this is a full-rank positive Gram on the SAME complete module
as the Casimir metric. It does not identify two differently contracted
scalar formulas without an actual linear map. No claim of invertibility
of T is needed, at prime, even, or composite levels.

## 3. The actual figure-eight prefix has the sharp packet energy

Take the literal prefix B=R_12^(-1)R_23. With the terminal U of (5),
the full action order is [2,-1,2,2], the original zero-framed
four-plat in the [whole-source proof](figure_eight_whole_source_identity.md).
Its finite forced-transfer calculation can be kept open at the middle
physical color n AFTER the second crossing. The initial lowest column
I_p|d> is p tensor |d>. After the first two crossings the physical
state is (d-k,a+k,d-a), so that n=a+k is precisely the projector
index in (6), not a new auxiliary label. The final two crossings and
the actual caps force their transfers to a and 0, respectively.

Consequently the proof there, retaining its full Cartan and boundary
factors, gives the ROW-BY-ROW identity

    T_n(Bp)=sum_(k=0)^n [n choose k]_Q
                            (Q;Q)_k (Q^(-n);Q)_(n-k)
            =(-1)^n Q^[-n(n+1)/2] F_n^2
            =|F_n|^2.                                 (11)

For the middle equality, reverse the last Pochhammer product and use
the finite q-binomial identity; all factorial indices are below N.
This is an exact statement about the uncontracted terminal packet on
the complete module, not just equality after summing n. The original
zero-framing normalization has chi_N=1 for this benchmark.

Therefore (10) is

    E_final=sum_(n<N)|F_n|^4+exp(-N^2)||R_12^(-1)R_23p||^2.

The uniform sine-factorial estimate proved in the packet note gives

    log(sum_(n<N)|F_n|^4)=N Vol(4_1)/pi+O(log N).          (12)

The last term is superexponentially small by Section 4 below. Thus
this ACTUAL complete-module positive metric has the sharp energy rate.
It mixes distinct Casimir channels; it is not a positive diagonal
reweighting of their separate squared amplitudes.

The estimate is reusable for every prefix with this fixed terminal
tangle, but equation (11) is special to the displayed prefix.
For another knot the full coherent quantities T_n(Bp) must be bounded;
replacing them by sums of absolute values is not authorized.

## 4. The regularizer is negligible for fixed original braid words

At the principal root, for 1<=j<N,

    4/N<=|1-Q^j|<=2.

Every original balanced signed crossing coefficient is a monomial
of modulus one times a bounded number of factorial/Pochhammer ratios,
each of length at most N-1. The explicit signed formulas therefore
bound its logarithmic magnitude above by C N log N. A physical
crossing has at most polynomially many entries at fixed braid width,
so the same order bound holds for its operator norm.

For a fixed prefix acting on the odd heads, the highest vector of the
initial source is p tensor |0> (and p^tensor r tensor |0> at larger
width), of polynomial norm. Apply its fixed number of physical signed
crossings and extract the last color0 coefficient. This extraction
IS the complete multiplicity inverse and has norm one. For an arbitrary
EVEN-plat prefix, including crossings of the last marked partner, use
the original invariant bottom p^tensor(r+1) instead. Its complete
multiplicity inverse is (x^d/N) times extraction of the last TWO colors
(0,d), as proved in the invariant-tensor source theorem. Both the
initial norm and extraction cost are polynomial. These arguments prove

    ||B p||^2<=exp(C_B N log N),                         (13)

and the same statement for the full all-width initial source.
No ill-conditioned eigenframe or unestimated reduced inverse enters
this proof. Equation (13) is a coarse original-source bound used only
to control the regularizer; it is not offered as a volume estimate.

## 5. All-width extension and the remaining sharp theorem

For 2k heads, r=k-1, let W_r and I_w:V->V^tensor(2r+1) be the
complete original multiplicities. Put D_r w=I_w|d>,
c_top=ell^tensor r tensor <d| and lambda=ell^tensor r.
For a specified terminal braid U_phys on these odd heads and ANY
specified mutually orthogonal physical-color projectors Pi_a summing
to identity, set

    T_a=c_top U_phys Pi_a D_r.

Exactly the same complete intertwiner calculation proves
sum_a T_a=lambda U_red. Choosing a fixed number s of physical heads
to record gives N^s packets and a dual norm at most N^s in (1).
The literal last marked cap and all original normalizations are
retained by the all-width invariant-tensor source theorem. This
construction is valid for every preceding signed braid and at all N.

The unresolved geometric problem is now the coherent estimate

    |chi_N|^2 sum_a |T_a(B w_0)|^2
                         <=exp(o(N)) Z_N(geometric angles). (14)

This note proves the sharp energy rate (12) for the original figure-eight
benchmark and provides a genuine complete-module realization of its
sharp Gram. Comparison (14) then follows for any of the already proved
positive geometric partitions with that same volume rate.
It does not prove (14) for a broad knot class, or prove broad geometric
survival. The new structural point is that a controlled physical
terminal contraction can define the metric; an invertible global
spectral frame is not required to do so.

[Audit](../experiments/audit_actual_terminal_packet_positive_gram.py)
constructs the entire highest/lowest intertwiner, original signed
crossings and the terminal physical projector rows independently of
(11). It checks all rows, every input column of (7), and the
positive-completion inequality on unrelated state vectors.

The finite tests compare complete terminal modules, figure-eight packet families and positive full-module Grams. The proof keeps the full common Cartan scalar and uses the full even-plat inverse in its regularizer.