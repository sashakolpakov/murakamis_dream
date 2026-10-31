# The original beta current is a geometric extension, not a degenerate sector

28 October 2026. The retained current has an exact triangular connection.
Its power-series symbol is rational, but its logarithmic continuation
can carry the SAME nondegenerate geometric full-Psi block as the residue.
Thus a current in a full knot expansion cannot be declared geometrically
degenerate from its local leading symbol alone. The complete original
source is the invariant section of a rank-two extension.

All identities below use the original polynomial B_N and the exact
source cycle in
[the beta-source theorem](actual_trivalent_quantum_beta_source.md), with
the [proved normalizer](actual_trivalent_beta_normalizer.md). They do
not introduce a different positive invariant or inserted coupon.

The [audit](../experiments/audit_actual_beta_current_connection_and_monodromy.py)
and [results](../experiments/actual_beta_current_connection_and_monodromy_results.json)
check the commuting source-preserving matrices, seven normal-jet
orders, nine actual full-Psi deck laws, eighteen Ward laws and six
differential identities. The all-level proofs below do not infer
their claims from those finite checks.

## 1. The exact extended state

Put h=2*pi*i/N, Q=exp h, u=exp l, v=exp(l+c). Initially take

    -pi<Im l<0, 0<Im c<pi.

The original state and source are

    B_N(u,v)=sum_(a=0)^(N-1) product_(j<a)(u-Q^jv),
    U=u^N, V=v^N, A=U-V, D=1-A,
    S_N(l,c)=(N/phi_N) exp(Nl-cl/h)
                         Psi_+(c)Psi_+(h-l),
    B_N=S_N+D I_N.                                      (1)

I_N is the UPWARD Barnes line of the cited theorem, including its
actual source residues. It is holomorphic and uniformly bounded on
compact subsets of this initial positive boundary chamber, including
the matched D=0 locus. Formula (1) defines its actual continuation
elsewhere with the transported logarithmic marks. Apparent divisions
by D below are always removable in this initial matched chamber;
they must not be inverted separately on every continued branch.

## 2. Exact inhomogeneous Ward system

The two original finite recurrences and exact Psi steps give

    S_N(l,c)=(u-v) S_N(l,c+h),
    I_N(l,c)=(u-v) I_N(l,c+h)+1,                         (2)

    v S_N(l+h,c)=(u-1) S_N(l,c),
    v I_N(l+h,c)=(u-1) I_N(l,c)+1.                       (3)

The equations are literal on a common convergence chamber, and hold
under continuation with its residue currents. They do not permit
shifting a bare Barnes line across poles without those currents.
Combining them, the u-only root shift is

    v S_N(Qu,v)=(u-1)(Qu-v)S_N(u,v),
    v I_N(Qu,v)=(u-1)(Qu-v)I_N(u,v)+Qu.                  (4)

The +1 and +Qu are fixed original endpoint sources, not unspecified
knot periods. The central D is invariant under each root shift.

There is also an exact differential connection. Write
p(Z)=d_Z Log Psi_+(Z), a meromorphic function explicitly given in
the original full-Psi source note. Put

    q_c=-l/h+p(c), q_l=N-c/h-p(h-l).

Then d_c S_N=q_c S_N, d_l S_N=q_l S_N. Differentiating the original
invariant (1) gives the safe cross-multiplied form

    D d_c I_N+NV I_N=d_c B_N-q_c S_N,
    D d_l I_N-NA I_N=d_l B_N-q_l S_N.                   (5)

No localization at a vanishing D is needed. Off that divisor, let
J_N=B_N/D. The entire connection is equivalently

    d(I_N-J_N)=d Log(S_N/D) * (I_N-J_N).                 (6)

Thus the inhomogeneous source is explicit and rational in the
marked root coordinates u,v (not only their central powers U,V);
its homogeneous line is precisely the original
geometric full-Psi line. The connection is flat, since
d_l q_c=d_c q_l=-1/h. This calculation does not classify its
nonperturbative sectors from a formal asymptotic series.

## 3. Both boundary deck generators and their commutator

Let T=2*pi*i. Under a v-only logarithmic deck turn c->c+T,
the full-Psi monodromy and the Gaussian in (1) give exactly

    S_v=S/A, I_v=I-S/A.                                (7)

For the simultaneous u,v deck turn l->l+T, c fixed, they give

    S_s=(U-1)S/V, I_s=I+S/V.                           (8)

Therefore a u-only turn l->l+T,c->c-T gives

    S_u=A(U-1)S/V, I_u=I+U S/V.                        (9)

These are meromorphic connection formulas with the full central
factors retained. They are first established away from their displayed
divisors, then interpreted by the matched total source. For example
A=0 can make the individual continued terms singular although the
polynomial B_N remains regular.

For the column (S,I)^t, the v and simultaneous matrices are

    M_v=[[1/A,0],[-1/A,1]],
    M_s=[[(U-1)/V,0],[1/V,1]],
    M_u=[[A(U-1)/V,0],[U/V,1]].                         (10)

They obey M_v M_s=M_s M_v and M_u=M_s M_v^(-1). Thus both
boundary deck generators commute, with their actual extension cocycle;
there is no untracked central commutator. Direct multiplication shows

    [1,D]M_v=[1,D]M_s=[1,D]M_u=[1,D].                  (11)

The literal original source B_N=S+D I is their invariant section.
On the balanced locus A=1, all three diagonals are one and their
nonidentity parts square to zero. This is a genuine unipotent rank-two
extension, not a claim of nilpotence of the full knot transport group.
Generically the same extension also has nontrivial multiplicative norm
characters; those characters cannot be discarded.

More generally an arbitrary v deck of order m and simultaneous deck
of order n have the exact solved transport

    mu=A^(-m)[(U-1)/V]^n,
    S' =mu S, I'=I+[(1-mu)/D]S.                        (12)

Since mu=1 on D=0, the quotient is regular there and tends to
-m+n/V. For the normal-jet ring modulo D^(p+1), write M=Id+L.
Then L^k=(mu-1)^(k-1)L and therefore L^(p+2)=0. Every fixed normal
jet has finite unipotent transport, with the full all-winding answer
already given by (12). For an individual v deck the index p+2 is
attained. This statement concerns the proved local deck connection,
not every change of charts in a knot triangulation.

Away from D=0 the gauge (S,I)->(S,B=S+D I) diagonalizes these
matrices. Its determinant is D. Thus this splitting is invalid on
the balanced source divisor itself; it cannot be used to discard
the nontrivial unipotent extension or its normal derivatives.

The geometric line span(S) is preserved, but the decomposition into
an invariant original source and a current is not preserved as two
independent scalar sectors. This is the precise failure of a proposed
global proof that excludes every current term before its continuation.

## 4. A regular growing geometric sector inside a continued current

Consider a compact original gap family with |u|<|v| and

    Lambda(u,v)>max(0,log|u|,log|v|),

where Lambda is the exact residue rate in the normalizer theorem.
Such genuine positive bipyramid families exist near |v|=1 and lower
u with |u|<1. The principal current is O(1), whereas S grows with
its specified full-Psi geometric phase. On this chamber

    1/A=-v^(-N)[1+O((|u|/|v|)^N)].

Equation (7) therefore gives

    I_v=I+v^(-N)S[1+O((|u|/|v|)^N)].                   (13)

Since Lambda-log|v|>0, the continued current has a nonzero growing
geometric sector. Its added phase differs from S only by the integer
logarithmic mark -2*pi*i Log v. Their exponentiated canonical relations
are the SAME and the geometric shapes remain regular. This conclusion
uses an exact current connection and a checked rate gap; it is not
inferred merely from a nonzero local density.

An especially transparent fixed-center example is u=-i,v=1 along
N=4m+1. Then A=-1-i stays nonzero and the principal I is bounded,
while the current after the v deck has exponential rate

    lim_(m->infinity) (2*pi/N)log|I_v(-i,1)|=2D(i)>0.   (14)

The underlying positive bipyramid has p=q=2+i, H=1-2i and two
outputs i,i. All five signed shapes are strictly nondegenerate.
The source and all physical centers are unchanged by the logarithmic
turn; B_N is exactly invariant by (11). This is a local original-source
countercheck to automatic geometric degeneracy of retained currents.
It is NOT a counterexample to a global knot volume statement, nor a
claim that a particular full knot cycle must perform this deck turn.

## 5. Exponentially small geometry is also present in the current extension

There is a second exact description in the open contraction chamber
|u|+|v|<1. Its infinite Newton series

    H_N(u,v)=sum_(a>=0) product_(j<a)(u-Q^jv)

converges absolutely and normally. The integer relation
P_(a+N)=A P_a shows

    H_N=B_N/(1-A)=B_N/D,
    I_N=H_N-S_N/D.                                    (15)

No tail or boundary source has been omitted. The single-valued analytic
series H_N stays fixed; the full-Psi block produces precisely the
current deck jumps (7)--(9).

For u=-4i/5,v=1/100 from the positive-bipyramid example in the
beta-source theorem, the exact residue rate is strictly negative:

    Lambda=[ImLi_2(i/80)+ImLi_2(4i/5)]/(2*pi)
                                      +(1/4)log(1/125)<0.

The imaginary dilogarithms are each less than their positive imaginary
arguments; this bounds their sum by 65/80, while the logarithm is
strictly negative by a fixed larger margin. Thus the full current
contains the explicitly specified exponentially small term -S_N/D
in (15). Its rational power-series symbol cannot determine this sector
or its deck continuation. The source identity, rather than a chosen
formal series, is needed for exterior composition.
This is a specified exact source decomposition, not a claim that
H_N itself has no further exponentially small components or that a
unique transseries convention has been proved for it.

### The principal normalization symbol to every power

On every compact subset of the initial positive boundary chamber,
the actual current has an asymptotic expansion to every fixed order

    I_N(u,v)=sum_(k=0)^K h^k R_k(u,v)+O_K(h^(K+1)),
    R_0=1/(1-u+v),
    R_k=(u-v)/(1-u+v) sum_(j=1)^k
                            (v*d_v)^j R_(k-j)/j!.       (15a)

All coefficients are rational, with poles ONLY on 1-u+v=0 and
pole order at most 2k+1. The first correction is the one already
independently derived in the beta theorem. Equation (15a) follows
formally from the exact inhomogeneous Ward equation (2); the actual
uniform remainder requires the contour estimate as well.

Here are details supplying that estimate to every fixed order. The
full-Psi logarithm has a complete fixed-order expansion on compact
subsets of its selected strip. In a left-half-plane anchor this is
proved directly: its noncentral logarithmic Fourier coefficient is

    -exp(nZ)/[n(1-Q^n)], N not dividing n.

For n below a fixed small multiple of N, expand 1/(exp(hn)-1)
to the required Bernoulli order. The remainder is bounded by a
fixed power of |hn|, whose sum against exp(n Re Z) is convergent.
The remaining modes and the explicit central logarithmic terms
are exponentially small. To continue to an arbitrary compact
selected-strip set, use the EXACT finite derivative formula
sum_(ell=0)^(N-1)g_Z(ell/N) in equation (7b) of the full-Psi source
note. Its g_Z is holomorphic on a common neighborhood of [0,1].
Euler--Maclaurin to any fixed order has a uniform remainder there;
integrate it from the already normalized anchor. Cauchy estimates
give the same derivative bounds. This proves the needed full-Psi
expansion with its actual normalization, not a formal periodic
replacement.

In the Barnes integral, cut |Im a| at C log N, choosing C sufficiently
large for the requested order. The already proved strict exponential
tails make the omitted part smaller than that order. On the retained
part the expansion of the ratio at c and c+ha has polynomial
coefficients in a and a uniformly bounded remainder times a fixed
power of 1+|a|. Taylor's formula and the exponential contour majorant
then permit termwise integration with an O(h^(K+1)) remainder.
Each coefficient is an ordinary Barnes moment of (u-v)^a, hence
a rational derivative of 1/(1-u+v). Uniqueness of the recursion
identifies it with (15a). Differentiation in u,v is uniform on smaller
compact sets by holomorphy.

There is a precise formal bubble geometry: on 1-u+v=0 the two
shape arguments are x=v/u=1-y, y=1/u, and

    D(x)+D(y)=0.                                      (15b)

This justifies calling the FORMAL rational current a normalization
or bubble channel in this chart. It does not classify the exact
current: (7)--(15) display its additional geometric continuation
and exponentially small sectors. In particular a formal pole
calculation cannot replace the rank-two source connection.

## 6. What this settles for the next global step

The normalization-current symbol and exact Ward equations are now
available for whole-word composition. A global proof may use the
invariant rank-two extension and its matched currents, or prove that
its particular physical cycle avoids specified deck transfers. It
cannot prove the needed gap by declaring every current sector a
degenerate representation: (13)--(14) would contradict that assertion.

The remaining geometric question is about the ACTUAL joint original
cycle, its permitted branch transport, and the exterior stationary
equations. None of the local identities above supplies a global
geometric quotient or forces its coefficient to be nonzero.

## 7. Why killing the current is not a source-preserving deck quotient

There is a concrete algebraic obstruction, stronger than observing a
continued current with a large rate. Work over a ring R of single-valued
meromorphic boundary functions on a regular marked chart, with A and D
units. The logarithmic deck transformations fix R. Use the ACTUAL source
presentation with generators S,I and its pointing B=S+D I. This is
meromorphic deck descent data, not a claim that its variable coefficient
matrices are constant monodromy matrices of a complex local system.

Put J=D I. Equation (7) gives

    T_v(S)=S/A, T_v(J)=J-(D/A)S.                       (16)

Let pi be an R-linear quotient whose kernel is stable under this
actual deck transport. If pi kills the current J, it also kills
T_v(J)-J. Since D/A is a unit, it follows that

    pi(S)=0, pi(B)=0.                                  (17)

Thus a nonzero invariant geometric quotient cannot be constructed by
simply quotienting out this current. This uses the original polynomial
pointing and its exact full-Psi deck law; no arbitrary replacement
period or unknown knot scalar is introduced.

Without inverting D, the same calculation forces D pi(S)=0. Hence
a D-torsion-free quotient still kills S and B. A quotient supported
on the balanced divisor, its derived normal source, or a comparison
which is not deck-equivariant is a different object. The normal jets
of Section 3 must not be discarded to identify those alternatives.

The quotient here is taken over the REMAINING boundary variables
before their period pushforward. A final exterior integral is not
R-linear in a variable which it integrates. Hence (17) does not say
that a particular integrated current can never vanish while a
geometric integral survives. It excludes setting the current KERNEL
to zero in a pointwise, deck-compatible comparison; nonlocal cycle
cancellation after the exterior integration is a separate question.

There is no assertion here that every local v turn is an allowed
independent deck transformation after all boundary variables have
been coupled. That is checked by the actual monomial boundary map.
The following coupled version makes the required check explicit.

## 8. Disjoint original sink fibers and their coupled descent presentation

In the original reduced atomic graph, an eligible beta sink has
three incident atoms, all pointing into it before factorial reflection:
one reciprocal factorial, one positive Euler transfer, and one positive
factorial. Its finite coefficient contraction is exactly B_N from (1).
Two such sinks cannot share an atom: an oriented incidence column has
only one positive entry. Since neither sink is an original boundary
cap vertex, no cup/cap factor has been removed by this observation.

Consequently a family of s eligible sinks can be contracted
simultaneously at the finite-coefficient level. The local result is
the product of their B_N kernels with the SAME remaining original
boundary functional. The sums are finite, so no contour interchange
or independent-sector convergence is assumed for that identity.
Its expansion into S_i+D_i I_i is pointwise exact on their common
marked boundary chart.
The exact u=Q^2U,v=QV tags and reflected NQ^d source factors are
those of the beta-source theorem; each stays in its specified kernel
or exterior density, according to that representation. None is reset.

Eligibility matters: an original U/u/F sink is not the U/v/F beta
kernel. BEFORE exact Gaussian absorption, the strict nine-atom
crossing has the proved star {0,1,3} for either sign and additionally
{2,4,6} for a negative crossing. The final raw star {5,7,8} contains
a u transfer. For a positive crossing, however, the original finite
Gaussian and its adjacent reciprocal diagonal combine EXACTLY by
d_a/F_a=p_a*x^(-2a). Slot 5 is thereby a V diagonal, and {5,7,8}
becomes a second genuine beta star, disjoint from {0,1,3}. This is
an identity of the COMPLETE original finite Gaussian operator, not
a pointwise removal at fixed continuous Gaussian variable. Thus each
sign has two simultaneous eligible beta stars after this exact
preprocessing, with the remaining adapters retained. Their literal
whole-word monomials and Gaussian grouping belong to the original
crossing assembly; they cannot be guessed from only the local shape
relations.

For each selected beta sink form its rank-two presented descent
module M_i with the matrices of Section 3. Pull these modules back
by the ACTUAL boundary monomials in the remaining head/Gaussian
variables, and tensor them:

    M_presented=tensor_(i=1)^s M_i,
    b=tensor_(i=1)^s(S_i+D_i I_i).                       (18)

This has a rank-2^s presentation. Its evaluation into actual functions
may have further relations after boundary coupling; faithfulness is
not inferred. Its pointing evaluates to the original product of
finite B_N kernels. It has not been defined from the final knot value.

The first guaranteed sink gives a literal check on this pullback.
Label the single-crossing boundary/head coordinates as in the original
nine-atom graph, with the sink z_2 and its neighbors z_0,z_1,z_4.
Its reciprocal leg, positive Euler leg and positive factorial give
the finite coefficient product

    (z_2/z_1)^i/F_i,
    p_j(x^(-1)z_2/z_0)^j,
    F_a(z_4/z_2)^a.

The z_2 constant coefficient forces a=i+j and is exactly

    B_N(u_0,v_0),
    u_0=z_4/z_1, v_0=x^(-1)z_4/z_0.                    (18a)

Thus a local z_0 logarithmic turn has a=0,b=-1 in the notation
below, and its beta character is A_0=u_0^N-v_0^N, generically
different from one. The nontrivial individual characters in (20)
therefore occur in an ACTUAL crossing boundary map. In a whole word
that head can also enter other sinks or source factors; all their
pulled-back transformations must be composed. Equation (18a) does
not assert that the local v turn is independent of those changes.

For a particular head logarithmic turn, let the actual boundary map
shift Log u_i by 2pi*i*a_i and Log v_i by 2pi*i*b_i. In (12) this
means n=a_i and m=b_i-a_i. Thus each beta factor has its explicit
character mu_i and current coefficient from that formula. Tensor
the corresponding matrices. They preserve (18), and their
geometric/current sectors mix by these specified coefficients.
Untouched full-Psi factors, Gaussian and peripheral/source lines
must carry their OWN descent factors as well; no conclusion about
the full graph character follows from the beta factors alone.

One useful falsification criterion applies directly to this coupled
presentation. Localize where every D_i and mu_i is a unit, and put
J_i=D_i I_i. Suppose a deck-stable quotient kills EVERY tensor sector
containing at least one J_i. Under an allowed head turn,

    S_i -> mu_i S_i,
    J_i -> J_i+(1-mu_i)S_i.                              (19)

Apply the turn to the sector with precisely its ith factor J_i and
all other factors S_j. Modulo the killed sectors its image is

    (1-mu_i) product_(j!=i)mu_j * product_j S_j.          (20)

If any such 1-mu_i is a unit, the quotient kills the entire geometric
product and therefore the original pointing b. It is not enough that
the PRODUCT of the mu_i equals one: individual current sectors still
mix into that product by (20). If all relevant characters are one,
or one restricts to their fixed-character divisors, this obstruction
alone decides nothing; the retained normal jets and exterior source
still have to be computed.

Equations (18)--(20) specify a source-preserving composition object
and a check against an invalid quotient. They do not make the
individual sector integrals single-valued on the original head torus.
On overlapping logarithmic charts the FULL tensor descent data, and
the matched source seams, are compulsory. Nor does the nonzero
meromorphic product of local residues imply that its FINAL exterior
period is nonzero. That remaining pairing is precisely what a global
geometric coefficient theorem must control.
