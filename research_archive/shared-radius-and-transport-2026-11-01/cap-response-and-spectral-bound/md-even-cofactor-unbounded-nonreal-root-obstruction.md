# The shorter even cofactor has unboundedly many nonreal roots

This note concerns the actual even central cofactor at spectral value
\(-2\). It gives an obstruction to a Hermitian pencil with a bounded
negative index, not a counterexample to an even source bound. In
particular, it does not rule out a signed sum of stable polynomials, a
non-Hermitian perturbation of bounded rank, or cancellation after the
original shared face extraction.

## 1. The original polynomial and the proposed bounded-index route

Let \(N=2m\ge6\), \(M=m-1\), and \(\theta=\pi/N\). Keep the original
level and put

\[
a_r=2+2\cos((2r+1)\theta),\qquad s_r=2\sin(r\theta).
\tag{1}
\]

The exact lower cofactor of the original resolvent numerator satisfies

\[
\begin{aligned}
R_0(b;x,y)&=1,\\
R_j(b;x,y)&=b^j\prod_{r<j}a_r
 +s_j^2(x+y)R_{j-1}(b;x,y)
 +s_js_{j-1}a_{j-1}xyR_{j-2}(b;x,y).
\end{aligned}
\tag{2}
\]

An absent negative-index term is zero. The actual central polynomial is

\[
\begin{aligned}
D_b&=R_M(b;x,y),& E_b&=a_M R_{M-1}(b;x,y),\\
P_C&=s_m^2(x+y)D_bD_c
 +s_ms_{m-1}xy(D_bE_c+E_bD_c).
\end{aligned}
\tag{3}
\]

These are the cleared cofactors and the three central path types in
`actual_cross_cofactor_factorization.md`, Sections 1–2. The common raw
source sign has been removed in (3), exactly as in that note. There is
no replacement by the nearest complete node.

**Theorem.** For each fixed integer \(L\), all sufficiently large even
levels have at least \(2L\) nonreal zeros, counted with multiplicity,
in the actual polynomial \(E_b\) specialized at \(x=y=1\).
Consequently \(E_b\) cannot be represented, at all even levels, by a
Hermitian generalized characteristic polynomial whose coefficient of
\(b\) has a uniformly bounded negative index.

The statement remains true for each fixed shorter terminal cofactor
\(R_{M-s}(b;1,1)\), where \(s\ge1\) is fixed before \(N\) tends to
infinity. No claim about the full maximal cofactor \(R_M\) is needed.

## 2. Reverse the polynomial at its actual upper endpoint

Write \(A_j=\prod_{r<j}a_r\). The exact path expansion of (2) is

\[
R_j(b;1,1)=\sum_{i=0}^j b^i A_i K_{i,j},\qquad
K_{i,i}=1,\quad K_{i,i-1}=0,
\tag{4}
\]

where

\[
K_{i,v}=2s_v^2 K_{i,v-1}
       +s_vs_{v-1}a_{v-1}K_{i,v-2}.
\tag{5}
\]

Thus every term is an actual monomer/dimer path, including its unused
diagonal factors. Fix \(s\ge0\), set \(j=M-s\), and define

\[
B_N=\frac{2N^2}{\pi^2},\qquad
F_{N,s}(t)=\frac{t^j}{A_j B_N^j}R_j(B_N/t;1,1)
 =\sum_{r=0}^j c_{N,s,r}t^r,
\tag{6}
\]

with

\[
c_{N,s,r}=
\frac{K_{j-r,j}}{B_N^r\prod_{\ell=j-r}^{j-1}a_\ell}.
\tag{7}
\]

Equation (6) is a polynomial identity; its displayed expression at
\(t=0\) has the removable value one. For fixed \(r\), the relevant
diagonal rows have

\[
k=M-\ell\in\{s+1,\ldots,s+r\},\qquad
a_\ell=4\sin^2((k+\tfrac12)\theta).
\tag{8}
\]

Consequently

\[
B_Na_\ell\longrightarrow8(k+\tfrac12)^2,
\qquad K_{j-r,j}\longrightarrow8^r.
\tag{9}
\]

The second limit follows directly from (5): every monomer weight tends
to eight, while every dimer weight tends to zero. Hence

\[
c_{N,s,r}\longrightarrow
\frac1{(s+\tfrac32)_r^2}.
\tag{10}
\]

Here \((a)_r=a(a+1)\cdots(a+r-1)\), with \((a)_0=1\).

The convergence is locally uniform on the entire complex \(t\)-plane.
Indeed (5) and \(s_v\le2\), \(a_v\le4\) imply
\(K_{i,i+r}\le10^r\): the induction closes because
\(8\cdot10+16\le10^2\). Since every angle in (8) lies in
\([0,\pi/2]\), the elementary chord bound for sine gives

\[
a_\ell\ge\frac{16(k+\tfrac12)^2}{N^2},\qquad
0\le c_{N,s,r}\le
\frac{(5\pi^2/16)^r}{(s+\tfrac32)_r^2}.
\tag{11}
\]

Set \(c_{N,s,r}=0\) for \(r>j\). The majorant in (11) is summable on
every compact disk. Dominated convergence therefore proves

\[
F_{N,s}(t)\longrightarrow
f_{s+3/2}(t):=\sum_{r=0}^{\infty}\frac{t^r}{(s+\tfrac32)_r^2}
\quad\text{locally uniformly in }\mathbb C.
\tag{12}
\]

The limit for the actual shorter cofactor \(E\) is \(f_{5/2}\), since
its terminal row is \(j=M-1\). Its positive scalar \(a_M\) does not
change its zeros.

## 3. The limiting shorter cofactor has no real zeros

Coefficient comparison gives the exact identity

\[
f_{5/2}(t)=\frac9{4t}\bigl(f_{3/2}(t)-1\bigr).
\tag{13}
\]

The removable value at zero is one. For real \(x>0\), expansion of
sine and integration of each term give

\[
f_{3/2}(-x^2/4)
=\frac1x\int_0^1\frac{\sin(xu)}{\sqrt{1-u^2}}\,du.
\tag{14}
\]

To verify the normalization without a special-function formula, use

\[
\int_0^1\frac{u^{2r+1}}{\sqrt{1-u^2}}\,du
=\frac{2^{2r}(r!)^2}{(2r+1)!}.
\tag{15}
\]

The identity follows either by the substitution \(u=\sin v\) and
integration by parts, or by its elementary recurrence beginning at
one. Substitution into the sine series gives exactly the coefficients
\((-x^2/4)^r/(3/2)_r^2\) in (14).

For every \(x>0\), the strict inequality \(\sin(xu)<xu\) holds for
all \(u\in(0,1]\). Since the weight is positive and
\(\int_0^1 u/\sqrt{1-u^2}\,du=1\), equation (14) implies
\(f_{3/2}(-x^2/4)<1\). Equation (13) therefore gives

\[
f_{5/2}(t)>0\quad(t<0).
\tag{16}
\]

For \(t\ge0\) the same conclusion follows from its positive series.
Thus \(f_{5/2}\) has no real zeros.

For completeness, every fixed \(a>5/2\) is a positive average of this
same function. Let \(U,V\) be independent variables in \((0,1)\)
with density proportional to
\(u^{3/2}(1-u)^{a-7/2}\). Their elementary beta integrals give
\(\mathbb E U^r=(5/2)_r/(a)_r\), and hence

\[
f_a(t)=\mathbb E f_{5/2}(tUV)>0\quad(t\in\mathbb R).
\tag{17}
\]

This uses only a finite-parameter integral on a bounded interval;
there is no root-level limiting measure. It proves the assertion for
all shorter terminal rows \(s\ge1\).

## 4. There are infinitely many zeros, all of them nonreal

For \(a\ge1\), \((a)_r\ge r!\), so

\[
|f_a(t)|\le\sum_{r\ge0}\frac{|t|^r}{(r!)^2}
\le\exp(2\sqrt{|t|}).
\tag{18}
\]

For the last inequality retain only the even powers in the exponential
and use \(\binom{2r}{r}\le4^r\). The function is not a polynomial:
every Taylor coefficient in (12) is nonzero.

Here is the needed elementary entire-function argument. If \(f_a\)
had only finitely many zeros, divide out their polynomial \(Q\), with
multiplicities. The quotient \(g=f_a/Q\) is entire and nowhere zero,
so it has an entire logarithm \(h\), obtained by integrating \(g'/g\)
on the simply connected plane. On sufficiently large circles,
\(\Re h=\log|g|\le C+2\sqrt R\). The same bound, with a different
constant, holds on circles about any fixed center. If an analytic
function \(h\) on a disk of radius \(R\) obeys \(\Re h\le M_R\),
the first Fourier coefficient of \(\Re h\), or the Poisson formula,
gives

\[
|h'(z_0)|\le\frac{2(M_R-\Re h(z_0))}{R}.
\tag{19}
\]

Applying (19) with \(M_R=O(\sqrt R)\) and letting \(R\to\infty\)
forces \(h'\equiv0\). Thus \(f_a\) would be a constant times \(Q\),
contradicting its nonpolynomial series. Therefore it has infinitely
many zeros. By (16)–(17), all zeros for \(a\ge5/2\) are nonreal.

Choose finitely many disjoint disks around as many nonreal zeros as
desired, with no zero on their boundaries and with all disks disjoint
from the real axis and zero. Local uniform convergence in (12) and
Rouché's theorem give the same number of zeros, counted with
multiplicity, of \(F_{N,s}\) in these disks for every sufficiently
large even \(N\). The inverse change \(b=B_N/t\) preserves nonreality
and multiplicity. This proves the theorem.

## 5. The precise matrix obstruction

Suppose, after specialization \(x=y=1\), a proposed construction writes
the cofactor as a nonzero scalar times

\[
\det(bJ_N-H_N),\qquad J_N=J_N^*,\quad H_N=H_N^*,\quad\det J_N\ne0,
\tag{20}
\]

with the negative index of \(J_N\) bounded by a constant \(k\).
Then \(A_N=J_N^{-1}H_N\) is self-adjoint for the nondegenerate Hermitian
form \([v,w]=v^*J_Nw\). The sum of its generalized eigenspaces for
eigenvalues in the open upper half-plane is totally isotropic.
For eigenvectors this follows from
\((\overline\lambda-\mu)[v,w]=0\); for generalized vectors the same
statement follows by induction on their chain lengths. A totally
isotropic subspace has dimension at most the negative index: its
projection to the negative summand of the diagonalized form is
injective. Hence there are at most \(k\) upper-half-plane eigenvalues
with algebraic multiplicity. Hermitian generalized characteristic
polynomials have conjugate-paired roots, so the total number of
nonreal zeros is at most \(2k\). This contradicts Section 4.

Thus the exact shorter cofactor cannot admit this bounded-index
representation. In particular, a proposed Hermitian model obtained
by a uniformly bounded-rank change of the positive coefficient of
\(b\) cannot work. This is stronger than the previously known single
level failure of real stability, but narrower than a general
impossibility statement about bounded-rank perturbations.

The conclusion does **not** exclude any of the following:

* A signed sum of a bounded number of stable determinants or minors.
  A sum can have many nonreal roots even when each summand is stable.
* A bounded-rank perturbation that is not self-adjoint in a Hermitian
  form of bounded negative index. Even rank one can then move many
  eigenvalues off the real axis.
* A bound for the full polynomial (3) after the original face targets
  have been extracted. The obstruction is local and uses a
  specialization, not an actual shared boundary assignment.
* A common-axis exponential estimate that holds without real
  stability. Nonreal roots alone do not disprove such an estimate.

The existing coefficientwise comparison with a stable nearest-node
polynomial also remains valid. It still does not control signed
negative-axis values. The parity bridge therefore remains open, with
the bounded-negative-index shortcut now excluded by an exact
large-level argument.

The scaling is important for the quantitative interpretation. Each
fixed nonreal zero \(t_0\) detected in (12) gives a root
\(b_N=B_N/(t_0+o(1))\) of size proportional to \(N^2\). In the
Bernoulli coordinate \(p_N=(1-b_N)^{-1}\), used for a polynomial
normalized at \(b=1\), this root has \(p_N=O(N^{-2})\). Thus any
fixed finite collection of these pairs has a vanishing contribution
to normalized positive logarithmic derivatives and to normalized
logarithmic moduli on compact boundary fugacity sets. The proof does
not show that a positive fraction of all roots is nonreal, nor that
their combined spectral cost is exponential. An \(o(N)\)-defect
model or a subexponential correction remains possible.

## 6. Dependency record and finite scope

All source identities used above are the actual polynomial identities
in the following publication-checkout files. Their SHA256 hashes at
the time of this derivation are:

| File | SHA256 |
| --- | --- |
| `notes/actual_cross_cofactor_factorization.md` | `d0e8012d4627495c9fbdfb7ea0cfb1063d3fbfc24dc960ceec0bcdc0111b1727` |
| `notes/actual_fejer_half_block_entropy.md` | `3f92c7fc9af003822aba97b5394dcbe4a81ce6a1db177049c29817d891699a7d` |
| `notes/research_even_cross_stability_obstruction.md` | `ee4399a5e1c7ad915a7b18fb90983525aa4cf11924c6d4c92f8a3be3e119ad8c` |
| `notes/actual_cross_cofactor_interior_packet.md` | `0c02df98f40a0c0a36401430faa1812761018a42ab437515a314bd407c03ed75` |

No sampled root computation enters the proof. The statement is about
every sufficiently large even level for each requested finite number
of nonreal roots. It supplies neither a quantitative count proportional
to \(N\) nor a numerical threshold in \(N\), and neither is required
to rule out a uniform negative-index bound.
