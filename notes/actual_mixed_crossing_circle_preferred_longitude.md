# The actual mixed crossing-circle longitude, flag and central sign

29 October 2026. The literal auxiliary loop [2,1,1,2] has the
crossing-disk preferred longitude, with no hidden meridian power.
For the actual auxiliary meridian M_aux=-q^j and H=Q^(N-j), the
source coordinate L_H=(H-X)/(1-HX) gives

    preferred SL2 longitude lambda=-L_H^(-1),
    centered longitude ell=-lambda=L_H^(-1).              (0)

The minus is forced by the original ordinary auxiliary pivot. It
is not a choice of a different geometric component. This note proves
the mixed local transport/framing certificate and records the exact
central character. A geometric representation lift and regulator
calibration must still use that character explicitly.

## 1. The literal mixed universal crossing and its color contiguity

Use q=exp(pi i/N), Q=q^2, eta=q^(1/2), and colors
x_1=q^alpha, x_2=q^beta. In the factorial basis, a positive checked
mixed crossing sends input (a,b) to (b+k,a-k). Its coefficient is
EXACTLY

\[
 r^+_{\alpha,\beta}(a,b,k)
 =q^{\alpha\beta/2}(-1)^k q^{k^2-k}
 x_1^{-b-2k}x_2^{-a+k}Q^{(a-k)(b+k)}
 \frac{F_{b+k}}{F_bF_k}(Qx_1^2/A;Q)_k,
 \quad A=Q^a,\ B=Q^b,\ C=Q^k.                         \tag{1}
\]

All indices have their actual physical support and F_a=(Q;Q)_a.
The half-Cartan is the unwrapped q^(alpha beta/2), not an inferred
square root after reducing indices. Derive (1) directly by expanding
the finite universal nilpotent factor followed by its full Cartan:

    Ecal_(a-1,a)=q^(-1)(x_1^(-1)-x_1 Q^(-a+1)),
    F_(b+1,b)=1-Q^(b+1),
    q^(k(k-1)/2)rho^k/[k]!
                         =(-1)^k q^(k^2)rho^(2k)/F_k.

The two independent positive color shifts therefore obey

\[
 \frac{r^+_{\alpha+1,\beta}}{r^+_{\alpha,\beta}}
    =K_{2,\mathrm{in}}^{-1/2}\tau_q^{-1},\qquad
 \frac{r^+_{\alpha,\beta+1}}{r^+_{\alpha,\beta}}
    =K_{1,\mathrm{out}}^{1/2},
 \quad
 \tau_q=\frac{BC}{x_2}
                 \frac{1-Qx_1^2/A}{1-Qx_1^2C/A}.       \tag{2}
\]

These are common-index identities: changing the ordinary dimension
does not authorize dropping its new boundary states. At zeros the
first relation means the CLEARED finite-product identity

    (1-Qx_1^2/A)r_shift
      =K_2^(-1/2) x_2/(BC)(1-Qx_1^2 C/A)r.

It remains valid when a displayed ratio is 0/0. Every square root in
(2) is its literal q^(H/2) from (1).

## 2. Four mixed crossings cancel the full Cartan color density

Start with ordered strand labels (A,B,C), where C is the auxiliary
color j. Chronological positive crossings [2,1,1,2] give

    (A,B,C) -> (A,C,B) -> (C,A,B) -> (A,C,B) -> (A,B,C).

The auxiliary is UNDER first B then A, and OVER first A then B.
Each main head's K after its first crossing is exactly its K before
its second crossing. Hence the two K^(1/2) factors in (2) cancel
the two inverse factors EXACTLY, even before taking q to one.
No square-root sign is chosen from a cyclic exponent.

The original auxiliary closing pivot is g_j=K_j^(1-N), with NO
1/j. On its physical weights g_j=(-1)^(j-1)K_j at the root.
The shift j->j+1 changes a common closing weight by q^(1-N).
Consequently its common-state source multiplier is

    q^(1-N) (tau_(3,q)tau_(4,q))^(-1).                 (3)

The classical central factor is -1, since q^(1-N)=-q. This factor
must be kept when interpreting a color derivative. Taking only the
Cartan monodromy and silently replacing the pivot by K would miss it.

There is also a FULL all-input identity retaining every dimension
endpoint and every root normal jet:

    L_j=(-1)^(j-1)U_(j-1)(Omega/2),
    L_(j+1)+Omega L_j+L_(j-1)=0.                        (4)

It is the proved literal mixed-loop theorem, not an N-dimensional
ADO replacement for a separate ordinary component. Thus the
characteristic positive color-shift roots Lambda satisfy
Lambda+Lambda^(-1)=-Tr(P), consistently with (3). Formula (3) fixes
their flag and orientation on a regular chart; (4) retains the
states that are not common under a dimension change.

## 3. Mixed-color eigenvector transport fixes the actual flag

Use the original classical triangular matrices

    b_+(K,e)=[[K,e],[0,1]], b_-(K,f)=[[1,0],[-Kf,K]],
    G=b_-^(-1)b_+,
    K_i=x_i/A_i,
    e_i=(x_i^(-1)-K_i)p_i, f_i=(1-A_i)/p_i.

Their Casimir is x_i+x_i^(-1), without assuming equal colors.
The actual universal crossing has the Gauss/Hurwitz map

    d=1-e_1 f_2,
    K'_1=K_2 d, K'_2=K_1/d,
    f'_1=K_1f_2/d, e'_2=e_1/(K_2d),
    e'_1=[d e_2+e_1(dK_2-K_2^(-1))]/K_1,
    f'_2=K_2[d f_1+f_2(d/K_1-K_1)].

This map and its three triangular factorizations are independent of
the individual Casimir values; it swaps x_1 and x_2. Let
H_i be its prefix-transported raw meridians and mu_i=-H_i the
actual meridians. The global flag vector v_i is the lower-prefix
transport of (p_i,1)^t. It has mu_i eigenvalue -x_i^(-1), the
M_i^(-1) flag for M_i=-x_i classically. Direct matrix multiplication,
with different x_1 and x_2 retained, gives

    v'_under=-mu_over^(-1)v_under,
    v'_over=tau_+ v_over,
    tau_+=BC/x_2 * (1-x_1^2/A)/(1-x_1^2C/A).           (5)

For example p'_under=(p_2-e_1)/K_1, while
tau_+=1/[K_2(1-x_1^(-1)p_1 f_2)]. These prove (5) directly.
They agree with the q->1 limit of (2), including its orientation.

## 4. The disk word is preferred, not a meridional shear

In global ACTUAL meridians the positive Hurwitz rule is
(A,B)->(A^(-1)BA,A). Multiplying the four specified moves gives

    C_out=P^(-1)CP, P=BA;
    A_out=C^(-1)AC, B_out=C^(-1)BC when [C,P]=1.         (6)

Closing the auxiliary therefore imposes [C,P]=1. Its underpass
vector transport is W=A^(-1)B^(-1)=P^(-1): B is encountered
first and A second, in the literal operator order. Including its
two overpasses, flag closure reads

    v_C=(tau_3 tau_4)P^(-1)v_C.                         (7)

The positively oriented blackboard parallel of C has word W^(-1)=P.
This is checked by pushing the parallel across the two underpasses:
the inverse vector transport records their positively oriented
puncture meridians in reverse product order. It is also the boundary
of the crossing disk with its two punctures removed. The loop has
NO auxiliary self-crossing. Its self-writhe is zero, so the disk
parallel has zero self-linking; no power of C is subtracted or
inserted. Thus the preferred crossing-disk longitude is

    lambda_C=P=BA.                                     (8)

The disk may have nonzero linking with other components; that does
not change its zero SELF-linking or its preferred framing. If a
target leg is dualized, its oriented puncture meridian is inverted
by the actual duality, rather than by altering (8) with a power of C.

On the M_C^(-1) flag, (7) gives eigen(lambda_C)=tau_3 tau_4.
On the positive M_C flag the eigenvalue is the inverse:

    lambda=(tau_3 tau_4)^(-1).                          (9)

Equations (3),(9) prove that the actual positive j shift has symbol
Lambda=-lambda. Its complete central sign is therefore fixed, not
selected from a metric cusp shape.

## 5. The main half twist and actual quarter-turn retain this framing

The original base box is R^(-1)L_j. The retained R^(-1) crosses
only the two MAIN strands. Its Hurwitz action preserves their
product P, and algebraically it commutes with the Casimir loop L_j.
It creates no auxiliary self-crossing and does not change (8) by a
meridional power. Its full original Cartan phase remains in the
box; it is not removed from the scalar source.

There is an elementary surgery-coordinate check of the slope sign.
Let theta run along the positively oriented auxiliary meridian and
phi along the oriented boundary of its crossing disk. Straightening
a filling meridian (theta,phi)=(t,pt) uses phi'=phi-p theta. Hence
one positive normal turn rotates the two disk punctures by -p FULL
turns. In the displayed checked-braid convention its inserted tangle
is R^(-2p). The retained R^(-1) therefore gives R^(-(2p+1)), while
the primitive killed curve is mu_C+p lambda_C. This derives the
integer sign; it is not assigned by matching an asymptotic volume.

The genuine unscaled quarter-turn is formed with the original main
cup and ordinary main cap. It bends target legs by their actual
Hopf duality and is an orientation-preserving movement of this
ribbon tangle; the auxiliary circle and its crossing disk move
together. It introduces no auxiliary curl or new auxiliary pivot.
Consequently the image of the disk word (8) is still its preferred
zero-self-linking longitude. This does NOT assert that rotating a
polynomial is multiplicative. All statements concern the literal
typed turn of R^(-1)L_j with its actual cup/cap.

The metric cusp has the two possible half-twist meridians differing
by one disk longitude. Once the port representation lift is made,
(8)--(9) fix the longitude's sign/flag, so the source derivative may
calibrate which corner meridian represents the retained R^(-1).
It is not permissible to infer (8) from the cusp derivative alone.

## 6. Match the actual mixed source and retain the central character

For j=N-h, the literal auxiliary meridian is M_aux=-q^j=q^(-h),
so H=Q^h=M_aux^(-2). The source phase has

    G_(LogH)=Log L_H,
    L_H=(H-X)/(1-HX).

The positive j shift sends M_aux->qM_aux and H->Q^(-1)H.
Its symbol is therefore L_H^(-1). Combining with the ACTUAL mixed
pivot and disk certificate (3),(9) proves precisely (0), rather than
identifying a same-color cut theorem with a closed ordinary loop.
In particular

    Tr(P)=-(L_H+L_H^(-1)),
    M_aux=e^u, centered ell=e^v=L_H^(-1),
    preferred lambda=-ell, Log lambda=pi i+v.            (10)

The sign agrees with the literal circle recurrence (4); at complete
color L_H=1, the preferred SL2 disk longitude has eigenvalue -1.
The squared geometric peripheral coordinates are
M_aux^2=H^(-1), lambda^2=L_H^(-2). Their uncentered logarithmic
lift retains its 2pi i deck shift.

Centering lambda by -1 is represented on the PHYSICAL color lattice
by the explicit character (-1)^(j-1)=(-1)^(N-1)(-1)^h from g_j.
At complex color this character must be transported together with
the full filling kernel; it is not an identically one gauge. A
preferred logarithmic action may differ from the centered action by
the corresponding +/-pi i LogH term, whose two choices differ by
2pi i LogH and agree on the physical lattice. It must not be dropped
separately from its kernel or regulator trivialization.

Finally the actual filled saddle equation

    LogH+2p LogL_H=2pi i m

gives M_aux ell^p=(-1)^m, hence

    M_aux lambda^p=(-1)^(p+m).                          (11)

Thus its PSL2 relation is exactly the primitive disk-framed slope
mu_C+p lambda_C, with the retained half twist in its base meridian.
The displayed central lift is part of the marking; no replacement
of p by p+1 or hidden longitude shear was used. Geometric action
calibration must retain this lift and its explicit source character.

[Audit](../experiments/audit_actual_mixed_crossing_circle_preferred_longitude.py)
compares (1) with the original mixed universal matrices, checks both
independent color contiguities and literal four-crossing path weights,
and verifies the unequal-color eigenvector and disk-word transport.
