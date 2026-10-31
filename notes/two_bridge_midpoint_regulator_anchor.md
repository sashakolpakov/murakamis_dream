# A zero regulator anchor for every two-bridge component

28 October 2026. For every two-bridge knot, all SL2(C) representations
with meridian eigenvalue M=+i or -i have finite projective image and
marked representation volume zero. The nonabelian character branches
have finite limits there. Consequently the macroscopic source point
x=1/2, M=-exp(pi i x), supplies a common ZERO geometric anchor for
every genuine peripheral component of this class.

This proves a geometric input for the whole-source transport problem.
It does not identify an actual quantum operator with the peripheral
curve or estimate its branch conversion.

## 1. The group relation forces a finite image

Use a two-bridge presentation, p=2m+1 odd,

    G=<a,b | a w=w b>,
    w=b^(epsilon_1)a^(epsilon_2)...
                         b^(epsilon_(2m-1))a^(epsilon_(2m)),
    epsilon_j in {+1,-1}.                           (1)

The generators are the two bridge meridians; the signs encode the
rational tangle. The argument below works for every sign word of this
form which presents the knot, so it does not require a restriction on
continued-fraction length or twist parameters.

If rho(a) has eigenvalues i,-i, Cayley-Hamilton gives rho(a)^2=-I.
The same is true of rho(b), since meridians are conjugate. In PSL2(C),
write their images as A,B. Then A²=B²=1, and every sign in w disappears:

    A(BA)^m=(BA)^m B.                               (2)

Set R=AB. Since BA=R^-1 and A R A=R^-1, (2) becomes

    R^m A=R^(-(m+1))A, hence R^p=1.                (3)

Every word in A,B reduces to R^j or R^j A. Thus the projective image
has at most 2p elements. Its inverse image in SL2(C) has at most 4p
elements. This applies to reducible representations as well as
irreducible ones, and uses no unitarity assumption.

The image is metabelian: its subgroup above <R> is cyclic (R^p=+/-I
in a lift), and its commutator subgroup lies there. The preferred knot
longitude lies in G'': choose a Seifert surface and express its boundary
as a product of commutators of surface generators. Their push-offs have
zero linking number with the knot, so each generator lies in G'. Hence

    rho(longitude)=I.                               (4)

In particular all these midpoint peripheral points have L=1 in the
original preferred-longitude eigenvalue convention. A changed framing
must retain its meridian correction rather than reuse (4) unchanged.

## 2. The ABSOLUTE representation volume is zero

A finite group of hyperbolic isometries fixes a point c in H3. One
elementary construction is to sum its orbit of a future unit timelike
vector in the hyperboloid model and normalize that timelike sum.

Use the constant equivariant map c on a truncated core. On each cusp,
choose a peripheral fixed ideal point xi and extend along the ray from
c to xi, depending only on the cusp height. The ray is peripheral
invariant because both endpoints are fixed. These choices extend
equivariantly to all lifted cusps. Every cusp and its interpolating
collar have rank at most one; the core has rank zero. The pullback of
the hyperbolic volume form therefore vanishes everywhere.

By the independently proved choice-independence of the
[general peripheral volume](general_peripheral_representation_volume_bound.md),
this is the SAME absolutely marked regulator used by the Bloch chain:

    R(rho)=Vol(rho)=0.                              (5)

No additive shift of a primitive is used to arrange (5).

## 3. No character branch escapes at this meridian

For an irreducible pair with M!=+/-1, put

    A_M=[M,1;0,M^-1], B_(M,z)=[M,0;-z,M^-1].        (6)

To justify this form, choose the M-eigenline of the first meridian
and the M^-1-eigenline of the second as the two coordinate lines.
If they coincide the pair is reducible. Otherwise the first upper
off-diagonal entry is nonzero for an irreducible pair and may be
normalized to one. The remaining entry defines z.

Let W be the word in (1). The top-right entry of A_M W-W B_(M,z) is

    P(M,z)=W_22+(M-M^-1)W_12.                      (7)

It is a polynomial in z of degree m, with leading coefficient

    (-1)^m product_(j=1)^(2m) epsilon_j in {+1,-1}. (8)

Here is a direct leading-term proof. Each pair B^epsilon A^delta has
z-leading matrix -epsilon e_2 (M^delta,delta). Multiplying these
rank-one matrices shows that W_22 has the coefficient (8), while
W_12 has degree at most m-1. This proves (8), independently of M.

Every actual irreducible representation satisfies P=0. On a compact
M-neighborhood of +i or -i, the other coefficients are bounded Laurent
polynomials in M. The elementary monic polynomial root bound then
bounds z uniformly. Thus the matrices (6) have convergent subsequences
at the midpoint and their limits still satisfy the full group relation.
Their limits are the finite-image representations of Section 1.

There is a stronger local check. At M=i, inverse meridians differ from
positive meridians by -I, so W is a sign times (BA)^m. Put
t=tr(AB)=-2-z and define U_0=1, U_1=t, U_(r+1)=t U_r-U_(r-1).
Equation (7) becomes, up to that same sign,

    P(i,z)=U_m(t)-U_(m-1)(t).                      (9)

The identity follows from the determinant-one matrix recurrence for
BA, or directly from P_0=1, P_1=t-1. Its m roots are distinct:

    t=2 cos((2j-1)pi/p), j=1,...,m.                (10)

Indeed U_m(2cos theta)-U_(m-1)(2cos theta)
=cos(p theta/2)/cos(theta/2), with endpoint values obtained by limits.
This also follows from the finite sine-sum formula for U_m.
At M=-i one obtains the same roots, since replacing M by -M negates
both meridian matrices after a constant diagonal conjugation.

Thus each actual local branch through the midpoint has an ordinary
finite analytic representative (possibly after taking its character
normalization), not an escaping Riley parameter. The monic equation
is finite over C[M,M^-1]; every one-dimensional nonvertical component
of the actual relation locus reaches M=i and M=-i. More explicitly,
a dominating irreducible component is closed in this finite scheme,
so its image is a closed dense subset of C*, hence all of C*.
No assertion about a vertical component is needed for a meridian
transport curve.

The volume is continuous at these limits. One can check this without
assuming cross-ratios stay nondegenerate: M remains away from +/-1,
so the peripheral eigenlines and axis vary continuously on each local
branch. Choose the axis cusp maps continuously; their volume forms
vanish on the cusp. The equivariant interpolation over the fixed finite
compact core varies continuously, so its finite volume integral does
too. Hence every such branch has limiting marked regulator zero.
Reducible representations have zero regulator throughout and cause
no additional endpoint case.

## 4. Consequence for COMPLEX conversion paths

Combine (5) and the finite-limit statement with the
[complex peripheral action identity](complex_peripheral_action_and_conversion_bound.md).
For any path which genuinely lifts to a connected representation/Bloch
curve, starts at this midpoint and ends at unit meridian,

    |Im integral Log(L) dLog(M²)| <= Vol(S³ minus K). (11)

Ramification points on the normalized lifted curve are allowed.
For the quantum step h=2pi i/N, the corresponding exponential action
has growth at most Vol/(2pi). This controls all such lifted paths for
the entire hyperbolic two-bridge class, rather than selected twist
examples. It does NOT prove that every contribution of the original
quantum recurrence admits this path description, nor that the number
and prefactors of those contributions are subexponential. Those are
the remaining analytic/source requirements.

## 5. Coverage and checks

The trace-free slice and binary-dihedral representations are established
subjects; coverage includes [Nagasato--Yamaguchi](https://arxiv.org/abs/0807.0714).
No proof from that source is used here. The group reduction, monic
matrix calculation, finite limit and zero-volume argument are supplied
above; no novelty is claimed for the representation classification.

[Audit](../experiments/audit_two_bridge_midpoint_anchor.py) checks the
generic leading coefficients, actual two-bridge sign words, the
trace-free polynomial recurrence, and the exact finite-order relation.

The finite audit checks 84 generic sign words and 41 two-bridge midpoint sign words, including simple roots and the exact finite-order relation.