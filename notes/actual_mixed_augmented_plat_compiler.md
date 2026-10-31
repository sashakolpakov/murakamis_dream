# Every actual auxiliary color in the arbitrary-plat source compiler

30 October 2026. The original augmented-plat compiler extends to ALL
ordinary auxiliary colors 1<=n<=N and signed local coupons
R^epsilon L_n, epsilon in {0,+1,-1}. Its value and first-normal
columns, inverse measures, color phases and source are explicit.
No unknown recoupling inverse remains. The additional normal and
color factors have uniform polynomial bounds; all exponential
factorial profiles are displayed rather than absorbed in that claim.

This is a finite ROOT-LEVEL source theorem at arbitrary fixed bridge
width. It does not assert a coherent global gap or a uniform complex
color interpolation, and is not yet an arbitrary-plat filling theorem.
In particular the exact root normal below must not be confused with
the generic-q normal of the whole original pointed invariant.

## 1. The circle polynomial is fixed by the original typed source

Use d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, kappa=q^(d^2/2).
The ordinary n-dimensional auxiliary module has its ACTUAL pivot
K_n^(1-N), with no new factor 1/n. The typed threading [2,1,1,2]
followed by that pivot trace gives, as a full physical matrix,

    L_n=l_n(Omega),
    l_n(z)=(-1)^(n-1) P_(n-1)(z), P_r(z)=U_r(z/2),
    P_0=1, P_1=z, P_(r+1)=z P_r-P_(r-1).                 (1)

Thus L_1=I and L_2=-Omega. This normalization, including the sign,
is the proved [original mixed-circle identity](actual_crossing_circle_source_and_filling.md).
It is not a replacement of an ordinary module by an N-dimensional
ADO component at a putative meridian value.

For an actual physical pair degree S set t=min(S,2d-S) and translate
the first index by max(0,S-d), exactly as in the complete compiler.
Use the canonical physical columns

    v_j=f(c_j), w_j=f'(c_j),
    c_j=q^(2j+1)+q^(-2j-1), nu_j=(-1)^j q^[j(j+1)].

All j=0,...,t are retained, grouped by equal nodes. The only double
pair is j,l=d-j. The self-paired odd-level node is SIMPLE. Ordinary
colors also retain the unpaired simple nodes killed by L_N.

## 2. An exact generic finite formula for the normal column

The root formula for v_j is the q-Hahn sum in the
[complete phase compiler](actual_augmented_plat_phase_compiler.md).
To compute its first NORMAL, one must first use the actual generic
highest-weight-d family, not differentiate a root-only simplification.

Let zeta vary near q, Q=zeta^2, x=zeta^d and F_b=(Q;Q)_b. Define

    R_(j,a)=F_(N-j+a-1) F_(N-a-1) /
                              [F_(N-j-1) F_(N-1)],

    C_(j,u,a)(zeta)=(-1)^a x^(u-2a)
       Q^[a(t-u)+a(a-1)/2] R_(j,a)
       [u choose a]_Q [t-u choose j-a]_Q/[t choose j]_Q,

    C_(j,u)(zeta)=sum_(max(0,u-t+j)<=a<=min(j,u)) C_(j,u,a).
                                                               (2)

Every factorial index lies in 0,...,d, so these are regular finite
functions at the actual root. They are the normalized actual
generic Clebsch columns. One direct derivation starts with the
highest vector of degree j, whose a-th coefficient is

    (-1)^a x^-a Q^[a(j-1)-a(a-1)/2] R_(j,a).

Apply F_tot^(t-j)/F_(t-j), with F_tot=F tensor I+K^-1 tensor F.
The q-binomial expansion contributes
x^[-(t-j-u+a)]Q^[a(t-j-u+a)] [u choose a][t-u choose j-a].
Its first component is x^[-(t-j)] [t choose j], which is a unit.
Dividing by it gives precisely (2). Thus its eigenvalue is

    lambda_j(zeta)=zeta^(2N-1-2j)+zeta^(-2N+1+2j).          (3)

At the root, R_(j,a)=Q^[a(a-j)] [j choose a]_Q, recovering the
previous physical column and its exact Fourier phase. This equality
is used for the VALUES, not for their zeta derivatives.

For a double pair j<l=d-j, put D=zeta d/dzeta. Then exactly

    w_(j,u)=[D C_(j,u)(q)-D C_(l,u)(q)] /
                  [-2N(q^(2j+1)-q^(-2j-1))].              (4)

Indeed C_(j,u)=f_u(zeta,lambda_j(zeta)); subtracting derivatives
cancels the common derivative of f with respect to zeta. The
remaining eigenvalue gap derivative from (3) is the displayed
denominator. This retains the actual generic confluence.

The differentiated sum in (4) is fully explicit. Write

    H_b=D log F_b=-2 sum_(r=1)^b r Q^r/(1-Q^r), H_0=0,
    Hbin(v,w)=H_v-H_w-H_(v-w).

At the root each summand derivative is its original root value
times

    Gamma_(j,u,a)=d(u-2a)+2a(t-u)+a(a-1)
       +H_(N-j+a-1)-H_(N-j-1)+H_(N-a-1)-H_(N-1)
       +Hbin(u,a)+Hbin(t-u,j-a)-Hbin(t,j).                 (5)

Thus (4) is a difference of two finite factorial/Fourier sums with
known q-harmonic coefficients. No chosen solution of a homogeneous
recurrence or unidentified normal amplitude has been inserted.

## 3. Explicit bilinear measures and every signed mixed kernel

Put CalP_t(z)=product_(r=0)^t(z-c_r) and B_t=(-1)^t s_t^2.
At a simple node define

    sigma_j=x^t nu_j CalP_t'(c_j)/B_t.

At a double node c=c_j=c_l put Q_j=CalP_t/(z-c)^2 and

    sigma_j=x^t nu_j Q_j(c)/B_t,
    rho_j=-(d-2j)/[2(q^(2j+1)-q^(-2j-1))],
    eta_j=rho_j+Q_j'(c)/Q_j(c).                           (6)

These are the actual Christoffel--Darboux measures. In particular
sigma_j never vanishes. The bilinear Gram block of (v_j,w_j) is
sigma_j [[0,1],[1,eta_j]], with inverse
sigma_j^-1 [[-eta_j,1],[1,0]]. The value rho_j is the spectral
logarithmic derivative of the original normalized crossing R/kappa.

For EVERY auxiliary color n and either sign, the entire contribution
of a double node to R^epsilon L_n is therefore

    kappa^epsilon nu_j^epsilon /sigma_j *
      { [l_n'(c)+(epsilon rho_j-eta_j)l_n(c)] v_j v_j^T
                    +l_n(c)(v_j w_j^T+w_j v_j^T) }.       (7)

A simple node contributes

    kappa^epsilon nu_j^epsilon l_n(c_j)
                                      v_j v_j^T/sigma_j. (8)

Proof: in the actual Jordan chain, a function A(Omega) has matrix
[[A(c),A'(c)],[0,A(c)]]. Multiplying by the displayed bilinear
inverse gives
sigma^-1[(A'-eta A)vv^T+A(vw^T+wv^T)]. Here
A(c)=kappa^epsilon nu_j^epsilon l_n(c) and
A'(c)=kappa^epsilon nu_j^epsilon[l_n'(c)+epsilon rho_j l_n(c)].
This proves (7), including epsilon=-1. It is a bilinear physical
identity; conjugating a column would give the wrong coupon.

Summing (7),(8) over ALL distinct nodes gives the original full
matrix. In particular n=N collapses to the complete-circle formula:
at a double node l_N(c)=0, leaving its specified first normal, and
at an unpaired simple node l_N(c)=0. The self-paired simple value
is treated separately. This reduction checks, rather than assumes,
the complete-image formula.

## 4. Color dependence and uniform polynomial factors

The color dependence is explicit and coherent. With theta_j=(2j+1)pi/N,

    l_n(c_j)=(-1)^(n-1) sum_(b=0)^(n-1)
                               q^[(2j+1)(n-1-2b)].        (9)

All its n-dependent phases remain. The derivative is the derivative
of the SAME polynomial in z; it is not a derivative of a chosen
eigenvalue lift. Away from sin theta=0 it can also be written

    l_n'(2cos theta)=(-1)^(n-1)
      [sin(n theta)cos theta-n cos(n theta)sin theta] /
                                             [2sin(theta)^3]. (10)

At the odd self-node c=-2 use its polynomial limit, with l_n(-2)=n.
There is no 0/0 cancellation left to a numerical prescription.

Uniformly for every 1<=n<=N and every real node in [-2,2],

    |l_n(c)|<=n,   |l_n'(c)|<=n(n^2-1)/6.                  (11)

For the second bound group the finite Laurent expression for U into
pairs 2cos(m theta). Its z derivative is m sin(m theta)/sin theta,
whose absolute value is at most m^2 by the finite geometric sum.
The sum of these positive-frequency squares is n(n^2-1)/6. This
also proves the endpoint bound by continuity, without dividing by
an endpoint sine.

Every H_b in (5) has magnitude O(N^2(1+log N)), since
sin(pi r/N)>=2min(r,N-r)/N. The remaining exponents in (5) are
O(N^2). The denominator of (4) has modulus at least eight.
Consequently, with Ebar_(t,j,u) the sum of the two positive
q-Hahn envelopes at j,l,

    |v_(j,u)|<=E_(t,j,u),
    |w_(j,u)|<=C N^2(1+log N) Ebar_(t,j,u).               (12)

The known node gap bound also gives |rho_j|<=N^2/8 and
|eta_j|<=C N^3. Thus every color and every extra normal factor in
(7) is polynomially controlled, uniformly over the ENTIRE physical
color interval, with normal order at most one on each local column.

The inverse measure is NOT hidden in this statement. If
a_j=|1-Q^(2j+1)|, its exact magnitudes are

    unpaired simple: |sigma_j|=s_(t-j)s_(t+j+1)/(s_t^2 a_j),
    double: |sigma_j|=N s_(t-j)s_(t+j-d)/(s_t^2 a_j^2),
    odd self-paired: |sigma_j|=N s_(t-j)^2/s_t^2.          (13)

Its phase is explicitly fixed by (6) or the simple product. All
factorial indices are below N. Therefore an all-input bound for
(7),(8) is a fixed polynomial times the sum of the products of the
stated column envelopes divided by |sigma_j|. The exponential
growth of those factorial profiles has not been proved to disappear.

## 5. Arbitrary fixed plats and the remaining filling problem

Insert (7),(8) at every original augmented region of any fixed
2k-head plat and perform the literal wire contractions. Retain the
original cup, ordinary caps, unrestricted marked cap, pivots and
external line. The whole-source integer-degree argument permitting
the final marked-pair restriction is the same as in the complete
compiler. This yields an exact finite formula for EVERY physical
auxiliary-color tuple (n_1,...,n_b), not merely a coefficientwise
upper envelope or a complete-color value.

Expanding (4),(5),(9) makes all color/normal couplings explicit:
they are the original finite Fourier factors, factorial weights
and bounded-order q-harmonic prefactors. For a fixed diagram the
number of discrete variables and the total number of normal factors
are fixed. Contracting does not increase that normal order with N.
One may also use the finite polynomial values (1) directly; the two
expressions are identities of the original matrices.

This supplies a concrete all-color input to the existing exact
full-twist resolution for any fixed signed slopes p_i. A prospective
geometric threshold T(D) concerns the fixed skeleton and the sizes
of those integer twists, not the quantum level N. The compiler
alone gives no such threshold or nonzero geometric period.

In particular an explicit finite formula is NOT automatically the
uniform holomorphic packet required by analytic filling transfer.
The naive expression sin(n theta)/sin theta is singular at the odd
self-node theta=pi for nonintegral n; its cancellation at integer
n does not authorize that continuation. A valid complex-color packet
must specify its whole finite continuation and prove its uniform
estimates, preserving all these endpoint and normal contributions.

Likewise the polynomial bounds in (11),(12) leave the column and
inverse-measure factorial rates present. A geometric global gap,
source-preserving complex deformation, selected nonzero amplitude
germ and actual marked regulator identification are separate tasks.
The new result removes the UNKNOWN mixed local kernel and normal
formula; it does not replace those analytic and geometric proofs.

Audit: [generic normals and all original mixed signed operators](../experiments/audit_actual_mixed_augmented_plat_compiler.py).
Fresh exact finite-field checks pass N=2,...,12: 143 physical blocks,
2,904 canonical value entries, 1,177 generic-confluence normal entries,
and 231 full signed mixed-color operator identities. The normal
columns from (2)--(5) are compared with independent continuant
derivatives. Every compiled matrix is compared with the original
coproduct Casimir polynomial and original signed crossing matrices.

The generic matrix identities do not supply a uniform complex-color estimate or coherent gap.