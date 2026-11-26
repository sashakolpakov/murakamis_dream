# Bounded outward pilot for the new own-four left cutoff

This is an incomplete pilot, not a complete source certificate. It
tests only the face circle-three times disk-four, for an own-four
ordinary block. Both conditional orientations must pass on every
accepted leaf. The other five faces/families have not been run.
The fixed limit is 511 visited nodes or 60 seconds. The saved run
accepted 250 leaves and left 12 parameter boxes pending.

The parameter cube is (theta,rho,phi) in [0,1]^3:

    A = c3 + r3 exp(2 pi i theta),
    C = c4 + rho r4 exp(2 pi i phi).

The derivative of A is 2 pi i(A-c3) in theta. Those of C
are r4 exp(2 pi i phi) in rho and 2 pi i(C-c4) in phi.
This includes the full disk and its center; repeated polar images
cause no missing parameters.

Every accepted cell reuses the original two-complex-input affine
root witness, original-log self-map test, midpoint lift and Neumann
response bounds. No old four-dimensional root cover is rerun.
Floating roots and scalar stationary points propose witnesses and
trial targets only; they do not decide acceptance.

## Target concavity at the new cut

For ell=1/8, let f(x)=Re[g(ell+x+ih)-lambda*g(x+ih)],
where lambda>=1, x in [.22,.45], and |h|<=.12.
Put C=cos(pi ell), S=sin(pi ell), K=cosh(2 pi h),
and T=cos(2 pi x+pi ell). Then -1<=T<=0, and

    Re[cot(pi(x+ih))-cot(pi(x+ell+ih))]
      = 2S(C-KT)/(T^2-2CKT+C^2+K^2-1)
      >= 2S/(C+K).

After multiplication by the positive denominators, the last
comparison is (1+T)[1-T-K(K-C)]>=0. It follows from
C>9/10, K<4/3 and T<=0. The exact half-angle values give
S>3/8 and C<15/16. Hence

    -f''(x) > 36 pi/109 > 1,

using pi>157/50. The allocated extra halfweight only increases
this curvature, since Re cot(pi(x+ih))>0.

## Whole-cell acceptance inequality

Let Z=U+iH=(a,b) denote the correlated retained arguments, phi
the original allocated conditional critical phase, P=phi', and
Hphi=phi''. Keep kappa=1/2500000. For a fixed rational trial
target Xhat, define

    D = Re F(ell; Xhat+iH) - Re phi(Z)
        - Re P dot (Xhat-U) + kappa |Xhat-U|^2.

The exact reference derivatives are

    D_U = (-Re Hphi - 2 kappa I)(Xhat-U),
    D_H = Im[P - F'_cut + Hphi(Xhat-U)].

The code obtains Hphi by the full complex Schur complement
F_XX-F_Xs F_sX/F_ss. It chains these two real derivatives
through the original interval response of (s,t) to (A,C).
The midpoint value uses the tiny original-log root disk; a
three-parameter mean-value bound covers the entire reference cell.

The target slope at Xhat is

    beta = Re F'_cut - Re P + 2 kappa(Xhat-U).

The target curvature is at most -(1-2 kappa). The code therefore
adds the exact clipped quadratic gain in each target coordinate,
using the whole-cell interval for beta and the full target interval
[.22,.45]. Stable one-sided endpoint optimizers have zero gain.
No target grid is used.

An accepted leaf has the sum of midpoint upper value, reference
mean-value allowance and both target gains strictly below zero
in BOTH conditional orientations. Unaccepted cells are subdivided
or remain explicitly pending at the resource limit.

The boundary-reference lemma could propagate a completed boundary
bound to the auxiliary input product. This pilot does not complete
even its one face, so it supplies no such conclusion. Auxiliary
Fourier allocations remain formal where a type-four input has
positive height; a physical conclusion would retain the actual
unselected reference-height hypotheses.
