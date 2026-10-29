# Independent audit of actual finite transport and the peripheral normal adapter

Proof audit, 27 October 2026, of
[the whole two-period transport construction](whole_two_period_transport_and_actual_coefficients.md).
Its algebraic identities, singular-lattice treatment and actual-source scope
pass. This audit does not identify the analytic two-nome period with a
selected whole knot period.

## 1. The free lattice and its actual first-period ratios

On the four-coordinate Laurent domain, the maps
sigma(e)=(1-z)e and tau(e)=(1-w)e commute: their base automorphisms
commute and each fixes the other's multiplier. Both positive maps are
injective before specialization. Their rational inverses have the
specified translated-factor poles. Thus the genuine invertible
difference torsor is a localization, whereas the original free line
with its vanishing maps is retained at norm zero.

Iteration gives t_n(z)=(z;Q)_n for n>=0, and the stated reciprocal
product for negative n. Directly splitting the product proves
t_(m+n)(z)=t_m(z)t_n(Q^m z) for all integers. These ratios depend
only on Q,z; every sigma-periodic completion cancels from them.
The Gaussian ratio of three factorial transports is its original
rational Gaussian polynomial, with cancellation performed before
singular evaluation.

Consequently the finite-word substitution changes no matrix entry:
the original monomial, Cartan and framing characters, support,
cup/cap, pivot, modified dimension, source and moment insertions
remain exactly where they were. Products, finite sums and normal
derivatives preserve the identity. This verifies an exact rational
transport realization, rather than an identity of completed analytic
state contractions.

At a primitive N-th root, the polynomial identity
product_(j=0)^(N-1)(1-Q_N^j z)=1-z^N proves
sigma^N(e)=tau(e)=(1-z^N)e on the marked commensurate base. The
line map is not the identity. A Kummer norm-one gauge divides by
nu with nu^N=1-z^N, and so cannot replace the original lattice on
its zero divisor. The actual affine finite Ward source z^N/N is
also retained. No primality or odd-N assumption is used here.

## 2. The whole peripheral source requires its adapter

Set t=M^2 and keep the SAME original phase lift on both dimension
factors. The exact quotient is

    C_N(Q,M)=d_N^tr/d_N=(1-t^N)/(t;Q)_N.

At a generic regular M it equals one at Q=Q_N. Near M=1 its
regular continuation is obtained BEFORE evaluation:

    C_N=(1+t+...+t^(N-1))/product_(j=1)^(N-1)(1-tQ^j).

The denominator is N at (Q_N,t=1), so the ratio is a regular unit
there with value one. Holding M fixed and using D_Q=Q partial_Q
gives

    D_Q log C_N=sum_(j=1)^(N-1) j t Q^j/(1-tQ^j).

The sign is positive because this differentiates the reciprocal
product. At N=2, Q=-1, M=1 it is -1/2. Therefore the two dimension
lifts agree at the root but have different quantum-normal jets.
The phase cancels only because its actual whole lift was kept the
same on both sides.

Other norm-zero points may involve moving zero/pole intersections;
the local regularity statement above is specifically near M=1.
The note correctly retains the original rational lattice instead
of asserting a global unit adapter across every such point.

Finally, the actual fixed-N power W=M^(2N) satisfies W->Q^N W
under M->qM, while sigma fixes the independent dual coordinate w.
Their root values agree, but their whole normal dynamics do not.
Keeping the original d_N unchanged, as the construction does,
avoids imposing a false off-root equivariant identification.

The separate fixed-n exceptional-slope theorem is consistent with
this calculation: its rational-slope statement is a telescope over
shifted arguments, not an off-root equality R^b=(z;Q)_(aN).
