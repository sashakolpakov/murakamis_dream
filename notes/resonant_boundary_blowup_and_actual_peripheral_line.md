# The resonant framing blowup and the actual peripheral line

27 October 2026. This note proves exact identities on the geometric
framing chart of the original first-slot inverse-pair cut. The full
ADO dimension cancels the chart's apparent first-order pole before
specialization. The paired principal Gaussian line also extends.
Neither statement constructs the required map from the actual finite
source to a selected geometric period.

One correction matters: the generic physical inverse-pair atom is
`AC=M*b_h/b_(h+1)`. Its first boundary coefficient is `s*zeta`.
The coefficient `s*zeta+a/2` belongs to the RAW prefix quotient
`b_h/b_(h+1)`, which omits its physical factor M. Those expressions
cannot be substituted for each other in a quantum-product boundary
calculation.

## 1. Work on a geometric formal branch, before imposing level N

Let R be a characteristic-zero formal discrete valuation ring with
uniformizer epsilon, containing the marked geometric coefficients.
Fix a meridian deformation with

    kappa=M-M^(-1)=epsilon*a,  M(0)=1,
    p=1-epsilon*zeta,
    d=1-kappa*beta,
    t=r+beta*s=d/(epsilon*zeta).

Here M is the unique formal root near one of M-M inverse=epsilon*a.
The coefficients c,beta,s may vary regularly with epsilon; c and s
are units at zero. All leading formulas below use their values at
epsilon=0. We work where zeta and s*zeta+a are units. These are
classical geometric coordinates, not a newly chosen finite source.

The actual generic-M first-slot matrices, as fixed in
[the checked meridian-germ appendix](universal_resonant_cut_word_audit.md),
are

    F=[[r,1-r],[s,-kappa-s]],
    U=[[M-c*beta,kappa*beta-c*beta^2],
                         [c,M^(-1)+c*beta]].

Set Delta=s+kappa*r. Exact substitution gives

    Delta=d*(s*zeta+a)/zeta.                         (1)

In particular Delta is a unit on this chart, despite r having
valuation minus one. Direct conjugation gives, for k=(F inverse U F)_11,

    k=M^(-1)+a*(epsilon*a+s)/(s*zeta+a)
              -c*d*p/[epsilon^2*zeta*(s*zeta+a)].    (2)

For completeness, U-M inverse I is the rank-one product

    [kappa-c*beta;c]*(1,beta).

Its conjugated (1,1) entry is

    [kappa*(kappa+s)+c*(d-t)]*t/Delta,

which proves (2), without discarding any meridian term. The actual
physical momentum is still

    -(F inverse U F)_12/(k-M^(-1))=p.

The SECOND balanced physical position, denoted A_e to distinguish
it from the reference cut coordinate A_cut, is

    A_e=M/k,
    epsilon^(-2)*A_e -> -zeta*(s*zeta+a)/c.          (3)

Thus its valuation is two on this unit chart. The reference coordinate
remains A_cut=M/(M+s); the two coordinates must not be conflated.

## 2. The framing lattice extends although the scalar clock escapes

The matrix F has determinant -Delta, a unit, and at least one entry
of valuation minus one. Over R its Smith exponents are therefore
(-1,+1). Equivalently

    Lambda=F^(-1)R^2

is a free rank-two lattice inside the framed representation space.
For a geometric representation defined over R, every conjugated
holonomy F inverse rho(g) F preserves Lambda. Also

    F*(1,1)^t=(1,-kappa)^t,

so the marked inverse flag remains primitive. This proves flatness
of the underlying geometric representation lattice, not a comparison
with a quantum source lattice.

There is a useful precise restriction on that comparison. The actual
finite second position operator has relation B_e^N=1 on the complete
root fiber. A multiplicative scalar specialization carrying B_e to
the geometric A_e in (3) cannot preserve that relation: A_e^N has
valuation 2N, whereas 1 has valuation zero. Multiplication by a unit
does not change this discrepancy. Dividing A_e by epsilon squared
changes the N-th-power relation by epsilon^(2N), which is precisely
a factor that must be accounted for, rather than a harmless unit
gauge.

This excludes a regular scalar-clock substitution with the original
norm relation. It does not exclude a linear period transform, a
singular change of lattice with its determinant retained, or an
irregular/nonlocal source comparison. Such a construction would
still need to carry the actual word and selected source.

## 3. The actual dimension cancels the framing-form pole exactly

At fixed M the invariant form already specified by the marked
centralizer calculation is

    Omega_cut=-dr wedge ds/[Delta*(M+s)].

Treat epsilon and a as base parameters. Using (1) and
dlog A_cut=-ds/(M+s), its exact expression is

    epsilon*Omega_cut
      =dlog A_cut wedge dzeta/[zeta*(s*zeta+a)].      (4)

This is an algebraic identity, not a claim about a selected integration
cycle or a uniform Gaussian expansion.

Now retain the original dimension line, including its phase:

    d_N(M)=eta_N/u_N(M),  eta_N=i^(N+3),
    u_N(M)=(M^N-M^(-N))/(M-M^(-1)).

The quotient u_N is a Laurent polynomial with u_N(1)=N. With
B=M^N its exact fraction-field expression is

    d_N/eta_N=kappa*B/(B^2-1).

Consequently, before any limiting argument,

    (d_N/eta_N)*Omega_cut
      =a*B/(B^2-1)
           *dlog A_cut wedge dzeta/[zeta*(s*zeta+a)]. (5)

The epsilon inverse pole in (4) cancels against the original
peripheral line. The factor B squared minus one remains in (5).
It cannot be deleted at a torsion value or used to replace the
whole regular lattice by two separately undefined quotients.
At M=1 the original polynomial formula gives d_N/eta_N=1/N.

On the physical power graph epsilon=1/N and fixed a, the branch is

    M_N=exp(asinh(a/(2N))),
    B_N=exp(N*asinh(a/(2N))) -> exp(a/2).

Thus the scalar in (5) tends to a/[2*sinh(a/2)] away from its
remaining norm divisor. At a=0 its regular continuation is one,
in agreement with the exact value (1/N)/epsilon=1. This verifies
the peripheral normalization at this boundary. It does not identify
the rest of a geometric density with the original quantum period.

## 4. Physical inverse-pair atoms and the first-order correction

Let mu_M=[[M,1],[0,M inverse]] and

    u_h=(M^h-M^(-h))/kappa,
    a_h=(F inverse mu_M^h F)_11=M^h+s*u_h,
    b_h=(F inverse U*mu_M^h F)_11.

The power identity gives (mu_M^h)'_21=s*u_h in the framed chart.
Since U'_12=-p*(k-M inverse), we get the exact formula

    b_h=k*[M^h+(1-p)*s*u_h]+p*M^(-1)*s*u_h.         (6)

For the negative move carrying U left across the next reference
meridian, the actual physical dictionary A_j=M*ell_previous/ell_next
gives

    A=M*a_h/a_(h+1),
    B=M*a_(h+1)/b_(h+1),
    C=a_(h+1)*b_h/[b_(h+1)*a_h],
    AC=M*b_h/b_(h+1).                              (7)

This is the generic-M extension of the complete formulas; the factors
M in A,B and AC are forced by the signed Gauss/position dictionary.
At the boundary M=1+epsilon*a/2+O(epsilon squared) and
u_h=h+O(epsilon squared). Equation (2) has common leading coefficient
`-c/[zeta*(s*zeta+a)]` at order epsilon minus two. From (6),

    b_h/b_(h+1)=1-epsilon*(s*zeta+a/2)+O(epsilon^2),
    AC=1-epsilon*s*zeta+O(epsilon^2).                (8)

The physical atom therefore has no additional a/2 term. Keeping
only the raw prefix ratio would introduce a false half-shift into
a proposed product or Gamma-profile normalization. No such quantum
profile is established in this note.

At completeness the five negative coefficient atoms
A,C,1/B,AC,C/B have valuations (0,0,-2,0,-2). The same valuations
hold on this generic blowup chart when their leading coefficients
are units. The atom AC approaches one at order epsilon. Consequently
the ordinary fixed-atom Gaussian expansion is not uniform here,
even though the inverse-pair principal normal line below is regular.

## 5. The paired principal normal ratio extends

The squared PRINCIPAL variable amplitudes from the actual balanced
coefficients, with Y=M squared and all fixed phases retained separately,
are

    a_-^2=C/(AB)*(1-AC)*(1-Y/B)
                         /[(1-A)*(1-C)*(1-YC/B)],
    a_+^2=AB*(1-BC)*(1-Y/A)
                         /[(1-B)*(1-C)*(1-YC/A)].

The inverse move uses (A',B',C')=(B/C,AC,1/C). Direct cancellation,
valid before putting Y=1, proves

    a_-^2(A,B,C)*a_+^2(A',B',C')=-C^2/(1-C)^2.      (9)

The mixed Hessians are V_-=C/(1-C) and
V_+(1/C)=-V_-. The added normal Hessian has determinant -V_- squared.
Thus its squared principal amplitude divided by that determinant
is EXACTLY one. On the unit chart C tends to A(0) inverse and
V_- tends to 1/[A(0)-1], a unit. The inverse-pair PRINCIPAL normal
line extends through this blowup after pairing.

This does not say that the individual amplitudes, all higher
coefficients, the open source, or the full quantum normal lattice
extend in this Gaussian frame. Equation (8) explicitly shows an
atom colliding with one. An all-order completed source transform
would have to control that collision with its actual word data.

## 6. Critical-path implication and exact checks

The actual full dimension supplies the precise first peripheral
pole cancellation; no extra numerical normalization is available
to choose here. The inverse-pair principal determinant also causes
no additional unknown scalar. What remains is a source-compatible
linear/irregular geometric period map at the resonance, proving
that the original selected class has a nonzero geometric image,
with subexponential coefficient and a sharp global norm estimate.
The displayed cancellations do not prove those three assertions.

[The symbolic audit](../experiments/audit_resonant_boundary_blowup.py)
checks the raw conjugation, the whole dimension/form identity,
the physical-versus-raw first-order correction, the generic inverse
principal-amplitude identity, and the dimension polynomial through
level twelve. Its [saved output](../experiments/resonant_boundary_blowup_results.json)
is a verification of these identities, not evidence of a volume
limit or a finite-source/geometric identification.
