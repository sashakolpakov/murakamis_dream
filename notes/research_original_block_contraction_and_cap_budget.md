# Original coefficient blocks, stationary touching, and the absolute cap budget

31 October 2026. **analytical research lemma.**
Unpublished. No full-source or filling theorem is asserted.
The purpose is
to identify an exact usable closure statement and the two missing steps
between the proved whole-star estimate and an absolute Phi_D bound.

Inputs are the [whole-star spectral gap](research_cap_cross_shared_star_spectral_gap.md),
[cap-leaf structural theorem](research_cap_star_cut_and_cross_stellar_reduction.md),
[original stationary classification](research_full_fiber_sharp_stationary_classification.md),
[uniform sharp coefficient upper](research_global_sharp_coefficient_limsup_majorant.md),
[closed endpoint coefficient entropy](actual_fejer_full_kernel_entropy_identity_reduction.md), and
[unique endpoint maximum](actual_fejer_unique_geometric_maximizer.md). Their local estimates,
endpoint theorem and original source identities are inputs. The
unproved prescribed-chart full-source theorem is not an input.

## 1. Exact contraction before localization

Fix the original marked diagram. Every coupon has degree d=N-1;
ordinary targets are d and protected targets are zero. Keep the actual
finite LEFT/CROSS/RIGHT restrictions whenever a sector is specified.
Let B be a collection of coupons and I a set of ordinary faces all of
whose incidences belong to B. Define the original contracted polynomial

    B_N(Y;theta)=[prod_(a in I) A_a^d] prod_(e in B) P_e,N(A,Y;theta_e).

The exterior G_N has no A_a incidence. Consequently

    [original target] prod_e P_e,N
      =[Y^t] B_N(Y) G_N(Y).                              (1)

All shared boundary variables remain identified. The degree of B_N is
d(|B|-|I|); no new target or normalization occurs.

Expand the EXTERIOR into its original local coefficient arrays k.
Its boundary demand left for B is

    a_N(k)_f=t_f-sum_(e outside B) k_(e,f).

Only nonnegative a_N contribute. The exact identity is

    [Y^t]B_N G_N
      =sum_k [Y^(a_N(k))]B_N prod_(e outside B) p_e,N(k_e). (2)

This is a sum over polynomially many arrays at a fixed diagram. In
(2) all internal B allocations have ALREADY been summed with their
original signs. In particular no restriction on one internal cap
index is introduced by restricting k.

Let a=a_N/d. Suppose, uniformly on a spectral compact K, the actual
boundary coefficients have an upper rate b(a,theta), in the sequential
sense that every convergent admissible (a_N/d,theta_N) has limsup
N^-1 log |[Y^a_N]B_N| at most b(a,theta). Take b upper semicontinuous.
The established uniform local coefficient upper for the exterior then
gives

    limsup N^-1 log sup_(theta in K) |[Y^t]B_N G_N|
       <= max_(q_out,theta in K)
          {b(tbar-A_out q_out,theta)+sum_(e outside B) H_e(q_e,theta_e)}.
                                                               (3)

The maximum ranges only over limits of exact exterior arrays for which
the boundary degree is supported. Enlarging this to the corresponding
closed original incidence image is safe for an upper bound. If that
image is empty, there is no term. Formula (3) uses compactness and the
polynomial array count, not lower rounding or a minimax interchange.

In particular a torus estimate

    sup_(|Y|=L) |B_N(Y;theta)| <= exp(N(W(L)-delta(L)+o(1)))

implies the genuine boundary coefficient estimate

    b_L(a)=W(L)-delta(L)-a dot log L.                    (4)

Any finite number of such bounds can be MINIMIZED for the SAME
boundary coefficient. One may also include its direct sharp block
upper, obtained by summing its actual internal arrays. Thus

    b(a,theta)=min{b_direct(a,theta),b_L1(a),...,b_Ls(a)} (5)

is legitimate. For a local spectral domain, include b_L only there;
one can work with closed smaller domains or continuous majorants to
avoid a discontinuous convention at its boundary.

The same proof works for a FIXED partition into port-disjoint blocks
with disjoint exclusive internal faces. Boundary variables of distinct
blocks may coincide. Sum their b's and the remaining local H's on the
reduced original flow. This gives an explicit finite-dimensional upper
bound for the same source, retaining all targets.

## 2. What a finite cover is allowed to cover

A spectral cover is harmless: at a fixed theta, estimates from different
block decompositions bound the SAME full coefficient. Thus one may take
the minimum of their full capacities from (3), and use a finite spectral
cover on which this minimum is below Phi_D by a uniform positive margin.
That is the same logical operation as the mark-spectral cover.

A cover in INDIVIDUAL INTERNAL INCIDENCE ARRAYS is different. A mask
cutting (2) preserves B_N exactly if it is constant on each fiber of
the map from full arrays to exterior arrays k. Equivalently the mask
must depend only on data left outside the contracted block. This is an
exact sufficient condition. It is also necessary for the proposed
factorization with unchanged B_N and a mask depending only on exterior
data, as a formal identity for arbitrary local coefficients. Assign an
independent symbol to each local monomial coefficient of each coupon.
Distinct original incidence arrays give distinct products of these
symbols. For fixed exterior array k, comparison of these independent
monomials forces the full-array mask to have the same value on every
internal array over k. No cancellation between different symbolic
products can repair a nonconstant mask.

This formal coefficient test is a logical obstruction to an inference,
not an actual-link counterexample. A special identity for the actual
coupons could give additional cancellations, but it would be a new
input beyond the unchanged whole-star theorem.

For overlapping stars a priority partition into neighborhoods need not
have this fiber property for the star assigned to each piece. For
example, the exterior degrees of one star may include a coupon inside
the other. A common-exterior degree partition is safe, as is a fixed
disjoint-block contraction. Otherwise an additional projection or
boundary-tensor identity is required. One cannot reuse the unchanged
whole-star bound for an arbitrarily cut internal sum.

Consequently (3)-(5), rather than a cover of individual saddle arrays,
are a rigorous quantitative extraction theorem. An absolute criterion
is that the right side of (3), or the minimum over finitely many valid
full capacities, is less than Phi_D. This criterion still has a
variational comparison to prove on a general prescribed diagram.

## 3. The star envelope actually touches the stationary sharp action

There is a useful precise connection between the existing weighted star
bound and the sharp maximum; the two are not unrelated envelopes.

Take a classified stationary residual cap F=(u,A,v,C), u=v=0,
q_F,A=1-nu, q_F,C=nu, 0<nu<1/2. Suppose every other A-incident
coupon is CROSS. Let B consist of F and ALL these neighbors, and
I={A}. The common positive multipliers give L_A=L_C. Let q* be the
classified stationary assignment and let a* be its total B-boundary
loads, with A omitted. Write

    W(L)=sum_(e in B minus F) X_e(L),
    X_e(L)=Q_e,input(L)+Q_e,output(L).

At each stationary CROSS neighbor, the same ordinary positive weights
attain its triangle Legendre formulas, including its protected zeros.
Therefore

    X_e(L)=h_e(q*_e)+q*_e dot log L.

This follows alternatively from concavity of the complete two-triangle
entropy and the common first-order equations; it is not a weighted
maximality assertion about a Green coupon.

The total B load at A is one, and its cap weighted load equals

    (1-nu)log L_A+nu log L_C=log L_A.

Since the cap sharp action is zero, exact cancellation of these two
log L_A terms gives

    W(L)-a* dot log L = sum_(e in B) H_e(q*_e).          (6)

Thus the proved spectral-star estimate, with its actual gap delta>0,
gives a boundary-coefficient upper at a* equal to the original sharp
block action MINUS delta. After adjoining the unchanged exterior at
q*_out, the expression in (3) is

    total sharp action(q*)-delta.                      (7)

Continuity of the exterior H and of the affine term in (4) preserves a
strict improvement in a neighborhood of the EXTERIOR data and spectra.
The whole cap spectral disk and CROSS strips are genuine fixed
neighborhoods, as required by the star theorem. Equation (7) also holds
for a maximum restricted to closed NC once the independently proved
strict overload margin permits the original stationary equations.

Notice what is and is not localized: (7) bounds every internal star
allocation compatible with that exterior coefficient, not just those
near q*. This is exactly why (2) is the correct decomposition.

As a useful conditional consequence, if all maximizers of a specified
sharp sector capacity M are covered by exterior-fiber neighborhoods
admitting (7) for ONE FIXED block, and the block direct sharp upper
is at most M elsewhere, compactness of (3)-(5) gives an actual strict
upper M-delta_0 for some delta_0>0. A compatible finite partition into
blocks has the same consequence. This is a strict improvement relative
to M; it does not assert M-delta_0<Phi_D.

## 4. The absolute cap deficit is exactly 2 f(nu)

Let

    f(t)=-integral_0^t log tan(pi s) ds,
    f(0)=f(1/2)=0, f(t)>0 for 0<t<1/2.

Use h_0 for the actual positive endpoint coefficient entropy (both
parities, with the prescribed odd regularizer), and H for the sharp
real spectral upper. The closed monomer formula proves on the cap
degrees just used

    H_cap=0,       h_0,cap=-2f(nu).                    (8)

At a classified CROSS neighbor at spectrum -2, H=h_0. Hence for a
cap-only classified datum, with caps indexed by F,

    F_sharp(q)=H_endpoint(q)+2 sum_F f(nu_F).          (9)

This is an identity on the original flow, not a smoothing or a changed
triangle allocation. The endpoint theorem and unique geometric maximum
give H_endpoint<=Phi_D. More quantitatively let

    g_D=Phi_D-max_(q in original closed NC) H_endpoint(q)>0. (10)

The maximum exists on the compact original flow; it is strictly below
Phi_D because the unique geometric optimizer is strictly CROSS. Empty
NC is vacuous. Thus on the cap-only data

    F_sharp(q)-Phi_D <= 2 sum_F f(nu_F)-g_D.            (11)

In particular a cap-only datum of value at least Phi_D must satisfy
2 sum f(nu_F)>=g_D. With one cap its nu is in a compact subinterval
of (0,1/2). With two caps at least one has a definite positive f;
this does not place BOTH parameters away from their endpoints.

Formula (11) identifies a quantitative sufficient budget for a VALID
localization or disjoint-block extraction: a cancellation loss exceeding
2 sum f(nu_F)-g_D gives an absolute improvement below Phi_D at that
datum. Loss at least 2 sum f(nu_F) is a simpler conservative sufficient
budget, leaving the original endpoint gap untouched. A potentially
sharper budget uses the actual endpoint value H_endpoint(q), not g_D.

The star theorem currently provides delta>0, not an inequality between
delta and this deficit. Equations (6)-(7) explain how to compare the
quantities without confusing different weighted envelopes. They do
not prove the missing comparison.

For the actual contracted star an even more intrinsic target is its
positive ENDPOINT REFERENCE with the SAME A^d and boundary degrees,
including the actual odd regularizer and the same sector projections.
Let its coefficients be r_N(a)>0 on the relevant support. An estimate

    |[Y^a]B_N| <= exp(o(N)) r_N(a)                    (12)

uniformly over original admissible a, and in an appropriate spectral
neighborhood, pays the entire boundary-optimized endpoint deficit.
The [two-spectrum degree-two theorem](research_cap_cross_two_spectrum_neighborhood_stability.md)
proves the endpoint version with exp(o(N)); on a fixed nearby spectral
polydisk it gives exp(N omega(epsilon)+o(N)), with omega(epsilon) tending
to zero, for its typed pair. The arbitrary
valence star theorem has not proved (12).

## 5. The exact minimal replacement test for arbitrary exteriors

Fix any contracted B_N and positive comparison R_N with the same
boundary degree. Restrict to boundary exponents a which are compatible
with the specified remaining original target t, namely 0<=a<=t and
any additional genuine exterior support restrictions. For a family of
arbitrary exterior coefficients supported on all such complements,
the following are equivalent:

  (i) |[Y^a]B_N| <= kappa_N [Y^a]R_N for every such a;

 (ii) |[Y^t]B_N G_N| <= kappa_N [Y^t]R_N |G_N|_coeff
      for every polynomial G_N with that allowed exterior support.

The implication (i)->(ii) is exact convolution and the triangle
inequality. For (ii)->(i), choose the single monomial G_N=Y^(t-a).
One may include its harmless unit phase. Unsupported comparison
coefficients must then force the corresponding B coefficient to vanish.
No statement about inadmissible exponents is needed.

For the actual fixed exterior, (i) is a sufficient condition, not a
claimed necessary condition: its special source correlations can
provide more cancellation. This distinction leaves room for a genuine
larger-source identity beyond (12).

For port-disjoint exclusive blocks, (12) at every block combines by
ordinary positive convolution while retaining shared boundary labels.
For overlapping blocks it does not automatically iterate. Taking an
absolute value after the first contraction can erase the second block's
internal signs, and its factors are no longer the unchanged original
block. Either a single larger-block comparison or a proved compatible
replacement operator is needed.

## 6. Why strict loss at old maxima is not an iteration theorem

Two logically distinct claims are sometimes conflated:

  A. every high maximum of the original sharp functional has a
     cancellation block giving some positive loss;
  B. the actual source has rate at most Phi_D.

Even with completely compatible localization, A gives a strict reduction
from the original maximum M. It does not say the reduction exceeds
M-Phi_D. A one-dimensional logical test is H(x)=Phi_D+a-x^2 and
an exactly known improved bound H(x)-b, where 0<b<a. The maximum is
strictly reduced, all original maxima are covered, but the resulting
upper remains Phi_D+a-b>Phi_D. This is not a diagram counterexample;
it disproves the purported abstract implication.

Nor can the SAME estimate simply be applied again to subtract another
b. After replacing the original upper by the minimum of new bounds,
its new maxima can occur on a switch between bounds and need not
satisfy the original sharp stationary equations. The boundary
activation and cap-leaf theorems classify maxima of the original
functional on its original fiber. They have not been proved for these
new contracted, often nonsmooth upper functionals. Reusing their
conclusion there would be circular.

A valid finite iteration must therefore supply, at each stage, an exact
coefficient-preserving replacement and a proved decreasing potential
with a quantitative budget, together with either termination at the
positive endpoint source or an absolute terminal bound. Current
cap-leaf selection proves existence of an applicable relative star
at certain original maxima; it does not supply these iteration data.

The stellar identity reinforces the distinction: it preserves
M_cap-Phi while increasing the cap incidence degree. It transports a
CLASSICAL sector optimization, not the finite signed boundary
polynomial or its needed compensation (12).

## 7. Endpoint resolvent: exact identity, but no free positivity

For the full original Casimir quotient, chi_N(Omega)=0 and
chi_N(2)=4 give the exact polynomial resolvent identity

    (2-Omega)V_N(2)=4I.                              (13)

Every unchanged linear original source functional Lambda therefore
satisfies 2Lambda(V_N(2))-Lambda(Omega V_N(2))=4Lambda(1).
The extra Omega coupon has not disappeared. Projecting to the cap
range produces the already known boundary currents of the Newton
contiguity; omitting them would alter the source.

An ordinary self-adjoint Casimir model would bound the scalar inverse
by its spectral distance, but cannot be assumed to preserve the
complete-colored quotient. The even coupon
L_N=(-1)^d U_d(z/2) has L_N^2=0 modulo chi_N and vanishes at every
distinct spectral node, whereas the [actual conditioned coefficients](research_cap_cross_high_demand_signed_contraction.md#8-low-demand-still-detects-the-actual-casimir-jordan-data)
Lambda_n(1,L_N) are strictly positive for every 0<=n<=M,
where M=N/2-1; in particular Lambda_0(1,L_N)=N^2. Thus a coupon-uniform
semisimple adapter preserving these observables is impossible. This
does not exclude a special identity for the fixed resolvent, an
explicit treatment of its confluent corrections, or a nonlinear
bound not intertwining arbitrary coupons.

## 8. Current concrete missing lemma

The precise new candidate is a cancellation-aware boundary comparison
for a whole cap/CROSS star at original A^d, either (12), or a weaker
weighted coefficient bound whose loss satisfies the explicit budget
in (11) after a legitimate reduced-flow maximization (3). It must
retain every boundary face degree and the actual parity reference.

Such a theorem would be a real absolute input. A finite collection of
compatible bounds satisfying (3)<Phi_D uniformly off the geometric
spectral cube would feed the [existing entire-period criterion](research_mark_spectral_cover_filling_volume.md); its
nonzero geometric packet and primitive filling action are separate
already proved inputs. Neither a positive local gap by itself nor a
classification of old maxima supplies that strict absolute premise.

No global counterexample has been proved here. The existing shared-star
and structural notes state their limitations correctly; the gap is in
the unproved bridge one might try to infer from them.

## scope

Block localization uses independent formal local coefficients. Its stationary touching identity retains the negative endpoint cap entropy and the non-iteration limitation; a relative block loss alone does not pay an absolute volume deficit.

The all-parity original target, actual sector projections, protected
zeros, and distinction between endpoint compensation and a positive
relative gap are retained. No source lower bound, universal cap
elimination, absolute prescribed-chart comparison, or filling theorem
is inferred.
