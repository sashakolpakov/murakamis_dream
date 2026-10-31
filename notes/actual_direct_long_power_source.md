# Direct crossing powers and a limitation of phase-blind spectral bounds

, 30 October 2026. This is an exact root-source statement for the
original connected fixed flat-plat compiler. It retains every cap, mark,
level coset and crossing scalar. It gives a direct formulation for fixed
integer twist powers and rules out one particular positive spectral
upper bound as a route to a strict filled-volume rate. It does not bound
the phase-preserving source or prove a filling asymptotic.

Write N>=3, d=N-1, q=exp(pi i/N), S_j=prod_(v=1)^j 2sin(pi v/N),
and lambda0=q^(d^2/2), with the original exponential lift. All Casimir
derivatives below are taken at this fixed root, not in a generic-q germ.

## 1. Direct powers in the original coefficient source

The [homogeneous source theorem](actual_homogeneous_casimir_face_source.md)
assigns a degree-d polynomial H_F(x,b,c,y) to a polynomial F in the
actual pair Casimir Omega. For two coupons on the SAME pair,

    H_(FG)(x,b,c,y)=[z^d] H_F(x,b,z,y) H_G(x,z,c,y).       (1)

A left term has intermediate exponent d-j, while a right term has
output exponent i. Extraction imposes i=j, exactly matrix composition.
The outer x,y powers add; there is no extra N or pivot factor. The
identity is H_1=sum_(j=0)^d b^j c^(d-j).

For every nonzero integer n, therefore,

    H_(R^n)(x,b,c,y)
      =[prod_(r=1)^(|n|-1) z_r^d]
         prod_(r=1)^|n| H_(R^sign(n))(x,z_(r-1),z_r,y),
    z_0=b, z_|n|=c.                                     (2)

Each layer retains its original scalar lambda0^sign(n). Thus the
right side contains lambda0^n and the full repeated-node data. A
filled box with exponent n_e=epsilon_e-2p_e may be compiled directly
by (2), with all other physical tensors and marked face targets
unchanged. This exact identity needs no external-color or alias split.
The exponents p_e are fixed before N; no uniform asymptotic in growing
word length is asserted. Casimirs at different ports need not commute.

For reference, the normalized one-layer coefficient is

    [x^k b^i y^l c^t] H_(r_N^epsilon)
       =(-1)^(k+l+1) q^[epsilon(kl-(i+1)(t+1))]
                              N/(S_i S_k S_l S_t),
    i+k+l+t=d, epsilon=+/-1.                            (3)

The full layer is lambda0^epsilon times (3). For scaled simplex
coordinates I,K,L,T its principal phase includes

    E_simplex + I Log b+K Log x+L Log y+T Log c
        +pi i(K+L)+epsilon pi i(KL-IT)+epsilon pi i/2.    (4)

Here E_simplex=sum Lambda(pi I_j)/pi. The finite d=N-1 offsets and
order-one signs stay in (3). Each intermediate extraction subtracts
Log z_r in (4). The [crossing Casimir transport theorem](actual_crossing_casimir_torus.md)
derives the signed local characteristic, its punctured norm torus and
its distinct endpoint schemes. None of these local statements selects
the original global coefficient contour.

## 2. A general obstruction for the Hermite triangle bound

The paired nodes are c_a=q^h+q^(-h), h=2a+1<N. Let P_a,Q_a denote
the canonical confluent Hermite polynomials modulo
chi(z)=2T_N(z/2)+2: P_a has value1 at c_a and all other node data0;
Q_a has derivative1 there and all other node data0. At odd N retain
the single c_*=-2 node with its value projector P_*.

The ACTUAL normalized crossing data are

    r_N(c_a)=nu_a=(-1)^a q^[a(a+1)],
    gamma_a=r_N'(c_a)/r_N(c_a)
             =-(N-h)/[2(q^h-q^(-h))].                  (5)

Thus r_N^n has data nu_a^n and n gamma_a nu_a^n for every integer n;
negative powers are legitimate because the values are units. These
are full Hermite data, not an eigenvalue-only interpolation.

For a polynomial H let |H|_coef replace each coefficient by its
absolute value. Define the positive polynomial

    E_n=sum_a (|H_(P_a)|_coef+|n gamma_a| |H_(Q_a)|_coef)
                       +[odd N: |H_(P_*)|_coef].       (6)

For n!=0, |H_(R^n)|_coef<=E_n. The unit lambda0^n does not affect
this inequality. The complete coupon is
L_N=(-1)^(N-1)U_(N-1)(Omega/2). Its paired values vanish, while

    |L_N'(c_a)|=N/[2sin^2(pi h/N)],
    |L_N'(c_a)|/|gamma_a|
          =2N/[(N-h)sin(pi h/N)] <= N^2.              (7)

Indeed sin(pi h/N)>=2min(h,N-h)/N. If h<=N/2 the ratio is at most
N^2/[h(N-h)]<=N^2; if h>=N/2 it is at most N^2/(N-h)^2<=N^2.
At the odd simple node L_N(-2)=N. The triangle inequality, |n|>=1,
and the independently proved nonnegative coefficients of H_(L_N)
give the EXACT coefficientwise comparison

                         H_(L_N) <= N^2 E_n.            (8)

This comparison is local, but its consequence retains the full shared
source constraint. On any certified original connected fixed flat
plat with R boxes and nonzero integers n_e, multiply (8) and extract
the original marked target:

    [target] prod_e E_(n_e)
       >=N^(-2R) [target] prod_e H_(L_N).                (9)

The common original prefactor is polynomial in N and every crossing
scalar has modulus1. The right side has the augmented complete-volume
rate, by the [complete augmented-source theorem](general_signed_augmented_source_volume.md)
with zero half twists. Every positive-radius Cauchy bound for the left
side is at least that coefficient, so optimizing the radii cannot
remove this obstruction. In particular this specific phase-blind
Hermite strategy cannot yield any upper exponential rate strictly
below the augmented volume, even for arbitrarily large fixed powers.

When a hyperbolic nontrivial filling with smaller volume is under
consideration, the [representation-volume strictness theorem](general_representation_volume_kernel_strictness.md)
identifies the needed strict geometric decrease. Inequality (9)
shows why a successful direct spectral proof must retain cancellation
beyond (6). It does not contradict a phase-preserving bound, the volume
conjecture, or a source estimate using different structure. The case
n=0 is excluded: its nilpotent derivative weight vanishes.

## 3. The exact Gaussian retains the missing phases

The existing [Gaussian filling theorem](actual_coherent_filling_gaussian_chirp.md),
section1, proves even powers using full Hermite functional calculus.
The same value-and-derivative argument gives every integer n:

    hbar=2pi i/N, K(z)=arccosh(-z/2)^2,
    R^n=q^(n d^2/4) exp[n K(Omega)/(2hbar)].              (10)

K is analytic on C minus[2,infinity), with its removable value at -2.
The fractional q power uses the literal original Log q. At a paired
node set phi=pi(2a+1)/N and s=d-2a. Then

    K(c_a)=-pi^2s^2/N^2,
    q^[(d^2+s^2)/4]=lambda0(-1)^a q^[a(a+1)],
    K'(c_a)=-pi s/[Nsin(phi)],
    [n/(2hbar)]K'(c_a)=-ns/[4i sin(phi)]=n gamma_a.

Thus (10) matches every derivative as well as every value. The odd
simple node needs only its value. The unwrapped sign in the value
formula is (-1)^a=exp(-pi i a); resetting it to the opposite analytic
character would change the derivative. Full Hermite uniqueness proves
(10), including n<0. This is not a generic-q identity or a unitary
diagonalization. The cut at2, the nodes approaching it, all source
punctures and the noncommuting neighboring Casimirs remain relevant
to a global estimate.

## Validation and remaining scope

The [focused audit](../experiments/audit_actual_direct_long_power_source.py)
compares homogeneous compositions with independently built original
R matrices, including wrong-unwrapped totals and both signs. It also
constructs the canonical Hermite basis and checks the coefficientwise
comparison and Gaussian value/derivative data at both parities.
[Results](../experiments/actual_direct_long_power_source_results.json)
record the finite checks; they do not serve as a proof of an asymptotic.

The finite audit checks the original powers, physical entries, wrong-total zeros, Hermite data, Gaussian values and derivatives. The phase-blind envelope does not imply a phase-preserving global rate or a selected-cycle contribution.