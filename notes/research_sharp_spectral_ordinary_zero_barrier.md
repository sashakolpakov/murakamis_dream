# Ordinary-zero barriers for the sharp spectral interval entropy

31 October 2026. **Internally reviewed research reduction.** Root and a
separate reader completed full analytical reviews. This concerns the ORIGINAL
positive-eta tail and both unused intervals at a fixed real spectral
parameter. It is not the fractional perspective entropy. The shared
conclusion is conditional on a feasible activation direction and on the
stated regularity of every affected local term. It does not establish
universal regularity of all source maxima or finite positive multipliers
on structural-zero strata.

## 1. Exact functional and source qualification

Fix delta in a compact subset of (0,1/2), and put k=cos(pi delta)>0,

    alpha(t)=4[k^2-sin^2(pi t)], beta(t)=4sin^2(pi t),
    eta(t)=k^2/sin^2(pi t),
    rho(t;x)=[1+x+sqrt((1-x)^2+4 eta(t)x)]/2,
    Lambda(t;x,1)=beta(t) rho(t;x).

For an original LEFT degree vector

    q=(xi,mu,1-nu,zeta), zeta=nu-mu-xi,
    0<=mu<nu<1/2, xi,zeta>=0,

write

    h_delta(mu,nu,xi)=B_delta(mu,nu)+S(mu,nu)+J^*(mu,nu,xi), (1)
    B_delta=int_0^mu log|alpha|+int_nu^(1/2) log|alpha|,
    S=int_mu^nu log beta,
    J^*=inf_(x>0){J(mu,nu,x)-xi log x},
    J(mu,nu,x)=int_mu^nu log rho(t;x) dt.

At xi=0 or zeta=0, use the continuous monomial value of J^*, which
is zero. Formula (1) is the sharp interval Legendre functional, not t C(alpha). Its coefficient input
is the exact normalized word

    Q_(i,j)=sum_(w in{x,y}^{j-i}) x^#x y^#y
               product_(r=i+2)^j eta_r^[w_(r-1)=y,w_r=x],
    eta_r=[cos(pi/N)+cos(2pi delta)]/
               [cos(pi/N)-cos((2r-1)pi/N)].             (2)

For the fixed delta compact these eta_r are positive at all sufficiently
large levels. The usual tail is K_(i,j)=product_(r=i+1)^j s_r^2 Q_(i,j).
All unused alpha rows and the omitted-half scalar still multiply it.

The positive word's coefficient entropy equals J^*: for mu>0 and
strict outer proportions this is the reviewed
[positive-transfer Perron/coefficient theorem](research_positive_eta_word_transfer.md). The same rate identification extends to
mu=0 by endpoint truncation. For precision, cut the first aN letters,
with a>0 fixed and small. Their total coefficient mass at any bounded
positive tilt has normalized logarithm O(a log(1/a)), since

    eta_r<=C N^2/r^2,
    sum_(r<=aN) log max(1,eta_r)
                      <=C aN log(1/a)+O(log N).        (3)

For an upper bound sum over the at most aN+1 prefix degrees, use (3),
and apply the strict coefficient theorem to the remaining regular
interval. For a lower bound choose an all-y prefix and retain the
desired x count in the remaining interval; for a strict limiting outer
proportion this is possible for all small a. The joining transition is
bounded below by a positive constant at the cut. The limiting tilted
integrals converge as a decreases to zero, because log rho has only an
integrable logarithm at t=0. This proves the rate for each strict outer
proportion at mu=0, without assuming a relative packet at its initial row.
At the outer endpoints the word coefficient is exactly one. The same
finite-tilt upper argument and the all-word lower bound using
min(1,eta_r)>=c>0 give continuity at those endpoints.

This identifies the positive tail, not a nonzero lower bound through a
sampled omitted-half zero. For any fixed sign chamber of varying rows,
the common unused factors can be factored EXACTLY before comparing the
remaining positive coefficients. If a common factor vanishes, the whole
corresponding source piece vanishes. Formula (1) and the arguments below
are also valid as calculus statements for the sharp variational upper
functional; they do not identify the absolute rate of a signed sum of
central CROSS paths. No full-source entropy theorem is being assumed.

## 2. Complete boundary expansion on a nonterminal interval

Fix a source point as in (1), with nu strictly between zero and 1/2,
positive interval length, and neither positive endpoint at the moving
pole t_c=1/2-delta. Allow mu=0. Keep delta fixed. Along any fixed
admissible affine direction q(eps)=q+eps dot_q, write dots for the
corresponding affine coordinates. Then

    h_delta(q(eps))-h_delta(q)
           =b(q,dot_q) eps log(1/eps)+O(eps),          (4)

with the following coefficients:

    mu,xi,zeta>0:               b=0;
    mu=0, xi,zeta>0:            b=dot_mu;
    mu>0, xi=0:                b=dot_xi;
    mu>0, zeta=0:              b=dot_zeta;
    mu=xi=0:                   b=2(dot_mu+dot_xi);
    mu=zeta=0:                 b=2(dot_mu+dot_zeta).    (5)

Vanishing-coordinate slopes are nonnegative. In particular every b is
nonnegative; it is positive whenever the direction activates one of the
listed zero coordinates. These cases exhaust the positive-length domain.
The constants are uniform for delta in a fixed compact and for the
remaining strict coordinates in fixed compact subsets. A single fixed
direction suffices for the shared exclusion argument below; no moving
regularization or diagram-uniform constant is asserted.

Here is a proof using the actual positive root rather than the endpoint
triangle-difference formula. If mu>0 and the outer loads are strict,
strict tilt convexity gives a finite smooth minimizing x. At xi=0,
rho=1+eta x+O(x^2), uniformly on the interval, so

    J=x int_mu^nu eta(t)dt+O(x^2),
    partial_(log x)J=x int_mu^nu eta(t)dt+O(x^2).

When xi=eps X with X>0, the minimizer satisfies x asymptotic to a
positive constant times eps, and J^*=-X eps log eps+O(eps). If X=0,
the affine path remains on the exact monomial boundary. The symmetry
of the original continuant in x,y gives the zeta-reflected statement.
The remaining terms in (1) are smooth here, including row variations.

If mu=0 and both outer loads are strict, the minimizing tilt stays
in a positive compact. Uniformly there,

    Lambda(t;x,1)=4 pi k sqrt(x) t [1+O(t)], t->0.

Removing the interval [0,eps dot_mu] therefore contributes
-dot_mu eps log eps+O(eps) to the tail integral. Its tilt derivative
has a finite limit, so the tilt changes by O(eps); the other row and
degree variations contribute O(eps). The unused prefix is smooth at
zero because alpha(0)=4k^2>0. This proves the second case of (5).

For the simultaneous corner mu=xi=0 put mu=eps B, xi=eps X.
First separate the monomer part S. Since beta(t)=4pi^2 t^2[1+O(t^2)],
its removed prefix contributes

    S(eps B,nu+O(eps))-S(0,nu)
                       =-2B eps log eps+O(eps).        (6)

If X=0, J^*=0 exactly and this finishes the proof. Suppose X>0.
For x sufficiently small, put D=sqrt((1-x)^2+4eta(t)x). Direct
differentiation gives the exact identity

    partial_(log x)log rho
      =1/2+(x-1)/(2D)=2eta(t)x/[D(D+1-x)].

For x<=1/2 its denominator is comparable to 1+eta(t)x. Since
eta(t) is comparable to t^(-2) throughout the fixed interval ending
at nu<1, this proves the uniform comparisons

    partial_(log x)log rho(t;x) asymp min(1,x/t^2).

Integrating min(1,x/t^2), splitting at sqrt(x) when that point lies
inside the interval, gives, for mu small and nu bounded below,

    partial_(log x)J(mu,nu,x) asymp x/(mu+sqrt(x)).     (7)

At xi=eps X the unique tilt solving this equation therefore satisfies
x asymp eps^2, with constants depending on the fixed B,X and compact
parameters. Also

    0<=J(mu,nu,x)<=C sqrt(x)=O(eps).                  (8)

To see (8), split at t=sqrt(x): below that point log rho is bounded
by C+log(sqrt(x)/t), and above it by Cx/t^2, plus a smooth O(x) tail.
Thus J^*=-2X eps log eps+O(eps). Adding (6) and the smooth unused
factor changes proves b=2(B+X). Reflection gives the final case.
If both B and X vanish the affine path stays on that corner, and only
the regular nu dependence changes. No constant hidden in (8) divides
by a vanishing source coefficient or omitted-half scalar.

The same calculation applies to any full-row strict interval contained
in [0,1), with its upper endpoint bounded away from 1 and the two poles,
after replacing the constant upper integration endpoint in B. The
singular behavior at the lower endpoint is identical. Exact finite row
reflection supplies the corresponding upper-endpoint-only statement.
This observation does not claim the simultaneous two-terminal corner.

## 3. A width-independent feasible-direction lemma

Let P be the actual selected source's bounded incidence-flow fiber:
the original unit port supplies (or separate half-unit triangle rows
when those are genuinely the specified local variables), unchanged
ordinary face demands, original lower/upper incidence bounds, and
protected demands zero. In a reflected
RIGHT row use its actual exchanged parent/child coordinates. Let q be a
local maximum of the sum of sharp interval functionals. Suppose:

1. Each affected sharp row has positive interval length, strictly
   nonterminal upper row and endpoints away from the spectral poles,
   as in section 2, or satisfies its stated exact reflection.
2. All other objective terms have a directional expansion whose
   eps log(1/eps) coefficient is nonnegative and whose remaining
   change is O(eps). Smooth terms qualify. Actual complete-triangle
   entropies also qualify by their elementary closed-corner expansion,
   when those triangles are genuinely the specified source functional.
3. There is a point q^+ in P which activates at least one of the zero
   ordinary incidences appearing in (5). Protected zeros remain zero.

Then q is not a maximum. Indeed the EXACT common-target segment
q(eps)=(1-eps)q+eps q^+ stays in P. The strict interval and pole
margins survive for small eps. Every term in (5) is nonnegative, and
at least one is strictly positive. Hence the sum increases by

    b_total eps log(1/eps)+O(eps)>0, b_total>0.        (9)

No concavity of h_delta in the row or face variables is used. No
fractional atomization, cover, or redistribution of triangle mass is
invoked. All balances are maintained by the original feasible segment.
The conclusion applies at every fixed width whenever these hypotheses
are verified, not to every boundary point of every diagram.

In particular, if every nonstructural zero ordinary incidence has
some feasible activation, average finitely many such witnesses to
obtain one q^+ activating all of them. A maximum on this regular
stratum then has only the ordinary zeros FORCED by P and the prescribed
protected zeros. This differs from asserting that every ordinary
incidence is positive or that the complete geometric flow lies in the
selected spectral-sector fiber.

## 4. The finite source test for a removable zero

The feasibility input is a finite transport question, not a geometric
assumption. Let l_a<=q_a<=u_a be the original arc bounds. Subtract
lower bounds to obtain residual row supplies r'_e, residual face
demands d'_f, and arc capacities u_a-l_a. Feasibility is equivalent
to their nonnegativity, equality of total supply and demand, and all
the finite cut inequalities

    sum_(e in I) r'_e - sum_(f in J) d'_f
          <=sum_(a:e in I,f notin J)(u_a-l_a).         (10)

They are the cuts of the ordinary source-row-face-sink maxflow network.
For a zero arc a with positive upper capacity, replace its lower
bound by eps>0 and test (10), updating both incident margins. That
arc is removable exactly when the modified network is feasible for
some eps>0. Protected zero arcs have upper capacity zero and remain
absent. Repeated incidences are retained as separate arcs.

Equivalently, from a given feasible q draw a directed row-to-face arc
when q_a<u_a and a directed face-to-row arc when q_a>l_a. A zero
incidence a=(e,f) can increase iff its forward capacity is positive
and this residual graph has a directed path from f back to e. The
cycle augmentation proves sufficiency. Necessity follows by decomposing
the difference of two feasible bounded flows into residual circulations.
Thus tight Hall cuts characterize precisely the structural zeros on
this fixed fiber; an abstract middle-edge forest does not remove them.

Any finite-level support offsets and eventual-feasibility qualifications
belong to the original definition of P and must already have been
checked if P is obtained as a limiting sector polytope. This lemma
does not replace that source check by a larger relaxed network.

## 5. Why the excluded strata cannot be hidden in O(eps)

There are exact negative singular terms outside section 2. At the
row-zero diagonal take the actual monomer direction

    mu=0, nu=eps W, xi=eps W, zeta=0, W>0.

Its sharp entropy difference is

    int_0^(eps W) log[beta(t)/|alpha(t)|]dt
                        =2W eps log eps+O(eps)<0.     (11)

Thus a zero-length port at the initial row can offset another port's
positive activation barrier. A shared regularity theorem cannot ignore
such terms merely because they are continuous.

Similarly, if a monomer interval begins at mu=t_c, increasing its
start by eps B>0 changes the entropy by

    int_(t_c)^(t_c+eps B) log[|alpha(t)|/beta(t)]dt
                          =B eps log eps+O(eps).      (12)

This is another negative singular coefficient. It explains the explicit
pole exclusion. The opposite endpoint and full-row reflections require
the same care. Neither example is asserted to extend to a globally
feasible maximizing source flow.

The previous fractional-forest and cover-star obstructions remain
unaffected: they concern t C(alpha), while (1) is the true sharp
interval functional. They warn against assuming a lossless same-sector
activation or a supplied global concavity theorem. Here feasibility is
tested in P and only the exact directional singularities are used.
The result supplies no automatic finite positive multipliers, no control
of all diagonal/pole/terminal strata, and no complete-volume inequality.

## 6. Terminal-row calculus, with the KKT boundary retained

The six ordinary-zero coefficients in the reviewed barrier theorem remain
valid at nu=1/2 when 0<=mu<nu and delta lies in a fixed compact subset
of (0,1/2). Only the affine directions allowed by the original LEFT
bound are used: dot_nu<=0 at this endpoint.

Indeed beta(1/2)=4, eta(1/2)=cos^2(pi delta)>0, and
alpha_delta(1/2)=-4sin^2(pi delta) is bounded away from zero.
Thus the upper-row changes in B, S and the finite-tilt word integral
are O(eps), exactly as in the original proof. The positive-length
condition still prevents mu=nu. At a joint mu=xi=0 corner, the
estimate eta(t) comparable to t^(-2) remains uniform on [0,1/2],
so the same x comparable to eps^2 calculation applies unchanged.
No coefficient in the six-case table depends on a singularity at
nu=1/2; its former strict inequality was only a convenient stratum
restriction. Exact RIGHT reflection gives the corresponding terminal
constraint on the reflected interval.

Consequently the feasible-direction exclusion of removable ordinary
zeros extends to these terminal rows, provided the SAME original
fiber supplies a direction, the stated pole exclusions hold at the
other endpoint, and all other affected terms have no negative singular
coefficient (or are diagonals controlled by free spectral retuning).

This is a directional boundary calculation, not terminal stationarity.
The active inequality nu<=1/2 remains in the variational problem.
There is no conclusion partial_nu h + lambda=0; an inequality or
additional KKT multiplier can remain. No terminal retagging, complete
triangle substitution, or all-interior spectral classification is
licensed by this extension.

## Dependencies and review scope

The [original one-sided source](actual_global_left_weighted_spectral_envelope.md)
retains both unused row products and the omitted-half scalar. The
[exact positive word](research_positive_eta_word_transfer.md) supplies
the coefficient input used above. This note proves its own directional
boundary estimates and bounded-flow activation criterion; it does not
borrow concavity or atomization from a different entropy.

Root and an independent reader checked the entire proof: endpoint
truncation, both tilt scales, all six singular coefficients, finite Hall
cuts and residual activation, and the negative fixed-spectrum examples.
The terminal-row calculus extension received separate full analytical
review with its active-inequality qualification. No numerical asymptotic
audit is claimed. The open strata and conditional
source-identification scope in sections 1, 3 and 5 remain part of the
theorem.
