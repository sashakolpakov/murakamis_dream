# Independent audit of the unfolded Ward factorial

Research audit, 27 October 2026. The formulas in
[the unfolding theorem](unfolded_ward_factorial_and_regulator.md)
pass an independent coefficientwise proof check. This audit does
not assert a global network-period identity.

## 1. All-level uniqueness

Fix a coefficient index `j`. For all sufficiently large `N>j`, the
actual nilpotent jet prescribes the value
`c_j(Q_N)=1/(Q_N;Q_N)_j`; neither denominator vanishes there.
A nonzero rational function has finitely many zeros, while the
`Q_N` are infinitely many distinct points. Thus the coefficient is
uniquely `1/(Q;Q)_j`. The exceptional set can depend on `j`.
No common bound in `j` on degrees or exceptional levels is required.
This proves uniqueness in the specified rational coefficient class,
and the displayed universal factorial supplies existence in this case.

## 2. Cyclotomic pole and constant

The formal logarithm is

    log F(Q,z)=sum_(m>=1) z^m/[m(1-Q^m)].

Put `Q=zeta exp(h)`, with `zeta` primitive of order `N` and `X=z^N`.
For `m=kN`,

    1/[m(1-exp(mh))]=-1/(m^2 h)+1/(2m)+O(h).

The pole is therefore `-Li_2(X)/N^2`. The resonant constant is
`Li_1(X)/(2N)=-Log(1-X)/(2N)`.

For `D_N=product_(j=1)^(N-1)(1-zeta^j z)^(j/N)`, the coefficient
of `z^m` in its logarithm is

    -1/(mN) sum_(j=1)^(N-1) j zeta^(jm).

For nonresonant `m`, this equals `1/[m(1-zeta^m)]`, exactly the
constant of `log F`. For `m=kN`, it is `-(N-1)/(2kN)`, so the
whole resonant part of `log D_N` is
`(N-1)Log(1-X)/(2N)`. Subtracting `Log(1-X)/2` leaves precisely
the resonant constant of `log F`. This checks the sign and every
factor of `N` in the pole and regular part.

The parameter `h=Log(Q/zeta)` here is a fixed-root deformation
parameter. It is not the earlier large-level parameter `Log q`
with `q_N=exp(pi*i/N)`.

## 3. Norm-root gauge and its uniqueness

The marked cyclic product satisfies

    D_N(zeta z)/D_N(z)=(1-z)/(1-X)^(1/N),
    product_(a=0)^(N-1) D_N(zeta^a z)
                          =(1-X)^((N-1)/2).

Both follow directly by rearranging the marked logarithms, hence
hold for even and composite `N` as well. With
`nu=(1-X)^(1/N)`, the gauge

    g_D=D_N/nu^((N-1)/2)

has norm one and the required normalized cyclic transport.
Its nilpotent specialization has constant one and solves the same
coefficient recurrence as the literal actual factorial. It therefore
equals that finite factorial modulo `e^N`.

The ratio of this gauge and the previously constructed norm-root
gauge is sigma invariant, hence scalar in the completed base: the
basis `1,e,...,e^(N-1)` has distinct sigma eigenvalues. Its norm is
its `N`-th power. The identity marking forces this scalar to be one.
This proves equality on the completed common marked cover, rather
than merely equality of norms. The even-`N` square root is fixed by
the same identity mark.

For the actual cyclic sign `e^N=(-1)^(N+1)kappa_N`, substitution
`z=-te` gives `X=-kappa_N t^N` and
`1-X=1+kappa_N t^N`, with no remaining parity sign.

## 4. Period and source conventions

For `S=Li_2(X)+UV`, `U=Log X`, `V=Log(1-X)`, direct differentiation
gives `dS=U dV`. Thus the stated Heisenberg matrix has
`Pi^(-1)dPi` with zero central entry; equivalently its right equation
is `dPi=Pi Omega`. The opposite Maurer--Cartan convention would
require a different central coordinate.

Since `d kappa_N/d kappa=N` at completion,

    partial_kappa[-Li_2(-kappa_N t^N)/N^2]_(kappa=0)=t^N/N.

The actual divided affine source is `-t^N`, exactly minus `N`
times this normal derivative. The local Bloch--Wigner logarithmic
metric term is retained by the displayed regulator formula.

## 5. Identity-meridian formal rigidity is already available

[The closed-braid period note](closed_braid_period_line.md), Section 4,
already proves that an Artinian representation with every meridian
congruent to identity factors through knot abelianization. Its
induction is valid: if all meridians agree modulo `m^r` and lie in
`I+m`, their pairwise commutators lie in `m^(r+1)`. A Wirtinger
crossing then equates consecutive understrand meridians modulo
`m^(r+1)`. A knot has one connected understrand cycle, so all agree
at the next order. Nilpotence terminates the induction.

For matrix groups this argument does not require characteristic
zero. More generally it applies whenever the identity congruence
filtration satisfies `[G_r,G_s] subset G_(r+s)`. For the present
`SL_2` application it proves the stated Artin functor equality and
the claimed formal inability to reach nonabelian geometry from the
identity representation. It says nothing analogous about a
noncentral parabolic meridian or a different residual representation.
