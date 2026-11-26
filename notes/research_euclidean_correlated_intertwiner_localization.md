# Actual Euclidean off-matching windows and their Ward current

Private written proof, 19 November 2026.

An actual total intertwiner can be restricted by a correlated coherent
window which keeps the entire real lowering-observable matching locus
and every occupation endpoint. The discarded operator and the resulting
Ward current have exponentially small trace norm relative to the norm
of the original whole operator. The estimate is in the physical
coefficient Euclidean metric, with the actual meridian family and caps.

This is a positive norm estimate for an explicit marked operator.
Its budget is the whole-operator norm, not a selected geometric
contribution. It neither isolates a geometric component nor estimates
the contribution of the original relative cycle.

The complete directs W and B, pinned below, supply the actual source
comparison and its Euclidean boundary-kernel bridge. The localization
argument is proved here from the finite lowering matrices; no estimate
in the binomial Hilbert metric is transferred to this metric.

## 1. Actual matrices, real observable, and window

Fix \(m\ge2\), \(N\ge2\), \(d=N-1\), and
\[
 h=N^{-1},\quad c_0=2\pi i,\quad Q=e^{c_0h},\quad
 q=e^{\pi ih},\quad M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
On \(V=\operatorname{span}\{w_0,\ldots,w_d\}\), the displayed vectors
are orthonormal. All norms use the tensor coefficient metric;
\(\|\cdot\|\) is operator norm and \(\|\cdot\|_1\) is trace norm.
Use exactly
\[
 Ew_a=(MQ^{-a}-M^{-1})w_{a-1}\ (a>0),\quad Ew_0=0,\qquad
 Kw_a=xQ^{-a}w_a,
\]
\[
 E_\Sigma=\sum_{j=1}^m E_jK_{j+1}\cdots K_m.
 \tag{2}
\]
Every operator in this note acts on \(V^{\otimes m}\). Let \(W_N(M)\)
be a holomorphic actual family on a buffered scaled meridian disk,
with
\[
                        E_\Sigma(M)W_N(M)=W_N(M)E_\Sigma(M).
 \tag{3}
\]
In particular any actual fixed braid word satisfies the required
lowering identity. Its original scalar and prescribed current-free
marks remain in \(W_N\). No norm bound for \(W_N\) is assumed.

Use B's coefficient-Euclidean coherent vectors and probability measure,
\[
 \psi_z=(1+|z|^2)^{-d/2}\sum_{a=0}^d\sqrt{\binom da}\,z^a w_a,
 \qquad d\nu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
 \tag{4}
\]
Write tensor products as \(\psi_{\mathbf z}\). On a chart with
\(z_j\ne0,\infty\), define
\[
 p_j=\frac{|z_j|^2}{1+|z_j|^2},\qquad
 e(z_j)=\frac{z_j}{|z_j|}(e^{-c_0p_j}-1),\qquad
 k(z_j)=-e^{-c_0p_j},
\]
\[
             \epsilon(\mathbf z)
                  =\sum_{j=1}^m e(z_j)\prod_{\ell>j}k(z_\ell).
 \tag{5}
\]
These are the principal values for the real Euclidean coherent states
in (4), as verified below. They are not the weak values of an
arbitrary off-diagonal kernel.
They extend continuously to the endpoints by \(e(0)=e(\infty)=0\)
and \(k(0)=k(\infty)=-1\); analytic estimates use only strict charts.

Here is an explicit fixed window. Choose a smooth
\(0\le\kappa\le1\) with compact support in
\((\mathbb C^\times)^m\times(\mathbb C^\times)^m\), a number
\(\gamma>0\), and a smooth function \(0\le\vartheta\le1\) on
\([0,\infty)\) which is zero on \([0,\gamma^2]\) and one on
\([4\gamma^2,\infty)\). Set
\[
 b(\mathbf y,\mathbf z)
  =\kappa(\mathbf y,\mathbf z)\,
       \vartheta(|\epsilon(\mathbf y)-\epsilon(\mathbf z)|^2),
 \qquad \chi=1-b.
 \tag{6}
\]
Extend \(b\) by zero outside the protected chart. Thus \(\chi=1\)
near every pair with \(\epsilon(\mathbf y)=\epsilon(\mathbf z)\),
and near every occupation endpoint in either set of variables.
On the support of \(b\) the observable gap is at least \(\gamma\).
Both functions are independent of \(N\) and \(\mu\).

Define the actual correlated marked operator
\[
 C_{\chi,N}(M)=N^{2m}\int\chi(\mathbf y,\mathbf z)
 |\psi_{\mathbf y}\rangle
 \langle\psi_{\mathbf y},W_N(M)\psi_{\mathbf z}\rangle
 \langle\psi_{\mathbf z}|\,
                         d\nu^{[m]}(\mathbf y)d\nu^{[m]}(\mathbf z),
\]
\[
                            R_N=W_N-C_{\chi,N}.
 \tag{7}
\]
This is a finite matrix integral. A correlated \(\chi\) need not
factor into separate input and output windows, and \(C_{\chi,N}\)
is not asserted to be positive or a projection.

**Theorem.** Fix \(0<\eta<\eta'<\pi\). There are \(C,c>0\),
independent of \(N,W_N\), such that on \(|N\mu|\le\eta'\),
\[
 \|R_N(M)\|_1+\|[E_\Sigma(M),C_{\chi,N}(M)]\|_1
            \le C N^{2m}e^{-cN}\|W_N(M)\|.
 \tag{8}
\]
Constants may depend on \(m,\eta'\) and the fixed window. Put
\(\mathcal W_N=\sup_{|N\mu|\le\eta'}\|W_N(e^\mu)\|\).
They do not depend on the word length or integer filling powers
inside \(W_N\). Holomorphy is assumed on a neighborhood of this
closed larger disk.
For every fixed \(r\ge0\), on the smaller disk,
\[
 N^{-r}\left(\|\partial_\mu^rR_N\|_1+
        \|\partial_\mu^r[E_\Sigma,C_{\chi,N}]\|_1\right)
                 \le C_rN^{2m}e^{-cN}\mathcal W_N.
 \tag{9}
\]
The norms are literal matrix norms in the stated metric. The constants
and exponent do not depend on a phase choice or a nonzero entry of
\(W_N\). All finite levels are included after enlarging \(C,C_r\).

## 2. Exact local rows and the cap-safe power estimate

Represent a vector locally as \(\psi_z(a)H(a/N)\), and write
\(t=a/N\). Ratios of the coefficients in (4) give the exact rows
\[
 \begin{split}
 \mathcal E_{z,h,\mu}H(t)
 &=z\sqrt{\frac{1-h-t}{t+h}}\,
       (e^\mu e^{-c_0(t+h)}-e^{-\mu})H(t+h),\\
 \mathcal K_{z,h,\mu}H(t)
 &=-e^\mu e^{-\pi ih}e^{-c_0t}H(t).
 \end{split}\tag{10}
\]
They are used only in a fixed complex tube about a strict subinterval
of \((0,1)\), where the square roots have analytic branches agreeing
with their positive real values. No analytic extension across a cap
is asserted. The actual adjoint lowering row is
\[
 \mathcal E^*_{z,h,\mu}H(t)
 =z^{-1}\sqrt{\frac{t}{1-t}}\,
             (e^{\bar\mu}e^{c_0t}-e^{-\bar\mu})H(t-h),
 \tag{11}
\]
and the Cartan adjoint is the conjugate diagonal row. The adjoint
rows are pointwise statements in \(\mu\), not holomorphic
differentiation in \(\bar\mu\).

Compose these rows in the ordered sum (2). On each protected compact
coherent chart, both \(E_\Sigma\) and its adjoint act on amplitudes
by a fixed finite set of shifts of size at most \(h\) in each
coordinate, with uniformly bounded holomorphic coefficients on a
fixed tube about the corresponding binomial means. At \(h=\mu=0\),
their multiplication values at the mean are respectively
\(\epsilon(\mathbf z)\) and \(\overline{\epsilon(\mathbf z)}\).
This follows directly from (10)--(11) at
\(t_j=p_j\), including every factor in (2).

For \(|\mu|\le\eta'h\), the sum of the local coefficients differs
from that principal value by at most
\[
                              C(|\mathbf t-\mathbf p|+h).
 \tag{12}
\]
Independently, the finite matrices in (2) and their adjoints have
uniformly bounded Euclidean norm on the scaled collar. Indeed
\(\|E\|\le |M|+|M|^{-1}\) and \(\|K^{\pm1}\|=|M|^{\pm1}\).
They have propagation at most one in the maximum occupation distance.
These global facts use the exact zero arrows at the caps.

Let \(D_N=E_\Sigma-\epsilon(\mathbf z)I\). The same argument below
applies to \(E_\Sigma^*-\overline{\epsilon(\mathbf z)}I\).
Choose \(k=\lfloor\delta N\rfloor\ge1\), and put
\[
                              \rho=A\sqrt{k/N}.
 \tag{13}
\]
Choose \(A\) first and then \(\delta\) sufficiently small. The
polydisk of radius \(2\rho\) about the mean lies in the coefficient
tube. Use \(k\) nested polydisks between radii \(2\rho\) and
\(\rho\), with radius decrement \(\rho/k\). The shift condition
\(kh\le\rho/2\) holds after reducing \(\delta\). Multiplication
estimate (12), and Cauchy's estimate for each shifted difference
\(H(\mathbf t+h\mathbf s)-H(\mathbf t)\), give at every step
\[
 \|\mathcal D_N H\|_{\rm next}
 \le C\left(\rho+h+\frac{k}{N\rho}\right)\|H\|_{\rm previous}.
 \tag{14}
\]
Thus, for all \(0\le j\le k\), the exact sampled amplitude of
\(D_N^j\psi_{\mathbf z}\) on
\(|\mathbf a/N-\mathbf p|\le\rho\) is bounded by
\[
                 q_\delta^j,\qquad
 q_\delta=C(A+A^{-1}+1)\sqrt\delta.
 \tag{15}
\]
Every contributing path there stays in the local tube. The same
nested \(k\) domains are used for all \(j\le k\).

The complementary output indices require a different argument.
Let \(P_{\rm out}\) project onto
\(|\mathbf a/N-\mathbf p|>\rho\). Exact finite propagation gives
\[
 P_{\rm out}D_N^j
 =P_{\rm out}D_N^j
       \mathbf1_{\{|\mathbf a/N-\mathbf p|>\rho-jh\}}.
 \tag{16}
\]
Since \(jh\le\rho/2\), only the initial binomial tail outside
\(\rho/2\) can reach these outputs. Intermediate paths may touch
a cap; the global finite matrix norm, rather than (10), bounds them.

The squared coefficients of \(\psi_{\mathbf z}\) are independent
binomial probabilities with means \((1-h)p_j\). Their tail obeys
\[
 \mathbb P(|\mathbf a/N-\mathbf p|>r)
                                      \le C e^{-c_1Nr^2}
 \tag{17}
\]
when \(h\le r/2\). One direct proof uses the Bernoulli moment
generating function: the second derivative of
\(\log(1-p+pe^\lambda)\) is at most \(1/4\) for real \(\lambda\).
Integration twice, Markov's inequality, optimization in \(\lambda\),
and a union bound give (17), including the \(O(h)\) shift of the mean.
Equations (16)--(17) and \(\|D_N\|\le C_0\) show that the outside
norm is at most \(C C_0^j e^{-c_2A^2k}\). Therefore
\[
 \|D_N^j\psi_{\mathbf z}\|
       \le q_\delta^j+C C_0^j e^{-c_2A^2k},
                         \qquad 0\le j\le k.
 \tag{18}
\]
For any prescribed fixed \(B>0\), choose \(A\) so large that the
second term is at most \(Ce^{-Bk}\) for every \(j\le k\).
Then choose \(\delta\) to make \(q_\delta\) small and all tubes
valid. The two terms remain a sum: the tail is not absorbed into
\(q_\delta^j\).

## 3. Intertwining and the correlated trace-norm estimate

Fix protected \(\mathbf y,\mathbf z\), and put
\(\alpha=\epsilon(\mathbf y)\), \(\beta=\epsilon(\mathbf z)\),
\(D_+=E_\Sigma-\alpha I\), \(D_-=E_\Sigma-\beta I\).
Equation (3) gives
\[
                      (\alpha-\beta)W_N=W_ND_- -D_+W_N.
 \tag{19}
\]
Left and right multiplication commute. Expanding its \(k\)-th
power exactly and taking the coherent entry proves
\[
 |\alpha-\beta|^k|\langle\psi_{\mathbf y},W_N\psi_{\mathbf z}\rangle|
 \le\|W_N\|\sum_{j=0}^k\binom kj
       \|(D_+^*)^j\psi_{\mathbf y}\|\,
       \|D_-^{k-j}\psi_{\mathbf z}\|.
 \tag{20}
\]
Apply (18) to both factors. The sum is bounded by
\[
 (2q_\delta)^k+
 C e^{-Bk}(1+q_\delta)^k+C e^{-2Bk}2^k.
 \tag{21}
\]
First choose \(B\) sufficiently large in terms of \(\gamma\),
then \(A\) as above, and finally \(\delta\) with
\(q_\delta<\min(1/4,\gamma/4)\). Dividing (21) by
\(|\alpha-\beta|^k\ge\gamma^k\) gives, uniformly on the support of \(b\)
in (6) and on the scaled meridian collar,
\[
 |\langle\psi_{\mathbf y},W_N(M)\psi_{\mathbf z}\rangle|
                        \le C e^{-cN}\|W_N(M)\|.
 \tag{22}
\]
B's exact resolution is \(N\int|\psi_z\rangle\langle\psi_z|d\nu=I\).
Applying it on both sides of \(W_N\) shows that (7) with
\(\chi=1\) is exactly \(W_N\). Hence \(R_N\) is the same integral
with multiplier \(b=1-\chi\). Each outer rank-one matrix has
nuclear norm one. Its middle scalar satisfies (22), and the
product measure has mass one. Therefore
\[
                       \|R_N(M)\|_1
                         \le C N^{2m}e^{-cN}\|W_N(M)\|.
 \tag{23}
\]
Since \(W_N\) intertwines \(E_\Sigma\),
\([E_\Sigma,C_{\chi,N}]=-[E_\Sigma,R_N]\).
The inequality
\(\|[E_\Sigma,R_N]\|_1\le2\|E_\Sigma\|\|R_N\|_1\)
proves (8).

The fixed cutoff and coherent vectors make \(R_N\) a holomorphic
matrix family in \(\mu\). Its commutator is holomorphic as well.
Cauchy's formula in the finite-dimensional trace-norm space, on
the buffer between \(\eta/N\) and \(\eta'/N\), proves (9).
In particular these are actual derivatives of the capped meridian
matrices, not derivatives of a root coherent symbol.
For example the first current derivative is
\([\,\partial_\mu E_\Sigma,C_{\chi,N}\,]
 +[\,E_\Sigma,\partial_\mu C_{\chi,N}\,]\); neither term is omitted.

## 4. Degree pinching and the original closed source

If the actual word has integer degree zero, put
\(J_\Sigma=\sum_jJ_j\), \(U_\theta=e^{i\theta J_\Sigma}\), and
\[
 \overline C_{\chi,N}
   =\frac1{2\pi}\int_0^{2\pi}
                U_\theta C_{\chi,N}U_\theta^{-1}\,d\theta.
 \tag{24}
\]
Then \(\overline C_{\chi,N}\) has degree zero and
\(W_N-\overline C_{\chi,N}\) is the same average of \(R_N\).
Unitary invariance and the triangle inequality contract its trace
norm. Since \(U_\theta E_\Sigma U_\theta^{-1}=e^{-i\theta}E_\Sigma\),
\[
 [E_\Sigma,\overline C_{\chi,N}]
  =\frac1{2\pi}\int e^{i\theta}
          U_\theta[E_\Sigma,C_{\chi,N}]U_\theta^{-1}\,d\theta.
 \tag{25}
\]
Thus (8)--(9) hold for the degree-preserving window too, including
every true meridian jet.

For clarity the original coupons and supported projections of W and B are
\[
 \begin{split}
 Q_{\rm pt}&=\Pi_0\otimes K_2^{-d}\otimes K_Z^{-d},&
 Q_{\rm top}&=|0\rangle\langle d|\otimes|d\rangle\langle0|
                                                  \otimes K_Z^{-d},\\
 P&=\Pi_0\otimes(I-\Pi_0)\otimes I_Z,&
 L&=\mathbf1_{\{J_1+J_2\le d-1\}}\otimes I_Z ,
 \end{split}
\]
where \(Z=V^{\otimes(m-2)}\), \(\Pi_0=|0\rangle\langle0|\), and
the empty spectator tensor has \(K_Z=I\). Put
\(\Phi_M(C)=\operatorname{Tr}(Q_{\rm pt}C)\).
Both coupons have degree zero, so (24) changes neither trace pairing.
For either choice \(C=C_{\chi,N}\) or \(\overline C_{\chi,N}\),
the actual compressed current is
\[
                         Y=L[E_\Sigma,C]P.
 \tag{26}
\]
Compression contracts trace norm. B's exact vacuum-input resolution
then supplies a concrete boundary-kernel estimate:
\[
 N^{-r}\|\mathcal K_{\partial_\mu^rY}\|_{L^2}
 \le C_rN^{m+1/2}e^{-cN}\mathcal W_N.
 \tag{27}
\]
Indeed \(\|\mathcal K_Y\|_{L^2}=N^{-m+1/2}\|Y\|_{\rm HS}\)
and \(\|Y\|_{\rm HS}\le\|Y\|_1\). The kernel is unnormalized,
with the first input head at the vacuum and all remaining caps retained.

There are also direct closed-source estimates. The coupons have
uniformly bounded operator norm on a fixed scaled collar, and
\(\Phi_M(W_N)=\operatorname{Tr}(Q_{\rm top}W_N)\) by (3) and W.
Consequently, for every fixed \(r\), on the smaller collar,
\[
 \begin{split}
 N^{-r}\left|\partial_\mu^r
       \{\Phi_M(C)-\Phi_M(W_N)\}\right|
       &\le C_rN^{2m}e^{-cN}\mathcal W_N,\\
 N^{-r}\left|\partial_\mu^r
       \{\Phi_M(C)-\operatorname{Tr}(Q_{\rm top}C)\}\right|
       &\le C_rN^{2m}e^{-cN}\mathcal W_N .
 \end{split}\tag{28}
\]
For the second row subtract the exact zero discrepancy for \(W_N\)
and pair \(C-W_N\) with \(Q_{\rm pt}-Q_{\rm top}\); this gives the
stated bound without an additional primitive factor. All pivot
derivatives are included. Equivalently W's polynomial Ward identity
applies to the small current in (26). Root-only commutation would not
justify (9), (27), or (28); the whole-family identity (3) is used.

The budget \(\mathcal W_N\) may itself grow exponentially. Neither
\(c\) nor \(\mathcal W_N\) is calibrated here against a geometric
action or a nonzero top-source contribution. The window keeps the
whole real matching locus and all endpoint charts, so no geometric
component or original relative-cycle coefficient has been selected.
Independent coherent arguments can describe complex mixed coordinates,
but this fact does not turn the real principal values in (5) into a
proved geometric boundary-decay estimate. No new volume case follows.

## Complete directs and author verification

* W: [research_polynomial_top_source_ward_transport.md](research_polynomial_top_source_ward_transport.md),
  376 lines, SHA256
  \(\texttt{fe6493819fa24ce3ccf27b4625be57f34513d6542830f9aeb591fed6e495d8ad}\).
* B: [research_compressed_euclidean_boundary_current.md](research_compressed_euclidean_boundary_current.md),
  313 lines, SHA256
  \(\texttt{ada0f793a92ef4f9d42a1d0a32ac5e76c28ec4b6f70af97ae5cc317993cc677d}\).

Both complete directs were freshly read nontruncated in this
uninterrupted author sequence; their matching source and metric
implications were checked. The earlier binomial-metric real
localization note was a coverage read, not a transferred norm proof.
Only written mathematics and text/hash operations were used.
No mathematical programs, numerical tests, builds, or frozen-file
edits were performed. The entire matching final and both complete
directs were freshly reread nontruncated before the final pins were
renewed. Independent matching-final review and parent adoption remain
separate.
