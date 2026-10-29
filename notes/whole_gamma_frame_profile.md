# A whole Gamma profile of the actual retained quantum-factorial source

Research proof, 27 October 2026. The exact residual in the actual
balanced-to-symmetric source frame has a uniform whole-function
profile on the N^2-scaled quantum normal. It includes its integer
resonance zeros and all fixed holomorphic jets. A middle-index
residual is also exactly a holomorphic unit times the independently
fixed actual meridian Weyl half-adapter, after a necessary parameter
reparametrization that aligns their zeros.

The opposite profiles multiply to the entire centered meridian
factor already present in the full modified dimension. No growth
assumption on the knot invariant is used. These are actual scalar
source/frame comparisons, not an asserted equivalence of the whole
q-normal and meridian-normal knot modules.

The retained residual is established in
[the exact clock-shear audit](exact_clock_shear_star_automorphism_audit.md)
and [the actual polynomial source](integral_color_global_q_difference_source.md).
The actual meridian half-adapter is the marked rational function of
[the Weyl-gluing theorem](twisted_cotangent_source_and_weyl_gluing.md).

## 1. The actual residual and its marked normal

Put c=2pi*i, n=N-1 and retain the symmetric q-binomial. On the
actual integral-color family the residual after removing the
quadratic clock shear is exactly

    V_(N,j)(q)={N-1 choose j}_q/M^j,
    M=-q^N.                                               (1.1)

Use the whole scaled normal

    H=Log Q=c/N+z/N^2,
    q=exp(H/2), z=ca,
    M=exp(z/(2N)),
    b=a_N=a/(1+a/N).                                     (1.2)

The marking M=-q^N gives the stated exponential since exp(c/2)=-1.
The exact identity H b=z/N is important. All powers N^a below
mean exp(a log N) with the real logarithm of the positive integer.

For every j<N,

    V_(N,j)(a)
      =exp(-Hbj/2)
         product_(r=1)^j
             sinh[H(r-b)/2]/sinh(Hr/2).                  (1.3)

Indeed sinh[H(N-r)/2]=sinh[H(r-b)/2], because HN=c+z/N.
There is no omitted sign. Equation (1.3) is an equality of the
original finite residual, not a model chosen to reproduce its jets.

Set J(x)=2sinh(x/2)/x, J(0)=1. Then (1.3) separates exactly as

    V_(N,j)=exp(-Hbj/2)
       product_(r=1)^j(1-b/r)
       product_(r=1)^j J(H(r-b))/J(Hr).                  (1.4)

Zeros in the first product must not be removed by logarithms.

## 2. Uniform whole-profile theorem

Define the marked chord function for 0<T<1 by

    G(T)=(exp(cT)-1)/c
        =exp(pi*i T)sin(pi T)/pi,
    Log G(T)=log[sin(pi T)/pi]+pi*i T.                   (2.1)

For every compact K in the complex a-plane and every delta>0,
there is C_(K,delta) such that, for all sufficiently large N,

    sup_(a in K, delta<=j/N<=1-delta)
      |N^a V_(N,j)(a)-Phi_a(j/N)|
          <=C_(K,delta) log N/N,                         (2.2)
    Phi_a(T)=G(T)^(-a)/Gamma(1-a).                       (2.3)

The convergence is absolute and locally uniform in complex a.
It includes every positive integer a, where the limiting function
vanishes. It is not a relative-error assertion at those zeros.
In particular if j_N/N->T in (0,1), then
N^a V_(N,j_N)->Phi_a(T) locally uniformly in a.

### 2.1 An elementary Euler-product lemma, including zeros

For b in a fixed complex compact set and j sufficiently large,

    E_j(b)=j^b product_(r=1)^j(1-b/r)
          =1/Gamma(1-b)+O(1/j),                          (2.4)

uniformly and absolutely. One direct proof uses

    (1-b/r)exp(b/r)=1+O_K(r^(-2)).

For r beyond a fixed compact-dependent threshold choose the
logarithm near one. Its tails sum uniformly to O(1/j).
Also sum_(r<=j)1/r-log j=gamma+O(1/j). Therefore E_j converges
at the stated rate to the entire Euler product

    exp(-gamma b)product_(r>=1)(1-b/r)exp(b/r).            (2.5)

The finitely many possible zero factors are kept as factors, so
this proof remains valid at positive integers.

For completeness (2.5) is the reciprocal of the Euler Gamma
function, not an imported asymptotic formula. For Re b<1 repeated
integration by parts gives

    I_j(b)=integral_0^1 t^(-b)(1-t)^j dt
          =1/[(j+1-b)product_(r<=j)(1-b/r)].

After u=jt, dominated convergence gives
j^(1-b)I_j(b)->integral_0^infinity u^(-b)exp(-u)du=Gamma(1-b).
Near zero use a fixed integrable power on each compact subset of
Re b<1; away from zero use (1-u/j)^j<=exp(-u). Thus the entire
product (2.5) agrees with 1/Gamma(1-b) on that half-plane and
defines its entire continuation. This proves (2.4) independently
of a Gamma-ratio or Stirling theorem.

### 2.2 The nonzero J product has a uniform logarithm

For T=j/N in the stated interval, all Hr and H(r-b) stay in a
fixed zero-free neighborhood of the segment c[0,1-delta] once N
is large. Choose L(x)=Log J(x), L(0)=0. Its first two derivatives
are bounded there. Taylor expansion with its uniform remainder
and a Riemann sum give

    sum_(r<=j)[L(H(r-b))-L(Hr)]
       =-Hb sum_(r<=j)L'(Hr)+O(1/N)
       =-b L(Hj)+O(1/N)
       =-a L(cT)+O(1/N).                                (2.6)

The Riemann sum can be integrated along the straight complex
segment from zero to Hj; the same derivative bound gives its
O(1/N) error. Exponentiating proves that the J product is
J(cT)^(-a)(1+O(1/N)), uniformly on K and the indicated interval.

Finally b=a+O_K(1/N),

    N^a j^(-b)=T^(-a)[1+O_K(log N/N)],
    exp(-Hbj/2)=exp(-caT/2) exactly.

Combining these identities, (2.4) and (2.6) proves (2.2), since
T J(cT)exp(cT/2)=G(T). The proof never divides by Gamma^-1
near a resonance zero.

## 3. The profile retains the entire normal resonance data

For fixed T, Phi_a(T) is entire in a. The finite normalized
functions in (2.2) are holomorphic too. Cauchy's formula therefore
gives convergence of every fixed a-derivative on smaller compact
sets. This packages the large root-normal jets in one whole
function, rather than assuming a finite jet controls the source.

The exact numerator zeros are at b=r, equivalently

    a=N r/(N-r), 1<=r<=j.                                (3.1)

They approach the positive-integer zeros of (2.3), but they are
not located exactly at those integers at finite N. At a=-k,
k>=0, the profile is instead

    Phi_(-k)(T)=G(T)^k/k!,
    V_(N,j)(-k)~N^k G(T)^k/k!.                           (3.2)

This is a polynomial source scale in N. No complete knot-growth
assumption appears in either (3.1) or (3.2).

As a check on the known exact first normal,

    partial_a Log V_(N,j)|_(a=0)
       =-log N-Log G(T)-gamma+o(1).                       (3.3)

Since q partial_q=(2N^2/c)partial_a in this normal, (3.3)
agrees with the exact cotangent sum of the clock-shear audit.
The N^2 log N term is real source data, resolved by (2.3).

## 4. The actual meridian Weyl half-adapter has the opposite profile

Keep the actual fixed root Q_N=exp(c/N), and put M(a)=exp(ca/(2N)).
The already specified rational half-adapter is, with its even-level
mark i retained,

    beta_N(M)=(M^2Q_N;Q_N)_L/(Q_N;Q_N)_L, N odd,
    beta_N(M)=[(1+iM)/(1+i)]
                    (M^2Q_N;Q_N)_L/(Q_N;Q_N)_L, N even,
    L=(N-1)/2 odd, L=N/2-1 even.                         (4.1)

It is not a newly normalized scalar: beta_N(1)=1 and the actual
Weyl norm identity fixes it as in the cited gluing theorem.

For each factor there is the exact identity

    (1-exp[H_0(r+a)])/(1-exp(H_0r))
      =exp(H_0a/2)(1+a/r) J(H_0(r+a))/J(H_0r),
    H_0=c/N.                                             (4.2)

Apply the same proof as Section 2 with b=-a, now without the
a_N drift. The even prefactor in (4.1) is 1+O_K(1/N). Thus,
uniformly on every compact complex a-set, including its zeros,

    N^(-a) beta_N(exp(ca/(2N)))
       =G(1/2)^a/Gamma(1+a)+O_K(1/N)
       =Phi_(-a)(1/2)+O_K(1/N).                          (4.3)

The same whole Gamma half-profile is therefore derived separately
from an actual q-normal frame and an actual fixed-root meridian
source adapter. No logarithm of a vanishing factor is used.

## 5. An exact finite scalar source bridge aligns their zeros

There is a stronger comparison before taking any limit. Let
H,b be as in (1.2), choose L as in (4.1), and put

    M_tilde=exp(-H_0 b/2).

Define the explicit unit

    u_N(a)=exp[-(H-H_0)bL/2]
       product_(r=1)^L
          J(H(r-b))J(H_0r)/[J(Hr)J(H_0(r-b))],           (5.1)

and at even N divide its right-hand side by
(1+iM_tilde)/(1+i). Then exactly

    V_(N,L)(a)=u_N(a) beta_N(M_tilde).                    (5.2)

All J factors in (5.1) are units on fixed compact a-sets for
sufficiently large N: their arguments remain near c[0,1/2],
which misses the first nonzero J zero. The even prefactor is
a unit near M=1. In particular (5.2) is valid through integer
resonances; it was not defined by dividing its two vanishing
sides. It has u_N(0)=1 and

    u_N=1+O_K(1/N)                                       (5.3)

locally uniformly and holomorphically.

Proof: in (1.4), take j=L. The corresponding beta product
has the exact factorization

    exp(-H_0bL/2)product_(r<=L)(1-b/r)
                         J(H_0(r-b))/J(H_0r),

times the even prefactor if appropriate. The zero polynomial
product cancels as a common factor of the two expressions;
what remains is precisely (5.1). For (5.3), H-H_0=O_K(N^-2).
The exponent in (5.1) is O(1/N). The logarithm of each J cross
ratio is also O_K(N^-2), by differentiating the bounded smooth
difference L(H(r-b))-L(Hr) with respect to H. Summing L terms
is O(1/N). The even prefactor differs from one by O(1/N).

The reparametrization b=a_N is essential. Comparing directly
to beta_N(exp(-H_0a/2)) would put its zeros at a=r, while
the q-normal frame zeros are (3.1). A claimed uniform unit ratio
without that adjustment would be false near integer zeros.

This is an exact holomorphic scalar source-line comparison with
its origin mark, phase, zeros and unit all specified. It is not
an intertwiner of the full q-normal and meridian-normal knot
states, their quantum clocks, or their selected regular parts.

The [full-head source theorem](full_head_gamma_source_transport.md)
extends this comparison to every color by using the complementary
actual Weyl chart in the upper half. Its comparison unit is
uniformly I+O(1/N) in any common diagonal metric, including
the resonance divisors. Its source and dual fractional lattices
are retained; the potentially singular source factors themselves
are not declared units.

The same coordinate also matches the retained central power,
with the meridian reflection explicit. On the integral-color
leg M_col=exp(Hb/2), while M_tilde=exp(-H_0b/2). Therefore

    chi_H(M_col)=exp[-2c Log(M_col)/H]
                 =exp(-cb)=M_tilde^(2N).                 (5.4)

Here chi_H is the geometric whole flux character of
[the Gauss-wall calculation](gauss_wall_flux_and_actual_peripheral_character.md).
The target inverse-power character is its reciprocal, as required
by the opposite meridian orientation. Equation (5.4) matches
specified scalar characters; it does not assert that this
geometric lift is an unspecified off-root auxiliary-matrix center.

## 6. Opposite profiles give the exact universal meridian function

The actual finite Weyl scalar is

    c_N(M)=N M^(N-1)/S_N(M^2),
    beta_N(M)beta_N(M^(-1))=c_N(M)^(-1).                 (6.1)

At M=exp(z/(2N)), the exact centered inverse norm is

    H_N(z)=c_N(M)^(-1)
          =sinh(z/2)/[N sinh(z/(2N))].                   (6.2)

It has its removable entire values at the apparent common zeros.
On each fixed compact z-set it tends uniformly, with O(N^-2) error,
to H(z)=2sinh(z/2)/z. Multiplying the two limits in (4.3) therefore
proves independently

    Phi_a(T)Phi_(-a)(T)
       =1/[Gamma(1-a)Gamma(1+a)]
       =sin(pi a)/(pi a)
       =H(ca),                                          (6.3)

for every T in (0,1), with entire continuation at all a. The T
factors cancel. In particular the actual c_N tends meromorphically
to Gamma(1-a)Gamma(1+a), locally uniformly away from its poles.
Its inverse and the beta norm converge to the entire H. This
orientation is retained.

For completeness the finite norm input to this reflection identity
does not require a published proof. At odd N pair residues r and
N-r in the beta factors; their numerator is the full product
(M^2Q;Q)_(N-1)=S_N(M^2), and their denominator is N with the
displayed phase. The leftover M power is M^(-(N-1)), giving
(6.1). At even N the unpaired residue is Q^(N/2)=-1; its factor
is supplied exactly by

    (1+iM)(1+i/M)/(1+i)^2=(1+M^2)/(2M).

The same product argument gives (6.1). These are the actual marked
finite identities already audited in the gluing construction.

The entire difference identities are

    G(T)Phi_(a+1)(T)=-a Phi_a(T),
    (a+1)H(c(a+1))=-a H(ca).                             (6.4)

They follow from the Gamma recurrence and hold even at their zeros;
ratio notation would exclude those points. These rank-one shifts
agree with the retained inverse meridian-norm half-step character.
The half-adapter with a->-a has shift factor G(T)/(a+1).

The [centered regular-profile theorem](scaled_meridian_regular_profile.md)
keeps H_N and the whole knot-dependent regular part separately.
Equality of the universal factor (6.3) does not identify that
regular part or prove a growth or convergence theorem for it.

The subsequent [full-head source transport](full_head_gamma_source_transport.md)
extends the finite comparison to every head index, using the actual
Weyl complement in the upper half. The interior profile here is
unchanged; a naive upper prefix would introduce different zero
divisors and is not that source extension.

## 7. Coverage and precise novelty

A repository search found earlier factorial-frame periods and
normal jets, but no existing derivation of (2.2), (4.3), or the
zero-preserving actual comparison (5.2). The Gamma reflection
factor itself is classical, not a new identity. For background
coverage, [Iritani's survey](https://arxiv.org/abs/2307.15938)
uses it in Gamma-class factorizations and integral flat-section
structures. That coverage is not used as a proof or as an
identification of this knot source with quantum cohomology.

The contribution here is the independent whole-function derivation
from the actual retained q-binomial residual, its uniformity through
the shifted integer resonances, and its exact marked unit comparison
to the already fixed actual meridian half-adapter. These statements
do not assume the volume conjecture or any K_N growth hypothesis.

The [audit](../experiments/audit_whole_gamma_frame_profile.py)
checks finite hyperbolic factorizations, zero alignment, the exact
unit, both parities of the actual beta norm, uniform compact profiles
and the paired entire function. The
[independent normal-profile audit](gamma_residual_normal_profile_independent_audit.md)
also checks the whole zero-preserving unit and its uniform bound.
