# A static central budget for the second selected coordinate

Research deduction, 6 November 2026. This is an analytic upper-bound
formula for the main/main currents in the position-2 reduction.
Its uniform scalar signs are not proved. No root, finite source,
parameter sweep or numerical certificate is evaluated.

## 1. The five variables and both original boundary tangents

Use the actual references and literal source in
[the position-2 reduction](research_mixed_second_selected_plateau_reduction.md),
with \(m\ge4\), \((\epsilon_1,\epsilon_2,\epsilon_3)
=(\alpha,1,\beta)\), and \(\alpha,\beta\in\{0,1\}\).
Position 1 is unselected. Rename the five coordinates
\[
 a=r_1,\qquad u=s_2,\qquad z=r_2,\qquad v=s_3,\qquad b=r_3.
 \tag{1}
\]
Stars denote the same actual coupled reference throughout. Only the
height of \(z\) changes, from \(c=\Im z_*\) to
\(0<H\le7/500\). All other heights remain their original
values. The full main-current real domain is the product
\[
 K=P\times[1/8,1/2]\times P\times[\ell_\beta,1/2]\times P,
 \quad P=[.22,.45],\quad\ell_0=3/20,\quad\ell_1=1/8,
 \tag{2}
\]
in the order \((a_R,u_R,z_R,v_R,b_R)\).
The actual real reference lies strictly inside every interval.

Write \(V(s,w)=g(s+w)-g(s)-g(w)\). The original allocated
phase is exactly
\[
 \begin{split}
 F={}&V(u,a)+V(u,z)+V(v,z)+V(v,b)
      -g(u)-\beta g(v)-g(z)\\
 &-\frac\alpha2g(a)-\frac\beta2g(b)+2\pi iau+2\pi izv.
 \end{split}
 \tag{3}
\]
Equivalently this is equation (6) of the position-2 reduction.
Let \(p_L=F_{a,*}\), \(p_R=F_{b,*}\), and define
\[
 f(x,k)=\Re\{F-p_L(a-a_*)-p_R(b-b_*)\},\qquad
 M=f(x_*,c).
 \tag{4}
\]
The three internal critical equations and these two fixed boundary
subtractions give \(f_x(x_*,c)=0\). The full complex equation
\(F_{z,*}=0\) also gives \(f_k(x_*,c)=0\).
Neither boundary marginal is dropped or replaced by an independent
parameter.

Use \(\nu=1\) for the factorial alternative and \(\nu=0\)
for the forced alternative. At the final height put
\[
 f_\nu(x)=f(x,H)+(1-\nu)\Re g(z_R+iH)-2\nu\pi H.
 \tag{5}
\]
These are the two complete Fourier upper rates for the one selected
polynomial at position 2. We bound both on the same original set
(2); no claim that their optimizers agree is needed.

## 2. Exact vertical cost and exact final gradient

Set \(z_H^*=\Re z_*+iH\),
\(U=e^{-2\pi iu_*}\), \(V_*=e^{-2\pi iv_*}\),
\(Z=e^{-2\pi iz_*}\), and
\[
 \lambda=e^{2\pi(H-c)},\qquad\ell=\log\lambda,
 \quad
 A=\log\left|\frac{1-\lambda UZ}{1-UZ}\right|,
 \quad B=\log\left|\frac{1-\lambda V_*Z}{1-V_*Z}\right|,
 \quad C=\log\left|\frac{1-\lambda Z}{1-Z}\right|.
 \tag{6}
\]
The exact fixed-reference vertical cost is
\[
 \begin{split}
 \mathcal V={}&\Re\{g(u_*+z_H^*)-g(u_*+z_*)
                 +g(v_*+z_H^*)-g(v_*+z_*)\\
 &\hspace{20mm}-3g(z_H^*)+3g(z_*)}
               -2\pi\Re v_*\,(H-c).
 \end{split}
 \tag{7}
\]
In particular \(f(x_*,H)-M=\mathcal V\). The last term is
the original \(2\pi izv\) chirp; the other chirp is unchanged.
Define
\[
 G_H=\Re g'(z_H^*)=\log|1-\lambda Z|,\qquad
 D_\nu=A+B-3C+(1-\nu)G_H,
 \qquad
 T_\nu=\mathcal V+(1-\nu)\Re g(z_H^*)-2\nu\pi H.
 \tag{8}
\]
Then the exact final trial data are
\[
 f_\nu(x_*)-M=T_\nu,\qquad
 \nabla f_\nu(x_*)=(0,A,D_\nu,B-\ell,0).
 \tag{9}
\]
The negative \(-\ell\) belongs to the right ordinary index,
whose incoming argument is selected. The left ordinary index has
gradient \(A\), because its selected argument is outgoing.
The unchanged two boundary derivatives cancel exactly at this trial.

The actual reference also implies
\[
                       0<A<\ell,\qquad 0<B<\ell.
 \tag{10}
\]
Indeed the [reduced-disk pair sums](research_mixed_reduced_disk_pair_sums.md)
give \(.49<\Re(u_*+z_*)<.77\) and
\(.545<\Re(v_*+z_*)<.77\). Thus the cosine of either
argument of \(UZ,V_*Z\) is less than \(1/4\).
The ordinary bounds and existing exponential estimates give
\(1/4<|UZ|,|V_*Z|<8/5\): the lower bound follows from
\(e^{.408\pi}<(19/10)^2<4\), and the upper bound from
\(e^{.136\pi}<8/5\). Hence for either product \(P_0\),
\(|P_0|^2>\Re P_0\) and \(\Re P_0<2/5\).
The squared-modulus differences
\[
 \begin{split}
 |1-\lambda P_0|^2-|1-P_0|^2
   &=(\lambda-1)\{(\lambda+1)|P_0|^2-2\Re P_0\}>0,\\
 \lambda^2|1-P_0|^2-|1-\lambda P_0|^2
   &=(\lambda-1)\{\lambda+1-2\lambda\Re P_0\}>0
 \end{split}
 \tag{11}
\]
prove (10). These signs do not impose a sign on \(D_\nu\).

## 3. A useful vertical bound, and its quantitative limitation

There is a common elementary bound retaining the actual height:
\[
 \mathcal V\le\frac{k_\beta\pi}{2}(H-c)^2,
 \qquad k_0=21/5,\quad k_1=39/10.
 \tag{12}
\]
To prove it, put \(x=\Re z_*\in(.24,.36)\).
For every \(k\in[c,H]\),
\[
 \frac{f_{kk}(x_*,k)}\pi
 =\Re\{3\cot\pi(x+ik)-\cot\pi(u_*+x+ik)
                              -\cot\pi(v_*+x+ik)\}
 \le K_\beta(x),
 \tag{13}
\]
where
\[
 K_0(x)=3\cot\pi x+\tan\pi(x-.14)+\tan\pi(x-.067),
 \qquad
 K_1(x)=3\cot\pi x+2\tan\pi(x-.14).
 \tag{14}
\]
The actual upper real bounds are \(u_{*,R}<.36\) and
\(v_{*,R}<.433\) or \(.36\), according to \(\beta\).
A shifted sum below one half contributes a nonpositive term to
the left side of (13), which can be discarded for this upper bound.
For a sum above one half, an imaginary displacement decreases the
magnitude of its negative real cotangent. Thus (13) does not assume
\(\Re(u_*+z_*)>1/2\), which is not supplied in every type pattern.

Both functions in (14) are convex on \([.24,.36]\). The
existing tangent witnesses in the
[first-selection Legendre proof](research_mixed_selected_endpoint_legendre_budget.md),
[half-index proof](research_mixed_half_index_contour.md),
[smaller-cut proof](research_mixed_four_left_cut_extension.md), and
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md) give
\[
 \cot(.24\pi)<129/121,\quad \tan(.10\pi)<1/3,
 \quad \tan(.18\pi)<2/3,
 \quad \cot(.36\pi)<13/25,\quad\tan(.30\pi)<3/2.
 \tag{15}
\]
For the first bound, \(\tan(.01\pi)<4/125\) and the
addition formula give \(129/121\). The only additional
witness needed is \(\tan(.18\pi)<2/3\): at
\(t=99/175>.18\pi\), the sine upper polynomial
\(s_5=t-t^3/6+t^5/120\) and positive cosine lower polynomial
\(c_6=1-t^2/2+t^4/24-t^6/720\) satisfy exactly
\[
                  (2/3)c_6-s_5
                =23076987022109/861687011718750>0.
 \tag{16}
\]
At \(x=.24\), (15) gives
\(K_0<508/121<21/5\) and
\(K_1<1403/363<39/10\). At \(x=.36\), use also
\(\tan(.22\pi)<1\) and \(\tan(.293\pi)<3/2\), giving
\(K_0<203/50<21/5\) and \(K_1<89/25<39/10\).
Integrate (13), using the zero initial derivative in Section 1,
to obtain (12).

Replacing \(c\) by the universal floor \(-.102\) is too
coarse already for the \(\beta=0\) factorial allowance.
For every \(0<H\le7/500\), the function
\((21/10)(H+51/500)^2-2H\) is decreasing and remains positive;
at its largest permitted height it equals
\[
 \frac{21}{10}\left(\frac7{500}+\frac{51}{500}\right)^2
                   -\frac{14}{500}=\frac{161}{625000}>0.
 \tag{17}
\]
Thus that worst-height vertical *upper bound*, even before adding a
horizontal gain, cannot prove a factorial gap on this height range.
This does not exhibit an actual word with positive defect. It shows
why the exact cost (7), the actual \(c\), or sharper actual-reference
information must be retained in a useful test.

## 4. An exact convex dual using whole pairs

All scalar functions below use final height \(H\) for \(z\)
and unchanged actual heights for the other four variables. Write
\(g_h(t)=\Re g(t+ih)\). Modulo real affine chirps and the
two boundary terms, minus \(f_\nu\) is the sum of four
two-variable potentials on consecutive pairs in (2):
\[
 \begin{split}
 W_1(a,u)&=(1+\alpha/2)g_{h_a}(a)+(3/2)g_{h_u}(u)
                                      -g_{h_a+h_u}(a+u),\\
 W_2(u,z)&=(3/2)g_{h_u}(u)+(1+\nu/2)g_H(z)
                                      -g_{h_u+H}(u+z),\\
 W_3(z,v)&=(1+\nu/2)g_H(z)+(1+\beta/2)g_{h_v}(v)
                                      -g_{H+h_v}(z+v),\\
 W_4(v,b)&=(1+\beta/2)g_{h_v}(v)+(1+\beta/2)g_{h_b}(b)
                                      -g_{h_v+h_b}(v+b).
 \end{split}
 \tag{18}
\]
Here the displayed arguments are real variables, rather than new
complex reference coordinates. The node coefficients add to
\((1+\alpha/2,3,2+\nu,2+\beta,1+\beta/2)\).

**Lemma 1.** Every \(W_j\) is strictly convex on its entire
real target rectangle in (2).

For an index real part at least \(.15\), the positive pair
Hessian proved in the [half-index theorem](research_mixed_half_index_contour.md)
applies to \(g(s)+g(w)-g(s+w)\) at index heights in
\([-.108,.068]\) and outer heights in \([-.12,.12]\).
All coefficients added in (18) are nonnegative multiples of
\(g_h\), whose real second derivative is nonnegative on
\((0,.5]\). Hence all these cases are strictly convex.

For an own-four index in \([.125,.15]\), use the scalar
estimates of the [smaller-cut proof](research_mixed_four_left_cut_extension.md).
Let \(q=\Re\cot\pi s>21/20\),
\(p=\Re\cot\pi w>0\), and
\(C_0=\Re\cot\pi(s+w)\). After division by \(\pi\),
the pair matrix in (18) has diagonal entries
\(3q/2-C_0,\lambda p-C_0\), with \(\lambda\ge1\),
and off-diagonal entry \(-C_0\). If \(C_0\le0\), its
Schur remainder is positive. If \(C_0>0\), the cited
estimates give \(p-C_0>3/10\), \(C_0<11/20\), so
\[
 C_0+\frac{C_0^2}{\lambda p-C_0}<\frac{187}{120},
 \qquad
 \frac32q-C_0-\frac{C_0^2}{\lambda p-C_0}
              >\frac{63}{40}-\frac{187}{120}=\frac1{60}>0.
 \tag{19}
\]
This proves the lemma, including both forced and factorial branches.

For any potential \(W\), centered at the corresponding actual
real coordinates \(x_*\) but with its stated final heights, put
\[
 D_W(d)=W(x_*+d)-W(x_*)-W'(x_*)\cdot d.
 \tag{20}
\]
Restrict this cost to its target rectangle by assigning value
\(+\infty\) outside it. Let \(\mathcal C_j=D_{W_j}\)
and use the convex conjugate convention
\(\mathcal C_j^*(p)=\sup_d(p\cdot d-\mathcal C_j(d))\).
Define the actual final horizontal gain
\(L_\nu=\max_{x\in K} f_\nu(x)-f_\nu(x_*)\).
Then
\[
 \boxed{\quad L_\nu=
 \inf_{r,t,q\in\mathbb R}\{
 \mathcal C_1^*(0,r)+\mathcal C_2^*(A-r,t)
 +\mathcal C_3^*(D_\nu-t,q)
 +\mathcal C_4^*(B-\ell-q,0)\}.\quad}
 \tag{21}
\]
Indeed the four dual vectors sum at each node to the exact gradient
(9), so Fenchel inequalities prove the upper bound. For equality,
take a maximizing point of the compact primal problem. Its gradient
condition says that the difference between (9) and the sum of the
four pair gradients is a normal vector to the product box. At each
node assign this normal component to one incident pair. Every pair
then satisfies its restricted-conjugate equality condition, with
the same primal point, and their dual forces have the form in (21).
This proves equality and attainment without evaluating that point.
The full connecting domains and their original actual centers are
retained; no conditional source root is moved.

## 5. An explicit scalar majorant, with nonconvex edges retained

Equation (21) is an exact convex formulation. The following different
decomposition makes a sufficient upper bound entirely scalar.
Let \(\phi_a,\phi_u,\phi_z,\phi_v,\phi_b\) be the
one-dimensional Bregman costs (20), on the node intervals in (2),
for the potentials
\[
 (1+\alpha/2)g_{h_a},\quad3g_{h_u},\quad
 (2+\nu)g_H,\quad(2+\beta)g_{h_v},\quad(1+\beta/2)g_{h_b}.
 \tag{22}
\]
For the four consecutive edges, let \(\chi_j\) be the
Bregman cost of \(-g_{h_i+h_{i+1}}\), centered at the actual
sum of the real coordinates. Restrict its target interval to the
sum of the two corresponding node intervals. Thus its upper endpoint
is \(.95\), while its lower endpoint is either \(.345\)
or \(.37\).

**Proposition 2.** For every four real trial flows \(w_1,\ldots,w_4\),
\[
 \begin{split}
 L_\nu\le\mathcal E_\nu(w):={}&
 \phi_a^*(-w_1)+\phi_u^*(A-w_1-w_2)
 +\phi_z^*(D_\nu-w_2-w_3)\\
 &+\phi_v^*(B-\ell-w_3-w_4)+\phi_b^*(-w_4)
                      +\sum_{j=1}^4\chi_j^*(w_j).
 \end{split}
 \tag{23}
\]
The infimum over trial flows is still an upper bound; equality is
not asserted for this scalar relaxation.

To prove (23), expand the Bregman identity for minus \(f_\nu\)
using (22) and the four edge potentials. Apply the defining conjugate
inequality to each term. The edge linear forms are the adjacent-node
sums, and their coefficients cancel the four subtractions in (23).
Fenchel's elementary upper inequality is valid for the edge costs
whether or not they are convex.

That qualification is essential. Each edge interval crosses
\(1/2\), and
\[
                (-g_h)''(t)=-\pi\Re\cot\pi(t+ih)<0
                         \qquad(0<t<1/2).
 \tag{24}
\]
Thus the separated edge costs need not be nonnegative. In particular
\(\chi_j^*(0)\) cannot be discarded merely because its argument
is zero. The reference center of the internal own-four edge
\(u+z\) is itself only proved greater than \(.49\) in
the pattern \((3,4,3)\). In contrast, the whole convex pair
costs in (21) are nonnegative. Their allocation is what preserves
the exact convex dual.

Every scalar conjugate in (23) has an explicit finite evaluation
rule on its closed interval. Put
\[
 N_h(t)=1+e^{4\pi h}-2e^{2\pi h}\cos(2\pi t).
 \tag{25}
\]
For a node potential \(m g_h\), its conjugate maximizer is the
clipped solution on \(0<t\le1/2\) of
\[
                    N_h(t)=N_h(t_*)e^{2p/m}.
 \tag{26}
\]
The derivative is strictly increasing before \(1/2\), so an
out-of-range force selects the appropriate endpoint. The value is
the original scalar objective \(p(t-t_*)-D_{m g_h}(t-t_*)\).

For an edge, its conjugate objective is convex below \(1/2\)
and strictly concave above \(1/2\). Its global maximum is the
larger of its value at the left interval endpoint and its maximum
on \([1/2,.95]\). The latter is the clipped solution of
\[
                    N_h(t)=N_h(t_*)e^{-2p}
                         \qquad(1/2\le t\le.95).
 \tag{27}
\]
Endpoint clipping includes the value at \(1/2\), so these two
candidates exhaust the full interval. The trigonometric branch in
(27) is the one with \(t\ge1/2\). The actual center \(t_*\)
is never moved to that branch or clipped when it appears on the
right side. These scalar choices are conjugate evaluations, not
solutions of a source critical equation.

## 6. A fully specified one-parameter trial and the missing signs

For a simpler sufficient trial choose any real \(\theta\), and
put
\[
 w_1=w_4=0,\qquad w_2=\theta A,\qquad
 w_3=D_\nu-\theta A,\qquad
 R_\nu=3C-\ell-(1-\theta)A-(1-\nu)G_H.
 \tag{28}
\]
The node forces become \((0,(1-\theta)A,0,R_\nu,0)\).
Since every node cost is convex and its center belongs to its
interval, its zero-force conjugate equals zero. Consequently
\[
 \begin{split}
 L_\nu\le\mathcal E_{\nu,\theta}:={}&
 \phi_u^*((1-\theta)A)+\phi_v^*(R_\nu)
 +\chi_1^*(0)+\chi_2^*(\theta A)\\
 &+\chi_3^*(D_\nu-\theta A)+\chi_4^*(0).
 \end{split}
 \tag{29}
\]
The two zero-force edge terms remain. For example
\(\Theta=\{0,1/4,1/2,3/4,1\}\) is a finite collection
of explicitly specified trials; neither their quality nor any
uniform sign is assumed. Allowing nonzero \(w_1,w_4\) in
(23) retains additional incoming and outgoing pair cost and can
improve this simpler bound.

**Theorem 3 (central sufficient budget).** For either Fourier
alternative and all main/main targets,
\[
 \max_{x\in K}f_\nu(x)-M
      \le T_\nu+\inf_{w\in\mathbb R^4}\mathcal E_\nu(w)
      \le T_\nu+\min_{\theta\in\Theta}\mathcal E_{\nu,\theta}.
 \tag{30}
\]
In particular a sufficient common central gap \(\delta>0\) is
the pair of reference-only inequalities
\[
 \boxed{\quad
 T_\nu+\min_{\theta\in\Theta}\mathcal E_{\nu,\theta}
                 \le-\delta,\qquad \nu=0,1,\quad}
 \tag{31}
\]
or the stronger four-flow version using any admissible trial flows
in (23). The exact grouped-pair dual (21) is another possible
upper evaluation of the same gain. The vertical estimate (12)
may replace \(\mathcal V\) in \(T_\nu\), subject to
the limitation in (17).

The proof is simply the exact trial identity (9), followed by the
horizontal gain bounds. Treating \(\nu=0\) directly keeps
its negative actual \(\Re g(z_H^*)\) credit and its changed
gradient and curvature. It does not bound a forced optimizer by a
factorial optimizer or assume a ceiling for either one.

All quantities in (6)--(31) come from the same actual coupled
reference, including both boundary marginals, all four fixed heights,
the centered edge sums and the outgoing coordinate. No independent
worst-case replacement of these data enters the formulas. Equations
(31), or an improved admissible trial version, remain unproved.
Even their proof would settle only the main/main term of the
32-term finite-source envelope. Its remaining currents, and the
128-term problem with both first coordinates selected, remain open;
no global filling-volume statement is concluded here.
