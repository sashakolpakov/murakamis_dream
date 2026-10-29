# The divided adjoint pairs nontrivially with the actual missing edge

Research proof, 27 October 2026. The genuine complete integral Weyl
color gives a divided Hopf-adjoint operator on its matrix space.
Applied to the literal missing cyclic edge, it has an exact nonzero
pairing with the prescribed marked cut. This yields a cohomologous
divided-normal realization of the original knot cut functional.
It does not prove survival of the geometric Gaussian period.

## 1. The two normal directions are distinct

Keep `Q=q^2`, `x=-M/q`. In the balanced basis the generic truncated
raising entries are

    Ecal_(a-1,a)=M Q^(-a)-M^(-1),       1<=a<N.

The absent cyclic entry is the specified coefficient

    w(q,M)=M Q^(-N)-M^(-1),
    W=E_(N-1,0).

It vanishes identically on the genuine integral Weyl color
`M=-q^N`. At the fixed root `Q^N=1` it becomes
`w=kappa=M-M^(-1)`. These two restrictions are different normal
directions. If `delta=1-Q^N`, their exact relation is

    w=kappa+M delta/(1-delta).

At the complete intersection `M=1,delta=0`, one has
`dw=d kappa+d delta`; the Weyl curve is `w=0`, not `kappa=0`.
No tensor divided power below is identified with the generic-M
cyclic-edge normal by replacing one parameter with the other.

## 2. The actual divided Hopf adjoint

Take the genuine Weyl family `V(q)=D_(N-1)(q)` on `M=-q^N`, as in
[the factorial fusion proof](divided_ward_factorial_fusion.md).
For a matrix `T` its actual generic Hopf adjoint is

    A(T)=ad_Ecal(T)=[Ecal,T]K^(-1).

Write `A=X+Y`, with

    X(T)=Ecal T K^(-1), Y(T)=-T Ecal K^(-1).

Then `XY=Q YX` and `X^N=Y^N=0` for every generic `q`. Hence the
same q-binomial cancellation as for the tensor divided power defines
a regular actual operator on the root matrix space:

    J_ad=[A^N/(1-Q^N)]_(q=q_N)
        =sum_(j=1)^(N-1) c_j Y^(N-j)X^j,
    c_j=N/[(Q;Q)_j(Q;Q)_(N-j)].                  (1)

This is the divided **Hopf** adjoint. It need not equal ordinary
commutation by the divided power on `V`; that latter power is zero
on the individual color. Formula (1) retains the mixed antipode
terms acting through `V tensor V*`.

## 3. Exact action on the missing edge

At the actual root set

    epsilon_a=Q^(-a)-1, P_a=product_(s=1)^a epsilon_s,
    P_(N-1)=(-1)^(N-1)N,
    K^N=(-1)^(N-1)I.

Let `l=N-j`. The `j`-th term of (1) applied to `W=E_(N-1,0)`
is supported only at matrix entry `(l-1,l)`. Its coefficient is

    c_j (-1)^l Q^(-l(l-1)/2-jl)
                       P_(N-1) epsilon_l K^(-N).

Using

    c_j=c_l=(-1)^(l-1)Q^(-l(l-1)/2)/(1-Q^l),
    epsilon_l=(1-Q^l)Q^(-l),

and `Q^N=1`, every coefficient simplifies to `-N`. Therefore

    J_ad(W)=-N sum_(l=1)^(N-1) E_(l-1,l).          (2)

This holds for every `N>=2`, with the original balanced root basis.
For the literal marked source and co-source,

    e_(a,b)=1/N, Phi(T)=Tr(eT)=Tr(g D T),

equation (2) gives the exact nonzero pairing

    Phi(J_ad(W))=-(N-1).                          (3)

The normalized ordinary trace of (2) is zero. Thus the marked
normal pairing is visible before the ordinary scalar Ward quotient.
Its degrees are explicit: `W` raises matrix index by `N-1`,
`J_ad` lowers it by `N`, and the marked cut supplies the remaining
one-step pairing. This is a mixed divided-normal/missing-edge
cochain calculation, not a nonzero closed geometric class.

## 4. An actual cohomologous divided-normal cut

Define the literal all-matrices row

    Phi_div(T)=-Phi(J_ad(T W))/(N-1).              (4)

Equation (3) says `Phi_div(I)=1`. Let
`delta_W(T)=([K,T],[F,T])` and let `h_W` be the explicit actual
Ward contraction in
[the finite Ward note](actual_borel_ward_cut_contraction.md), so

    h_W delta_W=I-i p,
    p(T)=Tr(T)/N, i(c)=c I.

Since `(Phi_div-Phi)i=0`, one obtains the exact cochain homotopy
on **all** matrices,

    Phi_div-Phi=(Phi_div-Phi)h_W delta_W.          (5)

In particular every actual closed cut tangle is Ward closed, hence
equals `F_N(1) I`. Equations (4)--(5) give

    Phi_div(C_K)=Phi(C_K)=F_N(1)=Kashaev_N(K).     (6)

Thus (4) is an explicit divided-normal source realization of the
original invariant, with its source and normalization fixed. It is
not a new invariant or a redefinition of its numerical values.
The full ADO value retains the entire external marked line; at
completion it multiplies (6) by `i^(N+3)/N`. That scalar is not
absorbed into (4).

## 5. Pivotal partial trace commutes with the genuine divided adjoint

For the genuine generic integral colors use the generic pivotal
partial trace

    ptr_K(T)=Tr_closed[(I tensor K_closed)T].

The generic Hopf adjoint and this trace commute on every matrix.
This follows from the ordinary antipode cancellation; equivalently
the generic pivotal cap is a Hopf map. Apply the generic identity
to the `N`-th adjoint power and divide both sides by `1-Q^N`.
The divided operators are regular by the q-binomial argument on
the corresponding tensor-and-dual colors. Specialization gives

    ptr_K J_ad,total=J_ad,cut ptr_K.               (7)

At the root, the actual pivot satisfies
`g_closed=K_closed^(1-N)=chi_closed^(-1)K_closed`, where the
entire scalar `chi_closed=K_closed^N` is retained. Thus (7) holds
also for the original actual pivotal partial trace `ptr_g`.

The order of the marked edge matters. For an arbitrary full tensor
matrix `T`, the cut edge lifts as `W_cut tensor I_closed`, so the
exact all-matrices identity is

    Phi_div(ptr_g T)
      =-Phi(ptr_g[J_ad,total(T(W_cut tensor I))])/(N-1). (8)

Here `ptr_g(T(W_cut tensor I))=(ptr_g T)W_cut` was used. There is
no license to replace the argument of `J_ad,total` by `T` and
move the edge unchanged outside it. The mixed Hopf-adjoint terms
are essential. Equations (7)--(8) transport the new source through
the actual contraction while keeping its insertion order.

## 6. What this proves about cohomology and HPL

The action `J_ad` lowers matrix weight by `N`, so its square is
zero on `End(V_N)`. It annihilates `I` and has zero normalized
ordinary trace on every matrix. It consequently induces a chain
map on the split image Ward complex: set

    J_ad^1(delta_W T)=delta_W(J_ad T).

This is well defined because the kernel of `delta_W` is `k I`
and `J_ad(I)=0`. Its action on scalar Ward cohomology is zero.
Likewise the marked row `Phi J_ad` is Ward exact, by composing the
old cut homotopy with this chain map. This is consistent with the
nonzero cochain pairing (3): the missing edge is not Ward closed.

The normalized row (4), in contrast, has the same **nonzero**
cohomology class as the original cut, by (5). It is now represented
using a genuine divided adjoint and the literal missing edge.
This gives concrete source data for a future source-preserving
Gaussian chain comparison. It does not construct that comparison
or show which geometric formal class has nonzero image. Nilpotence
of an inserted operator and exact scalar Ward normalization alone
do not supply the missing HPL map or an asymptotic volume theorem.

[Exact audit](../experiments/audit_divided_ward_factorial_fusion.py)
and [results](../experiments/divided_ward_factorial_fusion_results.json)
check (2)--(5) on every matrix unit at seven levels and verify the
all-matrices pivotal and ordered-insertion identities (7)--(8).
