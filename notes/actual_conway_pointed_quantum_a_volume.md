# The pointed quantum \(A\)-period has the strict Conway knot volume

31 October 2026. Internally reviewed research corollary.
This gives an operator-side expression for the original invariant and
proves its volume limit for the fixed long-twist knots of the
[strict Conway tree theorem](actual_conway_all_strict_tree_long_twist_volume.md).
The operator belongs to the actual literature ADO annihilator ideal.
Its finite pointing is fixed by ordinary small-color periods; it is not
chosen separately at each root of unity.

The conclusion concerns the selected complete period and its norm.
Identification of the selected classical main-meridian geometric factor
or of an entire quantum module is a separate stronger problem.

## 1. The knot, the literature family and the coordinates

Fix a strict literal Conway expression \(\tau=C(FG)\) in the sense of the
linked theorem. Fix all integer twist weights \(\mathbf n\) beyond that
theorem's threshold, with the original endpoint pairing a knot and with
no internal closed component. Put
\[
 K=K_\tau(\mathbf n),\qquad
 V=\operatorname{Vol}(S^3\setminus K)>0,\qquad
 q_N=\exp(\pi i/N).
\tag{1}
\]
The expression and weights are fixed before \(N\) tends to infinity.
Only the auxiliary crossing-circle cusps are filled; the main knot cusp
stays unfilled. The limit below runs through all sufficiently large
integer levels, with both parities and composite levels retained.

Use the zero-framed reduced ADO family defined by the original unrolled
crossings and pivotal trace. Its conventions and its comparison with the
original reduced enhanced Kashaev evaluation are proved in the
[ADO pointing note](kashaev_ado_pointing.md).
There are two different coordinates:
\[
 x=q_N^\alpha,\qquad M=-q_Nx,\qquad
 F_N(M)=f_N(-q_N^{-1}M),
\tag{2}
\]
where \(f_N(x)\) denotes the raw unrolled family and \(F_N\) the marked
meridian family. At the complete color \(\alpha=N-1\), the raw coordinate
is \(x=-q_N^{-1}\), and the marked coordinate is \(M=1\).
At the quotient color \(\alpha=j-1\), they are
\(x=q_N^{j-1}\) and \(M=-q_N^j\).

The [single-component quotient-color proof](root_orbit_pointing.md)
gives the exact identities
\[
 F_N(-q_N^j)=C_j(q_N)\quad(1\le j\le N),\qquad
 F_N(1)=C_N(q_N)=K_N(K).
\tag{3}
\]
Here \(C_j(q)\) is the actual zero-framed reduced \(j\)-dimensional
period, with unknot value one. Each fixed \(C_j\) is a Laurent polynomial
in the recorded quantum parameter, analytic at \(q=1\), and \(C_j(1)=1\).
The proof uses the invariant quotient of the original color and the
single-cycle cut trace; it is not an extrapolation from a link component.

The literature all-level ideal is defined by annihilation of the actual
ADO family at all but finitely many levels, in the \(q\)-Weyl algebra.
This is the convention of
[Brown–Dimofte–Garoufalidis–Geer, equation (1.5)](https://arxiv.org/html/2005.08176).
Their holonomicity and ideal-comparison theorems are not proof inputs
here. The repository's finite cut-state argument supplies existence
directly, as recalled next.

## 2. A genuine operator exists before the period is evaluated

The [finite cut-state annihilator theorem](finite_sum_annihilator.md)
constructs a nonzero level-independent operator for every knot.
Its auxiliary generic-\(q\), \(N\)-dimensional cut matrices specialize to
the actual root state; they are not asserted to define a topological
invariant away from the root. Their finite summands are aligned proper
\(q\)-hypergeometric products on the original integral support polytope.

The essential boundary safeguards are part of that proof. With \(s_0\)
internal summation variables, the span of the actions
\[
 x^a z^c T^b S_1^{\beta_1}\cdots S_{s_0}^{\beta_{s_0}},
 \qquad 0\le a,c,b,\beta_i\le R,\qquad z=q^N,
\tag{4}
\]
has dimension \(O(R^{s_0+2})\), including the zero-extended boundaries.
A rank-\(r\) boundary stratum has \(O(R^r)\) possible labels and a
remaining monomial span \(O(R^{s_0+2-r})\).
The \(O(R^{s_0+3})\) formal operators therefore give a nonzero relation
without internal multiplication variables.
Taking the first nonzero coefficient in its expansion at \(S_i=1\)
via finite exponential moments produces an actual relation for the sum,
even when direct summation of the first relation vanishes.
Finally, any common factor \((z+1)^h\) is canceled over generic \(q\)
before setting \(z=-1\). The lift is regular at \(q_N\).
These steps preserve the finite support and do not divide by a zero
root-specialized factor.

Transport the resulting raw-\(x\) operator by the exact substitution
\(x=-q^{-1}M\). In marked reduced coordinates, choose any fixed nonzero
actual annihilator and clear its rational denominators:
\[
 P(q,M,T)=\sum_{i=0}^{d}a_i(q,M)T^i,\qquad
 TM=qMT,\qquad
 a_i\in\mathbb C[q^{\pm1},M^{\pm1}],\qquad d\ge1.
\tag{5}
\]
Remove a common shift if necessary, so \(a_0a_d\ne0\).
For all but finitely many \(N\), the actual equation is
\[
 \sum_{i=0}^{d}a_i(q_N,M)F_N(q_N^iM)=0.
\tag{6}
\]
An order-zero nonzero multiplication operator cannot annihilate the
nonzero actual family. Thus the positive order in (5) is automatic.

The localized skew polynomial ring over \(\mathbb C(q,M)\) is left
Euclidean. The actual nonzero annihilator ideal consequently has a
unique monic element of least order. One may use that generator, or any
other specified genuine annihilator, in everything below.
The finite existence proof does not claim an efficient algorithm for
the minimal generator or identify its classical symbol.
In particular, (5) is not defined by the rootwise ratio
\(F_N(q_NM)/F_N(M)\).

## 3. Fixed small colors determine the exact operator period

The following reconstruction is the
[all-level finite-pointing theorem](all_level_a_period.md), in the
marked \(M\)-coordinate of (2). For a fixed integer \(j\ge1\), (3) and
(6) imply that the Laurent polynomial
\[
 H_j(q)=\sum_{i=0}^{d}a_i(q,-q^j)C_{j+i}(q)
\tag{7}
\]
vanishes at every sufficiently large \(q_N\) with \(N\ge j+d\).
It therefore vanishes identically. This derives the generic recurrence
from the actual root family and the quotient colors, without an
assumed equality of ADO and colored-Jones recursion ideals.

Write the collected leading coefficient as
\[
 a_d(q,M)=\sum_{(a,b)\in\mathcal S}c_{a,b}q^aM^b,\qquad
 A_q=\max_{\mathcal S}a-\min_{\mathcal S}a,\qquad
 D=\max_{\mathcal S}b-\min_{\mathcal S}b,\qquad
 s=|\mathcal S|.
\tag{8}
\]
Choose \(j_0=A_q+1\). For \(j\ge j_0\), the exponents \(a+bj\)
of \(a_d(q,-q^j)\) are distinct for distinct support pairs:
a collision with different \(b\)'s would give \(j\le A_q\).
Hence the leading coefficient is never identically zero on these
generic trajectories.

Let \(B_j(q)\) be the forward \(d\)-dimensional companion matrix of
(7), evaluated at \(M=-q^j\). Its first \(d-1\) rows shift the coordinates
left, and its last row is
\[
 -\frac{1}{a_d(q,-q^j)}
 \bigl(a_0(q,-q^j),\ldots,a_{d-1}(q,-q^j)\bigr).
\tag{9}
\]
Fix, once and for all,
\[
 \begin{aligned}
 c_0(q)&=(C_{j_0}(q),\ldots,C_{j_0+d-1}(q))^{\mathsf t},\\
 r_N(q)&=e_d^{\mathsf t}B_{N-d}(q)\cdots B_{j_0}(q).
 \end{aligned}
\tag{10}
\]
The generic recurrence gives \(r_N(q)c_0(q)=C_N(q)\) identically.
Consequently the operator period is
\[
 \boxed{\quad
 \mathscr P_N(P,c_0)
 =\operatorname{CT}_{t=0}
   \bigl[r_N(q_N(1+t))c_0(q_N(1+t))\bigr]
 =K_N(K).
 \quad}
\tag{11}
\]
Here \(\operatorname{CT}\) takes the constant coefficient of the
**whole** Laurent germ. Its product is regular, even if individual
companion factors have poles. No singular step is deleted or evaluated
by separately substituting a zero denominator.

Only a bounded number of quantum-parameter jets is needed. For all
sufficiently large \(N\), \(a_d(q_N,M)\) is nonzero and has at most
\(D\) zeros among the distinct orbit points \(-q_N^j\) in (10).
At any such step, \(a_d(q,-q^j)\) has vanishing order at most \(s-1\):
if a nonzero Laurent polynomial with \(s\) monomials and distinct
exponents vanished with multiplicity \(s\), its first \(s\) logarithmic
derivatives would contradict the Vandermonde determinant. Thus
\[
 B_N:=\sum_{j=j_0}^{N-d}
       \operatorname{ord}_{q=q_N}a_d(q,-q^j)
 \le B:=D(s-1).
\tag{12}
\]
This is a bound on moving-\(q\) tangencies, not merely fixed-\(q\)
meridian zeros.

Write
\[
 \begin{aligned}
 r_N(q_N(1+t))&=\sum_{\ell\ge-B_N}R_{N,\ell}t^\ell,\\
 J_k(N)&=[t^k]c_0(q_N(1+t)).
 \end{aligned}
\]
Then (11) is the finite formula
\[
 \boxed{\quad
 \mathscr P_N(P,c_0)=
       \sum_{k=0}^{B_N}R_{N,-k}J_k(N),\qquad B_N\le D(s-1).
 \quad}
\tag{13}
\]
Every \(J_k(N)\), \(0\le k\le B\), is bounded as \(N\to\infty\).
Its entries are \(q_N^kC_j^{(k)}(q_N)/k!\) for a fixed finite set of
colors, analytic near \(q=1\).
The operator, its order, its support, \(j_0\), and these initial
polynomials are fixed after the knot and its twist weights are fixed.
They do not vary to fit a level or a desired asymptotic.

## 4. The operator-period volume theorem and its peripheral factor

**Pointed quantum \(A\)-period theorem.** For the knot (1), for any
specified actual all-level annihilator (5) and the fixed pointing (10),
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
   \log\left|
       \sum_{k=0}^{B_N}R_{N,-k}J_k(N)
       \right|
 =V.
 \quad}
\tag{14}
\]
The same theorem holds for the localized minimum-order generator.
The expression inside the logarithm is nonzero for all sufficiently
large \(N\).

Proof: the exact whole-germ identity (11) identifies the left side
with the original invariant at every sufficiently large level.
The strict Conway theorem proves its nonzero asymptotic and the limit
(14) for the fixed long-filled knot. No additional choice of a
root-level solution, rank-one kernel, semisimplicity hypothesis, or
regular orbit is involved. This proof uses the already established
original source volume theorem; it does not claim a new asymptotic
estimate obtained directly from the companion matrix coefficients.

For the full literature ADO state, all peripheral data remain explicit:
\[
 \begin{aligned}
 \mathcal N_N(M)&=d_N(M)F_N(M),\\
 d_N(M)&=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}}
       =\eta_N\frac{M^{N-1}}{\displaystyle\sum_{r=0}^{N-1}M^{2r}},
       &\eta_N&=i^{N+3},\\
 d_N(1)&=\frac{\eta_N}{N},&
 \mathcal N_N(1)&=\frac{\eta_N}{N}\mathscr P_N(P,c_0).
 \end{aligned}
\tag{15}
\]
The last row evaluates the whole regular germ at \(M=1\).
At the reference point \(M=-q_N\), the full state instead has the
nonzero residue fixed in the pointing theorem. Replacing the full
state by an unspecified scalar normalization would lose this datum.

The full-to-reduced operator transport is the fixed Ore gauge
\[
 d_N^{-1}Td_N=g(q_N,M)T,\qquad
 g(q,M)=-q^{-1}\frac{q^2M^2-1}{M^2-1}.
\tag{16}
\]
Thus a full-state literature operator may first be transported to (5).
At \(M=1\), (15), rather than a formal substitution into the meromorphic
coefficient \(g\), specifies its actual period. Since
\(|\eta_N|=1\) and \(\log N/N\to0\), the full-state period has the same
volume limit (14). This keeps the generic peripheral factor and its
completion lattice, not only its exponential rate.

## 5. A positive determinant version of the same operator limit

There is also a positive algebraic left side, from the
[pointed Gram-period theorem](pointed_a_gram_period.md).
For completeness, its data are specified here. Use the fixed bound
\(B=D(s-1)\). At each level introduce the \(B\)-jets of the color values
for \(j_0\le j\le N\). Let \(\mathsf M_Ny=b_N\) be the square banded
system which fixes the first \(d\) jet blocks to the actual jets of
(10), and imposes (7) modulo \(t^{B+1}\) at every subsequent step.
Let \(\mathsf R_N\) select the constant coefficient of every color
block, and put
\[
 \begin{aligned}
 \mathsf H_N&=\mathsf M_N^\dagger\mathsf M_N,&
 v_N&=\mathsf M_N^\dagger b_N,&
 \beta_N&=b_N^\dagger b_N,&
 \nu_N&=\dim\ker\mathsf M_N,\\
 Q_N(\lambda)&=\det(\mathsf H_N+\lambda I),\\
 D_N(\lambda,z)&=
 \det\begin{pmatrix}
 \mathsf H_N+\lambda I+z\mathsf R_N^\dagger\mathsf R_N&v_N\\
 v_N^\dagger&\beta_N
 \end{pmatrix}.
 \end{aligned}
\tag{17}
\]
The variables \(\lambda,z\) are ordinary polynomial variables, not
peripheral eigenvalues. All matrices come from (5) and the fixed
small-color jets. Their size is \(O(N)\) and their bandwidth and jet
block size are fixed.

The finite jet valuation argument gives
\(\ker\mathsf M_N\subset\ker\mathsf R_N\) and \(\nu_N\le B\).
Consequently the exact positive coefficient ratio is
\[
 \mathscr G_N(P,j_0)=
 \frac{[\lambda^{\nu_N}z]D_N(\lambda,z)}
      {[\lambda^{\nu_N}]Q_N(\lambda)}
 =\sum_{j=j_0}^{N}|C_j(q_N)|^2.
\tag{18}
\]
The denominator is positive. To see the identity, restrict to the
orthogonal complement of \(\ker\mathsf M_N\), where
\(\mathsf H_N\) is positive definite. The derivative at \(z=0\) of
the bordered Schur complement is the squared norm of the unique
constant-color output. Both determinants acquire precisely the
common factor \(\lambda^{\nu_N}\).
Cauchy–Binet expresses their coefficients as nonnegative sums of
squared minors, with the actual source border retained.

The [positive ordinary-color bound](regularized_kashaev_period.md)
implies, for any fixed braid presentation with \(b\) strands,
\[
 \mathscr G_N(P,j_0)=|K_N(K)|^2+O_K(N^{2b-1}).
\tag{19}
\]
The ordinary colors \(j<N\) have polynomial size; no such bound is
asserted for the complete color. Equations (14) and (19) therefore give
the positive operator-period volume identity
\[
 \boxed{\qquad
 \lim_{N\to\infty}\frac{\pi}{N}\log\mathscr G_N(P,j_0)=V.
 \qquad}
\tag{20}
\]
Two actual operators, with a common sufficiently large fixed starting
color, give exactly the same value in (18). Different fixed starting
colors change it only by finitely many bounded terms.

In the normalization of the
[marked regulator norm](intrinsic_quantum_a_norm_torsor.md),
\(\log\|\mathcal P_{\mathrm{hyp}}\|=2V/\pi\). Thus (14) and (20) also say
\[
 \frac4N\log|\mathscr P_N(P,c_0)|
       -\log\|\mathcal P_{\mathrm{hyp}}\|\longrightarrow0,
 \qquad
 \frac2N\log\mathscr G_N(P,j_0)
       -\log\|\mathcal P_{\mathrm{hyp}}\|\longrightarrow0.
\tag{21}
\]
These are norm equalities for the actual selected periods. They do not
assert an isomorphism of unpointed torsors or of quantum modules.

## 6. What has been settled and what remains

For the covered knots, a genuine literature quantum \(A\)-annihilator,
its finitely pointed complete period, and that period's volume limit
are all available. The construction of the operator precedes the period
evaluation; the bounded initial jets contain no level-dependent
exponential normalization. The scalar equality (11) is exact, so no
new knot invariant is being substituted.

The stronger classical main-meridian question remains separate:
identify the selected geometric factor in the \(q\to1\) characteristic
polynomial, and compare the corresponding pointed quantum module with
the original marked regulator germ. The auxiliary crossing-circle
deformation used in the volume theorem holds the main meridian
complete; it is not by itself a main-meridian ADO WKB theorem.
Nor does a rational root-state solution identify a root-central
spectral curve with the classical \(A\)-polynomial: it always supplies
a central monodromy eigenvalue \(1\), as the pointing note explains.

No assertion is made here about equality of full annihilator ideals
with another knot recurrence ideal, equality of classical symbols,
minimal-order computation, growing syntax, arbitrary short twists, or
all arborescent presentations. None of these is required for
(14), (20), or (21).

## Review record

The author, primary reviewer and independent source reviewer fully
checked the finite cut-state existence proof and the all-level period
proof, including the boundary rank count, lowest-moment elimination,
central factor cancellation before specialization, fixed-color rigidity,
generic initial window, and the \(D(s-1)\) moving-\(q\) jet bound.
The original ADO/quotient-color normalization was checked as well.
The primary and independent source reviewers also reread the entire
pointed Gram-period proof and the positive ordinary-color bound:
truncated-jet valuation uniqueness, bounded nullity, the bordered Schur
coefficient ratio, positivity and the polynomial ordinary-color tail
all passed. The strict-tree source, analytic, geometric and filling
theorem has its separate internal review record at the linked source.

All six sections of this corollary passed independent final analytical,
source and geometric scope reviews. Exact native mathematical rendering,
AST links and control bytes were checked. The proof uses the stated
proved inputs; no numerical experiment or external holonomicity proof
is needed. These are internal analytical and reproduction checks, not
external peer review or a formal verification of the full dependency
chain.
