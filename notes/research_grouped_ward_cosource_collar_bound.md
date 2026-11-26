# A collar bound for the actual grouped Ward co-source

Private written proof, 19 November 2026.

The explicit grouped co-source in F's forced highest-cut formula has
an exponential bound with a specified width-dependent rate. Its pole,
finite part, and next Laurent coefficient have the same exponential
rate and only polynomially different costs. The bound concerns the
literal primitive in F, including its chosen turnover and Jordan
solver. It does not replace that primitive by an abstract solution of
a commutator equation.

The complete directs F and M are pinned below. F supplies the exact
forced source and its chosen primitive. M supplies the actual arrows,
turnover, prefix frames, and their polynomial collar conditioning.
The finite norm estimates and scalar error bounds are proved here.

## 1. The fixed source, norm, and collar

Fix \(m\ge2\), \(N\ge2\), \(d=N-1\), \(r=m-1\),

\[
 q=e^{\pi i/N},\quad Q=q^2,\quad M=e^\mu,\quad x=-M/q,
 \quad f_a=(Q;Q)_a.
 \tag{1}
\]

The physical occupation basis on \(V=(\mathbb C^N)^{\otimes m}\)
is orthonormal for the norm used throughout this note. All operator
norms below are its Euclidean operator norm. The remaining-head space
is \(U=(\mathbb C^N)^{\otimes r}\), with insertion and extraction
\(i_0,p_0\) of first occupation zero. Put

\[
 K_{\rm r}(M)=M^rK_0,\quad K_0^N=\varepsilon I,
 \quad\varepsilon=(-1)^{(N+1)r},\quad g=K_{\rm r}^{-d}.
 \tag{2}
\]

The prescribed functional, for an arbitrary analytic matrix \(A(M)\),
is the literal highest cut

\[
 \Phi(A)=\operatorname{Tr}_V((P_0\otimes g)A),\qquad
 P_0=|0\rangle\langle0|.
 \tag{3}
\]

No averaged cut or summed-output coupon is substituted. An external
scalar line is retained by applying every formula to \(\Xi(M)A(M)\).

Write \(S=S_m(M)\), \(q_F=p_0S^{-1}\), and

\[
 H=D_N(MK_{\rm r}),\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{4}
\]

F's exact formula is

\[
 \Phi(A)=D_N(M)\operatorname{Tr}_U(H^{-1}q_FAi_0)
       +\operatorname{Tr}_V(\mathcal W_E[E_\Sigma,A]).
 \tag{5}
\]

The finite part is taken in the fixed coordinate \(\mu=\log M\).
The primitive \(\mathcal W_E\) has at most a simple pole. Its
definition is recalled in Section 3 so that the bound refers to
exactly the same matrix as (5).

Fix buffered radii

\[
             0<\eta<\eta'<\pi/m,\qquad u=N\mu.
 \tag{6}
\]

There are constants \(C,p\), depending only on \(m,\eta'\), such that

\[
 \boxed{\quad
 \sup_{|u|\le\eta'}\left\|\frac uN
              \mathcal W_E(e^{u/N})\right\|
       \le C N^p\Lambda_m^N,\qquad
       \Lambda_m=2^{5m-2}.
 \quad}\tag{7}
\]

The notation \(\mathcal W_E(e^{u/N})\) means evaluation in its
meridian argument \(M\); the expression at \(u=0\) is removable.
The explicit rate is conservative. It is independent of \(A\), of a
braid length, and of any spectral or coherent localization of \(A\).

## 2. Bounds for the literal finite changes of basis

First work at \(M=1\). The prefix is

\[
 S_0=\sum_{n=0}^d\frac{(x_0^{-1}L_1F_{\rm r}(1))^n}{f_n},
 \qquad x_0=-q^{-1}.
 \tag{8}
\]

The ordered coproduct decomposes its argument as a sum of \(r\)
operators

\[
 X_j=x_0^{-1}L_1
             \left(\prod_{i=2}^{j-1}K_i(1)^{-1}\right)F_j,
                      \qquad 2\le j\le m.
 \tag{9}
\]

For \(j<k\), \(X_jX_k=Q^{-1}X_kX_j\). The finite quantum
binomial formula consequently gives

\[
 S_0=\prod_{j=2}^m e_Q(X_j),\qquad
 e_Q(X)=\sum_{n=0}^d X^n/f_n,
 \tag{10}
\]

with increasing \(j\) from left to right. All terms of total donor
lowering degree at least \(N\) vanish, so no infinite series is used.
The inverse reverses this order and replaces each factor by

\[
 e_Q(X)^{-1}=\sum_{n=0}^d(-1)^nQ^{n(n-1)/2}X^n/f_n.
 \tag{11}
\]

Here each factor has a direct absolute row and column estimate.
For fixed spectators, an input donor and recipient occupation
\((a,b)\) goes to \((a-n,b+n)\), with
\(0\le n\le\min(a,d-b)\). Its coefficient has modulus

\[
 \left|\frac{f_{b+n}}{f_bf_n}\right|
       =\left|{b+n\brack n}_Q\right|
       \le {b+n\choose n}.
 \tag{12}
\]

The inequality follows from the Gaussian polynomial's nonnegative
integer coefficients and evaluation at \(Q=1\). All other factors
in (9) have modulus one. For fixed output recipient occupation \(c\),
the row sum is at most \(\sum_{n=0}^c{c\choose n}=2^c\le2^d\).
For fixed input \(b\), the column sum is at most

\[
 \sum_{n=0}^{d-b}{b+n\choose n}
       ={d+1\choose b+1}\le2^N.
 \tag{13}
\]

The inverse factor has the same absolute coefficients. The inequality
\(\|T\|_2\le\sqrt{\|T\|_1\|T\|_\infty}\) proves

\[
                    \|S_0^{\pm1}\|\le2^{rN}.
 \tag{14}
\]

M's exact formula \(S(M)=B_F(M)S_0B_F(M)^{-1}\), with
\(B_F=M^{-\sum_i(i-1)J_i}\), retains every prefix endpoint.
On (6), its condition number is at most \(e^{\eta'mr}\).
Hence, also with \(M\) replaced by \(M^{-1}\),

\[
                    \|S(M)^{\pm1}\|\le C_{m,\eta'}2^{rN}.
 \tag{15}
\]

The remaining scalar factorial diagonal \(D_fw_a=f_aw_a\) obeys

\[
                  \|D_f\|\le2^N,\qquad
                  \|D_f^{-1}\|\le2^{N/2}.
 \tag{16}
\]

For the second bound, if \(a\le N/2\), then

\[
 |f_a|\ge(4/N)^a a!,\qquad
 |f_a|^{-1}\le(N/4)^a/a!\le e^{N/4}\le2^{N/2}.
 \]

If \(a>N/2\), the exact absolute reflection
\(|f_a||f_{d-a}|=N\) instead gives
\(|f_a|^{-1}\le2^{d-a}/N\le2^{N/2}\).
This includes both parities and all \(N\ge2\).

Finally M gives the literal turnover, including tensor reversal,

\[
 \mathscr C(M)=C(M)^{\otimes m}\mathsf J,\quad
 C(M)w_a=c_a(M)w_{d-a},\quad
 c_a(M)=(-1)^a h_a(M^{-1})^{-1},
 \tag{17}
\]

where \(h_a(M)=M^{-a}f_a/(M^{-2}Q;Q)_a\). The last equality
follows directly by factoring \(-M^{-1}\) from each numerator
\(MQ^j-M^{-1}\). M proves that \(h_a\) and its inverse have
uniform polynomial bounds on every scaled disk of radius less than
\(\pi\). These diagonal bounds are identical in the physical Euclidean
and binomial metrics. The complement and reversal permutations are
unitary in the Euclidean metric. Therefore

\[
            \|\mathscr C^{\pm1}\|\le C N^{p_0}.
 \tag{18}
\]

There has been no replacement of the chosen turnover by a different
Jordan frame.

## 3. The regularized co-source and its finite solver

F defines

\[
 Q_E=P_0\otimes g-D_N(M)i_0H^{-1}q_F,
 \quad \mathcal U_E=\mathscr C(M)S(M^{-1})(D_f\otimes I),
 \quad \widehat Q_E=\mathcal U_E^{-1}Q_E\mathcal U_E.
 \tag{19}
\]

The second term in \(Q_E\) has only a simple pole. More quantitatively,
on any physical weight \(K_0=\chi\), \(|\chi|=1\),

\[
 \mu D_N(M)H^{-1}
  =\frac{u/N}{\sinh(u/N)}
     \frac{\sinh u}{2\varepsilon\sinh(mu)}
       (e^{mu/N}\chi-e^{-mu/N}\chi^{-1}).
 \tag{20}
\]

Here \(m u\) is the product of the fixed head count and \(u\),
not the meridian coordinate \(\mu\). Both removable quotients are
bounded on (6); the restriction \(\eta'<\pi/m\) excludes every
other zero of \(\sinh(m u)\). Also \(\|g\|\le e^{r\eta'}\).
Equations (15),(20) give

\[
                    \|\mu Q_E\|\le C2^{rN}.
 \tag{21}
\]

Let \(\mathsf Uw_a=w_{a+1}\), with the top arrow zero, and tensor
it with \(I_U\). F's block recursion is exactly the linear solver

\[
 \mathcal X_E=\sum_{s=0}^{d-1}
       \mathsf U^s\widehat Q_E(\mathsf U^*)^{s+1},
 \qquad \mathcal W_E=\mathcal U_E\mathcal X_E\mathcal U_E^{-1}.
 \tag{22}
\]

Indeed its \(ij\) block is
\(\sum_{s=0}^{\min(i,j-1)}(\widehat Q_E)_{i-s,j-1-s}\),
including zero when \(j=0\). This is precisely F(14e).
The fixed \(\mathsf U^*\) is the Euclidean adjoint of the constant
shift; it introduces no antiholomorphic meridian dependence.
Since both shifts are contractions,

\[
                  \|\mathcal X_E\|\le d\|\widehat Q_E\|.
 \tag{23}
\]

F proves the missing last-column identities and
\(Q_E=[\mathcal W_E,E_\Sigma]\); the solver here retains that
same full capped matrix. From (15)--(18),

\[
 \|\mathcal U_E\|\|\mathcal U_E^{-1}\|
       \le C N^{2p_0}2^{(2r+3/2)N}.
 \tag{24}
\]

The condition number occurs twice: once in forming
\(\widehat Q_E\), once in returning the solver. Thus (21)--(24)
give

\[
 \|\mu\mathcal W_E\|
 \le d(\|\mathcal U_E\|\|\mathcal U_E^{-1}\|)^2\|\mu Q_E\|
 \le C N^{4p_0+1}2^{(5r+3)N}.
 \tag{25}
\]

Since \(5r+3=5m-2\), this proves (7). Every factor is the actual
finite matrix; in particular the bound does not introduce an
\(N^{cN}\) loss.

## 4. Laurent coefficients and genuine meridian derivatives

Put \(F_N(u)=(u/N)\mathcal W_E(e^{u/N})\). It is holomorphic on
(6). Buffered Cauchy estimates applied to (7) show, for every fixed
\(k\ge0\),

\[
 \sup_{|N\mu|\le\eta}
   \|\partial_\mu^k[\mu\mathcal W_E(e^\mu)]\|
       \le C_k N^{p+k}\Lambda_m^N.
 \tag{26}
\]

In particular, with Taylor coefficients in the coordinate \(\mu\),

\[
 \mathcal W_E(e^\mu)=\mu^{-1}W_{-1}+W_0+\mu W_1+\cdots,
 \qquad
 \|W_j\|\le C_jN^{p+j+1}\Lambda_m^N\quad(j\ge-1).
 \tag{27}
\]

The residue, finite part, and first regular coefficient have costs
\(1,N,N^2\), respectively, apart from the common polynomial in (7).
These are true fixed-\(q\) meridian derivatives of the literal
changes of basis and pivot. They are not derivatives of a root-only
symbol or of an ordinary-color interpolation.

For \(Y(\mu)=[E_\Sigma(e^\mu),A(e^\mu)]\), write
\(Y=Y_0+\mu Y_1+\mu^2Y_2+\cdots\). Then, exactly,

\[
 \begin{split}
 \operatorname{Res}\operatorname{Tr}(\mathcal W_EY)
       &=\operatorname{Tr}(W_{-1}Y_0),\\
 \operatorname{FP}\operatorname{Tr}(\mathcal W_EY)
       &=\operatorname{Tr}(W_{-1}Y_1+W_0Y_0),\\
 [\mu^1]\operatorname{Tr}(\mathcal W_EY)
       &=\operatorname{Tr}(W_{-1}Y_2+W_0Y_1+W_1Y_0).
 \end{split}\tag{28}
\]

Thus \(Y_1=[E_{\Sigma,1},A_0]+[E_{\Sigma,0},A_1]\);
the first regular scalar coefficient can additionally require the
second marked jet. Separate residues in (5) have not been set to
zero. With an external line \(\Xi=\Xi_0+\mu\Xi_1+\cdots\), the
finite part in (28) acquires
\(\Xi_1\operatorname{Tr}(W_{-1}Y_0)\), as well as multiplication
of its displayed finite part by \(\Xi_0\).

## 5. A quantitative scalar error estimate, in the proved norms

Let \(Y_N(\mu)\) be any analytic current on the larger disk (6),
and suppose its Euclidean operator norm there is at most \(a_N\).
The trace inequality in dimension \(N^m\), followed by the same
buffered Cauchy estimate, gives

\[
 \left|[\mu^j]\operatorname{Tr}(\mathcal W_EY_N)\right|
       \le C_j N^{p+m+j+1}\Lambda_m^N a_N,
                         \qquad j\ge-1\text{ fixed}.
 \tag{29}
\]

If \(a_N\) instead bounds the trace norm of \(Y_N\), the factor
\(N^m\) is omitted. Consequently a bound

\[
 \sup_{|N\mu|\le\eta'}\|Y_N(\mu)\|
       \le N^b\exp[-((5m-2)\log2+\delta)N],\qquad\delta>0,
 \tag{30}
\]

implies that every fixed coefficient in (29), including the finite
part required by (5), is \(O(N^{p+m+b+j+1}e^{-\delta N})\).
An explicitly retained analytic external line is incorporated in
\(a_N\), or bounded separately before using (29).

For an actual finite word \(A=A_L\cdots A_1\), its current is the
exact finite sum

\[
 [E_\Sigma,A]=\sum_{\ell=1}^L
 A_L\cdots A_{\ell+1}[E_\Sigma,A_\ell]A_{\ell-1}\cdots A_1.
 \tag{31}
\]

Actual signed crossings intertwine the corresponding ordered total
arrows; marked factors keep their own terms. Equation (29) applies
to any proved operator- or trace-norm bound for this literal sum or
its summands. A normalized coherent-kernel estimate only on a local
domain is not such a bound. It cannot be substituted into (29)
without a separate, controlled contraction or norm adapter.

The co-source cost is fixed by the number of heads, whereas the
current may depend on all crossings, marks, and extensive spectator
occupations. Nothing here bounds an arbitrary current, proves a
geometric window is transported, or supplies an original source
lower bound. The new conclusion is the explicit bound on the actual
grouped co-source and all the Laurent data needed to use its exact
source identity quantitatively.

## Complete proof directs

* F: notes/research_forced_source_and_opposite_kernel_transport.md,
  SHA256 2e92bab4e3c510519098e3a10ed4227a8f4b492393b3742d02e4fdcaa3cca0f5.
* M: notes/research_actual_meridian_source_frames.md,
  SHA256 6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.

Both complete directs were freshly read nontruncated in this active
author sequence. All used implications, endpoint rows, and scalar
orders were checked. Only written mathematics and text/hash
operations were used; no frozen or public file was edited.
