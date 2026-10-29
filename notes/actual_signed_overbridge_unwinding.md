# Exact simultaneous unwinding of signed overbridge interiors

28 October 2026. Every interior strand contraction within an original
overbridge has an exact closed root-of-unity formula, for arbitrary
signs and arbitrary regular spectator grids. This is a degree-complement
identity, not a Vandermonde formula requiring a central norm to be one.
It eliminates ALL such interior variables simultaneously in the original
network. Surviving clocks are monotone along each bridge, and the finite
binomial factors telescope to a q-multinomial.

The spectator-dependent original crossing normalizers and the entire
original boundary source remain. The result is still a coupled sum;
it does not prove scalar noncancellation or permit an automatic second
pass through the underbridges.

## 1. Original port coordinates and all four signed roles

Use N>=2, d=N-1, Q=exp(2*pi*i/N), x=-exp(-pi*i/N), so x^2=Q^(-1).
The actual signed crossing is in its proved regular propagated Fourier
frames. Denote inputs by z0,z1 and outputs by z6,z7. The physical OVER
pair is (z0,z7) for a positive crossing and (z1,z6) for a negative
crossing. The other pair is the UNDER pair. Root propagation is

    positive: (r6,r7)=(x r1,x r0),
    negative: (r6,r7)=(x^(-1)r1,x^(-1)r0).         (1)

Every grid has its actual label in 0,...,N-1, written i,j,k,l at
ports 0,1,6,7 respectively. With the opposite physical pair fixed
on its original grids, the exact conditional two-leg kernel is
rank one. Write it as

    M_sigma(Zout,Zin)=c_sigma Pout(Zout) Pin(Zin). (2)

The full scalar is fixed, for ANY old-grid reference pair, by

    c_sigma=M_sigma(Zout*,Zin*)
                      /[Pout(Zout*)Pin(Zin*)].      (3)

Here M_sigma is the ORIGINAL exact balanced Fourier entry, including
kappa, the actual Gaussian, every affine logarithmic mark and all
central factors. It is not an unknown knot period. Every denominator
in (3) is nonzero on the regular old grids. Crucially c_sigma depends
on BOTH spectator labels and roots and retains a leading phase.
The closed formulas below show its modulus is tame on the original
fixed-central grids. It is never discarded in the contractions.

After reordering an opposite-root product by

    (aZ;Q^(-1))_L=(a Q^(1-L) Z;Q)_L,

the signed table has a particularly uniform form. Write
(w;Q)_L=product_(j=0)^(L-1)(1-Q^j w).

| Sign, physical role | Clock h in 0,...,d | Pin(Z) | Pout(Z) | b | a |
| --- | --- | --- | --- | --- | --- |
| +, over (0,7) | (j-k) mod N | Z^(-h)(b/Z;Q)_(d-h) | (aZ;Q)_h | z1/x | Q^(-h)/(x z6) |
| -, over (1,6) | (l-i) mod N | Z^(-h)(b/Z;Q)_(d-h) | (aZ;Q)_h | Q^(h+2)x z0 | Qx/z7 |
| +, under (1,6) | (i-l) mod N | (b/Z;Q)_h | Z^h(aZ;Q)_(d-h) | Q^(1-h)x z0 | Q^(h+1)/z0 |
| -, under (0,7) | (k-j) mod N | (b/Z;Q)_h | Z^h(aZ;Q)_(d-h) | x^(-1)z1 | Q/z1 |

The positive entries are the actual
[paired port interpolants](actual_fourier_port_polynomials_and_profiles.md).
For the negative entries apply the COMPLETE antiunitary relation
R_minus=P conjugate(R_plus)P, including kappa, and then reorder the
Q^(-1) products. This is a finite polynomial identity; no contour
shift or unrecorded Gaussian removal is used. The changed clock
representatives in the table include the reversed Fourier labels.

On the corresponding spectator grids, ALL four rows also satisfy

    a b=Q^2 x.                                     (4)

For example in the positive over row z6=x z1 Q^(-h), so
a b=Q^(-h)z1/(x^2 z6)=Q/x=Q^2x. The other rows follow directly
from (1) or x^2=Q^(-1). This identity is useful but is not required
by the arbitrary-parameter contraction below.

### Closed original normalizers, with no hidden exponential modulus

In fact the scalar (3) is elementary for EVERY signed role:

    c_(+,over) =kappa/N (-1)^h Q^(h(h+1)/2) z6^h,
    c_(+,under)=kappa/N (-1)^h Q^(h(h+1)/2) z0^(-h),
    c_(-,over) =kappa^(-1)/N (-1)^h Q^(-h(h+1)/2) z7^h,
    c_(-,under)=kappa^(-1)/N (-1)^h Q^(-h(h+1)/2) z1^(-h). (4a)

These include the ORIGINAL full Cartan scalar. Here is a derivation
from the physical matrix, independent of an asymptotic full-function
normalizer. The original positive coefficient, for input (a,b),
output (a+b-j,j), is

    kappa x^(-b-j) Q^(jb)
       F_(a+b-j) F_a/[F_(a-j) F_b F_j],
    F_t=(Q;Q)_t.

For the over factor extract the Fourier coefficient z0^(-h)z7^0.
The lowest Pin coefficient and constant Pout coefficient are both one,
so this coefficient is exactly c. The original two-head Fourier
normalization gives

    c=kappa z6^h/N^2 *F_h
         sum_(t=0)^(d-h) [h+t choose t]_Q Q^(-ht).

The spectator grid gives z6/(x z1)=Q^(-h), including the cyclic
representative. Root complementation turns the summand into
(-1)^t Q^(t(t+1)/2)[d-h choose t]_Q. The finite q-binomial theorem
therefore makes the sum F_(d-h). Finally

    F_h F_(d-h)=N (-1)^h Q^(h(h+1)/2),

by factoring F_d=N into the last h factors. This proves the first
formula. For the under factor extract input degree zero and output
degree h; the same sum has z0^(-h) in place of z6^h. The original
antiunitary flip proves the two negative formulas. Reordering its
opposite-root Pochhammers permutes factors and adds no scalar.

If all central moduli range in a fixed compact subset of (0,infinity),
then uniformly in ALL spectator labels and clocks

    c_0/N <= |c_sigma| <= C_0/N.                    (4b)

Indeed |z|^h=|z^N|^(h/N), 0<=h<N, and every other factor in (4a)
has modulus one. The constants depend only on the chosen central
compactum. The phase Q^(+/-h(h+1)/2) remains exponentially
oscillatory as h scales with N; (4b) does not make the weights positive.
During a later deformation to fixed nonunit port radii the monomials
in (4a) must still be retained; (4b) concerns the original fixed-central
sampling grids and bounded changes of their centers.

## 2. The degree-complement contraction

Let 0<=L,s<=d and a,b be arbitrary nonzero parameters. Then

    CT_Z Z^(-s)(aZ;Q)_L(b/Z;Q)_(d-s)
       =0,                                      if s>L,
       =(-a)^s Q^(s(s-1)/2) [L choose s]_Q
                   *(ab Q^(-1);Q)_(L-s),        if s<=L.  (5)

This is a polynomial identity in a,b; it holds at every primitive
root of order N, including even and composite N. There is NO
condition (ab)^N=1. The mirrored identity is

    CT_Z Z^r(aZ;Q)_(d-r)(b/Z;Q)_K
       =0,                                      if r>K,
       =(-b)^r Q^(r(r-1)/2) [K choose r]_Q
                   *(ab Q^(-1);Q)_(K-r),        if r<=K. (6)

Proof of (5). Only powers i=s+j from the first polynomial and j
from the second can contribute. Root complementation gives

    [d-s choose j]_Q
       =(-1)^j Q^(-sj-j(j+1)/2)[s+j choose j]_Q.

Use

    [L choose s+j]_Q [s+j choose j]_Q
       =[L choose s]_Q [L-s choose j]_Q.

After extracting (-a)^s Q^(s(s-1)/2)[L choose s]_Q, the remaining
sum is the finite q-binomial expansion of (abQ^(-1);Q)_(L-s).
There are no zero denominator factorials: every index is at most d.
If s>L the two frequency intervals are disjoint. Exchanging Z with
Z^(-1), and a,L with b,K, proves (6).

For comparison the general contraction of
Z^(r-s)(aZ;Q)_L(b/Z;Q)_K is a terminating 2phi1. For s>=r its
argument is ab Q^(L+K), and its three parameters are

    Q^(s-r-L), Q^(-K); Q^(s-r+1).

In (5), K=d-s and r=0, so Q^(-K)=Q^(s+1) cancels the denominator
AUTOMATICALLY. This explains why an ordinary tuned Vandermonde
test misses the actual generic bridge identity.

## 3. Exact arbitrary-length signed bridge contraction

Consider an overbridge with m crossing encounters, in their physical
strand order, and with every spectator pair fixed on its actual
grids. Put h_j,a_j,b_j,c_j for the data of (2)--(3) at encounter j.
This includes arbitrary changes of crossing sign. Let Zin and Zout
be the first input and last output grid values. Every ordinary
internal physical strand edge is a finite Fourier contraction.
Its summand has frequencies between -d and d, so root averaging
has NO nonzero alias. Consequently summation over its N labels
is N times the constant term in (5).

The exact conditional bridge kernel is zero unless

    d>=h_1>=h_2>=...>=h_m>=0.                      (7)

If (7) holds, put Delta_j=h_j-h_(j+1). Its kernel is exactly

    N^(m-1) (product_(j=1)^m c_j)
       *Zin^(-h_1)(b_1/Zin;Q)_(d-h_1)
       *(a_m Zout;Q)_(h_m)
       *product_(j=1)^(m-1) W_j,

    W_j=(-a_j)^(h_(j+1)) Q^(h_(j+1)(h_(j+1)-1)/2)
          *[h_j choose h_(j+1)]_Q
          *(a_j b_(j+1) Q^(-1);Q)_(Delta_j).       (8)

The factor N per eliminated wire is essential: it is a SUM of
normalized Fourier matrix entries, rather than an already averaged
constant term. Formula (8) retains every c_j and original local
normalization. Untouched physical heads simply identify their
successive grid labels and do not alter the formula.

The q-binomial factors telescope:

    product_j [h_j choose h_(j+1)]_Q
       =F_(h_1)/[F_(h_m) product_j F_(Delta_j)],
    F_r=(Q;Q)_r.                                   (9)

This is a q-multinomial with total charge h_1. The lengths in the
new bridge Pochhammers sum to h_1-h_m<=d, independent of m.
Including the two endpoint Pochhammers, their total length is EXACTLY

    (d-h_1)+h_m+sum_j Delta_j=d.                   (9a)

There is a stronger bound for the COMPLETE non-Pochhammer,
non-multinomial prefactor, uniform even in bridge length. Let u_j
be its spectator output, z6 for a positive encounter and z7 for a
negative encounter. The signed table gives |a_j u_j|=1. Combining
(4a), all link monomials and the endpoint Zin^(-h_1), its modulus is
EXACTLY

    1/N * [ product_(j<m) |u_j^N|^(Delta_j)
                  *|u_m^N|^(h_m)/|Zin^N|^(h_1) ]^(1/N). (9b)

The positive exponents in the numerator sum to h_1<=d. If all
central moduli lie between c_min>0 and c_max, (9b) therefore lies
between c_min/(N c_max) and c_max/(N c_min), independently of
bridge length. Thus the displayed q-multinomial and total-degree-d
Pochhammer products carry ALL of this conditioned bridge's
exponential modulus. Their phases and the phases in (4a) all remain.
Using (4), their arguments can also be written

    a_j b_(j+1)Q^(-1)=x^(-1)a_j/a_(j+1).          (10)

For a fixed bridge, if every (a_j b_(j+1))^N differs from one,
all Pochhammer factors in (8) are nonzero, so (7) is exactly its
support condition. If a central ratio is one there can be further
zeros. The complete Pochhammer in (8) must then remain; no such
boundary factor is divided out. The formula itself is valid there.

The analogous underbridge statement follows from (6): its clocks
are nondecreasing, and its q-binomial factors and lengths telescope
in the opposite order. This is a separate conditional statement.

## 4. Simultaneous whole-source overbridge unwinding

Take ANY signed braid network in the regular propagated frames,
with the ORIGINAL endpoint source. Include every specified cup,
ordinary cap, FULL marked cap, pivot and external scalar exactly.
At an existing source coupon stop a bridge; this does not remove or
replace the coupon. A pure pivotal continuation could instead be
included as its exact Q-shift and scalar, but this is unnecessary.

Select all ordinary strand edges whose first endpoint is an OVER
output and whose second endpoint is an OVER input. After suppressing
untouched identity-head layers, these edges form disjoint directed
paths of crossing over-pairs. Time order excludes directed cycles in
an open braid. Each crossing belongs to exactly one path, possibly
of length one. These are the maximal overbridges relative to the
retained original source cuts.

Freeze the labels on every unselected wire, including all original
source ports. A selected variable is incident only to the two OVER
ports of its neighboring crossings. In particular it occurs in NO
spectator UNDER pair. Thus at every crossing (2) applies throughout
the selected sums. All sums are finite and all selected paths are
disjoint. Their factors separate, so (8) can be applied simultaneously
to EVERY path, without invalidating any other path's grid hypothesis.
Then sum the remaining labels and apply the SAME endpoint source.
This proves exact equality with the original whole knot scalar,
and in fact with the entire endpoint operator before its final source.

This is an arbitrary-width, arbitrary-sign, arbitrary-bridge-count
identity. It is not limited to a twist family or to a special knot.
For a diagram source with a nonordinary continuation or a turning
coupon, keep that coupon and its incident endpoint labels; no
unproved sliding or deletion of it is part of the theorem.

## 5. The coupling that remains

Every reduced path coefficient still depends on its spectator
under-port labels through h_j,a_j,b_j and the explicit phases and
monomials c_j in (4a). Those
ports occur in other paths' coefficients and in the original
boundary source. The remaining label sum is therefore coupled.
Monotonicity (7) and the multinomial (9) survive exactly within
every path, but do not make different paths independent.

One cannot automatically repeat the operation on ALL underbridges.
After the first pass, an under-port variable appears in the new
coefficients (8), the length choices h_j, and the original c_j of
several overbridges. Its dependence is no longer the isolated
complementary pair of (6). A second elimination would need a new
identity for this whole transformed source. Likewise, conditional
nonzero coefficients in (8) do not exclude cancellation in its
remaining whole knot sum.

The proved advance is a closed, source-preserving integration of
all original overbridge interiors and an explicit monotone charge
simplex on each bridge. Relating the remaining coupled period to
the global geometric cycle and proving its selected coefficient
are still required for a volume limit.

## 6. Reproducible audit

    python3 experiments/audit_actual_signed_overbridge_unwinding.py

The audit checks every complementary clock pair at several primitive
roots and arbitrary parameters, all four signed port tables against
ORIGINAL physical crossing matrices, arbitrary-length mixed-sign
bridge contractions, and simultaneous whole signed-word elimination
with the ORIGINAL full cup/cap/marked source. No replacement invariant
or arbitrary boundary vector is used for the whole-source tests.
