# Which custom definitions can agree with the literature construction?

Research note, 25 October 2026. The earlier custom candidates are preserved in
`quantum_a_volume.md`. They have different answers to the equivalence question.
The exact comparison below keeps q and the peripheral variable Q generic.

**Subsequent target clarification.** Kashaev's original invariant is the
target; the AK/Faddeev constructions discussed below are comparison
objects. The [crossing proof](kashaev_crossing_and_period_lattice.md) and
[ADO pointing proof](kashaev_ado_pointing.md) now fix the original enhanced
state and its meridian normalization independently of published comparison
proofs.

The exact triangular Kashaev crossing has, with k=a-c and d=b+k,

    |A_(c,d;a,b)|=s_N(a)s_N(b+k)
                       /(s_N(a-k)s_N(b)s_N(k)).

Thus the positive sine factorials occur in the actual literature kernel.
Its phase, pairing, and modified-dimension lattice are also specified in
those notes. This is a direct local connection with the earlier positive
candidate. Equality of the full positive sum and the complex Kashaev
period has not been established.

## 0. Current comparison after reviewing the notes

The custom constructions are not a single definition. Their status is:

| Construction | Comparison with the specified literature object | Useful result |
| --- | --- | --- |
| Compact local product Psi_q | Exactly the numerator factor of Faddeev Phi; its modular-dual completion is exactly Phi | A local definition that can be retained with its full completion |
| Positive sine-factorial sum | No exact generic-boundary state equivalence established | An independently proved volume rate and a positive comparison action |
| Naive figure-eight cone-transfer recurrence | No rational two-component gauge, even after a finite power cover of the peripheral coordinate | A classical-action/volume model with a different quantum deformation |
| Minimal annihilator of the fixed Faddeev state | Uses the literature annihilator convention; existence is proved independently in the b-shift algebra | A way to formulate the volume law for the same state and operator |
| Inverse Fourier transform of the normalized charged tensor | Exactly recovers the preceding meridian state in ordinary charts and extends it to a moving longitude plane | A tensor-derived state and volume theorem for every globally branched complete positive geometric chart |

For the last row, `general_annihilator_and_volume.md` supplies the existence
and geometric-component arguments. The uniform twist geometry and the
subsequent `twist_topology_and_peripherals.md` now supply the explicit
twist-knot realizations and preferred peripheral certificates. The subsequent
phase and tetrahedral-symmetry audits prove selected-state equivalence along
certified proper positive paths, including the actual three-to-two-tetrahedron
figure-eight move. A general connecting-path theorem remains an obligation.
The further `six_three_and_two_bridge_audit.md` gives a complete independent
geometric and peripheral certificate for the specified 6_3 literature state.
The subsequent `singular_faces_and_six_two.md` evaluates singular face
contractions of the original charged operators, rather than changing the
tetrahedral function. It recovers an exact boundary fiber for 6_2 and proves
its volume law and minimal-annihilator existence. Thus a direct reduction
of the literature tensor is useful beyond the earlier invertible-face
formulation. It does not establish equivalence of the positive factorial sum.
The further boundary-state note proves the exact Gaussian change between a
rationally sheared peripheral coordinate and the true meridian. This is an
explicit equivalence for the stated tensor-derived states. It does not identify
the earlier naive cone-transfer state or the positive factorial state with them.
An operator by itself
does not select the solution or its exponential normalization.

The structural continuation in `pointed_steinberg_recoupling.md` now
gives an algebraic role for finite q-factorial ratios: they are the
kernel of a pointed cyclic-module factorization, with its generic
normalization unit determined. The cyclic dilogarithm frames live on
the explicit Heisenberg torsor of `heisenberg_period_torsor.md`.
This supplies a uniform comparison target for the positive factorial
candidate, retaining its phases. Equality of its full contracted period
with that target remains unproved.

The further `fourier_boundary_state.md` now removes the ordinary-fiber
rank restriction. Its definition uses the existing charged tensor and
real level, followed by a completely normalized inverse Fourier transform.
The quadratic level term makes its coordinate the actual meridian.
It agrees exactly with the preceding fiber/Gaussian state wherever that
state is defined. Rational geometry and matrix certificates for a
six-tetrahedron 5_2 realization verify the additional moving-plane case.
This is a useful reformulation of the literature tensor; it is not an
identification of either earlier positive state with it. Independence
of arbitrary triangulations and equality with a canonical intrinsic
knot state remain obligations.

## 1. The compact quantum product has an exact literature completion

Our local function was

    Psi_q(x)=(x;q)_infinity=product_(k>=0)(1-q^k x),  |q|<1.

It satisfies Psi_q(qx)=Psi_q(x)/(1-x), and the formal pentagon in the earlier
note. This function is directly related to the Faddeev function used in the
literature state; it is one of its two compact product factors.

More precisely, take Re b>0 and Im(b^2)>0, and put

    q=exp(2 pi i b^2),             q_tilde=exp(-2 pi i b^(-2)),
    X=exp(2 pi b Z),               X_tilde=exp(2 pi Z/b).

Then both |q| and |q_tilde| are less than one, and the exact identity is

    Phi_b(Z)
      = Psi_q(-q^(1/2) X)/Psi_q_tilde(-q_tilde^(1/2) X_tilde). (1.1)

This is equation (44) of Andersen–Kashaev,
[arXiv:1109.6295v2](https://arxiv.org/pdf/1109.6295v2), with its compact
product notation expanded and the square roots fixed by the displayed
exponentials. The following argument checks the identity instead of assuming
the source's proof.

**Independent verification.** Let P_b(Z) be the product quotient on the right.
The elementary shift equation for Psi gives

    P_b(Z-i b/2)=(1+exp(2 pi b Z)) P_b(Z+i b/2),
    P_b(Z-i/(2b))=(1+exp(2 pi Z/b)) P_b(Z+i/(2b)).

The factors in the other product cancel in each equation. The same two
equations were derived directly for Phi from its integral in Section 2.2 of
`literature_state_volume.md`. Their continuation to the present complex-b
domain follows by holomorphic dependence on b from a common initial strip.

The quotient R(Z)=Phi_b(Z)/P_b(Z) is therefore meromorphic and has periods
i b and i/b. They are linearly independent over the reals in the stated
complex-b domain. Both Phi_b and P_b tend to 1 as Re Z tends to minus infinity
on a fixed horizontal line in their initial strip. For Phi this follows by
moving the defining w-contour a small positive distance; for P it follows
from the absolutely convergent products.

A meromorphic function with two independent periods and this left-end limit
must be identically 1. To see this explicitly, the real translation flow on
the compact period torus is recurrent. There are R_k tending to plus infinity
whose classes tend to zero. At a regular point Z_0 of the initial strip,

    R(Z_0)=lim_k R(Z_0-R_k)=1.

The meromorphic identity theorem extends the result to the plane. This fixes
the normalization as well as the functional equations and proves (1.1).

For real b>0, neither compact infinite product is defined by an absolutely
convergent |q|<1 product. Their *completed quotient*, continued as the Faddeev
integral, has a well-defined value. Dropping the dual factor at this boundary
is not justified by (1.1). In particular, the compact pentagon by itself does
not establish the required global unit-circle state-integral identities.

**Usefulness.** The compact product was a useful local definition. Its precise
connection to a standard literature building block is now explicit. To obtain
the literature knot state one still needs its dual factor, Gaussian, measure,
boundary variables, and integration cycle. Equation (1.1) does not identify
our entire custom knot model with the standard one.

### 1.1 Exact local operator agreement does not determine the completion

Write the numerator in (1.1) as N_b(Z) and the denominator as D_b(Z).
The modular-dual variable is unchanged by Z->Z-i b, since
exp(2pi(Z-i b)/b)=exp(2pi Z/b). Hence

    D_b(Z-i b)=D_b(Z),
    N_b(Z-i b)=(1+q^(-1/2)exp(2pi b Z))N_b(Z).

The completed Phi_b=N_b/D_b satisfies exactly the same latter equation.
Thus the custom compact factor and the literature tetrahedron function
already agree at the level of this local quantum difference operator.
This is an exact partial equivalence, stronger than a shared classical
action. Their quotient is an i b-periodic function, generally nonrational
in the peripheral exponential.

The second, dual shift equation and the left-end normalization fix the
completion in Section 1. The first operator alone does not. The period
factor can depend on b and can affect a semiclassical limit on a prescribed
ray. This is a concrete reason that a volume conjecture must specify the
state and normalization together with its quantum A-operator. The formulas
here initially hold in the convergent complex-b product domain of (1.1);
the real-b state uses the completed continuation, not a bare divergent
product on the unit circle.

## 2. The positive angle-factorial model retains magnitudes of q-factorials

At q=exp(2 pi i/N), and 0<=k<N, the exact identity is

    (q;q)_k
       =(-i)^k exp(pi i k(k+1)/(2N)) s_N(k),
    s_N(k)=product_(j=1)^k 2 sin(pi j/N).                     (2.1)

It follows term by term from

    1-exp(2 pi i j/N)=-2 i exp(pi i j/N) sin(pi j/N).

Consequently

    1/s_N(k)=(-i)^k exp(pi i k(k+1)/(2N))/(q;q)_k.            (2.2)

The custom positive state can therefore be written with compact q-factorial
weights and an explicit compensating quadratic phase. This gives a concrete
starting point for a comparison with cyclic or root-of-unity quantum
dilogarithms. It does not say that discarding or compensating those phases
commutes with summation, elimination, or Pachner moves.

Its proven Laplace volume limit remains useful. It supplies a positive
comparison action whose maximum is the complete geometric volume. It does
not yet control the interference and contour of the literature state.

The specialized local ratio 8 is still only a comparison of bare amplitudes.
Products of peripheral units can specialize to 8. To decide the correct move
law one must lift the boundary variables, specify how they enter the state,
compute the exact multiplier, and check compositions of moves. No particular
generic multiplier is identified by the single numerical test. In particular
the test proves neither equivalence nor an obstruction modulo permitted
boundary factors.

### 2.1 The factor-eight test has a measure-scale asymptotic

There is more information available without inventing a peripheral extension.
For the same symmetric bipyramid, on the lattice progression 6|N, write

    L_N=s_N(N/3)^(-6),
    R_N=s_N(2N/3)^(-3)
          sum_(p=1)^(N/3-1) [s_N(p)s_N(N/3-p)]^(-3).

Then

    L_N/R_N ~ N.                                            (2.3)

Thus the discrepancy has a natural scale associated with the extra summation
variable. An explicit measure factor N would remove this leading discrepancy;
it would not establish the exact finite-N identity, since L_6/R_6=8.

Here is the calculation. Uniformly for x in compact subsets of (0,1) with
Nx integral, Stirling and Euler–Maclaurin applied after extracting the factor
2 pi j/N at the origin give

    s_N(Nx)=sqrt(2N sin(pi x))
                 exp(-N Lambda(pi x)/pi)(1+O(1/N)).

The two-tetrahedron expression therefore has leading form

    L_N ~ 3^(-3/2) N^(-3) exp(N V/pi),
    V=6 Lambda(pi/3).

For the three-tetrahedron sum let x=p/N. Its classical volume is

    v(x)=3[Lambda(2pi/3)+Lambda(pi x)+Lambda(pi(1/3-x))].

Its unique maximum is at x=1/6, where v=V and v''=-6 sqrt(3) pi^2.
At this point the product of the three tetrahedral prefactors is
3^(-3/4)N^(-9/2). Summing the Gaussian with spacing 1/N supplies
3^(-3/4)sqrt(N). The uniform logarithmic factorial bound in the earlier note
controls the endpoints, which have a strict volume gap. Consequently

    R_N ~ 3^(-3/2) N^(-4) exp(N V/pi),

proving (2.3). This identifies a missing leading measure scale, not a full
boundary multiplier or a proof of equivalence.

More generally a nonzero rational boundary factor regular near (q,M)=(1,1)
has zero contribution to a semiclassical limit h log|Z|. A finite-order zero
or pole also contributes zero when approached along a nonzero algebraic path,
since h log h tends to zero. The exact specialized state can still be zero or
undefined if the factors are canceled in the wrong order. Factors accumulated
in a number growing like 1/h can change the exponential rate. Exact move
invariance and invariance of the volume rate are separate statements.

### 2.2 How a generic boundary multiplier changes the operator

Let A=sum_j a_j(q,Q)E^j annihilate Z and let Z'=U(q,Q)Z, where U is a
nonzero rational peripheral factor and E Q=q Q E. Before any specialization,

    A'=U A U^(-1)
       =sum_j a_j(q,Q) U(q,Q)/U(q,q^j Q) E^j               (2.4)

annihilates Z'. Clearing denominators must be recorded, since it introduces
explicit peripheral factors. This is the precise scalar gauge law; replacing
U by its value at Q=1 before shifting would give the wrong equation.
For example, for U=1+Q^n the coefficient multiplier is

    (1+Q^n)/(1+q^(jn)Q^n).

Although U(q,1)=2, its generic shift ratios carry nonconstant information.
A product of three such factors can specialize to 8. This illustrates the
user's normalization point without claiming that these particular factors
are the missing multiplier in the bare bipyramid calculation.

For a fixed number of moves, a nonzero multiplier meromorphic of finite
order in a semiclassical parameter h has h log|U|->0 along any path on which
its leading nonzero term is c h^k. It preserves the volume rate on that
path. This statement requires the nonzero leading term: an identically
vanishing specialization cannot be assigned a logarithmic rate by it.
Nor does it apply to an exponential normalization exp(C/h). Generic
normalization, exact quantum equivalence and volume-rate equivalence
therefore remain distinct questions.

## 3. The naive cone-transfer equation is a different rational q-system

For the figure-eight knot put

    F(Q)=Q^4-Q^3-2Q^2-Q+1,
    t(Q)=F(Q)/Q^2,
    A_custom=E^2-t(Q)E+1,
    E Q=q Q E.

This is the earlier left-ordered cone-transfer equation, expressed in
Q=m^2 so that its commutation parameter agrees with the literature one.

For the literature operator audited in Section 4 of
`literature_state_volume.md`, divide by its leading coefficient and write

    A_lit=E^2-T(Q)E+d(Q),
    T(Q)=(q^2 Q^2-1) R(Q)/(q^2 Q^2(q Q^2-1)),
    R(Q)=q^4 Q^4-q^3 Q^3-q(q^2+1)Q^2-qQ+1,
    d(Q)=(q^3 Q^2-1)/(q Q^2-1).

The earlier scalar-gauge invariant already distinguishes these operators.
The following stronger statement also rules out a rational change of the
two-component solution basis, in these fixed peripheral coordinates.

**Proposition 3.1.** For generic q, the companion systems

    C_custom(Q)=[[t(Q),-1],[1,0]],
    C_lit(Q)=[[T(Q),-d(Q)],[1,0]]

admit no invertible rational matrix D(Q) satisfying

    C_lit(Q) D(Q)=D(qQ) C_custom(Q).                         (3.1)

This excludes equivalence over C(q,Q), including overall rational equation
multipliers and rational scalar gauges. It does not address a change of
polarization or a gauge with essential singularities.

**Proof.** It suffices to work at a generic positive real q!=1: a matrix
rational in q,Q could be specialized there, away from its finitely many bad
parameters. The q-orbits of nonzero finite points are then infinite.

First D has no finite nonzero poles. C_custom and its inverse are regular
there. C_lit has poles only at alpha_+=q^(-1/2) and alpha_-=-q^(-1/2), and
zeros of its determinant only at q^(-1)alpha_+ and q^(-1)alpha_-.

Consider a q-orbit containing a pole of D. If beta is its lowest-index pole,
evaluate (3.1) at beta/q. Its right side has a pole and D on its left side
is regular. Hence C_lit must have a pole there: beta=q alpha_+ or
beta=q alpha_-. Every pole of D on that orbit therefore has index at least
1 relative to alpha. At its highest-index pole C_lit is regular and
invertible, so (3.1) forces another pole of D one step farther along the
orbit, a contradiction. Orbits containing no alpha give an immediate
contradiction at their lowest-index pole. Thus every entry of D is Laurent
polynomial in Q.

Taking determinants in (3.1), and using that a rational q-periodic function
is constant, yields

    det D(Q)=c(q)(q Q^2-1),  c(q)!=0.                        (3.2)

Write the lower row of D as (a(Q),b(Q)). If v=(f(qQ),f(Q))^T is a custom
solution vector, its image is (h(qQ),h(Q))^T with

    h(Q)=a(Q) f(qQ)+b(Q) f(Q).

The upper row is forced by the second row of (3.1) to be

    (a(qQ)t(Q)+b(qQ), -a(qQ)).                              (3.3)

It remains to bound the Laurent degrees of a,b. This can be done entirely
formally at zero and infinity. For a scalar equation

    E^2 f-U(Q)E f+v(Q) f=0,

the formal quotient r(Q)=f(qQ)/f(Q) obeys

    r(qQ)r(Q)-U(Q)r(Q)+v(Q)=0.

Its two distinct slopes give the following unique formal branches. The
leading constants follow by balancing this displayed equation; their formal
series are obtained recursively because the slopes are distinct:

| Location | Custom large branch | Literature large branch | Custom small branch | Literature small branch |
| --- | --- | --- | --- | --- |
| Q=infinity | q^(-2)Q^2 | q Q^2 | Q^(-2) | q^(-1)Q^(-2) |
| Q=0 | q^2 Q^(-2) | Q^(-2) | Q^2 | q^2 Q^2 |

For each branch set H_branch=a r_branch+b=h/f. It is nonzero: otherwise
the invertible D would kill the corresponding entire solution vector via
(3.3). Its leading integral Laurent power is fixed by

    r_lit/r_custom = H_branch(qQ)/H_branch(Q).

At infinity the powers of H_large and H_small must therefore be 3 and -1;
at zero their orders must be -2 and 2. Subtracting the two branch identities
gives

    a=(H_large-H_small)/(r_large-r_small).

Thus a has highest degree 1 at infinity and lowest order 0 at zero. From
b=H_small-a r_small one gets highest degree at most -1 at infinity and
lowest order at least 2 at zero. Since a,b are Laurent polynomials,

    a=A+BQ,      b=0.

Equations (3.2)–(3.3) now demand

    (A+BqQ)(A+BQ)=c(q)(qQ^2-1).

The coefficient of Q is AB(1+q), so AB=0. But the right side has both a
nonzero constant and a nonzero quadratic coefficient. This is impossible.
QED.

This result does not follow just from a different determinant: d(Q) is
itself a q-coboundary. The pole argument and both endpoint degree constraints
are needed.

**Corollary 3.2 (finite power covers do not remove the obstruction).** The
same non-equivalence holds over rational functions of q^(1/D) and Q^(1/D)
for every fixed positive integer D. In particular it covers rational factors
in the meridian eigenvalue m when Q=m^2, including (1+m^n).

**Proof.** Write Q=M^D and let E act by M->q^(1/D)M. Specialize to a generic
positive q!=1 and take its positive D-th root. The finite-pole propagation
argument in Proposition 3.1 works separately on every lifted orbit, so a,b
are Laurent polynomials in M. The formal endpoint constraints become

    degree_infinity a=D, order_zero a=0,
    degree_infinity b<=-D, order_zero b>=2D.

Thus b=0 and a is a polynomial of degree D with nonzero constant term.
The determinant identity becomes

    a(q^(1/D)M) a(M)=c(q)(q M^(2D)-1).                     (3.4)

All roots on the right have modulus q^(-1/(2D)). If rho is a root of a,
then rho and q^(-1/D)rho must both be roots on the right. They have different
moduli, and rho cannot be zero. This is impossible. A rational gauge over
the stated function field would specialize to a gauge at some such generic
positive q, so none exists. QED.

The exclusion is still for fixed peripheral coordinates (and their finite
power covers). It does not exclude Fourier-type changes of polarization,
nonrational gauges, or a different corrected quantization of the custom
classical action.

### 3.1 What survives of the custom volume theorem

Both systems have the same geometric classical characteristic equation
after removing the explicitly recorded limiting prefactor. Their difference
at generic q is a quantum correction. The positive transfer and dominant-root
estimates in the earlier note remain valid for their specified states and may
also apply to bounded perturbations of a literature transfer system when the
contour selects its dominant solution. They do not, by themselves, identify
that selected solution or its absolute exponential normalization.

There is also an opposite exponential convention to track: the custom norm
grows like exp(+V/h), while the literature Faddeev state here decays like
exp(-V/(2 pi b^2)). This can be compatible with a change of semiclassical
ray or polarization, but it is not an exact equality of states on the rays
already specified. A transform proving such a relation would have to be
written down with its measure and integration cycle.

## 4. Relation to the manuscript and next mathematical obligations

The manuscript's Schläfli identity and Euclidean endpoint explain the custom
cone-transfer normalization. Its warnings about measures, Jacobians and
pole accumulation also explain why equality of a classical action is too
weak to identify quantum states.

The independent literature-state proof in `literature_state_volume.md` avoids
the compact-fold limit by staying at a nondegenerate positive ideal saddle.
It gives a useful broad analytic criterion using the same polyhedral volume
functional. The original proof obligations now have the following status:

1. Uniform positive geometric and preferred peripheral certificates are
   supplied for both twist families in the two twist notes. Their extension
   to broader alternating families remains open.
2. A general annihilator-existence theorem for the same rescaled literature
   integrals is proved in `general_annihilator_and_volume.md`. Explicit useful
   minimal operators beyond 4_1, and stronger full-symbol equalities, remain
   separate algebraic work.
3. Global move identities with generic boundary factors, exact normalization
   and integration cycles remain to be audited before identifying arbitrary
   realizations as one knot state. `faddeev_pentagon_audit.md` now supplies
   the positive Faddeev charged pentagon, its exact phase, and its insertion
   into proper absolutely convergent full face contractions. It also gives
   the explicit constant equivalence J_coarea=J_printed/p_1^2 for the
   fiber-measure convention. The remaining work includes the precise
   meridian polarization and continuation between other move patterns.
   `peripheral_phase_and_state.md` subsequently reconstructs the exact
   charged-tensor phase and identifies the fiber integral with a specified
   published AK level. Its transform is injective, and move covariance
   reduces to an affine phase and possible meridian translation. This is
   an explicit equivalence for the fixed realizations; the coefficients
   and contours for general connecting sequences still require checks.
   `tetrahedral_symmetry_and_figure_eight.md` supplies one actual zero-slope
   certificate: the two published figure-eight realizations differ only
   by their explicit phase, and their selected minimal operators agree.
   This does not identify the different naive custom cone-transfer operator.
   The geometric-endpoint moment argument in the peripheral-phase note
   now forces zero slope along any certified proper positive path. It
   gives state equivalence up to the retained scalar within that component,
   rather than assuming arbitrary triangulations lie in one component.

For 4_1, the state asymptotic and explicit minimal annihilator are treated in
the companion note. For the certified geometric state-integral class,
the analytic volume theorem and general annihilator-existence proof are now
available. The two twist families also have uniform geometric and preferred
peripheral certificates. Exact global move equivalence and the extension
to all alternating knots remain unfinished; neither follows from the
shared classical action of the custom and literature constructions.
