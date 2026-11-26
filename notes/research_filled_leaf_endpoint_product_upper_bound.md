# The terminal upper budget for a literal filled-leaf endpoint product

Private written proof, 16 November 2026.

The actual leaf message is \(T(R^nB)\): multiply the endpoint
coupons and the original crossing inside the leaf trace, then
apply its original turn. For every fixed microscopic endpoint
product this message has upper rate \(\mathcal I_n\).
Its initial values and first normals are polynomially bounded.
The conjugated module supplies the whole-interval estimate.

This retains the literal source placement. It does not identify
the message with another endpoint product or compare its upper
rate with the action of an arbitrary parent.

## 1. Source and result

Use the original conventions
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad s=q-q^{-1},
 \quad c_j=2\cos((2j+1)\pi/N),\quad c_0=q+q^{-1},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\qquad
 S_j=\prod_{h=1}^j2\sin(h\pi/N),\quad S_0=1,
\]
\[
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\qquad
 Te_j=e_{D-j},\qquad \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{1}
\]
The notation \(T_N\) denotes Chebyshev's polynomial; \(T\)
is the original turn. Retain the original crossing \(R\) and
\[
 C f=Zf\pmod{P_N},\quad J=TCT,\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n},
 \qquad \kappa=q^{D^2/2}.
 \tag{2}
\]
The real norm is the ordinary supremum on \([-2,2]\) of the
canonical representative.

Fix an integer \(n\), an integer \(r\ge0\) of endpoint factors,
and \(A<\infty\). For bounded complex parameters put
\[
 w_i=2\cosh(\alpha_i/N),\quad |\alpha_i|\le A,\qquad
 B_N=\operatorname{can}\prod_{i=1}^{r}K_N(w_i,Z),\qquad
                         F_N=T(R^nB_N).
 \tag{3}
\]
The empty product is one. In particular the literal source is
\[
 F_N(Z)=\phi_W\!\left[
             K_N(Z,W)R^n(W)\prod_{i=1}^{r}K_N(w_i,W)\right].
 \tag{4}
\]
All products and product-rule normals are inside the same
original trace. The \(w_i\) and the output \(Z\) are ordinary
parameters in this polynomial identity.

Let \(L_n(u)\) be the terminal maximal logarithmic modulus
in the pinned product theorem, and
\[
             \mathcal I_n=\int_0^{1/2}L_n(u)\,du,\qquad
             \mathcal I_0=0.
 \tag{5}
\]
For \(n\ne0\), \(L_n\ge0\) is integrable. The signed physical
operators have conjugate coefficients on real rows, so
\(L_{-n}=L_n\). Also \(\mathcal I_1=\mathcal I_{-1}=0\).

**Theorem.** Uniformly on every fixed bounded complex parameter
polydisk,
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N
       \log\left(1+\sup_{|\boldsymbol\alpha|\le A}
                             \|F_N\|_{\mathbb R}\right)
                             \le\mathcal I_n .
 \quad}
 \tag{6}
\]
The same upper rate holds after any fixed spectral or parameter
derivatives, including all original physical first normals.
For \(n=0,\pm1\) the bound is subexponential. No lower coefficient
or equality of rates is asserted.

For \(r\ge1,n\ne0\), the proof gives, for every sufficiently small
fixed \(\epsilon>0\),
\[
 \begin{split}
 1+\sup_{|\boldsymbol\alpha|\le A}\|F_N\|_{\mathbb R}
 \le C_\epsilon N^{p_\epsilon}\exp\!\bigg\{
 &N\int_\epsilon^{1/2-\epsilon}L_n(u)\,du\\
 &+C_{n,r,A}N\epsilon\log(e/\epsilon)
   +C_\epsilon N^{1-1/(66r)}\bigg\}.
 \end{split}
 \tag{7}
\]
The endpoint constant is independent of \(\epsilon\).

## 2. Exact conjugation and polynomial source initialization

Assume first \(r\ge1\). Put \(k=33r\). For all sufficiently large
\(N\), the exact product module provides \(6^r\) ordinary gauged channels \(\mathcal W_N\),
scalar polynomial \(d\), and polynomial matrix \(E\), with
\[
 \{d(C)(J-c_0)I-s^2E(C)\}
                            \operatorname{can}\mathcal W_N=0,
 \quad \deg d=k,\quad \deg E_{ab}\le k,\quad
                         d(Z)\longrightarrow(Z-2)^k.
 \tag{8}
\]
The coefficients have bounded analytic expansions in \(N^{-1}\)
on bounded parameter sets; the leading coefficient \(d_k\)
tends to one. The product channel has gauge exponent \(r\).
Every canonical input channel, and \(B_N\), has polynomial
real norm. These are the full channels, including the original
source aliases, not a homogeneous truncation.

Set \(\mathcal A_n=T R^n\), with inverse \(R^{-n}T\).
The exact conjugations are
\[
 \mathcal A_n C\mathcal A_n^{-1}=J,\qquad
 \mathcal A_n J\mathcal A_n^{-1}
   =T R^nT\,C\,T R^{-n}T=D_{-n}.
 \tag{9}
\]
The two \(\kappa\) factors in the last equality cancel.
Thus, for
\(\mathcal F_N=T(R^n\operatorname{can}\mathcal W_N)\),
\[
 \boxed{\quad
 \{d(J)(D_{-n}-c_0)I-s^2E(J)\}\mathcal F_N=0,\qquad
                         (J-2)^rF_N=\mathcal F_{N,*}.
 \quad}
 \tag{10}
\]
The operator order in (10) is retained. Recovery is forced;
no inverse of \(J-2\) is taken.

For fixed rows write
\[
 f_j(W)=K_N(c_j,W),\qquad
 q_j(W)=\partial_ZK_N(c_j,W).
 \tag{11}
\]
Here the derivative is in the first kernel variable.
The whole-terminal source proves polynomial real norms for
both \(f_j,q_j\), uniformly over any fixed finite set of rows.
For every canonical input channel \(p_N\) one has exactly
\[
 \begin{split}
 (T(R^np_N))(c_j)&=\phi_N(f_jR^np_N),\\
 (T(R^np_N))'(c_j)&=\phi_N(q_jR^np_N).
 \end{split}
 \tag{12}
\]
The original crossing has physical values of modulus one and
angular first derivatives of size at most \(|n|N/2\).
Markov bounds the angular derivatives of \(f_j,q_j,p_N\).
Full-Hermite reconstruction of the product data, followed by
the coherent trace estimate, therefore bounds (12) polynomially.
This proves polynomial initial data simultaneously for
\(\mathcal F_N,F_N\), including their scaled angular normals.
No terminal exponential budget is spent at these initial rows.

## 3. The signed extreme coefficients and the full normal system

Write \(n=\sigma m\ne0\), \(m=|n|\), and set \(M=k+m\).
Use the original physical coefficient functions
\[
 A(j)=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 B(j)=\frac{s_j^4}{s_{2j}s_{2j+1}},\qquad
 s_x=2\sin(\pi x/N).
 \tag{13}
\]
In this convention the extremes of \(J\) are \(-A(j),-B(j)\).
The forward and backward extremes of \(D_{-n}\) are
\[
 q^{\sigma(2j+m+1)}\prod_{h=0}^{m-1}A(j+h),\qquad
 q^{-\sigma(2j-m+1)}\prod_{h=0}^{m-1}B(j-h).
 \tag{14}
\]
Multiplying the ordered \(J^kD_{-n}\) gives the extremes of
the first equation of (10):
\[
 \begin{split}
 a_+(j)&=d_k(-1)^k q^{\sigma(2j+2k+m+1)}
                         \prod_{h=0}^{M-1}A(j+h)\ I_{6^r},\\
 a_-(j)&=d_k(-1)^k q^{-\sigma(2j-2k-m+1)}
                         \prod_{h=0}^{M-1}B(j-h)\ I_{6^r}.
 \end{split}
 \tag{15}
\]
All lower powers of \(d\) have order at most \(M-1\), and the
entire correction \(s^2E(J)\) has order at most \(k<M\).
Thus it cannot change these scalar leading coefficients.
Recovery has order \(r\) in each direction and forward extreme
\[
                         (-1)^r\prod_{h=0}^{r-1}A(j+h).
 \tag{16}
\]

The normalized companions have dimensions \(2M\,6^r\) and \(2r\).
At center \(j\), their windows are
\[
 X_j^\mathcal F=(\mathcal F(c_{j-M}),\ldots,\mathcal F(c_{j+M-1})),
 \qquad X_j^F=(F(c_{j-r}),\ldots,F(c_{j+r-1})).
 \tag{17}
\]
Write the companions as \(\mathsf A_\mathcal F,\mathsf A_F\),
and let \(\mathsf B\) select the central component
\(\mathcal F_*(c_j)\) for recovery, divided by (16).
With derivative windows \(Z^\mathcal F,Z^F\), the exact system is
\[
 \begin{pmatrix}X^\mathcal F\\Z^\mathcal F\\X^F\\Z^F\end{pmatrix}_{j+1}
 =
 \begin{pmatrix}
 \mathsf A_\mathcal F&0&0&0\\
 \mathsf A_\mathcal F'&\mathsf A_\mathcal F&0&0\\
 \mathsf B&0&\mathsf A_F&0\\
 \mathsf B'&\mathsf B&\mathsf A_F'&\mathsf A_F
 \end{pmatrix}_{u=j/N}
 \begin{pmatrix}X^\mathcal F\\Z^\mathcal F\\X^F\\Z^F\end{pmatrix}_{j}.
 \tag{18}
\]
Primes mean derivatives in \(u\), where
\(c_N(u)=2\cos(2\pi u+\pi/N)\).
The ordinary residuals of (10) are \(P_N\) multiples, and
\[
                         P_N(c_N(u))=4\sin^2(\pi Nu).
 \tag{19}
\]
This gives the value and first derivative equations at every
regular grid row, with every coefficient derivative retained.
It is not an assertion of an off-grid homogeneous equation.

## 4. Compact propagation and the two endpoints

Let \(x=2\cos(2\pi u)\), and let \(y,x_{-n}\) be the physical
principal symbols of \(J,D_{-n}\). The principal equations are
\[
                         (y-2)^k(x_{-n}-2)I_{6^r},
                   \qquad (y-2)^r.
 \tag{20}
\]
Here
\[
                         y-2=-\tan^2(\pi u)t^{-1}(t-1)^2
 \tag{21}
\]
for the physical shift variable \(t\).
The terminal factor has \(m\) distinct nonzero roots, each
double, separated on every compact physical interval.
The root \(1\) is not terminal:
\(x_{-n}(u,1)=2+(-1)^n(x-2)\ne2\).
Thus the longest principal Jordan chain has length \(2k=66r\):
the unit root has that multiplicity, terminal roots have length
two, and recovery has a unit-root chain of length \(2r\).
The \(6^r\) repeated channels do not concatenate those chains.

Apply the explicit multiple-root estimate of the product theorem.
Scale a chain of length \(h\le66r\) by
\(\operatorname{diag}(1,\vartheta,\ldots,\vartheta^{h-1})\),
where \(\vartheta=N^{-1/(66r)}\), and give the four blocks
of (18) the additional grades \((1,N,N,N^2)\).
The finite diagonal-companion perturbations and every strict-grade
coupling are then \(O(\vartheta)\). This includes the actual
recovery forcing and the normal equations.
The maximal diagonal modulus is
\(\max(1,\max_\ell|\tau_{\ell,-n}(u)|)=e^{L_n(u)}\).
Consequently every compact forward prefix has upper bound
\[
 C_\epsilon N^{p_\epsilon}
 \exp\left\{N\int L_n(u)\,du+
                         C_\epsilon N^{1-1/(66r)}\right\}.
 \tag{22}
\]
The integral is over that prefix. The root statement gives an
upper estimate, not a selected coefficient.

Put \(J_N=\lfloor(N-1)/2\rfloor\). Start (18) at \(j=M\);
both windows use only fixed rows \(0,\ldots,2M-1\), so (12)
provides polynomial initial data. For
\[
 M\le j\le J_N-M,\qquad
 \delta_j=\min(j-M+1,J_N-M-j+1),
 \tag{23}
\]
all coefficient rows lie between \(j-M+1\) and \(j+M-1\),
hence in \(1,\ldots,J_N-1\). Each nonzero denominator sine
is at least \(c\,\delta_j/N\). The original estimates
\[
 |A|+|B|\le C(N/\delta_j)^2,\qquad
 |A^{-1}|\le C(N/\delta_j)^4
 \tag{24}
\]
and their scaled derivatives apply. The phases in (15) have
unit modulus on real rows and bounded scaled derivatives.
Since \(d_k\to1\) and all cleared coefficients are bounded,
the normalized matrix (18) has norm at most
\[
                              C_{n,r,A}(N/\delta_j)^b.
 \tag{25}
\]
No independent factor \(N^b\) is paid at every step.
The product across either strip of length
\(\epsilon N+O_{n,r}(1)\) is therefore at most
\[
 N^{O_{n,r,A}(1)}
                    \exp(C_{n,r,A}N\epsilon\log(e/\epsilon)).
 \tag{26}
\]
These constants are independent of \(\epsilon\).

The last joint center \(J_N-M\) generates \(\mathcal F\) at
row \(J_N\), but \(F\) only through row \(J_N-M+r\).
Continue the recovery value and normal equations alone for
\[
                         J_N-M+1\le j\le J_N-r.
 \tag{27}
\]
There are \(M-r\) such steps, a fixed number. Their forcing
rows and normals are already available; their coefficients
cost polynomially by (24). The last output is the actual
row \(J_N\). No coefficient beyond \(J_N-1\) is evaluated.
The odd last node needs only its simple value and has zero
angular derivative; the even last node retains its first normal.

Combine (26), (22), (26), and (27). Since \(L_n\ge0\), the
same total bound controls all preceding rows and normals.
Stable full-Hermite reconstruction costs only a polynomial
and proves (7). Taking \(N\to\infty\) first, then
\(\epsilon\to0\), gives (6).

For \(n=0,r\ge1\), the first-turn initialization theorem gives
the result directly. For \(r=0\), \(F_N=T(R^n)=G_{-n}\),
so the whole-terminal theorem gives (6), including \(n=0\).
Finitely many small levels excluded by the physical windows
are absorbed by compactness in the finite parameter polynomials.
Uniformity on larger parameter polydisks and Cauchy's formula
give fixed parameter derivatives; Markov gives fixed spectral
derivatives.

## 5. Placement and direct sources

Equation (4) is the actual message of a filled leaf with these
endpoint decorations. It differs from the operator placement
\(V_nB_N=\kappa^nT(R^{-n}TB_N)\). The proof never replaces one
by the other. Its polynomial initialization uses the original
input channels before the first turn.

All free endpoint parameters remain ordinary throughout, and the
derivative assertion retains their fixed derivatives. The norm
estimate is on the stated real output interval and bounded
microscopic parameter sets. Shared endpoint products and all their
normals remain. This supplies neither a geometric parent pullback
nor a bound for subsequent multiplication by arbitrary received
turned messages. The required comparison with a fixed parent's
action, and general repeated branching, remain separate.

The following complete direct-source reads are retained at the
stated unchanged versions; used implications and hashes were checked:

* [Exact divided-difference module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  full source channels, polynomial gauges, bounded cleared
  coefficients and ordered recovery.
* [Turned product upper estimate](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a:
  original signed extreme coefficients, physical normal equations,
  separated terminal roots, multiple-root/grade estimate and
  full-interval reconstruction.
* [First-turn initialization](research_first_turn_endpoint_product_initialization.md),
  SHA256 7d0871a7dcde94c1cc73f98495b9521a61478729ddd52c51570ffa95f1901105:
  the \(n=0\) product bound with the actual forced source.
* [Whole-terminal source](research_whole_terminal_characteristic_upper_bound.md),
  SHA256 ee91f066e0e5b0eb60e4076ba2a2090e1439787c57caf6eaaa09341138d05176:
  fixed-row kernel and normal bounds, original crossing jets,
  coherent trace estimates, and the empty-product case.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.
