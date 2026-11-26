# A uniformly bounded Newton lift through one Conway product

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The turned Casimir has an exact binary intertwining lift through the
actual Conway product. The lift is a sum of strict coordinate shifts
and explicit joint diagonal operators on the full Newton tensor space.
Its norm is at most 14 at every level. No inverse multiplication
operator, spectral quotient, or unknown closed period is used.

This is a binary intertwiner, not a claimed coassociative Hopf
coproduct. Its degree-clock and strict-shift factors are not yet
shown to have bounded transport through further subtrees. That
closure problem, and a geometric lower bound for the original source,
remain separate.

## 1. Full physical operations

Fix \(N\ge2\), and write
\[
 d=N-1,\qquad \theta=\pi/N,\qquad
 q=e^{i\theta},\qquad Q=q^2,
\]
\[
 s_r=2\sin(r\theta),\quad p_r=s_r^2,\quad
 S_r=\prod_{h=1}^r s_h,\quad S_0=1,\qquad
 c_r=2\cos((2r+1)\theta).
 \tag{1}
\]
The quantities \(s_r,p_r,c_r\) in formulas below are defined for
every integer \(r\). Factorials \(S_r\) are used only at indices
between 0 and \(d\).

Use the actual Newton basis \(e_0,\ldots,e_d\) of
\[
 H_N=\mathbb C[z]/(2T_N(z/2)+2),
 \tag{2}
\]
with its coefficient Hermitian norm. The Chebyshev polynomial is
normalized by \(T_N(\cos t)=\cos Nt\). This is the full
repeated-root algebra, including its physical first normals.
The product \(M:H_N\otimes H_N\to H_N\) is
\[
 M(e_i\otimes e_j)=\sum_r\mu_{ijr}e_r.
 \tag{3}
\]
If \(i+j\le d\), its coefficients are
\[
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}},
 \qquad \max(i,j)\le r\le i+j;
 \tag{4}
\]
they are zero elsewhere. If \(i+j\ge N\), the product is zero
in the entire algebra (2), not merely at its distinct roots.

Multiplication by \(z\), the actual turn, and the turned Casimir are
\[
 Ze_i=c_ie_i-p_{i+1}e_{i+1},\qquad
 Je_i=e_{d-i},\qquad
 Le_i:=(JZJ)e_i=c_ie_i-p_ie_{i-1}.
 \tag{5}
\]
The missing end vectors are zero. In particular \(\|Z\|,\|L\|\le6\).
All these are the original root operations. The original Frobenius
and marked cap rows remain unchanged.

## 2. The explicit bounded binary operator

For \(i,j\in\{0,\ldots,d\}\), put \(m=i+j\). When \(i>0\), define
the following asymmetric lift on that input:
\[
 \begin{split}
 \Delta_iL(e_i\otimes e_j)
 ={}&c_m e_i\otimes e_j\\
 &-p_m\left(1+\frac{p_j}{p_i}\right)e_{i-1}\otimes e_j\\
 &-s_ms_{m-1}\frac{p_j}{p_i}
                         e_{i-1}\otimes e_{j-1}.
 \end{split}
 \tag{6}
\]
A term with the end vector \(e_{-1}\) is zero. Let
\(\Delta_jL\) be the formula with the inputs exchanged and its
tensor outputs exchanged back.

The final symmetric lift has no ratios:
\[
 \boxed{\begin{split}
 \Delta_NL(e_i\otimes e_j)
 ={}&c_{i+j}e_i\otimes e_j\\
 &-p_{i+j}(e_{i-1}\otimes e_j+e_i\otimes e_{j-1})\\
 &-s_{i+j}s_{i+j-1}e_{i-1}\otimes e_{j-1}.
 \end{split}}
 \tag{7}
\]
Negative end vectors are zero. Every coefficient is explicit from
\(N,i,j\), and no comparison mask is used.

**Theorem 1.** On the full physical algebra, for every \(N\ge2\),
\[
 \boxed{\qquad M\Delta_NL=LM,\qquad
                         \|\Delta_NL\|\le14.\qquad}
 \tag{8}
\]
The norm is the ordinary operator norm on the full Newton tensor
Hilbert space. It is independent of the level and includes every
parity and composite level.

We first prove the auxiliary directional identity (6). Averaging
its two exact versions will give (7) without a denominator.

## 3. The elementary trigonometric identity

In this section \(s_x=2\sin(x\theta)\) also for real \(x\).
For \(m=i+j\) and \(s_i\ne0\), one has
\[
 \begin{split}
 s_{v+m}s_{v-i}s_{v-j}-s_v^3
 ={}&-\frac{s_m(p_i+p_j)}{s_i}s_{v-j}
       -\frac{s_j^3}{s_i}s_{m-v}.
 \end{split}
 \tag{9}
\]
Here \(p_i=s_i^2\), as before.

For a complete elementary verification, the product-to-sum formula
gives
\[
 s_{v+m}s_{v-i}s_{v-j}-s_v^3
       =s_{v+2i}+s_{v+2j}+s_{v-2m}-3s_v.
 \tag{10}
\]
Both sides of (9) are therefore linear combinations of
\(\sin(v\theta)\) and \(\cos(v\theta)\).
At \(v=j\) the left side is \(-s_j^3\), as is the right side.
At \(v=i\), use
\[
                       p_i-p_j=s_ms_{i-j}
 \tag{11}
\]
to evaluate the right side as
\[
 -\frac{(p_i+p_j)(p_i-p_j)+p_j^2}{s_i}=-s_i^3.
\]
For generic \(i,j\) these two evaluations determine both linear
coefficients, proving (9). Continuity proves the same identity
at coincident evaluation points, in particular at \(i=j\).
The final formula has no denominator \(s_{i-j}\).
Equations (10) and (11) themselves follow directly from the
ordinary sine addition formulas.

## 4. All coefficients and all physical support endpoints

Suppose first that \(i,j>0\) and \(m=i+j\le d\). Abbreviate
\[
 u=-p_m(1+p_j/p_i),\qquad
 v_*=-s_ms_{m-1}p_j/p_i.
 \tag{12}
\]
The coefficient of \(e_r\) in the desired intertwining identity is
\[
 c_r\mu_{ijr}-p_{r+1}\mu_{ij,r+1}
   =c_m\mu_{ijr}
         +u\mu_{i-1,j,r}+v_*\mu_{i-1,j-1,r}.
 \tag{13}
\]
For \(\max(i,j)\le r<m\), division of the positive factorials
in (4) gives
\[
 \begin{split}
 \frac{\mu_{ij,r+1}}{\mu_{ijr}}
   &=\frac{s_{r+1}s_{m-r}}
          {s_{r+1-i}s_{r+1-j}},\\
 \frac{\mu_{i-1,j,r}}{\mu_{ijr}}
   &=\frac{s_i s_{m-r}}{s_m s_{r+1-i}},\\
 \frac{\mu_{i-1,j-1,r}}{\mu_{ijr}}
   &=\frac{s_i s_j s_{m-r}s_{m-r-1}}
     {s_m s_{m-1}s_{r+1-i}s_{r+1-j}}.
 \end{split}
 \tag{14}
\]
The last expression is zero at \(r=m-1\), as required by its
product support. All denominators in these interior expressions
are nonzero. Also
\[
                     c_r-c_m=s_{r+m+1}s_{m-r}.
 \tag{15}
\]
Substitute (14)--(15) into (13), multiply by
\(s_{r+1-i}s_{r+1-j}/s_{m-r}\), and put \(v=r+1\).
The resulting identity is exactly (9). This proves every
interior coefficient.

At \(r=m\), both lowered products in (13) vanish, and the equality
is its diagonal term \(c_m\mu_{ijm}\).
The only other possible output is \(r=\max(i,j)-1\).
Its left side is \(-p_{\max(i,j)}\mu_{ij,\max(i,j)}\).
For \(i>j\), the two necessary ratios to \(\mu_{ij,i}\) are
\[
 \frac{\mu_{i-1,j,i-1}}{\mu_{ij,i}}=\frac{s_{i-j}}{s_m},
 \qquad
 \frac{\mu_{i-1,j-1,i-1}}{\mu_{ij,i}}
                         =\frac{p_j}{s_ms_{m-1}}.
 \tag{16}
\]
Equations (11)--(12) make their weighted sum \(-p_i\).
For \(i=j\), the single-lowered product has no such output;
the double-lowered ratio is \(p_i/(s_ms_{m-1})\), giving
\(-p_i\). For \(i<j\), that single-lowered product again has
no such output, and the double-lowered ratio to \(\mu_{ij,j}\)
is \(p_i/(s_ms_{m-1})\), giving \(-p_j\).
All still lower outputs vanish on both sides. This completes
the support proof when \(m\le d\).

If \(j=0\) and \(i>0\), (6) reduces to
\[
 c_i e_i\otimes e_0-p_i e_{i-1}\otimes e_0,
\]
which is the unit case of (5). The case \(i=0\) is supplied
by the exchanged formula; (7) handles both zero.

It remains to check the full repeated-root zero support:

* If \(m=N\), both lowering coefficients in (6) are zero
  because \(s_N=p_N=0\), and the diagonal product is zero.
* If \(m=N+1\), the single-lowered product still has total
  degree \(N\), while the double-lowering coefficient contains
  \(s_{m-1}=s_N=0\).
* If \(m\ge N+2\), even the double-lowered product has total
  degree at least \(N\), so every product in (13) is zero.

These statements use the full-algebra divisibility in (4), including
its multiplicities. They do not divide a vanishing coefficient.
They also cover \(N=2\).
Thus (6), and by input exchange its companion, intertwine at every
input where they are defined.

For \(i,j>0\), average these two directional output columns with
weights \(p_i/(p_i+p_j)\) and \(p_j/(p_i+p_j)\). Both have the
same product \(LM(e_i\otimes e_j)\), so their weighted average
does too. The first single-lowering coefficient becomes
\(-p_m\), as does the second, and the double-lowering coefficient is
\[
 -s_ms_{m-1}
 \left(\frac{p_i}{p_i+p_j}\frac{p_j}{p_i}
       +\frac{p_j}{p_i+p_j}\frac{p_i}{p_j}\right)
                         =-s_ms_{m-1}.
\]
This proves exactly (7). If one index is zero, (7) directly gives
the unit case of (5); if both are zero it gives \(c_0e_0\otimes e_0\).
The first claim in (8) follows.

## 5. The uniform Newton bound

Let \(E e_i=e_{i-1}\) for \(i>0\), and \(Ee_0=0\), and let
\(Ke_i=Q^ie_i\). Thus \(\|E\|\le1\) and \(K\) is unitary.
Put \(V=K\otimes K\), and define
\[
 \begin{split}
 D_0&=qV+q^{-1}V^{-1},\\
 D_1&=2I-V-V^{-1},\\
 D_2&=c_0I-q^{-1}V-qV^{-1}.
 \end{split}
 \tag{17}
\]
Their respective entries are \(c_{i+j}\), \(p_{i+j}\), and
\(s_{i+j}s_{i+j-1}\), by the product-to-sum identity for sine.
The exact operator is therefore
\[
 \Delta_NL=D_0-(E\otimes I+I\otimes E)D_1
                              -(E\otimes E)D_2.
 \tag{18}
\]
All diagonals act before the displayed strict lowering shifts.
Since \(|c_r|\le2\) and \(|s_r|\le2\),
\[
             \|D_0\|\le2,\qquad \|D_1\|,\|D_2\|\le4.
 \tag{19}
\]
The triangle inequality proves \(2+2\cdot4+4=14\).
This is an actual bounded tensor operator; no cancellation of
singular angular factors is needed to define it.

## 6. Completed currents, exact source transport, and the remaining limit

Subtracting the scalar part gives
\[
 M(\Delta_NL-c_0I)=(L-c_0I)M,\qquad
                   \|\Delta_NL-c_0I\|\le16.
 \tag{20}
\]
For the unturned Casimir the elementary lift is
\[
                  \Delta_NZ=Z\otimes I,\qquad
 M\Delta_NZ=ZM,\qquad \|\Delta_NZ\|\le6.
 \tag{21}
\]
Thus either completed Casimir current can be pushed through one
actual product with a uniform Newton bound.
Any original exterior row or adjoining tensor may be applied to
these operator identities. The exact original source, its phases
and every physical first normal are preserved.

More generally, for any specified noncommutative polynomial \(P\),
keep its written operator order and substitute the two lifts:
\[
 M P(\Delta_NZ,\Delta_NL)=P(Z,L)M.
 \tag{22}
\]
Induction on a word proves (22). Its norm is bounded by the sum
of the absolute polynomial coefficients times \(6^{n_Z}14^{n_L}\)
for the corresponding words. Different polynomial expressions for
the same one-packet operator may give different lifts in \(\ker M\).

No uniqueness, coassociativity, or Hopf-module structure is asserted.
In particular the explicit factors \(E,K,K^{-1}\) in (17)--(18)
are not supplied with bounded intertwining lifts through another
product, or with bounded conjugation formulas through every child
crossing. They are not shown here to be fixed-degree polynomials
in separate child Casimirs. Thus pushing the binary lift farther
can leave the proved transport alphabet. Equation (22) does not
solve that closure problem.
The present result is a uniform binary lift, not yet a bounded
transport theorem for every arborescent component or a geometric
lower bound for its prescribed closing.

## Complete proof sources

Both complete matching texts were read. They supply the actual
operations and full multiplication formula; the coefficient identity,
all endpoint cases, explicit lift and norm estimate are proved above.

| Complete proof source | SHA-256 |
|---|---|
| [Original centered compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Full positive Newton multiplication](actual_positive_newton_multiplication.md) | 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb |

Only written mathematics and text/hash operations were used.
No mathematical program, numerical experiment, test, build, git
operation, or earlier-final edit was performed.
