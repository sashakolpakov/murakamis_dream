# Whole clock functions require an endpoint extension

Independent algebraic proof and actual-source audit, 27 October 2026.
The exact endpoint-completed Jackson current retains its input
function, rather than only that function's finite matrix value.
There is a precise obstruction to forgetting the function and an
explicit flat tower that retains the additional endpoints. This is
the usual infinite-order quantum-shift phenomenon; no novelty claim
is made for the algebraic simplicity statement.

## 1. The actual whole current and its retained function

On one actual Frobenius residue string, let
\[
 C_Q=c Z^R,\quad 0\le R\le N,\quad Z=Q^N,
 \quad eC_Q=ZC_Qe,\quad fC_Q=Z^{-1}C_Qf.
\]
Here c=Q^s for the original physical clock. The actual divided
e(q),f(q) have nonzero interior arrow coefficients at the root.
Invert just those finite arrows and set the absent endpoint arrow
to zero. This defines regular original whole germs e^dagger,f^dagger
with
\[
 e^\dagger e=I-P_0,\qquad f^\dagger f=I-P_N.          \tag{1}
\]
No inverse of the whole nilpotent matrix is asserted.

For a RETAINED function g, the exact whole current is
\[
 \mathcal J_Z(g)=
 \frac{-e^\dagger[e,g(ZC_Q)]
              +P_0 f^\dagger[f,g(C_Q)]}{1-Z}
       =\frac{g(C_Q)-g(ZC_Q)}{1-Z}.                 \tag{2}
\]
The full proof and its actual matrix/source implementation are in
[the endpoint-completed normal clock current](endpoint_completed_normal_clock_euler_current.md).
For an independent check of the order, put D=g(C_Q)-g(ZC_Q).
The first numerator is (I-P_0)D, and the second is
P_0(I-P_N)D=P_0D. Their sum is D. This also identifies precisely
where the lower endpoint is repaired.

Polynomials and Laurent polynomials are always allowed. Rational
or marked analytic functions require their denominators or domains
at EVERY shifted spectrum used in (2). The root value is
C_0 g'(C_0), with any explicit coefficient parameter held fixed.
An additional coefficient derivative is a separate operation.

The inverse arrows are regular actual q-germs because their root
coefficients are r-R+1 and R+1, respectively (with r=N here),
times fixed nonzero root units. This is not a generic module inverse
or a Hopf-natural contraction on arbitrary tensor summands.

## 2. No finite-dimensional compatible function quotient at generic Z

Let K be a characteristic-zero field, let Z in K^times have infinite
multiplicative order, and put F=K[x,x^-1]. The shift is
sigma(g)(x)=g(Zx), fixing K. Then

**Claim.** A nonzero ideal I with sigma(I) contained in I is F.
Consequently F has no nonzero finite-dimensional quotient carrying
the induced whole shift or Jackson operator
D_Z=(1-sigma)/(1-Z).

Proof. Write I=(p), multiplying its Laurent generator by a unit
to make p an ordinary polynomial with nonzero constant term.
The divisibility p(x)|p(Zx), and equality of degrees, give
p(Zx)=a p(x) for a nonzero scalar a. If p has positive degree,
choose a root r over an algebraic closure. It is nonzero. Then
all Z^j r, j>=0, are roots, contradicting their infinitude.
Thus p is a nonzero constant and I=F. This also proves
sigma(I)=I; one-sided stability was sufficient. Because 1-Z is
a field unit, Jackson stability and shift stability are equivalent.

The statement concerns a COMPATIBLE FUNCTION-ALGEBRA quotient at
generic Z. It does not prohibit finite root modules, finite matrix
representations, or the actual cyclic/Steinberg source. Evaluation
on a finite spectral string is perfectly valid; it simply forgets
the endpoint value needed for the next shift.

## 3. The actual minimal-polynomial certificate and its normal order

For the actual spectral string let
\[
                  P_N(x)=\prod_{r=0}^N(x-cZ^r).
\]
Then P_N(C_Q)=0 exactly, whereas
\[
 P_N(ZC_Q)=P_N(cZ^{N+1})P_N^{\mathrm{top}},\qquad
 P_N(cZ^{N+1})=
       c^{N+1}Z^{N(N+1)/2}\prod_{j=1}^{N+1}(Z^j-1). \tag{3}
\]
Here P_N^top denotes the last BLOCK PROJECTOR, not the polynomial.
Every other entry of P_N(ZC_Q) is zero. Thus the retained function
P_N and the zero function have the SAME actual matrix value, but
their currents differ. With delta=1-Z, (2)--(3) give
\[
 \mathcal J_Z(P_N)=(-1)^N c_0^{N+1}(N+1)!
                 \delta^N P_N^{\mathrm{top}}+O(\delta^{N+1}). \tag{4}
\]
The defect is invisible to every normal truncation below order N.
This is an exact reason why a bounded-order jet calculation cannot
discard the whole clock function. It does not contradict bounded-jet
reconstruction in a separately fixed bounded-complexity pole lattice:
the degree of P_N grows with N.

## 4. A flat confluent tower supplies the missing endpoints

There is a constructive integral alternative to an impossible fixed
finite quotient. Let R=k[[delta]], Z=1-delta, and c in R^times.
Put
\[
 P_L(x)=\prod_{r=0}^L(x-cZ^r),\qquad
              A_L=R[x,x^{-1}]/(P_L),\quad L\ge0.     \tag{5}
\]
The polynomial is monic with unit constant term, so A_L is R-free
of rank L+1. Forgetting the last endpoint gives A_L to A_(L-1).
The exact Jackson operator induces
\[
                      D_Z:A_L\longrightarrow A_{L-1}. \tag{6}
\]
Indeed D_Z P_L is integral: every coefficient of
P_L(x)-P_L(Zx) is divisible by 1-Z. Over k((delta)) it vanishes at
c,cZ,...,cZ^(L-1), so is divisible by the monic P_(L-1).
Monic division shows the quotient is already integral over R.
The same argument applies to a multiple of P_L, or directly to
the Jackson product formula. Thus (6) is independent of a representative.

At the root,
\[
 A_L/delta A_L=k[x]/(x-c_0)^{L+1},\qquad
           D_Z\longmapsto x\partial_x:A_{L,0}\to A_{L-1,0}.
                                                               \tag{7}
\]
These are CONFLUENT jet lattices. They are not the ordinary root
matrix image: the latter sets C_0=c_0 I and kills all positive
powers of x-c_0. For example x-c_0 has zero ambient root matrix
value, but its Jackson image has root value c_0 I.

For the actual original interval L=N, one extra endpoint suffices
for one whole Jackson action; j actions use A_(N+j) to A_N.
The compatible inverse tower retains all such endpoint values
without divided Vandermonde or idempotent denominators. It is an
infinite completed FUNCTION object, not an extra finite quantum
color or a tensor-intertwining theorem. The functions supplied to
it must still be the specified actual whole functions, with their
marks; arbitrary formal sections are not substituted for them.

### The exact spectral index and its flat source extension

The integral distinction from the ambient finite matrix values can
be computed exactly. Use the Newton basis
\[
 p_j(x)=\prod_{u=0}^{j-1}(x-cZ^u),\quad 0\le j\le L.
\]
The monomial-to-Newton change of basis is unitriangular. Its
evaluation matrix V_(rj)=p_j(cZ^r), r=0,...,L, is lower triangular:
\[
 V_{rj}=c^jZ^{j(j-1)/2}
                   \prod_{k=r-j+1}^r(Z^k-1)
             =\delta^j W_{rj}\quad(r\ge j).          \tag{8}
\]
At the root W_(rj)=(-c_0)^j(r)_j, with falling factorial (r)_j.
Its diagonal entries (-c_0)^j j! are units. Thus W is invertible
over R and the evaluation map A_L to R^(L+1) has EXACT Smith
factors
\[
          1,\delta,\ldots,\delta^L,
       \qquad v_\delta(\det V)=L(L+1)/2.             \tag{9}
\]
This identifies the confluent source lattice lost by ordinary
ambient root evaluation. The kernel of forgetting the last
endpoint is explicitly
\[
 0\longrightarrow R\,P_{L-1}\longrightarrow A_L
                     \longrightarrow A_{L-1}\longrightarrow0.
                                                               \tag{10}
\]
Multiplication by x acts on this rank-one line by cZ^L. Its sole
nonzero generic spectral value is at the new endpoint, namely
\[
 P_{L-1}(cZ^L)=c^LZ^{L(L-1)/2}\prod_{j=1}^L(Z^j-1),
\]
of exact order L, with leading coefficient (-c_0)^L L!.

There is a second, different exact sequence giving an integral
Jackson primitive:
\[
 0\longrightarrow R\cdot1\longrightarrow A_L
                     \xrightarrow{D_Z}A_{L-1}\longrightarrow0.
                                                               \tag{11}
\]
Indeed D_Z x^j=[j]_Z x^j and [j]_Z is a root unit for 1<=j<=L.
The classes x,...,x^L form a basis of A_(L-1), because x is a
unit there. This proves surjectivity. If a degree-at-most-L
representative g has D_Z g=0 in the target, D_Z g must be a scalar
multiple of P_(L-1); its zero constant term and the unit constant
term of P_(L-1) force that scalar to vanish. Thus g is constant.
The whole primitive requires no division by delta.

Both actions are explicit in the same Newton basis:
\[
 x p_j=p_{j+1}+cZ^j p_j,\qquad
 D_Zp_j=[j]_Z x p_{j-1}\quad(j\ge1).                \tag{11a}
\]
The first identity makes the retained clock a bidiagonal matrix;
at delta=0 it is the single Jordan block c_0 I plus its nilpotent
shift. The second follows by factoring
p_j(Zx)=Z^j(x-cZ^{-1})p_{j-1}(x). These give constructive finite
flow equations on the confluent lattice, without diagonalizing by
singular idempotents. The root of every [j]_Z is the nonzero scalar
j, so the primitive is regular at the marked root at each fixed L.
Its whole rational formulas retain the other zeros of [j]_Z;
no common growing-L analytic neighborhood or bound is asserted.

These regular FUNCTION lattices are not every actual regular
matrix insertion. For example the original block-number matrix
R is regular, while the marked function
Log(x/c)/Log Z representing it on this spectrum contains a divided
normal factor. Saturating the evaluation lattice allows such
functions but can introduce poles in their Jackson currents:
already g=(x-c)/delta has a regular finite matrix value and
D_Z g=x/delta. Therefore fractional normal/current lattices and
their endpoint compensations remain part of the data. Equations
(9)--(11) do not discard those factors or assert that every matrix
coefficient is a regular scalar function of the clock.

## 5. The root primitive has a tame actual coherent norm

In the original divided basis, the Fr coherent metric is
\(\|v_k\|^2=\binom Nk\). The normalized inverse-arrow lengths are
\[
 \frac1{\sqrt{(k+1)(N-k)}}\quad(e^\dagger),\qquad
 \frac1{\sqrt{k(N-k+1)}}\quad(f^\dagger).
\]
Their largest values occur at the extreme arrows. Consequently
\[
        \|e^\dagger_0\|=\|f^\dagger_0\|=N^{-1/2},
                  \quad\|P_0\|=\|P_N\|=1.           \tag{12}
\]
This positive bound is for the ROOT inverse-arrow operators in the
specified actual Frobenius metric. It gives neither a uniform whole
normal-neighborhood estimate nor a norm bound for arbitrary inserted
functions and all full braiding operators. In particular it does
not remove the separate exponential endpoint-row norms computed in
[the actual relative source period](actual_frobenius_relative_endpoint_period.md).
The integrated row can still have cancellations; all endpoint and
source normalization factors remain.

The conclusions are therefore compatible: a tame finite root
primitive exists, while exact whole functional transport requires
the additional endpoint extension. A comparison with the actual
network's geometric framing currents must preserve that extension,
its true co-source and the ordinary/divided Hopf endpoint terms.

[The exact audit](../experiments/audit_whole_clock_endpoint_extension.py)
checks the integral confluent tower, the actual spectral-polynomial
defect and its sign/order, and the root primitive norms.
The independent
[confluent-lattice audit](../experiments/audit_whole_clock_confluent_lattice.py)
checks the Newton evaluation, Smith factors, primitive kernel and
new-endpoint line explicitly.
