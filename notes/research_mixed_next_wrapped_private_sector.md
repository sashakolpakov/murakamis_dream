# Removing the wrapped private rows from the middle incoming arc

Research deduction, 7 November 2026. On the real incoming interval
\([1/2,7/10]\), the retained conditional polynomial has outgoing degree
less than \(N/2\). This smaller degree pays the whole part of the
original cap whose private index reaches the wall \(a+e=1\), including
a fixed collar before that wall. The estimate retains each complete
endpoint coefficient. It does not deform either summation contour.

After this removal, the unresolved real main involves only private
and conditional indices strictly before their respective walls.
The initial vertical incoming connector remains separate.

## 1. The exact split and its degree

Write \(D=N-1\), \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), \(p_j(X)=(rX;r)_j\), and use the original factors
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{D}
        H_N(w,r^{-j})\,\frac{p_j(X)}{P_j},\\
 C_{1,N}(X,Y)&=\sum_{k=0}^{D}
        \frac{X^{-k}p_k(X)p_k(Y)}{P_k^3}.
\end{split}                                                     \tag{1}
\]
The polynomial \(H_N\) in each private row is its complete coherent
endpoint source. No absolute estimate of its separate Newton
summands is used below.

Let
\[
 \frac12\le a\le\frac7{10},\qquad X=e^{-2\pi ia},
 \qquad v=1-a\in[3/10,1/2].
                                                               \tag{2}
\]
Keep the conditional cuts of
[the end-range theorem, Section 3](research_mixed_next_selected_first_wall_rows.md):
\[
\begin{split}
 L_N&=\lfloor N/16\rfloor+1,&
 K_N(a)&=\lceil N(v-\varepsilon)\rceil,\\
 C_{1,N}^{\,\mathrm{mid}}(X,Y)
   &=\sum_{k=L_N}^{K_N(a)-1}
             \frac{X^{-k}p_k(X)p_k(Y)}{P_k^3}.
\end{split}                                                     \tag{3}
\]
Here \(\varepsilon>0\) is the fixed width in that theorem.
All assertions concern sufficiently large \(N\), for which these
indices are ordered as stated there. The physical conditional rows
omitted from (3) already have a selected-source gap, with the whole
original cap retained.

The elementary inequality \(\lceil q\rceil-1<q\), valid also when
\(q\) is an integer, gives the exact outgoing degree bound
\[
       \deg_Y C_{1,N}^{\,\mathrm{mid}}
       \le K_N(a)-1<N(v-\varepsilon)<Nv\le N/2.
                                                               \tag{4}
\]
This degree statement concerns the finite polynomial (3), not a
continuation of a discrete index.

For \(0\le\delta<1/20\), define the private part
\[
 U_{0,N}^{\,\ge v-\delta}(w,X)
   =\sum_{j=\lceil N(v-\delta)\rceil}^{D}
            H_N(w,r^{-j})\,\frac{p_j(X)}{P_j}.
                                                               \tag{5}
\]
These are literal subsets of the original private rows. At a
nonphysical \(a\), rows past the wall are not set to zero.

## 2. A bound for the complete private part

Use the continuous periodic primitive \(J\) of
\(\log(2|\sin\pi e|)\), normalized by \(J(0)=0\), and write
\[
\begin{split}
 h(e)&=\Re S(e)+J(e),\qquad b_0=101/125,\\
 B_v(e)&=J(e-v)+J(v)-J(e),\\
 A(v)&=J(v)-2J(v/2).
\end{split}                                                     \tag{6}
\]
The whole-index source estimates in
[the coherent cap bound, Sections 1--3](research_mixed_next_coherent_cap_far_arc.md)
give the rate \(h(e)+B_v(e)\) for a compact private row.
They apply to every real ordinary color \(w\in[-2,2]\), and on
sufficiently small fixed disks about the complete color, with
arbitrarily small prescribed tolerances. They preserve all numerator
zeros. The same source gives
\[
 h(e)\le b_0\quad(0\le e\le1),\qquad
 B_v(e)\le0\quad(v\le e\le1).
                                                               \tag{7}
\]
The second inequality follows from \(B_v(v)=B_v(1)=0\) and
the unique interior minimum of the sine quotient. It extends across
the integrable logarithmic endpoints by continuity.

The true upper private end is treated separately: its complete
positive row sum has rate \(3/5<b_0\) on \(|X|\le1\), by
[the complementary real-color theorem, Section 2](research_mixed_three_four_complementary_real_colors.md).
There is no use of a compact-index asymptotic at that endpoint.
Consequently
\[
 |U_{0,N}^{\,\ge v}(w,X)|
   \le C_\tau N^{B_\tau}e^{N(b_0+\tau)}.
                                                               \tag{8}
\]
In fact (8) bounds the sum of the absolute private-row contributions
after each coherent \(H_N\) has been estimated.

The function \(B_v(e)\) is jointly continuous on the compact real
domain of (2) and \(0\le e\le1\). Hence there is a fixed
\(0<\delta_*<1/20\) such that
\[
 B_v(e)<1/1000\qquad(e\ge v-\delta_*).
                                                               \tag{9}
\]
One may shrink \(\delta_*\) as needed. This follows from uniform
continuity and (7), including at the moving wall; it does not
assume continuity of a finite logarithmic derivative. The same
compact-row bounds and separate true-end bound prove
\[
 |U_{0,N}^{\,\ge v-\delta_*}(w,X)|
       \le C_\tau N^{B_\tau}e^{N(b_0+1/1000+\tau)}.
                                                               \tag{10}
\]
Both (8) and (10) hold for arbitrary subsets of the specified rows.

## 3. The smaller outgoing degree pays the selected radius

The exact numerator bound on the whole unit disk, the incoming
quotient estimate \(B_v(k/N)\le A(v)\), and
\(\max_{[0,1]}(L-2J)<7/15\), where
\(L(t)=-2J((1-t)/2)\), give
\[
 \sup_{|Y|\le1}|C_{1,N}^{\,\mathrm{mid}}(X,Y)|
 \le C_\tau N^{B_\tau}e^{N\{A(v)+7/15+\tau\}}.
                                                               \tag{11}
\]
This uses the positive upper bounds for the literal rows of (3).
The chirp \(X^{-k}\) has modulus one.

Differentiation gives
\[
 A'(v)=\log(2\cos(\pi v/2))>0\qquad(0<v\le1/2).
                                                               \tag{12}
\]
At the endpoint,
\[
 A(1/2)=-2J(1/4)=G/\pi=b_2/2<7/24.
                                                               \tag{13}
\]
Here \(G\) is Catalan's constant. The rational witnesses are given
explicitly in
[the low-index kernel margin, Section 2, equations (14)--(15)](research_mixed_next_low_index_kernel_margin.md):
\(G<229/250\) and \(\pi>333/106\) imply
\(b_2<24274/41625<7/12\). The latter bound on \(\pi\) is
proved there by Machin's formula and an alternating-series
truncation; no new evaluation is required for (13).

Thus, without the collar debit, the product of (8) and (11)
has whole-disk rate
\[
       b_0+7/24+7/15=\frac{4699}{3000}
                       =\frac{77}{50}+\frac{79}{3000}.
                                                               \tag{14}
\]
For a polynomial of degree \(d\), the exterior maximum principle
gives its bound at radius \(R\ge1\) by \(R^d\) times its
unit-disk bound. On the selected segment
\[
 y=x+i/100,\quad x\in P=[.22,.45],\qquad Y=e^{-2\pi iy},
                                                               \tag{15}
\]
equation (4) therefore costs at most \(\pi/100\) in the
exponential rate. The private factor in (5) is independent of \(Y\).
It follows that
\[
 |U_{0,N}^{\,\ge v-\delta_*}(w,X)
              C_{1,N}^{\,\mathrm{mid}}(X,Y)|
 \le C_\tau N^{B_\tau}
   e^{N\{4699/3000+\pi/100+1/1000+\tau\}}.
                                                               \tag{16}
\]
All physical rows and product zeros in (3) and (5) remain.

## 4. Calibration with the ordinary-next reference

Use exactly the ordinary-next canonical family and absolute affine
plane \(\Lambda_{123}(z)\) of
[the full selected-plateau comparison, equations (3)--(8)](research_mixed_next_filtered_selected_plateau.md).
Thus the flags are \((0,1,\beta)\), \(\beta=0,1\), the external
ordinary parameter is \(c=s_4^*\in K_3\cup K_4\), \(y\) is
as in (15), and
\[
 z=u+i\Im z_*,\quad u\in P,\qquad Z=e^{-2\pi iz}.
                                                               \tag{17}
\]
In particular this is not a terminal third-vertex reference.

The proof of Sections 3--4 of that comparison uses its prefix
polynomial only through the selected-radius rate
\(77/50+\pi/50\). The original selected halfweight, both
Fourier-weight alternatives, the entire third factor, and the
actual real marginal are otherwise unchanged. The improvement of
the rate in (16), before the collar debit, is
\[
 \frac{\pi}{100}-\frac{79}{3000}
     >\frac1{32}-\frac{79}{3000}
     =\frac{59}{12000}.
                                                               \tag{18}
\]
Here only \(\pi>25/8\) is used. Adding the original raw
gap \(1/500\) gives \(83/12000>1/150\). After the collar
debit in (16), the remaining raw gap is greater than
\[
             \frac{83}{12000}-\frac1{1000}
                    =\frac{71}{12000}>\frac1{200}.
                                                               \tag{19}
\]

**Theorem.** For every sufficiently small prescribed tolerance
\(\tau>0\), the literal product satisfies
\[
\begin{split}
 &|U_{0,N}^{\,\ge v-\delta_*}(w,X)
       C_{1,N}^{\,\mathrm{mid}}(X,Y)
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{15mm}\le C_\tau N^{B_\tau}
       e^{N\{\Lambda_{123}(z)-1/200+\tau\}} .
\end{split}                                                     \tag{20}
\]
It holds uniformly in (2), (15), and (17), for all real ordinary
colors, both level parities, and on sufficiently small fixed
complete-color disks. For \(\beta=0\), no outgoing weight is
inserted. A finite loss \(1/400\) remains after tolerances and
polynomial factors.

Fixed real ordinary derivatives are bounded by applying Markov to
each complete endpoint polynomial before the positive private sum.
Fixed complex ordinary derivatives follow on smaller disks.
For outgoing and reference derivatives, hold the base contour,
the integer sets (3), (5), and the reference allocation fixed,
and use Cauchy on sufficiently small fixed neighborhoods. The
strict reserve in (19) permits these neighborhoods uniformly.
Every fixed mixed derivative of the locally normalized error has
loss \(1/800\). No derivative of a moving floor or ceiling is
asserted.

Integrating (20) over \(a\in[1/2,7/10]\) and the selected
segment in \(y\) costs only their bounded lengths and the
original factors \(N\). In particular, the exact source contribution
is formed with
\[
 N^2\int_{P+i/100}\int_{1/2}^{7/10}
 U_{0,N}^{\,\ge v-\delta_*}(w,e^{-2\pi ia})
 C_{1,N}^{\,\mathrm{mid}}(e^{-2\pi ia},Y)
 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\,da\,dy .
                                                               \tag{21}
\]
The finitely many changes of row sets are kept in this integral.
Equation (21) is neither a physical-root sum nor a replacement
for either complete Fourier coefficient.

## 5. The exact part still to estimate

The complement of (5) with \(\delta=\delta_*\) has
\[
        e=j/N<v-\delta_* .
                                                               \tag{22}
\]
The retained conditional rows satisfy \(t=k/N<v-\varepsilon\).
Thus, after the already paid conditional end ranges and (20),
the only remaining real finite source has both inequalities
\[
               a+e<1-\delta_*,
               \qquad a+t<1-\varepsilon .
                                                               \tag{23}
\]
There is a fixed regular-strip margin at both walls.

The exact real-main reduction in
[the conditional-alias theorem](research_mixed_next_far_half_conditional_aliases.md)
may also be used after this split. Its alias proof uses the
positive complete cap-row bound, so applies to any private subset;
the subset in (5) has the smaller bound (10). Therefore replacing
its retained conditional polynomial by
\(N\int_{\ell_N}^{u_N(a)}T_N(t;a,y)\,dt\) changes (21)
only by an already paid error. This statement retains the two
original half-grid cuts and every alias remainder.

Nothing here pays the remaining joint region (23), deforms its
real main path, or estimates an unweighted connector from such
a deformation. In particular, the original first-coordinate
segment from \(1/2+i h_a\) to \(1/2\) is still separate.
