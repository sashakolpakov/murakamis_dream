# A whole moving trace can exceed its complete-admissible trace exponentially

1 November 2026. Private mathematical derivation; no repository changes.

The proposed comparison
\[
 \left|\phi_{N,s}\!\left(\prod_{\nu=1}^{B}e_{i_\nu}\right)\right|
 \le N^{C_R}\,
       \phi_{N,0}\!\left(\prod_{\nu=1}^{B}e_{i_\nu}\right)
 \tag{1}
\]
does not hold uniformly on complete-admissible tuples, even for a fixed number of factors. The same is true with a uniform \(e^{o(N)}\) factor. This note gives an exact fixed-valence family and an elementary finite exponential lower bound. No numerical observation or saddle approximation is used.

The family has one high Newton index and eight low indices. All pair sums are at most \(d=N-1\), the total is at least \(d\), and the complete trace is strictly positive. It lies on some pair-sum boundary faces; no assertion about a fixed strictly interior geometric window is made.

## 1. Exact algebra and a cardinal polynomial

Put \(q=e^{\pi i/N}\), \(d=N-1\), and
\[
 S_r=\prod_{j=1}^{r}2\sin(\pi j/N),\qquad
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_r(z)=S_r^{-2}\prod_{j=0}^{r-1}(c_j-z).
 \tag{2}
\]
Let \(\mathsf T_N\) be the monic Chebyshev polynomial with
\(\mathsf T_N(u+u^{-1})=u^N+u^{-N}\). The exact relations and coefficient trace are
\[
 \begin{split}
 P_0(z)&=\mathsf T_N(z)+2=\prod_{j=0}^{d}(z-c_j),\\
 P_s(z)&=P_0(z)+\Delta_s,\qquad
          \Delta_s=2\cos(2\pi s)-2,\\
 \phi_{N,s}(F)&=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \end{split}
 \tag{3}
\]
Polynomial reduction retains the repeated-root normals.

Choose \(0\le a<d/2\), and set \(h=d-a\). Reflection gives
\(c_j=c_{d-j}\) and \(S_aS_h=N\). Comparing roots, multiplicities, and leading coefficients proves
\[
 e_h(z)e_a(z)=\frac{(-1)^d}{N^2}\frac{P_0(z)}{z-c_a}.
 \tag{4}
\]
The right side is a polynomial. For any polynomial \(F\), put
\[
 F(z)=F(c_a)+(z-c_a)G(z).
 \tag{5}
\]
Using \(P_0=P_s-\Delta_s\), exact reduction gives
\[
 \phi_{N,s}(e_he_aF)
       =F(c_a)-\frac{(-1)^d\Delta_s}{N^2}\phi_{N,s}(G).
 \tag{6}
\]
Here \(\phi_{N,s}(e_he_a)=1\) at every parameter because its degree is \(d\). No division by \(\Delta_s\) or loss of repeated-root data occurs.

## 2. A fixed-valence admissible family

For each integer \(a\ge2\), take
\[
 N=5a+1,\qquad d=5a,\qquad h=4a,\qquad
 \mathcal P_a(z)=e_{4a}(z)e_a(z)^8.
 \tag{7}
\]
There are nine factors. Their pair sums are \(h+a=d\) or \(2a<d\), and the total degree is \(12a\ge d\). Every small index is low; \(h\) is high. Apply (6) with \(F=e_a^7\).

Write \(c=c_a\) and define
\[
 Q_a(y)=\frac{e_a(-y)^7-e_a(c)^7}{y+c}.
 \tag{8}
\]
This is a polynomial of degree \(7a-1\), and \(G(z)=-Q_a(-z)\).
Since \((2a+1)/(5a+1)<1/2\), one has \(c>0\). Also \(c_r>c\) for \(r<a\). With \(v=y+c\),
\[
 e_a(-y)^7=S_a^{-14}
             \prod_{r=0}^{a-1}\{v+(c_r-c)\}^{7}.
 \tag{9}
\]
Every coefficient in \(v\) is positive. Subtracting its constant and dividing by \(v\) shows that \(Q_a\) has nonnegative coefficients in \(v\), hence in \(y\). In particular,
\[
 Q_a(y)-S_a^{-14}(y+c)^{7a-1}
       \quad\text{has nonnegative coefficients in }y.
 \tag{10}
\]
This coefficient inequality does not assert positivity of the moving trace on arbitrary inputs.

## 3. The single Fourier difference

Expand
\[
 Q_a(u+u^{-1})=\sum_k b_k u^k,\qquad
 D_a=b_{N-1}-b_{N+1}.
 \tag{11}
\]
For every nonnegative integer \(j\), the two-step tail difference of
\((u+u^{-1})^j\) at a nonnegative frequency \(k\) is nonnegative. Where parity and support allow it, the difference is
\[
 {j\choose(j-k)/2}-{j\choose(j-k)/2-1}\ge0;
 \tag{12}
\]
otherwise both coefficients, or the second one, vanish. Thus every polynomial with nonnegative coefficients in \(y\), evaluated at \(y=u+u^{-1}\), has these nonnegative differences.

The degree satisfies
\[
             N-1\le7a-1<2N-1.
 \tag{13}
\]
The exact Fourier trace of \(Q_a(-z)\) therefore contains only its first alias, whose multiplier is \(U_0=1\), at both parities. Consequently
\[
 \phi_{N,s}\bigl(Q_a(-z)\bigr)=N^{2}D_a.
 \tag{14}
\]
for every \(s\). Equivalently, first use invariance of the top trace below degree \(2N-1\), then the complete single-alias formula. No higher alias has been omitted.

The coefficient of \(y^{7a-2}\) in the displayed summand of (10) is
\((7a-1)c/S_a^{14}\). Since \(N-1=5a\), its contribution to (11) is
\[
 \frac{(7a-1)c}{S_a^{14}}
 \left\{{7a-2\choose a-1}-{7a-2\choose a-2}\right\}.
 \tag{15}
\]
All remaining monomial contributions are nonnegative. The braces are a positive integer, so
\[
 D_a\ge
 \frac{(7a-1)c}{S_a^{14}}
 \left\{{7a-2\choose a-1}-{7a-2\choose a-2}\right\}
 \ge\frac{(7a-1)c}{S_a^{14}}>0.
 \tag{16}
\]
Equations (6), (8), and (14) now give the entire moving trace:
\[
 \boxed{\;
 \phi_{N,s}(\mathcal P_a)
       =e_a(c)^7+(-1)^d\Delta_s D_a.
 \;}
 \tag{17}
\]
All return contributions have been combined. The trace is affine in \(\Delta_s\), and the sign is the original coefficient-trace sign.

## 4. A finite exponential ratio

The identity
\(c_r-c_a=4\sin((a+r+1)\pi/N)\sin((a-r)\pi/N)\)
gives
\[
 e_a(c_a)=\frac{S_{2a}}{S_a^2}.
 \tag{18}
\]
Thus
\[
 \phi_{N,0}(\mathcal P_a)=
       \left(\frac{S_{2a}}{S_a^2}\right)^7>0,\qquad
 \frac{D_a}{\phi_{N,0}(\mathcal P_a)}
       \ge\frac{(7a-1)c_a}{S_{2a}^{7}}.
 \tag{19}
\]
Set \(L=2\sin(2\pi/5)>1\). Exact reflection at \(N=5a+1\) gives
\[
 S_{2a}S_{3a}=N,\qquad
 \frac{S_{3a}}{S_{2a}}
   =\prod_{r=2a+1}^{3a}2\sin(\pi r/N)\ge L^a.
 \tag{20}
\]
Each \(r/N\) in this product lies in \((2/5,3/5)\). Hence
\[
 S_{2a}^{-7}\ge N^{-7/2}L^{7a/2}.
 \tag{21}
\]
The numbers \(c_a\) increase from the positive value
\(c_*=2\cos(5\pi/11)\) at \(a=2\). Therefore
\[
 \boxed{\;
 \frac{D_a}{\phi_{N,0}(\mathcal P_a)}
       \ge (7a-1)c_*N^{-7/2}L^{7a/2}.
 \;}
 \tag{22}
\]
This bound is finite and elementary. In particular,
\[
 \liminf_{a\to\infty}\frac1{5a+1}
       \log\frac{D_a}{\phi_{N,0}(\mathcal P_a)}
       \ge\frac7{10}\log L>0.
 \tag{23}
\]
The usual closed sine-factorial rate gives the stronger bound
\(-7J(2/5)>0\) from (19), but is not needed here.

For every fixed nonzero \(s_0\) with \(|s_0|<1\),
\(\Delta_{s_0}\ne0\). By (17),
\[
 \frac{|\phi_{N,s_0}(\mathcal P_a)|}
      {\phi_{N,0}(\mathcal P_a)}
 \ge |\Delta_{s_0}|\frac{D_a}{\phi_{N,0}(\mathcal P_a)}-1.
 \tag{24}
\]
The ratio therefore grows exponentially through both parities. If desired, at odd levels take imaginary \(s_0\), so both terms in (17) are positive; at even levels take real \(s_0\in(0,1)\). Neither parity-specific choice is needed for (24).

For any fixed radius \(R>0\), select a nonzero \(s_0\) in its disk. Equations (22)–(24) disprove both the polynomial and subexponential uniform comparison. At radius zero there is only the complete identity.

## 5. Scope of the obstruction

This is a whole-trace failure with a positive complete denominator and the exact repeated-root normalization. Summing the return terms first does not restore pointwise domination on every complete-admissible tuple. Uniformly bounded paired turn or carrier factors cannot remove its exponential ratio.

The tuple lies on pair-sum boundary faces and has one high exterior index. It does not contradict the all-low theorem, any fixed strictly interior regular-window result, the trivalent component comparison, or the established whole-source estimates. A full physical contraction may suppress these states or retain additional correlations and cancellations. No invariant or knot-volume counterexample follows.

A higher-valence extension therefore needs the actual coupled geometric budget or a more restrictive source-selected class of tuples. The complete-admissible pointwise denominator alone cannot be the induction invariant.

## 6. Exact input references

The fixed basis, moving relation, coefficient trace and Fourier identity are those of notes/actual_main_meridian_source_bounds.md, Sections 1–2, and notes/actual_main_meridian_newton_compiler.md. The retained turn factors are those of notes/actual_main_meridian_turn_comparison.md. None of their analytic bounds is used to prove this counterexample.
