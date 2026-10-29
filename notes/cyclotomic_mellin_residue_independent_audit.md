# Independent check of integral-color periodicity and the residue

Audit, 27 October 2026. I checked the general proof in
[the residue construction](cyclotomic_mellin_residue.md), independently
of its finite examples. The subquotient and residue arguments check
out. The one-dimensional-shift step has the following direct
statewise proof, which avoids a possible ambiguity about cutting
both tensor factors in a parallel-link argument.

## 1. Direct framing calculation for the one-dimensional shift

Let V be an integer-weight root color of parity m, with weights
m-2a, and let h=kN. On V tensor C_h the displayed coproduct gives

    H'=H+h, K'=(-1)^k K, E'=(-1)^k E, F'=F.

Use the original full R, retaining its Cartan scalar and the fixed
square-root phase. Put

    s_0=q^(h^2/2)(-1)^(km), g_h=q^((1-N)h).

At a positive crossing the first output is c=b+u. The E^u factor
changes by (-1)^(ku), while the Cartan factor changes by

    q^(h^2/2) q^(h(m-a-b)).

Their product is exactly s_0(-1)^(k(c-a)). At a negative crossing
the Cartan factor is inverse and c=b-u; its exact multiplier is
s_0^(-1)(-1)^(k(c-a)). Thus for either sign,

    r'_sign/r_sign=s_0^sign (-1)^(k(c-a)),       (1.1)

meaning equality after multiplication even when a coefficient is
zero. On every closed state sum(c-a)=0, by the original integer
position coboundary. The crossing contribution is therefore s_0^w.

The pivot on each closed strand changes by g_h. The ribbon twist
changes by s_0 g_h, either directly from its weight formula or from
theta_(V tensor C_h)=theta_V theta_(C_h) times the scalar double
braiding (-1)^(km). Hence the reduced zero-framed knot multiplier is

    s_0^w g_h^(b-1)(s_0 g_h)^(-w)
                       =g_h^(b-1-w)=1.          (1.2)

Here g_h is a sign and b-1-w is even for a knot braid. There is
no closed auxiliary-component quantum dimension. This proves the
required one-dimensional-shift invariance in the original root
ribbon conventions, including its phase and pivot.

## 2. Integral specialization and subquotient naturality

On D_m the coefficient of the generic R term of order u has the
factor [u]! times two Gaussian coefficients, after multiplying
the E^u and F^u matrix entries and dividing by [u]!. The Gaussian
coefficients are Laurent polynomials. Every u>=N term therefore
vanishes at the root, and u<N terms are the exact truncated root
R. The inverse works the same way. This justifies specialization
of the generic scalar long-knot operator even when m>=N.

The ordinary pivot and root pivot differ by (-1)^m, as do their
twists, so the reduced zero-framed scalar is unchanged. The root
long-knot operator is natural for H,E,F,K intertwiners: the full
R, inverse, evaluations, coevaluations and pivot are all natural,
and a coupon can be followed along the single cut component.
Consequently a nonzero inclusion or quotient between scalar
root long-knot operators forces equality of their scalars.
No division by a zero quantum dimension is involved.

For n=kN+r, 0<r<N, the quotient of D_(n-1) on its first r
vectors has E coefficient (-1)^k[r-j], unchanged F coefficient
[j+1], and shifted H,K. This is exactly
D_(r-1) tensor C_(kN) with the stated coproduct. The killed tail
is a submodule because its boundary E coefficient is [kN]=0.

For n=kN, the first N vectors form a submodule because its
outgoing F coefficient is [N]=0. Its E coefficient is
(-1)^(k-1)[N-j], so it is
D_(N-1) tensor C_((k-1)N). The rescaling by [j]!, j<N,
identifies D_(N-1) with the actual Kashaev color by unit entries.
Together with (1.2) this proves the all-color periodicity claimed
in the construction, including multiples of N.

## 3. The residue for an arbitrary fixed tail

The periodic root series is

    [sum_(r=1)^(N-1)C_r X^r+K_N X^N]/(1-X^N).

Its constant term at infinity is -K_N. Removing the initial
colors up to any fixed n_0-1 subtracts a polynomial with no
constant term; it does not change the residue against dX/X at
infinity. Thus the infinity residue is K_N for every such tail.
The finite residue at gamma^N=1 is -P_N(gamma)/N, since
gamma times the derivative of 1-X^N there is -N. Root
orthogonality makes their sum -K_N. There is no additional
pole at X=0 because the selected tail starts in positive degree.

For n_0>1 the rational function can acquire a higher-order pole
at infinity from that subtracted polynomial. The statement about
simple cyclotomic poles concerns its finite poles. This causes
no change to the residue identity.

These arguments establish the stated periodic rational root fiber
and the exact original Kashaev residue. They do not establish its
geometric support or exponential regulator norm.

[Exact statewise phase audit](../experiments/audit_cyclotomic_shift_framing.py).
[Results](../experiments/cyclotomic_shift_framing_results.json).
