# A pole-free scalar cardinal completion of the original joint source

28 October 2026. Fixed powers of explicit cardinal windows remove every
factorial pole in a prescribed O(N) joint-state box, while leaving ALL
original integer physical state values unchanged and killing every
invalid integer state. This keeps the unwrapped linear output and
closure relations. It is a scalar completion of the original finite
source, not a new positive invariant or a replacement boundary state.

The windows are not innocuous on general complex contours. Their
wrong-side exponential growth and exact finite integer-mode packets
are calculated below. Their separated mode currents must remain at
outside-band integer collisions. No global volume bound is inferred.

## 1. Exact cardinal functions and quantitative half-plane bounds

Put d=N-1 and

    S_N(s)=sum_(j=0)^d 1/(s-j),
    w_N^+(s)=(exp(2pi*i*s)-1)S_N(s)/(2pi*i),
    w_N^-(s)=exp(-2pi*i*s)w_N^+(s).                    (1)

Both functions are entire. Their values are EXACTLY one at each
integer 0,...,d, and zero at every integer outside that range.
The outside zeros are simple: S_N(n) is a sum of strictly positive
terms if n>=N, and strictly negative terms if n<0, so is nonzero.

These are sums of the literal unit-circle Fourier coefficients in
[the physical projection theorem](actual_projected_transfer_cot_completion.md).
Orthogonality and Cauchy--Schwarz therefore give, on the WHOLE plane,

    |w_N^+(s)|<=sqrt(N) exp(2pi max(0,-Im s)),
    |w_N^-(s)|<=sqrt(N) exp(2pi max(0,+Im s)).            (2)

The normalizations dtheta/(2pi) and the complete turn 0<=theta<=2pi
are retained. Thus a fixed number of fixed window powers costs
exp(o(N)) on any joint tube |Im s|<=N^alpha, alpha<1, and polynomial
cost on its favorable half-plane. It may cost exp(cN) on the wrong
side of a macroscopic complex contour.

There are also N-1 additional real, noninteger zeros, one in each
(j,j+1). Indeed S_N'(x)=-sum_r1/(x-r)^2<0 there and its endpoint
limits are +infinity and -infinity. There are no nonreal zeros of
S_N, since Im S_N(s)=-Im s sum_j|s-j|^(-2). These zeros are kept;
one cannot replace the window by a nowhere-zero scalar unit.

## 2. An exact finite-mode formula, with its endpoint currents

Let psi be the ordinary digamma and define

    H_N(s)=psi(s+1)-psi(N-s),
    A_N(s)=1/2-H_N(s)/(2pi*i),
    B_N(s)=1/2+H_N(s)/(2pi*i), t=exp(2pi*i*s).

The digamma recurrence and reflection, equivalently the convergent
partial fractions of pi cot(pi s), give exactly

    S_N(s)=pi cot(pi s)+H_N(s),
    w_N^+(s)=A_N(s)+B_N(s)t,
    w_N^-(s)=B_N(s)+A_N(s)t^(-1).                      (3)

Thus any fixed integer power has a finite, explicit binomial packet
of INTEGER Fourier modes. No limit is used in (3). On the physical
strip -1<Re s<N the coefficients A_N,B_N are holomorphic. In a
scaled compact substrip, their asymptotics and derivative bounds are
those of the elementary uniform digamma expansion; for example

    H_N(Nz)=Log(z)-Log(1-z)+O(1/N), 0<Re z<1.          (4)

The logarithms in (4) are the consistent ones in this simply connected
strip. On nonreal compact scaled chambers the finite packets therefore
add only integer linear logarithmic marks to the original leading phase.

This decomposition is NOT a license to discard its endpoint currents.
At s=-r<0, H_N has residue -1; at s=N+r, H_N also has residue -1
in the s coordinate. In either case A_N and B_N have opposite simple
polar parts. In their COMPLETE combination (3) these parts cancel;
the derivative of t supplies the finite correction which makes the
window zero rather than one at that integer. Higher powers cancel
their complete principal parts and finite jets as well. Splitting
the modes and crossing those poles independently loses that source
cancellation.

For the macroscopic off-real symbol one may use

    S_N(Nz)=integral_0^1 du/(z-u)+O(1/N).

The integral is nonzero off [0,1]. On Im z>0, w^+ has no exponential
factor; on Im z<0 its leading factor is exp(2pi*i*Nz). For w^- the
roles reverse, with factor exp(-2pi*i*Nz) on Im z>0. Thus (2)'s
wrong-side growth is a REAL leading effect, precisely an integer
mark, not a tame multiplier that may be erased.

There is a useful precise local choice. On any compact scaled chamber
K disjoint from the real axis, the uniform digamma expansion gives

    H_N(Nz)=h(z)+O_K(1/N),
    h(z)=Log z-Log(1-z).

Use w^+ when Im z>0 and w^- when Im z<0. Uniformly with every fixed
number of z derivatives, that FAVORABLE window is respectively

    1/2-h(z)/(2pi*i)+O_K(1/N),
    1/2+h(z)/(2pi*i)+O_K(1/N).                    (4a)

Both limiting functions are nonzero: a zero would require h(z)=+pi*i
or -pi*i, hence exp(h)=z/(1-z)=-1, an impossibility. Compactness
therefore gives fixed positive upper and lower bounds for the
favorable window on K, for all sufficiently large N. The discarded
exponential in deriving (4a) is only an ESTIMATE inside that specified
chamber; the exact packet (3) is still used for transport.

Consequently, at any supplied regular joint critical point where all
physical forms ell/N are nonreal, choose each window orientation
favorably there. The completed scalar has the SAME leading phase
and a nonzero bounded local amplitude multiplier. This is an exact
completion with a controlled microlocal symbol, not an assertion
that the original cycle reaches that point. When some forms are real,
one must keep both modes and their real zeros; (4a) supplies no such
local ellipticity there.

## 3. Fixed powers cancel ALL factorial poles in a fixed joint box

The actual factorial interpolant has the exact integer divisor

    ord_(s=n) Fhat_N(s)=floor(n/N), n integer.          (5)

It has no noninteger zero or pole. For n>=0 the zeros come from
the denominator Gamma(Nk-s) of its defining product, one for each
Nk<=n. For n<0 its numerator Gamma(s+1) and Gamma(Nk+s+1)
give 1+floor((-n-1)/N)=-floor(n/N) poles. This also follows from
its exact N-shift, with the original strip nonzero. The conjugate
negative-root factorial has the SAME divisor.

Suppose a physical linear state form ell takes values with
|Re ell|<=Lambda N in the chosen complex box. For either exponent
epsilon=+1 or -1 and either window orientation eta, choose a fixed
integer p>Lambda+1. Then

    G_(epsilon,eta)(ell)
       =Fhat_(+ or -)(ell)^epsilon *w_N^eta(ell)^p       (6)

is holomorphic on that box and vanishes at EVERY outside-band integer
ell. At a physical integer it is exactly the original factorial or
its inverse. Indeed its divisor there is p+epsilon floor(n/N)>=1
outside the band. The half-open endpoints are exactly 0,...,N-1;
there is no division by F_N or a substituted value at a pole.

Use (6) for EACH factorial occurrence of the original coefficient.
Add an entire cardinal factor for any physical head/transfer form
not already present. This proves holomorphy also at dependent or
simultaneous collisions: each individual meromorphic factor has
already been canceled, so no appeal to a generic transverse
intersection or an unproved saturation quotient is needed.

The original positive coefficient has factorial forms

    input a,b; transfer k; outputs c=b+k, e=a-k,
    Fhat(c)Fhat(a)/[Fhat(k)Fhat(b)Fhat(e)].             (7)

The negative coefficient is its actual mirror. Thus every physical
input, output and transfer is one of the forms in (7). All Cartan
Gaussians, kappa, pivot and external source factors stay unchanged.
Formula (6) only changes the off-lattice analytic completion.

## 4. Exact whole original scalar with unwrapped gluing preserved

Start with the original COMPLETE balanced-basis scalar, after the
justified whole-word marked trace conversion,

    K_N=chi_N/N Tr[(I tensor g tensor ... tensor g)W_N]. (8)

Let v consist of the b initial physical head labels and the m
nonnegative physical transfer indices. At each signed crossing the
exact update is

    (a,b)->(b+sigma*k,a-sigma*k).

Every intermediate physical head label is an INTEGER LINEAR form in v.
The ordinary trace closure is the EXACT integer linear equation Lv=0,
not equality modulo N. A fixed integral basis B of ker_Z L gives a
bijection v=B u from Z^r to all integer closed paths. It is obtained
by integer row and column operations on the fixed diagram matrix;
no quantum-level or source normalization factor occurs.

Every physical closed path has all initial/transfer coordinates in
[0,d], so a fixed rational left inverse of B bounds |u|<=C N.
Choose an integer coordinate box containing them. All physical forms
ell(Bu) then satisfy |Re ell|<=Lambda N on a slightly enlarged fixed
O(N) complex box, with Lambda depending only on the diagram and box.
Use the window powers in Section 3 on its actual scalar summand,
calling the resulting holomorphic function F_N(u).

At EVERY valid integer state F_N has its EXACT original value. At
EVERY invalid integer state at least one physical form lies outside
0,...,d, and its completed factor is zero; all other completed
factors are holomorphic. Hence it contributes zero even when the
unwindowed formula had simultaneous poles. Therefore, exactly,

    K_N=chi_N/N sum_(u in integer box) F_N(u).          (9)

The same sum is its product cotangent residue contour. Any additional
integer states crossed while enlarging it inside the specified box
have zero residue unless they are original physical states. All
intersections are ordinary multivariate residues of a HOLomorphic
scalar summand, so no derivative residue is silently omitted. This
is a genuine complete-source comparison for arbitrary fixed braid
width, preserving unwrapped routing and all marked scalar factors.

### Explicit knot coordinates, dimension and forced-cut faces

For a ONE-component closure the lattice above has the particularly
simple explicit coordinates

    u=(t,k_1,...,k_m), dimension m+1.                  (9a)

Start at the distinguished cut with color t and follow the oriented
physical knot once. At the two visits to crossing j, the strand color
changes respectively by +sigma_j k_j and -sigma_j k_j. Hence every
physical arc color is exactly

    ell_r=t+sum_j epsilon_(r,j) k_j,
    epsilon_(r,j) in {0,1,-1}.                       (9b)

Each k occurs with both signs on the complete traversal, so the final
color is t for EVERY integer transfer vector. Conversely any original
closed path has one t and its unique transfers, and this traversal
recovers all its colors. This is an integer bijection with counting
Jacobian ONE, not a modulo-N or rational parametrization. Equivalently
the one-cycle closure permutation has rank b-1 after subtracting the
identity, so its m+b variables have kernel dimension m+1.

The exact original state polytope is

    0<=k_j<=d, 0<=ell_r(t,k)<=d for every physical arc. (9c)

The summand in these coordinates is the product of the original
signed r(a_j,b_j;k_j), every original ordinary-head pivot evaluated
on its closure arc, and chi_N/N. Thus the construction is concrete
for arbitrary braid width and involves no unknown knot scalar.
The cube 0<=t,k_j<=d contains all states; (6) analytically kills the
invalid intermediate colors inside that cube. A larger fixed O(N)
complex box is chosen only for contour transport and pole accounting.

Its STRICT real interior is nonempty for every nonempty one-component
diagram: set t=d/2 and all k_j=delta d, with
0<delta<1/(4(m+1)). Formula (9b) puts every arc in (d/4,3d/4),
and each transfer is strictly between zero and d. There is no
assumption that a quantum coefficient has no cancellations at that
point; this is an exact source-domain assertion.

A fixed highest-cut t=0 presentation is different and can force
k_j=0 or other boundary equalities. It must then be treated on its
actual affine face, with the corresponding constant factorials kept;
one cannot impose a missing normal stationary equation or pretend
that face has a full strict interior. The construction used here
instead makes the justified WHOLE original marked-trace conversion
to I/N BEFORE decomposing paths, yielding the original average over t.
It does not replace a cut separately in any clock sector or inserted
current. Thus the strict interior in (9c) is obtained without changing
the original selected scalar or discarding its fixed-cut boundary
mechanism. Links may retain the general lattice formulation above.

For a completely explicit contour, take each t,k_j on a rectangle
with real edges -1/2 and N-1/2 and any fixed nonzero imaginary height.
Its product encloses exactly the integer cube 0,...,d in these m+1
coordinates. Since the coefficients in (9b) are 0,+1,-1, every arc
form on that contour has |Re ell|<=(m+1)N. Thus, for example, the
fixed choice p=m+4 at EACH factorial occurrence suffices there.
For a larger box |Re(t,k_j)|<=C N, choose p>C(m+1)+2 instead.
The exact integral is (9)'s original chi_N/N times

    (2pi*i)^(-(m+1)) integral F_N(u)
                  product_j [pi cot(pi*u_j) du_j].     (9d)

There is no geometric Jacobian or root-grid multiplicity in (9d).

### Explicit original action at complete color

For clarity the leading action in Section 5 can be read directly
from the retained original coefficients, not an unspecified operator.
Let x=-q^(-1), Q=q^2=exp(2pi*i/N), and use the continuous choice
Log x=i*pi-i*pi/N. The two exact signed coefficients are

    r_+(a,b;k)=kappa x^(-a-b+k) Q^(b(a-k))
       Fhat_+(b+k)Fhat_+(a)
         /[Fhat_+(k)Fhat_+(b)Fhat_+(a-k)],
    r_-(a,b;k)=kappa^(-1) x^(a+b-k) Q^(-a(b-k))
       Fhat_-(a+k)Fhat_-(b)
         /[Fhat_-(k)Fhat_-(a)Fhat_-(b-k)].              (9e)

Here Fhat_-(z)=conjugate(Fhat_+(conjugate(z))). The second formula
is the actual complete-color swap/conjugation relation, including
the unit Cartan scalar; it is not a replacement R matrix. All its
physical inputs and outputs are the unwrapped forms in (9b).

On a regular marked chamber put

    L_+(s)=integral_0^s Log(1-exp(2pi*i*v)) dv,
    L_-(s)=integral_0^s Log(1-exp(-2pi*i*v)) dv.

The branches are the actual factorial branches continued from
0<s<1. For instance L_+(s)=[Li2(1)-Li2(exp(2pi*i*s))]/(2pi*i)
on that marked continuation. With A=a/N, B=b/N and K=k/N,
the state-dependent leading actions in (9e) are explicitly

    s_+=i*pi*(-A-B+K)+2pi*i*B*(A-K)
           +L_+(B+K)+L_+(A)-L_+(K)-L_+(B)-L_+(A-K),
    s_-=i*pi*(A+B-K)-2pi*i*A*(B-K)
           +L_-(A+K)+L_-(B)-L_-(K)-L_-(A)-L_-(B-K).  (9f)

Thus S_0 is the sum of (9f), with every A,B,K replaced by its
ACTUAL source linear form in y=(t,k)/N. The exact kappa factors,
the original external chi_N, and x^(1-N) factors in the pivots
remain in (9d); their state-independent phase is not discarded.
The pivot's remaining Q^(-a)=exp(-2pi*i*A) and the O(1) correction
from Log x are explicit amplitudes, not additional N-order state
actions. The usual uniform factorial symbol is applied only on
regular compact marked chambers, never across a factorial zero
by assertion. Equation (9f) therefore gives the actual complete
bulk stationary problem in the m+1 physical coordinates.

## 5. Leading equations and the still necessary global estimate

Write y=u/N, and suppose a regular open chamber admits the original
leading scalar action N S_0(y). Expand each power by the EXACT finite
mode formula (3), retaining its coefficients and all matched endpoint
currents. A mode indexed by integers n_ell has leading action

    N[S_0(y)+2pi*i sum_ell n_ell ell(B y)].              (10)

Its full stationary equations are

    partial_(y_j) S_0+2pi*i sum_ell n_ell
                         partial_(y_j)ell(B y)=0.       (11)

All added numbers are integers. Exponentiating (11) gives the SAME
original classical gluing equations. At a regular FULL stationary
point its retained integer marks are included by the already proved
phase/regulator identity. It is not an identification of a selected
geometric cycle from nonzero density alone.

Equations (10)--(11) have only been asserted on regular leading
chambers with the appropriate slow symbol control. Across a real
window layer one must retain its whole finite-mode packet, and at
outside-band integers the matched currents in Section 2. The function
F_N is holomorphic there, but its separated mode terms may have poles.
Nor does holomorphy bound the original factorial action or a global
transport mass. The window bound (2) is subexponential on normal
tubes, but a macroscopic wrong-side contour changes the leading
integer-marked action and must be calibrated as such. These facts
are retained, rather than claiming the windows are harmless weights.

The construction removes scalar factorial POLE exits in a fixed box
without imposing a new invariant or changing discrete gluing. It does
not yet supply the full high-action deformation, a sharp bulk bound,
or geometric noncancellation of the original knot state.

[Audit](../experiments/audit_actual_scalar_cardinal_source_completion.py):
exact window values and finite packets, factorial divisor cancellation,
half-plane growth, both literal signed coefficients and original full
signed-source lattice comparisons. The audit checks 288 finite-mode
packets, 96 whole-plane bound checks, 108 Barnes divisor packages,
670 exact original signed coefficient checks, and eight complete-source
lattice comparisons on braid widths two through four. These finite
checks supplement the proofs above; they are not all-level proofs or
tests of a volume claim.