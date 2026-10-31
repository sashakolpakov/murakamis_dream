# Independent audit of the actual two-head cyclic sewing

28 October 2026. The exact five-term resolvent and the two-sector
SMALL-CIRCLE period reduction in
[the sewing theorem](exact_quantum_quad_source_transport.md)
are correct, including the coincident-wall fibre. A balancing
gauge gives a useful local matrix estimate. It does not turn
the original period into a positive pairing or license the old
Hankel deformation term by term.

There is an explicit source-visible pole witness in the original
positive crossing: its two sewn cross pieces have nonzero double
poles absent from the nilpotent resolvent. Their contributions
must accompany any subsequent cut deformation.

## 1. Resolvent order and the coincident wall

On a total-index residue fibre choose basis b_n, n=0,...,N-1.
Let S be cyclic raising, A=aS, z=a/t, and h=k+1. For h<N the
actual truncated transfer deletes the arrows N-1 to 0 and h-1
to h. With U=[b_0,b_h], its deleted operator is UU^t A.
Woodbury therefore gives

    R_T=R_A-R_A U (I+U^t A R_A U)^-1 U^t A R_A.

Direct cyclic summation gives

    (I+U^t A R_A U)^-1
        =C_h(z)=[[1,-z^(N-h)],[-z^h,1]].

All orders in the displayed formula matter. At h=N the two
columns of U coincide, so a rank-two Woodbury inverse is NOT
available. Nevertheless the SAME compressed expression remains
correct, because

    U C_N(z) U^t=(1-z^N)b_0 b_0^t.

This is exactly the single-deleted-edge formula. Thus the global
five-term expression and its two cross terms are valid for every
fibre without double-counting the physical wall.

R_A and the two diagonal sewing terms are holomorphic at t=0.
Multiplying by the marked analytic inverse-D germ and integrating
on rho<min(1,|a|) kills those three terms entrywise. Other word
factors do not alter that conclusion, since they use different
integration variables. Consequently the at most 2^(3m) surviving
cross-sector networks retain the original source exactly on the
original product of small circles.

## 2. The balancing gauge and its quantitative scope

Retain a continuous Log z and put

    D_h=diag(1,z^(h-N/2)), w=z^(N/2).

Then exactly

    D_h^-1 C_h D_h=[[1,-w],[-w,1]],
    det C_h=1-z^N.                                (1)

The original physical scalar is a=x^-1 or Q^-1 x^-1. On an
actual inverse-D cut t=Q^(-epsilon j)r and at M=1,

    z^N=(-1)^(N+1) r^(-N).                        (2)

For odd N, w is one of the two real values +/-r^(-N/2).
The balanced C has positive eigenvalues 1+/-r^(-N/2) for r>1.
For even N, w is purely imaginary, and the Hermitian part of
the balanced C is EXACTLY identity. Both statements retain the
root phase; z^N has not been replaced by a positive number.

The gauge condition number is

    kappa(D_h)=r^|h-N/2|.

On the actual radial scale r=exp(s/N), it is bounded by exp(s/2),
uniformly in h and N when s is bounded. This includes h=N,
although U then has repeated columns. For odd N the smallest
balanced eigenvalue is 1-exp(-s/2), which tends to zero at the
radial endpoint. At fixed r>1 the gauge can instead have
exponential condition number; the stated bound is a scaled local
estimate, not a uniform estimate on the entire radial ray.

Moreover the two-sector Cauchy reduction keeps only C's OFFDIAGONAL
part. Its balanced version is [[0,-w],[-w,0]]: indefinite for odd N
and with zero Hermitian part for even N. Thus the positive diagonal
of full C belongs to terms whose original small-circle periods
vanish. Positivity of full C does not itself prove a lower bound
for their remaining cross-sector contraction. The actual co-source
is also a pivotal linear pairing, not the positive quadratic form
used by an accretivity estimate.

## 3. Added cyclic poles change the required relative cycle

Every cyclic R_A has poles at t^N=a^N, while R_T has only its
nilpotent pole at zero. The five-term formula cancels all added
poles. Discarding its analytic-at-zero terms preserves the small
circle period but does NOT preserve global holomorphy.

At completeness a^N=(-1)^(N+1). Thus for odd N the added poles
lie at N-th roots of unity: most hit D-cut endpoints, and t=1
is an added pole where D itself is regular. For even N they lie
at the interlaced half-roots, off those cuts. Separate cross
pieces can have double poles. Their old radial-cut integrals
may be nonintegrable when the pole hits a branch endpoint.
Pole residues or the corresponding marked finite-part chains
must be retained. Matrix balancing in Section 2 does not remove
this change of relative cycle.

## 4. An exact original positive-crossing source witness

Take N=2, M=1, Q=-1, q=i, x=i. In the opposite-root
realization of the actual U_+ factor, a=Q^-1 x^-1=i.
Use the original fusion C and Gaussian D=I from the strict
crossing factorization, and the original averaged first-cut
functional Phi with pivotal entries (-i,i). Keep its common
Cartan scalar and external line separately, unchanged.

Let R_cross(t) be the sum of the two cross terms, and R_T
the actual transfer resolvent. Exact source contraction gives

    Phi(C R_T(t) C^-1)=2i/t^2,
    Phi(C R_cross(t) C^-1)
        =-2i(t-1)(t+1)/[t^2(t^2+1)^2].             (3)

The leading double-pole coefficient of the second expression
at EACH of t=i and t=-i is i. These poles are source-visible
inside an actual positive crossing, rather than only in an
arbitrary matrix entry. The original inverse-D germ here is
f(t)=(1+t)^(-1/2). Both small-circle periods are exactly -i.

The uncorrected old D-cut integral for the sewn expression,
on t=-r, would instead be

    (2i/pi) integral_1^infinity
         (r^2-1)/[r^2(r^2+1)^2] (r-1)^(-1/2)dr.

It is purely POSITIVE imaginary and therefore cannot equal -i.
The missing cyclic-pole contributions are essential, even in
this smallest actual-source example. The original normalization
multiplies both expressions by the same retained nonzero factor;
it cannot correct the mismatch.

The missing ordinary residues are explicitly

    Res_(t=i) f(t)B(t)dt=(-9-i)/(4sqrt(1+i)),
    Res_(t=-i) f(t)B(t)dt=(9-i)/(4sqrt(1-i)).

Their sum is approximately 1.0596435755300515788i. The raw
cut integral is approximately 0.0596435755300515788i. The
correct contour identity is cut MINUS these pole residues,
which gives the original value -i.

## 5. Audit conclusion

The exact small-circle sewing is a real finite-sector reduction.
The balanced 2-by-2 matrix has a controlled condition number on
the natural radial scale and the stated parity-dependent sign.
Neither statement supplies a convergent termwise old-cut sewing
or a positive selected scalar. A usable geometric comparison must
carry the new cyclic poles and the original cross-sector source
through the transform, including its endpoint corrections.

There is a canonical linear repair when cyclic poles have order
at most two, as they do in each transfer variable. At a D-cut
endpoint alpha, put x=r-1 and write the remaining cut integrand
as x^(-u)f(x), where
f(x)=b_-2 x^(-2)+b_-1 x^(-1)+O(1). Its finite part is

    integral_0^1 x^(-u)[f-b_-2 x^(-2)-b_-1 x^(-1)]dx
      +integral_1^infinity x^(-u)f dx
      -b_-2/(u+1)-b_-1/u.

Use these marked finite parts on the branch cuts and subtract
the ordinary residues at unbranched cyclic poles. This gives
the original small-circle period exactly. The constants follow
from analytic continuation of the two elementary power integrals.
The small endpoint arcs cancel their fractional divergences and
have no additional finite residue: on the normalized cover a
residue exponent would require j to be a multiple of N.
Coordinatewise finite parts commute for this word because its
ordered matrix source is a finite sum of products of one-variable
rational factors. The tensor prescription retains the required
corner subtractions. It preserves the source, while still not
making its resulting scalar a positive quadratic pairing.

The [regularized cut theorem](cyclic_sewing_regularized_cut_cycle.md) has positive derivative factor 1/[u...(u+p-1)] for p=1,2. At every integration-by-parts step the boundary term at infinity is O(x^(-(N-1)/2)), and the zero-end finite constant vanishes because u is nonintegral. The final derivative integral converges at both ends. The whole-word tensor prescription is a finite sum of products of one-variable factors, with only coordinate pole loci. The unit-circle/completeness hypothesis excludes additional poles inside a radial cut. Geometric coupling remains separate.

[Exact and quantitative audit](../experiments/audit_two_head_cyclic_sewing_independent.py)
and [saved results](../experiments/two_head_cyclic_sewing_independent_results.json).
