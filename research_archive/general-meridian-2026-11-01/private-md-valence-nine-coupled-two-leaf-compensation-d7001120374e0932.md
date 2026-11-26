# The valence-nine moving trace inside an actual two-hub contraction

Private proof, 1 November 2026. This is a comparison for one specified
coupled configuration, and a small neighborhood of it. It does not
assert a general higher-valence moving-hub estimate.

## 1. The physical expression and the old coupled pressure

Consider the literal ordered expression
\[
                         C\bigl(h^8 T(h^2)\bigr).
\tag{1}
\]
After consecutive unturned products are grouped, it has a bare hub of
valence nine joined by one physical quarter-turn to a bare trivalent
hub. The other eight incidences at the first hub and the other two
incidences at the second hub are original leaf branches. Thus the
internal edge has equal covariant labels at its two ends. We do not
replace this edge by an unturned edge or by an extra cap.

Write
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(a)=J(2a)-4J(a),\qquad G_0=g(1/4),
\tag{2}
\]
and let \(f_k(b)\) be the original positive coefficient action of the
unturned product \(h^k\), at its ordinary output \(b\). Additive
constants on the ten incoming rigid leaf profiles may be included;
their sum is denoted by \(c\). We first write all formulas with
\(c=0\); adding \(c\) to both sides changes none of the comparisons.

At the complete parameter the exact Frobenius metric and turn are
\(\phi_0(e_i e_j)=\delta_{i+j,d}\) and \(T(e_i)=e_{d-i}\),
where \(d=N-1\). Consequently the complete contraction in (1) is the
positive sum of products of the coefficients of \(h^8\) and \(h^2\)
at the same ordinary output. Its original geometric pressure is
\[
             F_0=\max_{0\le b\le1}\{f_8(b)+f_2(b)\}.
\tag{3}
\]
Equivalently, if the covariant internal label is \(z\), both ordinary
outputs equal \(1-z\). The neighboring two-leaf branch therefore
contributes \(f_2(1-z)\), not \(g(z)\), \(g(1-z)\), or a separately
assigned capped volume. The strict-state theorem applies to the
literal expression (1), so (3) is the original coupled maximum.

The source and pressure comparison below does not require a choice
of knot parity. If it is used for a particular knot presentation,
the original whole-link component and marking conditions must still
be checked; no knot classification follows from (1) alone.

## 2. Inserting the exponential local counterexample

Use the fixed complete Newton polynomials
\[
\begin{gathered}
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_r=\prod_{j=1}^r2\sin(\pi j/N),\qquad
 e_r(v)=S_r^{-2}\prod_{j=0}^{r-1}(c_j-v),\\
 P_s(v)=\mathcal T_N(v)+2\cos(2\pi s),\qquad
 \phi_s(F)=(-1)^dN^2[v^d]\operatorname{rem}_{P_s}F.
\end{gathered}
\tag{4}
\]
For \(N=5a+1\), put \(h=4a\). The central tensor of the
counterexample is
\[
                       \phi_s(e_h e_a^8).
\tag{5}
\]
The exact complete value is \((S_{2a}/S_a^2)^7>0\), and the moving
value can exceed this complete value by an exponential factor. The
proof in
`/private/tmp/md-one-high-admissible-hub-trace-exponential-obstruction.md`
retains all Hermite normals. We do not use or assert a polynomial
comparison of (5) with its complete value.

For the physical type in which the central quotient is moving, the
quarter-turn joins it to a constant opposite-color quotient at the
neighboring cubic tensor. This is the actual six-type transition,
not a choice of two independent moving parameters. The opposite
ordering may change recorded reference phases, but it does not turn
that neighboring quotient into a moving equal-color quotient.

All paired edge factors are retained. In covariant coefficient
coordinates an edge contributes its prescribed
\(\gamma_e H_N(s)/W_h(s)\), where
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_r(s)=\prod_{j=1}^r
   \frac{\sin((j-s)\pi/N)\sin((j+s)\pi/N)}{\sin^2(\pi j/N)}.
\tag{6}
\]
For every fixed \(R<1\), these factors and their inverses have
bounded or polynomial size uniformly on \(|s|\le R\); the exact
typed phases and the one primitive closing factor are subexponential.
They are not removed as algebraic identities.

Here is an absolute bound on (5) that does remain valid. The complete
high polynomial \(e_h\), \(h>d/2\), has polynomial full spectral-jet
norm. Canonical polynomial sup and Chebyshev coefficient norms are
polynomially equivalent to that norm. For the low polynomial \(e_a\),
the corresponding norm is at most
\(\operatorname{poly}(N)\exp\{Ng(a/N)\}\). Ordinary polynomial
multiplication followed by reduction modulo \(P_s\) has only
polynomial cost for this fixed number of factors: Chebyshev folding
is uniform on every fixed parameter disk. The top-coefficient trace
also has polynomial cost. Therefore
\[
 \sup_{|s|\le R}|\phi_s(e_h e_a^8)|
        \le \exp\{N[8g(1/5)+o(1)]\}.
\tag{7}
\]
This is precisely the fixed-valence norm estimate proved in
`notes/actual_main_meridian_source_bounds.md`, Sections 1 and 3.4;
it uses the full polynomial, including the additional moving terms.

The eight actual low leaf coefficients at the first hub contribute
at most another \(8g(1/5)\). At the neighboring constant cubic hub,
the actual output is \((d-h)/N=a/N\). Its two attached leaf
coefficients and positive gate sum have the original profile
\(f_2(a/N)\), uniformly to subexponential factors. In particular,
the internal labels of that two-leaf branch have not been fixed
artificially or replaced by their individual maxima.

It follows that the contribution of the specified central tuple,
after summing the actual neighboring two-leaf branch, is bounded by
\[
       \exp\{N[\mathcal B+o(1)]\},\qquad
       \mathcal B=16g(1/5)+f_2(1/5).
\tag{8}
\]
The estimate applies to the original coefficient-cone majorants,
including physical auxiliary colors and fixed half-twist choices.
For pure complete-color leaves it is their original positive
profile. No quantum lower bound is used.

## 3. A lower bound supplied by a feasible coupled old state

The intrinsic pressure of the unturned eight-leaf product is
\[
       \max_{0\le b\le1/2}\{f_8(b)+g(b)\}=16G_0.
\tag{9}
\]
This is the old positive Newton evaluation identity, as recorded in
`notes/actual_main_meridian_source_bounds.md`, (H6) and (H10).
Its maximizing output can also be read directly from the strict
response equations. At intrinsic \(X=1\), an individual leaf has
\((B,Y)=(1,1)\). The unturned product law gives
\((B,Y)=(1/k,1/k)\) for a product of \(k\) leaves. Thus for \(k=8\),
\[
                b_8=\frac{\arctan8}{\pi}<\frac12,
                \qquad f_8(b_8)+g(b_8)=16G_0.
\tag{10}
\]
The original product-response inequality shows that \(f_8\) is
increasing on \([0,1/2]\). Hence evaluating the *coupled* pressure
(3) at \(b=1/2\) gives
\[
          F_0\ge f_8(1/2)+f_2(1/2)
             \ge16G_0-g(b_8)+f_2(1/2).
\tag{11}
\]
Only a feasible state of the original two-hub contraction is used
here. Formula (9) supplies a value of its actual branch profile;
the probe appearing in (9) is not added to the link in (1).

## 4. Elementary strict constants

Differentiating (2) gives \(g'(a)=2\log\cot\pi a\). Put
\(\delta=\arctan(1/8)\), so \(b_8=1/2-\delta/\pi\). Then
\[
\begin{split}
 g(b_8)
  &=\frac2\pi\int_0^\delta-\log\tan u\,du\\
  &\le\frac{2\delta}{\pi}(1-\log\delta)
   <\frac{1+\log8}{4\pi}<\frac14.
\end{split}
\tag{12}
\]
Here \(\tan u\ge u\), \(\delta<1/8\), and
\(u(1-\log u)\) is increasing for \(0<u<1\). The last bound uses
\(\log2<7/10\) and \(\pi>31/10\). The logarithm inequality follows
already by summing the first five nonnegative terms of
\(e^{7/10}\); the bound for \(\pi\) follows, for example, from
the perimeter of an inscribed regular twelve-gon.

For the genuine two-leaf profile, the exact positive response is
\[
 f_2'(b)=2\log(2X_2(b)^2),\qquad
 X_2(b)=\frac{\cot\pi b+\sqrt{\cot^2\pi b+2}}2.
\tag{13}
\]
This derivative decreases to zero at half. Integrate only over
\([1/5,1/4]\) and \([1/4,1/3]\), discarding the remaining positive
integral. At their right endpoints,
\(2X_2(1/4)^2=2+\sqrt3>7/2\) and
\(2X_2(1/3)^2=(4+\sqrt7)/3>11/5\). Consequently
\[
\begin{split}
 f_2(1/2)-f_2(1/5)
 &>\frac1{10}\log\frac72+\frac16\log\frac{11}5\\
 &>\frac18+\frac{201}{1536}
   =\frac{131}{512}.
\end{split}
\tag{14}
\]
Both rational logarithm bounds are direct. The positive expansion
\(\log((1+t)/(1-t))=2\sum_{j\ge0}t^{2j+1}/(2j+1)\)
at \(t=5/9\), through \(j=3\), gives
\(\log(7/2)>41893120/33480783>5/4\). At \(t=3/8\), through
\(j=1\), it gives \(\log(11/5)>201/256\).

Combine (8), (11), (12), and (14). Since \(g\) has its strict
maximum at \(1/4\),
\[
 \boxed{\quad
 F_0-\mathcal B
  >16\{G_0-g(1/5)\}+\frac3{512}
  >\frac3{512}.
 \quad}
\tag{15}
\]
All inequalities are at the original level-independent action scale.
No numerical optimization or guessed hyperbolic volume is used.

## 5. Uniform neighborhood and the exact limitation

The same absolute norm argument applies when the central high label
is \(z\) near \(4/5\) and its eight low labels are
\(u_1,\ldots,u_8\) near \(1/5\). Its attached-branch upper rate is
\[
               2\sum_{i=1}^8g(u_i)+f_2(1-z).
\tag{16}
\]
The high label remains above half and the eight low labels remain
below half. By continuity and (15), a fixed closed neighborhood has
rate strictly below \(F_0\), uniformly at both parities and on every
fixed disk \(|s|\le R<1\), after its polynomial factors are absorbed.
Summing all such grid tuples costs only a polynomial factor. Thus the
compensation is not confined to the exact pair-equality sequence.

The counterexample remains an exponential failure of a local
moving/complete trace comparison. What (15) proves is that its loss
of that pointwise bound does not overwhelm the actual coupled
geometric budget in the specific expression (1). This does not
control all index configurations of (1), an arbitrary attached
type-A profile, or an arbitrary higher-valence bare component.
The moving whole-hub problem therefore remains separate from the
proved simultaneous-half comparison for old whole-hub pressures.
