# Actual complementary heads and the outgoing large-clock packet

30 October 2026. Independently reviewed. Two exact source
identities extend the proved boundary packets. Generic Chevalley
complementation transports the retained 0F1 normals to the small
second-clock regime. A separate positive-matrix comparison controls
the outgoing large-second-clock numerator at the root, through the
fold. The original scalar factors and large partner remain explicit.
This does not yet assemble every cup factor or select a global period.

## 1. An exact generic reciprocity, before any root collision

Let H=H_m^B(U,V) be the actual generic white polynomial, and put
A0=Q^d=(BQ)^(-1), d=N-1 fixed. Then

    H(A0/V,A0/U)=A0^m(UV)^(-m)H(U,V).                   (1)

Here U=Q^x,V=Q^y use their marked logarithms, and the complementary
heads are EXACTLY d-y,d-x. In particular d does not move with the
quantum period, and (1) may be genuinely differentiated.

There is a direct independent-variable proof from the actual
[white Ward equations](actual_augmented_plat_framing_density_source_ward.md).
Set Htilde=(UV/A0)^m H(A0/V,A0/U). It is polynomial of degree at
most m in each variable. Substituting X=A0/V,Y=A0/U shows that
the E equation for H becomes the F equation for Htilde, and the F
equation becomes its E equation, with the original coefficients.
For example multiply the E equation at X,Y by UV/A0^2; it reads

    U(1-V)H(QX,Y)+(1-U)H(X,QY)=(Q^m-UV)H(X,Y),

which is precisely the transformed F equation.

These two equations determine the polynomial up to one scalar.
To see this without a finite-grid continuation assumption, expand
in the Newton basis P_b(U)=product_(r<b)(U-Q^r). After removing
the first b basis terms, evaluate the F equation at U=Q^b. The
coefficient h_b(V) must satisfy

    Q^b(1-V)h_b(V/Q)=(1-VQ^(b-m))h_b(V).

Among polynomials of degree at most m its solutions are exactly
the multiples of V^b P_(m-b)(V), as follows by coefficient
comparison, starting at its lowest power. Induction gives the
actual Newton basis used in the source. The E equation then fixes
its adjacent coefficients by the original generic ratio. This is
a rational-function proof for generic Q,B; specialization follows
after clearing denominators.

Finally H(0,0)=(-1)^m Q^[m(m-1)/2]. The coefficient of U^mV^m
in Htilde is A0^(-m)H(0,0)=(-B)^m Q^[m(m+1)/2], exactly the
top coefficient of H. This proves (1) with scalar ONE, and in
particular retains the actual Chevalley normalization.

## 2. The genuine small-second-clock packet

Suppose at the root U_N is in a fixed compact subset of C*,
V_N=N^(-2)v_N with v_N in such a compact, and the fixed marked
heads have size O(N log N). Retain t=N^2 epsilon and all moving
quantities from the
[generic resonant hard-edge theorem](actual_q_hahn_generic_resonant_hard_edge.md).
The transformed clocks U'=A0/V,V'=A0/U satisfy its hypotheses.
At t=0 define

    kappa'_N=A0(0)/v_N, V'_N=A0(0)/U_N,
    K'_N=sin^2(pi m/N)(V'_N-1)/(pi^2 kappa'_N V'_N).

Equation (1) transports the exact normalization as well:

    Z_low(t)=c_m(t)A0(t)^m
                 product_(r<m)(1-Q(t)^r V(t)/A0(t))
            =(-1)^m Q(t)^[m(m-1)/2]
                 product_(r<m)(1-B(t)Q(t)^(r+1)V(t)).     (2)

Thus, uniformly on each fixed |t|<=rho<pi,

    H_m^B(U,V)/Z_low(t)
      =0F1(;1-t/(pi i);-K'_N)+O((1+log N)/N).            (3)

All fixed scaled genuine quantum jets have the same convergence.
The transformed heads d-y,d-x are fixed as epsilon varies; neither
the A0 derivative nor the marked character is suppressed. Equation
(2) notably cancels the B powers in c_m A0^m exactly. The estimate
remains absolute across zeros of the limiting function.

## 3. A uniform comparison of the two actual positive matrices

At the ROOT let a<=floor((N-1)/2), theta=pi/N, and use the actual
Hermitian matrices H_+,H_- from the
[full physical determinant theorem](actual_q_hahn_full_physical_complex_packet.md).
Their diagonal is

    d_n=1/[cos(n theta)cos((n+1)theta)],

and their adjacent upper entries are

    sqrt(B_n)[sin(n theta)+/-i cos(n theta)],
    B_n=sin^2(n theta)/[cos^2(n theta)
                      sin((2n-1)theta)sin((2n+1)theta)].

They satisfy, uniformly in N,a including the maximal folded a,

    H_+ <= 2H_-+8I,       H_- <= 2H_++8I.                (4)

Here the inequalities are Hermitian quadratic-form inequalities.
The proof retains their exact endpoint coefficients. Both matrices
have the same Cholesky pivots as the positive D matrix, namely

    p_(n-1)=sin(n theta)/[cos(n theta)sin((2n-1)theta)].

Write their quadratic forms as sums of squared adjacent Cholesky
terms and the final positive pivot. Flipping an offdiagonal phase
changes its term by 2i sqrt(B_n)cos(n theta)/p_(n-1) times the
next coordinate. The inequality |x+y|^2<=2|x|^2+2|y|^2 gives
an additional diagonal cost

    8 B_n cos^2(n theta)/p_(n-1)
                 =4sin(2n theta)/sin((2n+1)theta)<=8.

Indeed sin(2n theta)=2cos(theta)sin((2n+1)theta)
-sin((2n+2)theta), and the last sine is nonnegative for every
actual offdiagonal n<=a-1. This proves the first inequality in
(4), and complex conjugation proves the second. No lower
eigenvalue estimate or inverse channel norm is introduced.

## 4. The actual root numerator when the second clock is large

Put K_a=[2a choose a]_Q. The exact source determinant, with its
retained scalar, gives

    H_a^1(U,V)/V^a
       =K_a det[I-(qU/2)H_--(q^-1/(2V))H_+].           (5)

For example derive this from R_a(z;-cos gamma)
=det[zI-(e^(i gamma)H_-+e^(-i gamma)H_+)/2], with
z=q^t/U, e^(i gamma)=q q^t and (q^t)^2=UV, before canceling
the displayed powers. This proves (5) as a polynomial identity
and does not make a square-root choice in its final formula.

Let qU range in a fixed compact subset of Re z<0, and let
V=N^2 kappa_N with kappa_N in a fixed compact subset of C*.
Set M0=I-(qU/2)H_-. Then

    H_a^1(U,V)=V^a K_a det(M0)[1+O(N^-1)].               (6)

This is a UNIFORM RELATIVE estimate, including folded a. To prove
it put D0=I+(eta/2)H_-, where -Re(qU)>=eta>0.
The conjugated M0 has inverse norm at most one, while (4) bounds
D0^(-1/2)H_+D0^(-1/2) uniformly. Thus the relative perturbation
from the last term in (5) has norm O(N^-2). Expanding Log det
costs at most a O(N^-2)=O(N^-1). This also proves nonvanishing
and a marked relative logarithm on the stated domain. At qU
negative real, det M0 is strictly positive. K_a and V^a retain
their original phases.

For the actual LARGE root channel m=d-a, the exact root partner
identity supplies

    H_m^1(U,V)=H_a^1(U,V)
                      product_(r=a)^(m-1)(UV-Q^r).

Consequently its corresponding packet is

    H_m^1(U,V)=V^m U^(m-a) K_a det(M0)[1+O(N^-1)].       (7)

The added product differs from (UV)^(m-a) by 1+O(N^-1).
This is explicitly a ROOT identity: it is not differentiated as
a generic large/small collision. Generic normals in this second
large-clock regime remain separate from (6),(7).

## 5. The genuine paired 200/220 circle

There is an exact geometric use of the negative ray in (6).
Take the root theorem's 200 box with B=-J, J=[[1,1],[0,1]],
and write

    A=[[a,-(a+1)^2/4],[4,-2-a]], P=BA,
    C=I+b(P+I), Aout=C^-1 A C,
    Q1=e[[1,z],[0,1]], W=A^-1Q1, e=+/-1.

Direct multiplication, with the ACTUAL inverse collar transport,
gives

    W_21=-4e,       (Aout W)_21=16e b^2,
    U_geom,out=-W_21/(Aout W)_21=1/(4b^2).               (8)

Here C names the auxiliary collar, so its inverse gives the displayed
transport. Conventions naming the transport itself C write C A C^-1
instead. The lower-left entry and ratio in (8) are unchanged under
b->-b, so this squared-ray certificate is identical in those two
notations; it does not change any primitive peripheral mark.

The [marked complete rectangle collar](actual_matching_edge_geometric_target_polynomial.md)
has b=-i/(2c), c>0,
including its retained half-twist convention. Thus U_geom,out=-c^2.
The physical half-index argument is U=q^-1 U_geom,out up to the
retained finite-r correction, so qU approaches precisely this
negative ray. Formula (7) therefore gives the nonzero outgoing
220 numerator paired with the incoming 200 Bessel packet. No
independent phase of U has been chosen.

The actual white monomial, F_m denominator, categorical dual,
channel cup, physical caps and exterior source scalar still have
to be retained when assembling the full box. Their exact lifts and
logarithmic-escape estimates remain available; they are not set
equal to one by (8). Other prefix patterns, original boundary
currents and the global relative-cycle coefficient are not resolved
by this local paired-numerator statement.

Focused audit: [original generic reciprocity and complementary packets](../experiments/audit_actual_q_hahn_complementary_hard_edge.py),
with [saved results](../experiments/actual_q_hahn_complementary_hard_edge_results.json).
It checks 126 original generic reciprocity four-jets, retaining 504
coefficients; three exact paired-circle matrix identities; 17 folded
positive-matrix comparisons and 173 pivot evaluations; 21 small and
21 large original-source determinant identities; and eight each of
root220 relative-rate, generic002 packet and genuine002 first/second
normal diagnostics. These finite checks supplement the proofs and do
not prove their uniform asymptotic estimates.

Independent analytical reviews checked the generic Ward uniqueness
and scalar, marked complement normalization, both uniform Hermitian
comparisons through the fold, actual root determinant and forced
partner factors, and the squared geometric collar ratio. A separate
fresh redirected audit replay passed every stated check at 95 digits.
The review covers the exact reciprocity, genuine002 normals and
root220 numerator packet; it does not supply generic220 normals,
a completed boundary-circle packet or a global period coefficient.
