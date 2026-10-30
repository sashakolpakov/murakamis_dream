# The actual face factor on a fixed real fold interval

30 October 2026. Independently reviewed. An analytic first
continuant correction improves the folded relative estimate to O(N^-1)
on a FIXED real interval. The action and displayed amplitude extend
holomorphically across the fold. This does not by itself continue the
actual finite-degree source, or control its Fourier transform with an
exponentially accurate error. An exact reflected finite sequence is
proved separately below using the original large q-Hahn numerator.

## 1. Actual finite factors and analytic functions

Use the original D_a, beta_a, P_s and

    B_(N,a)=beta_a^2 D_a(x,b,y)D_a(x,c,y)P_(d-2a)(x,y)

of the [signed source theorem](general_signed_augmented_source_volume.md).
The radii are in one of its fixed actual nonnegative patterns, with
positive entries in a compact set. In particular A=x+y>0 and
T_b+T_c>0, where T_b^2=bA+xy and T_c^2=cA+xy. Put
d=N-1, M=floor(d/2), s0=d-2M and h=1/N.

On a fixed sufficiently small complex z disk choose the square roots
at their positive value at zero and define

    D(z)=A^2-4xy sin^2(pi z),
    E_b(z)=A+2b sin^2(pi z)
                   +2sin(pi z)sqrt[T_b^2+b^2 sin^2(pi z)],
    J_b(z)=cos(pi z)sqrt[T_b^2+b^2 sin^2(pi z)]/T_b,
    a_b(z)=(1/2) partial_z log J_b(z).                  (1)

If T_b=0, define instead E_b=A, J_b=1 and a_b=0; this is the
exact single-summand case. Define the c functions in the same way.
All these are holomorphic on a disk uniform over the radius compact.
The E functions and J functions are nonzero there. Direct algebra gives

    E_b(z)E_b(-z)=D(z),  J_b(-z)=J_b(z),
    a_b(-z)=-a_b(z).

Consequently the following action is holomorphic and even, with V(0)=0:

    V'(z)=Log[E_b(z)E_c(z)/D(z)],
    V''(0)=2pi(T_b+T_c)/A>0.                          (2)

The logarithm in (2) is zero at zero. This fixes the branch and the
additive constant from the actual source, not from an interpolated
color index.

## 2. Analytic cancellation of the first correction

For the actual scaled Schur pivot e_a=(beta_a D_a)/(beta_(a-1)D_(a-1))
write z=(N/2-a)/N. Its exact recurrence is

    e(z)=(1+tau)[A+2b sin(pi z)sin(pi(z+h))]
                       -tau D(z+h)/e(z+h),
    tau=tan(pi z)/tan(pi(z+h)).                       (3)

Equation (3) denotes the original sequence only at its specified
physical lattice. Define a holomorphic approximation on the disk by

    e_b^*(z,h)=E_b(z) exp[h a_b(z)].                   (4)

It obeys the exact reflection e_b^*(z,h)e_b^*(-z,h)=D(z).
Clear the denominator in its recurrence residual, using this reflection:

    Rcal(z,h)=tan(pi(z+h)) e_b^*(z,h)
          +tan(pi z)e_b^*(-z-h,h)
          -[tan(pi(z+h))+tan(pi z)]
                       [A+2b sin(pi z)sin(pi(z+h))].   (5)

This is holomorphic jointly in z,h near zero. Its values at z=0
and z=-h are zero, because e_b^*(0,h)=A. Therefore
Rcal=z(z+h)F(z,h) with F holomorphic. One may divide by z first;
the remaining function vanishes at z=-h for h!=0 and hence also at
h=0 by holomorphy, which proves divisibility by z+h.

The h^0 term of (5) is zero because
E_b(z)+E_b(-z)=2[A+2b sin^2(pi z)]. The h^1 term is zero as well.
To verify its normalization explicitly, let gap=E_b(z)-E_b(-z).
The coefficient needed in log e is

    (gap'-[partial_z Log tan(pi z)] gap)/(2 gap)
       =(1/2)partial_z Log[gap/tan(pi z)]
       =(1/2)partial_z Log J_b(z)=a_b(z).             (6)

Here gap/tan(pi z)=4cos(pi z)sqrt[T_b^2+b^2sin^2(pi z)]
is a nonzero even function. Thus (6) has no fold pole. The constant
case is exact. Since F(z,0)=partial_h F(z,0)=0, division gives

    Rcal(z,h)=h^2 z(z+h) F_2(z,h),
    |e_b^*(z,h)-(the RHS of (3) applied to e_b^*)|
                                      <=C h^2 |z|.   (7)

The latter quotient at z=-h is understood by its removable limit;
(7) is a uniform analytic residual bound on a smaller fixed disk.

This analytic residual controls the ACTUAL physical real sequence.
The original positive pivot bound e_a>=A is already proved. On a
small positive real interval e_b^*(z,h)/A>=exp(c z) for small h,
unless T_b=0, which is exact. Subtract (3) for the two sequences
and use the same positive Gaussian propagation kernel as in the
signed theorem. Start at 2delta0 and estimate only z<=delta0.
Its initial error is exponentially suppressed. With z=k/N the
residual (7) is O(k/N^3), so

    sum_(j>=k) C(k/j)e^[-c(j^2-k^2)/N] j/N^3
                                                   <=C/N^2.

For k<=sqrt(N) use a Gaussian integral; for k>=sqrt(N) use tail
length O(N/k). Therefore, uniformly at all physical real pivots
with 0<z<=delta0, including k=1/2 or1,

    e_a/e_b^*(z,1/N)=1+O(N^-2).                      (8)

No actual meromorphic index continuation or generic-q normal has
been asserted in this passage.

## 3. The fixed real folded packet

Let delta=(d-2a)/(2N), delta_min=s0/(2N), so successive channel
steps have size h and the removed pivot is at their MIDPOINT.
The forced-factor ratio is exactly D at the same midpoint.
Taking the logarithm of these step ratios and using (8), then the
midpoint quadrature formula, proves uniformly for
delta_min<=delta<=delta0 on the original integer-channel grid

    B_(N,a)/B_(N,M)
      =exp[-N(V(delta)-V(delta_min))]
        *sqrt[ J_b(delta_min)J_c(delta_min)
                        /(J_b(delta)J_c(delta)) ]
        *[1+O(N^-1)].                                (9)

Indeed each step has log ratio
-V'(z)-h(a_b(z)+a_c(z))+O(h^2). There are O(N) steps.
The midpoint sum for V' has total error O(h), and that for h a
has error O(h^2). Its integral is one half of the logarithm of the
J product. Formula (9) retains the actual even-level delta_min,
the scalar beta and the forced product. It gives the earlier
Gaussian packet by expanding V(delta)=C delta^2+O(delta^4), with
C=pi(T_b+T_c)/A. In particular the limiting rate is even analytic;
there is no cubic term in this centered variable.

The RIGHT HAND SIDE of (9) is a specified holomorphic model on a
fixed complex disk. The comparison in (9) is proved on the physical
REAL grid. An O(N^-1) error there cannot be treated as an exponentially
small Fourier error when the frequency is of order N. Uniform
complex continuation of the exact finite source, or an exponentially
accurate physical-grid replacement with controlled analytic remainder,
is a further requirement.

## 4. An exact source-native reflected sequence

There is nevertheless an exact full finite sequence across the fold.
Let H_a^1 be the actual root q-Hahn Newton numerator, for every integer
0<=a<=d. Define its homogeneous polynomial

    Z_a(x,b,y)=(-q)^a q^(-a^2)y^a
                         H_a^1(-x/(qb),-b/(qy)).       (10)

The finite Newton sum makes this a polynomial: each denominator b
or y cancels in its own summand. Thus zero faces are assigned by
polynomial evaluation. Below the fold, the original determinant
identity gives Z_a=beta_a D_a, with its exact phase.

For m=d-a>=a and s=m-a, the actual root numerator collision is

    H_m^1(U,V)=product_(r=a)^(m-1)(UV-Q^r) H_a^1(U,V).

It follows either from the original Newton coefficient identity or
the already proved large-partner relation in
[the source gauge theorem](actual_generic_boundary_gauge_and_source.md).
Here UV=Q^-1 x/y. Its product is
Q^-s y^-s P_s(x,y), while the ratio of monomials in (10) is
(-1)^s q^[s-(m^2-a^2)] y^s. Since m+a=d and q^N=-1,
the remaining scalar is (-1)^s q^(-sN)=1. Hence EXACTLY

    Z_(d-a)(x,b,y)=P_s(x,y) Z_a(x,b,y).               (11)

This uses the actual large numerator; beta_m D_m is not evaluated
at a singular virtual matrix. Define the virtual forced factor in
the partner range to be P_s^-1. Its product with the two Z_m
factors has a polynomial cancellation, giving

    B_ext,(d-a)=Z_(d-a)^b Z_(d-a)^c/P_s
                         =Z_a^b Z_a^c P_s=B_(N,a).   (12)

At the even bridge (11) is Z_(M+1)=(x+y)Z_M. At the first odd
bridge it is Z_(M+1)=P_2 Z_(M-1). Thus all endpoints remain
specified even where a naively divided recurrence would be singular.
The canceled rational presentation in (12) does not introduce a pole
on its polynomial value.

Finally omega_(d-a)=omega_a exactly, because its ratio is
(-1)^s q^(Ns)=1. Pairing the two original integer indices therefore
gives the exact Fourier identity

    sum_(a=0)^M k_a omega_a^epsilon B_(N,a)
                              cos[pi(d-2a)chi]
       =sum_(a=0)^d omega_a^epsilon B_ext,a
                              exp[pi i(d-2a)chi].     (13)

It holds for every complex chi. The same equality holds after the
unchanged shared-face coefficient extraction and tensoring the
circle color registers. It is exactly the complete-image core of
[the entire color packet](actual_augmented_plat_entire_core_color_packet.md),
not the full mixed source: its explicit nonempty ordinary-color
alias subsets remain present. The finite support and both parities
are retained; there is no cyclic replacement of the physical head
interval and no choice of a new Fourier interpolation.

## 5. A finite q-difference system with its endpoints retained

The reflected sequence also has an exact quantum difference system.
Use the polynomial Z_j of (10) for 0<=j<=d. Clearing the denominators
in the original second-order recurrence gives

    u_j Z_j^b=v_j^b Z_(j-1)^b-w_j Z_(j-2)^b,
    u_j=cos((j-1)theta)sin(j theta),
    v_j^b=sin((2j-1)theta)
                         [A+2b cos(j theta)cos((j-1)theta)],
    w_j=sin((j-1)theta)cos(j theta)
                         [A^2-4xy cos^2((j-1)theta)].   (14)

Set Z_-1=0. Below the fold (14) is the original continuant, including
j=1. Above it (11) proves (14) without dividing by a vanishing u_j.
Explicitly set l=d-j and D_r=(x-Q^r y)(x-Q^(-r)y). The reflected
coefficients satisfy

    u_j=-w_(l+2)/D_(l+1), v_j^b=-v_(l+2)^b,
    w_j=-u_(l+2)D_(l+2).

After inserting Z_j=P_(d-2l)Z_l, equation (14) becomes the
negative of the lower recurrence at l+2 times its common factor.
The first fold bridges are checked directly: at odd N the middle
coefficient at j=M+1 is zero and (11) is precisely the resulting
equation; at even N the equation at j=M+1 gives Z_(M+1)=A Z_M,
and the equation at j=M+2 is its retained zero-leading-coefficient
consequence. Thus it does not choose a second solution there.

At the last index j=N, u_N=0 and the recurrence is still exact:
Z_d=P_d and Z_(d-1)=P_(d-2)Z_1, with
P_d=D_1 P_(d-2), give v_N^b Z_d=w_N Z_(d-1).
This is the actual terminal relation, not a periodic closing arrow.

Let Pcal_j denote P_(d-2j) below the fold and its canceled reciprocal
presentation above it. Uniformly,

    Pcal_j=P_d/product_(r=1)^j D_r,
    Pcal_j/Pcal_(j-1)=D_j^(-1), 0<=j<=d.

Work over the face coefficient ring localized at product_(r=1)^d D_r.
These factors do not vanish on the stated positive radius compacts.
The auxiliary components below may be RATIONAL face functions; only
their first component has already been proved to be the original
homogeneous face polynomial after cancellation. Put

    Y_j=(Z_j^b Z_j^c, Z_j^b Z_(j-1)^c,
                         Z_(j-1)^b Z_j^c, Z_(j-1)^b Z_(j-1)^c)^T,
    V_j=omega_j^epsilon Pcal_j Y_j.

The tensor product of (14), with all factors still ordered, is

    u_j^2 D_j V_j=(-Q^j)^epsilon M_j V_(j-1),
    M_j=
      [ v_j^b v_j^c, -v_j^b w_j, -w_j v_j^c, w_j^2 ]
      [ u_j v_j^b,    0,          -u_j w_j,   0     ]
      [ u_j v_j^c,   -u_j w_j,     0,         0     ]
      [ u_j^2,        0,           0,         0     ]. (15)

Here the exact twist ratio is omega_j/omega_(j-1)=-Q^j.
Extend V_j by ZERO outside 0,...,d. Equation (15) holds at j=0
because u_0=0, and at j=N because its first row is the product
of the two terminal scalar relations while its other rows contain
u_N. Thus (15) is exact on the entire integer line with that finite
support. No endpoint term has been discarded.

All coefficients in (15) are Laurent polynomials in w=Q^j.
For explicit substitution, put

    S(w)=(q^(-1)w-q w^(-1))/(2i),
    C(w)=(q^(-1)w+q w^(-1))/2,
    u(w)=[S(w)+sin(theta)]/2,
    v_b(w)=S(w)[A+b(C(w)+cos(theta))],
    wcoef(w)=[S(w)-sin(theta)]/2
                   *[x^2+y^2-xy(Q^(-1)w+Q w^(-1))],
    D(w)=x^2+y^2-xy(w+w^(-1)), L(w)=u(w)^2 D(w).

Form M(w) from the displayed matrix using these Laurent functions.
For the ACTUAL finite polynomial vector and shift

    mathcal V(z)=sum_(j=0)^d V_j z^j,
    Theta f(z)=f(Qz),

coefficientwise summation of (15) gives exactly

    [L(Theta)-z(-Q Theta)^epsilon M(Q Theta)]
                                      mathcal V(z)=0. (16)

The system has four components, z degree at most one, and Theta
powers only in [-5,5] for epsilon in {0,1,-1}, independently of N:
L has powers in [-3,3], M in [-4,4], and the twist shifts these by
at most one. This is not merely the root identity Theta^N-1.
It is a root-level external-color system, not a generic-q,
varying-N colored-Jones AJ operator.

The first component, multiplied by exp(pi i d chi) at
z=exp(-2pi i chi), is the literal single-circle Fourier core in
(13). Keep this Fourier gauge when naming the external shift. If
mathcal S(chi)=exp(pi i d chi) mathcal V(exp(-2pi i chi)), then

    exp(pi i d chi) Theta mathcal V
                         =q^d mathcal S(chi-1/N).

Thus on the full source vector Theta is q^d times the unit deficit
shift chi -> chi-1/N, not the bare shift. Equation (16) uses its
specified finite period, not a solution
chosen by a formal asymptotic expansion. After the full source's face
coefficient extraction, face multiplications in (16) couple nearby
coefficient indices; no closed scalar equation for an arbitrary
whole network is asserted without retaining that coupled family.

## 6. Its local principal characteristic and remaining analytic issue

For a/N->mu write r=cos^2(pi mu), A=x+y,

    D=A^2-4xy r, B_b=A+2br, B_c=A+2cr.

The original single scaled-continuant characteristic is
e_b^2-2B_b e_b+D=0. Tensoring the two roots and dividing by the
forced-factor ratio gives the four eigenvalues lambda=e_b e_c/D.
Their characteristic is the explicit palindromic quartic

    D(lambda^4+1)-4B_b B_c(lambda^3+lambda)
                   +(4B_b^2+4B_c^2-2D)lambda^2=0.     (17)

Indeed each root pair multiplies to D; their pairwise products give
the displayed elementary symmetric functions. The original twist
multiplies lambda by (-J)^epsilon, J=exp(2pi i mu).
The Fourier stationary characteristic of (16) is therefore

    z (-J)^epsilon lambda=1.                         (18)

The reduced quartic must not erase the factors of the FULL finite
system. In the classical limit u=(1/2)sin(2pi mu) and
M_cl=u^2 times the tensor transfer matrix. If P(w) denotes the
left side of (17), the full principal determinant is

    det[L_cl I-z(-J)^epsilon M_cl]
                    =u^8 D^3 P(z(-J)^epsilon).        (19)

Thus (17) is the reduced characteristic where uD!=0. At the complete
fold u=0 the full symbol degenerates; these factors have not been
declared globally harmless peripheral factors or canceled from the
actual operator. It is the specified finite source and its endpoint
relations, together with the selected analytic branch, that provide
the extension discussed here.

For real mu just below1/2, the positive original pivots select
e_b=E_b(1/2-mu), e_c=E_c(1/2-mu), with the single-variable cases
interpreted as above. Their continued local logarithmic branch is
fixed by (1), not by an arbitrary root of (17). This identifies the
principal characteristic of the actual finite source system.

Equations (16)--(18) do not yet prove a uniform complex-color packet,
the nonzero coefficient of a deformed period, an actual global
A-polynomial identification, or a gap for the ordinary-color alias
subsets. The real-grid error in (9) remains insufficient for those
Fourier conclusions. These are the precise remaining tasks.

Focused audit: [literal Newton sequence and fixed-fold factors](../experiments/audit_actual_positive_face_fixed_fold_packet.py),
with [saved results](../experiments/actual_positive_face_fixed_fold_packet_results.json).
It checks 1020 original homogeneous Newton values, including all large
channels and zero-face evaluations; 306 direct nonzero-chart H values;
540 original lower determinants and 540 large-partner reflections;
1020 endpoint-safe recurrences, including 60 zero-leading fold equations
and 120 terminal equations; 6840 tensor-system rows, 360 full finite
Fourier equations, and 180 reflected cosine identities. Five exact
symbolic identities retain the first correction and FULL characteristic
determinant. The maximum original-source relative error is below
1.7e-81 at 90 digits. The 72 fixed-real packet profiles are diagnostics,
with maximum N times relative error below .055; they do not prove an
actual complex degree continuation.

Two independent full analytical reviews: PASS. The readers checked
the analytic residual divisibility, original real contraction,
midpoint action and amplitude, literal large-source reflection,
localized tensor system, both fold bridges and finite endpoints,
Fourier ordering and retained gauge, and the full characteristic
factor u^8D^3. Independent full code read and fresh redirected
90-digit replay: PASS, reproducing every recorded count and exact
maximum error. The bounded shift order and the distinction from a
generic-q AJ operator are explicit. No actual complex-color packet
or ordinary-color alias gap is inferred.
