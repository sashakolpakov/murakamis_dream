# An independent root-Fourier certificate for the trivalent black scalar

29 October 2026. This derives an EXACT Euler-polynomial coefficient
formula from the actual highest/descendant source. It proves its
integer saturation support J>=d by cancellation of a complete Fourier
mode. The positive C R identity is not assumed in this derivation;
its remaining finite transformation is now separately
[proved](finite_trivalent_euler_racah_transform.md). This coefficient
certificate retains all original phases and root endpoint currents.

Let N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, F_a=(Q;Q)_a.
Assume integer 0<=j_i<=floor(d/2) satisfying the triangle inequalities,
and put r=j_2+j_3-j_1 and J=j_1+j_2+j_3. Thus 0<=r<=2min(j_2,j_3).
Use the original balanced coproduct and highest vectors
h^(j)_k=q^(k^2)[d-j choose k]_Q. The selected actual black coefficient
is N^3 A, with

    A=q^[-j_1(d-2j_1)] sum_k x^[k+j_1+j_3-2d]
       conjugate[h^(j_1)_k h^(j_3)_k
          W^(j_2)_r(j_3+k,d-j_1-k)].                 (1)

Here k=0,...,min(d-j_1,d-j_3), W^(j)_r=F_pair^r h^(j)/F_r.
This is the literal endpoint extraction of the all-port vertex,
including its lowest-column phase; no generic 6j formula is used.

## 1. Exact coefficient theorem

Define the unnormalized Jackson difference

    D_Q g(T)=[g(T)-g(QT)]/T,
    D_Q T^h=(1-Q^h)T^(h-1),
    f(T)=(TQ^(1-j_3);Q)_(j_3),
    g(T)=(TQ;Q)_(j_2).

The source-exact identity is

    A= N q^E/[F_(j_1)F_(j_2)F_(j_3)F_r]
                         *[T^d] g(T)^2 D_Q^r f(T)^2,
    E=3j_1^2+j_2^2+j_3^2-2j_1j_2-2j_1j_3
                              +2j_2j_3-2j_3-2.       (2)

Every polynomial and denominator is finite; all denominator indices
are below N. In particular deg(g^2 D_Q^r f^2)=J, so

    J<d implies A=0 EXACTLY.                         (3)

This is an original-source cancellation before taking absolute
values, not an admissibility rule imposed on a guessed 6j symbol.

## 2. Own finite Fourier proof

The original coproduct binomial gives, with b=d-j_1-k,

    W^(j_2)_r(j_3+k,b)=F_(j_3+k)F_bF_(d-j_2)
      *sum_z q^(z^2)x^[-r+j_3+k-z]
       Q^[z(r-j_3-k+z)]
       /[F_z^2 F_(d-j_2-z)^2 F_(j_3+k-z)
                                      F_(j_2-j_1-k+z)].

The range is exactly where every displayed denominator index is
nonnegative and <N. Substitute this and the two highest vectors
in (1). Use only

    conjugate(F_a)=(-1)^a Q^[-a(a+1)/2]F_a,
    F_(d-a)=N(-1)^a Q^[a(a+1)/2]/F_a,
    q^N=-1.

After the factors N cancel, the result is

    A=(-1)^(j_3)q^B/[F_(j_1)F_(j_2)F_(j_3)]
      *sum_(k,z) (-1)^(k+z)
       q^[(k-z)^2+(1+2j_1-2j_2)k+(1-2j_3)z]
       [(Q^(k+1);Q)_(j_3)(Q^(z+1);Q)_(j_2)]^2
       /[F_(j_3+k-z)F_(j_2-j_1-k+z)],
    B=3j_1^2-2j_1j_2+j_2^2-j_3-2.                  (4)

Equation (4) displays all phase bookkeeping; no root sign is left
in an unspecified scalar. Put l=k-z and p=j_3+l. The two last
factorials force p=0,...,r. For fixed p the z-dependent factor is

    Q^[(1-r)z]
       (Q^(z+p-j_3+1);Q)_(j_3)^2(Q^(z+1);Q)_(j_2)^2.

Its sum extends EXACTLY to z=0,...,N-1. For z>d-j_2 the second
Euler factor contains 1-Q^N. If k=z+p-j_3<0 then k>=-j_3 and the
first factor contains 1-Q^0; if k>d-j_3 it contains 1-Q^N. There
is no k>=N wrap because z<=d-j_2 and p-j_3<=j_2-j_1 imply k<=d-j_1.
Thus all added states are killed by their literal factorial zeros.

For a polynomial P(T) of degree <=2(j_2+j_3)<2N, complete root
Fourier summation consequently selects precisely

    sum_(z=0)^(N-1) Q^[(1-r)z]P(Q^z)
                =N([T^(r-1)]P+[T^(N+r-1)]P).         (5)

Absent or negative coefficient indices mean zero. The p sum in (4)
is, after its explicit constant phase is extracted,

    H(T)=sum_(p=0)^r (-1)^p Q^[p(p-1)/2+(1-r)p]
                   [r choose p]_Q f(Q^pT)^2.

If f(T)^2=sum_h c_h T^h, the finite binomial theorem gives

    H(T)=sum_h c_h T^h(Q^(1-r+h);Q)_r
         =T^r D_Q^r f(T)^2.                         (6)

In fact for h<r the product contains 1-Q^0, while for h>=r it
equals F_h/F_(h-r). Therefore the LOW Fourier coefficient r-1 in
(5) vanishes EXACTLY. The surviving high coefficient is
[T^(N+r-1)]g^2H=[T^d]g^2D_Q^r f^2. The p-independent phase in
(4) is q^E, with E as in (2), and its factorial denominator is F_r.
This proves (2) and (3), including r=0 and all level parities.

## 3. A finite low-degree version at saturation depth delta

For delta=J-d>=0, put c_e=[U^e](U;Q)_(j_3)^2. Reversal of the
two finite Euler products in (2) gives

    [T^d]g^2D_Q^r f^2
      =Q^[j_2(j_2+1)-j_3(j_3-1)] [U^delta]
       (UQ^(-j_2);Q)_(j_2)^2
       *sum_(e=0)^(2j_3-r) c_e
                       F_(2j_3-e)/F_(2j_3-e-r) U^e. (7)

Thus only coefficients <=delta need be computed. All denominator
indices in (7) are physical: delta<=j_i and delta<=2j_3-r follow
from the bounds on the other two j's. For any fixed saturation depth
this is a fixed-length source formula, with no unspecified boundary
data or q-normal derivative. It is not claimed that its summands
have a common phase.

## 4. Two entire saturation layers are manifestly nonzero

Let

    Lead=Q^[j_2(j_2+1)-j_3(j_3-1)]
                              F_(2j_3)/F_(2j_3-r).

This is the NONZERO leading coefficient of g^2D_Q^r f^2. Therefore
on the entire layer delta=0, equation (2) gives

    A=Nq^E Lead/[F_(j_1)F_(j_2)F_(j_3)F_r]!=0.      (8)

For delta=1, so J=N, the next-to-leading coefficient divided by
Lead is

    -2/(1-Q) [Q^(-j_2)(1-Q^(j_2))
             +(1-Q^(j_3))(1-Q^(2j_3-r))/(1-Q^(2j_3))]
      =2Q^(-2j_2)(1-Q^(j_2))(1-Q^(j_2+j_3))
                                      /[(1-Q)(1+Q^(j_3))]. (9)

The first equality follows by taking the next coefficient in the two
Euler squares before the Jackson derivative: their ratios are
-2sum_(a=1)^(j_2)Q^-a and -2sum_(a=0)^(j_3-1)Q^a; the derivative
multiplies the latter ratio by (1-Q^(2j_3-r))/(1-Q^(2j_3)).
For the second equality use 2j_3-r=J-2j_2=N-2j_2 and cancel the
factor 1-Q^(j_3) in 1-Q^(2j_3).

Every factor on the last line of (9) is nonzero. Indeed J=N and
2j_i<=d force j_i>=1; also j_2+j_3=N-j_1 lies strictly between
0 and N, and j_3<N/2 excludes 1+Q^(j_3)=0. Multiplying (9) by
the nonzero prefactor in (2) proves A!=0 on the ENTIRE delta=1
layer, at both level parities. Empty small-N layers are simply
absent. These are genuine all-triple source nonvanishing statements,
not deductions from a presumed positive formula.

## 5. The subsequent exact transformation

The complete positive formula from this independent route equates
the finite coefficient in (2) or (7), including its
displayed phase, to

    (-1)^(N+J)q^[2j_1^2-j_1j_2-j_1j_3+j_2j_3-J-3]
       *[prod_i s_(j_i)/(N s_delta)] R_N(j).

Equation (3) already proves its saturation-zero branch. The
[one-central-channel result](actual_trivalent_one_channel_source_packet.md)
supplies a proved nonzero boundary line. The finite coefficient-to-
short-series and Sears bridge is now proved in the linked finite
Euler-to-Racah transform, with an independent square-linearization
derivation. Finite experiments alone do not prove it. No sewn-graph
energy, magnetic norm or hyperbolic-volume claim is made from this
coefficient formula.

Audit: [literal source, Fourier selection and coefficient theorem](../experiments/audit_actual_trivalent_root_fourier_source_certificate.py).
