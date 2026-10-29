# A fixed compact algebraic period for the actual finite source

Research proof, 27 October 2026. The actual finite head admits an exact
coherent-kernel calculus on one fixed algebraic surface. Its normalized
trace is a period over a fixed compact sphere. Products, index moments,
both wall terms, and all finite crossing words are retained. The
physical large-level symbols have the same Gauss coordinates and
symplectic form as the actual classical holonomy calculation.

The coherent-state calculus is standard coverage; for example
[Alexanian--Pinzul--Stern](https://arxiv.org/abs/hep-th/0010187) discusses
coherent symbols, star products and the sphere measure. No proof from
that paper is used here. The statements below give their exact
normalizations for our actual balanced head and its source. No new
knot invariant or replacement positive state is defined.

The geometric contribution to the selected period is still unproved.
In particular a compact cycle does not by itself select the geometric
internal stationary point or bound its full quantum contraction.

## 1. The fixed surface, line, and cycle

Put n=N-1 and use the actual head basis e_0,...,e_n. For an arbitrary
matrix A define

    K_A(w,z)=sum_(i,j=0)^n w^i A_ij binom(n,j) z^j,
    sigma_A(w,z)=K_A(w,z)/(1+wz)^n.                (1.1)

This map is injective. It is the matrix pairing of the row (w^i)
with the column (binom(n,j)z^j), whose identity pairing is

    K_I(w,z)=(1+wz)^n.

Globally K_A is a section of O(n,n) on P1 times P1. Write

    D={s_0 t_0+s_1 t_1=0}, X=(P1 times P1) minus D.

Thus sigma_A is a global regular algebraic function on X. In the
displayed affine chart D is 1+wz=0. Define the algebraic two-form

    omega_A=-(1/(2pi*i)) K_A(w,z) dw wedge dz/(1+wz)^(N+1)
           =sigma_A omega_I,
    omega_I=-(1/(2pi*i)) dw wedge dz/(1+wz)^2.     (1.2)

The scalar 2pi*i records the period normalization. The underlying
forms without that scalar are algebraic over the matrix coefficient
field. The form omega_I is independent of N. The O(n,n) degree
makes (1.2) a global meromorphic two-form with poles only on D.

The fixed compact cycle is

    Gamma={w=v,z=bar(v)}, including the point at infinity.

It is an oriented real sphere, disjoint from D. On its finite chart,
dw wedge dz=-2i d(area v). Hence exactly

    integral_Gamma omega_A
      =(1/pi) integral_C K_A(v,bar(v))/(1+|v|^2)^(N+1) d(area v)
      =Tr(A)/N.                                  (1.3)

To prove the last equality integrate the angle first, killing i!=j.
For i=j use r=|v|^2 and the beta identity

    integral_0^infinity r^j/(1+r)^(N+1) dr
        =j!(n-j)!/N!=1/[N binom(n,j)].            (1.4)

Repeated integration by parts proves (1.4), starting with j=0.
In particular integral_Gamma omega_I=1. The whole period and its
normalization are specified before any local asymptotic expansion.

This cycle computes the actual normalized cut on every diagonal
matrix: the original coupon e_ij=1/N satisfies Tr(eA)=Tr(A)/N
there. Every original one-cut state array is diagonal term by term
by total-index conservation. Inserting any transfer-index or cut-index
moment preserves this property. Thus the original selected knot
scalar and the weighted finite arrays used by the full Green
certificate use precisely this compact trace period. Equality with
Tr(eA) is not asserted for an arbitrary off-diagonal A.

The [whole weighted-word/current map](relative_word_green_transport.md)
realizes these arrays by transfer-coupled actual crossings and
Euler weight derivatives. It supplies the explicit least-moment
Green currents and their relative endpoint transport, including
every internal head projector. Hence the compact cycle here
applies to that entire actual current family, not only its
unweighted scalar specialization.

## 2. Exact composition preserves the entire word

The same beta pairing gives the identity of polynomial kernels

    K_(AB)(w,z)=(N/pi) integral_C
         K_A(w,bar(v)) K_B(v,z)/(1+|v|^2)^(N+1) d(area v). (2.1)

Indeed a middle index j contributes binom(n,j) twice as appropriate
and the pairing (1.4) removes the middle binomial factor, leaving
the coefficient of AB. The factor N in (2.1) is essential.
Tensor products use product measures; the actual pivotal matrices,
turns, framing factors and crossing weights stay inside the kernels.
Iteration therefore represents every finite actual crossing word,
including all source constraints, without changing its value.

There is also a finite algebraic star product with no integrals in
its definition. Set d=1+wz and introduce centered parameters a,b:

    z_b=(z+b)/(1-wb), w_a=(w+a)/(1-za).

Then

    sigma_(AB)(w,z)
      =sum_(r=0)^n (n-r)!/[r! n!]
          [partial_b^r sigma_A(w,z_b)]_(b=0)
          [partial_a^r sigma_B(w_a,z)]_(a=0).      (2.2)

The one-variable expressions differentiated here are polynomials of
degree at most n. For example

    sigma_A(w,z_b)=d^(-n) sum_(i,j)
                   w^i A_ij binom(n,j)(z+b)^j(1-wb)^(n-j).

For a proof of (2.2), at w=z=0 the derivatives extract
r!binom(n,r)A_(0,r) and r!B_(r,0); the displayed coefficient
makes their product A_(0,r)B_(r,0). At any other point the change
of basis induced by

    (1/sqrt(d))*[[1,-w],[z,1]] in SL2

reduces the identity to the origin. Its dual projective coordinate
changes are precisely w_a,z_b. The result is independent of the
square-root sign and hence a rational identity on X.

Thus sigma is an algebra isomorphism onto its finite symbol space
equipped with (2.2). The trace is cyclic for this exact star product.
In particular ordinary multiplication of clock symbols must not be
substituted for star multiplication: sigma_clock star-powered N
times is 1 because the actual clock has N-th power I.

## 3. A global rational primitive for every traceless source

This period has an explicit algebraic source contraction. Let

    J_0 e_j=j e_j, J_- e_j=j e_(j-1).

Direct differentiation of (1.1) gives

    sigma_[J_0,B]=V_0 sigma_B, V_0=w partial_w-z partial_z,
    sigma_[J_-,B]=V_- sigma_B, V_-=partial_w+z^2 partial_z. (3.1)

These are global vector fields on P1 times P1, preserve D, and
preserve omega_I. For V_- this follows from
V_-(1+wz)=z(1+wz) and divergence(V_-)=2z; the two terms cancel.
The verification for V_0 is immediate.

For any A put tau=Tr(A)/N and decompose

    A-tau I=A_off+A_diag, Tr(A_diag)=0.

Define B_off by (B_off)_ij=A_ij/(i-j) for i!=j and zero diagonal.
Define B_diag to have only raising entries

    (B_diag)_(j+1,j)=[sum_(k=0)^j(A_kk-tau)]/(j+1), j<n.

Then exactly

    A-tau I=[J_0,B_off]+[J_-,B_diag].             (3.2)

For the diagonal identity, its j-th entry is
(j+1)b_j-jb_(j-1); the last entry uses the trace-zero condition.
Combining (3.1)--(3.2) and Cartan's formula proves

    omega_A-tau omega_I=d eta_A,
    eta_A=sigma_(B_off) iota_(V_0)omega_I
                      +sigma_(B_diag) iota_(V_-)omega_I.     (3.3)

Every term is a global rational form on X, not a primitive defined
only on a framing chart. Stokes' theorem on the actual compact
Gamma proves its zero pairing. Equation (3.3) is a whole algebraic
cohomology identity specifying exactly the coefficient selected
by the cycle. It does not estimate that coefficient as N grows.

This differs from discarding every divergence on an affine chart:
omega_I has period one and cannot be globally exact on X. A local
primitive for it necessarily fails to extend or has boundary/period
data. The compactification retains precisely that distinction.

### The source cohomology is one fixed algebraic line

The surface itself is a smooth affine quadric. Under the Segre
embedding write the four coordinates as (a,b,c,d), with ad-bc=0.
On X normalize a+d=1. Then

    h=2a-1, e=2b, f=2c, h^2+ef=1.               (3.4)

Conversely these formulas recover all four coordinates and the
point of X. On Gamma, h is real and f=bar(e), giving the unit
real sphere h^2+|e|^2=1.

Every global regular algebraic two-form on X has some finite pole
order m on D in P1 times P1. The space of such forms with pole
order at most m is the section space of

    Omega^2(mD)=O(m-2,m-2).

For m<2 it is zero. For m>=2 set n=m-2; its every section is
exactly the form (1.2) for one (n+1)-dimensional matrix, with the
inessential common normalization removed if working over Q.
Equation (3.3) therefore proves on this affine surface

    H^2_dR(X)=k[dw wedge dz/(1+wz)^2].             (3.5)

The generator is not exact because its compact period is -2pi*i.
No comparison theorem or dimension count is needed for this top
cohomology calculation: the explicit primitive covers every form.
This is a fixed source cohomology line, not the full Bloch regulator
of the knot. The latter is still carried by the knot's coefficient
transport and its selected large-level class.

The contraction also has a uniform norm bound. Give the original
head the positive metric G_jj=1/binom(n,j). On Gamma, sigma_A is
the expectation of A in its normalized coherent vector for this
metric, so |sigma_A|<=||A||_G and |tau|<=||A||_G. The constructed
matrices obey

    ||B_off||_G<=(pi/2)||A||_G,
    ||B_diag||_G<=2||A||_G.                       (3.6)

For the first bound there is the exact Fourier inverse

    B_off=(1/(2pi))integral_0^(2pi) i(theta-pi)
                    exp(i theta J_0) A exp(-i theta J_0)dtheta.

Its nonzero m-th Fourier coefficient is 1/m and its constant
coefficient is zero. These conjugations are G-unitary, and the
average absolute weight is pi/2, proving the bound. For the
second, the trace-zero prefix sum S_j can be bounded from either
end, giving |S_j|<=2min(j+1,n-j)||A||_G. The raising entry changes
the orthonormal basis by sqrt((j+1)/(n-j)); hence its magnitude is
at most 2min(j+1,n-j)/sqrt((j+1)(n-j)) times ||A||_G, at most
2||A||_G. A one-step weighted shift has norm the largest magnitude
of these entries. The vector fields and omega_I are fixed smooth
tensors on Gamma. This source contraction therefore has no
large-level norm loss in the same coherent metric. That metric
can be exponentially conditioned relative to the original Euclidean
basis; no crossing-word norm bound or absence of scalar cancellation
is inferred from (3.6).

## 4. Both actual wall terms are whole functions in this calculus

Use the finite balanced head, with Q=q^2 and kappa=M-M^(-1):

    K e_j=-(M/q)Q^(-j)e_j,
    Ecal e_j=(M Q^(-j)-M^(-1))e_(j-1), j>0,
    Ecal e_0=0,
    F e_j=(1-Q^(j+1))e_(j+1), j<n, F e_n=0.

These are the actual finite auxiliary matrices off the root, with
their known wall defect. Put t=wz/(1+wz) and

    R_+=[1+(Q-1)t]^n, R_-=[1+(Q^(-1)-1)t]^n,
    delta=1-Q^N.

Summing the binomial kernel gives exactly

    sigma_K=-(M/q) R_-,
    sigma_Ecal=w^(-1)[M R_- -M^(-1)-kappa(1-t)^n],
    sigma_F=w[R_0-Q R_+-delta t^n], R_0=1.       (4.1)

The apparent w inverse cancels in the numerator as required by the
polynomial matrix kernel. At the actual root delta=0. At the
complete meridian kappa=0. Before those restrictions the lower
vacuum and upper head walls are the explicit functions (1-t)^n
and t^n. Their derivatives must be retained before specializing.

The lower vacuum coefficient kappa is not the second normal of
the common-Verma two-wall construction: that normal is
M Q^(-N)-M^(-1)=kappa+M delta/(1-delta). They agree on the root
wall, but their off-root derivatives differ. Formula (4.1) keeps
the actual finite-head coefficients and does not identify those
two normals.

Indeed sigma_(E_00)=(1-t)^n and sigma_(E_nn)=t^n. Both have
normalized trace 1/N, despite being exponentially small on fixed
interior subintervals. For a fixed polynomial moment t^h,

    N integral_0^1 t^(n+h) dt=N/(N+h),
    N integral_0^1 (1-t)^n t^h dt
                   =h!/[(N+1)...(N+h)],          (4.2)

where the empty product at h=0 is one. Thus the marked endpoint
rows, including their normal factors N, are exact beta identities.
Interior Taylor/asymptotic jets alone would lose them.

For the actual number operator J_0, more generally,

    sigma_(p(J_0))(t)=sum_(j=0)^n binom(n,j)
                                    t^j(1-t)^(n-j)p(j),
    sigma_((J_0)_r)=(n)_r t^r.                  (4.3)

Here (a)_r is the falling factorial. These finite Newton identities
transport every bounded index moment. They coexist with the exact
whole-clock formula R_+, because products use (2.2). Coupling
derivatives of a crossing kernel must still obey the full Leibniz
rule. There is no substitution of an ordinary coordinate for a
number operator before taking products.

## 5. The physical symbol and its holonomy form

This construction also addresses the physical parameter, rather
than the distinct normal to one fixed root. Set

    Q_N=exp(2pi*i/N), h_N=2pi*i/N.

For t in compact sets, the whole function

    [1+(exp(2pi*i*s)-1)t]^(1/s-1)

has a removable analytic germ at s=0, with value exp(2pi*i*t),
using its logarithm near one. This follows by factoring s from
that logarithm. At s=1/N it is exactly R_+. The inverse version
gives R_- and has value exp(-2pi*i*t).

Away from the two endpoint walls on the real cycle, at M=1 the
resulting principal functions are therefore

    A=exp(2pi*i*t), p=1/w, x=-M,
    K=x/A, Ecal=(x^(-1)-K)p, F=(1-A)/p.          (5.1)

At generic M the same statements hold on compact interior portions
where the explicit vacuum term is exponentially small; that term
cannot be dropped in a whole meridian/source identity.

These are exactly the Gauss coordinates of the actual classical
[longitude/holonomy calculation](quantum_longitude_and_regulator_action.md).
The source geometry has the exact symplectic identity

    dLog A wedge dLog p
       =2pi*i dw wedge dz/(1+wz)^2.              (5.2)

On Gamma, w=sqrt(t/(1-t))exp(i phi), this becomes
2pi dt wedge dphi. Its normalized Liouville measure is precisely
the trace measure dt dphi/(2pi). Formula (2.2) has first-order
commutator, in a controlled smooth symbol class,

    (1/n)(1+wz)^2
       [partial_z a partial_w b-partial_z b partial_w a].

Dividing by h_N gives the Poisson tensor inverse to (5.2), since
n h_N tends to 2pi*i. For the actual generators the bracket identities
also follow directly from their exact matrix relations. No uniform
star expansion is asserted for an arbitrary rapidly growing matrix
family, in particular not for the unknown full knot period.

## 6. A direct actual-A period has fixed pole order as well

There is a second useful application, directly to the specified
quantum A-operator. It uses the compact calculus at a fixed matrix
size d, rather than the growing color size N. Keep these two uses
distinct.

The [actual all-level theorem](all_level_a_period.md) supplies the
generic recurrence for the actual colors, with fixed companion rank d,

    v_(j+1)(q)=A_j(q)v_j(q),
    v_j=(C_j,...,C_(j+d-1))^t.

Choose the fixed sufficiently large starting color j_0 prescribed
there. All initial entries v_0:=v_(j_0) are fixed Laurent-polynomial
colors, and no subsequent leading coefficient is identically zero.
Set

    H_N=A_(N-d)...A_(j_0), ell=e_d^t,
    R_N(q)=v_0(q)ell H_N(q).                      (6.1)

This is a specified rank-at-most-one d by d rational matrix. Its
input is only the actual operator and finite initial-color pointing.
The exact recurrence proves

    Tr R_N(q)=ell H_N(q)v_0(q)=C_N(q).             (6.2)

Use the kernel (1.1) at matrix size d, denoted K^(d), and define

    Omega_N(q)=-(d/(2pi*i))
          K^(d)_(R_N(q))(w,z) dw wedge dz/(1+wz)^(d+1).

Then the literal actual A-period identity is

    integral_Gamma Omega_N(q)=C_N(q),
    [integral_Gamma Omega_N(q)]_(q=q_N)=K_N.      (6.3)

Thus both the algebraic surface, cycle and pole order d+1 are fixed
independently of N in this operator realization. The ordered transport
product still has N-dependent coefficient complexity; no bounded
height, fixed degree in q, or volume estimate follows from (6.3).

Apparent quantum-normal poles can also be removed as exact forms.
At q_N expand R_N=sum_(r>=-s)epsilon^r R_(N,r). Since C_N(q) is
the original regular color polynomial, every coefficient R_(N,r)
with r<0 has trace zero. Formula (3.3) gives a specified rational
one-form eta_(N,r) with omega^(d)_(R_(N,r))=d eta_(N,r). Therefore

    Omega_N^reg=Omega_N
               -d*d_deRham[sum_(r<0)epsilon^r eta_(N,r)]      (6.4)

is regular at q_N, has the same period and specializes to K_N.
The first d in the subtracted expression is the integer companion
rank; d_deRham is the exterior derivative. This procedure never
divides by C_N or assumes K_N!=0. The uniform leading-coefficient
pole budget from the all-level theorem bounds s independently of N.

Equivalently slide the pointed source through the whole product:

    R_N^right=H_N v_0 ell,
    R_N-R_N^right=[v_0 ell,H_N].                 (6.5)

The right representative is regular, since H_N v_0 is exactly the
vector of actual regular colors. The commutator in (6.5) has the
global primitive (3.3), proving equality of the two whole period
classes. In the order (6.1) apparent poles can be nonzero matrices;
one must not mistake cancellation of their traces for entrywise
regularity before retaining this exact source map.

Projection to the one-dimensional cohomology must occur after the
ordered product and source pairing. The trace-zero subspace is not
a left ideal: a later matrix can give a nonzero trace when multiplied
by a traceless one. Accordingly the star product and pointing in
(6.1), not only the individual trace classes, remain part of the
whole actual A-object. This is precisely the source information
that a bare scalar norm equation would omit.

## 7. What this supplies to the global torsor problem

The actual normalized finite cut now has a fixed algebraic domain,
a marked compact cycle, an exact product calculus, a global rational
cohomology identity, and explicit two-wall functions. Every weighted
finite word and its Green-current insertions can be carried through
this same construction. The original invariant is their same selected
period. This is a concrete whole-function source model for the
torsor program, with no change of invariant or root normalization.

There is still a substantive globalization to prove. The internal
geometric Gaussian sector has not been shown to define a global
cohomology component of these actual forms with a controlled
coefficient. Its critical framing family can degenerate or escape
at the compactified poles. A local nonzero Gaussian and (5.2) do not
prove that its internal cycle is selected or that its boundary
contributions vanish. Nor does the algebraic identity (3.3) bound
tau(A): arbitrary scalar matrices already give arbitrary periods.

The next source-preserving comparison must commute with the exact
product and current maps, and account for these possible critical
boundary terms. The existing
[Rivin optimizer](rivin_flow_and_quantum_source.md) supplies its
algebraic geometric place and strict concavity, not this global
cycle comparison. The general volume conjecture remains unproved.

[Universal exact checks](../experiments/audit_compact_coherent_source.py)
and [results](../experiments/compact_coherent_source_results.json)
verify the centered star product, global primitive commutators,
compact beta trace, and both off-root walls at N=2,...,9. They
also check the physical Gauss brackets and form, the retained
clock star power, and the removable clock germ. The formulas
above are the uniform proofs; these tests do not establish a
selected volume estimate.
Eight fixed-rank actual-operator tests additionally retain a nonzero
traceless apparent root pole in the left source frame and remove it
in the source-preserving right frame. The
[independent audit](compact_coherent_source_independent_audit.md)
checks the whole product, global cohomology, bounds, and direct
actual-A period normalization.
