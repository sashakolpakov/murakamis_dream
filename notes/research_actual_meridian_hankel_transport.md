# Actual meridian jets on fixed cyclic-dilogarithm Hankel banks

Private written proof, 19 November 2026.

The exact moving diagonal frames of F extend the root estimates of W
and H to a complex scaled meridian collar. The result concerns the
literal highest-cut pivotal source, with its external scalar displayed.
The new conclusion is uniform radial-tail control for that family and
every fixed true meridian jet. The root banks do not move. W already
supplies an exact meridian period; no whole-meridian Euler/Gaussian
factorization is used below.

## 1. Source, scalar, and exact moving frames

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and a
signed braid word \(\beta\) on \(m\) heads with \(c\) crossings and
writhe \(w\). Put \(r=m-1\), \(M=e^\mu\), \(x=-M/q\), and

\[
 \mathcal P_N(M)=\Xi_N(M)\operatorname{Tr}
   [(P_0\otimes K_{\rm r}(M)^{1-N})W_\beta(M)].                 \tag{1}
\]

Here \(P_0=|0\rangle\langle0|\), both the first input and output
are zero, and \(\Xi_N\) is the prescribed external dimension,
framing, and peripheral line. Every crossing in \(W_\beta\)
includes its actual scalar \(\kappa(M)^{\pm1}\).
We remove precisely that scalar and write
\(\mathcal E_N(M)=\Xi_N(M)\kappa(M)^w\),
\(\mathcal P_N=\mathcal E_N\widehat{\mathcal P}_N\).
This defines the hatted source directly from stripped matrices,
even at a zero or pole of the external line.

Let \(J_iw_a=aw_a\), \(f_a=(Q;Q)_a\), and
\[
 h_a(M)=M^{-a}\frac{f_a}{(M^{-2}Q;Q)_a},\qquad
 D_h(M)=\operatorname{diag}(h_a(M)).                           \tag{2}
\]
Put \(\widehat R_{i,0}^{\pm}=\kappa(1)^{\mp1}R_i^{\pm}(1)\).
F(32), with the actual checked flip and inverse order, gives
\[
\begin{split}
 \kappa(M)^{-1}R_i^+(M)
 &=M^{-J_i-J_{i+1}}D_{h,i+1}(M)
              \widehat R_{i,0}^+D_{h,i}(M)^{-1},\\
 \kappa(M)R_i^-(M)
 &=M^{J_i+J_{i+1}}D_{h,i}(M)
              \widehat R_{i,0}^-D_{h,i+1}(M)^{-1}.
\end{split}                                                   \tag{3}
\]
We insert these factors at their original stages, without cancelling
or commuting adjacent frames. All crossing scalars are counted once
in \(\mathcal E_N\); in particular no extra \(\kappa(1)^w\) remains.

For \(0<\eta'<\pi\), \(M=e^{u/N}\), \(|u|\le\eta'\), F(24)--(25)
prove, uniformly over the complete occupation range,
\[
 \|D_h^{\pm1}\|\le(N+1)^{C_{\eta'}},\qquad
 \|M^{\pm(J_i+J_{i+1})}\|\le e^{2\eta'}.                     \tag{4}
\]
These diagonal bounds hold in the ordinary Euclidean head norm as
well as F's binomial norm: both norms are the maximum of the diagonal
entries. The proof uses the zero-free sine factors
\(1-e^{-2u/N}Q^j\), \(1\le j<N\), and integration of
\(|\partial_u\log h_a|\le C_{\eta'}\log(N+1)\).
Thus both frames and inverses are holomorphic on this collar.
The actual coupon has trace norm exactly
\[
 \|P_0\otimes K_{\rm r}(M)^{1-N}\|_1
       =N^r|M|^{-rd}\le e^{r\eta'}N^r.                       \tag{5}
\]
This is not W's summed-output first-input-zero coupon. No equality
between those coupons after resolvent insertion is asserted.

## 2. Only the root factors are replaced by contour kernels

Write \(u_N(t)=\sum_{a<N}t^a/f_a\) and
\(v_N(t)=\sum_{a<N}(-1)^aQ^{a(a-1)/2}t^a/f_a\).
Use W's strict root factorization with \(x_0=-q^{-1}\):
\[
 C=F_2u_N(T_-)F_1F_2^{-1},\quad
 C^{-1}=F_2F_1^{-1}v_N(T_-)F_2^{-1},\quad
 \widehat R_0^+=CDu_N(T_+)C^{-1},\quad
 \widehat R_0^-=Cv_N(T_+)D^{-1}C^{-1}.                        \tag{6}
\]
Here \(F_i=\operatorname{diag}(f_a)\),
\(T_\pm=x_0^{-1}S_1^\pm S_2^\mp\) are the literal truncated
unit shifts, and
\(D_{a,k}=(-1)^kQ^{k(k-1)/2}x_0^{-2k}\).
In particular \(T_\pm^N=0\), \(\|T_\pm\|\le1\), and \(D\) is unitary.
The conventions in (6) match F(31): the same head has
\(Fw_a=(1-Q^{a+1})w_{a+1}\), \(Kw_a=x_0Q^{-a}w_a\), and
\(R^+(1)w_{0,b}=\kappa(1)x_0^{-b}w_{b,0}\).
For example the fusion coefficient of (6) from \((a,k)\) to
\((a-h,k+h)\) is \(x_0^{-h}f_af_{k+h}/(f_hf_k)\), exactly its
physical fusion coefficient; both negatives are the matrix inverse.
Thus (6) replaces the root matrices in (3), including their scalar
convention, and makes no assertion about (6) at \(M\ne1\).

For \(\epsilon=\pm1\) let
\[
 A_\epsilon(t)=\prod_{j=1}^{N-1}(1-Q^{\epsilon j}t)^{-j/N},
       \qquad A_\epsilon(0)=1.                              \tag{7}
\]
W's all-inverse realization uses three transfer slots and six
factorial slots per crossing. A \(v_Q(T)\) slot uses
\(A_+(t)(tI-T)^{-1}\); a \(u_Q(T)\) slot uses
\(A_-(t)(tI-Q^{-1}T)^{-1}\). The inverse and direct factorial
slots respectively use
\[
 A_-(t)\operatorname{diag}_a(Q^{-a}t^{-a-1}),\qquad
 A_+(t)\operatorname{diag}_a(NQ^{-a-1}t^{a-N}).                \tag{8}
\]
Every slot is integrated with \(dt/(2\pi i)\) on its marked small
circle. Its matrix Laurent orders are precisely among \(-1,\ldots,-N\).
These identities are finite coefficient identities; all caps survive.
There are \(s=9c\) slots. Keep the moving factors (3), the coupon
(1), and their original order around these slots.

For each slot orientation \(\epsilon\) and \(1\le j<N\), set
\[
 H_{\epsilon,j}(\rho)=(\rho-1)^{-j/N}
       \prod_{k\ne j}(1-\rho Q^{\epsilon(k-j)})^{-k/N},
                      \qquad 1<\rho<\infty.                 \tag{9}
\]
The nonendpoint logarithms continue radially from zero; the first
power is positive real. H's oriented jump is
\(2i\sin(\pi j/N)H_{\epsilon,j}\). A Laurent matrix kernel
\(\sum_{a=0}^{d}B_at^{-a-1}\) becomes
\(\sum_aB_aQ^{\epsilon ja}\rho^{-a-1}\).
Let \(\mathcal R_N(\boldsymbol\rho,\boldsymbol j;u)\) be the
literal pointed trace of that ordered cut network with (3).
Then exactly
\[
 \widehat{\mathcal P}_N(e^{u/N})
 =\sum_{\boldsymbol j\in\{1,\ldots,N-1\}^{s}}
   \int_{[1,\infty)^s}\mathcal R_N(\boldsymbol\rho,\boldsymbol j;u)
   \prod_{\ell=1}^{s}
       \frac{\sin(\pi j_\ell/N)}{\pi}
       H_{\epsilon_\ell,j_\ell}(\rho_\ell)\,d\rho_\ell.       \tag{10}
\]
The identity follows at the matrix level before applying the chosen
linear functional. Every bank, sheet mark, and curve is independent
of \(u\). At finite endpoints the exponents \(-j/N>-1\) are
integrable; at infinity \(A_\epsilon=O(|t|^{-(N-1)/2})\) and every
matrix kernel is \(O(t^{-1})\). H's cut-arc proof therefore applies
also at even and composite levels, without assuming a closed lift
of a large base circle. Moving diagonals introduce no new \(t\)-poles.

## 3. Uniform absolute tails and true meridian derivatives

On every bank, a transfer resolvent has norm at most \(N/\rho\),
a direct factorial kernel at most \(N/\rho\), and an inverse
factorial kernel at most \(1/\rho\). Equations (4)--(5) give constants
\(C,B\), depending only on the fixed word and \(\eta'\), such that
\[
 |\mathcal R_N(\boldsymbol\rho,\boldsymbol j;u)|
       \le C(N+1)^B\prod_\ell\rho_\ell^{-1}.                \tag{11}
\]
For instance \(B=r+6c+2cC_{\eta'}\) suffices after changing \(C\).
No exponentially conditioned factorial remains in this rational
source. No norm of a prefix quotient or a reduced axis trace is used.

Put \(G_j=|f_j|/N^{j/N+1/2}\) and
\(c_N=(N-1)(N-2)/(4N)\). H proves
\[
 |H_{\epsilon,j}(\rho)|\le
 G_j(\rho-1)^{-j/N}\rho^{-C_j},\quad
 C_j=(N-1)/4-j/(2N)\ge c_N,
 \quad\frac{\sin(\pi j/N)}\pi
       \int_1^\infty(\rho-1)^{-j/N}\frac{d\rho}{\rho}=1.    \tag{12}
\]
Let \(\widehat{\mathcal P}_{N,\mathrm{tail}}(R,u)\) denote (10)
restricted to \(\max\rho_\ell\ge R\), \(R\ge1\). Absolute
integration and the union bound now prove, uniformly on \(|u|\le\eta'\),
\[
 |\widehat{\mathcal P}_{N,\mathrm{tail}}(R,u)|
 \le C(N+1)^B sR^{-c_N}\Big(\sum_{j=1}^{N-1}G_j\Big)^s.     \tag{13}
\]
The same bound without \(sR^{-c_N}\) controls the full absolute
integral. This integrable envelope also proves holomorphy under the
integral. For \(0<\eta<\eta'\), Cauchy's formula in \(u=N\mu\) gives
\[
 \sup_{|u|\le\eta}
 |\partial_\mu^k\widehat{\mathcal P}_{N,\mathrm{tail}}(R,u)|
 \le\frac{k!N^k}{(\eta'-\eta)^k}
 C(N+1)^B sR^{-c_N}\Big(\sum_jG_j\Big)^s                    \tag{14}
\]
for every fixed \(k\ge0\), and the analogous full-integral bound.
Here \(\partial_\mu=N\partial_u\) differentiates the actual
fixed-\(q\) family, including its pivot and all moving frames.
The derivative is not a derivative of a root-only symbol.

H's uniform factorial estimate is
\(\log G_j=N\int_0^{j/N}\log(2\sin\pi t)dt+O(\log N)\),
whose maximal rate is \(v_3/(2\pi)\), with \(v_3\) the regular ideal
tetrahedron volume. Thus for fixed \(R>1\)
and fixed \(k\), (14) yields
\[
 \limsup_{N\to\infty}\frac1N\log
 \sup_{|u|\le\eta}|\partial_\mu^k
             \widehat{\mathcal P}_{N,\mathrm{tail}}(R,u)|
       \le\frac{9cv_3}{2\pi}-\frac14\log R.                 \tag{15}
\]
For \(c=0\) the integral is empty and the radial tail is zero.
For \(N=2\), \(c_N=0\) in the exact bound; decay in (15) is a
large-level conclusion. No restriction on parity or compositeness
was used.

## 4. Restoring the original line and the scope of the estimate

For the standard zero-framed raw source, R(23) supplies the exact
compensation \(\Xi_N=\alpha^{-w}\), \(\alpha=\kappa x^{-d}\).
Consequently its line is not an extra hypothesis:
\[
 \mathcal E_N=\alpha^{-w}\kappa^w=x^{dw},\qquad
 \sup_{|u|\le\eta'}|\mathcal E_N(e^{u/N})|
                           \le e^{|w|\eta'}.               \tag{16}
\]
Its \(\mu\)-derivative of order \(a\) is \((dw)^a x^{dw}\).
Thus (15) holds unconditionally for every fixed meridian jet of
this actual zero-framed pointed source. Explicit additional fixed
powers of \(M^d\) and \(D_N(M)/N\), or their inverses, preserve the
conclusion, including any retained polynomial \(N\)-prefactor:
F(26) gives \(D_N(e^{u/N})/N=\sinh u/[N\sinh(u/N)]\), a uniformly
bounded holomorphic unit with bounded inverse on the buffered collar.

The full original tail is exactly
\(\mathcal E_N(e^{u/N})\widehat{\mathcal P}_{N,\mathrm{tail}}\).
Every true derivative retains the product rule
\[
 \partial_\mu^k\mathcal P_{N,\mathrm{tail}}
  =\sum_{a=0}^{k}\binom ka(\partial_\mu^a\mathcal E_N)
                 (\partial_\mu^{k-a}\widehat{\mathcal P}_{N,\mathrm{tail}}).
                                                                  \tag{17}
\]
If the prescribed line is holomorphic on the buffered collar and
\(\sup_{|u|\le\eta'}|\mathcal E_N(e^{u/N})|\le e^{o(N)}\),
the same rate (15) holds for every full source jet by Cauchy.
Otherwise (13)--(14),(17) retain its exact size and derivatives;
no subexponential bound for an unspecified external line is assumed.
A meromorphic line is retained as a Laurent germ, with its prescribed
finite part taken only after multiplication; its additional pole and
jet orders are not suppressed.

The radial tail becomes exponentially small in absolute size for
\(R>\exp(4\cdot9cv_3/(2\pi))\), after any retained subexponential
line. This gives neither relative angular localization nor a nonzero
closing contraction. The reduced axis trace has an additional prefix
coupon and is not covered by (11) merely by renaming the source;
an equality after the full axis contraction does not give separate
sample bounds or identify geometrically localized densities.
Arbitrary inserted marks likewise require their own bounds. The
meridian normal is transported by the actual fixed banks; geometric
cycle selection and an arbitrary-short-component lower bound remain open.

## Complete proof directs and author verification

* F: `notes/research_actual_meridian_source_frames.md` (506 lines),
  SHA256 `6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976`.
* W: `notes/actual_whole_word_cyclic_dilog_resolvent_period.md` (290 lines),
  SHA256 `9725d8955cb9bf4770566756eb00470d7e990c7e06b9513276509b01a037d59d`.
* H: `notes/actual_cyclic_dilog_hankel_cycle.md` (316 lines),
  SHA256 `502ddfc4b13c7bd775bf27398592085f3951019ff959e1fe6e363a1a468993ea`.
* R: `notes/research_actual_reduced_braid_source.md` (330 lines),
  SHA256 `9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243`.

All four complete directs were freshly whole-read nontruncated in this
active author sequence. Only written proofs and text/hash operations
were used. No mathematical program, test, or build was run; frozen and
public files were not edited.
