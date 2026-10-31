# The actual Fourier source reduces exactly to one exterior index

Research theorem, 27 October 2026. For the original root family the
fully reclosed one-cut operator is scalar. Hence ANY fixed first
input column, paired with the original output row, gives the original
period. Applied to the actual second-wire Fourier polarization, this
removes the first exterior average exactly and leaves one finite
Fourier-label sum. A whole actual Ward homotopy records every normal
defect of this source reduction; off-root scalarity is not assumed.

## 1. The scalar root closure and its precise source

Use the actual nilpotent color at q_N=exp(pi*i/N), Q_N=q_N^2,
with M left as its original meridian parameter. In the balanced
head frame

    K=x diag(Q_N^(-j)), x=-M/q_N,
    F_(j+1,j)=1-Q_N^(j+1), 0<=j<N-1.

The original signed local crossings intertwine the true coproduct.
Closing every other strand with its original root pivotal cap
therefore makes the one-cut matrix C_N(M) a module endomorphism.
The literal closure proof, including the root cap and all full
peripheral factors, is given in
[the closed-braid period construction](closed_braid_period_line.md),
Sections 2--3. No extra pivot is attached at the opened identity wire.

One can prove scalarity directly with just the actual K and F rows.
Distinct K eigenvalues make C_N diagonal. The F commutator then gives

    (1-Q_N^k)(C_(k-1,k-1)-C_(k,k))=0, 1<=k<N.

Every prefactor is nonzero, so all entries agree. This proves

    C_N(M)=P_N(M) I.                                    (1.1)

If C_N includes the original external d_N, then P_N=d_N F_N;
if that line is recorded externally, P_N=F_N. Use the SAME choice
on every side. The equality first holds on the admissible generic
M chart and continues as its actual rational-map/source-lattice
identity. It includes every regular complete value M=1. It does
not invert a peripheral norm-zero factor or assert off-root q
scalarity of the compressed auxiliary family.

Let 1 denote the all-ones column, and retain the actual source

    Phi(C)=(1/N)1^t C 1,
    lambda_a(C)=1^t C e_a=sum_c C_(c,a).               (1.2)

Equation (1.1) proves, for EVERY a in the physical head,

    lambda_a(C_N)=Phi(C_N)=P_N.                       (1.3)

This fixes only the INPUT column. The output row still sums all c.
It is not the diagonal source E_aa when applied to current tensors.

## 2. One remaining Fourier-label sum, with its original normalization

For the literal two-cut tensor let

    T^V=(I tensor V)T(I tensor V^-1),
    V_(j,b)=Q^(jb),
    Jtilde_(a,j)=sum_c T^V_(c,j;a,j).

Use the WHOLE actual inverse from
[the Vandermonde source theorem](actual_two_cut_fourier_polarization_and_cap.md).
Its exact partial-trace identity gives, even before specializing Q,

    sum_j Jtilde_(a,j)=lambda_a(C).                   (2.1)

At the actual root the scalar closure therefore proves

    P_N(M)=sum_(j=0)^(N-1) Jtilde_(a,j)(M)           (2.2)

for ANY chosen first input a. There is no remaining first average
and no extra 1/N outside this last sum. The inverse Fourier matrix
still supplies its own 1/N INSIDE each raw Jtilde. For charge-zero T,

    Jtilde_(a,j)=(1/N)sum_(b,q)
                        Q_N^(jq)T_(a-q,b+q;a,b).     (2.3)

Thus fixing a does not force q=0 and does not remove the second
momentum coordinate. The original first output row is essential.

The specified proper-root partial lift with Q^(jq)/N has the same
values in (2.2) at every original root. Off root its inverse need
not equal V(Q)^-1. Equation (2.1) with the whole inverse and (2.2)
with the root/proper-root inverse have these stated different scopes.
Their q-normal source jets are not silently identified.

## 3. A whole balanced Ward contraction for the source change

This section is an exact finite-matrix identity, before jets. It
uses the actual balanced finite K,F matrices at whole Q,M. Put

    D_K(C)=K C K^-1-C,
    D_F(C)=F C-K^-1 C K F,
    delta C=(D_K(C),D_F(C)), p(C)=Tr C/N.            (3.1)

At a genuine Hopf fiber these are the actual Hopf-adjoint rows.
Elsewhere (3.1) remains its specified compressed finite-matrix
formula; its whole network defects must be retained. Work only
over the localization where Q^l-1 is a unit for 0<|l|<N.
These units do not invert 1-Q^N.

For X=(X_K,X_F), set

    O(X)_(i,j)=(X_K)_(i,j)/(Q^(j-i)-1), i!=j,
    O(X)_(i,i)=0,
    d_k(X)=(X_F)_(k,k-1)/(1-Q^k), 1<=k<N.

Let Q_k be the centered diagonal step

    (Q_k)_(i,i)=(N-k)/N-1_(i>=k),
    h(X)=O(X)+sum_(k=1)^(N-1) d_k(X) Q_k.          (3.2)

Off-diagonal recovery is immediate from D_K. The selected F entry
has NO off-diagonal pollution, since both left F and right F have
only one arrow in that direction:

    (D_F C)_(k,k-1)
            =(1-Q^k)(C_(k-1,k-1)-C_(k,k)).         (3.3)

Telescoping the centered steps proves the WHOLE identity

    h delta C=C-p(C)I,   p h=0,   delta I=0.        (3.4)

In particular the actual image complex End -> im delta contracts
onto the scalar line. No cokernel assertion is made for the entire
unrestricted two-row space. No integral-factorial basis change has
been introduced; this is the original balanced head.

Write

    Q_a=e_a 1^t, e=(1/N)1 1^t,
    gamma_a(C)=lambda_a(C)-Phi(C)=Tr[(Q_a-e)C],
    b_a(X)=gamma_a(h(X)).

Since gamma_a(I)=0, applying gamma_a to (3.4) gives

    lambda_a-Phi=b_a delta                              (3.5)

as an exact WHOLE source/current identity. For the actual reclosed
matrix this says

    sum_j Jtilde_(a,j)-Phi(C)=b_a(delta C).          (3.6)

At its root Hopf fiber delta C_N=0, so (3.6) becomes (2.2).
For whole q/M auxiliary arrays, or inserted Green/current coupons,
the right side records the actual remaining closure/current row;
it is not discarded by an off-root Schur argument.

Normal derivatives follow by differentiating (3.5). In Taylor
coefficients at any specified actual normal path,

    gamma_a(C_n)=sum_(i+j+k=n) (b_a)_i delta_j(C_k). (3.7)

This includes the derivatives of the whole operators, source and
unit denominators. For an uninserted scalar C_0 at first order,
delta_1(C_0)=0 because delta_t(I)=0 for all t, and delta_0 C_0=0.
Hence gamma_a(C_1)=(b_a)_0 delta_0(C_1). A current insertion
with nonscalar C_0 retains the other terms in (3.7).

On a full diagram use the original ordered Hopf/coprod and pivotal
row, including prefixes, to evaluate delta C. The whole frozen
pivotal cap is chi^-1 ptr_K M_(Z^J), not ptr_K by itself, with
Z=Q^N. Its exact moment-clock and divided rows are retained in
[the actual cap theorem](actual_divided_ward_closure_and_green_caps.md).
This source homotopy does not set those cap/Green endpoints to zero.

## 4. A polynomial root bound in the original balanced metric

Give the balanced head its flat positive metric and End its
Hilbert--Schmidt norm, with the orthogonal product norm on the two
current rows. The K-row inverse gap at Q_N is bounded by

    1/[2 sin(pi/N)] <= N/4.                        (4.1)

For the diagonal part integrate edge gradients from the middle
vertex m=floor(N/2), then subtract the mean. This is the SAME
centered step operator in (3.2); only its norm estimate changes.
For left edges k<=m,

    1/|1-Q_N^k| <= N/(4k).

The relevant tail-sum matrix is A_(i,k)=1/k for 1<=i<=k<=m.
With weights w_i=i^(-1/2), elementary sums give

    sum_(k>=i) A_(i,k)w_k <=3w_i,
    sum_(i<=k) A_(i,k)w_i <=2w_k.

The weighted Cauchy--Schwarz inequality then gives ||A||<=sqrt(6)<3.
The right half has the same estimate with k replaced by N-k.
The two edge sets and anchored outputs are disjoint; subtracting
the mean is orthogonal projection. Thus

    ||h_diag|| <=3N/4,   ||h||<=3N/4.              (4.2)

For completeness the matrix bound follows by writing
|sum_k A_ik x_k|^2 <= (sum_k A_ik w_k)
sum_k A_ik |x_k|^2/w_k and then summing i. This proves the estimate
without importing a Hardy inequality. Complex reciprocal phases
are bounded by the same positive kernel. No q-factorial condition
number has been omitted.

The original row difference has exactly

    ||Q_a-e||_HS=sqrt(N-1).

Consequently its actual source primitive satisfies

    ||b_a|| <=(3N/4)sqrt(N-1).                    (4.3)

These are root metric bounds for this specified Ward/source map,
not bounds on the whole word or the geometric quantum period.
They make no uniform-neighborhood estimate for its normal units.

## 5. Choosing a good first-position anchor at every large level

Assume the established geometric framing model has a nonempty
regular algebraic chart for (A,p_e), with nondegenerate Fourier
normal block as in
[the actual Fourier construction](actual_fourier_polarized_geometric_normal_block.md).
This is its stated complete positive geometric/marked branch
input, not a new conclusion from (1.1). Over the fixed marked
representation/half-density cover, remove every denominator and
critical discriminant used for that chart. These are finitely
many nonzero algebraic functions on its selected connected component.
For a finite algebraic marking cover, take their nonzero field
norms first, then clear denominators on the rational (A,p_e) chart.
Since A=1/(1+s) is a nonconstant
framing coordinate, only FINITELY many A-values have their entire
fiber excluded. Explicitly, clear denominators of each defining
function as a polynomial in the other coordinate; a fiber is
identically zero only when all its coefficient polynomials in A
vanish. They have finitely many common roots.

Choose a root of unity A_*=exp(2pi*i p/d) outside that finite set,
with 0<p<d, gcd(p,d)=1. Its finite marked-cover lifts are retained.
There is no assertion that the particular choice A_*=-1 is good
for every knot. Set

    a_N=floor(pN/d), r_N=pN-d a_N in {0,...,d-1}.

Then a_N is an original physical head index, and

    A_N=Q_N^(a_N)=A_* exp[-(r_N/d)H_N],
    H_N=2pi*i/N.                                   (5.1)

Along each residue class of N modulo d, r_N is constant. The
classes may be refined by every previously retained parity/phase
modulus; no existing root sign or source branch is reset. The
selected good geometric point deforms on its fixed marked cover
to A_N for all sufficiently large N; the remaining framing/
Fourier coordinate is still free on a nonempty open. Formula
(2.2) therefore computes the SAME original root period using a
good fixed first-position sequence and just one exterior j sum.
Existence of this formal geometric branch does not prove its
survival in that last selected finite sum.

The WHOLE clock before normal differentiation is

    A=Z^(p/d) Q^(-r_N/d), Z=Q^N,                  (5.2)

on its MARKED power cover: the root value of Z^(p/d) is A_*.
One may realize it with v^d=Q, W^d=Z, W=v^N and A=W^p v^(-r_N).
This equals Q^(a_N) exactly on the actual power graph. Keeping
Z and its phase branch is essential. Replacing its marked value
by the constant A_* FIRST would lose

    D_Q log A=a_N,

and would give only -r_N/d instead. Thus residue-class root
selection does not identify off-root q-normal germs. Equation
(3.7) and the whole inverse must be used for those germs.

## 6. Scalarity is necessary, and the source is not a diagonal probe

There is an actual WHOLE auxiliary counterexample even for the
one-positive-crossing unknot. At N=2 use x=-M/q, Q=q^2 and remove
only the common Cartan scalar as in the actual residual matrices.
In the ordinary F-shift frame its checked crossing is

    Rplus=[[1,0,0,0],
           [0,0,x^-1,0],
           [0,x^-1,1-x^-2,0],
           [0,0,0,Q*x^-2]].

The frozen cap is g=x^-1 diag(1,Q); the original zero-framing
multiplier is theta^-1=x. Taking the literal partial trace gives

    C(Q,M)=d_2(M)diag(1,1+Q(Q^2-1)/M^2),
    d_2(M)=i M/(1+M^2).                              (6.1)

The balanced diagonal frame does not change this diagonal cut.
At Q=-1 it equals d_2(M)I, including the original complete value.
Nevertheless the whole source difference and its first normal are

    gamma_0 C=-d_2(M) Q(Q^2-1)/(2M^2),
    D_Q(gamma_0 C)|_(Q=-1)=d_2(M)/M^2 !=0.           (6.2)

Here M is held fixed and the original phase i is fixed. At M=1
this normal value is i/2. Equation (3.5) reproduces (6.2) exactly
from (D_F C)_(1,0)/(2(1-Q)). Thus the whole Ward row genuinely
survives differentiation; scalar root closure cannot erase it.
Using the ordinary generic ribbon cap instead of the specified
frozen auxiliary cap would be a different off-root source.

For the literal two-cut unknot T is the flip. Inserting the actual
matrix-unit coupon X=E_00 at the second identity wire gives the
one-cut matrix C=X. Its selected average is Phi(C)=1/N, whereas

    lambda_0(C)=1, lambda_a(C)=0 for a!=0.

The fixed-input reduction therefore fails without scalarity.
Its exact discrepancy is (3.5), with the nonzero F/K current
of that specified coupon. Similarly a charged C=E_(c,a), c!=a,
has lambda_a(C)=1 while its diagonal probe at a is zero. Removing
the output sum would change the current/source problem even when
the eventual uninserted knot matrix is scalar.

[The exact audit](../experiments/audit_actual_one_index_fourier_source.py)
and [saved results](../experiments/actual_one_index_fourier_source_results.json)
check the whole two-row contraction and sources, actual signed
root braid/Fourier tensors at complete and generic meridians,
off-root current defects, metric bounds and marked clock exponents.
No hyperbolic-volume or global selected-cycle conclusion is claimed.
