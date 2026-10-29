# The whole Verma crossing on the cyclic Rees source

Research proof, 27 October 2026. The actual Verma R-factor has an
exact operator factorization after the irregular Rees transformation:
a regular norm-one cyclic matrix factor and a specified resonant
quantum period. Together with the actual Cartan factor, the latter
carries the nontrivial classical holonomy transport. The original
head source and every internal head projector are transported
explicitly and remain irregular. No regular same-fiber full cyclic
R matrix or selected geometric period is inferred.

## 1. The exact transformed crossing and its ramified factors

Use the genuine balanced common Verma crossing with its full marked
Cartan factor retained:

    R=D Theta, Theta=P_Q(q Ecal_1 F_2),
    log P_Q(z)=-sum_(m>=1) z^m/[m(1-Q^m)].

The nilpotent series terminates on every original fixed total-index
sector before transformation. For its transformed functional
calculus, introduce a central bookkeeping parameter `t` and work
coefficientwise in `t`; no convergence assertion is required.

Set `d=N(Q^N-1)`, choose one common marked root `eta^N=d`, and
take the two actual Rees transformations

    C_i=D_eta exp(-p_i u_i/d), D_eta h_j=eta^j h_j,
    Ehat_i=eta C_i Ecal_i C_i^(-1),
    Fhat_i=eta^(-1) C_i F_i C_i^(-1),
    Khat_i=C_i K_i C_i^(-1).

The nonzero momenta `p_i` are not required to coincide. The module
theorem proves regularity of these operator coefficients and gives
their full cyclic root values. Since the same Hopf scale is used
on both factors, its eta factors cancel in the R argument. Thus
the exact transformed operator is

    Rhat=Dhat P_Q(Zhat),
    Zhat=q Ehat_1 Fhat_2,
    Dhat=(C_1 tensor C_2)D(C_1 tensor C_2)^(-1).   (1)

Independent choices `eta_i` instead insert the explicit ratio
`eta_2/eta_1` in `Zhat`. Its N-th power is one, but its cyclic
phase is retained; it is not reset after specialization.

## 2. Exact resonance separation before taking any root value

Let `W=Zhat^N`. Split the logarithmic series into indices divisible
and not divisible by `N`. This gives the exact operator identity

    P_Q(t Zhat)=C_Q(t Zhat) R_res,Q(t^N W),
    log C_Q(z)=-sum_(N not dividing m) z^m/[m(1-Q^m)],
    R_res,Q(w)=P_(Q^N)(w)^(1/N).                (2)

Both factors are functions of the **same** operator, hence commute.
Their logarithms and fractional roots are marked by constant one
at `t=0`. Equation (2) follows by comparing each coefficient; its
resonant coefficient is

    -(1/N) w^k/[k(1-(Q^N)^k)].

No value of a divergent infinite factor at a root has been assigned.
The first factor is regular in the root normal coefficientwise in
`t`, because each denominator with `N` not dividing `m` is a unit
and `Zhat` is a regular Rees operator.

The exact functional equation also separates:

    C_Q(Qz)/C_Q(z)=(1-z)^(-1)(1-z^N)^(1/N),
    R_res,Q((Qz)^N)/R_res,Q(z^N)=(1-z^N)^(-1/N). (3)

Their product is precisely the original Pochhammer transport.
This retains the whole central divisor, rather than replacing it
by a numerical factor at an ideal source.

## 3. The regular root factor is the actual marked cyclic dilogarithm

At the root write `Z_0` for the cyclic matrix symbol of `Zhat`, and
put

    k_i=Khat_i^N, e_i=Ehat_i^N, f_i=Fhat_i^N,
    X=Z_0^N=-e_1 f_2.

Here `q_N^N=-1` fixes the sign. Let

    nu=(1-t^N X)^(1/N),
    D_N(t Z_0)=product_(j=1)^(N-1)(1-Q_N^j t Z_0)^(j/N),
    g_D(t Z_0)=D_N(t Z_0)/nu^((N-1)/2).

All powers use the common mark at `t=0`. Weighted root summation
in the logarithm gives exactly

    C_(Q_N)(t Z_0)=g_D(t Z_0)^(-1).               (4)

For nonresonant degrees the logarithms agree coefficient by
coefficient. For resonant degrees the `nu` normalization cancels
the resonant part of `log D_N`. This proves (4) for even and
composite `N` as well as odd `N`.

On the cyclic algebra with generator `z^N=t^N X`, the norm of
`g_D` is one: the deck sum of its logarithm vanishes. On the
generic N-squared-dimensional pair matrix space each cyclic
eigenvalue occurs N times, so its matrix determinant is also one.
These are marked equalities, not permissions to choose a new
root of unity phase. Algebraic continuation away from `1-t^N X=0`
keeps this root cover and its marking.

When `X=0`, equation (3) and constant term one determine the
nilpotent factor coefficient by coefficient through degree `N-1`.
It is exactly the original finite factorial in the actual R.
Thus the finite cyclic factor is anchored to the literature state
at the nilpotent source; it has not been independently normalized.

## 4. The resonant factor is a quantum period, not a regular scalar

For a scalar commuting argument `w` independent of the normal,
equation (2) gives, with `d=N(Q^N-1)`,

    log R_res,Q(w)
      =Li_2(w)/d+[Li_2(w)+Log(1-w)]/(2N)+O(d).    (5)

Indeed for `Q^N=1+epsilon`,
`1/(1-(1+epsilon)^k)=-1/(k epsilon)+(k-1)/(2k)+O(epsilon)`.
For the logarithmic normal `d_log=N Log(Q^N)` the same formula is

    log R_res,Q(w)=Li_2(w)/d_log+Log(1-w)/(2N)+O(d_log).

The finite `Li_2/(2N)` adapter is therefore necessary when using
the actual linear Rees normal. For the operator `W(d)` the whole
factor in (2) is retained: its lift and noncommutative normal terms
can alter its finite part. Only its leading symbol is
`Li_2(t^N X)/d`.

This fixes the local dilogarithm phase from the actual whole
factorial and its zero mark. It does not select a knot fundamental
class, a global branch, or a dominant exponential. The normal `d`
is not the physical large-level parameter `2pi*i/N`.

## 5. Leading cyclic-center transport is the characteristic braiding

The generic conjugation formulas of the whole universal R are
rational after the Pochhammer functional equation is used. They
therefore apply to (1). The Rees operators entering them are
regular. On the chart where the full divisor is a unit, their
root values give the exact center transport below.

With the fixed multiplication order define

    v=q_N Ehat_1 Khat_1^(-1)Khat_2 Fhat_2,
    v^N=-e_1 f_2 k_2/k_1,
    D_c=1-v^N=1+e_1 f_2 k_2/k_1.

The powers follow by ordered multiplication, including the two
factors `Q_N^(N(N-1)/2)=(-1)^(N-1)` and `q_N^N=-1`.
The uncheck center pullback is

    k'_1=k_1 D_c, k'_2=k_2/D_c,
    e'_1=e_1 k_2, f'_2=f_2/k_1,
    e'_2=k_1 e_2+e_1-e_1 k_2^2/D_c,
    f'_1=f_2+f_1/k_2-f_2/(k_1^2 D_c).            (6)

For the checked point map apply the literal flip and the
contravariant inverse convention already established in the
[holonomy calculation](regular_holonomy_braiding.md). Equation (6)
is precisely the characteristic classical braiding on the Gauss
leaf. In balanced variables `e_G=e/rho_N^N`, `f_G=-rho_N^N f`,
the divisor is `1-e_(G,1)f_(G,2)k_2/k_1`; the physical meridian
uses the separately marked `gamma=(-1)^(N+1)` factor. All of these
scalings are retained.

Equation (4) alone is an inner cyclic matrix factor and preserves
the root central scalars. The center change (6) is carried by
the resonant/Cartan canonical part. In particular one may write
the exact ordered factorization

    Rhat=[Dhat R_res,Q(W)] C_Q(Zhat).             (7)

The regular root finite factor in (7) has been identified explicitly.
The bracketed factor is the specified whole canonical period;
it has not been replaced by an unproved regular matrix.

There is a direct reason such a replacement is generally impossible.
A regular invertible matrix on a **fixed** pair of full cyclic
fibers intertwining `Delta Ecal` with `Delta^op Ecal` would require

    e_1 k_2+e_2=k_1 e_2+e_1.                    (8)

For the dense two-dimensional Rees leaves with independently
varying `p_i` this is false generically. A regular same-fiber
matrix limit cannot implement the whole R. It must transport
the center/base (or retain a quantum canonical operator). Special
pointed subloci where (8) holds do not remove this generic obstruction.

## 6. The original head and every internal projector are retained exactly

Let `i_2,p_2` be the actual two-head inclusion and projection, and
put `C=C_1 tensor C_2`. Define

    i_new=C i_2, p_new=p_2 C^(-1).

Then the exact source identity is

    p_2 R i_2=p_new Rhat i_new, p_new i_new=I.     (9)

In the head basis their factors are the ramified flags `eta^j`
and `eta^(-j)` and the source exponential
`exp[-(p_1u_1+p_2u_2)/d]`. They have not been canceled by
calling the source normalized.

For an intermediate head projector `P_2=i_2p_2`, one has

    C P_2 C^(-1)=exp[-(p_1u_1+p_2u_2)/d] P_2.   (10)

The finite cut coupon additionally retains its head entry ratios
`eta^(i-j)/N`. These formulas must be inserted at every compression
in a word. Dropping them would compare an uncompressed Verma
period with the actual finite-head period and lose the specified
two-wall excursion adapter `delta w H_beta`.

The original literal pivot transforms as the literal clock power,
with `g_lit=U g_red` and the inverse defect adapter. The common
Cartan half-character, zero-framing scalar and full external
modified-dimension function remain exactly the original ones.

The left side of (9) is regular at the root as the actual finite
crossing matrix. Thus its right side has precisely the necessary
source/period cancellations in this head pairing. This local
regularity does **not** show that the resonant pole survives as a
selected geometric action; nor does it make `i_new` or (10) regular.

## 7. Exact gain and remaining whole-source step

The actual whole Verma R now supplies, in the same Rees source,
the marked cyclic factor, the resonant dilogarithm period, and
the characteristic full-cyclic center braiding. The pointing is
retained as the explicit irregular and ramified source (9)--(10),
rather than reset to a cyclic vacuum.

This identifies the local whole-clock coefficient transport behind
the Green carry module more concretely than an unspecified
root matrix. It does not compute the continuation of a complete
word/current through every retained projector or the pairing of
the two final geometric framing currents. In particular it gives
no license to set their coefficient carry `C-I` to zero, erase
the finite source jets, or infer a nonzero selected scalar period.
Those remain the actual full scalar comparison.

[The quantum matrix/base theorem](quantum_matrix_base_intertwiner_torsor.md)
now constructs the local matrix intertwiner on a whole quantum-torus
cover. The remaining base transport is explicit and its resonant
Hamiltonian yields all six center formulas. The source has its own
specified residual; a regular matrix lift alone does not cancel it.

[Universal crossing audit](../experiments/audit_rees_whole_crossing_source.py)
and [results](../experiments/rees_whole_crossing_source_results.json)
check the norm-one cyclic coefficients and functional transport,
the resonant linear/logarithmic normal adapter, and all six center
powers on twelve dense full-cyclic Rees pairs at even and composite
levels as well as odd levels. No knot-specific check or selected
phase assertion enters these diagnostics.

[Independent normalization and source audit](rees_whole_crossing_independent_audit.md)
confirms the proof and its coefficientwise/finite-head scope.
