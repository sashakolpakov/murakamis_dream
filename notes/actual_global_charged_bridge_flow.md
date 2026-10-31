# The whole original source as an exactly charged bridge-flow coefficient

28 October 2026. After the exact simultaneous overbridge reduction,
ALL remaining understrand anchor sums can also be performed exactly.
The result is a finite charged coefficient, with one charge N-1 at
every anchor. There are no extra cyclic alias sectors in this whole
coefficient. This follows from nonnegative polynomial degree and
global homogeneity, with the original closed-braid source retained.

This is a larger closed algebra than the isolated complementary
Pochhammer class. Its coefficients remain coupled and oscillatory.
It does not prove a positive state, geometric selection or scalar
noncancellation.

## 1. Use the original scalar source before splitting

Put N>=2, d=N-1, Q=exp(2*pi*i/N), x=-exp(-pi*i/N), s=x^N.
Let W be ANY original complete signed braid word on b heads, in the
balanced factorial basis. Every actual crossing preserves total
INTEGER head degree. The original closed-head pivots are diagonal,

    g_a=(x/s)Q^(-a).

Therefore the original one-cut partial trace is diagonal on its
remaining head. The original averaged marked row, with every entry
1/N, has exactly the same scalar pairing as I/N on this already
assembled diagonal matrix. Hence the actual scalar is

    K_N=chi_N/N *Tr[(I tensor g tensor ... tensor g) W].  (1)

The external original dimension/framing line chi_N remains. This
uses integer-degree conservation BEFORE any Fourier or bridge
decomposition. It is not a sectorwise replacement of the marked row,
a claim about arbitrary inserted currents, or an extra pivotal trace.

Put W in the exact regular propagated frames. This removes every
interior Fourier adapter. At closure head i retain its exact adapter,
including the pivot when i>1. If Z is its final-grid input and Y its
initial-grid output, the kernel is

    E_i(Y,Z)=eta_i/N *Z^(-d) C_i(Z,Y),
    C_i(Z,Y)=sum_(a=0)^d Z^(d-a)(t_i Y)^a,
    (eta_1,t_1)=(1,1),
    (eta_i,t_i)=(x/s,Q^(-1)), i>1.                  (2)

This is the finite Fourier sum, including its removable values.
Its numerator is a homogeneous d-form. Equivalently

    C_i(Z,Y)=product_(r=1)^d (Z-Q^r t_i Y).         (3)

Every nontrivial boundary adapter stays in (2). Matching incompatible
central grids or replacing it by an identity is unnecessary.

## 2. Each reduced overbridge is a homogeneous d-form

Use the exact [signed overbridge theorem](actual_signed_overbridge_unwinding.md).
An overbridge e has m encounters in physical strand order, signs
sigma_j, clocks d>=h_1>=...>=h_m>=0, and spectator UNDER outputs u_j.
Its conditional crossing parameters can be written

    a_j=alpha_j/u_j, b_j=beta_j u_j,
    alpha_j=Q^(-h_j)/x, beta_j=Q^(h_j+1), sigma_j=+1,
    alpha_j=Qx,         beta_j=Q,           sigma_j=-1.

In either case alpha_j beta_j=Q^2x. Write Delta_j=h_j-h_(j+1),
and f_sigma(h)=(-1)^h Q^(sigma*h(h+1)/2). Define the explicit factor

    Gamma_e=kappa^(sum_j sigma_j)
       *product_j f_(sigma_j)(h_j)
       *product_(j<m) [(-alpha_j)^(h_(j+1))
                         Q^(h_(j+1)(h_(j+1)-1)/2)]
       *F_(h_1)/[F_(h_m) product_(j<m)F_(Delta_j)],
    F_r=(Q;Q)_r.                                    (4)

Every factorial index in (4) is at most d. All crossing normalizers
are now explicit. In particular the powers N from the internal
strand sums and the factors 1/N at crossings leave precisely 1/N
for this ENTIRE bridge.

Let Zin and Zout be its overstrand endpoint variables. Directly
clearing the denominators in the exact bridge formula gives

    B_e=Gamma_e/N *Zin^(-d) P_e(Zin,Zout,u_1,...,u_m), (5)

    P_e=
      product_(0<=r<d-h_1)(Zin-Q^r beta_1 u_1)
      *product_(j<m) product_(0<=r<Delta_j)
                         (u_j-Q^(r-1)alpha_j beta_(j+1)u_(j+1))
      *product_(0<=r<h_m)(u_m-Q^r alpha_m Zout).      (6)

The three collections have lengths d-h_1, sum Delta_j, h_m.
Their total is EXACTLY d. Thus P_e is a homogeneous degree-d
polynomial with no negative powers, even when spectator variables
later coincide or particular coefficients vanish. Equation (5)
has only ONE denominator, at the overbridge input.

For example each link denominator u_j^(Delta_j) is canceled by
the corresponding spectator powers of the closed crossing scalar
and link monomial. The last spectator power clears the last output
Pochhammer; the input endpoint becomes Zin^(-d). This is an exact
polynomial identity, not a modulus estimate.

## 3. Understrand clocks and a global bijection

At a signed crossing the overclock from the actual port table is

    label_under,out=label_under,in-sigma*h (mod N),
    z_under,out=x^sigma z_under,in Q^(-sigma*h).     (7)

The label equation holds for both signs, with the table's physical
over/under conventions. The root equation also uses the actual
propagated roots, not an independently imposed meridian value.

Regard every compressed overbridge and every retained closure
adapter (2) as an event with one physical input and one output.
Cut the oriented strand at these events. Between successive events
the remaining encounters are exclusively UNDER encounters. Untouched
head identities have already been suppressed. If there are B
overbridge events, there are

    k=B+b

events and exactly k intervening directed segments. The closure
adapter events break any directed cycle of under encounters, even
on a link component which is always under in the open braid.

Assign one anchor variable X_a to the first grid port on each such
segment. Starting there, (7) gives EVERY port on the segment as

    z_v=zeta_v(h) X_a,
    zeta_v=x^(sum_previous sigma) Q^(-sum_previous sigma*h). (8)

For fixed clocks the map from the segment anchor label to its
port labels is a cyclic translation. Conversely a collection of
the old segment labels determines each h by (7) and its initial
anchor label. Thus the change from all remaining port labels to
the crossing clocks h and k anchor labels is a BIJECTION, of
counting Jacobian one. No congruence sectors are thrown away.

Every anchor segment ends at the input of exactly one event. Thus,
after (8), it acquires exactly ONE denominator X_a^d, from (2) or
(5). The phase zeta_event,input^(-d) is retained in the event factor.
All event output and spectator variables in their numerators are
also substituted by (8). No selected-overbridge variable reappears.

Write P_h(X) for the product of these k substituted event numerator
polynomials, and

    W_h=product_overbridges Gamma_e
          *product_closure eta_i
          *product_events zeta_event,input^(-d).    (9)

The root substitutions in each event polynomial preserve degree, so
P_h has nonnegative exponents and TOTAL degree k d. Its coefficients
and W_h are fully explicit functions of Q,x,kappa,h; they do not
depend on an unknown knot period or on the initial Fermat centers.
The latter only specify the anchor sampling grids.

## 4. Exact disappearance of EVERY cyclic anchor alias

The complete source (1), after the bijection and simultaneous
overbridge reduction, is

    K_N=chi_N/N *N^(-k)
       sum_(h over-monotone) W_h
       sum_(X_a^N=C_a, all a) [product_a X_a^(-d)] P_h(X). (10)

Each C_a is the actual fixed nonzero central value at its segment
anchor. It need not be one. Every event contributes its exact 1/N;
there are k events.

Expand a monomial X^e in P_h. Root sampling can keep it only if

    e_a-d=N l_a, for integers l_a, all a.

But e_a>=0 and d=N-1 imply l_a>=0. Global homogeneity gives

    sum_a N l_a=sum_a e_a-kd=0.

Therefore ALL l_a are zero. The argument includes arbitrarily
large single-variable degrees: there is no omitted high-degree
positive alias, because it would require a negative alias elsewhere,
which the lower bound -d excludes. Consequently, termwise in h,

    sum_(X_a^N=C_a) [product X_a^(-d)]P_h(X)
       =N^k [X_1^d ... X_k^d]P_h(X).               (11)

There are no powers of the C_a on the right. This proves exact
frame-center independence of the WHOLE anchored coefficient at
each clock assignment, without deleting a separate current sector.
Substituting into (10) gives the final original-source identity

    K_N=chi_N/N *sum_(h over-monotone)
                    W_h [X_1^d ... X_k^d]P_h(X).   (12)

All k finite anchor sums have been evaluated. Their N^k cancels
the N^(-k) event normalizations EXACTLY. The remaining 1/N is the
original averaged first-cut source in (1), not a guessed normalization.

## 5. The resulting charged flow algebra and its scope

Every event polynomial is a product of d explicit linear differences
of anchors; closure uses (3). Expanding these factors chooses an
endpoint anchor for each factor. The coefficient in (12) keeps
exactly d choices at EACH anchor. Thus it is a finite nonnegative
integer-charge flow problem, with a complex unit-phase weight on
each choice. The overbridge clock domain is the independent product
of monotone simplexes, equivalently the compositions

    (d-h_1,Delta_1,...,Delta_(m-1),h_m), all >=0, sum=d.

The polynomial coefficient algebra is closed under further anchor
elimination: taking one degree-d coefficient preserves nonnegative
polynomial exponents and lowers total degree by d. It does not
preserve the isolated two-Pochhammer factorization. It is in this
larger EXACT charged algebra that the understrand elimination
closes; no tuned Vandermonde identity or discarded boundary term is
required.

### Exact anchor-cycle transport and charged source currents

For every FIXED h the period in (12) is the specified Laurent
polynomial form

    (1/(2*pi*i)^k) integral P_h(X)
                               product_a dX_a/X_a^(d+1). (13)

It has no finite noncoordinate poles. Consequently the product
circle radii can be changed to ANY finite positive radii, with the
original coefficient and source unchanged. This is a literal torus
homotopy in (C*)^k; it does not use the raw off-grid four-Psi
continuation. Its linear-form zeros are zeros, not residue divisors.
No discarded Phi seam, Cauchy collision or unretained cyclic carry
is needed for this anchor-radius transport. Escape to zero/infinity
is not part of the assertion.

The exact charged Ward current at each anchor is

    [X^d](X_a partial_(X_a)-d)P_h=0.                (14)

More generally the integral of
X_a partial_(X_a)[F P_h product_b X_b^(-d)] against
product_b dX_b/X_b is zero, for a Laurent-polynomial test F.
After multiplying by the FULL W_h and summing h it is still zero.
This is a current of the proved charged representation, not a
claim that arbitrary new matrix coupons preserve its previous
root-grid support theorem.

If none of the linear forms L_r vanishes, the finite-N stationary
anchor equations of (13) in logarithmic coordinates are explicitly

    sum_r c_(r,a) X_a/L_r(X)=d, all a,
    L_r(X)=sum_a c_(r,a)X_a.                        (15)

Thus the stationary current is a rational charge-balance equation.
Each form contributes total one, so the sum of (15) is the known
identity kd=kd. One common scale is redundant. Exactly, without an
asymptotic argument,

    [X_1^d...X_k^d]P_h(X)
       =[Y_1^d...Y_(k-1)^d]P_h(Y_1,...,Y_(k-1),1). (16)

This follows from total degree kd. It removes the common C* scale
from the actual source period. Neither (15) nor (16) by itself
identifies its stationary scheme with the knot A-curve; the remaining
clock equations and their actual source selection must also be proved.

### The exact grouped graph connection

Let q=exp(pi*i/N). A block of length 0<=L<=d has the form

    product_(r=0)^(L-1)(alpha X_i-Q^r beta X_j).

Its coefficient with j-charge a is

    alpha^L S_(L,a) w^a X_i^(L-a)X_j^a,
    w=-(beta/alpha)q^(L-1),
    S_(L,a)=product_(r=1)^L sin(pi*r/N)
       /[product_(r=1)^a sin(pi*r/N)
          product_(r=1)^(L-a) sin(pi*r/N)] >0.     (17)

This follows from [L choose a]_Q=q^(a(L-a))S_(L,a), together
with the q-binomial expansion. Thus the phase is LINEAR in the
block charge after a fixed block phase is removed; it is not a
quadratic approximation.

For the actual blocks in (6), after the undertransport (8), the
connection phases are exactly

    input:   w=q^(sigma_1*h_1) zeta_(u_1)/zeta_(Zin),
    link j:  w=q^(sigma_(j+1)*h_(j+1)-sigma_j*h_j)
                               zeta_(u_(j+1))/zeta_(u_j),
    output:  w=q^(-sigma_m*h_m) zeta_(Zout)/zeta_(u_m),
    closure: w=t_i zeta_(Zout)/zeta_(Zin).          (18)

For closure the first argument in its length-d block starts at Q,
as in (3), which makes its residual phase exactly the actual pivot
t_i=1 or Q^(-1). No extra half-turn is hidden in (18).

Within one bridge, (18) telescopes using the local potentials
q^(sigma_j*h_j)zeta_(u_j) and the unshifted endpoint potentials.
That fact alone is not global flatness: distinct spectator ports
u_j can belong to the SAME under-anchor segment and have different
local potentials. A gauge test must use the actual grouped graph
and differences of FEASIBLE charge flows, including its capacities,
rather than an unsupported abstract cycle.

The audit exposes this graph through graph_blocks(H,S,h). Its
metadata records every block's anchor endpoints, length, event type,
and exact integer q-exponents for alpha,beta,w, modulo 2N. It also
records the baseline outgoing degree at each anchor. If a block
chooses head charge a_e in [0,L_e], the exact charge equations are

    sum_(head=i) a_e-sum_(tail=i) a_e
       =d-sum_(tail=i)L_e.                         (19)

These metadata reproduce the whole polynomial coefficient, with
(17) and all fixed block phases retained. They do not assert that
the connection has trivial holonomy on the feasible-flow lattice.

Equation (12) is stronger than retaining a generic higher
hypergeometric remainder at every underbridge. It supplies the
complete source charge at all anchors and removes all cyclic carry
ambiguity from those sums. It does not make the remaining h/flow
sum positive. The phases in (4), (8), and the linear forms remain;
they can produce cancellation. Identifying a global geometric
critical branch and its selected coefficient is still required.
No broad scalar volume limit follows solely from (12).

For literature COVERAGE only, quantum-determinant presentations of
the Kashaev invariant were already reported by
[Huynh--Le, *On the Colored Jones Polynomial and the Kashaev invariant*](https://arxiv.org/abs/math/0503296).
The abstract also proposes comparing that determinant with a
determinant expression for hyperbolic volume. No determinant formula
or analytic proof from that paper is used here, and no novelty claim
for coefficient/determinant reformulations in general is intended.
The independent statement proved above is the exact original-source
clock bijection, event charge and absence of cyclic anchor aliases.

The proof is for the original complete braid word and its stated
scalar source. An inserted degree-changing coupon need not permit
(1) and would need its own charged source form. The theorem does
not discard such a coupon or claim the same charge automatically.

## 6. Reproducible audit

    python3 experiments/audit_actual_global_charged_bridge_flow.py

The audit verifies the signed undertransport and event/segment
bijection, pointwise homogeneous bridge forms with all original
normalizations, the alias-free root-grid coefficient identity, and
the full formula (12) against original signed physical word matrices
and their actual averaged pivotal scalar, including its external
framing/dimension line.
