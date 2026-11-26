# Reducing the shallower own-three upper strip to its last alternative

Private research proof, 8 November 2026. At shared radius at least
\(7/10\), the part of the remaining upper physical strip with
\(q\ge3/20\) or reflected index \(v\ge1/5\) reduces to the original
last alternative and an already paid band. The complete first source
is retained. This is a new finite-row reduction, not a claim that the
actual first-main by next-last comparison has been paid at these radii.
No numerical evaluation or frozen-source edit is used.

## 1. Original source and same-coordinate rate comparison

Keep the actual ordinary-next own-three references and allocations of
[the fixed-shared band theorem](research_mixed_next_own_three_upper_band_fixed_shared.md):
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\qquad
x,u\in P=[11/50,9/20],\quad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad -.065<h_z<.068,\\
X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad Z=\rho e^{-2\pi iu},\qquad
7/10\le R<1,\quad 0<\rho<L:=43/28.
\end{gathered}                                                    \tag{1}
\]
All actual reference correlations remain imposed. Put
\[
\begin{split}
E(t)&=\int_0^t\log|1-Ye^{-2\pi ib}|\,db+
       \int_0^t\log|1-Ze^{-2\pi ib}|\,db-2J(t)-t\log R,\\
F(v)&=E(1-v),\quad L_0=-\log R+\log_+\rho,\quad T=R^{-1},\\
S(v)&=2\sin\pi v,\quad
A(v)=|T-e^{2\pi i(v-q)}|,\quad
B(v)=|1-\rho e^{2\pi i(v-u)}|.
\end{split}                                                       \tag{2}
\]
The exact reflected identity, with both original carriers, is
\[
                  F(0)=L_0,\qquad
F'(v)=\log\frac{S(v)^2}{A(v)B(v)}.                              \tag{3}
\]
Outgoing zeros retain their integrable logarithmic limits.

**Proposition 1.** On (1),
\[
\boxed{\quad
F(v)\le\max\{L_0,F(3/10)\},
\qquad 3/20\le q\le11/50,\quad q\le v\le3/10.
\quad}                                                           \tag{4}
\]
This compares rates at the same shared coordinate, heights and target.
It does not divide by a terminal finite row.

## 2. Positive reflected force for \(v\ge9/50\)

Suppose \(q\ge3/20\), \(\max(q,9/50)\le v\le3/10\).
The incoming modulus increases with \(T\ge1\), and
\(0\le v-q\le v-3/20\), so
\[
A(v)^2\le \frac9{49}+\frac{20}{7}
                      \{1-\cos(2\pi(v-3/20))\}.                \tag{5}
\]
The following elementary bounds give \(A(v)B(v)<S(v)^2\):
\[
\begin{array}{c|c|c|c}
v\text{ interval}&A(v)<&B(v)<&S(v)^2>\text{ or }\ge\\ \hline
[9/50,1/5]&4/7&2&8/7\\
[1/5,9/40]&5/7&13/7&11/8\\
[9/40,1/4]&7/8&12/7&59/35\\
[1/4,3/10]&6/5&5/3&2\quad(\ge).
\end{array}                                                       \tag{6}
\]
Here are witnesses for every entry. For the first two incoming
bounds, \(1-\cos t\le t^2/2\) and \(\pi<22/7\) give respectively
\[
A^2<557/1715<16/49,\qquad A^2<1719/3430<25/49.                  \tag{7}
\]
For the third, \(\cos(\pi/5)>4/5\) gives
\(A^2<37/49<49/64\). For the fourth,
\(\cos(3\pi/10)>7/12\) gives \(A^2<202/147<36/25\).
The last cosine inequality follows by squaring its radical formula:
\(\sin^2(\pi/5)=(10-2\sqrt5)/16>49/144\), using
\(\sqrt5<9/4<41/18\).

The outgoing angular distances in these intervals are at most
\(27/100,1/4,9/40,1/5\). Their cosines are greater than
\(-13/100,3/20,3/10\) in the first, third and fourth cases,
and nonnegative in the second. Use
\(\cos(27\pi/50)=-\sin(\pi/25)>-13/100\),
\(\sin(\pi/20)>3/20\), and \(\cos(2\pi/5)>3/10\).
The squared modulus is convex in \(\rho\in[0,L]\), so checking
\(\rho=0,L\) suffices. The four comparisons are
\[
\begin{split}
1+L^2+(13/50)L&<4,\\
1+L^2=2633/784&<(13/7)^2,\\
1+L^2-(3/10)L&<(12/7)^2,\\
1+L^2-(3/5)L&<13/5<25/9 .
\end{split}                                                       \tag{8}
\]
For the last line one may enlarge \(L\) to \(8/5\).

Finally,
\[
\begin{split}
S(9/50)^2&=2-2\sin(7\pi/50)>8/7,\\
S(1/5)^2&=(5-\sqrt5)/2>11/8,\\
S(9/40)^2&=2-2\sin(\pi/20)>2-\pi/10>59/35 .
\end{split}                                                       \tag{9}
\]
For the first, \(7\pi/50<11/25\) and
\(\sin t<t-t^3/7\) on \(0<t\le1/2\) give
\(\sin(7\pi/50)<46794/109375<3/7\).
That sine bound follows from
\(\sin t\le t-t^3/6+t^5/120\); its right side is increasing
on the interval used. The other witnesses use \(\sqrt5<9/4\)
and \(\sin t<t\). Thus \(F'(v)>0\) throughout this region.

## 3. No interior maximum on the remaining small interval

For \(3/20\le q\le v\le9/50\), the outgoing difference
\(u-v\in[1/25,3/10]\), so both moduli in (3) are nonzero.
Differentiation gives
\[
\frac{F''(v)}{2\pi}
=\cot\pi v-\frac{T\sin(2\pi(v-q))}{A(v)^2}
          +\frac{\rho\sin(2\pi(u-v))}{B(v)^2}.                  \tag{10}
\]
The last term is nonnegative. At a stationary point, (3) gives
the exact relation \(A(v)^2B(v)^2=S(v)^4\).
Also, using \(\cos(3\pi/5)>-1/3\) and convexity in \(\rho\),
\[
B(v)^2<1+L^2+(2/3)L=10307/2352<9/2.                            \tag{11}
\]
Thus the only negative term at a stationary point is less than
\[
\frac{10}{7}\frac92
       \frac{\sin(2\pi(v-3/20))}{S(v)^4}<\frac{63}{64}.          \tag{12}
\]
For the last inequality the ratio increases on \((3/20,9/50]\):
its logarithmic derivative is
\[
2\pi\cot(2\pi(v-3/20))-4\pi\cot(\pi v)>0.                      \tag{13}
\]
Indeed \(\cot(3\pi/50)>5\), whereas
\(\cot(\pi v)<1/(\pi v)<20/9\).
For the former bound,
\(3\pi/50<19/100\), \(\cos t>49/50\), and \(\sin t<t\)
give \(\tan(3\pi/50)<19/98<1/5\).
At the right endpoint the numerator in (12) is less than \(1/5\),
while (9) makes the denominator greater than \(64/49\).
This gives exactly \((10/7)(9/2)(1/5)(49/64)=63/64\).

Since \(v<1/4\), every stationary point therefore satisfies
\[
                            F''(v)>\pi/32>0.                  \tag{14}
\]
The smooth compact interval has no interior local maximum.
Its upper endpoint is bounded by \(F(3/10)\) by Section 2.
At its lower endpoint the all-radius
[upper-end lemma](research_mixed_next_own_three_upper_end_last_reduction.md),
equation (10), gives \(F(q)\le L_0\). This proves (4).
If \(q\ge9/50\), Section 2 proves it directly.

## 4. Diagonal transport from smaller \(q\) when \(v\ge1/5\)

Let \(s\) be an original first main clipped to
\(1/6\le\Re s\le5/12\) at its fixed negative height, or one
of its real cuts \(s=1/8,1/2\). Put
\[
\begin{split}
\mathcal B_s(q,v)&=B_U(x)+\Re Q_1(s;a,y)+F(v)-\Re g(y),\\
\mathcal L_s(q)&=B_U(x)+\Re Q_1(s;a,y)+L_0-\Re g(y).
\end{split}                                                       \tag{15}
\]
The cap plane and full shared allocation are original. There is no
outgoing halfweight for own type three. For \(q\le3/20\),
\(1/5\le v\le3/10\), increase \(q,v\) together, stopping at
\(q=3/20\) or \(v=3/10\). The exact multiplier of
[the enlarged-band proof, equation (10)](research_mixed_next_own_three_upper_band_old_face.md)
is
\[
\exp\frac d{dq}\mathcal B_s(q,q+d)
=\frac{R|1-Y/S_s|S(v)^2}{|1-Y|^3B(v)},\quad
S_s=e^{2\pi is},\quad d=v-q.                                  \tag{16}
\]
Here
\(|1-Y/S_s|=|1-R e^{2\pi\Im s}e^{-2\pi i(q+\Re s)}|\).
This does not transport a positive-height first alias.

On the path, \(B(v)<13/7\) and \(S(v)^2>11/8\).
The following bounds make (16) strictly greater than one:
\[
\begin{array}{c|c|c}
q\text{ interval}&R/|1-Y|^3>&|1-Y/S_s|>\\ \hline
[0,1/10]&3&7/10\\
[1/10,1/8]&9/5&1\\
[1/8,3/20]&5/4&9/8 .
\end{array}                                                       \tag{17}
\]
The smallest displayed product is
\[
              \frac54\frac98\frac{11}{8}\frac7{13}
                   =\frac{3465}{3328}>1.                       \tag{18}
\]
For the radial column use successively
\(\cos2\pi q>4/5,7/10,7/12\).
The function \(R/(1+R^2-2cR)^{3/2}\) has no interior
minimum on \([7/10,1]\): its derivative has the sign of
\(1-2R^2+cR\), changing at most once from positive to negative.
The squared endpoint comparisons are
\[
\begin{array}{c|c|c}
c&R=7/10&R=1\\ \hline
4/5&(49/100)/(37/100)^3&1/(2/5)^3\\
7/10&(49/100)/(51/100)^3&1/(3/5)^3\\
7/12&(49/100)/(101/150)^3&1/(5/6)^3 .
\end{array}                                                       \tag{19}
\]
Each row exceeds the square of its entry in (17) by rational
cross multiplication.

The first numerator bound is unchanged from the enlarged-band proof.
On the middle interval a clipped main has
\(q+\Re s\in[4/15,13/24]\), hence negative cosine.
For the real low cut its squared modulus exceeds
\(1+(7/10)^2-(8/25)(7/10)>1\); the real half is stronger.
On the last interval a main has
\(q+\Re s\in[7/24,17/30]\), with cosine less than \(-1/4\);
its radius is greater than \(7/20\). Its squared modulus therefore
exceeds \(519/400>81/64\). Both real cuts have stronger bounds.
This proves (17).

The endpoint \(v=3/10\) has the existing original profile deficit
\(10^{-10}\), for every current \(q\), from the old-band and
fixed-shared-band theorems. If the path stops at \(q=3/20\),
(4) reduces its rate to that paid boundary or the last profile there.
Thus for all main or real-cut profiles,
\[
\mathcal B_s(q,v)
\le\max\{\Lambda_{123}(z)-10^{-10},
                   \mathcal L_s(\max\{q,3/20\})\}
\tag{20}
\]
on
\[
 q\le v\le3/10,\qquad q\ge3/20\ \hbox{or}\ v\ge1/5.             \tag{21}
\]
For \(q\ge3/20\) this follows directly from (4). The first
main is clipped at the current shared coordinate before comparison.

## 5. First last alternative and the full finite-row reduction

For \(q\ge1/10\), the established same-point comparison
\[
                     E_1(1/8;a,y)>\delta_a+3/2000,
              \qquad \delta_a=-2\pi h_a,                     \tag{22}
\]
is Section 2 of
[the complete-first below-half theorem](research_mixed_next_own_three_below_half_complete_first.md).
It applies throughout the present radial interval and can be
multiplied by any positive next row. Thus the first last alternative
reduces to the first real low profile in (20).
For \(q\le1/10\), \(v\ge1/5\), its diagonal multiplier is
\[
\frac{R S(v)^2}{|1-Y|^2B(v)}
 >\frac{70}{37}\frac{11}{8}\frac7{13}>1.                        \tag{23}
\]
Indeed \(R/(1+R^2-2cR)\) increases for \(R\le1\); use
\(R\ge7/10,c>4/5\). Transport until \(q=1/10\) or the paid
boundary \(v=3/10\). In the former case use (22), then (16).

Here is a precise finite consequence, with the remaining obligation
visible. Let \(\mathscr S\) consist of the clipped negative-height
first main segment and the two real cuts \(1/8,1/2\). Set
\[
\mathfrak L(q')=\max_{s\in\mathscr S}
 \{B_U(x)+\Re Q_1(s;a,q'+ih_y)+L_0-\Re g(q'+ih_y)\}.
\tag{24}
\]
This is the actual first-main/real-cut by next-last envelope;
no unquantified old last-row margin is spent.
Let \(\mathcal J_N(q)\) consist exactly of the original indices
\(\lceil N/2\rceil\le j<N\) for which \(v_j=1-j/N\)
satisfies (21). With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
and \(p_j(W)=(rW;r)_j\), every fixed \(\tau>0\) gives
\[
\begin{split}
&|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|
 \sum_{j\in\mathcal J_N(q)}
        \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|\\
&\qquad\le C_\tau N^{B_\tau}
 \exp N\left\{\max\bigl(\Lambda_{123}(z)-10^{-10},
                  \mathfrak L(\max\{q,3/20\})\bigr)+\tau\right\}.
\end{split}                                                       \tag{25}
\]
It holds for all real ordinary colors and both parities, as well as
arbitrary subsets of the indicated positive rows. The central first
incoming integral retains \(+N\,da\); integration adds a polynomial
prefactor and the supremum of the displayed rate on that original
central path.

For the source proof use the unchanged first decomposition of the
enlarged-band theorem: positive low rows reduce to their real cut,
the full middle retains both horizontal aliases, all four weighted
vertical halves and both unweighted joins, and the positive upper
block retains its real half and last alternatives. All first-current
comparisons are made at the same \(q\) before (16), so no
positive-height first profile is transported by that formula.
The cap plane and the complete forced-\(d_N\) upper envelope are
the same original inputs. Uniform zero-safe numerator and factorial
bounds turn every actual next row into (2), with polynomial factors
and arbitrarily small total rate tolerances. These next indices stay
in a compact upper-half interval; rounding and endpoint errors are
uniform. Numerator zeros remain one-sided upper bounds.
No finite value is substituted at a nonintegral transported row.
Apply the continuous comparisons first, then sum the literal rows.
This proves (25) with every original row, normal and scalar retained.

Equation (25) gives no new loss below the next action until its
displayed last envelope is paid. No pending actual-reference radius
or first-height comparison is assumed. The only intermediate strip
not reduced by this note and the old bands is
\(q<v<1/5,\ q<3/20\). Noncentral first paths, the other Fourier
contours and arbitrary short-word closure remain separate.

