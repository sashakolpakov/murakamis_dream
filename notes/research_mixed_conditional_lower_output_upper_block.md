# The complete upper conditional block at lower outgoing height

Research deduction, 8 November 2026. The entire physical upper half
of the original type-four conditional kernel has a uniform bound on
the outgoing unit disk. Multiplied by the complete first cap, its
rate is strictly below \(25/16\) on the full incoming rectangle
\([1/2,7/10]-i[0,9/125]\). The original ordinary-next supporting
plane then pays this block on the whole unselected outgoing plateau,
including when the incoming path is vertical.

This is a bound for an actual finite-source group. It does not assert
that these rows lie below the conditional kernel's moving critical
action, and it does not continue a conditional packet to lower
outgoing height. No numerical evaluation or frozen-source edit is used.

## 1. Source and exact reflected rate

Keep the original definitions
\[
 r=e^{-2\pi i/N},\quad D=N-1,\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,
\]
\[
 \begin{split}
 a&=x-i\eta,\qquad \frac12\le x\le\frac7{10},
                         \quad0\le\eta\le\frac9{125},\\
 X&=e^{-2\pi ia},\quad \rho=|X|=e^{-2\pi\eta},
                         \quad\delta=2\pi\eta,\\
 C^{\rm up}_{1,N}(X,Y)
   &=\sum_{j=\lceil N/2\rceil}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 U_{0,N}(w,X)
   &=\sum_{k=0}^{N-1}
       H_N(w,r^{-k})\,p_k(X)/P_k .
 \end{split}                                                     \tag{1}
\]
Each \(H_N\) is the complete original endpoint coefficient. In
particular, it is not replaced by a positive sum of its private
Newton terms. No physical termination rule is imposed at a
continuous \(X\) or \(Y\).

For \(0\le R\le1\), write
\[
 f_R(s)=\log|1-Re^{-2\pi is}|,\qquad
 A_R(z,v)=\int_{z-v}^{z}f_R(s)\,ds,\qquad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds .
                                                               \tag{2}
\]
All integrable zeros use their continuous integral limits. If
\(Y=R e^{-2\pi iz}\), its angle \(z\) may be arbitrary. The complete
absolute physical-row rate at \(t=j/N\) is
\[
 E(t)=\delta t+\int_0^t f_\rho(x+s)\,ds
                    +\int_0^t f_R(z+s)\,ds-3J(t).
                                                               \tag{3}
\]
Both radial logarithms have period mean zero. Therefore, with
\(v=1-t\),
\[
 E(1-v)=\delta(1-v)-A_\rho(x,v)-A_R(z,v)+3J(v).
                                                               \tag{4}
\]
In particular \(E(1)=\delta\). This is a continuous endpoint rate;
there is no new finite row \(j=N\). Equation (4) retains the exact
incoming factor \(X^{-j}\).

## 2. A whole-disk bound for every upper row

The incoming complementary-arc inequality
\[
 A_\rho(x,v)\ge0,\qquad
 \frac12\le x\le\frac7{10},\quad0\le v\le\frac12,
                                                               \tag{5}
\]
is [the upper-tail theorem, Lemma 1](research_mixed_conditional_negative_height_upper_tail.md).
Its proof uses only \(0<\rho\le1\), and has no outgoing-height
hypothesis. For \(v\le1/5\), the incoming arc lies in
\([3/10,7/10]\), where \(f_\rho\ge0\). For \(v\ge1/5\),
the arc is minimized at \(x=1/2\) or \(x=1/2+v\); symmetry
and the zero half-period mean give the same nonnegative value
at those two endpoints. This includes the possible numerator zeros.

The outgoing inequality needed here has the opposite radial
direction from the former positive-height application:
\[
                         A_R(z,v)\ge2J(v/2)
             \qquad(0\le R\le1,\ 0\le v\le1/2).
                                                               \tag{6}
\]
Indeed \(f_R\) is even and increases with distance from an integer
up to one half. Among arcs of fixed length \(v\), its minimum
is the centered arc. Put
\[
 B_R(v)=\int_{-v/2}^{v/2}f_R(s)\,ds.
 \]
For \(0<R<1\), the convergent Fourier series, differentiated in
\(R\), gives
\[
 \partial_R B_R(v)=
       \frac{1}{\pi R}\Arg(1-Re^{i\pi v})\le0.
                                                               \tag{7}
\]
The argument is the continuous principal argument, lying in
\((-\pi/2,0]\). Thus \(B_R(v)\ge B_1(v)=2J(v/2)\).
Continuity gives both radial endpoints, including \(R=0\).
This proves (6) for every outgoing angle, not just the plateau.

Set
\[
                         D(v)=3J(v)-2J(v/2).
                                                               \tag{8}
\]
Equations (4)--(6) imply
\[
                  E(1-v)\le\delta(1-v)+D(v).
                                                               \tag{9}
\]
The scalar properties used in
[the upper-tail proof, Section 3](research_mixed_conditional_negative_height_upper_tail.md)
and [the upper-half proof, Section 2](research_mixed_conditional_negative_height_upper_half.md)
are
\[
 \begin{split}
 D(v)&\le0&& (0\le v\le1/3),\\
 D'(v)&>1&& (1/3\le v\le1/2).
 \end{split}                                                    \tag{10}
\]
For clarity, \(D(0)=D(1/3)=0\); the second equality follows
from sine duplication. Also
\[
 D''(v)=\frac{\pi(5\cos\pi v-1)}{2\sin\pi v}>0
                         \quad(0<v\le1/3),
 \]
which proves the first assertion. On the remaining interval,
\[
 e^{D'(v)}=
       \frac{(2\sin\pi v)^3}{2\sin(\pi v/2)}
 \]
increases and then decreases. Its endpoint values are
\(3\sqrt3>5\) and \(4\sqrt2>5\). Hence \(D'>\log5>1\),
using \(e<3\).

Since \(\delta\le18\pi/125<1/2\), (9)--(10) give
\[
 \sup_{1/2\le t\le1}E(t)
 \le\max\{\delta,\ \delta/2-2J(1/4)\}
 <\frac7{24}+\frac{9\pi}{125}
 <\frac{10877}{21000}.
                                                               \tag{11}
\]
Here \(-J(1/4)<7/48\) is the existing written scalar inequality
in [the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md),
also recorded in
[the far incoming-arc comparison, Section 2](research_mixed_next_far_incoming_arc_comparison.md).
The last comparison uses \(\pi<22/7\). The first alternative
\(\delta\) also obeys the displayed strict ceiling because
\(9\pi/125<7/24\).

The zero-safe shifted-product upper bounds and the uniform
sine-factorial estimate now yield, for every \(\tau>0\),
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}
       \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\tau N^{A_\tau}
       \exp N\left\{\frac7{24}+\frac{9\pi}{125}+\tau\right\},
              \qquad |Y|\le1 .
                                                               \tag{12}
\]
The finite estimates are the same ones used in
[the original all-row bounds, Section 2](research_mixed_boundary_strip_bounds.md).
In a numerator logarithm, truncation below \(-\log N\) has
total variation \(O(\log N)\) and changes the integral by
\(O(1/N)\), uniformly in the angular shift and in the closed
radial disk. The shifted Riemann upper error is therefore
\(O(\log N)\). For the denominator,
\(\log|P_j|=NJ(j/N)+O(\log N)\) uniformly up to both ends.
The original carrier in (3) is exact. Thus (12) retains all
upper rows, every zero, and both level parities. It also bounds
every positive subset of the displayed rows.

## 3. Multiplication by the complete cap

The complete physical coefficient and true-end bounds give
\[
 \sup_{w\in[-2,2]}|U_{0,N}(w,X)|
       \le C_\tau N^{A_\tau}
             e^{N(1549/1500+\tau)}
                                                               \tag{13}
\]
on the entire incoming rectangle in (1). This is the positive
physical-source consequence of
[negative-depth cap transport, equations (3)--(6)](research_mixed_cap_negative_depth_positive_transport.md):
for \(e\le1/2\), the rate is at most
\(\lambda(e)-J(1/2-e)<1549/1500\); for \(e\ge1/2\),
it is at most \(\lambda(e)+J(e)<101/125\).
Those radial inequalities hold for all \(1/2\le x\le1\) and
\(0<|X|\le1\), although that note's stronger decreasing bound
has a shorter angular range. The two true private ends are
separately bounded by \(3/5\), as in
[all-real complementary completion, Section 2](research_mixed_three_four_complementary_real_colors.md).
No extrapolation of a coherent signed bound to a partial cap
source is made.

Combining (12)--(13) proves the whole-disk estimate
\[
 \begin{split}
 &|U_{0,N}(w,X)|
       \sum_{j=\lceil N/2\rceil}^{N-1}
          \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                 \exp N\left\{\frac{32563}{21000}+\tau\right\},
                     \qquad |Y|\le1 .
 \end{split}                                                    \tag{14}
\]
The useful reserve is explicit:
\[
                  \frac{25}{16}-\frac{32563}{21000}
                             =\frac{499}{42000}>0.
                                                               \tag{15}
\]
Consequently \(U_{0,N}(w,X)C^{\rm up}_{1,N}(X,Y)\), as
an actual polynomial of degree at most \(D\) in \(Y\), has
a uniform disk rate strictly below \(25/16\). The same
statement holds after integration in \(a\) over any fixed
bounded-length chain in the rectangle, with the original
factor \(N\,da\). A factor \(N\) costs only a power.

## 4. The actual ordinary-next unselected insertion

Use exactly the ordinary-next references, variables, action,
marginals and independent outgoing plateau of
[paired localization, Section 2](research_mixed_next_low_cardinal_paired_localization.md):
\[
 \begin{gathered}
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
       \qquad(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\\
 P=[.22,.45],\quad h_*=\Im y_*\in(-.102,-.001),\quad
 y=q+ih_*,\quad z=u+i\Im z_*,\quad q,u\in P,\quad
 Z=e^{-2\pi iz},\quad \beta\in\{0,1\}.
 \end{gathered}                                                 \tag{16}
\]
The incoming variable \(a\) in (1) remains independent of
the real target \(q\) in (16). Let \(B_3(q,u)\) be the
original complete third-factor plane, and let
\[
 A_*=\Re\{\mathcal P_{34}(-2,y_*)-g(y_*)/2\},\quad
 \alpha=\Re y_*,\quad
 p=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\}.
 \]
That source proves
\[
 \begin{split}
 |d_N(Y)|^{1/2}
       &\le \operatorname{poly}(N)e^{N(-J(q)/2+\tau)},\\
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
       &\le \operatorname{poly}(N)e^{N(B_3(q,u)+\tau)},\\
 A_*+p(q-\alpha)+B_3(q,u)&\le\Lambda_{123}(z),\qquad
 A_*>\frac74+\frac{819}{35200}.
 \end{split}                                                    \tag{17}
\]
These are complete finite-source bounds. The first keeps both
the factorial and forcing alternatives of the true Fourier
polynomial, and the second retains all rows and currents of
the actual ordinary third block.

The marginal estimates in the same source give
\[
 -J(q)/2-p(q-\alpha)
 \le
 \begin{cases}
 11/80,&p\le0,\\
 1/12+801/10000,&p\ge0 .
 \end{cases}                                                    \tag{18}
\]
For \(p\le0\), replacing the prefix rate by \(25/16\)
leaves a gap greater than
\[
                 \frac74-\frac{25}{16}-\frac{11}{80}
                             =\frac1{20}.
 \]
For \(p\ge0\), use \(819/35200>1/50\); the remaining
gap is greater than
\[
 \frac74+\frac1{50}
        -\frac{25}{16}-\frac1{12}-\frac{801}{10000}
       =\frac{661}{15000}>\frac1{25}.
                                                               \tag{19}
\]
Together with (14)--(17), this proves the actual bound
\[
 \begin{split}
 &|U_{0,N}(w,X)|
   \sum_{j=\lceil N/2\rceil}^{N-1}
     \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
   |d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{13mm}\le C_\tau N^{A_\tau}
       e^{N\{\Lambda_{123}(z)-1/25+\tau\}} .
 \end{split}                                                    \tag{20}
\]
It holds throughout the complete incoming rectangle (1), the
independent unselected plateau (16), and all real ordinary
colors. Thus the upper physical block is paid along both the
far incoming real arc and its whole original initial vertical
connector. Arbitrary positive subsets of its rows are paid as
well. No individual row is recovered from a signed finite sum.

## 5. Normalization, fixed jets, and the remaining source

The original first integration has measure \(N\,da\); the next
integration has measure \(N\,dy\). Multiplying (20) by these
factors and integrating on fixed finite chains preserves the
gap after absorbing polynomial costs. Nothing has been divided
by an endpoint coefficient or by a Fourier polynomial on an
independent plateau.

At the actual \(z_*\), the original normalization is
\[
 \Lambda_{123}(z_*)=
       \Re\mathcal P_\beta^+(-2,z_*)-\frac\beta2\Re g(z_*).
                                                               \tag{21}
\]
For \(\beta=1\), the established nonzero factorial packet for
\(d_N(Z)\) near the actual \(z_*\in O_4\) removes the displayed
outgoing halfweight exactly as in paired localization, Section 3.
For \(\beta=0\), no outgoing factor is inserted. Hence the
unweighted upper-block contribution, normalized by the original
next conditional action, has gap \(1/100\) on sufficiently
small fixed ordinary-color and actual-output neighborhoods.
All fixed normalized mixed derivatives have the same weakened
gap on smaller neighborhoods.

To justify this local scope, retain the fixed physical index set
in (1). The integrated logarithmic upper rates are jointly
continuous through their zeros; the finite product bounds admit
arbitrarily small exponential tolerances. The all-real complete
cap bounds admit the original local ordinary-color extension.
Thus the fixed compact parameter sets in (14), (20) have small
complex neighborhoods with the same strict margins after a
prescribed debit. Cauchy's formula applies to the original
holomorphic unweighted source after (21), with paths, endpoints,
and row sets held fixed at the base reference. The even half row
and the first odd row above it remain included.

This theorem removes the complete upper physical half of the
troublesome first conditional block from the ordinary-next
unselected source. It leaves the retained lower conditional
rows, their main integral and unweighted connectors at negative
outgoing height. It does not pay the rest of the lower period,
assert a whole next transfer, or promote this independent
ordinary reference argument to a terminal family.
