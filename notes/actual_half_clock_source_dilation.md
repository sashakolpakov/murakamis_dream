# A source-exact full half-clock dilation of the physical head

28 October 2026. At complete color the ORIGINAL N-dimensional head is
an invariant orthogonal window in an explicit 2N-clock representation.
The weighted cyclic shifts have zeros at both window boundaries.
The unrolled H, full half-Cartan, genuine dual, N-normalized turns,
original pivot and selected cut all lift exactly. For a one-component
knot, the selected cut forces the physical window around the entire
component, so the full extended contraction is the original scalar.

This supplies a legitimate unitary 2N Fourier ambient space. It does
not supply the global triangulation edge character required by the
[positive-angle majorant](positive_angle_majorant_and_integer_winding.md).
The new ambient clock dilates the old window; its conserved physical
charge is already present in the original unrolled degree equations.

## 1. Exact complete-color generators

Put q=exp(pi*i/N), Q=q^2, d=N-1, x=q^d=-q^-1, and c=q-q^-1.
Use the ORIGINAL balanced basis w_a=v_a/(Q;Q)_a. The original head is

    H w_a=(d-2a)w_a,       K w_a=x Q^-a w_a,
    F w_a=(1-Q^(a+1))w_(a+1),
    E w_a=(Q^-a-1)/c^2 w_(a-1),    0<=a<N,                      (1)

with the nonexistent endpoints set to zero. Indeed the original
unbalanced E coefficient is [a]_q[N-a]_q=[a]_q^2 and
[a]_q^2/(1-Q^a)=(Q^-a-1)/c^2. No factorial metric change is being
made in this note: (1) is the already used balanced presentation.

On W=C^(2N), with orthonormal basis u_J, define

    T u_J=q^J u_J,     X u_J=u_(J+1 mod2N),
    F_W=X(1-Q T^2),   E_W=X^-1(T^-2-1)/c^2,
    K_W=x T^-2,       H_W u_J=(d-2J)u_J.                          (2)

Here TX=qXT; Q is still q^2 of order N. The zeros of F_W occur
at J=d,2N-1 and those of E_W at J=0,N. Hence

    W=W_0 direct_sum W_1,
    W_0=span(u_0,...,u_d),  W_1=span(u_N,...,u_(2N-1))            (3)

is an orthogonal decomposition into invariant unrolled modules.
Under u_(N epsilon+a) <-> w_a, E,F,K are the original matrices,
and H is shifted by -2N epsilon. In particular

    W=V_d direct_sum V_(d-2N),
    E_W^N=F_W^N=0.                                               (4)

The first-window inclusion i and p=i^* are isometric and satisfy
p i=I. Any prescribed original head metric can instead be copied
orthogonally to both summands; the inclusion remains isometric.
Unitary ordinary DFT statements below use the balanced flat metric.

The unrolled quantum relations follow on each summand from (1).
For example [H,E]=2E and [H,F]=-2F hold at the cyclic wraps because
the corresponding weights are ZERO, not because H was made cyclic.
Replacing H by a residue class would lose this justification.

## 2. The full Cartan and the genuine dual

Use the ORIGINAL finite universal crossing, in its original order,

    Rcheck=Flip q^(H tensor H/2)
          sum_(n=0)^d q^[n(n-1)/2] c^n/[n]_q!
                                      E^n tensor F^n.            (5)

Formula (5), and its actual inverse, are well defined on W. Every
denominator has n<N and is nonzero. Since each summand in (3) is
invariant, a crossing transports its two summand labels with the
physical strands. On the selected W_0 tensor W_0 its restriction
is EXACTLY the original Rcheck, including the common Cartan scalar
kappa=q^(d^2/2). No kappa was stripped or replaced by a 2N scalar.

The full Cartan is not the bare cyclic phase Q^(ab). On the original
window it is

    q^[(d-2a)(d-2b)/2]
        =kappa q^[-d(a+b)] Q^(ab).                               (6)

On W_epsilon tensor W_eta its ratio to the original Cartan is
(-1)^[d(epsilon+eta)]. This is a unit phase; it follows by expanding
the two unrolled H shifts before taking q powers. The restriction
statement itself does not require dropping this phase elsewhere.

Use the GENUINE dual W^*, with the ORIGINAL antipode and pivotal
duality. It is V_d^* direct_sum V_(d-2N)^*. In the copied original
dual basis u_(N epsilon+a)^vee its H weights are

    H_Wvee=d+2N epsilon-2a.                                     (7)

In particular, its second dual summand is not assigned the naive
weight d-2(N+a). Those two expressions differ by 4N, which is
invisible to q^H but not to unrolled H as an operator. The true
dual is what justifies the cups, caps and half-Cartan identities.

Write the original pivotal matrix as

    g_a=x^(1-N) Q^-a.

The root parameter is still N: the pivot on W is K_W^(1-N), not
K_W^(1-2N). Copy this exact matrix to both summands. In the original
unrolled convention the twist at highest weight alpha is
q^[(alpha^2+2(1-N)alpha)/2]; its values at d and d-2N agree, since
their ratio is q^(2N^2)=1. Thus the original zero-framing correction
also lifts with its exact scalar. The original left turns,
in the original factorial boundary frame, lift as

    coev_L^W=sum_(epsilon=0,1) sum_(a=0)^d
              N x^-a u_(N epsilon+d-a) tensor u_(N epsilon+a)^vee,
    ev_L^W(u_(N epsilon+a)^vee tensor u_(N eta+b))
              =delta_(epsilon,eta) x^a/N delta_(a+b,d).           (8)

The right turns have the SAME original pivot factors; for example

    coev_R^W=sum_(epsilon,a) N x^-a g_(d-a)^-1
               u_(N epsilon+a)^vee tensor u_(N epsilon+d-a).    (9)

These are the direct-sum genuine turns, not new normalization
choices. They use N and 1/N, not 2N and 1/(2N). Restricting every
leg to the first summand gives the literal original turns. The
ordinary cap is still not declared to be the Hermitian adjoint of
the cup; this dilation does not change the pivotal trace's positivity.

## 3. Exact original one-component source

Let P_0=i p be the first-window projector. If the original closed-braid
source is the normalized averaged cut, retain it literally as

    (1/N) Tr_(W cut)(P_0 C_W),                                  (10)

with every original closed pivot and zero-framing factor retained.
If the original source is a specified cut matrix entry, retain that
entry in W_0 instead. These choices agree for the uninserted scalar
knot endomorphism; they are NOT interchanged for arbitrary inserted
exteriors. In a plat retain its actual marked coupon g E_00 and its
prescribed pivotal side, extended in W_0. No replacement by
I_W/(2N) is made.

**Source theorem.** Replace every physical head by W, every dual by
W^*, and use (5),(8),(9) and their actual inverse/right versions.
For ANY one-component knot presentation, its original selected
scalar is unchanged.

Proof. Expand the extended contraction by summand labels epsilon.
Each crossing transports the two labels with their physical strands;
each cup or cap matches the label on its two incident physical legs.
Thus the label is constant along each physical link component.
The original selected cut forces label0 on its component. Since
there is only one component, every nonzero term lies in W_0 on every
physical leg. Each local restriction is exactly the original coupon,
including Cartan, pivot, boundary and framing constants. Therefore
the entire sum equals the original scalar, not merely its modulus
or its leading exponent. This proof also retains literal original
insertions which preserve or are lifted inside the selected summand,
provided their original cut functional is kept unchanged. It does
not apply a scalar-knot trace conversion after inserting new coupons.

For a multi-component link, each component must carry its specified
selected projector if this same statement is wanted. Leaving another
component unselected permits its other summand and is a different
source. Likewise arbitrary new offdiagonal summand-changing coupons
are outside the theorem.

The construction is an exact COMPLETE-COLOR lift. At generic color
the direct sum V_alpha direct_sum V_(alpha-2N) still gives an exact
isometric module lift, but the simple E polynomial in (2) no longer
gives its boundary values: endpoint projectors are then required.
No unproved whole-meridian polynomial-weight extension is inferred
from the complete-color q-number zeros. The original full modified
dimension remains an external normalization line throughout.

## 4. What full-clock information actually follows

On W and its genuine dual the copied half-clock is T u_J=q^J u_J.
Although their unrolled H lifts differ, both satisfy

    T=q^(d/2) q^(-H/2).                                         (11)

The dual second-summand difference4N contributes q^(2N epsilon)=1.
Unrolled total-H conservation therefore gives the EXACT identity

    [Rcheck,T tensor T]=0.                                      (12)

On every full turn, J+Jvee=2N epsilon+d, so

    (T tensor Tvee)coev=q^d coev.                               (13)

The corresponding cap has the same affine charge. Consequently a
full q-character average is legitimate at these PHYSICAL vertices.
The charge in (12) is not only modulo N: on the original window,
the conserved unwrapped total lies in[0,2d], whose width is <2N,
so its modulo2N equation is equivalent to exact integer equality.

However, (12)--(13) already hold on the original N-window. They are
its existing integer flow and inverse-meridian pairing laws, now
realized in a full-clock ambient space. The quantum factorial still
has base Q=q^2 and length N; the nilpotency order in (4) is still N.
Nothing has changed it to a 2N-dimensional cyclic dilogarithm.

There is an explicit limitation for the OLD unweighted N-cyclic
shift used in cyclic-atom factorizations. Its exact blockwise lift
is not X. Put

    P_wall=|d><d|+|2N-1><2N-1|,
    S_hat=X(I-P_wall)+X^(1-N)P_wall.                             (14a)

Then S_hat is the direct sum of the two ORIGINAL N-cyclic shifts,
so S_hat^N=I. Directly on every basis vector,

    T^2 S_hat=Q S_hat T^2,
    T S_hat-q S_hat T=-2q X^(1-N)P_wall T.                        (14b)

The right side is a nonzero rank-two wall current, of norm2 in the
flat metric. The two weights in (2) kill their respective endpoint
terms, which is why the complete original R lifts cleanly. An old
cyclic-atom factorization, however, must use S_hat and retain (14b)
if its old Q-Weyl relation is refined to a q relation. Replacing its
unweighted S_N by X without this correction changes its physical
restriction. Thus the dilation does not automatically upgrade the
old cyclic shape algebra to a free full-q Weyl algebra. The small
rank alone supplies no bound after arbitrary factorial conjugations.

Let F_(2N) be the unitary 2N discrete Fourier transform. The physical
window becomes the rank-N projector

    (F_(2N) P_0 F_(2N)^*)_(rs)
           =(1/(2N)) sum_(a=0)^d q^[a(r-s)].                     (14)

Its diagonal is1/2. For r!=s its entry is zero if r-s is even and
1/[N(1-q^(r-s))] if r-s is odd. Thus the selected Fourier source is
not an independent uniform full-clock source: it retains this exact
projector, or its propagated equivalent under the full contraction.
Plancherel preserves it rather than deleting it.

To apply the positive affine-angle theorem one must STILL construct
the actual source map to tetrahedral nonnegative angles with sum d,
identify the geometric edge-incidence rows, and prove the full edge
character Ek=2d modulo2N with subexponential comparison norm. Physical
head conservation (12) is not that global geometric edge equation.
Joint noncommuting quantum shapes are not automatically positive
angle labels either. This dilation resolves the cyclic-wrap issue
for the physical head; it does not close those geometric/source gates.

[Audit](../experiments/audit_actual_half_clock_source_dilation.py):
literal generators and unrolled relations, full Cartan/crossings,
genuine dual turns, physical affine charge, Fourier projector and
selected original one-component braid sources. Finite checks are
supplementary to the direct-sum and component-label proof above.
