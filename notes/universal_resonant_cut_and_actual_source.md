# An actual cut with a universal complete framing pole

Research theorem, 27 October 2026. For every complete discrete-faithful
knot representation, an exact inverse-pair insertion in the ORIGINAL
braid places a noncommuting meridian on the first slot at a second
physical cut. The actual prefix there is V=I. Its Fourier momentum
is a Möbius coordinate whose inverse framing map and density have
pole p=1, independent of the knot and first framing phase. The
added crossings have a nonempty regular
atom chart, so the existing nonzero geometric normal block persists.

This is an actual source-preserving choice of presentation and cut.
It does not replace the selected source by sampling its principal
density. That density is resonant at EVERY level. Controlling its
whole quantum completion and the original selected class remains
the missing geometric-period theorem.

Subsequent exact source calculation: the
[complete first-slot localization theorem](universal_resonant_fourier_source_completion.md)
proves J_(a,j)=P_N delta_(j,0) for EVERY first input, and in fact
L(X_j)=P_N X_j. Thus the original regular Fourier rows j!=0
vanish identically at completeness. The missing geometric-period
comparison concerns the resonant row. An
[actual all-strand Euler/Cauchy formula](all_strand_euler_cauchy_cap.md)
now supplies its finite source as an exact coefficient or two-point
divided difference, with the entire word retained.

## 1. Choose a meridian that does not fix the reference cusp

Fix a b-strand braid presenting the knot and the complete marked
holonomy. Normalize the reference meridian to

    J=[[1,1],[0,1]].

Write its initial developed meridians as mu_1=J,...,mu_b, using
the signed convention of [the actual prefix dictionary](prefix_adapted_two_position_framing_cover.md).
Some mu_i has nonzero lower-left entry, since otherwise the
representation is reducible. Choose the first such i.

Every preceding mu_j is J, not merely another upper triangular
matrix. Indeed mu_j=g J g inverse. If mu_j has lower-left zero,
its unique fixed point is infinity, hence g also fixes infinity.
In a torsion-free discrete projective group containing J, every
upper triangular word has diagonal ratio one. Otherwise suitable
conjugates of J, or their commutators with J, tend nontrivially
to the identity; a nontrivial finite-order ratio gives projective
torsion. This is the elementary discreteness argument already
proved in the Fourier framing theorem. Such a g commutes with J.

Put U=mu_i. It is nontrivial trace-two unipotent, with c=U_21
nonzero, and has the unique form

    U=I+c[-beta;1] * (1,beta), beta=(U_22-1)/c.            (1)

The rows/columns in (1) have zero contraction, so this expression
retains determinant one and the actual meridian orientation.

## 2. Move it with a literal inverse pair, preserving every source factor

Use inverse Hurwitz moves

    (X,Y) -> (Y,YXY inverse).

Let P be the braid whose ACTION order is
sigma_(i-1) inverse,...,sigma_1 inverse. It moves U left unchanged
past the preceding J's. Insert the action words P then P inverse
before the original action word beta_braid. The matrix order is

    R_beta_braid R_P inverse R_P=R_beta_braid.             (2)

The second cut is the FIRST physical slot between P and P inverse.
At that level its developed meridian is exactly U; its physical
prefix products are therefore

    V=I, U=mu_i, prefix sign sigma=-1.                    (3)

The original first cut and its reference J are untouched. Closing
the second cut with its original identity gives (2). The first
output row, fixed-input source, all original pivotal caps and
full d_N(M) line remain the original ones. Strand number and
writhe are unchanged; the presentation acquires at most 2(b-1)
crossings, independently of N.

At an actual root use the genuine signed crossing matrices and
their inverses. For a whole auxiliary q-normal calculation use
the specified whole inverse matrices BEFORE specialization, so
(2) is still an exact matrix identity and preserves all its jets.
No inverse is obtained by first deleting a central norm factor.

The second cut is at slot ell=0. The EXACT open meridian insertion
therefore has no endpoint q^(-ell nu) character, by
[the actual horizontal transport theorem](actual_open_meridian_horizontal_source_transport.md).
Its Fourier dilation and scaled-frame correction are identity.
The original gamma_N, x=-M/q and full meridian ratio g_N are still
retained; their absence is not implied by ell=0.

## 3. The added crossings have a nonempty regular geometric chart

Use the actual complete framing matrix

    F(r,s)=[[r,1-r],[s,-s]], s nonzero, t=r+beta s.

For h preceding J's set

    a_h=ell_(J^h)=1+hs,
    b_h=ell_(U J^h)
       =a_h+(c/s)(1-t)(t+hs).                            (4)

One negative move carrying U left across J has actual physical
positions A,B and transfer C

    A=a_h/a_(h+1), B=a_(h+1)/b_(h+1),
    C=a_(h+1)b_h/[b_(h+1)a_h].                          (5)

Its five balanced coefficient atoms at completeness are

    A, C, 1/B, AC, C/B
      =a_h/a_(h+1), C, b_(h+1)/a_(h+1),
                        b_h/b_(h+1), b_h/a_h.            (6)

All are different from zero and one on a NONEMPTY Zariski open.
For an explicit proof, in addition to their denominator factors
exclude

    1-t, t+hs, t+(h+1)s, s+c(1-t).

The differences from one in (6) have these nonzero factors, and

    C-1=-c(1-t)^2/[b_(h+1)a_h].                          (7)

Every displayed factor is a nonzero rational function because
c is nonzero. The finite intersection over h=0,...,i-2 is
nonempty over the infinite marked representation field. It also
intersects any existing nonempty regular framing open for the
original word.

Reversing a move has A'=B/C,B'=AC,C'=1/C. Its positive atoms are

    AC, 1/C, C/B, A, 1/B,

so the inverse path introduces no new nondegeneracy condition.
This verifies admissibility of the ACTUAL new crossings rather
than assuming that an arbitrary identity insertion is regular.

On this common open the added critical equations are the actual
crossing graph followed by its inverse. Intermediate states
eliminate uniquely over local Artin rings; the marked critical
scheme is the original one. Thus its two framing tangent modes
and regular Morse--Bott property are unchanged. Equivalently,
each inverse pair is a generating-family stabilization: in regular
input/output position coordinates its added normal block has
form [[0,mu],[mu,*]] with mu a unit. Its determinant is -mu^2.
The explicit local mixed coefficients are C/(1-C) for the
negative move and 1/(1-C') for its positive inverse, C'=1/C;
they are negatives of each other and are units on (6).
The original nonzero normal Gaussian therefore persists. Fourier
polarizing the new cut removes the remaining framing mode as
in the proved bordered-Hessian theorem.

This proves persistence, not equality of every old and new formal
coefficient in arbitrary Gaussian frames. The marked fundamental
cycle/action calibration remains the same, since the actual inverse
path adds a cancelling relative cycle. All Gaussian phases and
source lines must still be transported.

## 4. The complete momentum and leading density are universal

Direct conjugation of (1) gives

    F inverse U F
      =I+(c/s)[1-t;-t] * (t,1-t).

Its first diagonal is k=1+(c/s)t(1-t). With the ACTUAL slot-one
prefix sign -1, the balanced momentum is

    p=-[(F inverse U F)_12]/(k-1)
      =1-1/t,
    r=1/(1-p)-beta s.                                   (8)

Consequently (A_cut,p), A_cut=1/(1+s), are birational framing
coordinates, with partial_r p=1/t^2 nonzero. No new quadratic
framing cover or arbitrary change of the finite band source is
introduced. The actual Fourier stationary incidence is xi=p inverse
because this second cut has ell=0.

The original geometric framing density is exactly

    Omega_cut=-dr wedge ds/[s(1+s)]
             =-p/[s(1-p)^2] dlog A_cut wedge dlog p.       (9)

Its only principal-density momentum pole is p=1, corresponding
to r=infinity. At a root that point belongs to EVERY finite
Fourier grid. This theorem is on the COMPLETE M=1 fiber; it
does not assert a single generic-M double-pole model or freeze
its normal splitting.

## 5. What has become universal, and what is still missing

For the principal rational coefficient alone, the regular nodes
p=Q_N^j, j=1,...,N-1, have the exact sum

    sum_(j=1)^(N-1) -Q_N^j/[s(1-Q_N^j)^2]
                         =(N^2-1)/(12s).                (10)

This is the elementary inverse-sine-square identity already used
in the source-current norm proof. It is NOT the original period:
the omitted node p=1 is a pole of this coefficient, while the
actual finite tensor and its raw Fourier array are regular.
No principal sampling is justified at that node, and the local
Gaussian expansion is not uniform near it. Higher coefficients
and the full source can retain other shape-chart exclusions.

Equation (8) specifies the escaping scale explicitly. If
p=1-zeta/N, then

    r=N/zeta-beta s.                                    (11)

The fixed-label nodes near zero therefore leave every fixed
compact framing chart as N grows. A fixed-r formal expansion
cannot decide their selected contribution. The full quantum
boundary layer, together with its actual word and current terms,
must be retained. Equation (10) provides neither its missing
value nor a no-cancellation theorem.

More strongly, the exact actual localization just cited says the
regular-node contribution of the ORIGINAL array is zero, even
though the sum of this isolated PRINCIPAL coefficient is (10).
That principal sum is therefore not a bulk approximation to the
actual complete array. The geometric formal block can be nonzero
while its exact regular-node source value vanishes.

The critical-path gain is concrete: an actual source-preserving
presentation now removes the prefix-dependent leading pole and
the port meridian half-step for ANY complete discrete-faithful
knot representation on its regular geometric branch. The chosen
leading pole is the single fixed resonance p=1. This supplies a
uniform location and scale for the next source comparison.
It does not by itself reduce all remaining shape/global issues
to a knot-independent cap or prove gate C, D or E of
[the critical-path audit](critical_path_to_original_volume_conjecture.md).

[Exact source, atom and normal-Hessian tests](../experiments/audit_universal_resonant_cut.py)
and [saved results](../experiments/universal_resonant_cut_results.json)
support the direct proof. The
[independent proof audit](universal_resonant_cut_independent_audit.md)
checks the actual placement, admissible chart, prefix momentum
and scope of the normal-block persistence.
The separate [word/source audit](universal_resonant_cut_word_audit.md)
also records the explicit mixed-Hessian stabilization and a
carefully scoped meridian-germ calculation with its split poles.
