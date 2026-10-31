# The actual source cannot descend by a raw finite critical-algebra quotient

28 October 2026. There is a precise algebraic obstruction to using
the new exact sewing as an exact multiplicative quotient onto a
fixed geometric critical algebra while retaining every coupon.
The original cut pairing is faithful. Moreover an insertion which
vanishes on the geometric critical scheme can still have the FULL
volume exponent in an actual hyperbolic-knot period.

The latter is proved below for the original figure-eight source:
its geometric polynomial p(Z)=Z^2-Z+1 has

    N * mu_N(p(Z)p(Z^-1))/K_N -> 2pi sqrt(3).      (1)

Thus the critical relation costs a power of N, not a smaller
exponential action. This changes the needed construction: a
geometric critical algebra must arise through a specified formal
or derived reduction with Gaussian counterterms and source degree,
rather than by an exact raw source-preserving algebra quotient or
by discarding all insertions of smaller exponential order.

## 1. A perfect cut excludes every proper exact algebra quotient

Let C be a finite algebra over a field and let tau:C->k have
nondegenerate pairing (x,y)->tau(xy). If an algebra quotient
pi:C->A carries the same co-source, tau=lambda pi, then pi is
injective. Indeed for x in ker pi and every y in C,

    tau(xy)=lambda(pi(x)pi(y))=0,

and nondegeneracy gives x=0. The same proof works over a ring
when the displayed pairing is perfect.

The [actual projective cut theorem](integral_projective_cut_duality.md)
applies this hypothesis to

    C_(b,R)=End_(E,F,K)(V_M^(tensor b)), R=k[[M-1]],
    tau=d_N(M) times the original pivotal first cut.

Its pairing is perfect over R and on the complete fibre, with
rank N^(2b-3) for b>=2. Thus there is no proper exact quotient
of this full coupon algebra through which that whole source
factors. Exact sewing and basis changes do not alter the
conclusion, since they retain the original cut.

The statement also survives the normal direction. Modulo u^(J+1),
u=M-1, the R-linear trace pairing remains perfect. Even the
scalar top-normal co-source

    lambda_J(c)=[u^J]tau(c)

has nondegenerate k-pairing lambda_J(cd): choose the lowest
nonzero u coefficient of c, pair it nontrivially by tau's
special-fibre perfect form, and multiply the other input by
the complementary power of u. Hence an exact algebra quotient
preserving this co-source and all normal coupon products is
again injective. Retaining divided sources does not justify
semisimplifying their algebra.

This excludes a SPECIFIC strong construction. It does not exclude
a derived pushforward, a source-compatible corner or restricted
insertion algebra, or an action-normalized associated graded.
Such constructions must state which operations and currents they
retain. Boundary Ward homotopies need not be algebra quotients.

## 2. An actual complete-colour nilpotent source survives

There is a small exact model inside the original crossing.
At N=2 take q=i, Q=-1, x=i in the original balanced frame:

    K=diag(i,-i), F=[[0,0],[2,0]], E=[[0,1/2],[0,0]].

Use the original coproduct and normalized Casimir Omega. On
two heads it is exactly

    Omega=[[0,0,0,0],
           [0,4i,-4,0],
           [0,-4,-4i,0],
           [0,0,0,0]],   Omega^2=0, Omega!=0.

The full two-head centralizer is k[Omega], of dimension two.
With the original averaged first-cut Phi and closed pivot
(-i,i), direct contraction gives

    Phi(1)=0, Phi(Omega)=-4,
    Gram_(1,Omega)(Phi(xy))=[[0,-4],[-4,0]].      (2)

Multiplying by the original modified dimension d_2(1)=i/2
retains perfection and makes the offdiagonal entries -2i.
The reduced classical Casimir point Omega=0 forgets exactly
the nonzero source in (2). For the normalized actual crossing
R_0=1+(i/4)Omega one has Phi(R_0)=-i. Its nilpotent term is
essential, even though all characters of k[Omega] send it to zero.

This persists in a full original hyperbolic-knot check. On
three heads form the original figure-eight word

    W=R_(1)^+ R_(2)^- R_(1)^+ R_(2)^-

in its operator-action order. Its writhe is zero, so the
crossings' common Cartan factors cancel. With both original
closed pivots and the original first-cut average, exactly

    Phi_3(W)=5, Phi_3(1)=0.                       (3)

Replacing each local crossing by its value at Omega_i=0
would give zero instead of five. This replacement is not a
proved algebra map of the global word; (3) shows precisely
why that local-character substitution cannot represent the
original source. No arbitrary source or renormalized model
was introduced.

There is a second exact local-to-global warning. At every N,
Tr(g)=0 for the complete-colour pivot. Therefore, for an
actual local coupon X,

    Phi_(b+1)(X tensor I)=Phi_b(X) Tr(g)=0.        (4)

A nonzero local sourced class can be killed by the original
global pivotal closure. Nonzero local sine jumps, nonzero
Fourier coefficients or nonzero local radial symbols do not
by themselves imply a nonzero global geometric image.

## 3. The exact original figure-eight insertion algebra has rank N

Use its proved [whole-source identity](figure_eight_whole_source_identity.md):

    K_N=sum_(n=0)^(N-1)w_(N,n),
    w_(N,n)=|(Q_N;Q_N)_n|^2>0.

On this EXACT reduced whole-source expression retain the
literal insertion Z=Q_N^n. Define

    mu_N(f)=sum_n w_(N,n) f(Q_N^n),
    A_N=C[Z,Z^-1]/(Z^N-1).                      (5)

No change of the unweighted period is made: mu_N(1)=K_N.
Every weight in (5) is nonzero. Root evaluation identifies
A_N with C^N and its pairing mu_N(fg) with a diagonal
pairing whose entries are those weights. It is nondegenerate.
Consequently Section 1 applies: no proper multiplicative
quotient of A_N retains all these literal inserted moments.
In particular no quotient of uniformly bounded rank can do so.

This remains true if the proposed relation has N-dependent
coefficients. If mu_N(p q)=0 for every Laurent polynomial q,
then p(Q_N^n)=0 for every n. Its representative in A_N is
zero, or equivalently p is divisible by Z^N-1. For degrees
less than N a nonzero relation is impossible.

This is an exact whole hyperbolic-knot source calculation,
stronger than checking an unrelated identity insertion or
changing a normalized source functional. It does not assert
that (5) is already the geometric critical observable of a
different polarization.

## 4. The geometric relation retains the full exponent

Let p(Z)=Z^2-Z+1. Its two roots are the complete regular ideal
shapes. The actual positive source has its unique bulk maximum
at x_*=5/6, Z_*=exp(5pi*i/3), also a root of p. Nevertheless

    mu_N(p(Z)p(Z^-1))>0                           (6)

at every N, and its exponential rate is the SAME as K_N.
Since p has real coefficients and |Z|=1, the insertion in
(6) is |p(Z)|^2=(2cos(2pi*n/N)-1)^2.

Here is a quantitative proof. Put

    Phi(x)=integral_0^x Log(4sin^2(pi*t))dt,
    lambda=-Phi''(5/6)=2pi sqrt(3).

The endpoint-aware factorial estimate gives the uniform
central expansion

    w_(N,n)=2N sin(pi*x) exp(N Phi(x))(1+O(1/N)),
                                                x=n/N,

on every compact subinterval of (0,1). Away from x_* the
already proved strict maximum gives an exponential gap.
Under xi=sqrt(N)(x-x_*), the normalized sums therefore
converge, including their second moments, to the real
Gaussian of variance 1/lambda. This follows directly by
Taylor expansion, a Gaussian bound on a fixed central
neighborhood, and the outside exponential estimate.

For g(x)=|p(exp(2pi*i*x))|^2,

    g(x_*)=g'(x_*)=0, g''(x_*)/2=12pi^2.

Thus discrete Laplace evaluation gives the exact limit

    N mu_N(g)/K_N ->12pi^2/lambda=2pi sqrt(3).    (7)

In particular

    lim N^-1 Log mu_N(g)=Vol(4_1)/(2pi),

although g belongs to the ideal of the geometric critical
polynomial. A vanishing of finite order at the saddle loses
only powers of N. The same argument gives the full exponent
for every fixed nonzero polynomial insertion |f(Z)|^2, even
when it vanishes at Z_*.

Therefore an associated graded which discards ONLY smaller
exponential rates cannot impose p(Z)=0 while retaining this
source. The ordinary semiclassical H-adic leading symbol does
impose that relation, but its next Gaussian contractions and
normal/divided co-source remain necessary: (7) records one
of the terms it would otherwise erase.
Here H=Log Q is the quantum semiclassical direction; it is
not the distinct meridian normal U-1. A source comparison
must retain both rather than identify their filtrations.

## 5. A constructive exact current module in the SAME original source

The correct relation can be exhibited without guessing a critical
quotient or dividing by the unknown scalar. Put

    A(Z)=2-Z-Z^-1=(1-Z)(1-Z^-1),
    S_Q f(Z)=f(QZ), B_Q=A(QZ) S_Q.

The actual weights in (5) satisfy

    w_(n+1)=A(Q^(n+1))w_n, w_0=1, w_N=0.

Consequently telescoping the original finite sum gives, for every
Laurent polynomial insertion f, EXACTLY

    mu_N((I-B_Q)f)=f(1).                         (8)

The endpoint value on the right is compulsory. For example the
left side for f=1 is one, rather than zero. This is an affine
q-difference/Green identity with the original endpoint source,
not an ideal relation for the multiplication algebra.

There is also a unique completely algebraic realization. On the
finite clock A_N one has S_Q^N=I and

    B_Q^N=product_(l=1)^N A(Q^l Z)
         =(1-Z^N)(1-Z^-N)=0.

It follows that

    mu_N=ev_(Z=1)(I-B_Q)^-1
        =ev_(Z=1)sum_(k=0)^(N-1)B_Q^k.           (9)

Evaluation of the k-th term is exactly w_k f(Q^k), proving
that (9) uses the original period, not an adapter normalized
by K_N. Equation (8) uniquely determines this functional.

At the classical limit Q=1 its operator has multiplication
symbol

    1-A(Z)=Z+Z^-1-1=p(Z)/Z.                     (10)

Thus the finite geometric algebra really does appear, but as
the principal symbol of a sourced DIFFERENCE OPERATOR. Away
from the root set Q=exp(H). Its next formal term contains the
Euler derivative, so integration by parts produces higher
Gaussian contractions. It is precisely those terms that make
(7) compatible with the classical critical relation (10).

Equations (8)--(10) supply an actual nonzero affine source
object with fixed operator data and exact endpoint pointing.
They do not prove a general geometric trace descent. They
show concretely which category permits the desired reduction:
relative twisted difference/de Rham cohomology, with its
boundary current, rather than the raw multiplicative algebra.

## 6. The resulting next construction target

The irreducible trace nonvanishing theorem requires an ACTUAL
descended critical algebra and source. The exact sewing and
its regularized periods do not yield it by taking a raw
multiplicative quotient: Sections 1--3 forbid that operation
on the full faithful source objects. Taking the final matrix
Ward cohomology first instead leaves only its scalar pointed
line, rather than a new nontrivial geometric field action.

The appropriate test is therefore on the partly integrated
weighted/current module, BEFORE final scalar Ward closure:
construct its action-normalized formal or derived critical
observable, with the required Gaussian counterterms, and map
the original relative sewing and meridian-normal co-source
through that reduction. A literal flow observable need not
satisfy its critical polynomial there; (7) shows the required
counterterms are already visible at order 1/N.

The existing [formal insertion construction](actual_pointed_commutant_and_critical_observable.md)
provides such a renormalized critical observable on the
transverse FORMAL block. The still-missing step is its
source-compatible whole/derived realization from the exact
sewn period. This is a sharper requirement than finding
another local nonzero unit. The lemma and original-source
calculations above do not prove that realization, but rule
out two tempting constructions and specify which source
information it must retain.

[Exact source and scaling audit](../experiments/audit_actual_source_quotient_critical_relation.py)
and [saved results](../experiments/actual_source_quotient_critical_relation_results.json).
