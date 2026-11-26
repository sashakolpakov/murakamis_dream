# Rank-one Casimir deformation: uniform polynomial reduction and its limitation

Private continuation, 1 November 2026. No repository file is changed. The input is the fixed-coordinate refinement (18a–e) of `notes/actual_main_meridian_newton_multiplication.md`. This report proves a uniform, all-resonance remainder bound for degree proportional to $N$. It also explains why the small generator perturbation does not give a small error for arbitrary such polynomials or for a whole tangle.

## 1. The exact generator and the return count

Put $d=N-1$, $\mathcal T_n(t+t^{-1})=t^n+t^{-n}$, and

\[
 P_0(\omega)=\mathcal T_N(\omega)+2,\qquad
 P_s=P_0+\Delta_s,\qquad
 \Delta_s=2\cos(2\pi s)-2.
 \tag{1}
\]

Identify the vector spaces of degree-$<N$ representatives using the normalized complete Newton basis. Multiplication by $\omega$ has the exact matrix

\[
 A_s=A_0+\frac{(-1)^N\Delta_s}{N^2}E,
 \qquad E=\mathbf e_0\mathbf e_d^T,
 \tag{2}
\]

where $A_0$ has diagonal $c_r(0)=2\cos((2r+1)\pi/N)$ and subdiagonal $-4\sin^2(\pi(r+1)/N)$. The sign follows from $B_N(0)=(-1)^NP_0$ and $S_d=N$. Thus the coefficient Euclidean norm of the generator difference is exactly $|\Delta_s|/N^2$.

The fixed-coordinate product of two canonical representatives is also exact: if $fg=P_0Q+R$, $\deg R<N$, then $\deg Q<N$ and

\[
 \operatorname{rem}_{P_s}(fg)=R-\Delta_sQ.
 \tag{3}
\]

In particular its first $s$ derivative vanishes at zero. The nonzero derivative of the moving Newton multiplication coefficients is the basis-change coboundary recorded in the source note; it is not a contradiction to (3).

Because $A_0$ is lower bidiagonal, $EA_0^jE=0$ for $j<d$. Starting from $\mathbf e_0$, a return from the last coordinate to the first therefore requires at least $N$ multiplication steps. A polynomial of degree below $2N$, evaluated on $\mathbf e_0$, has at most one return. This does not hold for all entries of its matrix: an initial vector already supported at the last coordinate can return on its first step.

## 2. Exact Chebyshev folding, uniformly through all resonances

Use the Chebyshev normalization

\[
 C_n(t+t^{-1})=\frac{t^n+t^{-n}}2,
 \qquad C_0=1.
 \tag{4}
\]

Thus $\mathcal T_n=2C_n$, including $n=0$. Set $b=\cos(2\pi s)$ and let $\mathcal R_b$ denote the canonical remainder modulo $2(C_N+b)$. In the quotient $C_N=-b$. The elementary identity $2C_iC_j=C_{i+j}+C_{|i-j|}$ gives, for $0<r<N$,

\[
 \mathcal R_b C_r=C_r,\qquad
 \mathcal R_b C_{N+r}=-2bC_r-C_{N-r},
 \tag{5}
\]

and for $k\ge2$,

\[
 \mathcal R_b C_{kN+r}
 =-2b\,\mathcal R_b C_{(k-1)N+r}
       -\mathcal R_b C_{(k-2)N+r}.
 \tag{6}
\]

For $r=0$, the initial values are $\mathcal R_bC_0=1$ and $\mathcal R_bC_N=-b$, followed by the same recurrence. These are polynomial identities in $b$, not interpolation formulas at distinct roots. Hence they remain valid at every collision and resonance.

For a polynomial $F=\sum_n a_n C_n$, define its Chebyshev coefficient norm by

\[
 \|F\|_{\mathrm{Ch}}=\sum_n|a_n|.
 \tag{7}
\]

The product identity gives $\|FG\|_{\mathrm{Ch}}\le\|F\|_{\mathrm{Ch}}\|G\|_{\mathrm{Ch}}$ exactly, including zero indices. If $|b|\le B$, $B\ge1$, put $L=2B+1$. Induction in (5)–(6) proves

\[
 \|\mathcal R_b C_{kN+r}\|_{\mathrm{Ch}}\le L^k
 \quad(0\le r<N).
 \tag{8}
\]

For the induction step, $2BL^{k-1}+L^{k-2}\le L^k$. At $r=0$, the initial bound $|b|\le L$ is sufficient. Consequently, for every polynomial of degree at most $mN$,

\[
 \boxed{\quad
 \|\operatorname{rem}_{P_s}F\|_{\mathrm{Ch}}
       \le L_R^m\|F\|_{\mathrm{Ch}},\qquad
 L_R=2\cosh(2\pi R)+1,\quad |s|\le R.
 \quad}
 \tag{9}
\]

The bound is independent of $N$ and includes every fixed complex resonance, with no restriction $R<1$. It concerns polynomial reduction, not the existence of a bounded polynomial representative for a physical coupon at a resonance.

There is also a quantitative difference bound. Differentiating (5)–(6) with respect to $b$ gives

\[
 \|\partial_b\mathcal R_b C_{kN+r}\|_{\mathrm{Ch}}
       \le 2kL^{k-1}.
 \tag{10}
\]

The induction follows from $2L^{k-1}+2B\cdot2(k-1)L^{k-2}+2(k-2)L^{k-3}\le2kL^{k-1}$. Integrate along the segment from $1$ to $b$; its modulus is at most $B$. Since $\Delta_s=2(b-1)$,

\[
 \|\operatorname{rem}_{P_s}F-\operatorname{rem}_{P_0}F\|_{\mathrm{Ch}}
       \le mL_R^{m-1}|\Delta_s|\,\|F\|_{\mathrm{Ch}}.
 \tag{11}
\]

Thus the change is uniformly $O_R(s^2)$ near completeness in this norm, but it has no additional negative power of $N$. Cauchy's estimate in $s$ on a larger fixed disk bounds every fixed parameter derivative of the remainder operator by a constant depending on $m,R$ and the derivative order, not on $N$.

## 3. Products, ordinary sup norms, and a finite quotient expansion

For $m$ canonical inputs $f_1,\ldots,f_m$, each of degree below $N$, their product has degree below $mN$. Equations (7)–(9) sharpen to

\[
 \left\|\operatorname{rem}_{P_s}\prod_{j=1}^m f_j\right\|_{\mathrm{Ch}}
       \le L_R^{m-1}\prod_{j=1}^m\|f_j\|_{\mathrm{Ch}}.
 \tag{12}
\]

This applies to $s$-dependent input polynomials pointwise; any bounds or poles of those inputs remain their own responsibility. It does not assume positivity of their coefficients.

For a polynomial of degree $d_F$, elementary cosine coefficient integration gives

\[
 \|F\|_{[-2,2]}\le\|F\|_{\mathrm{Ch}}
       \le(2d_F+1)\|F\|_{[-2,2]}.
 \tag{13}
\]

Therefore (9) implies

\[
 \|\operatorname{rem}_{P_s}F\|_{[-2,2]}
       \le L_R^m(2mN+1)\|F\|_{[-2,2]}
 \qquad(\deg F\le mN).
 \tag{14}
\]

For each fixed derivative order, Markov's inequality for the output polynomial of degree below $N$ adds only a fixed power of $N$. The same assertion for complex polynomials follows by applying the real inequality after rotating the value of a derivative into the real axis, or by bounding real and imaginary parts. Thus this is a polynomial-cost bound for the value and derivative norms of the canonical remainder. It was proved from exact folding, not inferred from the norm of $A_s-A_0$.

A useful weighted version follows with no new proof. For $\eta\ge0$ let $\|F\|_{\mathrm{Ch},\eta}=\sum_n|a_n|e^{\eta n}$. The product remains submultiplicative. Every term in the remainder of $C_n$ has index at most $n$, so the bounds (9) and (12) hold with the same constants in these weighted norms as well. These are Chebyshev coefficient weights; they do not automatically coincide with the optimal geometric weights of an arbitrary tangle.

There is a finite quotient decomposition underlying (3). Repeated monic division gives, uniquely,

\[
 F=\sum_{j=0}^{m}P_0^jR_j,\qquad \deg R_j<N,
 \qquad
 \operatorname{rem}_{P_s}F=\sum_{j=0}^{m}(-\Delta_s)^jR_j
 \quad(\deg F\le mN).
 \tag{15}
\]

The degree in $\Delta_s$ is at most $m$. On $|\Delta|=1$, one has $|b|=|1+\Delta/2|\le3/2$, so (9) has $L=4$. Banach-valued Cauchy coefficient extraction in (15) yields the uniform quotient bounds

\[
 \|R_j\|_{\mathrm{Ch}}\le4^m\|F\|_{\mathrm{Ch}},
 \qquad 0\le j\le m.
 \tag{16}
\]

The higher quotients are invisible in the complete algebra, where only $R_0$ remains. They are controlled relative to the unreduced polynomial norm in (16), not relative to a possibly much smaller complete signed contraction of $R_0$.

## 4. A sharp obstruction to treating the generator perturbation as a small source error

The level-dependent polynomial $P_0=2C_N+2$ has Chebyshev norm four and vanishes at $A_0$, but

\[
 P_0(A_0)=0,\qquad P_0(A_s)=-\Delta_s I.
 \tag{17}
\]

Thus even a uniformly bounded Chebyshev coefficient norm and degree exactly $N$ do not turn the $N^{-2}$ generator perturbation into an $o(1)$ functional-calculus error.

The same effect occurs for a product of two allowed canonical inputs. Choose $1\le a,b<N$ with $a+b=N$. Both $C_a$ and $C_b$ have coefficient norm one. Their product identity gives

\[
 \operatorname{rem}_{P_s}(C_aC_b)
       -\operatorname{rem}_{P_0}(C_aC_b)
       =-\frac{\Delta_s}{4}.
 \tag{18}
\]

This has order one for fixed $s$ with $\Delta_s\ne0$. At even $N$, take $a=b=N/2$. Since $4C_{N/2}^2=P_0$, the complete product itself is zero, while its moved product is $-\Delta_s/4$. This is an obstruction inside the canonical polynomial algebra, not a reliance on an arbitrary high-degree representative. It does not claim these two factors are the physical coupons or the selected stationary contribution of a knot.

For comparison, the same generator written in the canonical Chebyshev basis has a last-column difference $-\Delta_s/2$ in its constant coordinate. Its coefficient-norm difference is therefore of order one. The $N^{-2}$ in (2) belongs to the normalized complete Newton coordinate norm; it is not a coordinate-free smallness statement.

The first derivative of every fixed-coordinate product is zero because $\Delta'_0=0$, whereas (18) has a nonzero second derivative. A first-jet bound alone does not constrain this genuinely finite microscopic change.

## 5. A restricted analytic stability statement and the remaining source issue

For a function with a uniformly convergent Chebyshev expansion $F_N=\sum_{n\ge0}a_{n,N}C_n$, suppose for some fixed $\eta>0$ that

\[
 \sum_{n\ge0}|a_{n,N}|e^{\eta n}\le A_N.
 \tag{19}
\]

For large $N$, the folding series converges absolutely because $L_R e^{-\eta N}<1$. The terms below $N$ are unchanged. Applying (10)–(11) to the remaining terms, with $k=\lfloor n/N\rfloor$, gives

\[
 \|\mathcal R_bF_N-\mathcal R_1F_N\|_{\mathrm{Ch}}
       \le C_R |\Delta_s| e^{-\eta N}A_N,
       \qquad |s|\le R,
 \tag{20}
\]

once $N$ is large enough in terms of $R,\eta$. For instance use $kL_R^{k-1}e^{-\eta kN}\le C_R e^{-\eta N}$. This is exponential stability of the canonical remainder of an analytic test function, equivalently its action on the constant vector. It is not the same estimate for every entry of $F_N(A_s)-F_N(A_0)$, as the return-count qualification in Section 1 already shows. Physical polynomial representatives of growing degree need not satisfy (19) with a selected-source-sized $A_N$.

The immediate use of (12) is nevertheless general: in a fixed finite polynomial multiplication circuit, reduction in the equal-color algebra has no new exponential cost in the Chebyshev coefficient norm, even across ordinary resonances. The unresolved operations are the actual physical leaf realization, the typed turns, their coordinate norms at the required geometric weights, and comparison with the selected closing scalar. A physical coupon may have a pole in its polynomial coordinates while its physical matrix remains regular; the polynomial identity (9) does not remove that pole.

The bounded quotient index in (15) is a Casimir-algebra index. It is different from the main-meridian carry $U=Y^N$ in the finite-matrix criterion. The rank-one representation therefore does not supply the whole preoperator's first-normal source, its saturated kernel frame, or a lower singular-value bound for that criterion. It could simplify an explicit construction of such data, but no source-retaining map between the two reductions has been proved here.

The precise limitation can be stated without an example knot: (16) controls all returned quotients by an unreduced polynomial norm, while (18) shows that the complete product can lose the entire relevant contribution. Any relative bound by the actual complete knot scalar must still use the physical source and its cancellations. No absolute-sum replacement or high-degree polynomial stability assumption is hidden in the folding estimate.
