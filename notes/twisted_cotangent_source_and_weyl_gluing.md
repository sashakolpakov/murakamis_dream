# The compact source torsor and its actual Weyl gluing

Research proof, 27 October 2026. The fixed compact source is a nontrivial
cotangent torsor with an explicit Chern transition. The actual finite
root module has a meridian-dependent Weyl adapter whose square is
exactly the full modified-dimension function times its recorded scalar.
The resulting order-two cocycle has a marked rational splitting at
every level, including even levels.

Quantum/dynamical Weyl operators have existing coverage; see the scope of
[Etingof--Varchenko](https://arxiv.org/abs/math/0011001). We use that
reference for coverage, not a proof or a claim that its precise
normalization equals the one below. The cotangent torsor is identified
directly by its transition equations (1)--(2). The already proved
[actual Weyl descent](actual_weyl_descent.md) gives state reciprocity.
The new calculations identify the compact source transition and the
explicit balanced-basis scalar cocycle with our full peripheral factor.

These are source and gluing theorems. They do not identify the actual
global geometric period or prove its volume norm.

## 1. An explicit twisted cotangent torsor

Use the [compact source](compact_coherent_source_period.md)

    X=(P1 times P1) minus {s_0t_0+s_1t_1=0},
    omega_0=dw wedge dz/(1+wz)^2.

Project to the first P1. On its affine chart w define the fiber
coordinate b=z/(1+wz). Each fiber is an affine line, including
the value z=infinity when allowed. On the second chart put

    w'=1/w, b'=1/(w'+z).

The exact overlap formulas are

    b'=w-w^2 b, dw' wedge db'=dw wedge db=omega_0. (1)

In particular X is a torsor under the cotangent bundle O(-2),
with the affine term w retained. For the local primitives

    lambda=-b dw, lambda'=-b' dw'

one has

    d lambda=d lambda'=omega_0,
    lambda'-lambda=dlog w.                         (2)

This is the connection torsor of O(1), in this explicit transition
convention. It is not the split total cotangent bundle. On the marked
real sphere z=bar(w), lambda is the Chern connection form
-bar(w)dw/(1+|w|^2), and

    integral_Gamma omega_0=-2pi*i,
    integral_Gamma[-omega_0/(2pi*i)]=1.             (3)

Thus the sign agrees with c1(O(1))=1. Equation (2), rather than a
globally defined primitive, records the nonzero source class.

There is a useful obstruction to an incorrect global comparison.
On a split framing chart with global tau and invertible A,

    Omega_cut=dtau wedge dlog A=d(tau dlog A)

is exact. No globally regular map from X to this split chart can
pull Omega_cut back to a nonzero multiple of omega_0 in cohomology:
pullback preserves exactness and (3) forbids it. A nonzero whole
comparison must retain a twisted transition, a divisor residue or
its equivalent marked relative class. Equality of local two-forms
does not supply that data.

## 2. The actual complete head patches globally

Let N>=2, n=N-1, q=exp(pi*i/N), Q=q^2. At complete color M=1
identify the actual balanced head with H^0(P1,O(n)), by e_j=w^j.
Its exact generators on this space are

    K=-(1/q)D_(Q^-1),
    Ecal=w^(-1)(D_(Q^-1)-1),
    F=w(1-QD_Q), D_Q f(w)=f(Qw).                 (4)

The E numerator cancels at w=0. The F coefficient on w^n is
1-Q^(n+1)=1-Q^N=0, so all three preserve this finite section space.
They are exactly the finite matrices, not an independent quantization.

The line transition is f_infinity(u)=u^n f_zero(1/u), u=1/w.
It transforms the shift to

    D_Q^(w) -> Q^n D_(Q^-1)^(u)=Q^(-1)D_(Q^-1)^(u).

Consequently the generators in the second chart are

    (K,Ecal,F) -> (K_u^(-1),-F_u,-Ecal_u).         (5)

Equivalently let C e_j=e_(n-j). Direct matrix multiplication gives
C K C=K^(-1), C Ecal C=-F, C F C=-Ecal. The original constant
source vector, average co-source, and coupon e_ij=1/N are fixed
by C. Thus the actual complete source has this exact Weyl gluing,
not just a matching semiclassical two-form.

The source level also has a precise half-form description:

    O(N-1)=O(N) tensor K_(P1)^(1/2),
    K_(P1)^(1/2)=O(-1), dim H^0(O(N-1))=N.       (6)

This is a bundle identity with the unique half-canonical line on P1.
In the physical convention Omega_phys=2pi*i omega_0,
h_N=2pi*i/N, its prequantum curvature is
Omega_phys/h_N=N omega_0, with the Chern sign of (3). Thus the
root level N and the actual section degree N-1 differ by this
specified half-form factor. No limit is required for (4)--(6).

## 3. The balanced Weyl matrix at generic meridian

Keep the actual root finite head with meridian M, and write

    K_M e_j=-(M/q)Q^(-j)e_j,
    E_M e_j=(M Q^(-j)-M^(-1))e_(j-1), j>0,
    E_M e_0=0,
    F e_j=(1-Q^(j+1))e_(j+1), j<n, F e_n=0.

Here E_M is Ecal, not the unscaled Chevalley E. Put

    P_j=(Q;Q)_j, P_j(M^2)=(M^2 Q;Q)_j,
    D_M e_j=M^j P_j/P_j(M^2) e_j,
    W_M=D_M C.                                  (7)

Work on the marked open where the displayed denominators and
numerators are units; in particular they are units near M=1.
Then the actual generator comparison is

    W_M K_M W_M^(-1)=K_(M^-1)^(-1),
    W_M E_M W_M^(-1)=-F,
    W_M F W_M^(-1)=-E_(M^-1).                    (8)

For E after reversing the basis, its raising coefficient is
M Q^(j+1)-M^(-1). The adjacent ratio of D is

    D_(j+1)/D_j=M(1-Q^(j+1))/(1-M^2Q^(j+1)),

giving -(1-Q^(j+1)). The F equation follows from the inverse
ratio and 1-Q^(-j)=-Q^(-j)(1-Q^j). The K equation is immediate
from Q^n=Q^(-1). This proves (8) including both endpoints.

On full unrolled colors the same matrix sends H_M to
-H_(M^-1), with the meridian lift alpha'=2n-alpha retained.
Termwise substitution in the actual universal R therefore gives
the Chevalley turnover with reversed tensor order. The original
Cartan half-character, cups, caps and twist transform as in the
generator proof of actual Weyl descent. This does not discard
the stripped-Cartan multiplier recorded there.

## 4. The square is the full peripheral function

Following each reversed basis vector twice gives

    W_(M^-1) W_M=c_N(M) I,
    c_N(M)=N M^(N-1)/S_N(M^2),
    S_N(Y)=1+Y+...+Y^(N-1).                     (9)

For a direct proof the j-th diagonal product is
D_(M^-1,j) D_(M,n-j). Using Q^(N-r)=Q^(-r) pairs its suffix
factors and proves independence of j. At j=0 it is

    D_(M,n)=M^n (Q;Q)_n/(M^2Q;Q)_n
           =N M^n/S_N(M^2),

since (Q;Q)_(N-1)=N and (M^2Q;Q)_(N-1)=S_N(M^2).

This is exactly the already fixed full modified-dimension adapter:

    c_N(M)=(N/eta_N)d_N(M), eta_N=i^(N+3).       (10)

It is invariant under M inversion and has value one at M=1.
Its whole meridian germ is not constant. On M=exp(u),

    c_N(exp u)=N sinh(u)/sinh(Nu)
             =1-(N^2-1)u^2/6+O(u^4).           (11)

Thus even where the ideal-point multiplier equals one, its peripheral
normal data must not be reset. Formula (10) ties
the Weyl cocycle to the specified period normalization, rather
than an arbitrary projective scalar.

## 5. A marked rational splitting at odd and even levels

The cocycle in (9) can be solved explicitly, with its divisors kept.
For N=2m+1 put

    beta_N(M)=(M^2Q;Q)_m/(Q;Q)_m.

For N=2m put

    beta_N(M)=[(1+iM)/(1+i)]
                      (M^2Q;Q)_(m-1)/(Q;Q)_(m-1).            (12)

The specified i is in the root coefficient field at even N; its
phase is retained. In both cases beta_N(1)=1 and

    beta_N(M) beta_N(M^(-1))=c_N(M)^(-1).         (13)

To prove this, pair Q^r with Q^(-r). For odd N all nonzero residues
pair, and

    (Q;Q)_m^2=N(-1)^m Q^(m(m+1)/2).

For even N the unpaired residue is Q^m=-1, so

    (Q;Q)_(m-1)^2=(N/2)(-1)^(m-1)Q^(m(m-1)/2).

The remaining scalar norm is
(1+iM)(1+i/M)/(1+i)^2=(1+M^2)/(2M), precisely the missing factor.
These identities prove (13). Therefore

    Wtilde_M=beta_N(M) W_M,
    Wtilde_(M^-1) Wtilde_M=I.                   (14)

This is a marked rational norm splitting, not a permission to omit
c_N or beta_N from an exact comparison. Their zero/pole divisors
are part of the integral source lattice. On the M=1 chart the
splitting is regular and fixes the original complete source.

## 6. Relation to the remaining geometric boundary theorem

The actual source now has an explicit cotangent-torsor cocycle,
complete quantum chart gluing, and generic-meridian Weyl scalar
whose norm and full modified-dimension role are known exactly.
This solves the order-two source gluing problem on its stated
charts, uniformly in the knot and level.

Equations (7)--(14) are identities of whole meridian functions at
the fixed quantum root. They do not assert the same finite-matrix
relations off the root Q^N=1. A q-normal extension must retain the
actual two-wall source and its corrections before differentiating.

It does not assert that the standard polynomial SL2 action on
H^0(O(N-1)) equals the actual quantum dressing of every geometric
framing. The actual finite Weyl adapter (8) is proved; a general
unipotent dressing and its source-normal comparison require their
own derivation. Nor does (14) select which internal geometric
stationary component contributes to the original period.

The global regulator/selected-norm comparison remains to be proved.

[Exact source and cocycle checks](../experiments/audit_twisted_source_weyl_gluing.py)
and [results](../experiments/twisted_source_weyl_gluing_results.json)
verify all three generator comparisons, the full scalar square and
marked norm splitting in 78 actual root-module cases at N=2,...,14.
They also check the cotangent transition and full peripheral germ.
The [independent audit](twisted_source_weyl_independent_audit.md)
confirms the proof, normalizations, phases and endpoints.

The [geometric framing compactification](springer_centralizer_boundary_source.md)
now produces this same twisted cotangent torsor by rescaling its
centralizer coordinate. Its nonzero principal Gaussian residue is
computed in [the explicit gauge calculation](compact_framing_gauge_and_boundary_residue.md).
The physical selected-cycle comparison remains separate from that
exceptional-divisor residue.
