# A sharp projector barrier for the original repeated-crossing blocks

28 October 2026. The actual physical factorial frame gives a sharper
uniform bound when its spectral-projector interval products are estimated
together. Write v_3 for the regular ideal tetrahedron volume and v_8 for
the regular ideal octahedron volume. There are absolute constants C,A
such that, for every N>=2 and every integer ell,

    ||B_N^ell||_op
       <= C N^A(1+|ell|) exp[N(2v_3+v_8)/pi].           (1)

B_N is the ORIGINAL complete crossing in the balanced physical metric,
with its original unit Cartan and framing factors. The HS estimate costs
one further factor N. No spectrum-only or semisimplicity assumption is
used. The proof retains the actual nilpotent blocks by the meridian
Cauchy argument in [the factorial-frame theorem](actual_twist_block_factorial_frame_bound.md).

This improves that theorem's volume constant 12v_3 to 4v_3+2v_8.
It is a coarse bound for the whole original knot source at arbitrary
braid width, not the desired sharp hyperbolic-volume estimate.

## 1. The entire projector product, with its physical domain

Keep the actual degree-T bidiagonal Casimir and interval-projector formula
from Sections 3--5 of the factorial-frame theorem. Let integer indices
0<=r<=k<=s<N obey 0<=T-s<=T-r<N. Its projector entry is

    (E_k)_(r,s)=product_(l=r+1)^s b_l(M)
                 /product_(l=r,l!=k)^s(c_k(M^2)-c_l(M^2)).

Put J(u)=integral_0^u log(2sin(pi t))dt on [0,1], and extend J
periodically. This is consistent because J(1)=0. In the following
formula T,r,s,k denote the integer indices DIVIDED by N. The exact
root-factorial identities give the leading projector exponent

    p(T,r,s,k)=J(s)-J(r)+J(T-r)-J(T-s)
               -J(k-r)-J(s-k)-J(k+s)+J(k+r).           (2)

The last two terms use the periodic extension. The physical domain is

    0<=r<=k<=s<=1,  0<=T-s<=T-r<=1.                  (3)

The numerator consists of two ordinary interval products. The first
denominator is |F_(k-r)F_(s-k)|. The second is a circular root interval,
with one factor omitted and at most one complete-meridian zero. Thus
the endpoint-uniform factorial estimate gives (2) with error O(log N)
after removing that possible zero. The +1 in k+l+1 shifts endpoints
by 1/N; the logarithmic modulus of continuity of J bounds its effect
by O(log N), uniformly even at the endpoints. This does not assume
uniform separation from a root.

On the specified circle

    |M-1|=delta=1/[8N^3(1+|ell|)],

all noncolliding products change by a uniformly bounded factor, using
the harmonic sum of their relative changes. The one possible zero
costs at most C delta^(-1). The prefactors which are not exactly unit
off the complete fiber have modulus exp(O(N delta)). Consequently

    |(E_k)_(r,s)|
       <=C_0 N^A0(1+|ell|) exp[N p(T/N,r/N,s/N,k/N)].  (4)

Here the notation on the right restores integer indices. The constants
are independent of the degree block and of the chosen spectral node.

## 2. Exact maximization of the projector exponent

Let G(u)=log|2sin(pi u)|, periodically extended. For 0<=l<=1,
every interval of length l has its G-integral between

    B(l)=2J(l/2),
    A(l)=J((1+l)/2)-J((1-l)/2)=-2J((1-l)/2).           (5)

Indeed G is symmetric and increases strictly with distance from its
integer zero until that distance reaches 1/2. The minimum interval is
centered at an integer and the maximum at a half-integer. Alternatively,
differentiate J(t+l)-J(t): its regular stationary intervals have exactly
these two centers. Moving through a singular endpoint gives the same
ordering by continuity and monotonicity. The cases l=0,1 follow by limits.

Set l=s-r. Both numerator differences in (2) are integrals over an
interval of length l, so each is at most A(l). The last difference,
J(k+s)-J(k+r), is at least B(l). The remaining split denominator obeys

    J(k-r)+J(s-k)>=2J(l/2).                           (6)

For 0<l<1 this follows directly from strict convexity:

    d^2/dx^2 [J(x)+J(l-x)]
       =pi sin(pi l)/[sin(pi x)sin(pi(l-x))]>0.

Symmetry places the minimum at x=l/2; the endpoints follow by continuity.
Combining (5)--(6) gives

    p<=2A(l)-4J(l/2)
      =-4[J((1-l)/2)+J(l/2)]
      <=-8J(1/4)=v_8/pi.                              (7)

For the last inequality the two arguments have sum 1/2, and the same
convexity calculation places their minimum at 1/4 each. Equality in
ALL these inequalities holds at

    T=1, r=1/4, s=3/4, k=1/2.

These values satisfy (3). Thus v_8/pi is the exact maximum of the
specified projector profile, not an estimate obtained by separately
maximizing its factorials. The identity -8J(1/4)=v_8/pi uses
v_8=8 Lambda(pi/4) and J(u)=-Lambda(pi u)/pi.

## 3. Restore both physical frames, eigenvalues and the complete source

The explicit physical fusion and its inverse each have norm
exp[2 gamma_* N+O(log N)], where gamma_*=v_3/(2pi). Both are necessary.
The spectral eigenvalue powers are bounded on the delta circle;
the full original Cartan obeys

    kappa(M)/kappa(1)
       =M^(N-1) exp[(Log M)^2/(2Log q)],

whose ell-th power is bounded there too. Summing projectors costs
only a polynomial. Equations (4)--(7) therefore bound the full matrix
power on the circle by

    C N^A(1+|ell|) exp[N(4gamma_*+v_8/pi)].

The original matrix power is holomorphic across M=1 for either sign
of ell. Cauchy's formula transfers this estimate to its center without
another inverse delta. Since 4gamma_*+v_8/pi=(2v_3+v_8)/pi, this proves
(1), including the complete nilpotent normal contribution.

For a fixed b-strand braid closing to a knot, the original reduced cut is

    K_N I=theta_N^(-w) Tr_env[W_N(I tensor g_N^(tensor(b-1)))],

where the retained complete pivot g_N is unitary and |theta_N|=1.
Expanding that partial trace in an orthonormal environmental basis gives

    |K_N|<=N^(b-1)||W_N||_op.                          (8)

This is a norm bound for the actual complex pivotal trace, not a claim
that it is positive. Partition the specified word into consecutive
repeated-generator blocks with nonzero exponents ell_t. The matrices
are coherently multiplied inside each block BEFORE estimating. From
(1), (8), and the independently proved one-crossing exponent,

    limsup_N (2pi/N)log|K_N|
       <=sum_t min(|ell_t|v_8, 4v_3+2v_8).             (9)

This applies to odd or even braid width and either sign of each block.
It implies the corresponding full Fourier-energy upper bound by the
audited polynomial ordinary-color remainder. The complete full-state
modified-dimension factor is a specified root phase divided by N, so
its exponential rate obeys the same estimate. None of those factors
has been reset at an intermediate meridian.

Every block of at least four crossings improves its separate-crossing
bound, since 4v_3+2v_8<4v_8. The block must be a repeated generator of
the specified braid; arbitrary diagram twist regions would require a
proved tangle conversion. Formula (9) has not been shown to be bounded
by Vol(S^3 minus K). It proves neither the sharp upper bound nor
geometric survival.

## 4. Verification

The root agent independently checked the actual factorial-frame proof
and replayed its 240 generic-meridian signed-degree comparisons. Two
other agents independently verified (2)--(7), including the circular
interval and endpoint shifts. The supplementary audit
`experiments/audit_actual_twist_block_projector_barrier.py` checks the
profile inequalities, exact factorial products after zero removal,
physical endpoint domains and convergence at the maximizing profile.
These checks supplement the uniform proof above.
