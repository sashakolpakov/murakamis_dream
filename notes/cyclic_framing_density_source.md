# The prefix-adapted framing density has an exact cyclotomic source factor

Research calculation, 27 October 2026. This computes an actual finite
root-filter functional on the rational density supplied by the
[prefix-adapted framing chart](prefix_adapted_two_position_framing_cover.md).
The result keeps an explicit power character and its cyclic norm.
It is not a proof that this root filter is the original source after
geometric Gaussian pushforward. That interchange remains unproved.

## 1. The density, with the physical prefix retained

Fix the complete parabolic meridian mark. Use signed developed prefix
products U,V from the actual braid-to-Gauss dictionary; the physical
inverse position is k=ell_U/ell_V. On the framing torsor write

    P = [[r, r(1-r)/s], [s,1-r]],
    ell_W = Tr(W P),
    A=1/(1+s), B=1/k.

For a matrix W write c_W=W_21 and h_W=W_11-W_22. The equation
ell_(U-kV)=0 is quadratic in r. In the regular quadratic field put

    D = partial_(r/s) ell_(U-kV).

The actual framing two-form is

    Omega = ell_V/(B D) dlog A wedge dlog B.        (1.1)

Its field trace over the two-position base is

    Tr Omega = T(B) dlog A wedge dlog B,
    T(B) = W B/(c_U B-c_V)^2,
    W = c_V h_U-h_V c_U.                          (1.2)

In particular it need not be zero. The earlier special case V=I
had W=0 and an odd unweighted density; that case cannot be used
for an arbitrary physical edge. The chart note proves (1.1)--(1.2)
from the actual prefix dictionary.

For completeness the elementary trace calculation is short. Put
tau=r/s, C=U-kV, and write

    ell_C = -s c_C tau^2+(c_C+s h_C)tau+d_C+s b_C.

At its two simple roots the values of D are opposite. Reducing the
quadratic ell_V modulo ell_C, or subtracting its two root values,
gives

    Tr(ell_V/D) = (c_V h_C-h_V c_C)/c_C^2
                = W/(c_U-k c_V)^2.

Multiplication by 1/B gives (1.2). Notice that the trace coefficient
has no remaining s dependence.

The coefficients in (1.2) are intrinsic marked character functions.
With the reference cut meridian J=[[1,1],[0,1]], direct multiplication
gives

    c_W = Tr(J W)-Tr(W),
    W = Tr(J(VU-UV)).                             (1.3)

Thus c_U,c_V,W, and their ratios below are rational trace-word
functions of the marked representation. Conjugating while retaining
J does not change them. Equivalently its residual unipotent
centralizer fixes c_W and changes h_W by a common multiple of c_W,
which cancels from W. They live on the marked character cover, not
in the free framing-coordinate field. On a geometric component
generically finite over the peripheral curve, they are algebraic
over its A-curve field. The identities here concern the complete
parabolic slice; no independent full holonomy deformation is imposed.

## 2. Exact root averaging is a derivative of a cyclic norm

Suppose c_U!=0, W!=0, and set

    lambda=c_V/c_U, gamma=W/c_U^2,
    T(B)=gamma B/(B-lambda)^2.                    (2.1)

Let Q be a primitive N-th root and assume lambda^N!=1. Define the
finite algebraic functional

    A_N(T) = (1/N) sum_(b=0)^(N-1) T(Q^b).

Then, EXACTLY,

    A_N(T) = gamma N lambda^(N-1)/(1-lambda^N)^2.  (2.2)

No limiting operation or quantum expansion is involved in (2.2).
To prove it, first use the literal cyclic norm

    product_(b=0)^(N-1)(1-lambda Q^(-b))
                       = 1-lambda^N.             (2.3)

With theta=lambda partial_lambda, direct differentiation gives

    T(B)=-(gamma/lambda) theta^2 log(1-lambda/B).

Applying theta twice to log (2.3) proves (2.2). Logarithms are only
notation for logarithmic derivatives of rational functions here;
no branch of a logarithm is needed. Equivalently the ordinary
partial-fraction identity for B^N-1 proves the same formula.

The case lambda=0 is taken directly: T(B)=gamma/B and A_N(T)=0
for N>1. Formula (2.2) is then interpreted by its polynomial limit.
The displayed rate assertions below assume lambda!=0.

This also has a WHOLE off-root representative. Before setting
Q^N=1 retain

    P_N(Q,lambda)=product_(b=0)^(N-1)(1-lambda Q^(-b)).

For arbitrary nonzero Q, away from the specified poles,

    (1/N)sum_b T(Q^b)
        = -gamma/(N lambda) theta^2 log P_N.       (2.4)

Only after taking the actual whole derivatives may P_N specialize
to (2.3). Its Q derivative is

    Q partial_Q log P_N
      = sum_b b lambda Q^(-b)/(1-lambda Q^(-b)).   (2.5)

Specializing (2.3) first and differentiating it would incorrectly
erase this current. The exact finite product retains the quantum
normal, its moments, and its source factors.

## 3. A nonzero rational density can acquire an exponential source weight

At any fixed complex lambda with 0<|lambda|!=1 and gamma!=0,
(2.2) implies

    lim_(N->infinity) (1/N)log|A_N(T)|
                         = -|log|lambda||.        (3.1)

For |lambda|<1 the denominator tends to one, and the numerator
has rate log|lambda|. For |lambda|>1 factor lambda^(2N) out of
the denominator; the resulting rate is -log|lambda|.

There is no contradiction with the polynomial bounds for a fixed
algebraic coefficient on one controlled arc. A_N has a growing
cyclic norm and power character; it is not evaluation of one fixed
algebraic function of Q near one. Nor does (3.1) prove that the
actual geometric coefficient is exponentially small. The source
pairing has not been shown to commute with this field trace and
principal-density sampling. It does show that such an interchange
cannot be declared harmless merely because T is rational and
pointwise nonzero.

Ordinary B residues do not replace this functional either. The
one-form T(B)dlog B=gamma dB/(B-lambda)^2 is exact and has zero
ordinary residues. Its finite cyclic average (2.2) is nevertheless
nonzero. The marked source and its cyclic norm supply information
which absolute de Rham exactness would lose.

## 4. A calibration on the actual figure-eight representation chart

The prefix chart note constructs a fixed triple for the actual
mixed braid (1,-2,1,-2), over u^2+u+1=0. For its third physical
strand the signed developed prefix products reduce to

    V = [[1,1],[-u,1-u]],
    U = [[u+1,2u+1],[1-u,3-u]].

These are determinant-one matrices. The chart computation gives

    W=2u+1,  lambda=1/(u+2),  gamma=-lambda.

Consequently (2.2) becomes

    A_N(T)=-N lambda^N/(1-lambda^N)^2,             (4.1)
    |lambda|=1/sqrt(3).

At either marked geometric embedding its rate is therefore
-log(3)/2. This is a calibration of the exact density functional,
not a recomputation of Kashaev's figure-eight invariant. In
particular it must not be inserted as a new prefactor in that
invariant. A source-preserving comparison must instead explain
how this character and its dual/source normalization are transported.
The example tests a general prefix formula; the conjecture target
remains unrestricted hyperbolic knots.

The [symbolic audit](../experiments/audit_cyclic_framing_density_source.py)
checks the cyclic norm, an independent companion-matrix trace,
the whole off-root current, and the exact figure-eight field values.
