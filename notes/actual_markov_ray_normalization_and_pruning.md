# Actual full-volume ray components and exact normalization-cell pruning

28 October 2026. A strict exponential gap for EVERY radial component of
the full-dilogarithm source is false for original hyperbolic knots. This
can be proved in a literal Markov stabilization of the original word,
with its original pivotal source. The resulting ray group is an explicit
nonzero tame scalar times the WHOLE original invariant.

The constructive conclusion is to contract complete normalization cells
before estimating irreducible boundary components. Circle and ray terms
of these cells combine exactly to their original normalization. No
unproved knot value is used to define a replacement source.

## 1. A universal pivotal evaluation on the actual fusion channel

Use the actual strict equal-color crossing and its original factors:

    R_+=kappa C D U_+ C^(-1),
    C=F_2 U_- F_1 F_2^(-1),
    C^(-1)=F_2 F_1^(-1) V_- F_2^(-1),
    d=N-1, F_j=(Q;Q)_j,
    g_b=x^(-d)Q^(-b).

The notation and scalar line are those of
[the original strict factorization](actual_euler_gaussian_cauchy_network.md).
Let r=diag(r_0,...,r_d) be ANY diagonal on the second relative
head. Then the exact operator identity is

    Tr_2[(I tensor g) kappa C D U_+ (I tensor r) C^(-1)]
                                  =kappa x^(-d) r_0 I.   (1)

In particular this holds before choosing a fixed cut entry, an averaged
marker or an exterior tangle. All color, Cartan and pivotal factors
are retained. No assumption on the norm or nonvanishing of r is made.

Here is a direct all-level proof. Total integer degree makes the
partial trace diagonal. Fix its first input a and the relative
channel k. Expanding the original C,C^(-1),U_+,D coefficients,
then setting j=k-b and s=j+(central shift-j), gives its value

    T_k(a)=kappa x^(-d-2k)(-1)^k F_k
      sum_(s=0)^k Q^[-k+(k-s)(k-s-1)/2]
                                     J_s(a)/(F_s F_(k-s)),

    J_s(a)=sum_(j=0)^s (-1)^(s-j) Q^[j(j+1)/2]
                 (Q^(a-j+1);Q)_s/(F_j F_(s-j)).          (2)

The Pochhammer in (2) automatically kills illegal head indices:
j>a contains 1-Q^0, and upper overflow contains 1-Q^N.
Thus the displayed extended sum is exactly the original supported
sum, including endpoints.

The finite q-binomial theorem gives J_s(a)=(-1)^s. To verify this
without a summation citation, expand (T Q^(1-j);Q)_s as a polynomial
in T=Q^a. The j-sum of its coefficient of T^ell contains
(Q^(1-ell);Q)_s. It vanishes for 1<=ell<=s; the constant
coefficient is (-1)^s (Q;Q)_s/F_s=(-1)^s. Applying the same
finite binomial theorem to the remaining s-sum gives

    T_k(a)=kappa x^(-d-2k)Q^(-k)(1;Q)_k
           =kappa x^(-d) delta_(k,0).                    (3)

This proves (1) for every N>=2, including composite and even N.
It does not rely on a scalar-endomorphism theorem for the modified
crossing. The modified partial trace itself has been computed.

For r=I, (1) is the original positive Markov/kink scalar
alpha=kappa x^(-d). For general r the extra factor is exactly
r_0. That factor must remain in the peripheral/framing line;
it is not automatically a unit or a numerical normalization.

## 2. A radial component of an original Markov-stabilized knot

Positively Markov-stabilize ANY original knot word. In its kink,
split only the positive F_2 at the left end of C^(-1), using the
EXACT full-Psi coefficient source from
[the circle/ray theorem](actual_modular_dilog_circle_and_boundary_source.md).
Keep every other factor as the original finite operator, or equivalently
as its complete unsplit relative source.

The positive factorial coefficient is

    F_k=N Q^(d-k) v_(+,d-k)
       =N Q^(d-k)[B_(+,d-k)(R)-E_(+,d-k)(R)].          (4)

Its selected radial term, including the minus sign, has coefficient

    F_k^ray=-N Q^(d-k) E_(+,d-k)(R),
    r_k=F_k^ray/F_k.

Replacing that F_2 in C^(-1) is exactly insertion of (I tensor r)
immediately after C^(-1). Equation (1), with the unchanged Markov
normalization alpha, therefore gives

    WHOLE radial group = h_N(R) K_N,
    h_N(R)=-N Q^(-1) E_(+,N-1)(R).                   (5)

This is an identity of the actual stabilized source for every N,
not an approximation or a source chosen from K_N. Since (1) is an
operator identity, it applies equally to every original cut convention
and to arbitrary exterior tensors. No sectorwise Ward replacement is
performed after the decomposition.

The corresponding circle group is (1-h_N)K_N. Their sum is exactly
K_N. Expanding the other factors into circles and rays merely refines
each of these groups into a fixed finite number of actual relative
components; that count depends on the diagram, not on N.

## 3. The radial group has the same exponential rate

Fix ANY 0<R<1 and put

    phi_R=Li_2(R)/(2*pi),
    c_R=R sqrt(1-R)/[-log(1-R)], 0<c_R<1.

The exact small-disk full-Psi expansion, with two fixed derivatives,
is uniform on 0<=t<=R. Its central logarithmic terms are exponentially
small there and extend with the required fixed derivatives at t=0
for all sufficiently large N. Consequently

    Psi(log t)/(1-t^N)
       =sqrt(1-t) exp[-i N Li_2(t)/(2*pi)]
                                     (1+O_(R,C^2)(1/N)).

The phase phi(t)=Li_2(t)/(2*pi) has no stationary point on [0,R]:
phi'(t)=-log(1-t)/(2*pi*t)>0 and phi'(0)=1/(2*pi).
Two integrations by parts yield

    E_(+,N-1)(R)
        =[c_R exp(-iN phi_R)-1]/N+O_R(N^(-2)),

    h_N(R)=Q^(-1)[1-c_R exp(-iN phi_R)]+O_R(1/N).     (6)

Thus h_N is bounded above and below by positive R-dependent
constants for all sufficiently large N. The circle factor is tame
and nonzero too:

    1-h_N=c_R exp(-iN phi_R)+O_R(1/N).

Multiplication by either factor changes normalized logarithmic growth
by o(1), and preserves zeros at all sufficiently large levels. In
particular the ray group (5) in a Markov-stabilized ORIGINAL figure-eight
knot has the independently proved rate Vol(4_1)/(2*pi), not a strict
smaller rate. This is a whole-knot example; the exterior has not been
replaced by a scalar toy model.

It follows that no theorem asserting a strict gap for every non-pure-
circle component can hold for arbitrary original presentations. If all
finitely many refined ray components had strictly smaller limsup rate,
their group would too, contradicting (5)-(6) for the figure-eight.
This does not refute a statement about a correctly pruned presentation
or a grouped boundary class.

## 4. A source-compatible normalization quotient

There are two exact pruning rules available BEFORE any asymptotics:

1. An adjacent typed fusion pair C_x^(-1)C_x or C_x C_x^(-1) is the
   identity on the original finite heads. If its full relative sources
   were already split, their COMPLETE sum is retained and contracted;
   individual rays need not be negligible.
2. A visible positive pivotal Markov cell in the form (1) is replaced
   by its original alpha times r_0. A complete circle-plus-ray cell has
   r_0=1. An isolated ray or circle group has the explicit factor in
   (5)-(6), which can be retained as a nonzero tame scalar.

These are contextual operator identities: tensoring with an exterior,
composing at its open port, and applying the original cap/source preserve
them. On the channel algebra the Markov evaluation is the character
r->r_0; its kernel is an ideal. This gives a precise pointed quotient
for THESE normalization cells, rather than discarding all radial edges.
The original alpha and any r_0 depending on peripheral variables remain
specified until the actual source is evaluated.

A fixed finite pruning sequence terminates because it removes visible
fusion pairs or kink cells. No confluence or canonical reduced form is
claimed. Negative kinks may also be removed as COMPLETE original
normalization cells by their original Markov identity; the arbitrary-r
evaluation (1) is asserted only for the displayed positive cell.

The rule does not move arbitrary internal projectors or defects to the
boundary. The actual failure of that operation is documented in
[the interior-wall test](actual_interior_wall_cut_relocation.md).
Nor does it claim that every remaining boundary component has a gap.
The meaningful global target is now the source-preserving geometric
comparison AFTER these explicit normalization groups have been
contracted or retained with their known nonzero factors.

## 5. Reproducible audit

`experiments/audit_actual_markov_ray_normalization.py` evaluates the
original finite crossing independently, checks (1) for every channel
and cut entry at complete and generic root colors, verifies both
binomial sums, contracts literal whole figure-eight cut matrices with
the normalized cell, and checks the exact radial factor against (6).
The algebraic all-level proof and uniform lower bound are above.
