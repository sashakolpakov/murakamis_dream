# The actual paired normal on a fixed complex corridor near the fold

Subsequent full-domain result: the
[full strict physical packet](actual_q_hahn_full_physical_complex_packet.md)
extends the actual ordinary amplitude and the stated small/near-fold
complex bounds to fixed physical compacts, with the necessary finite-level
boundary correction. The [selected-factor corollary](actual_augmented_plat_selected_factor_localization.md)
then selects every ordinary factor outside one prescribed matching-edge
block. Global contraction and period estimates remain open. The argument
below keeps its original domain and proof scope.

30 October 2026. The original paired normal admits a polynomial bound
on every fixed compact magnetic corridor when the two channel indices
remain a bounded number of steps apart. More generally it has only
subexponential relative cost when their separation s satisfies
s log N=o(N). The magnetic corridor is genuinely complex and has
width independent of N. This follows from the original generic source,
not from interpolation of its physical-grid values.

The channel window in this statement shrinks in scaled coordinates.
It does not give subexponential cost at a fixed nonzero scaled channel
displacement, a relative normal amplitude, or a whole-source estimate.

## 1. Statement and exact source

Let q0=exp(pi i/N), d=N-1, and let

    0<=j<l, j+l=d, s=l-j.

For q=q0 exp(epsilon) put Q=q^2, B=Q^(-N), x=q^d and

    t=N tau, u=N nu, U=Q^u, T=Q^t, sigma=q^t,
    D_m(T)=product_(r=0)^(m-1)(T-Q^r).

Use the literal generic finite source from
[the small-channel generic theorem](actual_q_hahn_small_channel_generic_normals.md)
and [the collision theorem](actual_q_hahn_partner_normal_collision.md):

    C_m(q;t,u)=x^u H_m^B(U,T/U)/D_m(T),

    H_m^B(U,V)=sum_(a=0)^m (-1)^a B^a Q^[a(a+1)/2]
      [m choose a]_Q (BQ^(m-a+1);Q)_a/(BQ;Q)_a
      V^a product_(r<a)(U-Q^r) product_(r<m-a)(V-Q^r).   (1)

All powers use log q=pi i/N+epsilon. In particular this is the
original generic highest-weight-d deformation, not the root-only
squared-binomial formula. Its paired normal is

    w_(j,l)(t,u)=[D C_j(q0;t,u)-D C_l(q0;t,u)]
                     /[-2N Delta_j],
    Delta_j=q0^(2j+1)-q0^(-2j-1), D=q d/dq.            (2)

Let K be a compact subset of the joint central wedge

    W={ (tau,nu): 1/2<Re tau<1,
                          |2Re nu-Re tau|<1/2 }.

There exist eta_K,c_K,C_K>0 such that, for all sufficiently large N
and all 1<=s<=eta_K N of the required parity,

    |w_(j,l)(N tau,N nu)/C_j(q0;N tau,N nu)|
                <= C_K N^8 (C_K N^16)^s,   (tau,nu) in K.        (3)

Every function in this quotient is holomorphic on a neighborhood of
K, and C_j(q0) is nonzero there. No omitted tail is used in (3).

Consequently, for bounded s the cost is polynomial in N. Uniformly
over any windows 1<=s<=h_N with h_N log N=o(N),

    |w_(j,l)| <= exp(o(N)) |C_j(q0)|                 (4)

on the SAME fixed complex compact K. This includes windows of size
O(N^a) for every fixed a<1, in particular square-root windows.

## 2. The generic recurrence is valid beyond the small channel

Keep B temporarily independent of Q. Put A=B^(-1) and

    K_m=(B^2 Q^(m+1);Q)_m/(BQ;Q)_m,
    S_m(U,T)=U^m H_m^B(U,T/U),
    R_m(z)=z^m S_m(sigma/z,sigma^2)/(sigma^(2m) K_m).

These are monic polynomials for generic parameters. Their exact
source normalization is

    C_m=x^u q^(mt) K_m R_m(sigma/U)/D_m(T).            (5)

Write

    Lambda_n=AQ^(-n)+BQ^(n+1),
    b_n=[(1+A)+Q sigma^2(1+B)
                -Q^(-n)(Q sigma^2+A)-Q^n(BQ sigma^2+1)]/sigma,
    d_n=Q^(1-n)+Q^n-1-Q,
    u_0=0, u_n=b_n/(Lambda_n-Lambda_(n-1)),
    v_0=v_1=0,
    v_n=(b_(n-1)u_n+d_n)/(Lambda_n-Lambda_(n-2)), n>=2,
    alpha_n=u_(n+1)-u_n,
    beta_n=v_(n+1)-v_n-alpha_n u_n, n>=1.

Then, as RATIONAL identities in generic B,Q,sigma,

    R_0=1, R_1=z+alpha_0,
    R_(n+1)=(z+alpha_n)R_n+beta_n R_(n-1).             (6)

The small-channel note proves these formulas by its original Casimir
identity and finite moment argument. Their use at a large channel
requires an additional justification. Fix n and clear the denominators
in (6). The residual is a finite Laurent polynomial in B,Q,sigma,z,
independent of the source size N. For every N>=2n+3 the proved
small-channel result makes it vanish at B=Q^(-N), identically in
generic Q,sigma,z. Writing the residual as sum_a B^a p_a(Q,sigma,z),
choose N larger than all its finite Q-exponent widths. The supports
of Q^(-Na)p_a are then disjoint. Therefore every p_a is zero.
This proves (6) formally for every n. The scalar identity for K_m
already has the independent finite Vandermonde proof and no
small-channel restriction. Thus (5),(6) describe the actual large
generic source wherever their generic factors are defined.

At the actual root some monic R_m have poles because K_m vanishes.
We do not assume these monic polynomials are holomorphic there.

## 3. A small generic circle controls every intervening row

Let a_K=inf_K(Re tau-1/2)>0. Choose

    0<eta_K<min(1/4,a_K).

Then l/N<1/2+eta_K/2 and every extra source divisor T=Q_0^r,
j<=r<l, remains uniformly separated from K. The same holds for
the factors already present in D_j. All elementary exponentials
q^n, B and sigma, and their inverses, are uniformly bounded for
|epsilon|<=c N^(-3), n<=N, (tau,nu) in K.

Use the circle

    |epsilon|=rho_N=c_K N^(-8),                     (7)

with c_K chosen from the small-channel theorem, decreasing it if
needed. That theorem supplies a tridiagonal matrix M_j(epsilon)
with det M_j=R_j(z), z=sigma/U. At zero it is the original
accretive matrix zI+cD+K_skew, c=-cos((t+1)pi/N), and its change
in operator norm is O(N^7 |epsilon|). Consequently, throughout the
disk enclosed by (7),

    ||M_j^(-1)||<=C_K,
    |C_j(q)/C_j(q0)|<=C_K,
    |R_(j-1)(z)/R_j(z)|<=C_K.                       (8)

The last identity follows from the last diagonal entry of M_j^(-1):
the cofactor is its leading (j-1)-row determinant, exactly R_(j-1).
Thus the initial two values for propagating (6) are controlled.

For every n<=l, the only spectral denominators in (6) are

    Lambda_n-Lambda_(n-1)
       =(1-Q)A Q^(-n)(1-B^2 Q^(2n)),
    Lambda_n-Lambda_(n-2)
       =(1-Q^2)A Q^(-n)(1-B^2 Q^(2n-1)).             (9)

At the root a vanishing last factor in (9) occurs only at
2n=N or 2n-1=N, respectively. All other last factors have modulus
at least c/N, and both first factors have modulus at least c/N.
These nonresonant differences therefore stay at least c/N^2 on
the circle (7). At a resonant n the last factor is exactly
1-Q^(-N)=1-exp(-2N epsilon), whose modulus is at least c N rho_N
on that circle. Multiplication by the first factor gives a lower
bound c rho_N. Hence EVERY required denominator on (7) obeys

    |Lambda_n-Lambda_(n-r)|>=c_K rho_N, r=1,2,        (10)

with r=2 used only for n>=2. This explicitly retains the folded
resonance rather than pretending its root denominator is a unit.

The numerators b_n,d_n are O_K(1). The definitions in section 2
and (10) give, on the circle,

    |u_n|+|alpha_n|<=C_K rho_N^(-1),
    |v_n|+|beta_n|<=C_K rho_N^(-2).

Propagating the two-component recurrence (6) exactly s times, from
R_(j-1),R_j to R_l, now gives

    |R_l(z)/R_j(z)|<=(C_K N^16)^s.                  (11)

No positivity, missing-current cancellation, or interpolation of
physical samples enters this estimate.

## 4. The scalar ratio and holomorphy of the FULL source

The scalars in (5) cannot be discarded. Their exact cancellation is

    K_l/K_j=
      product_(r=2j+1)^(2l)(1-B^2 Q^r)
      /[product_(r=j+1)^l(1-B^2 Q^r)
         product_(r=j+1)^l(1-BQ^r)].                 (12)

There are 2s numerator and 2s denominator factors. The denominator
indices lie uniformly near N/2 under s<=eta_K N, so all those
denominators are bounded below on (7). The numerator factors are
uniformly bounded above. One numerator factor vanishes at the
center of the circle; it is retained in (12). Thus

    |K_l/K_j|<=C_K^s,
    |D_j(T)/D_l(T)|<=C_K^s,
    |q^((l-j)t)|<=C_K^s.                            (13)

Equations (5),(8),(11),(13) prove on the circle

    |C_l(q;t,u)/C_j(q0;t,u)|
                         <=C_K(C_K N^16)^s.         (14)

We apply Cauchy's formula to C_l, NOT to its singular monic factor.
The original finite expression (1) proves C_l is holomorphic
throughout the enclosed disk: its factors (Q;Q)_a and (BQ;Q)_a
have indices a<=l<N and are units at q0; their possible zeros
stay outside this polynomially small disk. Its factors D_l(T)
are uniformly nonzero by the separation at the beginning of
section 3. The finite numerator is entire in the displayed
exponentials. Thus every apparent monic pole inside (7) is already
canceled in the original source, before Cauchy's estimate is used.

Consequently (14), and the small-channel bound for C_j, imply

    |D C_l(q0)/C_j(q0)|<=C_K N^8(C_K N^16)^s,
    |D C_j(q0)/C_j(q0)|<=C_K N^8.                    (15)

Finally |Delta_j|=2sin(pi s/N) and

    2N |Delta_j|=4N sin(pi s/N)>=8s>=8

in this near-fold range. Dividing the two ACTUAL generic
derivatives in (15) by the original gap in (2) proves (3).

## 5. What the estimate supplies

The full paired normal, including its large-channel tail, is
holomorphic and has at most subexponential relative cost on a fixed
complex magnetic corridor for s log N=o(N). This can accompany the
proved ordinary-column complex action in a shrinking channel window
at the complete endpoint. It is an upper bound: no nonzero normal
amplitude or leading coefficient is asserted.

For s proportional to N the bound (3) is too large to identify an
exponential rate. In particular it does not control a fixed
nonzero scaled channel shift that might arise at a filling saddle.
The extra-pole obstruction outside the near-fold corridor remains
valid. Neither physical-grid interpolation nor an assertion that
the generic monic determinant is regular has been used to avoid it.

Focused audit: [full generic large source and resonant circle](../experiments/audit_actual_q_hahn_near_fold_complex_partner_bound.py),
with [saved results](../experiments/actual_q_hahn_near_fold_complex_partner_bound_results.json).
Exact dual arithmetic passed 208 all-degree source recurrences,
582 original large-channel generic value-and-normal comparisons,
and 110 scalar-ratio identities. At 220 digits, 120 literal
nonphysical large-source circle comparisons, 5,080 spectral-gap
checks, 30 original-versus-transverse paired normals, and 120
retained scalar identities passed. The maximum source comparison
error was below 1.1e-206. Both bounded and square-root-sized
channel separations occur in these checks. The uniform conclusion
is the proved circle estimate, not an inference from the samples.

The estimate requires s log N=o(N). It does not include a fixed positive scaled-channel displacement or an amplitude theorem.

The conclusion remains a relative upper bound in the stated shrinking channel window on a fixed magnetic corridor.