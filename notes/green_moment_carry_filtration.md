# Actual Green moments: a bounded carry extension and an exact Fock jet map

Research proof, 27 October 2026. The polynomial moments in the full
scalar Green certificate have an exact bounded triangular carry
complex. Its graded differential is the **coefficient monodromy**;
it is not zero in general. Actual integer-index moments also have
an exact Newton/Fock normal-ordering map, and the Mellin relative
source has a finite endpoint-preserving normal-jet complex.

These constructions do not identify the remaining geometric Green
boundary with zero. In particular a top divided-monodromy row is
not the original marked cut or its full higher normal jet.

## 1. The actual Green currents have bounded logarithmic degree

Let `h` be the fixed least moment degree of the actual global
certificate. In
[the full Green formula](full_certificate_framing_boundary.md),
every current is a finite sum of terms

    A_beta(M,T_M) p(k) D^gamma I,
    degree p<=h,

with the literal shifted finite coefficient array retained. After
transverse Gaussian contraction, divide only by the recorded common
Gaussian generator and its base line. The result belongs to

    sum_(|alpha|<=h) K_geo((H)) ell^alpha,        (1)

where `ell` is the finite list of logarithms of the actual critical
flow characters. This is an all-order bound on logarithmic degree.

Proof: an internal finite shift changes the coefficient by a proper
rational ratio and changes `p` by a polynomial of the same degree.
Write every actual index as its chosen logarithm divided by `H`.
Taylor expansion about the critical point differentiates a polynomial
in these logarithms and cannot increase its degree. Wick contractions
and formal division by the unit Gaussian amplitude have algebraic
coefficients in the same common field. A meridian shift changes a
critical logarithm by its original logarithm plus a formal series
with algebraic coefficients; it also preserves the degree bound.
Its common exponential/base ratio is kept, as in the normal-period
calculation. The fixed negative H orders of the moment are retained.

The common algebraic field is finite over the marked geometric/frame
field. After a fixed algebraic cover makes a chosen loop return all
algebraic branches, continuation shifts the critical logarithms by
specified integral multiples of `2pi*i`. Thus the logarithmic part
of (1) is unipotent of length at most `h+1` for that loop. Before
passing to that cover, its algebraic coefficient monodromy must
also be retained.

This statement concerns the actual **formal Green images**. It does
not say that the entire zero-extended finite coefficient array is
a unipotent monodromy module.

## 2. The exact triangular carry complex keeps the coefficients

For one chosen carry coordinate let `P_h` be polynomials in `k`
of degree at most `h`. Let `M` be the actual coefficient-current
module and `C` its carry transport. The total carry is

    T_total=exp(N partial_k) tensor C.

Use the Newton basis `b_j(k)=binom(k/N,j)`, `0<=j<=h`. Translation
by `N` sends `b_j` to `b_j+b_(j-1)`. With `L b_j=b_(j-1)`,

    T_total-I=I tensor(C-I)+L tensor C,
    L^(h+1)=0.                                  (2)

Therefore the two-term current complex with differential `T_total-I`
is a finite triangular extension of `h+1` copies of the coefficient
complex `M --(C-I)--> M`. This is the correct bounded carry complex.
It applies termwise to the actual polynomial-times-coefficient
decomposition above. Tensor Newton bases give the multivariable
version, with the actual commuting carry transports retained.
If coefficient/moment relations are present, this is the explicit
moment presentation mapping equivariantly onto the actual current
module; those relations are retained in the quotient. No linear
independence of polynomial moments on a finite support is assumed.

Only when `C=I` do its invariants consist of constant polynomials
and its cokernel consist of the top Newton degree. For an arbitrary
coefficient transport one has the exact expansion

    (T_total-I)^h
      =sum_(r=0)^h binom(h,r)
                    L^r tensor C^r(C-I)^(h-r).                (3)

Terms with `r<h` are the coefficient-monodromy correction, not
discardable scalar factors. In particular even the divided h-th
power need not land in the coefficient-horizontal constant line.

For actual zero-extended finite arrays the stronger obstruction is
elementary. Translation by `N` minus identity is injective on the
space of finite-support arrays: a finite-support periodic array is
zero. Hence none of its positive powers kills a nonzero such array.
Multiplying by a polynomial moment does not change that fact.
Consequently polynomial degree alone cannot make the **full actual
array** carry nilpotent. One must either pass to the specified
formal continuation (1), or retain the coefficient complex in (2).

## 3. Actual index moments are number operators in the common Fock source

In the actual common Verma basis write an edge index as `a=rN+j`.
The Fock operators are `B=partial_t,T=t`, with
`v_(rN+j)=h_j t^r/r!`. Its actual index multiplication is therefore

    n_a=j+N T B.                                (4)

It is not multiplication by `T/(2pi*i)`. Under
[the exact Mellin map](fock_cyclic_normal_mellin_map.md),

    T -> u=Log U, B -> nabla=U partial_U,
    n_a -> j+N u nabla.                         (5)

This distinction applies to the Green currents themselves: each free
flow index is either an edge index or an integral difference of
adjacent crossing edge indices. Multiplication by its polynomial is
thus a polynomial in the corresponding commuting edge-number
insertions, on the appropriate sides of the actual crossing kernels.
No quantum-group intertwining of that insertion is presumed.

There is nevertheless an exact bounded conversion on coherent
kernels. For every degree-h polynomial `p`, Newton interpolation
gives

    p(j+Nr)=sum_(m=0)^h binom(r,m) Delta_N^m p(j),
    Delta_N p(a)=p(a+N)-p(a).

Since `binom(TB,m)exp(st)=(st)^m exp(st)/m!`,

    p(n_a) theta_s(h_j)
       =theta_s(h_j) sum_(m=0)^h
                          Delta_N^m p(j) (sT)^m/m!.           (6)

On the normal side this is the literal identity

    M[p(n_a)theta_s(h_j)]
       =epsilon_j U^s sum_(m=0)^h
                          Delta_N^m p(j) (su)^m/m!.           (7)

Thus actual number moments do map to bounded logarithmic polynomials
times the coherent kernel, with their full lower triangular terms.
The map is not the false substitution `n_a=j+u/(2pi*i)`.

Set `c=2pi*i`. Physically `U=A^N`, `H_N=c/N`, so
`k=Log A/H_N=u/c` on the chosen logarithmic lift, up to the
marked residue label. Choosing the coherent anchor `s_*=1/(cN)`
in (7) gives the exact polynomial transform

    B_(N,j)p(x)=sum_(m=0)^h Delta_N^m p(j) x^m/(m! N^m),
    x=u/c.                                      (8)

It is unitriangular by polynomial degree, comparing with `p(j+x)`:
its highest coefficient is the same. Lower terms can contain
positive powers of `N`, so the transform is exact rather than an
asymptotically identity adapter. Products of these transforms give
the bounded multiedge map for the actual flow moments. In particular
the step-N falling factorial has the exact image

    M[product_(r=0)^(m-1)(n_a-j-rN) theta_(s_*)]
                           =(u/c)^m M[theta_(s_*)].

This is a linear current/kernel map, not a multiplicative map of
its scalar polynomial images. For example the image of `n_a^2`
is `(j+x)^2+N x`, while the square of the image of `n_a` is
only `(j+x)^2`.

The physical whole clock gives a sharper test. Since `a=rN+j`,

    exp(H_N n_a)theta_s=Q^j theta_s,

whereas ordinary exponentiation of the proposed coordinate image
would give

    exp[H_N(j+u/c)]=Q^j exp(u/N)=Q^j alpha(U).

Thus the bounded polynomial conversion does not intertwine the
literal whole clock `A` without its additional normal/star adapter.
After rescaling by `H_N`, some fixed-degree corrections become
small for fixed `u`; this is not uniform at the geometric scale
`u=N Log A`, which is generally of order `N`. No whole-function
or geometric gluing comparison is inferred from (8).

All coherent anchors have `pi_0 theta_s=I`; the original finite cut
is retained. The marked relative source path is `s->s+1`, so its
endpoint ratio remains `U`, independently of choosing `s_*`.
Choosing an anchor does not rescale `T` or replace that endpoint.
The actual coherent crossing changes the source parameters, so
moving a moment through a crossing differentiates its finite kernel
coefficients as well. These Leibniz terms, of order at most `h`,
must be retained. Equations (4)--(7) specify their operator order.

## 4. The marked relative source has an exact finite normal-jet complex

Take the actual Mellin source differential and transgression

    delta_U f=((partial_sigma-u)f,f(0),f(1)),
    L_U(a,b_0,b_1)=integral_0^1 exp(-sigma u)a(sigma)dsigma
                                      -exp(-u)b_1+b_0.

For a coefficient germ regular at `u=0`, take its normal jets
`f_n=(partial_u^n f)|_(u=0)`, `0<=n<=h`. Let `E_h` be the
jet vector space and define the nilpotent triangular operator

    (T_h f)_n=n f_(n-1), f_(-1)=0.

The actual jet differential is exactly

    (delta_h f)_n=(partial_sigma f_n-n f_(n-1),
                                      f_n(0),f_n(1)).        (9)

The jet map from `delta_U` to (9) is strict: this is just the
Leibniz formula for `partial_u^n(u f)` at zero. Its transgression is

    (L_h(a,b_0,b_1))_n
      =integral_0^1 sum_(j=0)^n binom(n,j)(-sigma)^(n-j)
                                                    a_j(sigma)dsigma
        -sum_(j=0)^n binom(n,j)(-1)^(n-j)b_(1,j)+b_(0,n).     (10)

This is `partial_u^n L_U|_0`. In particular the endpoint-U carry
survives as every displayed binomial term at the second endpoint.
Replacing it by just `-b_(1,n)` is incorrect.

Conjugation by the finite matrix `exp(-sigma T_h)` reduces (9)
to the ordinary relative polynomial complex. It follows directly
that `L_h delta_h=0`, the inclusion is `exp(sigma T_h)f`, and
`L_h i_h=I`. This is an actual finite triangular relative-source
complex, with top cohomology `E_h`; it uses no asymptotic hypothesis.

It is a normal-jet complex, not a finite-dimensional Weyl
representation. `partial_u` needs the next jet to act on the last
component. One must not impose `[B,T]=I` on a fixed finite jet
space; its trace would give the impossible equation `0=dim E_h`.

The original finite-rank coupon is the zero-jet row
`Gamma(f)=[tau(f)]_(u=0)`. Higher rows are `Gamma nabla^j`.
They are distinct source data, as in the Mellin theorem. Whole
coefficient projection `tau(f)1` is not substituted for `Gamma`.
Both reduced and literal pivot lifts remain paired with their
inverse defect lifts; each product is exactly the original `e`.

## 5. The proposed top-monodromy row has a computable extra term

For a constant coefficient polynomial `p(k)=a_h k^h+...`,

    Delta_N^h p/(h! N^h)=a_h.                   (11)

For the actual moment `binom(k,h)`, this row is `1/h!`, not one.
The moment-normalized row is instead `Delta_N^h/N^h`, which sends
`binom(k,h)` to one. Products of the corresponding factorials are
required for multivariate moment indices.

Even if a coefficient function has trivial loop monodromy, its
normal derivatives need not vanish. Let `f(u)` be such a whole-normal
coefficient and keep `c=2pi*i`. The power-normalized Fock normal row
on the candidate coordinate polynomial has the exact value

    Gamma [c^h partial_u^h/h!][p(u/c)f(u)]
      =sum_(r=0)^h c^(h-r)p^((r))(0)/(r!(h-r)!)
                                            Gamma(nabla^(h-r)f). (12)

Its `r=h` term is the top polynomial-monodromy row. All `r<h`
terms are the explicit coefficient-normal-jet correction. Equations
(9)--(10) transport these extra rows with the correct endpoint carry.
Equations (6)--(8), rather than an uncorrected coordinate replacement,
must first be used for the actual index-number moment.

In particular, after that actual Newton conversion the averaged
power-normalized row is explicitly

    R_(h,p)(f)
      =(1/N)sum_(j=0)^(N-1)sum_(r=0)^h
          c^(h-r) Delta_N^r p(j)/[r!(h-r)! N^r]
                              [nabla^(h-r) f_j]_(u=0).       (12a)

Here `f_j` retains the whole coefficient germ, including any
coherent unit and kernel/pivot factors. Thus (12a) computes the
bounded additional coefficient-current rows for the actual
polynomial moment, rather than assuming them horizontal. It is
applied at each relevant edge/side of the kernel; derivatives
through a crossing obey the literal Leibniz rule. If a coefficient
is not regular at the normal point, its specified Laurent finite
part and polar source must be kept instead of silently applying
the regular-jet formula.

Finally the full Green equation has `A_alpha I` in **polynomial
degree zero**. A top-degree projection for `h>0` kills that term.
It therefore cannot by itself preserve the moment repair or prove
that all its carried currents vanish. The lower extension maps in
(2), and the full endpoint rows in (10), are indispensable.

## 6. A singular coherent anchor repairs the whole clock sector

There is a useful exact whole-function extension of the polynomial
conversion, with an equally explicit source defect. Keep `Q` near
its marked root, put `z=Q^N`, and set

    s_Q=1/[N(z-1)], G_Q(u)=exp(s_Q u).

The actual whole index clock acts under Mellin by

    Q^(n_a)=Q^j D_z, (D_z f)(u)=f(zu).

Consequently the exact conjugated operator is

    G_Q^(-1) Q^(n_a) G_Q
                  =Q^j exp(u/N) D_z.            (13)

For every integer `m` its m-th power is

    Q^(mj) exp[(z^m-1)u/(N(z-1))] D_(z^m).      (14)

The quotient is regular at `z=1`, including negative `m`, and the
limit is multiplication by

    Q_N^(mj) exp(m u/N)=A^m.

Thus the **whole Laurent clock algebra** has a regular operator
limit at this irregular coherent anchor. This is stronger than a
finite polynomial symbol identity. On any fixed normal-jet space
its matrices have regular coefficients by (13)--(14).

The other operators retain explicit counterterms:

    G_Q^(-1)B G_Q=nabla+s_Q,
    G_Q^(-1)n_a G_Q=j+N u nabla+u/(z-1).        (15)

The Weyl commutator remains one. An actual degree-h Green moment
therefore has pole order at most `h` from this insertion. If
`p(a)=a_h a^h+...`, then

    [(z-1)^h G_Q^(-1)p(n_a)G_Q]_(z=1)=a_h u^h.

This rescaling cannot be applied to the Green equation and then
forgotten: for `h>0` it also kills a regular degree-zero operator
term `A_alpha I` on the wall. Coefficient/excursion counterterms
must be retained when deciding its finite part.

### The actual finite source projector is not regularized automatically

The gauge commutes with `partial_sigma-u`, its relative
transgression, and the endpoint `U`. The finite cut **row** satisfies
`Gamma G_Q=Gamma`, because `G_Q(0)=1`. However its finite-rank
projector transforms as

    G_Q^(-1) Gamma G_Q=exp(-s_Q u) Gamma.        (16)

Its image/source-one section has n-th normal jet `(-s_Q)^n`.
These are poles of order `n`; equality of the zero-jet normalization
does not identify this source with the constant vacuum. The whole
coefficient projector `f->tau(f)1` does commute with `G_Q`; it is
not the finite-rank `Gamma` in (16).

The remaining normal source row is explicit:

    [nabla,exp(-s_Q u)Gamma]
      =-s_Q exp(-s_Q u)Gamma-exp(-s_Q u)Gamma nabla.           (17)

Thus on the finite jet complex (9) the irregular source is the
specified triangular jet vector `((-s_Q)^n Gamma)_(n<=h)`, with
the full endpoint terms of (10). It is not an unspecified anomaly,
but it has not been shown to cancel against the actual kernel
coefficients. The whole-clock regular limit alone is therefore not
a regular pointed-source or knot-period limit.

## 7. The two-wall coefficient curvature must accompany this limit

For the actual common Verma source, the compressed braid differs
from the ambient head-to-head braid by the specified term
`delta w H_beta`. Here `delta=1-Q^N=1-z`, so `s_Q=-1/(N delta)`.
An r-th coherent-source coefficient can therefore turn a nominal
`delta w` excursion into `delta w s_Q^r`. Its order is not fixed
by the polynomial moment degree alone. One may not set both walls
to zero before computing these terms at the singular anchor.

The source complex (9)--(10), the finite vacuum jets (16), and
the actual coefficient/current transport must be used together.
They keep precisely the data that a bare top divided-monodromy
row or an ordinary cyclic specialization would erase.

## 8. Exact gain and remaining comparison

The actual Green currents now have a proved bounded logarithmic
filtration, a coefficient-sensitive triangular carry complex, an
exact number-moment/coherent-kernel conversion, and a finite normal
jet relative-source map with every endpoint coefficient specified.
These are concrete current/source constructions, not a statement
that nilpotence alone solves the transport.

They do not identify the Gaussian coefficient germs with their
actual whole-source specializations at all retained cut roots.
Nor do they suppress the coefficient carry `C-I` of the finite
zero-extended arrays. The remaining contribution is exactly the
coefficient-monodromy terms in (3), the coefficient-normal jets in
(12), the marked endpoint sum in (10), and the irregular finite
vacuum/excursion terms (16)--(17), applied to the actual Green
currents. Their geometric source image has not been computed or
shown to cancel. A nonzero sourced full geometric period and the
geometric factor of the actual full scalar operator remain unproved.

[Exact current/source audit](../experiments/audit_green_moment_carry_filtration.py)
and [results](../experiments/green_moment_carry_filtration_results.json)
verify actual Green binomial moments through degree six, their
step-N falling factorials, all coefficient normal-jet terms,
the relative endpoint complex, whole clock powers at the irregular
anchor, and the finite-vacuum projector defect. These are universal
operator/jet identities, with no knot-by-knot checks.
