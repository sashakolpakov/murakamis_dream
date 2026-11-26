# A complete inner three-crossing asymptotic on the larger rectangle

Private research theorem, 9 November 2026. The original inner
three-crossing trace has a nonzero relative asymptotic throughout
the independent outgoing rectangle
\[
 \mathcal V_+=
 \{u=\beta-iK:0\le\beta\le\pi/2,\ 0\le K\le7/10\}.
 \tag{1}
\]
The result includes both full edges, all physical rows, and both
parities. The previously unestimated low horizontal is controlled
by Cauchy--Schwarz and the complete diagonal Newton profiles.

The theorem concerns an inner trace with complete incoming color.
It does not estimate the final outer trace, prove that its
geometric point lies in (1), or establish stability under arbitrary
short partial fillings. The manuscripts remain unchanged.
No mathematical numerical evaluation is used.

## 1. Exact function and leading term

Retain the original trace algebra
\[
 \mathcal A_N=\mathbb C[x]/(2T_N(x/2)+2),\qquad
 \phi_N(f)=(-1)^{N-1}N^2[x^{N-1}]
              \operatorname{rem}_{2T_N(x/2)+2}f ,
 \tag{2}
\]
where \(T_N\) is the Chebyshev polynomial. Let \(R_N\) be its
original crossing element. Write
\[
\begin{gathered}
 c_a=2\cos((2a+1)\pi/N),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\qquad
 \mathcal K_N(w,x)=\sum_{j=0}^{N-1}e_j(w)e_j(x).
\end{gathered}                                                     \tag{3}
\]
The function in the theorem is exactly
\[
 Q_N(u)=\phi_N\!\left[
 R_N^3\mathcal K_N(-2,x)\mathcal K_N(x,-2\cos u)\right].
 \tag{4}
\]
It is an entire function of \(u\). The trace, including its
derivatives at double physical roots and its odd-level simple
root, has not been replaced by an ordinary sum of values.

Use the original critical point and absolute phase:
\[
\begin{gathered}
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\\
 t_*(u)=a_*(u)-iH(u),\qquad
 \Phi_t(t_*(u),u)=0,\qquad S(u)=\Phi(t_*(u),u).
\end{gathered}                                                     \tag{5}
\]
Their branches and constants are those of the
[larger-strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md).
Throughout (1),
\[
 0<a_*<\pi/2,\quad 2/3<H<1,\quad
 \Re S(u)>321/200,\quad \Phi_{tt}(t_*,u)\ne0.
 \tag{6}
\]

For the edge coefficient set
\[
\begin{gathered}
 c=\cos(t/2),\quad C=\cos(u/2),\quad
 D_0=c^2+C^2-c^2C^2,\quad W=c^2C^2/D_0,\\
 a_e(t,u)=\frac1{4\sqrt{D_0}\,W^{1/4}} .
\end{gathered}                                                     \tag{7}
\]
The roots in (7) are the original real-branch continuations
specified by the
[taller mixed-edge theorem](research_mixed_symmetric_closing_taller_mixed_edge.md).
Put
\[
\begin{gathered}
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)},\\
 A(u)=\frac{i\sqrt{2\pi}}{\pi}
 \frac{\sin t_*(u)\,a_e(t_*(u),0)a_e(t_*(u),u)}
                         {\sqrt{-\Phi_{tt}(t_*(u),u)}} .
\end{gathered}                                                     \tag{8}
\]
The Gaussian square root has the original increasing-contour
orientation. The functions \(S,A\) are holomorphic on a
neighborhood of (1), and \(A\) is nowhere zero there after a
fixed shrink.

**Theorem.** Uniformly for \(u\in\mathcal V_+\), along both
even and odd levels,
\[
 \boxed{\quad
 Q_N(u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}
                         \{1+O(N^{-1})\}.
 \quad}                                                         \tag{9}
\]
In particular, for a fixed \(c>0\) and all sufficiently large \(N\),
\[
                  |Q_N(u)|\ge cN^{-3/2}e^{N\Re S(u)}
                            \qquad(u\in\mathcal V_+).             \tag{10}
\]
On every compact subset of the interior of (1), each fixed
\(u\)-derivative of the normalized relative error in (9) is
\(O(N^{-1})\). The same holds for derivatives in the ordinary
coordinate \(w=-2\cos u\) on those compact subsets. This
derivative statement concerns the normalized error, not
unnormalized derivatives of the exponentially large function.

## 2. Complete remainder comparison

The [fixed-low-remainder theorem](research_mixed_symmetric_closing_fixed_low_remainder.md)
proves, for this literal function and on exactly (1),
\[
 Q_N(u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}
                         \{1+O(N^{-1})\}
             +L_N(u)+O(e^{N(\Re S(u)-\epsilon)})
 \tag{11}
\]
for some fixed \(\epsilon>0\). Its remaining term is precisely
\[
 L_N(u)=-\frac{N^2C_{N,3}}{\pi i}
  \int_{2\pi/3-i/10}^{5\pi/6-i/10}
       \sin t\,K_N^<(t,0)K_N^<(t,u)
       e^{3iNt^2/(4\pi)}
       \frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2}\,dt ,
 \tag{12}
\]
where both shortened kernels retain all rows
\(0\le j\le\lfloor N/2\rfloor-1\).
Equation (11) already includes restoration of both full edges
in (4), with the full Hermite trace.

The [complete row-norm theorem](research_mixed_symmetric_closing_low_horizontal_norm.md)
estimates exactly the absolute integral in (12), including its
prefactor. It gives
\[
                  |L_N(u)|\le Ce^{N(\Re S(u)-1/100)}
                                    \qquad(u\in\mathcal V_+).
 \tag{13}
\]
There is no change of cutoff, contour orientation, parity
normalization, or sampling factor between the two statements.

Since \(\min_{\mathcal V_+}|A|>0\) and \(|C_{N,3}|=1\),
division of the last two terms of (11) by its leading term
costs at most
\[
 C N^{3/2}e^{-N\min(\epsilon,1/100)}=O(N^{-1}).
 \tag{14}
\]
This proves (9), and hence (10).
The nonzero lower bound is obtained by controlling the signed
remainder; no positivity of \(Q_N\) is assumed.

To justify the derivative assertion, form the exact normalized
error
\[
 E_N(u)=C_{N,3}^{-1}N^{3/2}A(u)^{-1}e^{-NS(u)}Q_N(u)-1 .
 \tag{15}
\]
It is holomorphic near (1), and (9) bounds it by \(C/N\)
on that rectangle. Every compact subset of its interior has
a fixed positive distance from its boundary. Cauchy's formula
on disks of smaller fixed radius gives the claimed bounds
for all fixed derivatives of (15). Since \(\sin u\ne0\)
in that interior, the local inverse of \(w=-2\cos u\) and
the chain rule give the ordinary-coordinate assertion.
No bound beyond the closed rectangle has been inferred
from the pointwise estimate.

## 3. What this resolves, and what remains

The small complex neighborhood of the geometric inner critical
point supplies the nonzero Gaussian coefficient. The rest of
the finite trace is now bounded as well: both edge-deletion
errors, far physical samples and normals, endpoint verticals,
the negative and central intervals, and the full right
connection. The low segment was the last part of this
particular inner contour not covered by the earlier estimates.

The ordinary symmetric \(343\) closure has an additional
integration variable. Its actual geometric middle coordinate
must first be shown to lie in (1). Even then, a local
application of (9) at that point does not control the rest of
the outer trace. Establishing a nonzero complete closing
asymptotic therefore remains a separate task.

The function (4) also fixes its incoming ordinary color at
\(-2\). Theorem (9) does not free that color or prove a
composition theorem for arbitrary short tangles. These
requirements remain part of the route to finitely many
exceptional filling assignments.

## Source versions

- Original cubic/action and its larger holomorphic domain:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Local edge symbol, full central interval, and normalized phase:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Larger-domain complete trace with one fixed segment remaining:
  03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0.
- Complete low-current bound with original cutoff and scalar:
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
