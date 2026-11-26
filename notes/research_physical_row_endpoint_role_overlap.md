# Comparing the two endpoint roles on common positive charts

Private written proof, 16 November 2026.

The regular continuation theorem constructs a source-normalized mode
by treating either nonzero endpoint as the degree variable. Here the
two constructions are compared on a common domain. Exact joint
physical data give an exponentially small normalized difference on
a two-variable real seed neighborhood. Holomorphic propagation then
compares them on every compact subset of a connected common domain
where both action bounds hold.

The shared seed and common phase are hypotheses. This result does
not identify arbitrary off-grid representatives merely because their
physical jets agree. It neither constructs a global glued scalar
nor removes window interfaces, endpoint packets or exterior currents.

## 1. The two constructions and the shared seed

Put
\[
 h=N^{-1},\quad X_j=(j+\tfrac12)h,\quad Y_k=(k+\tfrac12)h,\qquad
 C(X)=2\cos(2\pi X),\qquad t(X)=\pi-2\pi X .
 \tag{1}
\]
Take one representative from the pinned regular continuation theorem
with the first endpoint as degree variable, and one with the roles
interchanged. In common centered coordinates write them as
\[
 A_N(X,Y)=\mathcal F_{N,1}^{\sigma_1}(X,t(Y)),\qquad
 B_N(X,Y)=\mathcal F_{N,2}^{\sigma_2}(Y,t(X)).
 \tag{2}
\]
The choices of anchors, first-degree windows and designated signs
may differ. Every representative is the actual normalized construction
with its exact one-sided repair; it is not a raw Sears cutoff.

Require two fixed intervals
\[
 I_X,I_Y\Subset(0,1/2)
 \tag{3}
\]
and fixed complex neighborhoods \(U_X,U_Y\) of the respective
intervals, with buffers, such that:

1. \(I_X\) lies in the matched first window of \(A_N\), and \(I_Y\)
   lies in the matched first window of the transposed construction
   \(B_N\). These intervals have positive length, independent of \(N\).
2. Both constructions are holomorphic on a neighborhood of
   \(\overline{U_X}\times\overline{U_Y}\). In particular the local
   second-parameter domain for \(A_N\) contains \(t(U_Y)\), and
   that for \(B_N\) contains \(t(U_X)\).
3. Their continued phases agree there with the original symmetric
   phase
\[
                         \Psi(X,Y)=\psi(t(X),t(Y)).
 \tag{4}
\]
   Both phase-normalized representatives have uniform \(e^{o(N)}\)
   bounds on this buffered seed product.

The third condition holds on sufficiently thin real seed products
when the two regular constructions use the same original phase:
each designated-half estimate also supplies a fixed thin opposite
collar. The intervals in (3) must nevertheless be shared as stated.
A local second-parameter chart need not contain any other physical
row.

At every joint seed node, the exact full-jet identities give
\[
 \partial_X^a\partial_Y^b A_N(X_j,Y_k)
 =\partial_X^a\partial_Y^b B_N(X_j,Y_k)
 =\left.\partial_X^a\partial_Y^b
          K_N(C(X),C(Y))\right|_{(X_j,Y_k)},
 \qquad 0\le a,b\le1.
 \tag{5}
\]
Here \(X_j\in I_X,Y_k\in I_Y\). These are double physical
spectral rows for all sufficiently large \(N\).

To verify (5), the first construction has the exact holomorphic
identities
\[
 A_N(X_j,Y)=F_j(C(Y)),\qquad
 \partial_XA_N(X_j,Y)=C'(X_j)\widehat G_j(C(Y)).
 \tag{6}
\]
The source normal \(\widehat G_j\) has the value and first
spectral normal of the original \(G_j\) at every physical second
row. Differentiate (6) in \(Y\) and use this identity. The
transposed construction gives the same four entries by symmetry
of the original kernel. In particular the mixed entry is
\[
 C'(X_j)C'(Y_k)\,
             \partial_z\partial_wK_N(c_j,c_k).
 \tag{7}
\]
No assertion that a first normal follows from values alone is used.
The equality also survives multiplication by any common holomorphic
spectator, with its full mixed product rule.

## 2. Two successive dense-grid estimates

We record the analytic estimate used at each stage. Let \(f_N\) be
holomorphic on a fixed complex neighborhood of a real interval,
bounded there by \(e^{o(N)}\). Suppose on its centered nodes
\[
                        |f_N(X_j)|\le e^{-\kappa N}
 \tag{8}
\]
for a fixed \(\kappa>0\). Then \(f_N=O(e^{-\kappa' N})\)
on a smaller open neighborhood of a shorter interior interval,
for some \(\kappa'>0\). All statements are uniform in any
buffered holomorphic parameters.

For clarity, subtract the finite cardinal correction
\[
                q_N(X)=\sum_j f_N(X_j)
                                  \operatorname{sinc}(N(X-X_j)).
 \tag{9}
\]
On a sufficiently thin fixed neighborhood,
\[
 |q_N(X)|\le CN e^{-\kappa N+\pi N|\Im X|}
                                      \le e^{-\kappa N/2}.
 \tag{10}
\]
Thus \(f_N-q_N\) has exact zeros at every selected node and
is still bounded by \(e^{o(N)}\). Take a disk inside that thin
neighborhood and \(cN\) nodes in a smaller concentric disk.
The corresponding disk Blaschke factors have modulus at most
a fixed \(\vartheta<1\) on a still smaller disk. Dividing out
these factors and using the maximum principle gives
\[
                  |f_N-q_N|\le e^{o(N)}\vartheta^{cN}.
 \tag{11}
\]
Finite covering and buffered Cauchy estimates prove the assertion,
including all fixed derivatives. For exact nodal zeros omit (9).
This is the dense-zero argument of the pinned normal theorem,
with its approximate-zero step made explicit.

Set
\[
                 D_N(X,Y)=e^{-N\Psi(X,Y)}(A_N-B_N).
 \tag{12}
\]
It is holomorphic and bounded by \(e^{o(N)}\) on the seed
product. Fix a physical \(Y_k\in I_Y\). Equation (5) gives
exact zeros \(D_N(X_j,Y_k)=0\) for \(X_j\in I_X\).
The exact-zero case of (11), uniformly in \(k\), gives a fixed
open \(U_X'\Subset U_X\) and \(c_1>0\) such that
\[
                       \sup_{X\in U_X'}|D_N(X,Y_k)|
                                             \le e^{-c_1N}.
 \tag{13}
\]

Now fix \(X\in U_X'\) and regard \(D_N(X,Y)\) as a
holomorphic function of \(Y\). Its values at the second grid
are exponentially small by (13), although they need not be
zero. Apply (9)--(11) in \(Y\), using \(X\) as a uniform
holomorphic parameter. On a fixed smaller product,
\[
                 |D_N(X,Y)|\le C e^{-c_2N}.
 \tag{14}
\]
All fixed mixed derivatives obey this estimate after further
fixed buffers. This proves a two-complex-variable seed estimate;
an estimate merely on the real product would not suffice for
the propagation below.

Only the value entries in (5) are needed for (14). The remaining
entries establish that the compared constructions still represent
the original full physical source. No independent jet has been
discarded to obtain the analytic comparison.

## 3. Propagation on a connected common domain

**Theorem.** In addition to the shared seed conditions, let
\(\mathcal W\subset\mathbb C^2\) be a connected open common
domain containing the seed product and a target compact set.
Require a single holomorphic phase \(\Psi\) on \(\mathcal W\),
equal to (4) on the seed, and assume that \(A_N,B_N\) are
holomorphic there with
\[
 \sup_K\bigl(|e^{-N\Psi}A_N|+|e^{-N\Psi}B_N|\bigr)
                                      \le e^{o_K(N)}
 \quad\text{for every }K\Subset\mathcal W.
 \tag{15}
\]
For the one-sided representatives this means that the common
domain stays in their designated half-domains and permitted
opposite collars, or elsewhere where (15) has separately been
proved. Then for every \(K\Subset\mathcal W\) there is
\(c_K>0\) such that
\[
 \sup_K\left|
   \partial_X^a\partial_Y^b
       \bigl[e^{-N\Psi}(A_N-B_N)\bigr]\right|
                             \le C_{K,a,b}e^{-c_KN}
 \tag{16}
\]
for every fixed \(a,b\). The exponent may be decreased when
derivatives are taken.

**Proof.** Equation (14) supplies one open seed ball. Cover
compact paths from that ball to \(K\) by finitely many buffered
Euclidean balls in \(\mathcal W\). The three-balls estimate
for a holomorphic function is the usual three-circles estimate
on each complex line through the center: a bound on an inner
ball and a bound on an outer ball give the interpolated bound
on an intermediate ball. Thus an inner \(e^{-cN}\) bound and
the \(e^{o(N)}\) outer bound from (15) give an
\(e^{-c'N}\) intermediate bound, with \(c'>0\).
Choose the next center in the known smaller ball and repeat.
A finite chain reaches each compact target neighborhood;
compactness gives a finite collection of chains. Every step
multiplies the positive exponential constant by a fixed
positive number, while its \(o(N)\) term stays negligible.
Buffered Cauchy estimates prove (16). \(\square\)

The statement is uniform for buffered holomorphic exterior parameter
families when the domains, phase, source identities and bounds above
are uniform. Their fixed derivatives follow by Cauchy on the larger
parameter compacts.

The same conclusion holds for the two unrepaired baselines under
the same common-domain bounds. Their actual nodal value errors from
the regular continuation theorem are exponentially small relative
to the physical rows. On a buffered real bulk seed the normalized
physical rows have \(e^{o(N)}\) size. Hence the first stage uses
the approximate-zero argument (9)--(11), rather than the exact-zero
case; the rest of the proof is unchanged.

## 4. Scope for source transport

The theorem compares two actual endpoint-role constructions. It
allows different anchors and different matched windows, provided
the fixed shared seed intervals in (3) remain. It cannot be applied
when the local second domains omit the other seed window, when the
target component is disconnected from the seed, or when the
continued phases differ by an unrecorded branch or constant.

On any overlap satisfying the theorem, a common holomorphic spectator
multiplies (16) by its actual bound. Thus an interface primitive or
contour integral still needs that bound and its original orientation;
the theorem does not declare its integral zero.

In particular the exact window identity in the continuation source
uses \(\Phi^\sharp_{N,I}\), the finite residue expression with
\(\widehat G_j\). Its difference from the original free-endpoint
window trace is \(P_N(w)\) times a holomorphic function. Equality
with the original follows only after the prescribed complete
second trace, with all spectator normals. The present overlap
estimate does not change that scope.

No first-angle evenness of the one-sided repairs is asserted.
No full-lens substitution, whole-grid interpolation, simultaneous
fold construction, global Cousin gluing or global current bound
follows from (16). All unmatched rows, angular endpoint packets,
opposite-side closures and exterior currents remain in the
original problem.

## Direct sources and author scope

Both complete direct texts and their used implications were read at:

* [Regular positive continuation](research_physical_row_regular_positive_continuation.md),
  SHA256 3a7d81d55f60396c2e3058d5ebe967ae625ff47c4b527b4e102e37fa8f28d644:
  actual repaired and baseline modes, full-normal window identities,
  common phase and designated-half bounds, and the precise
  \(\Phi^\sharp\) versus original trace distinction.
* [Actual slit normal connection](research_physical_row_slit_normal_connection.md),
  SHA256 a5084adb4ff25cb08020e5f9485bd1aaea5b49468c6ab0af311ebc1c0c504d99:
  actual normal representatives and original mixed-jet equality,
  normalized bulk bounds, dense zeros and analytic propagation.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
