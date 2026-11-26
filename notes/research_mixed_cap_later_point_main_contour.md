# An outer-cap main contour at the exact later incoming point

Research deduction, 8 November 2026. An early departure from the
auxiliary-real curve gives a descending outer-cap main path through
the exact later critical point. The lower physical cap rows and
the entire unweighted left join have strict own-action gaps there.
The construction concerns the original finite row and its actual
constant-mode integral, with the original density \(+N\).

The main-integral conclusion below is conditional on the explicit
endpoint-source premise (W). That premise extends farther left than
the currently assembled rectangle starting at \(6/25\). The phase
comparisons and lower-row conclusion are unconditional. No
whole-cap or knot-family asymptotic is inferred, and no numerical
evaluation is used.

## 1. Source, point, and the additional source premise

Use the original cap row and phases:
\[
 \begin{split}
 U_{0,N}(w,e^{-2\pi ia})
  &=\sum_{j=0}^{N-1}H_N(w,r^{-j})\,p_j(e^{-2\pi ia})/P_j,\\
 \mathscr A_N(e,a,w)
  &=D_N(e)^{-1}C_N(e,w)\,\Pi_N(a+e)/\Pi_N(a),\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e,w)&=F(e,u_c(e))\quad(w=-2),\\
 \Psi(e,a,w)&=S(e,w)+J(a+e)-J(a)-i\pi ae.
 \end{split}                                                     \tag{1}
\]
At \(e=j/N\), the second line is exactly the physical row in
the first. The definitions, factorials, primitive constants, and
ordinary-color continuation are those of
[the original cap contour](research_mixed_cap_outer_contour_reduction.md).
No endpoint coefficient is divided out of the finite source.

Set
\[
 \begin{gathered}
 e_0=\frac14-\frac{i\log2}{4\pi},\quad h_0=\Im e_0,\quad
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\quad
 a_0=1-\frac{\Arg X_0}{2\pi},\\
 \mathcal T_0=\Psi(e_0,a_0,-2),\qquad M_0=\Re\mathcal T_0.
 \end{gathered}                                                   \tag{2}
\]
The original selected branch satisfies
\(1/2<a_0<7/10\), \(\Psi_e(e_0,a_0,-2)=0\), and
\[
              \Psi_{ee}(e_0,a_0,-2)
                       =-4\pi\sqrt2+8\pi i/3.                  \tag{3}
\]
These are the exact identities of
[the local curve obstruction](research_mixed_cap_auxiliary_real_curve_obstruction.md).

The available complete source on the auxiliary-real curve and
above it is given by
[the curve theorem](research_mixed_endpoint_auxiliary_real_curve.md)
and [the above-curve region](research_mixed_endpoint_region_above_real_curve.md).
For the new downward connection we require:

**(W)** On a fixed open neighborhood of
\[
 \{e:23/100\le\Re e\le49/100,\quad-3/50\le\Im e\le0\}
                 \times\{-2\},
 \tag{4}
\]
the whole original \(C_N(e,w)\) has its nonzero
\(N^{-3/2}A(e,w)e^{NS(e,w)}(1+O_{\rm hol}(N^{-1}))\)
asymptotic, with the same phase, symbol, parities, and fixed
normalized mixed derivatives.

This is an explicit source-domain premise, not an appeal to
unspecified neighborhood widths. It is sufficient to combine a
below-curve source extension through real part \(23/100\) with
the above-curve region and
[the assembled lower rectangle](research_mixed_endpoint_complete_lower_rectangle.md).
Until that extension is proved, conclusions using (W) remain
conditional.

## 2. A strictly subcritical departure point

Use the curve
\[
 p(t)=1-2t^2+2it,\qquad e(t)=\frac{\Log p(t)}{2\pi i},\qquad
 \frac{\sqrt3-1}{2}\le t\le\frac1{\sqrt2}.
 \tag{5}
\]
Write \(\sigma=\sqrt2,\ q=\sqrt2t,\ d=1-q\), and keep the exact
multiplier and logarithmic polynomial in equations (3)--(10) of
[the departure-barrier proof](research_mixed_cap_curve_departure_barrier.md).
We use the same expressions on the slightly longer interval
\(0\le d\le1/12\). Their logarithmic remainder is now bounded by
\[
 |\mathcal R(d)|\le225d^4,
 \tag{6}
\]
since the factored logarithms give
\[
 \frac{4+2(33/8)^4}{4(1-33/96)}<225.
 \tag{7}
\]
Indeed the numerator is less than \(584\), the denominator is
\(21/8\), and \(4672<4725\). No root or action is evaluated.

With \(\phi(d)=\Re\Psi(e((1-d)/\sqrt2),a_0,-2)\), the same
polynomial multiplication yields
\[
 \left|\phi'(d)-\frac{\sigma}{\pi}
       \left(\frac d3-\frac{74d^2}{9}-\frac{974d^3}{81}\right)
 \right|\le\frac{500}{\pi}d^4.
 \tag{8}
\]
Here the rational factor \(W=(1+q^4)^{-1}\) is at most \(2/3\),
because \(q\ge11/12>9/10\) and \((9/10)^4>1/2\).
Thus the logarithmic error contributes less than
\(225(1+\sqrt2)(2/3)d^4<375d^4\) before the factor \(1/\pi\).
The exact bound
\(|W-(1/2+d+d^2/2)|\le2d^3\) still holds.
The numerator polynomial \(\sqrt2P(d)\) in the cited proof has
modulus less than \(4d\), using its coefficient bounds
\(1,18,11,30,42,15\).
The corresponding rational-factor error is less than \(8d^4\).
The remaining terms of degree at least four contribute less
than \(83d^4\): respectively \(51,14,18\) for the three groups
used in that proof. Their sum is less than \(500d^4\), proving
(8). At \(d=0\) all remainder statements hold by equality.

At \(D=1/12\), integration gives the strict upper bound
\[
 \begin{split}
 \phi(D)-M_0
 &\le\frac{D^2}{\pi}
       \left\{-\frac{1927\sqrt2}{23328}+\frac{25}{432}\right\}\\
 &<-\frac{6739}{116640\pi}D^2<0,
 \end{split}                                                     \tag{9}
\]
where \(\sqrt2>7/5\) was used only in the last inequality.
Define
\[
 q_d=11/12,\qquad t_d=11/(12\sqrt2),\qquad
                 e_d=e(t_d)=E_d-i\eta_d.
 \tag{10}
\]
Its real part lies in the desired source corridor:
\[
                      23/100<E_d<6/25.
 \tag{11}
\]
Indeed
\[
 \cot(2\pi E_d)=\frac{23}{132\sqrt2}
       <\frac{115}{924}<\frac18<\tan(\pi/25),
 \qquad
 \cot(2\pi E_d)>\frac{23}{198}>
                  \frac{11}{164}>\tan(\pi/50).
 \tag{12}
\]
The elementary tangent bounds are the ones written in the
departure-barrier proof. Finally \(0<\eta_d<-h_0<3/50\),
because the curve radius increases strictly with \(t\).

## 3. The entire earlier curve is below the departure value

For the original lift, write \(L=\exp\Psi_e=A-iB\).
On the curve up to \(q_d\),
\[
 A=\frac{10q-3q^3-4}{3q^3}>1,\qquad
 B=\frac{2\sqrt2(1-q)(3q+2)}{3q^3}>0,\qquad
 m(q)=\frac{\sqrt2q^3}{1+q^2}.
 \tag{13}
\]
The curve has positive real derivative, and
\[
 \frac{d\,\Re\Psi(e(q/\sqrt2),a_0,-2)}{dE}
                       =\log|L|-m(q)\arctan(B/A).
 \tag{14}
\]
Its left endpoint has \(q_-=(\sqrt6-\sqrt2)/2>1/2\).

For \(q_-\le q\le4/5\), differentiation gives
\[
 A'(q)=\frac{4(3-5q)}{3q^4},\qquad B'(q)<0.
 \tag{15}
\]
Thus \(A\ge77/48\), \(B\ge55\sqrt2/48\), and
\[
 |L|^2\ge11979/2304>81/16,\qquad
 m(q)\le64\sqrt2/205<9/20.
 \tag{16}
\]
It follows that (14) is greater than
\(\log(9/4)-9\pi/40>4/5-99/140>0\).

For \(4/5\le q\le11/12\), (15) and monotonicity of \(m\) give
\[
                 A\ge1645/1331>6/5,\qquad m<3/5.
 \tag{17}
\]
For any \(A>0\), the minimum over \(B\ge0\) of
\(\log\sqrt{A^2+B^2}-(3/5)\arctan(B/A)\) occurs at
\(B=3A/5\). Its value is
\[
 \log A+\tfrac12\log(34/25)-\tfrac35\arctan(3/5)>0
                                      \quad(A\ge6/5).
 \tag{18}
\]
For explicit witnesses,
\[
 \log(6/5)+\tfrac12\log(34/25)>
       \frac2{11}+\frac9{59}=\frac{217}{649}>\frac13,
 \qquad
 \frac35\arctan(3/5)
 <\frac{25479}{78125}<\frac13.
 \tag{19}
\]
The arctangent bound uses its first three alternating terms.
Equations (17)--(19) prove that (14) is positive in this range
as well.

Consequently the entire curve segment from its \(E=1/8\)
endpoint to \(e_d\) has action at most \(\Re\Psi(e_d,a_0,-2)<M_0\).
This leaves the terminal ascending segment of the original curve
unused, as required by the obstruction.

## 4. The real lower cut and all lower physical rows

Let \(e_L=1/8-i\eta_L\) be the left endpoint of (5).
Since \(t_-^2=1-\sqrt3/2<1/7\),
\[
 \eta_L=\frac{\log(1+4t_-^4)}{4\pi}
                              <\frac1{49\pi}.
 \tag{20}
\]
For \(q_-\le q\le7/10\), the same formulas give
\[
 |L|>B(7/10)=820\sqrt2/343>10/3,\qquad m(q)<1/3.
 \tag{21}
\]
The two positive logarithmic-series terms show
\(\log(10/3)>7784/6591>7/6\). Hence (14) exceeds \(9/14\).
At \(q=7/10\), \(p=51/100+7\sqrt2\,i/10\) has argument
greater than \(\pi/3\), since \(9800>7803\). Its real
private part therefore exceeds \(1/6\). The curve rise
between \(e_L\) and that point is greater than
\[
                    (9/14)(1/6-1/8)=3/112.
 \tag{22}
\]
Sections 2--3 then give \(M_0-\Re\Psi(e_L,a_0,-2)>3/112\).

On the vertical segment \(1/8+i[-\eta_L,0]\), the above-curve
source theorem gives the original chamber and
\(\Im S'(e)>0\). Also
\(\Arg\sin\pi(a_0+e)\ge0\). Thus
\[
 \partial_h\Re\Psi(1/8+ih,a_0,-2)
       =-\Im S'(e)-\Arg\sin\pi(a_0+e)+\pi a_0
                                    <7\pi/10.
 \tag{23}
\]
Its total upward increase is less than \(1/70\), by (20).
We have proved the strict real-cut gap
\[
             M_0-\Re\Psi(1/8,a_0,-2)>3/112-1/70=1/80.
 \tag{24}
\]
The negative real Hessian of \(F\) is positive definite in
its original chamber; the Schur derivative gives \(-\Re S''>0\).
Since \(1/2<a_0+\Re e<1\), the outer cotangent strengthens this:
\[
                        -\Re\Psi_{ee}>0.
 \tag{25}
\]
Vertical convexity therefore pays the entire unweighted join
from the real cut to \(e_L\), using (22) and (24).
The exact complete endpoint packet holds on this join.

The corresponding physical row profile is
\[
 R(e,a_0)=h(e)+B_v(e),\quad
 h(e)=\Re S(e)+J(e),\quad
 B_v(e)=J(e-v)+J(v)-J(e),\quad v=1-a_0>3/10.
 \tag{26}
\]
The whole-coefficient bounds and profile identities in
[wrapped-row transport](research_mixed_cap_wrapped_row_transport.md)
give \(h'(e)>0\) on \(0<e<1/2\). For \(0<e\le1/8<v/2\),
\[
 B_v'(e)=\log\frac{\sin\pi(v-e)}{\sin\pi e}>0.
 \tag{27}
\]
Thus every compact lower physical row is bounded by the cut
value in (24). The true lower endpoint is treated separately:
the positive full-coefficient endpoint bound has rate \(3/5\),
whereas the cap-wall theorem gives \(M_0>41/60\).
After a fixed tolerance and polynomial row count, for some
\(\gamma_L>0\),
\[
 \sum_{j=0}^{\lfloor N/8\rfloor}
  \left|H_N(w,r^{-j})p_j(e^{-2\pi ia_0})/P_j\right|
                    \le CN^B e^{N(M_0-\gamma_L)}.
 \tag{28}
\]
This positive estimate holds for every real ordinary color,
including numerator zeros and both parities. Each fixed real
ordinary derivative has polynomial cost by the original
whole-coefficient estimates. On a sufficiently small complex
complete-color/incoming neighborhood it also has the local
normalized mixed-derivative conclusion. No bound for a signed
whole cap has been assigned to a partial sum.

## 5. The actual main integral, conditional on (W)

Choose the fixed upper proof cut \(b=b(a_0)\) from
[the upper-end current theorem](research_mixed_cap_upper_end_currents.md):
\[
 b=\min\{49/100,1-a_0-\delta\}>1/4,\qquad a_0+b<1-\delta.
 \tag{29}
\]
Its full upper physical tail, right unweighted join, and short
weighted right sides are paid independently by that theorem.
Use the exact half-grid cuts
\[
 L_N=\lfloor N/8\rfloor+1,\quad K_N=\lceil Nb\rceil,\qquad
 \ell_N=(L_N-1/2)/N,\quad b_N=(K_N-1/2)/N.
 \tag{30}
\]
They retain precisely the original private rows
\(L_N\le j<K_N\).

The following oriented path runs from \(\ell_N\) to \(b_N\):

1. the real segment from \(\ell_N\) to \(1/8\), then the
   vertical join to \(e_L\);
2. the curve (5) from \(e_L\) to \(e_d\);
3. the vertical segment from \(e_d\) down to \(E_d+ih_0\);
4. the horizontal segment from \(E_d+ih_0\), through \(e_0\),
   to \(b_N+ih_0\);
5. the right vertical join to \(b_N\).

All these are contours of the literal function \(\mathscr A_N\).
Under (W), their full endpoint symbols are available: the first
two pieces use the curve/above-curve theorems; the last three
lie in (4), up to the permitted \(O(N^{-1})\) cut shifts.
Every outer factorial stays in its original regular strip.

Equation (25) gives strict horizontal concavity at height \(h_0\).
Since \(e_0\) is stationary, the fourth piece has its unique
maximum \(M_0\) there. At the lower endpoint of the third piece
its action is strictly below \(M_0\); at the upper endpoint
this is (9). Vertical convexity pays that whole connector.
Sections 3--4 pay the first two pieces. The upper-end theorem
pays the last join. The small real segment at \(\ell_N\)
retains (24) by continuity. Thus every fixed portion away from
the saddle has a uniform strict gap.

The path and the real interval have the same endpoints and
are homotopic in the holomorphy domain of the exact finite row.
Their integrals, with the original \(+N\), are equal. In particular
the actual constant-mode contribution
\[
       \mathcal I_N(a,w)
                  :=N\int_{\ell_N}^{b_N}\mathscr A_N(e,a,w)\,de
 \tag{31}
\]
has, on a fixed sufficiently small complex neighborhood of
\((a_0,-2)\),
\[
 \mathcal I_N(a,w)=
       N^{-1}\mathcal B(a,w)e^{N\mathcal T(a,w)}
                              (1+O_{\rm hol}(N^{-1})),
                    \qquad \mathcal B(a,w)\ne0.
 \tag{32}
\]
Here \(\mathcal T(a,w)=\Psi(e_*(a,w),a,w)\) is the original local
critical action, continued from (2). If \(A(e,w)\) denotes the
endpoint coefficient in (W), the coefficient is
\[
 \mathcal B(a,w)=
 \frac{\sqrt{2\pi}\,A(e_*,w)}
       {\sqrt{-\Psi_{ee}(e_*,a,w)}}
             \sqrt{\frac{\sin\pi(a+e_*)}{\sin\pi a}}.
 \tag{33}
\]
All branches are the original ones. The exact cap-row symbol is
\(N^{-3/2}A(e,w)\sqrt{\sin\pi(a+e)/\sin\pi a}\,e^{N\Psi}\);
the density \(N\) and the full interior Gaussian \(N^{-1/2}\)
give precisely \(N^{-1}\). The saddle is crossed horizontally,
not used as an integration endpoint.

For (32), hold the integer cuts and all base paths fixed before
varying \(a,w\). The strict gaps persist on small fixed
neighborhoods; a local contour adjustment inside the regular
saddle chart proves the holomorphic expansion. A common shrink
works for the \(O(N^{-1})\) endpoint shifts. Cauchy's formula
then gives every fixed derivative of the normalized error on
smaller neighborhoods. Neither a cutoff nor a parameter-dependent
path is differentiated.

This conclusion retains the actual incoming normalization and
both level parities. It proves neither the remaining outer aliases
nor a complete cap asymptotic. Although separate tall horizontal
aliases are now bounded, replacing a shorter residue rectangle
by a tall one also retains its long side currents. Those currents,
and extension from this fixed incoming neighborhood to the whole
real arc, remain separate obligations.
