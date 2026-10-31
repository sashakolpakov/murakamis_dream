# An exact spectral total derivative for the original root source

, 31 October 2026. This is an exact fixed-root identity for the
original pair Casimir, retaining its simple and repeated spectral nodes.
No contour deformation or uniform exponential estimate is asserted.

Put N>=3,d=N-1,q=exp(pi i/N). Let chi(z)=2T_N(z/2)+2,
and let Omega be the ACTUAL pair Casimir from the
[original source theorem](actual_homogeneous_casimir_face_source.md).
Define its polynomial resolvent numerator

    V(z)=chi(z)(z-Omega)^(-1).

This is the unique degree-(N-1) matrix polynomial supplied by polynomial
division and chi(Omega)=0. It is not the determinant adjugate of the full
N^2-dimensional matrix. At a paired c=2cos(phi), its resolvent is

    (z-Omega)^(-1)=P/(z-c)+Q/(z-c)^2+regular.

Write h(z)=chi(z)/(z-c)^2 locally. The Chebyshev ODE gives

    h(c)=N^2/(4-c^2), h'(c)/h(c)=c/(4-c^2).

Consequently Q=V(c)/h(c) and P=V'(c)/h(c)-h'(c)V(c)/h(c)^2.
With Qhat(z)=(4-z^2)V(z)/N^2 this is

    Q=Qhat(c), P=Qhat'(c)+c Qhat(c)/(4-c^2).

For any function f holomorphic at the spectral nodes, therefore,

    f(c)P+f'(c)Q
      =[(4-c^2)(fV)'(c)-c f(c)V(c)]/N^2
      =-d_phi[2sin(phi) f(2cos(phi))V(2cos(phi))/N^2].    (1)

When N is odd, the simple node is c=-2, chi'(-2)=N^2, and the
right side of (1) at phi=pi is 2f(-2)P_*. Thus the original simple
term has exactly one half of that derivative. Each paired node occurs
twice in the full odd-angle grid and the derivatives are equal there.
The exact original operator is accordingly

    f(Omega)=-1/2 sum_(k=0)^(N-1) B_f'(phi_k),
    B_f(phi)=2sin(phi) f(2cos(phi))V(2cos(phi))/N^2,
    phi_k=(2k+1)pi/N.                                   (2)

No cyclic physical head is introduced: the cyclic variable in (2) is
the spectral parameter, with the original projector multiplicities.

For R^n use its [exact full-Hermite Gaussian](actual_direct_long_power_source.md)

    f(2cos(phi))=q^(n d^2/4)
       exp[-n(phi-pi)^2/(2hbar)], hbar=2pi i/N,
    0<=phi<=2pi.

On this interval B_f has equal zero endpoint values and equal first
derivatives. Its second derivatives can differ at the endpoints,
reflecting the K-cut at z=2. Thus its periodic extension is C^1,
but endpoint currents must be retained in further integration by parts.
In particular the zero Fourier integral of -B_f' is exactly zero.

With Fourier convention hat B(j)=(2pi)^(-1)int_0^(2pi) B(phi)e^(-ijphi)dphi,
the finite midpoint formula gives the convergent fixed-N identity

    f(Omega)=-(iN^2/2)sum_(ell in Z) ell (-1)^ell hat B(Nell). (3)

The ell=0 term is zero. For each fixed N,n the sum is absolutely
convergent: periodic B is C^1 with piecewise smooth higher derivatives,
so hat B(j)=O(j^-3). Constants here may depend exponentially on N;
this observation gives no uniform global bound. Formula (3) is an
alternative exact source period, closely related to the existing
[Fourier-Hermite Gaussian formulas](actual_coherent_filling_gaussian_chirp.md). It does not erase their endpoint
currents or determine which nonzero charge contributes after sewing.

## Why complete-channel samples do not control the derivative

At a paired node, L_N(c)=0 and
L_N'(c)=(-1)^(N-1)N/(2sin^2(phi)). Hence its complete sector equals

    L_N'(c)Q=(-1)^(N-1)2V(c)/N.

The complete positive packet therefore controls V(c), whereas V'(c)
also carries the independent semisimple projector P. The simplest
illustration is a diagonal coefficient on the face boundary x=y=0:
Omega is diagonal there, so at a paired eigenvalue c its entry
V(z)=chi(z)/(z-c) vanishes at z=c, but V'(c)=chi''(c)/2 is nonzero.
At even N every spectral node is paired, so all corresponding
complete diagonal samples vanish while the semisimple derivatives
reconstruct the identity. This example concerns the ACTUAL local
polynomial specialization, not a freely chosen off-grid interpolation.

Thus the proved exponential interpolation of complete packet values
cannot simply be differentiated to estimate (2) or (3). A bound on
the original polynomial resolvent numerator between nodes, including
its semisimple derivative and the retained endpoint charges, is an
additional input. No claim that such a bound is impossible is made.

## Exact link to the retained physical colors

Polynomial division of the Chebyshev identity gives, in the SAME
original Casimir quotient,

    V(z)=U_(N-1)(Omega/2)
           +2sum_(h=1)^(N-1)T_(N-h)(z/2)U_(h-1)(Omega/2)
        =(-1)^d L_N
           +2sum_(h=1)^(N-1)(-1)^(h-1)T_(N-h)(z/2)L_h.   (4)

One proof starts from

    [T_N(x)-T_N(y)]/(x-y)=U_(N-1)(y)
      +2sum_(h=1)^(N-1)T_(N-h)(x)U_(h-1)(y),

then substitutes x=z/2,y=Omega/2 and T_N(Omega/2)=-1.
The scalar polynomial identity also follows immediately by induction
in N using the two Chebyshev recurrences. It was checked exactly for
N=2,...,14 before recording it here.

The homogeneous source and every actual exterior functional preserve
(4) by linearity. Thus controlling the original off-node numerator
means controlling a SPECIFIED coherent combination of all physical
colors, with their signs. It is not determined by the complete packet
alone. On the other hand a bound on this coherent combination could
be sharper than bounds on its separate colors, so (4) is not a no-go
statement for a phase-preserving resolvent method.

## Validation and scope

The [focused audit](../experiments/audit_actual_spectral_total_derivative_source.py)
uses the original coproduct Casimir and independently built signed R
matrices. It checks all monomials through degree N-1 and powers n=+/-1,...,+/-5
at N=3,...,8, including both parity conventions. The divided-Chebyshev
identity is also checked symbolically at N=2,...,14.
[Results](../experiments/actual_spectral_total_derivative_source_results.json)
record finite identities; they assert no uniform Fourier constants.

The theorem is at a fixed root of unity. It does not establish a uniform Fourier estimate or select a contributing cycle.