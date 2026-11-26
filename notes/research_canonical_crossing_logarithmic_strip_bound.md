# A logarithmic strip bound for every canonical crossing power

Private written proof, 23 November 2026.

Every signed integer power of the original crossing has a canonical
polynomial whose real-boundary norm is logarithmic in the level, with
only linear dependence on the absolute power. The same estimate controls
its whole periodic microscopic strip and every fixed parameter derivative.
Both level parities and all first physical normals are retained.

This improves a polynomial evaluation bound for the actual finite
polynomial. It does not estimate a genuine turn or an original closing
from below, and supplies no new volume-identity case.

## 1. The complete original data

Fix \(N\ge2\), \(d=N-1\), and the recorded phases
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=e^{\pi i d^2/(2N)},\quad P_N(z)=2T_N(z/2)+2.
\]
For every \(n\in\mathbb Z\), let \(r_{n,N}\) be the canonical
degree-below-\(N\) representative of \(\kappa^{-n}R^n\) in the
original full algebra \(\mathbb C[z]/P_N\). Negative powers mean
the actual inverse. Put
\[
 t_j=(2j+1)\pi/N,\quad c_j=2\cos t_j,\quad
 \nu_j=(-1)^jq^{j(j+1)},\quad
 g(t)=r_{n,N}(2\cos t).
\]
The complete source [F] gives exactly
\[
 h_j:=g(t_j)=\nu_j^n,\qquad
 \gamma_j:=g'(t_j)=-\frac{in}{2}(d-2j)h_j
 \quad(0\le j<N).
 \tag{1}
\]
Thus \(|h_j|=1\), \(|\gamma_j|\le |n|N/2\), and
\(\sum_j\gamma_j=0\). For the last assertion pair \(j,d-j\):
their values agree and their derivatives are opposite. At odd \(N\)
the self-paired node is \(-2\) and its angular derivative is zero.
This imposes no additional spectral normal at that simple node.

Define
\[
 M_{N,n}=1+|n|\left\{\frac\pi2+
                         \frac4\pi(1+\log N)\right\}.
 \tag{2}
\]
**Theorem.** Uniformly for all \(N\ge2\) and all integers \(n\),
\[
 \boxed{\quad\max_{-2\le z\le2}|r_{n,N}(z)|\le M_{N,n}.\quad}
 \tag{3}
\]
For \(w_N(\alpha)=2\cosh(\alpha/N)\), every \(r\ge0\) and
integer \(k\ge0\) also satisfy
\[
 \sup_{|\Re\alpha|\le r}
       |r_{n,N}(w_N(\alpha))|\le e^rM_{N,n},
\]
\[
 \boxed{\quad
 \sup_{|\Re\alpha|\le r}
 |\partial_\alpha^k r_{n,N}(w_N(\alpha))|
                    \le k!e^{r+1}M_{N,n}.
 \quad} \tag{4}
\]
There is no restriction on the imaginary height in these suprema.
The unnormalized crossing has the retained scalar \(\kappa^n\),
of modulus one, so its absolute bounds are identical.

## 2. Exact trigonometric Hermite interpolation

For \(\delta=t-t_j\), define the removable trigonometric polynomials
\[
 K_j(t)=\frac1{N^2}
       \left\{\frac{\sin(N\delta/2)}{\sin(\delta/2)}\right\}^2,
 \qquad
 L_j(t)=\frac2{N^2}\sin^2(N\delta/2)\cot(\delta/2).
 \tag{5}
\]
The finite geometric series gives
\[
 K_j(t)=\frac1{N^2}\sum_{\ell=-(N-1)}^{N-1}
                         (N-|\ell|)e^{i\ell(t-t_j)},
\]
\[
 L_j(t)=\frac1{N^2}\left\{\sin(N\delta)
                     +2\sum_{\ell=1}^{N-1}\sin(\ell\delta)\right\}.
 \tag{6}
\]
At the grid, \(K_j(t_k)=\delta_{jk}\), \(K_j'(t_k)=0\),
\(L_j(t_k)=0\), and \(L_j'(t_k)=\delta_{jk}\).
The apparent singularity at \(\delta=0\) gives these same limits.
For real \(t\), \(K_j(t)\ge0\), and finite character summation
in (6) gives \(\sum_jK_j(t)=1\).

The exact original polynomial is
\[
                    g(t)=\sum_j h_jK_j(t)+\sum_j\gamma_jL_j(t).
 \tag{7}
\]
Indeed its right side matches all values and angular derivatives.
Its possible frequency-\(N\) term vanishes: since
\(\sin(N(t-t_j))=-\sin Nt\), its coefficient is a multiple of
\(\sum_j\gamma_j=0\). It therefore has trigonometric degree at
most \(N-1\), like \(g\). Their difference, multiplied by
\(e^{i(N-1)t}\), is a polynomial in \(e^{it}\) of degree at most
\(2N-2\), with double zeros at the \(N\) distinct grid points.
It vanishes identically. This argument includes even middle aliases
and the odd simple spectral node through precisely the data (1).

## 3. The logarithmic norm and the whole strip

Fix real \(t\), choose a closest grid point, and let its circular
distance be \(a\le\pi/N\). All numerators
\(\sin^2(N(t-t_j)/2)\) in (5) agree. The closest contribution obeys
\[
 |L_j(t)|\le\frac2{N^2}\frac{N^2a^2}{4}\frac2a=a
                                                    \le\frac\pi N.
\]
At \(a=0\) use the removable limit. The other points at circular
distance \(k\) grid steps have distance at least
\((2k-1)\pi/N\), with at most two points at each step.
Using \(|\cot(\delta/2)|\le2/|\delta|\) for
\(0<|\delta|\le\pi\), and bounding the odd harmonic sum by
\(H_N\le1+\log N\), gives
\[
 \sum_j|L_j(t)|\le\frac1N
                 \left\{\pi+\frac8\pi(1+\log N)\right\}.
 \tag{8}
\]
The value part of (7) has modulus at most one by positivity and
partition of unity. Combine (1) and (8) to prove (3).

For completeness, if a polynomial \(p\) has degree at most \(d\)
and real-interval norm \(M\), then
\(H(\zeta)=\zeta^dp(\zeta+\zeta^{-1})\) is a polynomial bounded
by \(M\) on the unit circle. The maximum principle in its disk,
and replacement of \(\zeta\) by \(\zeta^{-1}\), give
\[
 |p(\zeta+\zeta^{-1})|\le M\max(|\zeta|,|\zeta|^{-1})^d.
\]
Take \(\zeta=e^{\alpha/N}\) and \(d=N-1\) to obtain the first
bound in (4). Cauchy's formula on a unit disk about each \(\alpha\),
using the strip of width \(r+1\), proves the derivative bound.
These are fixed-root parameter derivatives, not moving-\(q\) normals.

## 4. The logarithmic factor is needed uniformly over all powers

Take the actual level-dependent integer power \(n=2N\). Its data are
\(h_j=1\) and \(b_j=\gamma_j/i=-N(d-2j)\).
For \(1\le\ell<N\), the exact Fourier--Hermite formula [F] says
\[
 r_{2N,N}(z)=1+\sum_{\ell=1}^{N-1}2a_\ell T_\ell(z/2),\qquad
 a_\ell=\frac1{N^2}\sum_{j=0}^{N-1}b_j e^{-i\ell t_j}
                         =\frac{i}{\sin(\ell\pi/N)}.
 \tag{9}
\]
To check the last equality, put \(s=Q^{-\ell}\ne1\).
The finite geometric series and its derivative give
\(\sum_js^j=0\), \(\sum_jjs^j=-N/(1-s)\); substitution in
(9) gives \(-2q^{-\ell}/(1-Q^{-\ell})=i/\sin(\ell\pi/N)\).
Consequently, at the endpoint itself,
\[
 r_{2N,N}(2)=1+2i\sum_{\ell=1}^{N-1}\csc(\ell\pi/N),\qquad
 |r_{2N,N}(2)|=\frac4\pi N\log N+O(N).
 \tag{10}
\]
For the asymptotic, subtract
\(1/(\pi t)+1/(\pi(1-t))\) from \(\csc\pi t\).
The difference is bounded on \([0,1]\). Its finite sum is \(O(N)\),
whereas the two subtracted sums total \(2NH_{N-1}/\pi\).
This proves (10). Thus a bound \((1+|n|)o(\log N)\) cannot hold
uniformly over all integer powers. This sharpness uses \(n=2N\);
it is not a growth claim for a fixed short filling.

## 5. Full-algebra multiplication in the same norm

For a canonical polynomial \(f\), write
\(M(f)=\max_{[-2,2]}|f|\), and put
\(A_N=\pi+(8/\pi)(1+\log N)\).
Let \(\operatorname{can}\) mean the remainder modulo the full \(P_N\),
including every first normal. Then
\[
 M(\operatorname{can}(fg))\le(1+2eA_N)M(f)M(g),
 \tag{11}
\]
and for every signed integer \(n\),
\[
 M(\operatorname{can}(r_{n,N}f))
       \le\{1+(e+|n|/2)A_N\}M(f).
 \tag{12}
\]
Indeed the strip proof applies to every canonical \(f\).
Cauchy's formula on a unit disk gives
\(|\partial_\alpha f(w_N(\alpha))|\le eM(f)\)
on the imaginary axis. With \(\alpha=iNt\), this implies
\(|\partial_t f(2\cos t)|\le eNM(f)\).
The full product has nodal values bounded by \(M(f)M(g)\)
and angular derivatives bounded by \(2eNM(f)M(g)\).
Insert those data in (7) and use (8) to obtain (11).
For (12), use the unit nodal values and the exact normal (1)
instead. The angular derivatives sum to zero by reflection in
both cases, including the self-paired odd simple node, so (7)
is valid for the canonical full product. Quotient carries have
already been retained; no semisimple projection is used.

Thus the canonical multiplication constants in this norm grow
only logarithmically with \(N\), with linear dependence on \(|n|\)
for an actual crossing power. This is a Banach norm estimate;
it supplies no comparison with a physical Hilbert metric.

## 6. Gain, limits and complete source versions

The earlier circle estimate [K] gives coefficient mass
\(2N(1+|n|/2)\); [F] already gives a polynomial real-boundary bound
from its first-kind coefficients. The addition here is the logarithmic
evaluation estimate for the canonical polynomial, its full periodic
strip and derivatives, the full-product estimates (11)--(12),
and the actual sharpness sequence (10).
The more general free-boundary interpolation estimate [H] deliberately
uses unoptimized polynomial cardinal bounds and concerns different data.

Canonical reduction and the full physical normals remain essential.
The estimates do not bound the Newton norm of a multiplication operator
by \(M_{N,n}\), make a genuine turn harmless, compare its contour with
an analytic representative without currents, or give a lower bound for
the original cap. Arbitrary fixed short components still require their
whole source and geometric comparison. No volume theorem is proved.

All three complete matching texts were read; the proofs above use only
written mathematics. Earlier final and public files are unchanged.

| Role | Complete text | SHA-256 |
| --- | --- | --- |
| F, input | [Original Fourier--Hermite twist kernel, 160 lines](actual_twist_circle_fourier_kernel.md) | 1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292 |
| K, coverage | [Canonical filling-kernel splitting, 351 lines](research_canonical_hermite_filling_kernel_split.md) | bf615d1dcf2193b1c277599c2730ab3e1da01001b7e42927c77c5cbe044a74e6 |
| H, coverage | [High-index full-Hermite bound, 363 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_high_index_free_boundary_hermite_bound.md) | 041ba93916ffb71d5549286538c24302d89f80b0f1936ea928f6dd3eaf490ac7 |

No mathematical program, numerical test, build or git operation was used.
