# The original factorial interpolant is exactly a full-Psi quotient

28 October 2026. The normalized factorial interpolation used for the
original finite sums is the SAME full Faddeev function already used in
the relative moment source. There is no residual period-one multiplier.
This supplies a literal five-full-Psi formula for every original physical
crossing coefficient, including its support zeros and complete scalar.

This is a normalization comparison inside the existing double-sine/Barnes
framework. It is not a new quantum invariant or a selected-cycle theorem.

## 1. Exact identity and elimination of the periodic ambiguity

Let N>=2, h=2pi*i/N, d=N-1 and use the exactly normalized functions
Fhat_N and G_N of
[the factorial theorem](exact_factorial_interpolation_and_complex_contours.md).
Let Psi be the original positive full function and

    phi_N=Psi(h)=sqrt(N)exp{i pi[1/4-(N+1/N)/12]}.

Then as meromorphic functions of z,

    Fhat_N(z)=phi_N/Psi(h(z+1)).                      (1)

Here is an independent proof fixing the possible period-one ambiguity.
Both sides are nonzero and holomorphic on -1<Re z<N. For Fhat this
was proved from its convergent Gamma product. For Psi use the proved
identification

    Psi(Z)=Phi_(1/sqrt(N))(sqrt(N)Z/(2pi)-c_b).

The zero-free strip |Im argument|<Im c_b becomes precisely
0<Im Z<2pi(1+1/N), or -1<Re z<N. These strip and conjugation facts
are proved from the defining integral in
[the full-Phi audit](faddeev_pentagon_audit.md), not assumed from a
published pentagon.

The two first-shift equations imply that

    H(z)=Fhat_N(z)Psi(h(z+1))/phi_N

is one-periodic on their overlap. It extends to an entire, nowhere-zero
one-periodic function by translations of this strip. Fix an entire
logarithm L of H. On a central vertical strip of width one, both signs
of log|H| have the bound

    |Re L(z)|<=C_N(1+|Im z|^2 log(2+|Im z|)).          (2)

For clarity this is a rough FIXED-N growth estimate, not a semiclassical
estimate. The finite Barnes-G expression for Fhat proves it directly.
All its Gamma/Barnes arguments have positive real parts in this strip.
The convergent digamma series gives psi(w)=O(log(2+|w|)) there; integrating
the proved derivative

    d_w log BarnesG(1+w)
          =w psi(1+w)-w-1/2+(log(2pi))/2

along a vertical line bounds its logarithm by O(t^2 log(2+|t|)).
The same estimates bound both numerator and denominator in the finite
Barnes product. The full-Phi left/right asymptotics on a fixed horizontal
strip bound the Psi part, including its reciprocal, by a quadratic
logarithm. This proves (2). Periodicity extends it to the whole plane.

An entire harmonic function with growth O(R^2 log R) has zero derivatives
of every order at least three: its circle Fourier coefficients of order
ell are O(R^(2-ell)log R), tending to zero for ell>=3. Apply this to
Re L, or the harmonic Cauchy formula. Thus L is a polynomial of degree
at most two. Periodicity of H forces L(z+1)-L(z) to be a constant
2pi*i*m, m integer, so the quadratic coefficient is zero. Since H(0)=1,

    H(z)=exp(2pi*i*m z).                              (3)

Finally take Re z=d/2. The real Gamma product and exact reflection
G_N(z)G_N(d-z)=N give |G_N(z)|=sqrt(N). The modulus of the explicit
Gaussian factor in Fhat is ONE on this line, hence |Fhat|=sqrt(N).
The argument h(z+1) has Im equal to pi(1+1/N); its Faddeev argument
is real. The proved conjugation identity therefore gives |Psi|=1.
As |phi_N|=sqrt(N), we have |H|=1 on this entire vertical line.
Equation (3) now forces m=0. This proves (1), including its phase.

## 2. Exact five-function original crossing coefficient

For the positive physical crossing with input (a,b), total transfer k,
and output (b+k,a-k), the original coefficient is

    r_plus(a,b,k)=kappa x^(-a-b+k)Q^(b(a-k))
                           F_(b+k)F_a/[F_k F_b F_(a-k)].

Apply (1) to the normalized interpolation in the transfer variable z.
Its FULL function factor, with all fixed factors also expressed in Psi,
is exactly

    Fhat(b+z)F_a/[Fhat(z)F_b Fhat(a-z)]
       =phi_N^(-1)
          Psi(h(b+1))Psi(h(z+1))Psi(h(a-z+1))
                        /[Psi(h(a+1))Psi(h(b+z+1))].       (4)

The original Cartan monomial and kappa remain unchanged. Formula (4)
is a literal equality, not an equality up to a central factor. Its
negative version is the actual balanced antiunitary mirror, with the
opposite full function and conjugate marked constants.

At every physical integer z in [0,d], forbidden transfers z>a or b+z>=N
are EXACT zeros of this expression. They are the actual pole/zero
cancellations of the completed function. The half-integer rectangle
of [the endpoint-packet theorem](actual_total_transfer_endpoint_packets.md)
therefore represents the original finite transfer sum directly with
these five functions, preserving all corners and source data.

The five classical arguments are B, A/V, V, A and T/V, where
A=Q^a, B=Q^b, V=Q^(a-z), T=AB. Their signed sum is exactly the
original direct crossing symbol

    -[A]-[T/V]+[V]+[B]+[A/V].

Thus no extra auxiliary nine-to-five calibration is needed in THIS
physical coefficient chart. This does not remove the true transfer
boundary current (the low normal packet has the nonzero source in
equation (12) of the endpoint theorem), provide an infinite-height
quadrature estimate, or establish a global cycle with a sharp bound.

[Audit](../experiments/audit_actual_total_transfer_endpoint_packets.py):
independent Barnes-G versus completed full-Psi evaluations, original
allowed/forbidden transfer values and exact normal/source identities.
