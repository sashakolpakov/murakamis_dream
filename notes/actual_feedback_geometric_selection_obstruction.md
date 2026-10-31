# Exact Gaussian stabilization preserves the unresolved geometric source

28 October 2026. The finite Fourier kernel in the actual clock-feedback
theorem has a nonzero coefficient with normalization exactly one. Its
Jacobian and transverse determinant can be computed without assumptions
about a geometric saddle. But it is an exact stabilization of the SAME
coupled action and the SAME original source. It does not supply the
missing geometric intersection number.

This answers a specific possible shortcut: Fourier-Gaussian ellipticity
does not turn the already known geometric normal block into a selected
global geometric contribution. No claim about the impossibility of a
different global contour construction is made.

## 1. The finite feedback extension splits exactly

Use the primitive variables and actual diagram matrix T of
[the feedback theorem](actual_clock_feedback_normal_form.md), not
independent physical spectator parameters. There are m crossings.
On a coefficient R^nu Y^h the normalized finite Fourier realization is

    N^(-m) sum_(eta,lambda in (Z/N)^m)
           Q^[-lambda dot eta+lambda dot h+nu^T T eta]. (1)

The clock h is the actual over-monotone clock; nu is the integer
primitive Laurent exponent. Every original closure, pivot, dimension,
framing and Cartan factor remains in its coefficient and its specified
charged source. Equation (1) is only the exact feedback kernel.

Make the finite change of variables

    eta=h+u, lambda=T^T nu+v,                         (2)

with all entries interpreted modulo N in this finite sum. For EVERY
integer nu,h and EVERY diagram T, this is a bijection, and its exponent
is exactly

    -lambda eta+lambda h+nu^T T eta
                  =nu^T T h-v dot u mod N.            (3)

Thus (1) is

    Q^(nu^T T h) * N^(-m) sum_(u,v)Q^(-v dot u)
                  =Q^(nu^T T h).                     (4)

For each fixed u the v sum is N^m if u=0 and zero otherwise.
The extra Gaussian therefore has coefficient ONE, at every N, with
no determinant character, unknown periodic unit or knot normalization.

This statement survives the original source pairing, including the
contracted closure jets. Indeed the change (2) does not change nu or h,
and (4) holds coefficientwise before any anchor substitution, charged
coefficient, clock sum or external scalar. Hence those operations commute
with eliminating this normalized Gaussian. No source division is used.

It is important that the shifts in (2) depend on the coefficient
momenta nu,h. They describe a canonical Fourier stabilization, not a
single substitution of the physical spectator coordinates. They cannot
be used to replace the coupled action by the zero-feedback action.

## 2. Exact Jacobian and Hessian comparison

The same fact has a precise local stationary interpretation. Let x be
any regular local phase coordinates, with scaled momenta nu(x),h(x).
Write alpha=2*pi*i and let S_0(x) be the independent coefficient action.
The extended action is

    S_ext(x,eta,lambda)=S_0(x)
               +alpha[lambda(h(x)-eta)+nu(x)^T T eta]. (5)

Use the local change

    eta=h(x)+u, lambda=T^T nu(x)+v.                    (6)

Its full Jacobian, including x, is block triangular with identity on
the diagonal, so its determinant is EXACTLY one. There is the exact
identity of functions, not just of quadratic terms,

    S_ext=S_act(x)-alpha v dot u,
    S_act=S_0+alpha nu(x)^T T h(x).                    (7)

Consequently the critical scheme is the product of that of S_act
with u=v=0, including multiplicities and local Artin rings. At a
critical point the Hessian is congruent to

    Hess(S_act) direct_sum [[0,-alpha I],[-alpha I,0]]. (8)

Thus

    nullity Hess(S_ext)=nullity Hess(S_act),
    det Hess(S_ext)=(-1)^m alpha^(2m)det Hess(S_act)     (9)

when the determinants are defined in the full coordinates. The same
formula applies to nondegenerate transverse slices in a Morse--Bott
germ, with the original radical retained. The normalized Fourier
half-density has the exact coefficient (4), so this auxiliary block
changes no selected transverse amplitude or residual source density.

Equations (5)-(9) are used only when a regular coefficient phase is
available. They do not assert uniform asymptotics across a finite
window, an endpoint, or a singular Fourier chart. Equation (4) itself
has none of those restrictions.

## 3. The complete geometric fixed set is not isolated by this operation

There is a concrete obstruction to applying an isolated-fixed-point
Bethe/Lefschetz formula after merely adding this feedback kernel.
For the actual marked knot critical scheme, simultaneous conjugation
by B_1=Stab_(PGL_2)(1) preserves the chosen inverse cut flag and all
closed braid equations. This group has dimension two. At the complete
discrete-faithful representation its projective centralizer is trivial,
so its orbit is a smooth two-dimensional family of distinct marked
critical points.

This is exactly the framing torsor in
[the actual geometric normal theorem](actual_geometric_normal_period.md),
whose Hessian has that two-dimensional radical. In particular, for
the regular marked Hurwitz return map Phi, its infinitesimal conjugation
vectors obey D Phi(v)=v. Therefore det(I-D Phi)=0 before a stated
framing reduction. Adding (1) does not repair that determinant: (7)
preserves the critical germ and (8) preserves its radical.

One may choose a transverse framing section and obtain the already
proved nonzero normal Gaussian block. Its two-form must still be
paired with the specified original relative source. Taking an arbitrary
section or assigning its relative period the value one would add a
source selection, rather than derive it from (4).

The new closure contractions in
[general flow fusion](actual_general_flow_fusion.md) do retain the
original source exactly. Their full length-d block is the reproducing
kernel of the finite source algebra: contraction through an arbitrary
exterior implements substitution modulo the original nilpotent walls.
It is an identity on the transmitted finite state space, with pivots
retained. It supplies no additional framing section or condition on
the geometric relative period. At a regular phase realization it
removes identity-wire coordinates, not the conjugation orbit above.

## 4. Exact consequence for the critical path

There is no unknown Gaussian normalization left in this part of the
comparison. If a source-preserving regular phase comparison with the
geometric chart is constructed, its feedback stabilization contributes
one and leaves its geometric coefficient unchanged. This is useful
normalization control.

But the full source coefficient which would have to be shown nonzero
is still the original one. Neither invertibility of G_T, its unit
coefficient norm, the perfect socle pairing, nor the nonzero transverse
determinant computes that coefficient. The precise unproved step is
the image of the original relative class in the action-normalized
geometric summand after the remaining framing/charge contraction.
The Gaussian (1) does not weaken that step, since (4) eliminates it
without changing that class.

This result therefore rules out the proposed inference from a nonzero
Fourier-Gaussian fiber to whole-source geometric survival. It is not
a volume-conjecture proof, a new sharp scalar bound, or an assertion
that a global positive contour cannot exist.

## 5. Reproducible audit

[audit_actual_feedback_geometric_selection.py](../experiments/audit_actual_feedback_geometric_selection.py)
checks (3)-(4) with actual diagram T rows, both crossing signs and
arbitrary primitive exponent signs; compares the stabilized complete
source with original pivotal signed matrices; and verifies the full
Jacobian, stationary Hessian congruence, determinant and lifted framing
radical on an explicit nonlinear regular phase germ. The finite
identities and general proofs above are not inferred from the tests.
