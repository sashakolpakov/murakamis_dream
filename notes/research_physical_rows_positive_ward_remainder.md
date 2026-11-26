# Positive Ward remainders for all original physical rows

Private written proof, 17 November 2026.

Every original physical value row has a specified Ward representative
with an exact positive Cauchy remainder. After normalization this
remainder has polynomial upper and lower bounds on compact slit sets,
uniformly in the physical row and the level. A free-color identity
also retains the original normal rows by differentiation. The known
polynomial divisor explains the growing negative index of the
unstripped turned-unit ratio. No further composition closure follows.

## 1. Original source and its free-color row

Put \(N\ge2\), \(D=N-1\), \(m=\lfloor N/2\rfloor\),
\(\theta=\pi/N\), \(\eta=(-1)^D\), and
\[
 c_j=2\cos((2j+1)\theta),\quad P_N(C)=2T_N(C/2)+2,
 \quad\Omega=\mathbb C\setminus[2,\infty).
 \tag{1}
\]
The double nodes have \(0\le j<m\); at odd \(N\) the additional
simple node is \(c_*=-2\). Define the original Newton data
\[
 S_r=\prod_{b=1}^r2\sin(b\theta),\quad
 e_r(C)=S_r^{-2}\prod_{a<r}(c_a-C),\quad
 K_N(w,C)=\sum_{r=0}^D e_r(w)e_r(C),\quad F_j(C)=K_N(c_j,C),
\]
\[
 h_j=\frac1{4\sin\theta\sin((2j+1)\theta)}\quad(0\le j<m).
 \tag{2}
\]
The pinned complete sources prove the genuine unscaled turn
\(Te_r=e_{D-r}\), including all repeated-root normals, and
\(S_rS_{D-r}=N\). For \(A_c=K_N(c,\cdot)\), they therefore give
the polynomial identity
\[
 H_c:=\operatorname{can}(TA_c)
   =\frac{\eta}{N^2}\frac{P_N(C)-P_N(c)}{C-c}.
 \tag{3}
\]
Here is the finite verification for every complex \(c\).
In \(\sum_r e_r(c)e_{D-r}(C)\), use \(c_{D-a}=c_a\) to write
its \(r\)-th product as
\(\eta N^{-2}\prod_{a<r}(c-c_a)\prod_{a>r}(C-c_a)\).
Summing these products telescopes to (3). Thus no nonphysical
evaluation is being substituted into a quotient algebra.

Keep exactly the pinned Ward representative of an actual input \(A\):
\[
 \widehat H_A=
 \eta\sum_{j<m}\{(4-c_j^2)A(c_j)\widehat G_j+
       ((4-c_j^2)A'(c_j)-c_jA(c_j))F_j\}
       +\mathbf1_{\mathrm{odd}}A(-2)F_*
       =Y_A+\widetilde Q_N L_A,
\]
\[
 L_A=\eta\sum_{j<m}A(c_j)F_j/h_j,\qquad F_*=K_N(-2,\cdot).
 \tag{4}
\]
The prescribed \(\widehat G_j\) and \(\widetilde Q_N\) are
holomorphic on \(\Omega\), real below \(2\), and retain every
original double-node value and first normal, together with the odd
simple value. No normal is prescribed at that simple node. The
polynomial \(Y_A\) is real for real input data. Formula (4) is not
an off-grid equality with the canonical polynomial \(H_A\).

For \(x>2\), the same complete source gives
\[
 \rho_N(x)=\frac{N}{4\pi\sin\theta}
   \tanh\!\left(\frac N2\operatorname{arcosh}(x/2)\right),
 \qquad d\mu(x)=\frac{N^2\rho_N(x)}{P_N(x)}\,dx,
\]
\[
 \int F_jF_k\,d\mu=h_j\delta_{jk},\qquad
 \frac{\widehat H_A-H_A}{P_N}(C)
       =\frac1{N^2}\int\frac{L_A(x)}{x-C}\,d\mu(x).
 \tag{5}
\]
The double rows have degree \(j\), satisfy \(F_j(c_0)=1\), and have
all their roots in \((2,\infty)\). In particular they are positive
below \(2\). The density of \(\mu\) is \(O_N(\sqrt{x-2})\) at \(2\)
and asymptotic to a positive constant times \(x^{-N}\) at infinity.
Its moments through degree \(N-2\) are finite. Every integral below
is over \((2,\infty)\).

## 2. Positive remainders, including the entire physical grid

For real \(c<2\), put
\[
 L_c(C)=\eta\sum_{j<m}\frac{F_j(c)F_j(C)}{h_j},\quad
 K_c=\sum_{j<m}\frac{F_j(c)^2}{h_j},\quad
 d\nu_c(x)=(x-c)d\mu(x),\quad
 V_c(C)=\int\frac{L_c(x)^2}{x-C}\,d\nu_c(x).
 \tag{6}
\]
The square here is bilinear, not an absolute square; it is nonnegative
and not identically zero on the interval because \(c\) is real.

**Theorem 1.** \(L_c\) has degree \(m-1\), with exactly \(m-1\)
simple roots in \((2,\infty)\). The function \(V_c\) is holomorphic
and zero-free on \(\Omega\), positive below \(2\), and has strictly
positive imaginary part in the upper half-plane. Exactly,
\[
 \boxed{\quad
 \widehat H_{A_c}(C)=
 \frac{P_N(C)V_c(C)/L_c(C)-\eta P_N(c)}{N^2(C-c)}.
 \quad}
 \tag{7}
\]
At every physical node \(c\), including the odd simple node, this is
\[
 \boxed{\quad
 \widehat H_{A_c}=\frac{P_N V_c}{N^2(C-c)L_c},\qquad
 \frac{\widehat H_{A_c}}{L_c}
       =\frac{P_N V_c}{N^2(C-c)L_c^2},\qquad
 \frac{\widehat H_{A_c}}{TA_c}=\frac{\eta V_c}{L_c}.
 \quad}
 \tag{8}
\]
Thus the first two functions in (8) have exactly the off-cut zero
divisor \(P_N/(C-c)\), with full multiplicities. The last ratio is
a holomorphic zero-free unit, positive below \(2\), and equal to
\(1\) at \(C=c\).

**Proof.** Orthogonality in (5) gives the evaluation formula
\[
 \int L_cf\,d\mu=\eta f(c)\quad(\deg f\le m-1),\qquad
 \int L_cq\,d\nu_c=0\quad(\deg q\le m-2).
 \tag{9}
\]
For the latter take \(f(x)=(x-c)q(x)\). All required moments
have degree at most \(2m-2\le N-2\). The top row coefficient in
\(L_c\) is nonzero. If \(L_c\) had fewer than \(m-1\) sign changes
in \((2,\infty)\), multiply it by the product of its sign-changing
roots there. The result would have fixed nonzero sign and finite
integral against \(\nu_c\), contradicting (9). Hence all its roots
are simple and lie in that interval. For \(m=1\), it is constant.

The density \(L_c^2d\nu_c\) is asymptotic to a positive constant
times \(x^{-1}\) for even \(N\), and \(x^{-2}\) for odd \(N\).
Thus (6) converges normally on compact slit sets, even though the
measure has infinite total mass at even levels. Its imaginary part
has the sign of \(\Im C\); on the real slit complement it is positive.
This proves its asserted positivity and absence of zeros.

Apply (9) to \((L_c(x)-L_c(C))/(x-C)\), whose degree is at most
\(m-2\), or which is zero when \(m=1\). It follows that
\[
 V_c(C)=L_c(C)\int\frac{L_c(x)}{x-C}\,d\nu_c(x).
 \tag{10}
\]
Also \(\int L_c\,d\mu=\eta\), whence
\[
 \frac{\eta}{C-c}+\int\frac{L_c(x)}{x-C}\,d\mu(x)
   =\frac1{C-c}\int\frac{L_c(x)}{x-C}\,d\nu_c(x).
\]
Substitution in (3) and (5) proves (7). Its apparent pole at
\(C=c\) is removable, since \(V_c(c)=K_c\) and \(L_c(c)=\eta K_c\).
At physical \(c\), \(P_N(c)=0\) gives (8). Neither \(L_c\) nor
\(V_c\) has an off-cut zero, and (6) gives \(L_c\) sign \(\eta\)
below \(2\). These facts prove the remaining assertions.
\(\square\)

For fixed real \(c\), division of the second ratio in (8) only by
its forced divisor leaves \(V_c/(N^2L_c^2)\), which is zero-free.
The positive Cauchy function itself is \(V_c\); no half-plane
mapping property for \(V_c/L_c^2\) is inferred.

## 3. Uniform all-row bounds and the full normal identity

**Theorem 2.** On each fixed compact \(K\Subset\Omega\), uniformly
for every physical node \(c\) and every \(N\ge2\),
\[
             a_KN^{-2}\le |V_c(C)|/K_c\le b_K
                  \qquad(C\in K),
 \tag{11}
\]
where \(a_K,b_K>0\) are independent of the row and level.

**Proof.** Equation (5) gives \(\int L_c^2d\mu=K_c\). Write the
integrand in (6) as \(L_c^2(x)(x-c)/(x-C)\,d\mu\).
All physical \(c\) lie in \([-2,c_0]\), so
\((x-c)/(x-C)=1+(C-c)/(x-C)\) gives the uniform upper bound.
For the lower bound put \(\alpha(C)=\arg(2-C)\in(-\pi,\pi)\).
The argument of \(x-C\), \(x\ge2\), lies between \(0\) and
\(\alpha(C)\). After multiplication by \(e^{i\alpha(C)/2}\)
the integrand has real part at least its modulus times
\(\cos(\alpha(C)/2)\), uniformly positive on \(K\).
Take \(R\ge\max(2,\sup_K|C|)\). Since \(R+c\ge0\),
\[
 |V_c(C)|\ge a\int L_c^2\frac{x-c}{x+R}\,d\mu
       \ge a\frac{2-c}{2+R}K_c
       \ge a'_K N^{-2}K_c,
 \tag{12}
\]
using \(2-c\ge2-c_0=4\sin^2(\pi/(2N))\ge4/N^2\).
\(\square\)

In particular \(V_c/K_c\) contributes only \(O_K(\log N)\) to
logarithmic magnitude. For the original unit \(A_{c_0}=1\),
\[
 K_{c_0}=\sum_{j<m}h_j^{-1}
         =4\sin^2(m\theta)\in[2,4].
 \tag{13}
\]
Thus \(a_KN^{-2}\le|V_{c_0}|\le b_K\). These bounds do not
assert subexponential growth of the full unit \(\eta V_c/L_c\);
its explicit factor \(1/L_c\), and for other rows \(K_c\), remain.

There is also an exact source-normal statement, with no hidden
complex-color denominator. Define
\[
 J_c(C)=\int L_c(x)\frac{x-c}{x-C}\,d\mu(x).
\]
This is polynomial in complex \(c\) and holomorphic in \(C\in\Omega\).
The evaluation identity (9) holds for all complex \(c\), so (10)
gives \(V_c=L_cJ_c\) algebraically; the bilinear square in (6)
continues unchanged. Also \(J_C(C)=\eta\). Thus (7), with \(V_c/L_c\)
interpreted as \(J_c\), is entire in \(c\), with its diagonal
singularity removed. Positivity is asserted only for real \(c<2\).
At a double physical node,
\(G_j=\partial_cK_N(c,\cdot)|_{c_j}\), and \(P_N(c_j)=P_N'(c_j)=0\).
Differentiating (7) therefore proves
\[
 \boxed{\quad
 \widehat H_{G_j}(C)=\frac{P_N(C)}{N^2}
   \left.\partial_c\!
    \left(\frac{V_c(C)}{(C-c)L_c(C)}\right)\right|_{c=c_j},
 \qquad TG_j(C)=\frac{\eta P_N(C)}{N^2(C-c_j)^2}.
 \quad}
 \tag{14}
\]
The physical singularities are interpreted by removable
continuation. This is the specified original Ward representative,
since (4)--(5) are linear in all input coefficients. It retains all
inner physical first normals as well. No positive bound on the
parameter derivative in (14) is inferred from (11). There is no
\(G_*\) at the odd simple node.

## 4. The unstripped turned-unit ratio

Set \(\mathfrak m_N=\widehat H_1/L_{c_0}\). Its exact cut jump,
away from the finitely many roots of \(L_{c_0}\), remains
\[
 \mathfrak m_{N,+}(x)-\mathfrak m_{N,-}(x)=2\pi i\rho_N(x),
 \tag{15}
\]
because \(\mathfrak m_N=\widetilde Q_N+Y_1/L_{c_0}\).
Nevertheless its Pick kernel
\[
 \mathcal K_N(z,w)=
 \frac{\mathfrak m_N(z)-\overline{\mathfrak m_N(w)}}{z-\overline w}
 \tag{16}
\]
has at least \(m-1\) negative squares: a finite Gram matrix has
that many strictly negative eigenvalues. Indeed (8) gives an
exact double zero at each \(c_j\), \(1\le j<m\):
\(\mathfrak m_N(c_j+\zeta)=a_j\zeta^2+O(\zeta^3)\), with real
\(a_j\ne0\). Choose \(\vartheta_j\in(0,\pi)\) with
\(a_j\sin(2\vartheta_j)<0\), and set \(z_j=c_j+t e^{i\vartheta_j}\).
At each fixed level, as \(t\downarrow0\),
\[
 \mathcal K_N(z_j,z_j)=-d_jt+O(t^2),\quad d_j>0,\qquad
 \mathcal K_N(z_i,z_j)=O(t^2)\quad(i\ne j).
 \tag{17}
\]
The matrix is negative definite for small \(t\). No uniform
spacing or quantitative eigenvalue estimate is required.

For \(N\ge3\), this ratio is neither Herglotz nor anti-Herglotz:
it is real across \((-\infty,2)\) and has at least two distinct
zeros there, including the odd simple zero when \(N=3\).
Either mapping property would force its real derivative to have
one sign, by expansion at \(x+iy\), and hence force it to vanish
between these zeros. This contradicts (8). At \(N=2\),
\(L_{c_0}=-4\) and \(\mathfrak m_2=\widetilde Q_2\);
the negative-square lower bound is then vacuous.

This concerns the specified ratio with its forced divisor still
present. Its positive stripped remainder is proved above. For
general received inputs, \(L_A\) has generally complex physical
weights and \(Y_A\) retains independent normal data, so (9) no
longer follows. Thus no class closed under arbitrary signed
crossings, products or further turns has been proved. Other scalar
ratios and matrix transfers are not excluded. No geometric
coefficient lower bound, knot or volume counterexample is asserted.

## Complete direct sources

* research_positive_ward_measure_and_coherent_cauchy_tail.md,
  SHA256 18d2aa9142806d0acd744abbbb412843acd35bf18015b8c6fc73b23428a75096:
  full original Ward representative, positive measure, orthogonality,
  coherent tail, cut jump, and odd simple scope.
* actual_newton_turn_positive_gram.md,
  SHA256 d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3:
  genuine unscaled full-normal turn and Newton product normalization.

Both complete texts were read and the used implications checked.
The new step is their original-row specialization and positive
remainder, not a new general orthogonal-polynomial theorem.
Only written mathematics, source reads and file hashes were used.
No programs, numerical tests, builds or frozen/public edits were made.
