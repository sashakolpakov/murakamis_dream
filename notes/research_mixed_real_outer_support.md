# Global real supporting planes for the complete conditional kernels

Research proof, 4 November 2026. This is a real-neighbor consequence
of the proved global root and full conditional-source theorems.
It supplies a reusable coherent bound on the whole open real
half-square. Its supporting planes are based at real points;
they are not the complex geometric supporting planes.

## 1. The allocated original rate

For \(\eta,\epsilon\in\{0,1\}\), retain
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi_{\eta\epsilon}(a,b)
   &=Q_\epsilon(s_*(a,b);a,b)
                      -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 f_{\eta\epsilon}(a,b)&=\Re\phi_{\eta\epsilon}(a,b),
                      \qquad 0<a,b<1/2 .
 \end{split}                                                     \tag{1}
\]
The global root is the original zero-lift root. By
[the cotangent-root theorem](research_mixed_global_cotangent_roots.md),
if \(S=\cot\pi s_*=u+iv\), then
\[
                         u>0,\qquad |v|<1.                     \tag{2}
\]
For real outer variables \(p=\cot\pi a\), \(q=\cot\pi b\), one has
\(p,q>0\). The root remains in \(0<\Re s_*<1/2\), so every
argument of (1) remains in its original regular strip. No periodic
replacement of the primitive is made.

**Theorem 1.** For every ordered pair of types, the real function
\(f_{\eta\epsilon}\) is strictly concave on the convex domain
\((0,1/2)^2\). Its negative real Hessian is positive definite
everywhere. On each compact convex subset \(K\) of this domain there
is \(\lambda_K>0\) such that, for all \(c,x\in K\),
\[
 f_{\eta\epsilon}(x)
 \le f_{\eta\epsilon}(c)+
       \Re\phi_{\eta\epsilon}'(c)\cdot(x-c)
                            -\frac{\lambda_K}{2}|x-c|^2.        \tag{3}
\]

## 2. Triangle forms and the complex Schur complement

Let \(V(s,a)=g(s+a)-g(s)-g(a)\). Put
\[
 C_p=\Re\frac{pS-1}{S+p}.
\]
The real negative Hessian of \(V\), divided by \(\pi\), is
\[
                 T_p=
       \begin{pmatrix}u-C_p&-C_p\\-C_p&p-C_p\end{pmatrix}.       \tag{4}
\]
Its determinant is exactly
\[
 \det T_p
   =\frac{(u+p)^2-p^2v^2}{(u+p)^2+v^2}>0.                    \tag{5}
\]
Indeed \(|v|<1\) implies that the numerator exceeds
\((u+p)^2-p^2=u(u+2p)>0\).
The determinant identity also gives
\(C_p<up/(u+p)<\min(u,p)\), so both diagonal entries are
positive. Thus \(T_p\) is positive definite. The same applies
to \(T_q\).

Before eliminating \(s\), the allocated phase is
\[
 V(s,a)+V(s,b)-\epsilon g(s)-\tfrac\eta2g(a)
                  -\tfrac\epsilon2g(b)+2\pi ias.              \tag{6}
\]
The chirp has purely imaginary Hessian. The real part of the
negative Hessian of (6) is the sum of the two positive pair forms
(4), embedded in \((s,a,b)\), and the nonnegative diagonal form
\[
                  \pi\,\operatorname{diag}
                      (\epsilon u,\eta p/2,\epsilon q/2).
 \tag{7}
\]
The overlapping pair forms already make the three-variable form
positive definite: a nonzero vector cannot vanish on both pairs.

For completeness, a complex Schur complement does preserve this
real positivity. Write the complex symmetric negative Hessian as
\[
 H=\begin{pmatrix}c+id&(U+iW)^T\\U+iW&A+iB\end{pmatrix},
 \quad c>0,
 \tag{8}
\]
where all displayed lowercase and uppercase coefficients other than
\(i\) are real. The outer condensed Hessian is
\(H_{\rm eff}=A+iB-(U+iW)(U+iW)^T/(c+id)\). Direct algebra gives
\[
 \Re H_{\rm eff}
 =A-\frac{UU^T}{c}
       +\frac{(dU-cW)(dU-cW)^T}{c(c^2+d^2)}.
 \tag{9}
\]
The first two terms are the Schur complement of \(\Re H\) and
are positive definite. The last term is nonnegative. Since
\(Q_{\epsilon,s}=0\), this is exactly
\(-\Re\phi_{\eta\epsilon}''\), with all conditional derivative
terms retained. This proves pointwise positivity in Theorem 1.
Continuity on \(K\), followed by the real segment Taylor formula,
proves (3). Here convexity of the real half-square is essential;
no convexity of the complex cotangent-domain preimage is assumed.

## 3. The literal finite-source bound

Let \(r_N=e^{-2\pi i/N}\), \(P_j=(r_N;r_N)_j\), and use the
original full Laurent kernel and polynomial Fourier weight:
\[
 C_{\epsilon,N}(X,Y)=
   \sum_{j=0}^{N-1}
     \frac{X^{-j}(r_NX;r_N)_j(r_NY;r_N)_j}{P_j^{2+\epsilon}},
 \qquad d_N(r_N^k)=P_k^{-1},\quad \deg d_N<N.
 \tag{10}
\]
For real \(a,b\in(0,1/2)\), set
\[
 {\cal B}_{\eta\epsilon,N}(a,b)=
 |C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ib})|\,
 |d_N(e^{-2\pi ia})|^{\eta/2}
 |d_N(e^{-2\pi ib})|^{\epsilon/2}.
 \tag{11}
\]
These half-powers are nonnegative real moduli. In original cyclic
products they recombine into integer powers.

**Corollary 2.** Uniformly on every compact \(K\Subset(0,1/2)^2\),
both parities satisfy
\[
 {\cal B}_{\eta\epsilon,N}(a,b)
 =N^{-(2+\eta+3\epsilon)/4}\,
     b_{\eta\epsilon}(a,b)e^{Nf_{\eta\epsilon}(a,b)}
                              (1+O_K(N^{-1})),               \tag{12}
\]
where \(b_{\eta\epsilon}\) is continuous, strictly positive and
bounded above and away from zero on \(K\). Consequently, for convex
\(K\), the whole original source satisfies
\[
 {\cal B}_{\eta\epsilon,N}(x)
 \le C_KN^{-(2+\eta+3\epsilon)/4}
  \exp N\left\{
    f_{\eta\epsilon}(c)+\Re\phi_{\eta\epsilon}'(c)\cdot(x-c)
                          -\frac{\lambda_K}{2}|x-c|^2\right\}
 \tag{13}
\]
for every \(c,x\in K\) and sufficiently large \(N\).

The [all-real conditional packet](research_mixed_all_real_conditional_packet.md),
Theorem 2, applies to the complete canonical sum, including both
tails, all revived rows and the original cotangent currents.
Dividing its two factorial interpolants gives the nonzero kernel
packet with power \(N^{-(1+\epsilon)/2}\) and phase
\(Q_\epsilon(s_*)-g(a)-g(b)\).
The [Fourier-weight comparison](research_mixed_fourier_weight_continuation.md),
Theorem 1, is relatively accurate on every such real compact set
because \(-\Re g(a),-\Re g(b)>0\). Each allocated half-weight
therefore contributes the power \(N^{-1/4}\) and the rate
\(-\Re g/2\). This proves (12), including its scalar power;
(3) and boundedness of the symbol give (13).

Any selected outer factor \(e^{2\pi iN a}\) has modulus one on
this real contour, so (13) also bounds every original selection
at the same real target points. No extra alias gain is asserted.

The compact restriction cannot be dropped from the uniform constants:
this note proves no uniform estimate at \(a=0\), \(b=0\) or the
half-period endpoints. It asserts no complex-neighbor packet or
ordinary derivative estimate beyond the scope of its source inputs.
Most importantly, replacing \(c\) by an actual complex geometric
reference is not permitted in (3) or (13). A coupled contour that
resets heights must still pay the difference between these real
supporting planes and the original geometric planes. The
[reset obstruction](research_mixed_left_support_obstructions.md)
shows why this difference cannot be omitted.

## Reproduction

The proof is analytic on the entire real domain. The focused checker
verifies the determinant, positive-numerator decomposition, complex
Schur identity and source powers symbolically, and checks the current
source-record bindings. It makes no sampled claim of global positivity.

    python3 experiments/check_mixed_real_outer_support.py
