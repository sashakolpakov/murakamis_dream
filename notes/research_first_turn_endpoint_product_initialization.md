# Subexponential first turns and the terminal upper budget for endpoint products

Private written proof, 16 November 2026.

An original first turn of any fixed ordinary product of microscopic
endpoint kernels has subexponential real norm. The same estimate holds
simultaneously for the gauged channels of the exact product module.
Consequently the actual initial data for a subsequent signed twist
cost subexponentially, and the product upper budget improves from
\(2\mathcal I_n\) to \(\mathcal I_n\).

The proof keeps the original full quotient and first normals. It
does not identify a turned product with another endpoint product,
or close arbitrary repeated branching.

## 1. Original source and statement

Retain the original conventions
\[
 q=e^{\pi i/N},\quad s=q-q^{-1},\quad D=N-1,\quad
 c_j=2\cos((2j+1)\pi/N),\quad c_0=q+q^{-1},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\quad
 \mathcal A_N=\mathbb C[Z]/(P_N),\quad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z).
 \tag{1}
\]
Here \(T_N\) is Chebyshev's polynomial, while \(T e_j=e_{D-j}\)
is the original turn. The original basis and trace normalization are
\[
 S_j=\prod_{h=1}^{j}2\sin(h\pi/N),\quad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad S_0=1,\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
\]
Let
\[
 C f=Zf\pmod{P_N},\qquad J=TCT,\qquad
 V_n=\kappa^nTR^{-n}T,\qquad \kappa=q^{D^2/2}.
 \tag{2}
\]
Every norm below is the ordinary supremum norm on \([-2,2]\)
of the canonical representative. Exterior parameters are not
quotiented.

Fix \(r\ge1\) and \(A<\infty\), and put
\[
 w_i=2\cosh(\alpha_i/N),\quad |\alpha_i|\le A,\qquad
 B_N=\operatorname{can}\prod_{i=1}^{r}K_N(w_i,Z).
 \tag{3}
\]
Use the exact divided-difference module's \(6^r\) ordinary
gauged channels \(\mathcal W_N\). Each is a tensor product of
\[
 (f_i,\mathcal Df_i,\mathcal Sf_i,\mathcal S\mathcal Df_i,P_N,1),
 \qquad f_i=K_N(w_i,Z),
\]
multiplied by its specified power \((Z-2)^a\), \(0\le a\le2r\).
The product component has gauge exponent \(r\).
Define
\[
 \mathcal F_N=T\operatorname{can}\mathcal W_N,\qquad Y_N=TB_N,
 \qquad
 \Lambda_N=1+\sup_{|\boldsymbol\alpha|\le A}
       \left(\|Y_N\|_{\mathbb R}+\max_a\|\mathcal F_{N,a}\|_{\mathbb R}\right).
 \tag{4}
\]

**Theorem 1.** Uniformly on every fixed bounded complex parameter
polydisk,
\[
                         \limsup_{N\to\infty}N^{-1}\log\Lambda_N=0.
 \tag{5}
\]
More precisely, for every sufficiently small fixed \(\epsilon>0\),
\[
 \Lambda_N\le C_\epsilon N^{p_\epsilon}
 \exp\!\left\{
 C_{r,A}N\epsilon\log(e/\epsilon)
       +C_\epsilon N^{1-1/(66r)}
 \right\},
 \tag{6}
\]
where the endpoint constant \(C_{r,A}\) is independent of
\(\epsilon\). The same subexponential conclusion holds after
any fixed spectral or parameter derivatives.

For fixed \(n\ne0\), let \(L_n(u)\ge0\) and
\(\mathcal I_n=\int_0^{1/2}L_n(u)\,du\) be the terminal maximal
logarithmic modulus and its finite integral in the pinned
product theorem. Set \(\mathcal I_0=0\).

**Corollary 2.** For every fixed integer \(n\),
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N
 \log\left(1+\sup_{|\boldsymbol\alpha|\le A}
                      \|V_nB_N\|_{\mathbb R}\right)
                      \le\mathcal I_n .
 \quad}
 \tag{7}
\]
The assertion includes all fixed spectral and parameter derivatives.
For \(n=\pm1\), \(\mathcal I_n=0\). No lower coefficient or
equality of rates is asserted.

## 2. The exact first-turn system and its initial data

Put \(k=33r\). The product module supplies fixed-degree polynomial
matrices \(d,E\), with scalar \(d\), satisfying, for all sufficiently
large \(N\),
\[
 \{d(C)(J-c_0)I-s^2E(C)\}\operatorname{can}\mathcal W_N=0,
 \quad \deg d=k,\quad \deg E_{ab}\le k,
 \quad d(Z)\longrightarrow(Z-2)^k.
 \tag{8}
\]
Their coefficients have bounded analytic expansions in \(N^{-1}\)
on bounded complex parameter sets. In particular, writing
\[
 d(Z)=d_k Z^k+\cdots,\qquad E(Z)=E_k Z^k+\cdots,
\]
one has \(d_k\to1\) and \(\|E_k\|\le M_A\), uniformly.
These statements concern the displayed matrix presentation,
not a scalar elimination.

Conjugating (8) by the original \(T\), using \(T^2=1\), gives
the exact full-algebra equations
\[
 \boxed{\quad
 \{d(J)(C-c_0)I-s^2E(J)\}\mathcal F_N=0,\qquad
                         (J-2)^rY_N=\mathcal F_{N,*}.
 \quad}
 \tag{9}
\]
The order \(d(J)(C-c_0)\) is essential. The second equation is
forced recovery of the original product component; it is not
solved by inverting \(J-2\).

All unturned input channels in (4) have polynomial real norm.
Indeed the two half-shift arguments are real in \([-2,2]\), so
\(\|\mathcal Sf\|\le\|f\|\) and
\(\|\mathcal Df\|\le\|f'\|\). The full microscopic kernels have
polynomial real norm, and Markov controls each fixed derivative.
Fixed tensor products and polynomial gauges retain that bound.
Their ordinary degrees are \(O_r(N)\); canonical reduction retains
all physical jets and costs only a polynomial by full-Hermite
reconstruction. This is the input estimate proved in the product
upper-bound source.

For each fixed row \(j\), write
\[
 F_j(Z)=K_N(c_j,Z),\qquad Q_j(Z)=\partial_wK_N(c_j,Z).
 \tag{10}
\]
The whole-terminal source proves polynomial real bounds for both
\(F_j,Q_j\), uniformly over any fixed finite set of rows.
The exact reproducing formulas, with every normal retained, are
\[
 (Tp)(c_j)=\phi_N(F_jp),\qquad
 (Tp)'(c_j)=\phi_N(Q_jp).
 \tag{11}
\]
For canonical \(f,p\), the original full-normal product estimate is
\[
 |\phi_N(fp)|\le C N^5\|f\|_{\mathbb R}\|p\|_{\mathbb R}.
 \tag{12}
\]
Thus every fixed initial window of \(\mathcal F_N,Y_N\), including
its first spectral or scaled angular normals, is polynomially
bounded. No exponential terminal source is used in this initialization.

## 3. The forward leading matrix at the two endpoints

Use the scaled physical coordinate
\[
 c_N(u)=2\cos(2\pi u+\pi/N),\qquad J_N=\lfloor(N-1)/2\rfloor,
\]
and the original coefficients
\[
 A(j)=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 B(j)=\frac{s_j^4}{s_{2j}s_{2j+1}},\qquad
 s_x=2\sin(\pi x/N).
 \tag{13}
\]
The physical action of \(J\) has forward coefficient \(-A(j)\)
and backward coefficient \(-B(j)\). Consequently the exact
forward extreme of the first equation of (9) is
\[
 (-1)^k\prod_{h=0}^{k-1}A(j+h)\,\mathsf K_j,\qquad
 \mathsf K_j=d_k(c_{j+k}-c_0)I-s^2E_k.
 \tag{14}
\]
The correction \(E_k\) really occurs at this highest order.
It must not be dropped by a principal-symbol argument.
The backward formula has \(A(j+h)\) replaced by \(B(j-h)\)
and \(c_{j+k}\) by \(c_{j-k}\); no backward inverse is needed below.
The recovery forward extreme is
\[
                         (-1)^r\prod_{h=0}^{r-1}A(j+h).
 \tag{15}
\]

For both parities and \(1\le l\le J_N\),
\[
 |c_l-c_0|
   =4\sin(l\pi/N)\sin((l+1)\pi/N)\ge16l^2/N^2.
 \tag{16}
\]
Here \(\sin((l+1)\pi/N)\ge\sin(l\pi/N)\); equality is possible
at the odd last row. This is why a bound using \(l(l+1)\)
is not used at that endpoint.

For sufficiently large \(N\), \(|d_k|\ge1/2\) and
\(|s|^2\le4\pi^2/N^2\). Choose a fixed integer \(j_0\ge k\)
large enough that \((j_0+k)^2\ge\pi^2M_A+1\).
Then for \(j_0\le j\le J_N-k\),
\[
 \|s^2E_k\|\le\tfrac12|d_k(c_{j+k}-c_0)|,\qquad
 \|\mathsf K_j^{-1}\|
                     \le \frac{N^2}{4(j+k)^2}.
 \tag{17}
\]
A fixed enlargement of the constant covers any chosen matrix norm.
The inverse follows from a Neumann series around the scalar
leading matrix, uniformly for all complex parameters in (3).
The starting row is fixed independently of \(N\).

Normalize the first equation of (9) by (14) and the recovery
equation by (15). Their windows at center \(j\) have lengths
\(2k\,6^r\) and \(2r\), respectively:
\[
 X_j^F=(\mathcal F(c_{j-k}),\ldots,\mathcal F(c_{j+k-1})),
 \qquad X_j^Y=(Y(c_{j-r}),\ldots,Y(c_{j+r-1})).
 \tag{18}
\]
Starting at \(j_0\), both windows involve only fixed rows, so (11)
initializes them polynomially. Let \(\mathsf A_F,\mathsf A_Y\)
be the normalized companions and \(\mathsf B\) the recovery
selector of the central value \(\mathcal F_*(c_j)\).
Including the scaled derivative windows gives exactly
\[
 \begin{pmatrix}X^F\\Z^F\\X^Y\\Z^Y\end{pmatrix}_{j+1}
 =
 \begin{pmatrix}
 \mathsf A_F&0&0&0\\
 \mathsf A_F'&\mathsf A_F&0&0\\
 \mathsf B&0&\mathsf A_Y&0\\
 \mathsf B'&\mathsf B&\mathsf A_Y'&\mathsf A_Y
 \end{pmatrix}_{u=j/N}
 \begin{pmatrix}X^F\\Z^F\\X^Y\\Z^Y\end{pmatrix}_{j}.
 \tag{19}
\]
These are equations for the actual full jets, not derivatives of
an off-grid homogeneous relation. The ordinary residuals of (9)
are \(P_N\) multiples and
\[
                         P_N(c_N(u))=4\sin^2(\pi Nu).
 \tag{20}
\]
Their values and first \(u\)-derivatives therefore vanish at
the grid. All coefficient derivatives in (19) remain.

## 4. Compact transfer and whole-interval recovery

On a buffered compact interval in \(0<u<1/2\), write
\(x=2\cos(2\pi u)\), and let \(t\) be the physical shift symbol.
The limiting symbol of \(J\) satisfies
\[
 y-2=-\tan^2(\pi u)t^{-1}(t-1)^2.
 \tag{21}
\]
Thus the first principal equation in (9) is
\[
                         (y-2)^k(x-2)I_{6^r},
 \tag{22}
\]
and recovery has symbol \((y-2)^r\).
The scalar \(x-2\) is nonzero in the compact interval.
After normalizing the leading coefficients, the first companion
is a direct sum of \(6^r\) scalar companions with the single
root \(1\), of multiplicity \(2k=66r\). Recovery has the same
root with multiplicity \(2r\). Channel repetition does not
concatenate the Jordan chains.

Use confluent Vandermonde frames and scale a chain of length
\(h\le2k\) by
\[
 \operatorname{diag}(1,\vartheta,\ldots,\vartheta^{h-1}),
 \qquad \vartheta=N^{-1/(2k)}.
 \tag{23}
\]
The normalized finite companions differ from their principal
ones by \(O(N^{-1})\), with fixed derivatives. Conjugating these
errors costs at most
\(N^{-1}\vartheta^{-(2k-1)}=\vartheta\).
The principal normalized scalar companions here are constant;
allowing bounded smooth frames would give the same estimate.
Give the four blocks of (19) the additional grades
\[
                              (1,N,N,N^2).
 \tag{24}
\]
Every strict-grade coupling is then \(O(\vartheta)\), including
the actual recovery forcing and both derivative couplings.
The entire one-step norm is at most \(1+C_\epsilon\vartheta\).
The endpoint frame changes cost polynomially. Hence every
compact forward prefix has bound
\[
                  C_\epsilon N^{p_\epsilon}
                         \exp(C_\epsilon N^{1-1/(2k)}).
 \tag{25}
\]
This is the same matrix estimate as in the product upper theorem,
with all diagonal characteristic moduli equal to one.

For \(j_0\le j\le J_N-k\), put
\[
                         d_j=\min(j-k+1,J_N-k-j+1).
 \tag{26}
\]
Every coefficient row in the first equation of (9) lies between
\(j-k+1\) and \(j+k-1\). The relevant nonzero denominator sines
are at least \(c\,d_j/N\). The usual bounds
\[
 |A|+|B|\le C(N/d_j)^2,\qquad |A^{-1}|\le C(N/d_j)^4
\]
and their scaled first derivatives therefore apply.
The extra leading inverse (17) costs at most \(C(N/d_j)^2\).
Its derivative follows from differentiating the inverse and
costs only further powers of \(N/d_j\).
The cleared coefficients of \(d,E\) are uniformly bounded.
Thus the entire matrix (19) is bounded by
\[
                              C_{r,A}(N/d_j)^b.
 \tag{27}
\]
There is no standalone \(N^b\) cost per row.

On each endpoint strip of length \(K=\epsilon N+O_{r,A}(1)\),
the product of (27) is at most
\[
 C^K\prod_{a=1}^{K+O_{r,A}(1)}(N/a)^b
 \le N^{O_{r,A}(1)}
                 \exp(C_{r,A}N\epsilon\log(e/\epsilon)).
 \tag{28}
\]
A fixed initial offset only changes the polynomial factor.
All rows below the initial window are already bounded by (11).

The last joint center \(J_N-k\) produces the last \(\mathcal F\)
row \(J_N\), but produces \(Y\) only through \(J_N-k+r\).
Continue only recovery and its normal equation for
\[
                         J_N-k+1\le j\le J_N-r.
 \tag{29}
\]
There are \(k-r\) such steps, a fixed number. All required
\(\mathcal F_*(c_j)\) and its angular normals have already been
computed. These additional steps cost polynomially by the same
sine bounds and end at the actual last \(Y\) row.
No coefficient beyond \(J_N-1\) is evaluated.
At odd levels the last node is simple and only its value is
required; its angular derivative is zero. At even levels the
last spectral first normal is retained.

The stable full-Hermite reconstruction bounds each canonical
output by
\[
 (2N-1)\max_{\rm physical}|f|
        +2\max_{\rm angular}|\partial_t f(-2\cos t)|.
 \tag{30}
\]
Apply (28), (25), (28), and then (29), starting with (11).
This proves (6) simultaneously for every \(\mathcal F\) channel
and \(Y\). Take \(N\to\infty\) first and then \(\epsilon\to0\)
to prove (5). Uniformity on larger parameter disks and Cauchy's
formula give fixed parameter derivatives; Markov gives fixed
spectral derivatives. Any finitely many excluded levels are absorbed
in the constants of (6), using their exact finite polynomials on
the compact parameter set.

## 5. Actual signed initialization and the single terminal budget

Let \(p_N\) be any of the canonical input channels
\(\operatorname{can}\mathcal W_N\), or \(B_N\). Theorem 1 says
\(\|Tp_N\|_{\mathbb R}\le\Lambda_N\), uniformly.
For every fixed row the exact source formulas are now
\[
 \begin{split}
 (V_np_N)(c_j)
   &=\kappa^n\phi_N(R^{-n}(Tp_N)F_j),\\
 (V_np_N)'(c_j)
   &=\kappa^n\phi_N(R^{-n}(Tp_N)Q_j).
 \end{split}
 \tag{31}
\]
No turn is moved through an ordinary product in this identity.
The original physical values of \(R^{-n}\) have modulus one;
their angular first derivatives are at most \(|n|N/2\).
Together with the polynomial fixed-row bounds for \(F_j,Q_j\),
Markov, full-Hermite reconstruction, and the trace bound, this gives
\[
 |(V_np_N)(c_j)|+|(V_np_N)'(c_j)|
                              \le C_{j,n}N^{b_{j,n}}\Lambda_N.
 \tag{32}
\]
All product-rule normals are inside the trace.
Thus every fixed window of the actual gauged and recovery system
for \(V_nB_N\) has subexponential initialization.

For \(n\ne0\), repeat the regular propagation proof of the pinned
product upper theorem, now with (32). Its exact equations are
\[
 \{d(D_n)(J-c_0)I-s^2E(D_n)\}V_n\operatorname{can}\mathcal W_N=0,
 \qquad (D_n-2)^r V_nB_N
                         =(V_n\operatorname{can}\mathcal W_N)_*.
 \tag{33}
\]
Their signed extremes, unequal recurrence windows, normal system,
endpoint bounds and final recovery remain exactly those already
proved. Only the bound on their actual initial vectors changes.
Consequently, for fixed \(\epsilon>0\),
\[
 \begin{split}
 1+\sup_{|\boldsymbol\alpha|\le A}\|V_nB_N\|_{\mathbb R}
 \le{}&C_\epsilon N^{p_\epsilon}\Lambda_N\\
 &\times\exp\!\left\{
 N\int_\epsilon^{1/2-\epsilon}L_n(u)\,du
 +C_{n,r,A}N\epsilon\log(e/\epsilon)
 +C_\epsilon N^{1-1/(66r)}
 \right\}.
 \end{split}
 \tag{34}
\]
Use (5), take the upper limit in \(N\), and then let
\(\epsilon\to0\). Integrability of \(L_n\) proves (7).
For \(n=0\), the original polynomial input estimate suffices.
The derivative assertions follow as in Theorem 1.

The removed initialization budget was an upper estimate for
arbitrary polynomially bounded inputs. Its removal here uses the
actual microscopic endpoint product and every gauged source channel
through (9). This is not a norm bound for \(T\) on arbitrary inputs.
Nor does it apply without further work to products already containing
received turned factors. No initial direction or quotient residual
has been discarded to obtain (7).

## 6. Direct sources and scope

The following complete direct sources were read at their unchanged
versions, with the used implications and hashes checked:

* [Exact divided-difference module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  ordinary channel construction, full source and aliases, polynomial
  gauge, bounded coefficients, ordered conjugation and forced recovery.
* [Turned product upper bound](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a:
  polynomial input bounds, exact physical companions, multiple-root
  and grade scaling, endpoint estimates, unequal recovery windows,
  original full-normal reconstruction and characteristic integral.
* [Whole-terminal source and initialization](research_whole_terminal_characteristic_upper_bound.md),
  SHA256 ee91f066e0e5b0eb60e4076ba2a2090e1439787c57caf6eaaa09341138d05176:
  fixed-row \(F_j,Q_j\) bounds, reproducing trace identities,
  original crossing jets and coherent full-Hermite product bounds.

The new input is the regular first-turn system (9), including its
highest-order matrix correction and fixed-start domination.
It supplies an actual source estimate and improves the upper budget;
it supplies no selected coefficient, filled-action comparison, or
general repeated-branching theorem.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.
