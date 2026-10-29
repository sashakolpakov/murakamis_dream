# Polynomial actual boundary Gram costs on the entire supported color domain

29 October 2026. The correlated six-head marked boundary Gram has
POLYNOMIAL source cost on EVERY supported folded color cell, at both
level parities. No fixed central corridor is required. The second-root-
zero Racah terms do not need a uniform strict exponential gap: a
global elementary sine-product inequality bounds every such term by
the same action as a positive main term. All low/high partner branches,
the original marked normal and every lower moment are retained.

This controls the pointed algebraic Gram from the
[actual six-pants boundary](actual_six_pants_boundary_torsor_and_sewing.md).
It does not identify its constructed reflection with a physical
mirror, bound the physical change of frame or general recouplings,
or prove a graph's sharp geometric energy/noncancellation.

## 1. The whole-support theorem

Let N>=2, d=N-1, M=floor(d/2), q=exp(pi i/N), and take ANY

    0<=l_1,l_2,l_3<=M, l_1+l_2+l_3>=d.            (1)

There is one paired axis for each 2l_i<d; let their number be r<=3.
The actual regular source cell, complete-circle coordinates eta_i,
original marked co-source lambda and nested-cup vector v_l are those
of the proved boundary theorem. In particular

    m_I=lambda(eta_I v_l),
    tau_l=m_all=Z_N(l)/N^(3-r)>0,
    q_l(eta)=sum_I (m_(I^c)/tau_l)eta_I, q_l(0)=1,
    K_l=sum_I |coeff_I(q_l^(1/2))|^2.              (2)

There are absolute constants C,C0, independent of N and of ALL
labels satisfying (1), such that

    max_I |m_I/tau_l|<=C0 N^C,
    1<=K_l<=C0 N^C.                               (3)

The exponent may be increased between the two estimates. Thus the
actual source and dual costs of this prescribed Gram are exactly
K_l and tau_l^2 K_l, with log K_l=O(log N)=o(N) uniformly on the
whole support. The estimates include saturation faces, edges,
corners, nearest paired neighbors and odd simple axes.

Unsupported open source cells are not deleted. They lack the positive
top moment in (2), so (3) is asserted precisely on (1). The theorem
does not assert a polynomial norm for the embedding of this finite
coordinate cell into the physical tensor product.

## 2. The original generic trace and all its normal factors

The [proved generic source identity](actual_generic_trivalent_racah_source_identity.md)
and the genuine ordered physical trace give, for each unfolded ordinary
triangle j=(a,b,c), the EXACT rational function

    T_j=(-1)^d product_i[2j_i+1]
         *[r_1]![r_2]![r_3]!/[J+1]!
         *product_i([j_i]!^2[d-j_i]!/[N+j_i]!) S_j^2,
    J=a+b+c, r_i=J-2j_i,

    S_j=sum_t (-1)^(d+t)[N+t]!
          /{[d+t-J]! product_i[t-j_i]![J-j_i-t]!},
    max(j_i,J-d)<=t<=J-max(j_i).                  (4)

Here [n] and [n]! are symmetric quantum integers and factorials at
zeta=q(1-Z)^(1/(2N)), with the branch through q. These are the
actual source functions, not a separately normalized 6j model.

The unfolded choices are j_i=l_i or d-l_i on a paired axis, and
the single l_i on a simple axis. With the original paired-circle
unit ell_j(Z)=L_N(c_j(zeta))/Z, the physical moment formula is

    m_I=(-1)^d(q-q^(-1)) [Z^(r+1-|I|)]
         sum_unfolded Z^r T_j product_(i in I)ell_(j_i)(Z). (5)

There are at most eight summands and the coefficient order is <=4.
The original marked physical trace is exactly the one in (5).
No ordinary quantum dimension is specialized to zero before this
coefficient is extracted.

Two elementary integer facts now hold on the ENTIRE supported domain.
For every unfolded branch,

    d<=J<=2d, 0<=r_i<=d.                           (6)

To verify them, increase a coordinate from l_i to d-l_i. The maximum
J is 3d-sum l_i<=2d and the minimum is sum l_i>=d. For r_i, its
maximum over the flips is 2d-sum l_i<=d and its minimum is
sum l_i-2l_i>=d-2l_i>=0. In particular every unfolded branch is
an ordinary triangle.

Moreover EVERY one of the seven denominator factorial indices in
S_j is less than N, for every true term. Indeed

    0<=d+t-J<=d-max j_i<=d,
    0<=t-j_i<=some other label<=d,
    0<=J-j_i-t<=some other label<=d.               (7)

For example t<=j_i+j_k bounds t-j_i, and t>=j_k bounds
J-j_i-t. No root denominator appears in any Racah summand. Its
numerator contains [N] once for t<N and both [N],[2N] for t>=N;
t<=2d<2N excludes a third zero. This is the only termwise change
at the second band.

## 3. A uniform global profile, including the second-zero band

Let L(t)=integral_0^t log|2sin(pi u)|du, extended periodically to
R. Its period is 1 and L(-t)=-L(t). Define the EXACT half-step
scaled colors

    a_i=(j_i+1/2)/N, S=sum a_i,
    x_i=S/2-a_i (i=1,2,3), x_4=1-S/2.

Equations (6) imply

    0<x_i<1/2 for all four i, sum_i x_i=1.         (8)

The half-step is useful: a high-partner replacement j_i->d-j_i
is exactly a_i->1-a_i. It permutes the four x coordinates while
replacing each by its complement 1/2-x. There is no O(1/N) error
in this assertion. For instance flipping the first color sends

    (x_1,x_2,x_3,x_4)
       ->(1/2-x_4,1/2-x_3,1/2-x_2,1/2-x_1).     (9)

For a summand put s=(t+3/4)/N and v=s-S/2=(t-J/2)/N. Its three
child pairs obey

    x_i+v=(t-j_i+1/4)/N>0,
    x_i-v=(J-j_i-t+1/4)/N>0, i<=3.                (10)

Also x_4+v=1-(J-t+3/4)/N is in (0,1). The fourth minus argument
is x_4-v=1-s=(N-t-3/4)/N: it is positive for t<N and negative
for t>=N, precisely the second-zero band.

After removing its one or two root zeros, the absolute factorial
summand has, up to polynomial factors, the profile

    H_x(v)=-sum_(i=1)^4 [L(x_i+v)+L(x_i-v)].       (11)

For t<N the numerator is s_t; for t>=N it is s_(t-N), apart from
the complete root-orbit polynomial factors. Both have rate N L(s)
up to O(log N), because L has period 1. The denominator d+t-J
has rate L(1+s-S)=-L(S-s). Substitution of (10) then gives (11).
This same argument covers endpoints: changing an argument by O(1/N)
changes N L by O(log N), uniformly even at a zero of sine. One may
prove this modulus of continuity by integrating |log u| over an
interval of length O(1/N) near the nearest integer.

The decisive inequality is

    H_x(v)<=H_x(0)=Phi(x):=-2sum_i L(x_i)          (12)

for EVERY actual term, including the second-zero band. Here is a
direct elementary proof. The function is even in v, and (10)
gives |v|<min(x_1,x_2,x_3). For v>0 away from its logarithmic
corner, put alpha_i=pi x_i and theta=pi v. Then

    H_x'(v)=log |P_minus/P_plus|,
    P_plus=product_i sin(alpha_i+theta)>0,
    P_minus=product_i sin(alpha_i-theta).          (13)

If theta<alpha_4, every factor is positive and
sin(alpha_i+theta)-sin(alpha_i-theta)
   =2cos(alpha_i)sin(theta)>0.
Thus |P_minus|<P_plus. If theta>alpha_4, exactly the fourth
minus factor is negative. Expand the sum of the two products:

    P_plus+P_minus
      =2 sum_(A subset {1,2,3,4}, |A| even)
         cos(theta)^(4-|A|)sin(theta)^|A|
         product_(i in A)cos(alpha_i)
         product_(i notin A)sin(alpha_i)>0.        (14)

Every factor is nonnegative, and an interior term is strictly
positive by (8). Since P_minus<0, (14) again says
|P_minus|<P_plus. Continuity across theta=alpha_4, where (13)
tends to minus infinity, proves (12). Evenness treats negative v.
No local concavity or uniform strict exponential tail gap was used.

The integer nearest t=J/2 is a true term of the FIRST band: (6)
gives max(j_i,J-d)<=floor(J/2) and ceil(J/2)<=min(J-max j_i,d).
At that term |v|<=1/(2N), so the same uniform modulus of continuity
gives H_x(v)=Phi(x)+O(log N/N).

## 4. Positive main value and polynomial normal envelopes

For t<N, the exact root identity is

    ([N+t]!/[N])|_q=(-1)^t[d]![t]!.

All denominators in (4) are positive symmetric factorials at q.
Thus S_main/[N] has ONE common phase (-1)^d. Its positive
absolute sum is

    Rcore_N(j)=N sum_(true t<N)
       s_t/{s_(d+t-J) product_i s_(t-j_i)s_(J-j_i-t)}.

It has at most N terms and contains the midpoint term identified
above. The uniform two-sided sine-factorial estimate and (12)
therefore give, throughout the whole support and every branch,

    N^(-C)e^(N Phi(x))<=Rcore_N(j)
                              <=N^C e^(N Phi(x)). (15)

The estimate uses only ONE midpoint summand for its lower bound;
no bulk Hessian, saddle width or distance from a saturation face
is assumed. Second-band terms, after removing [N][2N], obey the
same upper bound by (12). They may approach the leading action at
boundary scales, which is why a uniform strict gap is unnecessary.

Use the common disk |Z|<=c/N^2. A quantum-factorial ratio with a
fixed number of factors and indices <=3N has, after explicitly
removing its zeros, a polynomial envelope relative to its nonzero
root product on this disk. This follows either from the proved
[bounded normal factorial estimate](bounded_normal_quantum_factorial_envelope.md)
or directly: a nonzero 1-q^(2k) has magnitude >=c0/N; its change
is O(|Z|), and O(N) such factors accumulate only bounded relative
growth here. Removed [N] and [2N] factors and the symmetric-int
normalization cost fixed powers of N. Their count is uniformly bounded.
Equations (7),(12),(15) hence bound the ENTIRE holomorphic S_j/Z
by poly(N)e^(N Phi(x)). Cauchy estimates for four fixed normal
orders add only another fixed power of N. No alternating-sum
cancellation is needed for the second-zero terms.

To include the complete prefactor of (4), note first that

    ([N] [j]!^2[d-j]!/[N+j]!)|_q=(-1)^j.          (16)

Its zero-removed envelope is polynomial, with no factorial action.
All three r_i are <N, while N<=J+1<2N. The zero-removed triangle
factor therefore has rate

    P(x)=sum_(i=1)^3 L(2x_i)-L(S-1),

up to O(log N). Each simple axis contributes one dimension zero
[2j+1]=[N]; the other dimensions and all ell_j in (5) have
polynomial fixed jets, uniformly to the nearest paired neighbor.
If s0=3-r is the number of simple axes, the prefactor without S^2
has zero order s0-4. Multiplication by Z^r and S^2, whose order is
at least two, leaves order at least ONE. Consequently

    Z^r T_j product ell

is holomorphic on the common disk; it is never estimated as a bare
singular expression. The preceding bounds give for its fixed jets

    |[Z^k]{Z^r T_j product ell}|<=N^C exp(N E(x)), k<=4,
    E(x)=P(x)+2Phi(x)
        =sum_(i=1)^4[L(2x_i)-4L(x_i)]
        =-2sum_(i=1)^4[L(x_i)+L(1/2-x_i)].         (17)

The second equality uses L(S-1)=-L(2x_4), and the third is the
elementary duplication identity for L. This expression is unchanged
by every permutation or individual complement x_i->1/2-x_i.
Equation (9) therefore makes E EXACTLY the same function for all
unfolded branches of a fixed folded triple, with these half-step
coordinates.

Finally the PROVED actual positive top moment has the exact weight

    Z_N(l)=N^2 product_i k_(l_i)
              s_(J_l-2l_1)s_(J_l-2l_2)s_(J_l-2l_3)
                    /s_(J_l-d) *R_N(l)^2.

The same midpoint argument (15), uniform factorial bounds and its
positive prefactor give

    N^(-C)exp(N E_fold)<=tau_l<=N^C exp(N E_fold)  (18)

on the ENTIRE supported domain. Endpoint factors s_0=1 cause no
problem, and replacing their scaled arguments by the half-step
ones changes logarithms by only O(log N). Combine (5),(17),(18),
sum at most eight branches, and absorb the polynomial |q-q^-1|:
this proves the first estimate in (3).

The finite square root of q_l=1+n_l is
sum_(k=0)^r binom(1/2,k)n_l^k, with n_l^(r+1)=0. It is a polynomial
of degree <=3 in at most seven normalized moments. Thus the first
estimate implies the second, with constants independent of the
labels and N. Its constant coefficient is one, so K_l>=1. This
completes the whole-support actual Gram theorem.

## 5. Scope and verification

The new ingredient beyond the central-corridor bound is the global
sine-product inequality (12)--(14), together with the half-step
folding coordinates. A second-zero action gap may vanish at boundary
scales; uniform positive factorial comparison replaces it. The
result controls the correlated marked Gram on its actual regular
source cells. It supplies neither a physical mirror interpretation
of that Gram nor a bound for genuine transitions between different
pair decompositions. Those remain separate global source/geometry
tasks; polynomial K alone has no hidden cuboctahedral volume term.

The [multiprecision source diagnostic](../experiments/diagnose_actual_whole_support_boundary_conditioning.py)
uses the proved generic trace (4), every partner and the original
physical circle normal. It compares two precisions and two normal
steps on saturation faces/corners and interior examples. These are
diagnostics; the uniform theorem follows from the finite generic
source identity, (12), common-disk factorial envelopes and the
positive midpoint bound, not sampling.

The [focused audit](../experiments/audit_actual_whole_support_boundary_gram_envelope.py)
and [recorded results](../experiments/actual_whole_support_boundary_gram_envelope_results.json)
verify the universal even-product polynomial with an identically zero
cleared numerator; 46,495 unfolded integer branches and 257,107 true
Racah terms at N=2,...,32; 215 independent generic physical-double-sum
versus Racah traces; and five all-moment original marked crosschecks.
Floating-point action comparisons in that audit are labeled diagnostics;
the proof of (12) is the exact sign argument (13),(14).

The separate [paired-precision data](../experiments/actual_whole_support_boundary_conditioning_diagnostic_results.json)
include ten boundary/interior cases through N=256, both parities,
simple axes and saturation corners. The largest displayed K is below
2.78; this finite observation is not used to choose the polynomial
exponent or prove its uniformity.

Independent internal analytical review: the Euler-atom agent re-derived
the entire support/half-step/range argument, both bands of (12), first-
band midpoint, common-disk fixed jets, full prefactor zero count and
the actual positive tau lower bound, and reported PASS. This is an
internal proof check, not external peer review or a global source
volume theorem.

The primary agent independently checked the half-step domains, exact
partner transformation, midpoint admissibility, both signs of the
global sine-product inequality, root-zero accounting and the uniform
fixed-jet argument, then freshly replayed the focused audit: PASS.
