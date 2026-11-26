# Full real incoming colors in the complete and coupled column bounds

Private finite-source deduction, 10 November 2026. The complete
one-crossing column and its coupled three-crossing continuation admit
their original sharp upper rates for every real incoming color.
They also retain a fixed angular loss. The two true index-end groups
are bounded directly; no interior cap packet is extrapolated to
either index endpoint. Consequently the already controlled low and
far right outer path is controlled for both entire real incoming
intervals, and on fixed complex neighborhoods of those intervals.

This note does not assemble the entire outer complement or assert a
whole-knot conclusion. No mathematical numerical evaluation is used.

## 1. Exact columns and the theorem

Use the original notation
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad \kappa=q^{D^2/2},\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w),\qquad
 \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T,\\
 M_{j\ell}=\kappa(-1)^jq^{j(\ell+1)}
               \frac{S_j}{S_\ell S_{j-\ell}}\quad(0\le\ell\le j<N),
 \qquad (J_Nv)_i=v_{D-i}.
\end{gathered}                                                     \tag{1}
\]
Entries of \(M\) outside the indicated triangle are zero. The
complete column is exactly
\[
 \begin{split}
 C_{j,N}(w)&=\sum_{\ell=0}^j
       \frac{q^{j\ell}e_\ell(w)}{S_\ell S_{j-\ell}},\\
 (M\mathbf e(w))_j&=\kappa(-q)^jS_j C_{j,N}(w).
 \end{split}                                                       \tag{2}
\]
All original rows occur. In particular this is not a column with
an intervening reversal or an additional prepared source.

Keep the calibrated cap action of the
[complete-column theorem](research_mixed_symmetric_closing_complete_column_norm.md):
\[
\begin{gathered}
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad b_2=-4J(1/4),\\
 F(s,z)=-2J(1/2-z)-3J(z)-J(s-z)+i\pi sz,\\
 z_c(s)=\pi^{-1}\arctan\frac{i+\sqrt{1-2e^{2\pi is}}}{2},\qquad
 f(s)=\Re F(s,z_c(s))+J(s),\\
 \lambda_*=f(1/2),\qquad \sigma_*=b_2+\lambda_*-1/19,\qquad
 d(\theta)=1-\cos\theta .
\end{gathered}                                                     \tag{3}
\]
Every branch in (3) is the one in that source. In particular its
written bounds give
\[
 f(s)\le\lambda_*,\quad
 b_2+1/9<\lambda_*<175/216,\quad
 56/99<b_2<7/12.                                                   \tag{4}
\]

**Theorem 1.** There are \(c>0,C,A\), independent of level parity,
such that for every \(-\pi\le\theta\le\pi\),
\[
\boxed{\quad
 \begin{split}
 \|M\mathbf e(-2\cos\theta)\|_2
      &\le CN^A e^{N(\lambda_*-c d(\theta))},\\
 \|M^3\mathbf e(-2\cos\theta)\|_2
      &\le CN^A e^{N(\sigma_*-c d(\theta))}.
 \end{split}
 \quad}                                                          \tag{5}
\]
Every fixed ordinary incoming derivative has the same angular
exponent, at polynomial cost, including both real spectral endpoints.
For each prescribed \(\tau>0\), there is a fixed filled ellipse
containing \([-2,2]\) in its interior on which the respective
upper rates are \(\lambda_*+\tau\) and \(\sigma_*+\tau\).
Fixed ordinary derivatives have those rates on a smaller fixed
neighborhood of the entire real interval.

Only upper bounds are asserted for variable real incoming color.
The nonzero norm asymptotic at \(-2\) from the complete-column
theorem is unchanged and is not extended to other colors.

## 2. The compact physical rows, with their full cap source

Set \(\delta_0=1/100\). On the fixed compact interval
\(I=[\delta_0,1-\delta_0]\), Theorem 1 of the
[real outside-color theorem](research_mixed_endpoint_real_color_decay.md)
gives
\[
 |C_{j,N}(-2\cos\theta)|
   \le CN^A\exp N\{\Re F(j/N,z_c(j/N))-c_I d(\theta)\},
 \qquad j/N\in I,\quad c_I>0.                                    \tag{6}
\]
Its physical source is precisely (2): at \(s=j/N\), the
canonical reciprocal factorial vanishes on \(\ell>j\), and
on \(\ell\le j\) its denominator is \(S_{j-\ell}\).
The phase \(e^{i\pi s\ell}\) is exactly \(q^{j\ell}\).
Thus no different polynomial or physical-index continuation has
been substituted.

For clarity, the full-real statement in (6) is the separate
compact-physical-interval assertion of that theorem, not its
smaller complex index rectangle. Its proof inserts the reflected
factorial boundary loss on the actual compact wire contours,
retains both aliases and all vertical currents, and uses only
\(V_\theta(x)\le0\) for revived upper-half Newton rows. It does
not assume that the complete-color negative entropy dominates
all real colors above the half index. No cap statement at
\(s=0\) or \(s=1\) is used here.

The original uniform sine-factorial bound, together with (2),
therefore gives
\[
 |(M\mathbf e(-2\cos\theta))_j|
       \le CN^A e^{N\{f(j/N)-c_I d(\theta)\}}
                         \qquad(j/N\in I).                       \tag{7}
\]

## 3. Both actual endpoint groups for all real incoming colors

The elementary endpoint witnesses in Section 3 of the
complete-column theorem give
\[
 -J(\delta_0)<1/25,\qquad \log2<1,
 \qquad \log S_j=NJ(j/N)+O(\log N)
                                      \quad(0\le j<N).            \tag{8}
\]
The last estimate includes zero. For every \(w\in[-2,2]\),
the literal product satisfies
\[
                  |e_\ell(w)|\le4^\ell/S_\ell^2,                 \tag{9}
\]
because each real factor \(|c_\nu-w|\le4\).
If \(j/N=s\le\delta_0\), then \(S_j\le1\), so (2) gives
\[
 |(M\mathbf e(w))_j|
        \le\sum_{\ell=0}^j
                  \frac{4^\ell}{S_\ell^3S_{j-\ell}}
        \le CN^A e^{9N/50}.                                     \tag{10}
\]
Indeed \(J\) decreases on \([0,\delta_0]\); the upper rate
of each summand is at most \(2s\log2-4J(s)<9/50\), by (8).
This is the original small-index proof, now justified directly
for all real incoming colors rather than only \(-2\).

At the other endpoint put \(k=D-j\). The exact identity
\(S_{D-r}=N/S_r\) yields
\[
 S_j C_{j,N}(w)=\frac1{S_k}
       \sum_{\ell=0}^j q^{j\ell}e_\ell(w)
                              \frac{S_{k+\ell}}{S_\ell}.         \tag{11}
\]
Here \(k+\ell\le D\) throughout. The ratio in (11) is a
product of \(k\) positive sine factors, each at most two.
The [all-row real Newton bound](research_mixed_newton_color_tubes.md),
equations (4)--(5), gives
\[
 \sup_{w\in[-2,2]}\sum_{\ell=0}^{D}|e_\ell(w)|
                                      \le CN^A e^{Nb_2}.          \tag{12}
\]
On the lower half this uses \(V_\theta\le V_0\le b_2\),
and on the upper half it uses \(V_\theta\le0\). It does not
replace an absolute value by the signed complete-color sum.
Consequently (8),(11),(12) prove
\[
 |(M\mathbf e(w))_j|
     \le \frac{2^k}{S_k}CN^A e^{Nb_2}
     \le CN^{A'}e^{N(b_2+1/20)}
                    \qquad(k/N\le\delta_0).                     \tag{13}
\]
This includes \(k=0\), every odd-level zero and all upper
indices. No quotient by a Newton value is taken.

Every original row lies in (10), (13), or the compact interval
of (7). Indeed outside the two endpoint groups,
\(\delta_0<j/N<1-\delta_0-1/N\).
Both endpoint rates in (10),(13) are strictly below
\(\lambda_*-1/120\), by (4). Taking
\[
                     0<c\le\min\{c_I,1/240\}                    \tag{14}
\]
and using \(d(\theta)\le2\), (7), (10), and (13) prove
the first bound in (5), after summing at most \(N\) squared
coordinates. These endpoint estimates hold at both parities
without changing a physical stop.

## 4. The coupled column keeps its \(1/19\) loss

The exact original supported matrix is
\[
 (J_NM^2)_{ij}
 =Nq^{(i-j)^2}
       \frac{(q^2;q^2)_{i+j}}
            {(q^2;q^2)_i^2(q^2;q^2)_j^2}
                     \quad(i+j<N),                             \tag{15}
\]
and is zero otherwise. Its endpoint-uniform absolute profile is
\[
 G(x,y)=J(x+y)-2J(x)-2J(y),\qquad
 |(J_NM^2)_{ij}|\le CN^A e^{NG(i/N,j/N)}.                         \tag{16}
\]
The full factorial error is \(O(\log N)\), including the
boundary of the triangle. The
[coupled-column theorem](research_mixed_symmetric_closing_coupled_column_and_low_outer.md)
proves on that whole triangle
\[
              G(x,y)\le b_2,\qquad G(x,y)+f(y)\le\sigma_* .      \tag{17}
\]
These inequalities keep the distinct maximizing rows of the
two factors; replacing (17) by two separate maxima would lose
the required \(1/19\).

Expand the full finite product
\[
       J_NM^3\mathbf e(w)=(J_NM^2)(M\mathbf e(w)).                \tag{18}
\]
For its compact columns \(j/N\in I\), equations (7),(16),(17)
give rate at most \(\sigma_*-c_I d(\theta)\).
For the two endpoint column groups, (10),(13) and \(G\le b_2\)
give respectively the rates
\[
                         b_2+9/50,\qquad 2b_2+1/20.              \tag{19}
\]
Both are strictly below \(\sigma_*-1/120\). For the upper
group the exact available reserve is
\[
 \sigma_*-(2b_2+1/20)
 >\frac19-\frac1{19}-\frac1{20}
   =\frac{29}{3420}>\frac1{120},                                \tag{20}
\]
since \(3480>3420\). For the lower group use
\(\lambda_*>67/99>2/3\), \(9/50<1/5\), and
\(1/19<1/15\); its reserve is greater than \(2/5\).
Thus the same choice (14) pays the angular loss in every
endpoint term. Sum the at most \(N\) terms in each row of
(18), take its Euclidean norm, and use that \(J_N\) is an
isometry. This proves the second bound in (5).

This proof bounds the actual finite vector, with all complex
phases still present in (2),(15),(18). It uses absolute values
only for an upper bound, and claims neither positivity nor a
nonzero lower rate for a subsequent signed observation.

## 5. Ordinary derivatives and full-interval neighborhoods

Each coordinate of either vector in (5) is an ordinary
polynomial of degree at most \(D\). The weighted Laurent
maximum principle in the real outside-color theorem gives,
from either real bound with constant rate \(L\),
\[
 |P_N(-2\cos(\theta+iv))|
 \le CN^A\exp N\{L-cd(\theta)+(1+c)|v|\}.                       \tag{21}
\]
Applying it coordinatewise changes only the polynomial when
the norm is taken. An ordinary circle of radius \(N^{-2}\)
changes the inverse-cosine angle by \(O(N^{-1})\), uniformly
at both quadratic branch points. Cauchy's formula therefore
proves the asserted real angular bounds for every fixed
ordinary derivative, at polynomial cost.

For the unweighted complex-neighborhood assertion, let
\(\mathcal E_\rho\) be the filled Bernstein ellipse of
parameter \(e^\rho\), with foci \(-2,2\). Every polynomial
of degree at most \(D\) satisfies
\[
 \sup_{\mathcal E_\rho}|P_N|
       \le2(D+1)e^{D\rho}\sup_{[-2,2]}|P_N|.                    \tag{22}
\]
Apply (22) to every coordinate in (5). Choose \(\rho>0\)
smaller than the prescribed allowance \(\tau\), retaining
the polynomial factors. A smaller ellipse is a fixed ordinary
neighborhood of the whole closed interval; Cauchy there gives
each fixed derivative with the same allowed rate. This proves
all parts of Theorem 1. In particular it continues a bound on
an entire interval, not the value of one cancelling column.

## 6. The unchanged low and far outer paths for all real colors

The full finite inner kernel is
\[
 Q_N(w,u)=\mathbf e(-2\cos u)^TJ_NM^3\mathbf e(w).                 \tag{23}
\]
The transpose is not a Hermitian adjoint, but Cauchy--Schwarz
still bounds its modulus. The complete Newton-vector theorem
gives, uniformly for \(|a|\le\pi\), \(0\le h\le7/10\),
\[
 \|\mathbf e(-2\cos(a-ih))\|_2
                     \le CN^B e^{N(m_0(a)+h)}.                  \tag{24}
\]
Thus (5) proves the all-real incoming source bound
\[
 |Q_N(-2\cos\theta,a-ih)|
       \le CN^A e^{N\{m_0(a)+h+\sigma_*-cd(\theta)\}}.           \tag{25}
\]
It retains all rows. It also proves the same unweighted bound
with any prescribed positive allowance on a fixed neighborhood
of the entire real incoming interval.

Use the literal outer functions
\[
\begin{split}
 G_N(u;\mathbf w)&=\sin u\,Q_N(w_L,u)Q_N(w_R,u)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-(-1)^D e^{-iNu})^2},\qquad
 C_{N,4}=q^{D^2}.
\end{split}                                                       \tag{26}
\]
Set \(h_0=1/10000\), and retain exactly the midpoint \(a_N\)
and fixed height \(h_c\in(0,1/1000]\) of the far-boundary
theorem. Consider the path with successive vertices
\[
 2\pi/3-ih_0,\quad4\pi/5-ih_0,\quad4\pi/5-i/100,
                  \quad a_N-i/100,\quad a_N-ih_c .               \tag{27}
\]

**Corollary 2.** On fixed complex neighborhoods of both entire
real incoming intervals, the sum of the absolute integrals on
(27), multiplied by the original \(N^2/\pi\), is at most
\[
                          C e^{N(M_g-1/400)}.                    \tag{28}
\]
Every fixed mixed ordinary incoming derivative has the same
bound on smaller fixed neighborhoods. For real incoming
colors, the right side may additionally retain
\(\exp\{-Nc[d(\theta_L)+d(\theta_R)]\}\), with a possibly
smaller positive \(c\). The signed original current still
has scalar \(-C_{N,4}/i\). No alias of (26) is discarded.

On the first segment, the original real-row comparison is
\[
             m_0(a)\le b_2-67/(72\pi)\quad(a\ge2\pi/3).         \tag{29}
\]
Combine it with (25). The two evaluation vectors cost \(2h_0\),
and the outer crossing and full sampling factor cost
\((2a/\pi-1)h_0\). Their total height cost is at most
\(3h_0\). The written zero-height margin in the coupled-column
proof is exactly
\[
 \frac{163}{50}
 -2\left\{\frac{7987}{4752}-\frac1{19}\right\}
              =\frac{4211}{1128600}>\frac1{300}.                 \tag{30}
\]
Take a rate allowance \(1/10000\) for each column on the
full-interval neighborhood from (22), and spend another
\(1/10000\) on fixed polynomial factors. Together with
\(3h_0\), the expenditure is \(6/10000\), leaving
\(41/15000>1/400\). This is exactly the earlier finite-source
calculation, with its formerly small incoming disks replaced
by the now proved full-interval neighborhoods.

For the remaining segments one may use the weaker rate
\(b_2+\lambda_*<301/216\), already implied by (5), and
\(m_0(a)\le9/50\) for \(a\ge4\pi/5\). The earlier far-right
proof then bounds the complete density at rate less than
\[
                         301/108+9/25+3/100=8578/2700.           \tag{31}
\]
Its margin below \(M_g>321/100\) is greater than
\(89/2700\). The same prescribed allowances and polynomial
costs leave more than \(1/50\), hence more than the gap in
(28). On the added vertical at \(4\pi/5\), the height lies
between \(h_0\) and \(1/100\); on the remaining path it lies
between \(h_c\) and \(1/100\). Both lower heights are fixed
and positive. Thus throughout the path
\[
 |W_N(a-ih)|\le e^{-Nh}(1-e^{-N\min(h_0,h_c)})^{-2}
                                      \le C e^{-Nh}.             \tag{32}
\]
The sine factors and path lengths are bounded. Equations
(30)--(32) retain the exact double denominator, its parity,
the original \(N^2\), and the full traces in both factors.
They prove (28). For real colors retain the angular factors
from (25) at every step; ordinary derivative statements
follow from Sections 5 and the pointwise estimates before
integration.

The separately removed far physical values, first normals,
odd simple node and short midpoint currents already have
full-real incoming scope in the far-boundary theorem,
equations (13)--(21). They need no new extension here.
Its Markov estimate uses the whole real spectral interval,
and its incoming continuation uses the exact separate
degrees \(D,D\). The earlier far-left matrix bounds likewise
already have full-real incoming scope. The present deduction
fills the missing all-real scope of the sharper column bounds
used on (27); it does not by itself reassemble the remaining
deep connectors or the entire ordinary closing.

## Source bindings

- Exact complete column, cap profile and literal endpoint groups:
  research_mixed_symmetric_closing_complete_column_norm.md,
  SHA-256 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519.
- Whole-real angular cap estimate on compact physical index intervals:
  research_mixed_endpoint_real_color_decay.md,
  SHA-256 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb.
- All-row real Newton entropy, including the upper half:
  research_mixed_newton_color_tubes.md,
  SHA-256 61f5d6ffe8571bf309c75cd3c74d8ffefedf997095aac7347cbbcc64e0a8c57d.
- Full supported matrix and uniform factorial error:
  research_three_crossing_global_preparation_error.md,
  SHA-256 c1e80c6efbc9ff936d889eebd1f449e85c81820a64fb046e6dfe8e1003d2d239.
- Coupled profile loss and original low-current rate arithmetic:
  research_mixed_symmetric_closing_coupled_column_and_low_outer.md,
  SHA-256 f1a8fb899e580c3953136aaa7aeb86530e2c51d25aaecba28e66b16183083b51.
- Full complex evaluation vector and existing all-real left-far scope:
  research_mixed_symmetric_closing_left_far_connection.md,
  SHA-256 d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184.
- Explicit real-row loss at \(2\pi/3\):
  research_mixed_symmetric_closing_low_horizontal_norm.md,
  SHA-256 0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Exact far-right path, height and source comparison:
  research_mixed_symmetric_closing_earlier_far_right_connection.md,
  SHA-256 9b62082201e99c73371c19cd82f7279fb3a4a57cecff2135306815f3bc3ad416.
- Original all-real far samples, normals and midpoint currents:
  research_mixed_symmetric_closing_far_boundary_payment.md,
  SHA-256 dc1942698fe442e9995c6bf1ee44ae67f7432c54f2f2d2086e108d83f132fd6b.
- Geometric action lower bound with its original normalization:
  research_mixed_symmetric_closing_action_floor_163.md,
  SHA-256 f0bfaf90d7e331adf1df3ba59980dea76ebc8347b7244d2b52c4e1c692b5f825.
