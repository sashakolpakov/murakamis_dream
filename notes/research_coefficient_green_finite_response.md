# An exact finite coefficient response for the original regular period

Private written proof, 17 November 2026.

The actual affine meridian equation can be compressed to a system of
bounded size by eliminating only its nonzero coefficient pivots.
Every zero-pivot compatibility equation and every upper-support equation
remains. The resulting affine closing is the original complete value,
without division by that value. A terminal dual row exists precisely
when the retained scalar is unique on this system.

For rational operator coefficients, the torsion classification also
locates the pivots on finitely many affine functions of the level,
on eventual congruence classes. Neither statement estimates the long
transfer products or proves that the selected numerator is nonzero.

## 1. Actual source and one fixed operator

Fix a zero-framed knot and its marked squared meridian \(Y\). Put
\[
q_N=e^{\pi i/N},\quad Q_N=q_N^2,\quad
(T_Nf)(Y)=f(Q_NY),\quad S_N(Y)=\frac{Y^N-1}{Y-1}.
\]
The original regularization in [R] is
\[
F_N=S_NR_N+P_N,\qquad
K_N=F_N(1)=P_N(1)+NR_N(1).                         \tag{1}
\]
Here \(P_N\) is the ordinary-color interpolant of degree at most
\(N-2\), and \(R_N\) is Laurent polynomial. By the actual support
bound recorded in [D], enlarge a fixed integer \(A\ge1\) so that
\(\operatorname{supp}R_N\subset[-AN,AN]\) for all sufficiently large
levels. No bound on its unknown coefficients is assumed.

Choose one fixed rational-coefficient actual annihilator of
\((Y-1)F_N\), as supplied in [T]. Clear its fixed denominators.
After multiplication on the left by a Laurent monomial in \(Y\),
write it as
\[
\mathcal L(q,Y,T)=\sum_{j=0}^{w}Y^j p_j(q,T),\qquad
p_j\in\mathbb Q[q^{\pm1},T^{\pm1}],\qquad p_0p_w\ne0.
                                                               \tag{2}
\]
The case \(w=0\) is allowed. The normal gauge \(Y-1\) is retained.
At a root, \(Y^N\) is shift invariant, so (1) gives exactly
\[
\mathcal L_N R_N=\beta_N,\qquad
\beta_N=-\mathcal L_N(P_N/S_N).                    \tag{3}
\]
The right side is Laurent polynomial because the left side is.
Each shifted \(P_N/S_N\) is regular at zero and \(O(Y^{-1})\)
at infinity. Consequently
\[
\operatorname{supp}\beta_N\subset[0,w-1].          \tag{4}
\]
For \(w=0\) this means \(\beta_N=0\). The ordinary-color coefficient
bound of [R, Section 4] also gives polynomial bounds for (4), but
none are needed for the exact compression.

All statements concern levels beyond the finite exceptional set
for the supplied operator and its nonzero initial specialization.
Choose them also large enough that \(AN\ge w\). Set
\[
\ell=-AN,\quad u=AN,\quad
a_j(k)=p_j(q_N,Q_N^{\,k-j}),\quad
d_k=a_0(k),\quad \beta_k=[Y^k]\beta_N .
\]
For a candidate \(R=\sum_{\ell\le k\le u}c_kY^k\), extend \(c_k=0\)
outside that interval. The entire equation (3) is then
\[
\sum_{j=0}^{w}a_j(k)c_{k-j}=\beta_k,
                   \qquad \ell\le k\le u+w.       \tag{5}
\]
All other rows are zero by support. The shift eigenvalue \(Q_N^{k-j}\)
in (5) is essential.

## 2. Explicit elimination with all compatibility rows

Let
\[
\mathcal Z_N=\{k\in[\ell,u]\cap\mathbb Z:d_k=0\}
             =\{k_1<\cdots<k_{\kappa_N}\}.
\]
Introduce independent complex coordinates
\(\xi=(\xi_1,\ldots,\xi_{\kappa_N})^{\mathsf t}\).
Define affine functions \(c_k(\xi)=v_k+H_k\xi\) in increasing \(k\).
Below \(\ell\) they are zero. At a zero pivot set
\[
c_{k_\rho}(\xi)=\xi_\rho.                         \tag{6}
\]
At every other \(k\in[\ell,u]\), set
\[
c_k(\xi)=
\frac{\beta_k-\sum_{j=1}^{w}a_j(k)c_{k-j}(\xi)}{d_k}.
                                                               \tag{7}
\]
After this construction set \(v_k=H_k=0\) for \(k>u\).
Thus no absent upper coefficient is solved for or introduced.
The rows \(H_k\) depend only on the operator and support;
the scalars \(v_k\) depend linearly on the supplied forcing.

Retain the row set
\[
\mathcal R_N=\mathcal Z_N\ \sqcup\
                         \{u+1,\ldots,u+w\}.       \tag{8}
\]
For \(k\in\mathcal R_N\), define
\[
C_{k,:}=\sum_{j=0}^{w}a_j(k)H_{k-j},\qquad
b_k^{\mathrm{eff}}=\beta_k-\sum_{j=0}^{w}a_j(k)v_{k-j}.
                                                               \tag{9}
\]
Use the increasing order within the two displayed row groups.
This gives a \((\kappa_N+w)\)-by-\(\kappa_N\) matrix \(C_N\) and
an effective right side \(b_N^{\mathrm{eff}}\).

**Theorem 1.** The map
\[
\xi\longmapsto R_\xi(Y)=
                 \sum_{k=\ell}^{u}(v_k+H_k\xi)Y^k              \tag{10}
\]
is a bijection from the solutions of
\[
                         C_N\xi=b_N^{\mathrm{eff}}             \tag{11}
\]
to all Laurent solutions of (3) supported in \([\ell,u]\).
In particular (11) is consistent for the actual knot source.

**Proof.** Equations (7) impose all nonzero-pivot rows of (5).
Equations (9)--(11) impose the remaining rows: the zero-pivot
compatibilities and every upper-tail row. Below \(\ell\) and above
\(u+w\), both sides vanish. Thus every solution of (11) gives a
solution of the entire Laurent equation.

Conversely, for any Laurent solution, take
\(\xi_\rho=c_{k_\rho}\). Induction in \(k\) proves (6)--(7);
the omitted rows of that induction are exactly (8), so (11) holds.
The coordinates are recovered from (6), proving injectivity.
The actual \(R_N\) supplies consistency. \(\square\)

Let \(D=\operatorname{span}_T p_0\). For all sufficiently large
\(N\), \(p_0(q_N,Z)\) is nonzero. After removing a Laurent monomial
it has degree at most \(D\), hence at most \(D\) nonzero roots.
Each root that lies on the \(Q_N\)-orbit accounts for one residue
class of pivots modulo \(N\). Such a class meets \([-AN,AN]\)
at most \(2A+1\) times. Therefore
\[
                  \kappa_N\le(2A+1)D.             \tag{12}
\]
This is [D]'s dimension argument with its full response equations
retained. Empty pivot and empty row sets have their usual meaning;
Theorem 1 also applies when \(\kappa_N=0\) or \(w=0\).

## 3. The original affine closing and its exact dual

Define the known affine data
\[
\gamma_N=P_N(1)+N\sum_{k=\ell}^{u}v_k,\qquad
\lambda_N=N\sum_{k=\ell}^{u}H_k.                  \tag{13}
\]
For the actual pivot coordinates \(\xi_N\), (1) is exactly
\[
                         K_N=\gamma_N+\lambda_N\xi_N.          \tag{14}
\]
No complete value was used to construct (6)--(13).

**Theorem 2.** The following are equivalent:
the scalar (14) is the same for every solution of (11);
\(\lambda_N\ker C_N=0\); and the complex linear dual equation
\[
                              g_N C_N=\lambda_N               \tag{15}
\]
has a solution row \(g_N\). When these conditions hold,
\[
                         K_N=\gamma_N+g_Nb_N^{\mathrm{eff}}.   \tag{16}
\]
The value is independent of the dual solution.

Indeed the consistent solution set of (11) is a translate of its
kernel. Its annihilator is the row space of \(C_N\), proving all
equivalences. Equation (16) follows by substitution. A change of
dual row annihilating \(C_N\) also annihilates
\(b_N^{\mathrm{eff}}=C_N\xi_N\). These are complex linear pairings;
there is no positivity assertion.

The uniqueness condition is not presumed for an arbitrary chosen
root operator. One actual sufficient certificate is that its rational
kernel over \(\mathbb C(Y^N)\) is the line generated by \(F_N/S_N\).
Then the difference of two Laurent solutions is \(h(Y^N)F_N/S_N\).
The ordinary anchor \(F_N(Q_N)=1\) makes \(F_N/S_N\) have a simple
pole there. Regularity of the difference forces \(h\) to vanish at
\(Y^N=1\), so the difference vanishes at \(Y=1\). This proves the
condition of Theorem 2. This is precisely [R]'s two-lattice argument;
[T]'s single occupied torsion-curve test is one sufficient rank
certificate. Neither certificate is asserted for every knot operator.

## 4. Eventual affine pivot locations

Apply [T]'s proved torsion classification to the fixed rational
Laurent polynomial \(p_0(q,Z)\). Outside an effective finite range,
its zeros on \((q_N,Q_N^k)\) are exactly the grid points on a finite
list of contained nonvertical irreducible curves
\[
                    q^aZ^b=e^{2\pi i h/t},\qquad b\ne0.         \tag{17}
\]
The integers \(a,b\) are relatively prime. Invert the equation
if necessary so \(b>0\). At the specified half-root, (17) says
\[
a+2bk=2N(h/t+n),\quad n\in\mathbb Z,\qquad
k=\frac{h/t+n}{b}N-\frac{a}{2b}.                 \tag{18}
\]
The interval \([-AN,AN]\) leaves only finitely many possible \(n\),
uniformly for \(N\ge2\). For example \(|n|\le Ab+|a|+2\) suffices
when \(0\le h<t\). For each remaining affine expression, integrality
of \(k\) is periodic in \(N\), with period dividing \(2bt\).
Its membership in the closed support interval is eventually fixed:
compare its slope with \(\pm A\), and use its constant term at equality.

Take a common period over the finite list. On each congruence class,
the occupied affine expressions, their number, and their increasing
order are fixed for all sufficiently large \(N\). Two distinct
affine expressions cross at most once unless identical; identical
expressions are counted once. All intersections and initial
specialization exceptions may be included in the finite threshold.
Thus (8)--(11) have fixed dimensions and ordered row labels on each
eventual congruence class, with pivot locations explicitly affine
in \(N\). No primality or parity class is discarded.

For \(k=\alpha N+\beta\), the individual endpoint coefficient is
\[
p_j(q_N,Q_N^{k-j})
 =p_j(e^{\pi i/N},e^{2\pi i\alpha}e^{2\pi i(\beta-j)/N}).
                                                               \tag{19}
\]
It is a holomorphic germ in \(1/N\) near zero. This does not say
that the effective matrix (9) is one such germ: (7) retains
ordered propagation across intervals with \(O(N)\) indices.
Mann's classification controls exact pivots, not those products,
their small nonzero factors, or the selected dual numerator.

## 5. Coverage, scope, and proof sources

[D, Section 5] already proves the bounded homogeneous coefficient
dimension. [T] already classifies the torsion curves and their
periodic grid counts. The added construction is the explicit
unnormalized affine response (6)--(11), its retained closing and
dual (13)--(16), and the ordered affine pivot locations (18).

The entire coverage text
[Finite matrix criterion](actual_main_meridian_finite_matrix_criterion.md)
was also read. Its bounded matrix uses a supplied whole preoperator's
first quantum-normal equation, central kernel minors, and normalization
by an already nonzero complete value. The present construction
uses the root affine coefficient equation directly, preserves its
entire solution set, and makes no such normalization or conditioning
assumption. That coverage text is not a proof premise here.

The actual forcing remains the complete combination (3), including
all ordinary polar data. Although its original coefficients are
polynomially bounded, its effective forcing need not be. No common
rational dependence of that forcing on \(q\), uniformly tame
reconstruction, geometric branch identification, nonzero numerator,
or scalar lower bound follows. Additional pointing must be retained
if the condition of Theorem 2 has not been proved.

All three complete proof directs were read and their used implications
checked at the following pins:

| Label | Complete source | SHA256 |
|---|---|---|
| R | notes/regularized_kashaev_period.md | d7efc1e6e2995a0bff7553553e044f8554e559e51cdf8515d8048e2f603b94fc |
| D | notes/research_actual_operator_end_loss_and_coefficient_space.md | d4b516e508e461f8cf9d617476622bd4c1c2e59cf6d26e7655a845064ae0d4ea |
| T | notes/torsion_initial_rank.md | 1353531ca73f67ef29724252d49733c64f00d226a0c51426bb9ab85b42a660e5 |

Only written mathematics, source-text reads, and metadata hashes
were used. No mathematical programs, tests, numerical cases, or
builds were run. Frozen notes and public manuscripts are unchanged.
