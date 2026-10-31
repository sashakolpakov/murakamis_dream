# Both outer transfer collars admit a controlled original-source filling

28 October 2026. This completes the upper-end counterpart of the
[all-input projected lower-collar theorem](actual_projected_transfer_cot_completion.md).
The original positive and negative physical crossings admit exact
cotangent contours with BOTH ends extended by N^alpha, alpha<1.
Every new integer pole is removable, uniformly over all physical
input states. The added contour pieces have exp(o(N)) operator cost.

This is a local operator identity which may be inserted in any fixed
original signed word with its closure unchanged. It does not estimate
the unrestricted bulk factors or identify a geometric saddle of the
full Fourier-projected density.

## 1. Retain the same original projected interpolation

Use d=N-1, Q=exp(2pi*i/N), x=-exp(-pi*i/N), and the full original
Cartan scalar kappa. With the exact completed factorial Fhat, set

    r(a,b;z)=kappa x^(-a-b+z)Q^(b(a-z))
                 Fhat(b+z)F_a/[Fhat(z)F_b Fhat(a-z)],
    Rhat(z)|a,b>=r(a,b;z) v_N(b+z) tensor v_N(a-z),
    v_N(nu)=sum_(j=0)^d
        [(exp(2pi*i*nu)-1)/(2pi*i*(nu-j))]|j>.          (1)

The removable component at nu=j is one. The vector is the actual
orthogonal Fourier projection onto the original physical head; it
vanishes at every integer outside 0,...,d and obeys

    ||v_N(nu)||<=exp(2pi|Im nu|).                       (2)

No physical head is replaced by a different representation or metric.
At integer k in 0,...,d, Rhat(k) is the original kth transfer slice.
The lower-collar proof establishes its zero at every negative integer
-s with 1<=s<N, including scalar poles canceled by invalid-output
projection zeros.

## 2. Exact N-shift and the upper base strip

Iterating the original first-shift equation gives an additional exact
identity of the SAME meromorphic factorial,

    Fhat(z+N)=(1-exp(2pi*i*z)) Fhat(z).                (3)

Indeed product_(r=1)^N(1-Q^(z+r))=1-exp(2pi*i*z).
This retains the full central factor; it is not replaced by its value
at a root. Put z=d+w. Applying (3) to the three affected factorials
gives the identity

    Fhat(b+d+w)F_a/[Fhat(d+w)F_b Fhat(a-d-w)]
      =[Fhat(b-1+w)/F_b]
        [F_a/Fhat(a+1-w)]
        [1-exp(-2pi*i*w)]/Fhat(w-1).                  (4)

The shared factors 1-exp(2pi*i*w) in numerator and denominator have
been canceled as meromorphic functions, not evaluated separately at
an integer. The remaining central factor in (4) is still explicit.

Fix T>0. On the fixed fractional strip 0<=Re w<=1, |Im w|<=T,
away from integers by a fixed positive distance, each expression on
the right of (4) has modulus bounded by a fixed power of N, uniformly
over every a,b in 0,...,d. Only such fractional points are needed on
the half-integer vertical and fixed-height horizontal edges below.

Here is the endpoint-uniform bound in detail. Set nu=1-w. The basic
fixed-argument Gamma product gives polynomial upper and inverse
bounds for Fhat(w), Fhat(nu) and Fhat(1-nu). For b>=1,

    Fhat(b-nu)/F_b
      =[Fhat(1-nu)/F_1]
          product_(j=2)^b (1-Q^(j-nu))/(1-Q^j).

Every quotient is at most 1+C_T/min(j,N-j), so the product is
polynomial by the harmonic sum. For b=0 use
Fhat(-nu)=Fhat(1-nu)/(1-Q^(1-nu)); the single denominator is at
least c_T/N on the stated fractional edges.

Likewise

    F_a/Fhat(a+nu)
      =Fhat(nu)^(-1)
          product_(j=1)^a (1-Q^j)/(1-Q^(j+nu)).

For j<=N-2 each quotient is at most
1+C_T/min(j,N-j-1). If j=N-1 occurs, treat it separately: its
denominator is at least c_T/N away from the excluded integer w=0,
and its numerator is bounded. This adds only a polynomial factor.
Finally

    1/Fhat(w-1)=(1-Q^w)/Fhat(w)

is polynomially bounded, as is 1-exp(-2pi*i*w) at fixed height.
These statements prove the uniform polynomial base bound for (4)
without hiding a large complete factorial or its inverse. The
original Cartan in (1) has bounded modulus at this fixed height,
since a,b are physical integers and its prescribed logarithms have
bounded imaginary coefficients.

## 3. All newly crossed upper integer poles are removable

Take k=N,...,2N-2. The factorial orders, directly from (3) and its
nonzero original strip, are:

    ord Fhat(k)=1,
    ord Fhat(b+k)=1+1_(b+k>=2N),
    ord [1/Fhat(a-k)]=1+1_(k-a>=N+1).

Thus the scalar r(a,b;z) at z=k has order

    1+1_(b+k>=2N)+1_(k-a>=N+1)>=1.                    (5)

Both outputs b+k and a-k are outside the physical band. The two
vectors in (1) therefore each supply one further zero. In particular
Rhat has a zero of order at least three at every such k, and its
complete cotangent density is holomorphic there. Even the scalar
coefficient already has a zero on this upper collar; the full
physical projection remains part of the operator identity.

The only factorial singularities in the collar are at these integer
points. There is no unrecorded noninteger pole. Formula (5) includes
the physical input endpoints and all their simultaneous collisions.

## 4. Uniform collar estimate and the two-sided contour identity

The exact step recurrence is

    r(z+1)/r(z)
      =xQ^(-b)(1-Q^(b+z+1))(1-Q^(a-z))/(1-Q^(z+1)).  (6)

On a half-integer vertical edge or a fixed nonzero-height horizontal
edge, each forward step costs at most C_T N: its single denominator
is bounded below by c_T/N, and the two numerators are bounded.
Starting with the base strip (4), for 1<=s<N/2 this proves

    ||pi cot(pi z)Rhat(z)||
       <=N^(C_T)(C_T N)^(s+1)                       (7)

on the boundary of d+1/2<=Re z<=d+s+1/2, |Im z|<=T.
The finite number N^2 of input columns adds only a factor N to the
operator bound. Equations (2) and (5), followed by the matrix maximum
principle, extend (7) throughout the filled upper collar.

The original contour encloses exactly the physical transfers
0,...,d. Extend its left edge to -s-1/2 and its right edge to
d+s+1/2, retaining both finite-height connecting pieces. The added
integers are -s,...,-1 and N,...,N+s-1. The lower theorem and (5)
show that every new pole of the complete density is removable.
Consequently, as an original physical operator,

    R_plus=integral_(extended rectangle)
                   pi cot(pi z)Rhat(z) dz/(2pi*i).   (8)

Each added collar has length O_T(s+1), and both have the conservative
uniform operator cost

    exp[O_T((s+1)log N)].                             (9)

For s<=N^alpha, alpha<1, this is exp(o(N)). The negative crossing
uses its exact antiunitary mirror
Rhat_minus(z)=Flip conjugate(Rhat_plus(conjugate z)) Flip,
with the conjugate full Cartan scalar. Its residue identity and both
collar bounds follow with the same orientations at the integer
residues. Finitely many such identities can be composed inside any
fixed signed braid word before its original marked closure is taken.

The scale is compatible with the earlier regular descent window.
In the normalized transfer variable z/N, a width s=N^(1-epsilon)
is a collar of width N^(-epsilon). The regular-region flow cost is
exp(O(N^(B epsilon) log^2 N)), while (9) costs
exp(O(N^(1-epsilon) log N)). Both are subexponential whenever
0<epsilon<1/B. Thus these two local quantitative estimates do not
require incompatible cutoff scales. Compatibility of scales alone
does not identify the off-grid Fourier-projected density with the
previous scalar phase or estimate its projection-angle currents.

The cost in (9) concerns the added operator contours, not the norm of
an arbitrary exterior contraction. The original residues 0,...,d,
the whole sinc/Fourier source and every framing/pivotal/peripheral
line remain. A claimed full-volume bound must still estimate the
remaining bulk current with this source retained.

The expanded [projected audit](../experiments/audit_actual_projected_transfer_cot_completion.py) checks every physical input a,b at N=2,...,8. It checks the exact N-shift and fractional identity (4) off the integer lattice, the full upper matrix zero orders at N through N+min(3,N-2), and both-collar cotangent residue sums against the original positive and negative E/Cartan crossing matrices. The positive kappa=q^((N-1)^2/2) and its negative inverse are included explicitly. These tests supplement the uniform proof and do not change its full physical-source scope or establish a sharp whole-knot volume estimate.