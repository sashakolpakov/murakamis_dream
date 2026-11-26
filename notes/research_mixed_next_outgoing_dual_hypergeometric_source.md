# A common terminating dual source for the outgoing Fourier coefficients

Private exact-source deduction, 9 November 2026. A first difference at
odd levels puts both parities into the same terminating basic
hypergeometric sum. Its inverse is kept in the original observation,
where the exact odd radical factor cancels a Dirichlet denominator.
The consecutive-summand equation retains the complex outgoing root
and gives a quartic candidate for coherent stationary points.

These are finite identities and a principal-ratio statement. No
hypergeometric summation, admissible complex-index contour, selected
coefficient asymptotic, or sufficient attachment budget is asserted.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original normalization and a reversible parity change

Use the complete source of
[the positive transition theorem, (1)--(16)](research_mixed_next_outgoing_positive_chebyshev_transition.md):
\[
\begin{gathered}
 N\ge6,\quad D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad Q=q^2,\quad
 M=\lceil N/2\rceil,\quad U=D-M,\quad \sigma=N\bmod2,\\
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{h=1}^js_h,\quad S_0=1,\quad
 c_j=2\cos((2j+1)\pi/N),\\
 \mathcal D_d=S_{M+d}^2/S_M^2,\qquad
 B_{n,j}=S_n/(S_jS_{n-j}),\quad 0\le j\le n<N,\\
 P_{M+d}^{\rm rad}(X)
   =\prod_{h=M}^{M+d-1}\frac{c_h-X}{s_{h+1}^2},\\
 C_{b,N}(Z)=\sum_{\ell=0}^{D-b}
       \frac{r^{-b\ell}(r^{b+1};r)_\ell(rZ;r)_\ell}
                          {(r;r)_\ell^2},\\
 F_N^+(X,Z)=\sum_{d=0}^{U}(-q)^{M+d}
                    C_{M+d,N}(Z)P_{M+d}^{\rm rad}(X)
       =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2).
\end{gathered}                                                     \tag{1}
\]
Every stop is literal; in particular \(C_{D,N}=1\). The superscript
on \(F_N^+\) denotes the adopted complete outgoing polynomial, not a
choice of one Fourier sector.

Set \(\eta_0=1\), \(\eta_k=2\) for \(k>0\), and
\[
 g_{k,N}=f_{k,N}/\eta_k,\qquad g_{U+1,N}=0,\qquad
 h_{k,N}=
 \begin{cases}
 g_{k,N},&\sigma=0,\\
 g_{k,N}-g_{k+1,N},&\sigma=1 .
 \end{cases}                                                       \tag{2}
\]
Define positive weights
\[
 b_{d,k,N}=\frac{B_{2d+\sigma,d-k}}{\mathcal D_d},
                  \qquad 0\le k\le d\le U.                         \tag{3}
\]
The largest sine-binomial index is \(2U+\sigma=N-2\), so no
factorial in (3) reaches a zero sine.

**Proposition 1.** At both parities the exact transformed coefficient is
\[
 \boxed{\quad
 h_{k,N}(Z)=(-1)^{M+k}\sum_{d=k}^{U}
             q^{M+d}b_{d,k,N}C_{M+d,N}(Z).
 \quad}                                                           \tag{4}
\]
The transformation is exactly inverted by
\[
 g_{k,N}=h_{k,N}\quad(\sigma=0),\qquad
 g_{k,N}=\sum_{j=k}^{U}h_{j,N}\quad(\sigma=1).                       \tag{5}
\]

For even levels, (4) is the transition theorem with \(\eta_k\)
removed. For odd levels put \(X=-(z+z^{-1})\). The exact numerator is
\[
 (1-z)\mathcal D_dP_{M+d}^{\rm rad}(-(z+z^{-1}))
       =z^{-d}(q^{-2d}z;Q)_{2d+1}.                                \tag{6}
\]
Its coefficient of \(z^{-k}\) is
\((-1)^{d-k}B_{2d+1,d-k}\). On the other hand the coefficient of
\(z^{-k}\) in \((1-z)F_N^+(-(z+z^{-1}),Z)\) is
\(g_{k,N}-g_{k+1,N}\), including \(k=0,U\). Multiplication by
\((-q)^{M+d}\) leaves the sign \((-1)^{M+k}\) and proves (4).
Telescoping with the actual endpoint \(g_{U+1,N}=0\) proves (5).
The positive weights do not make (4) a positive sum: both the
conditional polynomial and \(q^{M+d}\) retain their phases.

## 2. A common terminating four-parameter series

For \(0\le k\le U\), \(0\le\ell\le U-k\), put
\[
 L=U-k-\ell,\qquad
 a=Q^{\,k+(1+\sigma)/2},\qquad b=Q^{\,k+1+\sigma/2}=qa.
                                                                    \tag{7}
\]
Fractional powers here mean \(Q^v=\exp(2\pi iv/N)\), not a freely
chosen root. Define the following finite series:
\[
 \mathcal W_{L,N}(a,b)=
 \sum_{p=0}^{L}
 \frac{(a;Q)_p(-a;Q)_p(b;Q)_p(Q^{-L};Q)_p}
      {(Q;Q)_p(a^2;Q)_p(-b;Q)_p^2}\,Q^p .
                                                                    \tag{8}
\]
Thus \(\mathcal W\) is the terminating
\({}_4\phi_3(a,-a,b,Q^{-L};a^2,-b,-b;Q,Q)\), with its finite
meaning specified in (8), even at this root of unity.

**Proposition 2.** The complete outgoing coefficient has the exact
dual expression
\[
 \boxed{\begin{split}
 h_{k,N}(Z)={}&\frac{(-1)^{M+k}}{\mathcal D_k}
 \sum_{\ell=0}^{U-k}
 i^\ell q^{\,M-U\ell+\ell(\ell-1)/2+k(\ell+1)}
       \frac{(rZ;r)_\ell}{S_\ell^2}\\
 &\hspace{12mm}\cdot
 \frac{S_{U-k}}{S_{U-k-\ell}}\,
           \mathcal W_{U-k-\ell,N}(a,b).
 \end{split}}                                                       \tag{9}
\]
All denominator factors in (8)--(9) are nonzero. No continuation
past a physical stop is used.

To prove the identity, use the original reflected row
[in the exact Newton theorem, (9)](research_mixed_next_middle_exact_newton_coefficients.md):
\[
 C_{M+d,N}(Z)=\sum_{\ell=0}^{U-d}
 i^\ell q^{-(U-d)\ell+\ell(\ell-1)/2}
       \frac{S_{U-d}}{S_{U-d-\ell}S_\ell^2}(rZ;r)_\ell .
                                                                    \tag{10}
\]
Changing order in the finite triangle of (4) leaves the inner sum
\[
 \sum_{d=k}^{U-\ell}T_d,\qquad
 T_d=q^{d(\ell+1)}b_{d,k,N}
                       \frac{S_{U-d}}{S_{U-d-\ell}}.                \tag{11}
\]
For \(d<U-\ell\), its exact ratio is
\[
 \frac{T_{d+1}}{T_d}
 =q^{\ell+1}
 \frac{s_{2d+\sigma+1}s_{2d+\sigma+2}s_{U-d-\ell}}
 {s_{d+1-k}s_{d+k+\sigma+1}s_{U-d}^{\,3}}.                           \tag{12}
\]
Here \(s_{M+d+1}=s_{U-d}\), so the denominator contains precisely
the two Newton factors and the reflected-row factor.

For clarity, set \(v=d+1+\sigma/2\) just for this trigonometric
calculation. Then
\[
 s_{U-d}=2\cos(v\pi/N),\qquad
 s_{2d+\sigma+2}=s_v\,2\cos(v\pi/N).
\]
Using \(s_\xi=iq^{-\xi}(1-Q^\xi)\) and
\(2\cos(\xi\pi/N)=q^{-\xi}(1+Q^\xi)\), (12) becomes
\[
 \frac{T_{d+1}}{T_d}
 =Q\,
 \frac{(1-Q^{2d+\sigma+1})(1-Q^{d+1+\sigma/2})
                        (1+Q^{d+1+\sigma/2+\ell})}
 {(1-Q^{d+1-k})(1-Q^{d+k+\sigma+1})
                        (1+Q^{d+1+\sigma/2})^2}.                  \tag{13}
\]
The phase is exactly \(q^{\ell+1}q^{1-\ell}=Q\).
For \(d=k+p\), the first numerator factor splits as
\((1-aQ^p)(1+aQ^p)\), and
\[
 -Q^{k+1+\sigma/2+\ell}=Q^{-L},\qquad
 -b=Q^{k-U}.
                                                                    \tag{14}
\]
Thus (13) is the consecutive-term ratio in (8). The initial term is
\[
 T_k=\frac{q^{k(\ell+1)}}{\mathcal D_k}
                         \frac{S_{U-k}}{S_{U-k-\ell}}.             \tag{15}
\]
Equations (11)--(15) prove (9), including \(L=0\).

For the denominator audit, \(p\le L\le U-k<N\). The exponents in
\((a^2;Q)_p\), when this product is nonempty, range from
\(2k+1+\sigma\) to at most \(k+U+\sigma\le N-2\).
By (14), the exponents in \((-b;Q)_p\) range from \(k-U\) to at
most \(-1\). None is zero modulo \(N\); the ordinary factors
\((Q;Q)_p\) are also nonzero. The remaining sine products have
indices between zero and \(U\). The terminating numerator
\((Q^{-L};Q)_p\) is used only for \(p\le L\); it is not divided by
an expression at its next zero.

Formula (9) does not evaluate the series or remove its phases.
It is an exact finite source for a later coherent analysis, with
the same \((rZ;r)_\ell\), both parities, and terminal row as (1).

## 3. The inverse difference inside the full observation

Keep the original full functional and outside scalar
\[
 \mathcal L_N(P)=
       \phi_N[R_N^3e_MQ_N^{\rm full}P],\qquad
          \frac{1}{\kappa_N^2N}\mathcal L_N(F_N^+),
       \qquad \kappa_N=q^{D^2/2}.                                 \tag{16}
\]
No internal Hermite normal of \(Q_N^{\rm full}\) is changed.
Define ordinary spectral polynomials
\[
 \mathcal T_{j,N}(X)=
 \begin{cases}
 \eta_jT_j(-X/2),&\sigma=0,\\
 1+2\displaystyle\sum_{k=1}^{j}T_k(-X/2),&\sigma=1 .
 \end{cases}                                                       \tag{17}
\]
Interchanging the finite sums in (5) gives exactly
\[
 F_N^+=\sum_{j=0}^{U}h_{j,N}\mathcal T_{j,N},\qquad
 \mathcal L_N(F_N^+)
       =\sum_{j=0}^{U}h_{j,N}\mathcal L_N(\mathcal T_{j,N}).
                                                                    \tag{18}
\]
There is no omitted constant term or far endpoint in this identity.

At odd levels, the second polynomial in (17) is the Dirichlet
polynomial
\[
 \mathcal T_{j,N}(-2\cos u)
       =\frac{\sin((j+1/2)u)}{\sin(u/2)}.
                                                                    \tag{19}
\]
Its apparent poles are removable. The original radical identities
[in the fold theorem, (9)](research_mixed_next_outer_fold_and_inner_source_lift.md)
therefore yield the following exact two-sector formulas:
\[
 e_M(-2\cos u)\mathcal T_{j,N}(-2\cos u)=
 \begin{cases}
 \displaystyle\frac{\eta_j}{2N}
  \{\cos((M+j)u)+\cos((M-j)u)\},&N\ {\rm even},\\[2mm]
 \displaystyle\frac{
  \cos((M+j)u)-\cos((M-1-j)u)}
       {2N\cos^2(\pi/(2N))},&N\ {\rm odd}.
 \end{cases}                                                       \tag{20}
\]
The odd \(\sin(u/2)\) factor cancels exactly before taking any
norm or trace. Equation (20) is an identity of ordinary
polynomials in \(-2\cos u\). It holds at all nodes and for every
Hermite derivative, including the odd simple endpoint. For even
\(j=0\), \(\eta_0=1\) correctly combines the two equal cosines
once. The lower frequencies remain positive through \(j=U\).
Neither sign in (20) has been suppressed.

This proves a dual finite representation of the complete attached
observation, not a bound for either sector separately.

## 4. The complex consecutive ratio and its stationary equation

On the actual outgoing reference family the
[absolute anchor theorem, (8)](research_mixed_next_outgoing_absolute_anchor.md)
proves that all \(C_{b,N}\) in (1) are nonzero and
\[
 \frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}
       =\mathcal L(b/N,Z)\{1+O(N^{-1})\},
                    \qquad M\le b\le D,                           \tag{21}
\]
where \(\mathcal L\) is the selected stable *complex* unsigned
ratio. For the summand
\(A_{d,k,N}=q^{M+d}b_{d,k,N}C_{M+d,N}\) in (4), direct division gives
\[
 \frac{A_{d+1,k,N}}{A_{d,k,N}}
 =q\frac{s_{2d+\sigma+1}s_{2d+\sigma+2}}
          {s_{d+1-k}s_{d+k+\sigma+1}s_{M+d+1}^2}
                    \frac{C_{M+d+1,N}}{C_{M+d,N}}.                 \tag{22}
\]
For \((x,t)=(d/N,k/N)\) in any fixed compact subset of
\(0<t<x<1/2\), (21)--(22) imply, uniformly at both parities,
\[
 \frac{A_{d+1,k,N}}{A_{d,k,N}}
 =\mathcal L(1/2+x,Z)\,
       \frac{\sin^2(\pi x)}
            {\sin^2(\pi x)-\sin^2(\pi t)}
                      \{1+O(N^{-1})\}.                            \tag{23}
\]
Only smooth finite shifts on that compact set were used. At odd
levels this is the ratio in the exact difference source \(h_k\),
not a claimed ratio for its cumulative coefficient \(f_k\).

The original unsigned recurrence
[in the paired-characteristic theorem, (5)--(6)](research_mixed_next_outer_paired_newton_characteristics.md)
has principal characteristic
\[
 (1-Y)^2\mathcal L^2+(3Y-2Y^2-Z)\mathcal L+Y(Y-1)=0,\qquad
           Y=e^{-2\pi i(1/2+x)}.                                  \tag{24}
\]
The complete source has zero cutoff forcing in this recurrence.
The selected root is fixed by (21), not by replacing \(\mathcal L\)
with its modulus.

Setting the principal ratio in (23) equal to one requires
\[
 \mathcal L=1-\frac{\sin^2(\pi t)}{\sin^2(\pi x)}
       =1-\frac{\mathfrak hY}{(1+Y)^2},\qquad
                       \mathfrak h=4\sin^2(\pi t).                 \tag{25}
\]
For \(Y\ne0,-1,1\), substituting this value in (24) is exactly
equivalent to the quartic
\[
 \boxed{\quad
 (1-Z)(1+Y)^4
 -\mathfrak hY(2-Y-Z)(1+Y)^2
 +\mathfrak h^2Y^2(1-Y)^2=0 .
 \quad}                                                           \tag{26}
\]
Indeed the left side of (24) at \(\mathcal L=1\) is \(1-Z\),
and its derivative there is \(2-Y-Z\). Substituting
\(\mathcal L=1-\mathfrak hY/(1+Y)^2\) and clearing that denominator
gives (26) without choosing a root. Conversely every solution of
(26) off those exclusions gives a characteristic root by (25);
agreement with the selected branch remains an additional condition.

The modulus envelope of the positive transition theorem instead
sets
\[
 |\mathcal L|\,
       \frac{\sin^2(\pi x)}
            {\sin^2(\pi x)-\sin^2(\pi t)}=1 .
                                                                    \tag{27}
\]
It does not imply (25). Equations (23)--(26) are a rigorous
principal-ratio reduction of the finite source; they do not assert
an analytic interpolation of \(C_{M+d,N}\) in a complex index,
an admissible contour through any root of (26), or a stationary
phase formula. Such a contour must also retain the endpoints
\(d=k,U\), both sectors in (20), and the exact stops in (9).
The attached signed observation at the geometric reference action
therefore remains unestimated by this note.

## Frozen source bindings

- Positive Chebyshev transition:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Exact reflected Newton source:
  d8b58688c4da4237ac9cc5073fb32e0601d1326aab52dc9d71cee2070618ed48.
- Complete attached source and original scalar:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Original outgoing recurrence and characteristics:
  8372ed7387b7465b6a66cc207f2ac8e3803e3def10d7beff115c038d4334c909.
- Uniform complex finite ratios and absolute anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original action and selected-root normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Exact radical formulas and full Hermite source:
  5aab98669016b0de450270300ca8e678e26c4862b6ba8b9e222cd8110e3f9ed9.
