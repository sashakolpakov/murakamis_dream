# A quantum-curve volume program with explicit proofs

**Scope clarification.** The task requires a definition already present in the
literature, followed by an independent proof audit. The custom constructions
in this note are preserved as potentially useful comparison candidates; their
equivalence to a literature quantum A-polynomial and its specified state has
not been proved. In particular, their volume laws do not establish the target
conjecture. See `literature_definition_audit.md` for the active comparison.

**Subsequent audit.** `literature_state_volume.md` now gives an independent
proof for the specified literature figure-eight state and a broader certified
state-integral criterion. `custom_literature_equivalence.md` proves the exact
completion of our compact product to the literature Faddeev function, and
rules out a rational two-by-two gauge between the naive figure-eight transfer
equation here and the audited literature equation in fixed coordinates,
including finite power covers of the peripheral variable. The compact
factor and its Faddeev completion have the same local b-shift equation;
their state normalizations still differ by the modular-dual factor.
`general_annihilator_and_volume.md` supplies the general annihilator argument,
and the two twist notes supply uniform geometric and peripheral certificates
for the specified twist-knot realizations. `faddeev_pentagon_audit.md` now
proves the positive Faddeev local move, including its scalar; the global
fiber-state identification remains open.
The custom constructions below are retained with their own state conventions.

Research note, 25 October 2026. No claim of novelty is made. This note does not
prove the colored-Jones volume conjecture or a theorem for all alternating knots.
It proves a volume theorem for a specified, Jones-independent quantum curve,
gives a broader sufficient criterion, and tests a separate local construction.

## 1. What the supplied manuscript contributes

Source: `/Users/sasha/Downloads/polyhedral_volumes_and_geodesic_identities.pdf`,
*Polyhedral coordinates, Weil–Petersson volumes, and geodesic identities*,
24 October 2026, 56 pages. All pages have been read.

The relevant inputs and limitations are unusually explicit in the manuscript:

* Section 8.2, equation (8.3), printed page 19: for a bounded polyhedron Q in a
  homothetic Klein family, enclosed volume is r^3 Vol_E(Q) + O(r^5).
* Section 8.3, equations (8.4)–(8.5), page 20: Schläfli gives
  sum_e L_e b_e = -3 Vol_E(Q). Doubling gives a cone manifold with a singular
  **graph**, not automatically a knot cone manifold.
* Section 8.5, equations (8.8)–(8.9), page 21: the WP-weighted exponential integral
  is explicitly a comparison model, not an identified quantum knot invariant.
* Sections 9.6–9.7, pages 25–27: a normalized change-of-polarization kernel needs
  spectral measures and Jacobians. The Liouville residue and the proposed joint
  geometric/semiclassical scaling are different limits.
* Sections 11.4–11.5, pages 35–37: the screened auxiliary Gram matrix has rank two
  and its reduced classical potential has no regular nonzero saddle. That
  residue cannot be substituted for a generic shrinking compact tetrahedron.
* Sections 11.6–11.8, pages 37–39: a genuine regular compact tetrahedron has a
  rank-three Euclidean fold. Its cubic classical phase does not establish a
  uniform quantum asymptotic, because double-sine poles accumulate in the saddle
  neighborhood. Equation (11.26) even locates poles at the classical saddle for
  an explicit sequence of quantum parameters.
* Sections 13–18 concern surface geodesic identities. Their constancy and
  unfolding results do not by themselves identify a three-dimensional quantum
  state or a knot A-polynomial.

Consequently, the manuscript supplies a classical normalization principle and
precise obstructions to one quantum construction. It does not already supply an
analytic quantum A-polynomial volume theorem.

### 1.1 What F_e means in the Klein expansion

For clarity, the parity assertion in the original question is about a
*homothetic* Klein family x=r y of a fixed bounded, nondegenerate Euclidean
polyhedron. It is not an automatic assertion about every knot cone family.
The curvature-minus-one Klein metric pulls back to

    g_r=r^2 h_tau,     tau=r^2,
    h_tau(dy,dy)=|dy|^2/(1-tau|y|^2)
                   +tau(y dot dy)^2/(1-tau|y|^2)^2.

This is an analytic positive metric in tau near zero. If an edge has fixed
endpoints p,q in y coordinates, put v=q-p and y(t)=p+t v. Its function F_e is
the length of that fixed segment in h_tau:

    F_e(tau)=integral_0^1 sqrt(
        |v|^2/(1-tau|y(t)|^2)
          +tau(y(t) dot v)^2/(1-tau|y(t)|^2)^2) dt.

The segment is a hyperbolic geodesic in Klein coordinates. Because v!=0, the
integrand has a positive analytic square root near tau=0, uniformly in t.
Thus F_e is analytic and F_e(0)=|q-p|=L_e, giving

    ell_e(r)=r F_e(r^2)=r L_e+r^3 F_e'(0)+O(r^5),   r>0.

Dihedral angles are computed from the two fixed face conormals using
h_tau^(-1), with their norms in the denominator. The overall metric factor
r^2 cancels from that quotient. Since the Euclidean angle is strictly
between 0 and pi, arccos is analytic at its cosine. Hence

    alpha_e(r)=G_e(r^2)=alpha_e^E+r^2 G_e'(0)+O(r^4).

If alpha denotes the doubled cone angle, multiply the dihedral angle by two;
the same parity holds. The functions F_e and G_e depend on the particular
edge and fixed polyhedron. Moving the rescaled vertices with an arbitrary
r-dependent rule, or degenerating a face or angle, can invalidate this
argument. The formal use of negative r is only an analytic continuation:
physical lengths are |r|F_e(r^2).

## 2. What a quantum A-polynomial statement must specify

Use the SL(2,C) meridian and longitude eigenvalues m,l, and write

    A(l,m) = sum_{j=0}^d a_j(m) l^j.

Choose an ordering and a quantum torus:

    (M f)_n = m_0 q^n f_n,       (L f)_n = f_{n+1},
    L M = q M L.

A quantum-curve problem consists of an operator Ahat_q, a specified solution,
its normalization/boundary data, and a prescribed path q -> 1. The minimal
symbol condition is

    Ahat_1(l,m) = A_geom(l,m)

up to declared nonzero factors and peripheral coordinate changes. This is a
definition of the quantization under study, not a claim that it is the Jones
recurrence.

An elementary obstruction explains why a state must be specified. If Ahat_q Z=0,
then Ahat_q [c(q) Z]=0 for every scalar c(q) independent of the boundary variable.
Taking c(q)=exp(C/h), q=exp(h), changes the exponential rate. The same operator
also usually has several independent solutions. Thus the operator alone has no
well-defined volume limit.

The manuscript's zero-volume Euclidean endpoint is a useful way to fix boundary
data, provided an actual geometric cone branch connects it to the cusp. We now
use that idea in an explicit finite recurrence, without a contour prescription.

## 3. A direct cone-transfer quantization

### 3.1 Geometric hypotheses

Suppose a knot has a selected geometric factor

    A_geom(l,m) = l^2 - t(m) l + 1,

where t is a Laurent polynomial, or a rational function without poles on the
path below. Suppose there is a geometric cone family K(alpha), 0<alpha<T, with:

1. m(alpha)=exp(i alpha/2), and t(m(alpha))=sigma a(alpha), sigma in {+1,-1};
2. a is continuous on [0,T], a>=2 there, and a>2 on (0,T);
3. K(0) is the complete finite-volume knot complement;
4. its curvature-minus-one volume tends to zero at alpha=T;
5. the singular locus is exactly K, and the longitude branch has

       l(alpha) = sigma lambda(alpha),
       lambda(alpha) = (a(alpha)+sqrt(a(alpha)^2-4))/2 >= 1.

These are geometric and algebraic hypotheses to check, not consequences of
alternation. In this normalization the singular geodesic length is

    ell(alpha) = 2 log lambda(alpha).

Schläfli then gives the classical identity

    Vol(K) = integral_0^T log lambda(alpha) d alpha.                 (3.1)

No volume value is used in the quantum definition below.

### 3.2 Exact quantum definition

For an integer n>=1 put h=T/n and

    q_n=exp(-i h/2),    m_k=exp(i(T-kh)/2).

Set f_0=1, f_1=sigma, and define

    f_{k+2} - t(m_k) f_{k+1} + f_k = 0,   0<=k<=n-2.             (3.2)

This is exactly the left-ordered quantum equation

    [L^2 - t(M)L + 1] f = 0,       LM=q_n ML,                    (3.3)

and its commutative symbol is the chosen A_geom. The normalization is fixed at
the zero-volume endpoint. Changing it by exp(c/h) is not allowed.

This is a new specified quantization problem. No assertion is made that the
absence of further q-corrections is forced by topology, or that this operator is
the usual quantum A-polynomial.

### 3.3 The volume theorem

**Theorem 3.1.** Under hypotheses 1–5,

    lim_{n->infinity} (T/n) log |f_n| = Vol(K).                   (3.4)

**Proof.** Put f_k=sigma^k g_k. Then g_0=g_1=1 and

    g_{k+2}=a(T-kh)g_{k+1}-g_k.

Induction gives g_{k+1}>=g_k>0: if this holds at k, then

    g_{k+2}-g_{k+1}
      =(a_k-2)g_{k+1}+(g_{k+1}-g_k)>=0.

Define r_k=g_{k+1}/g_k. If A=max a, then

    1<=r_k<=A,       r_{k+1}=a_k-1/r_k.

On any closed subinterval strictly inside (0,T), a_k>=2+eta for some eta>0.
After one step there, r_k>=1+eta. The positive fixed point lambda_k of this
Riccati map also satisfies lambda_k>=1+eta. Hence, away from the two ends,

    |r_{k+1}-lambda_k|
       = |r_k-lambda_k|/(r_k lambda_k)
       <=rho |r_k-lambda_k|,       rho=(1+eta)^(-2)<1.

Let omega(h) be the modulus of continuity of lambda on the chosen interior
interval. Allowing for lambda_{k+1}-lambda_k gives

    |r_{k+1}-lambda_{k+1}|
       <=rho |r_k-lambda_k|+omega(h).

The sum of these errors, multiplied by h, tends to zero: its transient part is
bounded by O(h)/(1-rho), and its remaining part by O(omega(h))/(1-rho).
Since log is Lipschitz on [1,A], the same is true for logarithms. Riemann sums
therefore give the integral of log lambda on every such interior interval.

The discarded endpoint intervals have total length at most 2 epsilon+O(h).
Both their discrete contribution and the corresponding integral lie between
zero and (2 epsilon+O(h))log A. First let h->0, then epsilon->0. Because

    log g_n = sum_{k=0}^{n-1} log r_k,

we obtain h log g_n -> integral_0^T log lambda. Equation (3.1) finishes the proof.
The omitted final coefficient in the recurrence changes a Riemann sum by O(h).
The proof does not assume a uniform nondegenerate saddle at either endpoint. QED.

### 3.4 The figure-eight knot: a complete example

For K=4_1 take the nonabelian factor

    t(m)=m^4-m^2-2-m^(-2)+m^(-4).

Along m=exp(i alpha/2),

    t(m)=-2 c(alpha),
    c(alpha)=1+cos(alpha)-cos(2alpha),
    c(alpha)-1=(1-cos alpha)(2 cos alpha+1).

Thus sigma=-1, a=2c>=2 on 0<=alpha<=T=2pi/3, with strict inequality in the
interior. The geometric cone family has precisely this Euclidean endpoint, and
Schläfli gives

    Vol(4_1)=integral_0^(2pi/3) arcosh(c(alpha)) d alpha
            =2.02988321281930725004240510854904057... .

The recurrence (3.2) now proves (3.4) for this explicitly normalized quantum
A-curve. In a root-of-unity indexing, let R be divisible by 3 and set n=R/3.
Then h=2pi/R, q_n=exp(-pi i/R), and

    lim_{R->infinity, 3|R} (2pi/R) log |f_{R/3}| = Vol(4_1).     (3.5)

The half-power quantum-torus parameter is declared explicitly: q_n^2 is the
root exp(-2pi i/R). There is no covert factor of two. Formula (3.5) concerns
this cone-transport state, not J_R and not a recurrence asserted to annihilate it.

### 3.5 An infinite alternating family, with its scope made explicit

Let K_r be the connected sum of r figure-eight knots, r>=1. These knots have
alternating diagrams. For r>1 their complements are not hyperbolic; the volume
in this paragraph means the sum of the hyperbolic JSJ-piece volumes, equivalently
the hyperbolic-volume normalization of simplicial volume:

    Vol_JSJ(K_r)=r Vol(4_1).

Define Laurent polynomials t_0=2, t_1=t, and

    t_{r+1}=t t_r-t_{r-1}.

The curve l^2-t_r(m)l+1=0 is a peripheral A-curve factor of K_r. Indeed, the
connected-sum group is an amalgam identifying the meridians. At a generic
semisimple meridian, the longitudes lie in its diagonal centralizer and their
eigenvalues multiply. Taking the same geometric root l_0 in each summand gives
l=l_0^r, and l_0^r+l_0^(-r)=t_r(m). These generic representations extend to the
closure of that peripheral curve. The polynomial is square-free and generically
irreducible: its quadratic discriminant is the figure-eight discriminant times
the square of a nonzero Chebyshev polynomial, so the nontrivial quadratic
extension is unchanged. Thus this curve supplies an actual factor, rather than
just an arbitrary point of the peripheral image.

For completeness, the original discriminant t(m)^2-4 is not a rational square:
it has a simple zero at m=exp(i pi/3), as direct differentiation of t+2 shows.
The Chebyshev square factor at this point is nonzero (its value before squaring
is plus or minus r).

For each fixed r choose the explicit quantum operator

    Ahat_{r,q}=L^2-t_r(M)L+1,

with the same meridian grid and initial data f_0=1, f_1=(-1)^r. On the cone arc,

    t_r(exp(i alpha/2))=(-1)^r 2 cosh(r arcosh c(alpha)).

The Riccati proof of Theorem 3.1 applies verbatim to this coefficient function,
whether or not the composite complement has a global hyperbolic cone metric.
Its limiting integral is r times (3.1) for 4_1. Hence:

**Corollary 3.2.** This specified A-based quantization satisfies

    lim_{n->infinity} (2pi/(3n)) log |f_n^{(r)}|
       =Vol_JSJ(K_r)=r Vol(4_1)                                (3.6)

for every r>=1. No global hyperbolic structure on a composite knot complement
is asserted. This is an infinite family of alternating knots, but it does not
settle an infinite family of prime hyperbolic knots.

There is also a multiplicative quantum definition: take the r-th tensor power
of the original two-dimensional transfer system and the state (f_n)^r. Its
boundary annihilator is obtained by a symmetric-power elimination, and the
volume law is immediately additive. Its classical characteristic polynomial
contains l^2-t_r(m)l+1 along with other connected-sum peripheral components.
This is a distinct finite-q ordering choice; the coincidence of leading volume
rates does not identify the two quantizations.

## 4. A wider positive-matrix criterion

Here is a genuinely higher-order sufficient criterion for quantum curves. It
involves finite matrices that can be checked, instead of assuming the desired
asymptotic in a saddle hypothesis.

**Theorem 4.1.** Let B(s), 0<=s<=T, be a continuous family of d-by-d matrices
with nonnegative real entries, uniformly bounded entries, and diagonal entries
at least c>0. Assume B(s) is irreducible for 0<s<T. Let rho(s) be its Perron
root. For a fixed nonzero v_0>=0 set

    v_{k+1}=B(kT/n)v_k,       P_n=1^T v_n.

Then

    lim_{n->infinity} (T/n)log P_n
       =integral_0^T log rho(s) ds.                              (4.1)

The logarithm of a fixed normalization of v_0 disappears after division by n.

**Proof.** On [epsilon,T-epsilon], choose the positive left Perron vector
p(s), normalized by sum_i p_i(s)=1. Irreducibility gives simplicity of the
Perron eigenvalue and continuity of p. Every component of p is bounded below
by a positive constant on this compact interval. Therefore uniformly in s,

    (1-delta_h)p(s)<=p(s+h)<=(1+delta_h)p(s),   delta_h->0,

componentwise. Since all v_k>=0 and p(s)^T B(s)=rho(s)p(s)^T,

    (1-delta_h)rho(s)p(s)^T v_k
      <=p(s+h)^T v_{k+1}
      <=(1+delta_h)rho(s)p(s)^T v_k.

Multiplying and taking h times logarithms bounds the error by
O(T delta_h), which tends to zero. The p-weighted and ordinary 1-norms are
uniformly comparable on the interior interval.

Let C bound the induced matrix 1-norm. Since B(s)>=c I componentwise,

    c ||v||_1 <= ||B(s)v||_1 <= C ||v||_1     for v>=0.

Endpoint intervals therefore affect h log ||v_n||_1 by at most their length
times max(|log c|,|log C|), plus O(h). Also c<=rho(s)<=C. Removing the endpoint
cutoff proves (4.1). QED.

**How this becomes a quantum A-volume theorem.** Seek a matrix B(m;q), rational
in the peripheral variable and q, whose system

    v(qm)=B(m;q)v(m)

has a geometric classical characteristic factor det(l I-B(m;1)). Along the
chosen cone arc, a declared phase gauge should turn the evolution into matrices
satisfying Theorem 4.1, with log rho=ell/2. A uniform q-dependent perturbation
can be included provided positivity, the diagonal bound, and convergence are
maintained. The same proof then applies using the perturbed Perron vectors on
compact interior intervals.

A scalar q-difference equation can be recovered algebraically when a chosen
observable is cyclic: the rows

    e^T, e^T B(m;q), e^T B(qm;q)B(m;q), ...

become linearly dependent over the rational coefficient field after at most
d+1 rows. At q=1, cyclicity makes its scalar characteristic polynomial the
matrix characteristic polynomial. Clear denominators with care about exceptional
parameters. This gives a concrete construction to test, not an assertion that
every knot A-polynomial admits a positive realization.

For the quadratic example, use the coordinates
(g_{k+1}-g_k,g_k). The transfer matrix is

    B(a) = [[a-1, a-2], [1,1]],

which is nonnegative, has diagonal >=1, and is irreducible when a>2. Its
characteristic polynomial is l^2-a l+1. This independently proves the Riccati
limit above. After the sign gauge it gives the figure-eight A-factor.

This criterion covers an infinite class of matrix/quantum-curve problems, and
Section 3.5 supplies an infinite family of composite alternating knot examples.
For higher-order curves with complex coefficients the following additional
criterion is useful; it does not require a positive matrix realization.

### 4.2 A dominant-root theorem for a normalized quantum-curve norm

Write a monic degree-d A-factor as

    A(l,m)=l^d+a_{d-1}(m)l^{d-1}+...+a_0(m).

Assume its coefficients are analytic on the closed meridian arc
m(alpha)=exp(i alpha/2), 0<=alpha<=T, and a_0 never vanishes there. Let C(alpha)
be the companion matrix, with first row (-a_{d-1},...,-a_0), and ones directly
below the diagonal. Assume:

* all roots are simple on 0<alpha<T;
* the geometric root lambda_1(alpha) is strictly dominant in modulus there;
* the geometric cone family runs from the complete cusp to a zero-volume
  Euclidean endpoint, so that integral_0^T log|lambda_1|=Vol(K).

For Laurent/rational A-factors these are algebraic conditions plus the stated
geometric branch identification. Puiseux expansions imply that eigenvector
bounds and inverse spectral gaps grow at most as powers of the distance to
the endpoints. This polynomial-growth qualification may alternatively be
included explicitly as a hypothesis for a more general analytic curve.

Here is the full quantum definition, including its state. For large n let

    epsilon_n=(log(n+e))^(-2),
    h_n=(T-epsilon_n)/n,
    alpha_k=T-epsilon_n-k h_n,
    q_n=exp(-i h_n/2).

If necessary restrict to n large enough that epsilon_n<T/4. Set

    f_j=lambda_1(alpha_0)^j,     j=0,...,d-1,

and evolve the exactly ordered scalar quantum equation

    [L^d+sum_{j=0}^{d-1} a_j(M)L^j]f=0,      LM=q_n ML.

Equivalently, v_0=(lambda_1^(d-1),...,lambda_1,1)^T and
v_{k+1}=C(alpha_k)v_k. Define the quantum amplitude to be the state-vector norm

    Q_n=(sum_{j=0}^{d-1}|f_{n+j}|^2)^(1/2)=||v_n||_2.           (4.2)

Thus the endpoint of the evolution is exactly the complete cusp alpha_n=0.
The initial point tends to the zero-volume Euclidean end. The norm is part of
this proposed definition: it cannot be substituted silently for a chosen
scalar wavefunction. It avoids cancellation of a single matrix component.

**Theorem 4.2.** Under the preceding hypotheses,

    lim_{n->infinity} h_n log Q_n=Vol(K).                        (4.3)

**Proof.** Stop first at alpha>=epsilon_n. On this truncated interval use the
Vandermonde eigenbasis whose columns are

    V_j=(lambda_j^(d-1),...,lambda_j,1)^T.

Its condition number and derivative, and the inverse modulus gap between
lambda_1 and the other roots, are bounded by powers of epsilon_n^(-1).
In this basis each step, after division by lambda_1(alpha_k), has the form

    w_{k+1}=(I+E_k)diag(1,D_k)w_k,
    ||E_k||<=h_n epsilon_n^(-p) C,
    ||D_k||<=1-gamma_n,       gamma_n>=c epsilon_n^r,

for fixed p,r,C,c, in the maximum norm. The initial vector is w_0=(1,0,...,0).
Put delta_n=C h_n epsilon_n^(-p). Since epsilon_n is a logarithmic cutoff,
delta_n/gamma_n^s tends to zero for every fixed additional power s.

Write w_k=(a_k,b_k). Induction in the projective ratio gives

    ||b_k||/|a_k| <= C' delta_n/gamma_n,

after increasing C': the lower bound for the next first component is
|a_k|(1-O(delta_n)), while the other components contract by 1-gamma_n and
receive O(delta_n)|a_k|. In particular a_k cannot vanish. Also

    log|a_{k+1}/a_k|=O(delta_n)

uniformly on this truncated interval. Summing shows that h_n times the log
of the normalized product is O(h_n epsilon_n^(-p)), which tends to zero.
Changing between the eigenbasis and the original basis costs at most
O(h_n log epsilon_n^(-1)) in the scaled logarithm. Consequently

    h_n log ||v_k||
      =h_n sum_{j<k} log|lambda_1(alpha_j)|+o(1)

up to the lower cutoff. The Riemann-sum error tends to zero by the same
polynomial endpoint bounds.

The remaining interval from epsilon_n to zero has length epsilon_n+O(h_n).
Since C and C^(-1) are uniformly bounded on the closed arc, its contribution
to h_n log ||v_n|| is bounded in absolute value by a constant times that
length. The same holds for the discarded integral; lambda_1 is bounded and
bounded away from zero because a_0 is nonzero. Removing the cutoff proves
(4.3). QED.

This also allows analytic q-corrections a_j(m;q)=a_j(m;1)+O(|q-1|), with
uniform bounds and nonzero leading/constant coefficients on the closed arc.
In the same classical eigenbasis their added one-step error is
O(h_n epsilon_n^(-p)), so the proof is unchanged. The state normalization,
dominant-branch hypothesis, and norm prescription remain essential.

### 4.3 A cubic prime example: the knot 5_2

Put x=m^2. A standard nonabelian factor, up to mirror/peripheral conventions, is

    A_52(l,x)=l^3+b(x)l^2+c(x)l+x^7,
    b=x^5-x^4+2x^2+2x-1,
    c=-x^7+2x^6+2x^5-x^3+x^2.

The companion operator is exactly

    L^3+b(M^2)L^2+c(M^2)L+M^14.

Here its classical symbol, ordering, initial data (Section 4.2), and quantum
amplitude (the norm of three consecutive values) are all explicit.

Dominance can be established algebraically. On |x|=1,

    c=x^7 conjugate(b),

so roots are paired by l -> 1/conjugate(l). A cubic can therefore have at
most one root strictly outside the unit circle. Its discriminant factors as

    Delta=x^4(x-1)^6(x+1)^6 H(x),
    H=x^8-6x^7+11x^6-12x^5-11x^4-12x^3+11x^2-6x+1.

On x=exp(i alpha), let u=x+x^(-1)=2 cos alpha. Then

    x^(-4)H(x)=P(u)=u^4-6u^3+7u^2+6u-31.

Writing v=u-3/2 gives P=v^4-(13/2)v^2-343/16. Its only real root in [-2,2] is

    u_E=(3-sqrt(13+16sqrt(2)))/2,
    T=arccos(u_E/2)=2.4071698135544546... .

Thus there is no discriminant zero for 0<alpha<T. At alpha=pi/2, x=i and
b=-4+3i has modulus 5. If all three roots were on the unit circle, the modulus
of their sum would be at most 3, a contradiction. There is consequently one
outside root there. It remains outside throughout the open interval: crossing
the unit circle would make it collide with its reciprocal-conjugate root and
force a discriminant zero. This proves simplicity and strict modulus dominance
on the whole interval.

The usual geometric cone family of this two-bridge knot identifies this unique
outside root with exp(ell/2+i theta/2). Its Euclidean endpoint must be the
discriminant zero above. The classical cone-existence input supplies the
geometric identification; the displayed discriminant and root-count argument
are independently checkable and are verified symbolically in the script.

Theorem 4.2 therefore proves (4.3) for 5_2 with the explicitly defined norm
state. The classical integral is

    integral_0^T log(max_{A_52(l,exp(i alpha))=0}|l|) d alpha
       =2.82812208833078... .

This is a second prime hyperbolic example. It is a theorem for the stated
cone-normalized quantum-curve norm, not a claim about a pre-existing scalar
invariant. Connected sums can also be treated by tensor-product definitions,
with volume interpreted as the sum over the hyperbolic pieces.

The next prime-family task is to check this root-dominance criterion for
general twist/two-bridge A-polynomials. Higher degree can have several outside
roots, so neither alternation nor reciprocity alone proves it. No theorem for
all twist or two-bridge quantum A-curves is claimed here.

## 5. A broad theorem for a positive angle-state comparison

This second construction explains why a volume limit is much easier once a
positive quantum object has been selected. It is not a substitute for the
operator and gluing requirements in Section 2.

Let T be a finite complete geometric ideal triangulation with t tetrahedra.
Its strict angle polytope P consists of triples (x_j,y_j,z_j)>0 with

    x_j+y_j+z_j=1,
    sum of incident corner variables at each global edge =2.

Variables are measured in units of pi; each pair of opposite tetrahedral edges
has the same variable. Let C x=b be this integer linear system. For N define

    P_N = {k in Z^(3t): Ck=Nb, all k_i>=1}.

The tetrahedral equations imply k_i<=N-2. For 0<=k<N set

    s_N(k)=product_{j=1}^k 2 sin(pi j/N),       s_N(0)=1,
    Z_N(T)=sum_{k in P_N} product_{i=1}^{3t} s_N(k_i)^(-1).      (5.1)

Empty sums are zero. Choose a denominator D for any strict rational point of
P; the theorem is along N in D Z_{>0}. That progression is a necessary lattice
qualification; no claim of nonemptiness at every N is made.

**Theorem 5.1.**

    lim_{N->infinity, D|N} (pi/N)log Z_N(T)=Vol(M).              (5.2)

Equivalently, for the positive comparison amplitude sqrt(Z_N), the factor is
2pi/N. Taking this square root does not establish a linear quantum A-equation.

### Proof: the quantum-factorial estimate

Write Lambda(theta)=-integral_0^theta log(2 sin u)du on [0,pi]. Uniformly for
0<=k<N,

    log s_N(k)=-(N/pi)Lambda(pi k/N)+O(log N).                  (5.3)

For a direct proof, decompose

    log(2 sin pi x)=log x+log(1-x)+g(x),

where g extends smoothly to [0,1]. The sum-integral discrepancy for g is O(1).
For each logarithmic term, Stirling's estimates or monotone integral bounds
give O(log N), uniformly in the terminal index k. This also covers k=0 and
k=N-1; no quantum-dilogarithm continuation is used.

Thus every summand in (5.1) has logarithm

    (N/pi)V(pi k/N)+O(t log N),

where V is the sum of ideal tetrahedral volumes. There are at most N^(3t)
summands. The upper bound in (5.2) follows from max V.

For the lower bound, let x_* be the geometric angles and x_0 a strict rational
point of denominator D. The integer kernel L=ker C intersect Z^(3t) spans the
real kernel, since C has integer entries. For D|N, round N(x_*-x_0) to L with
an error bounded independently of N. Adding Nx_0 produces k_N satisfying the
exact angle equations and k_N/N->x_*. Positivity holds for all sufficiently
large N. Retaining that one positive summand gives the lower bound max V.

### Proof: why the maximum is hyperbolic volume

For one tetrahedron with alpha+beta+gamma=pi,

    V_Delta=Lambda(alpha)+Lambda(beta)+Lambda(gamma).

Its Hessian in alpha,beta is minus

    [[cot alpha+cot gamma, cot gamma],
     [cot gamma, cot beta+cot gamma]].

The first diagonal entry is sin beta/(sin alpha sin gamma)>0, and its
determinant is 1. Hence V_Delta is strictly concave. The sum is strictly
concave on every angle leaf and extends continuously to the compact closure.

At a complete geometric gluing, choose compatible small horospheres at the
cusps. The truncated length of a global edge is the same in each incident
tetrahedron. Schläfli's formula, summed over tetrahedra, gives

    dV=-1/2 sum_e ell_e d(total angle at e)=0

for every variation inside the angle polytope. Contributions from changes of
horospheres cancel because the angles at every tetrahedral ideal vertex sum
to pi. Therefore the geometric point is stationary. Strict concavity makes it
the unique maximum; its tetrahedral volumes add to Vol(M). This completes
the independent proof of (5.2).

The hypotheses include the known geometric triangulations of hyperbolic
two-bridge knot/link complements and pseudo-Anosov once-punctured torus bundles.
This scope uses the geometric triangulations constructed by Gueritaud–Futer,
not a quantum-topology theorem. More generally, the proof applies to any
explicit complete geometric ideal triangulation, irrespective of alternation.

In particular, if T and T' are two complete geometric triangulations of the
same manifold, then on a common allowed lattice progression

    lim (pi/N)log[Z_N(T)/Z_N(T')]=0.

Thus the exponential rate is independent of triangulation, although the
finite-N partition function is not.

### A bare local comparison; boundary factors remain to be determined

The bare local weights do not obey a strict unnormalized 2–3 equality in the
following comparison. Take two regular ideal tetrahedra sharing a face, forming a symmetric
ideal triangular bipyramid. The alternative subdivision has three tetrahedra
with angles (2pi/3,pi/6,pi/6). Boundary equatorial edges have total angle
2pi/3, and the other six boundary edges have pi/3, on both sides. The new
internal edge has total angle 2pi. The three-tetrahedron angle fiber has the
form (2N/3,p,N/3-p) in every tetrahedron, with 1<=p<N/3, in lattice units.
At N=6 there is exactly one strictly positive integral angle state on each
side; no terms of that local sum have been omitted.

At N=6,

    s_6(1)=1,       s_6(2)=sqrt(3),       s_6(4)=6.

The two-tetrahedron weight is s_6(2)^(-6)=1/27; the three-tetrahedron weight
is s_6(4)^(-3)s_6(1)^(-6)=1/216. Their ratio is 8.

This is a normalization diagnostic, not a proof that no topological
interpretation exists. Allowed move identities can carry peripheral or
boundary factors: for example, a product of three factors (1+M^a) would give
8 after M=1, although no such multiplier has been derived for this model.
The test did not retain a symbolic peripheral holonomy or establish a common
boundary trivialization. It therefore cannot decide covariance up to such
factors, projective invariance, or equivalence to a literature model.

The remaining calculation is to specify the boundary quantum space, retain
the peripheral variables before specialization, and derive the full move
identity including its prefactor. The finite-N invariant question remains
open. This qualification does not change the positive-sum volume limit in
Theorem 5.1.

## 6. Exact local quantum identities, proved without a volume claim

There is a useful alternative local rule whose pentagon can be checked
algebraically. Let |q|<1 initially and define

    E_q(x)=1/(x;q)_infinity=sum_{n>=0} x^n/(q;q)_n,
    Psi_q(x)=1/E_q(x)=(x;q)_infinity.

Both have constant term one. Their difference equations are immediate from
shifting the products:

    E_q(qx)=(1-x)E_q(x),
    Psi_q(qx)=Psi_q(x)/(1-x).

If X is multiplication by x and Y shifts x to qx, then YX=qXY and

    [(1-X)Y-1]Psi_q=0.                                        (6.1)

The classical curve is y=1/(1-x), exactly the ideal tetrahedral relation
z'=1/(1-z), with x=z. This proves the local symbol match.

Here is also an exact formal pentagon. If xy=q yx in the completed quantum
plane, then

    E_q(x)E_q(y)=E_q(y)E_q(-yx)E_q(x),                         (6.2)
    Psi_q(y)Psi_q(x)=Psi_q(x)Psi_q(-yx)Psi_q(y).                (6.3)

To check it, q-binomial coefficients give
E_q(a+b)=E_q(b)E_q(a) whenever ab=q ba. Also

    E_q(x)y E_q(x)^(-1)=y E_q(qx)/E_q(x)=y-yx.

Put a=-yx and b=y; then ab=q ba, so
E_q(y-yx)=E_q(y)E_q(-yx). Conjugating the full power series E_q(y) gives
(6.2), and inversion gives (6.3). These formal identities require no contour
argument and no appeal to a Chern–Simons interpretation. The accompanying
script checks them to finite bidegree with exact rational arithmetic as a
separate algebraic verification.

Uniformly on |x|<=r<1, with h=log q tending to zero in a fixed closed sector
|arg(-h)|<=pi/2-eta, eta>0,

    log Psi_q(x)=Li_2(x)/log q+O(1).

This follows from

    log Psi_q(x)=-sum_{r>=1} x^r/[r(1-q^r)].

It does NOT give uniform radial asymptotics on the unit-q axis or through
coalescing poles. In particular, evaluating a compact q-product at a root of
unity is a separate prescription. The manuscript's pole calculation is a
reason to keep this distinction explicit.

## 7. The proposed global conjecture and a usable proof target

There are two coherent choices, with different remaining work.

**A-defined comparison curves.** The direct cone-transfer definition in Sections
3–4 depends on the intrinsic A-curve and a geometric branch/normalization.
For a family of knots, one may construct rational transfer systems with
the correct classical geometric factor and the positivity properties of
Theorem 4.1. The theorem would then establish their volume laws. This route
does not need a claim about a pre-existing quantum invariant or a tensor
pentagon. To meet the current task, however, it must be related to an existing
literature definition by an explicit equivalence, including the state and its
normalization. Different quantizations can have different subleading terms.

**Local topological quantization.** Start instead from (6.1)–(6.3), retain
boundary variables, and give an exact gluing prescription. The target is a
state Z_K and its annihilator Ahat_K for which:

1. quantum gluing is independent of the allowed subdivisions, including the
   state/contour and normalization, not only the formal operator;
2. boundary elimination has precisely the required geometric A-component in
   the classical limit, with extraneous factors controlled;
3. a stated continuation produces a convergent state at the desired q-values;
4. its normalization has no unaccounted exp(c/h) factor;
5. its geometric contribution yields the volume rate without cancellation.

A precise volume conjecture for this latter object, in a growing orientation
and declared h>0 with log q proportional to i h, is

    lim_{h->0+} h log |Z_K(complete cusp;h)|=Vol(S^3 minus K),

with the proportionality fixed from the single-tetrahedron normalization.
A decaying orientation has the opposite sign. The manuscript's equation
(11.24) illustrates why that conversion must be calculated, not guessed.

The constructive next target is hyperbolic two-bridge knots: geometric
triangulations are available, and their rational holonomy descriptions can be
tested for the matrix criterion. Alternating diagrams alone do not yet give
the needed positive transfer system or analytic gluing theorem. Menasco
polyhedra are topological ideal cells; actual right-angled augmented-link
geometry is useful initial data, but requires the Dehn-filling equations to
return to the knot.

## 8. Literature used for context, not as an unchecked quantum proof

* Gueritaud, with an appendix by Futer, *On canonical triangulations of
  once-punctured torus bundles and two-bridge link complements*, Geom. Topol.
  10 (2006), 1239–1284: https://arxiv.org/abs/math/0406242.
* Howie–Mathews–Purcell, *A-polynomials, Ptolemy equations and Dehn filling*,
  Algebr. Geom. Topol. 25 (2025), 1265–1320:
  https://msp.org/agt/2025/25-3/agt-v25-n3-p01-p.pdf.
* Tran–Yadav, *Exact integral formulas for volumes of two-bridge knot
  cone-manifolds*, Transformation Groups (2026):
  https://doi.org/10.1007/s00031-026-09973-z. This supplies geometric
  cone-family context and the figure-eight endpoint, not the recurrence proof.
* Andersen–Malusà, *A Geometric Quantisation view on the AJ-conjecture for the
  Teichmüller TQFT*: https://arxiv.org/abs/1711.11522. The displayed classical
  5_2 polynomial is used as input; its quantum operator or proof is not used.
* Champanerkar–Kofman–Purcell, *Right-angled polyhedra and alternating links*:
  https://arxiv.org/abs/1910.13131.
* Ben Aribi–Wong, *The Andersen–Kashaev volume conjecture for FAMED geometric
  triangulations*, version 2 (2026): https://arxiv.org/abs/2410.10776.
* Ben Aribi–Guilloux–Wong, *FAMED by computer: proving the Andersen–Kashaev
  volume conjecture for 42,000 knots*: https://arxiv.org/abs/2512.17437.
* Liu–Ming–Sun–Wu–Yang, *U_(q qtilde) sl(2;R) Turaev–Viro invariants for
  cusped 3-manifolds* (2026): https://arxiv.org/abs/2608.16560.

The last three papers formulate distinct existing quantum constructions and
report broad volume theorems. Those results are not used to prove any theorem
in this note, and their quantum states are not identified with our definitions.
