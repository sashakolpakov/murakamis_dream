# A complete endpoint corridor below the auxiliary-real curve

Research deduction, 8 November 2026. The complete endpoint packet
extends through a closed private corridor below the auxiliary-real
curve, down to depth \(3/50\), for real parts between \(6/25\) and
\(27/100\), wherever the curve itself is no deeper than \(3/50\).
The proof uses explicit critical-point bounds and a right
auxiliary cut at \(E-1/1000\). The earlier real-tail theorem already
controls every row beyond that later cut.

Every original row, reflected zero, alias and unweighted join is
retained. This proves an endpoint-source theorem, not an outer-cap
action comparison. No numerical evaluation is used and earlier
frozen files are unchanged.

## 1. Exact function and the corridor

Keep the full finite function
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^l2\sin(\pi j/N),
 \tag{1}
\]
and its original complete-color phase
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\qquad
 S(e)=F(e,u_c(e)).
 \tag{2}
\]
The normalization and zero-safe finite rows are those of
[the specified complex-index coefficient](research_complete_boundary_complex_index.md).

For \(E\in[6/25,27/100]\), let \(\eta_0(E)\) be the unique depth
on the [auxiliary-real curve](research_mixed_endpoint_auxiliary_real_curve.md):
\[
 p_0=1-2t^2+2it,\quad
 E=\frac{\arg p_0}{2\pi},\quad
 \eta_0(E)=\frac{\log|p_0|}{2\pi}.
 \tag{3}
\]
Its real part and radius increase with \(t\). Beyond \(E=1/4\)
this uses the same explicit parametrization, not an already proved
endpoint packet there. Equivalently, with
\(c_0=\cos(2\pi E)\),
\[
 R_0(E)=e^{2\pi\eta_0(E)}
       =\frac{2}{c_0+\sqrt{2-c_0^2}}.
 \tag{4}
\]
Define the closed corridor
\[
 \mathcal K_-=
 \{e=E-i\eta:6/25\le E\le27/100,\quad
                         \eta_0(E)\le\eta\le3/50\}.
 \tag{5}
\]
For \(E\le1/4\) it is nonempty, since
\(\eta_0(E)\le\log2/(4\pi)<3/50\). For a later \(E\) with
\(\eta_0(E)>3/50\), its vertical section is empty. No point above
the curve is included by that convention.

**Theorem.** On a fixed complex neighborhood of
\(\mathcal K_-\times\{-2\}\), the complete source (1) satisfies
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
 \tag{6}
\]
The phase, amplitude and accretive square root are the original
endpoint ones. Both level parities and every fixed mixed
ordinary-color/index derivative of the normalized error are included
on smaller neighborhoods.

## 2. Explicit critical-point bounds throughout the corridor

Put \(p=e^{2\pi ie}=Re^{2\pi iE}\), \(c=\Re p\), and write
\[
 \sqrt{1-2p}=A-iB,\qquad A>0,\ B>0,\qquad
 z=\frac{i+\sqrt{1-2p}}2
      =\frac A2-\frac{i(B-1)}2,\qquad
 u_c=\frac{\arctan z}{\pi}.
 \tag{7}
\]
These are the original branches. On the curve (3), \(B=1\)
and \(u_c\) is its real original critical point.

Throughout the corridor \(R<22/15\). On its part \(E\le1/4\),
\[
 R<22/15,\qquad 0\le c<1/10.
 \tag{8}
\]
Indeed \(2\pi\eta\le3\pi/25<66/175<14/37<\log(22/15)\),
where the last strict logarithm bound is the first positive
\(2\operatorname{atanh}(7/37)\) term. Also
\[
 c\le R\sin(\pi/50)
     <(22/15)(11/175)=242/2625<1/10.
\]

The exact square-root identities are
\[
 A^2=\frac{\sqrt{1-4c+4R^2}+1-2c}{2},\qquad
 B^2=\frac{\sqrt{1-4c+4R^2}-1+2c}{2}.
 \tag{9}
\]
At fixed \(E\), \(B^2\) increases strictly with \(R\).
For \(c_0\ge0\) this follows immediately from its derivative
\[
 \frac{2R-c_0}{\sqrt{1-4Rc_0+4R^2}}+c_0>0.
\]
When \(c_0<0\), the same derivative is positive: squaring the
positive terms in
\((2R-c_0)/\sqrt{1-4Rc_0+4R^2}>-c_0\) gives the strict
difference \(4R(1-c_0^2)(R-c_0)>0\).
Thus \(B\ge1\) throughout (5). For fixed \(R>1\), the second
expression in (9) also increases with \(c\), since its derivative
is \(1-1/\sqrt{1-4c+4R^2}>0\). Therefore (8) gives
\[
 B^2<
 \frac{\sqrt{2071}/15-1+1/5}{2}
 <\frac{17}{15}<\left(\frac{16}{15}\right)^2.
\]
The first expression in (9) decreases with \(c\), so
\[
 A^2<
 \frac{\sqrt{2161}/15+1}{2}
 <\frac{31}{15}<\left(\frac{36}{25}\right)^2.
\]
Finally \(A^2=B^2+1-2c>9/5>(4/3)^2\). On \(E\le1/4\) we have proved
\[
               \frac43<A<\frac{36}{25},\qquad
                         1\le B<\frac{16}{15}.
 \tag{10}
\]

Write \(u_c=\xi+ih_c\). Equation (10) makes the real part of
\(z\) greater than \(2/3\), and its imaginary part belongs to
\((-1/30,0]\). The real part of \(\arctan(x+iy)\) increases
with \(y^2\) in this range, so
\(\xi>\arctan(2/3)/\pi>1/6\). More explicitly,
\[
 \tan(2\pi\xi)
   =\frac{4A}{4-A^2-(B-1)^2}
   <\frac{144/25}{4-1296/625-1/225}<3.
 \tag{11}
\]
The denominator is positive. The last comparison is the exact
integer inequality \(32400<32433\), after multiplying by \(5625\).
As \(0<\xi<1/4\) and \(\tan(2\pi/5)=\sqrt{5+2\sqrt5}>3\),
(11) gives \(\xi<1/5\).

On the vertical segment from \(A/2\) to \(z\), the real part
of the arctangent derivative is positive and at most
\[
 \frac1{1+(2/3)^2-(1/30)^2}=\frac{300}{433}<\frac7{10}.
\]
Hence
\[
 \boxed{\quad
 \frac16<\xi<\frac15,\qquad
 -\frac{7}{300\pi}<h_c\le0,\qquad |h_c|<\frac1{120}.
 \quad}
 \tag{12}
\]
The last inequality uses \(\pi>14/5\).

For \(E\ge1/4\), one instead has \(c\le0\). Since \(B\ge1\),
\[
 R^2=c^2+B^2(B^2+1-2c)\ge(1-c)^2+1.
\]
Therefore \(c>1-\sqrt{259}/15>-11/150\), using
\(\sqrt{259}<161/10\). Monotonicity of the second expression
in (9) in \(c\) gives
\[
 B^2<16/15<(31/30)^2,\qquad
 A^2=B^2+1-2c<166/75<(3/2)^2,\qquad A>4/3.
\]
The same arctangent argument gives \(\xi>1/6\) and
\(-1/120<h_c\le0\). Its upper real bound is now
\[
 \tan(2\pi\xi)
  <\frac{6}{4-9/4-1/900}
  =\frac{2700}{787}<\frac72<\cot(2\pi/25),
 \qquad \xi<21/100.
 \tag{12a}
\]
For the last trigonometric inequality, use
\(\tan z\le z/(1-z^2/2)\) at \(z=2\pi/25<44/175\);
the resulting upper bound is less than \(2/7\).
Thus the unified bounds needed below are
\[
 \frac16<\xi<
 \begin{cases}1/5,&E\le1/4,\\21/100,&E\ge1/4,\end{cases}
 \qquad -\frac7{300\pi}<h_c\le0,\qquad |h_c|<1/120.
 \tag{12b}
\]
In particular \(0<\xi<E\), so every original primitive is regular.
The critical point remains simple by \(-\Re F_{uu}>0\) in that
chamber. The exponentiated original equation holds by (7), and its
zero logarithmic lift continues from (3), without crossing any
primitive wall. These are the same branch and action as in the
[bridge phase theorem](research_mixed_endpoint_bridge_phase_floor.md).

We will need a lower depth bound as well:
\[
                            \eta>\frac3{64}.
 \tag{13}
\]
The radius \(R_0(E)\) is increasing. At \(E=6/25\), its equation is
\[
 (1-c_0^2)R_0^2+2c_0R_0-2=0,\qquad
                         c_0=\sin(\pi/50)<11/175.
\]
At \(R=27/20\), its left side is less than
\[
 \frac{729}{400}+\frac{297}{1750}-2=-\frac{109}{14000}<0.
\]
The quadratic increases on the positive axis. Thus \(R\ge R_0>27/20\).
Using \(\log(27/20)>14/47\) and \(\pi<22/7\) gives
\[
       \eta>\frac7{47\pi}>\frac{49}{1034}>\frac3{64},
\]
where the last comparison is \(3136>3102\).

## 3. Two real cut gaps from explicit Hessian cones

Use the auxiliary real cuts
\[
                   a=\frac1{20},\qquad b(E)=E-\frac1{1000}.
 \tag{14}
\]
These are strictly on opposite sides of \(\xi\). On each straight
segment from \(u_c\) to one of these real cuts, \(0<\Re u<E<1/2\),
\(-1/120<\Im u\le0\), and
\[
 -F_{uu}/\pi=2\tan\pi u+3\cot\pi u+\cot\pi(e-u).
 \tag{15}
\]

The first two terms, denoted \(A_0+iB_0\), obey the elementary
estimates from the identities in Section 4 of
[the actual cap-path bridge](research_mixed_endpoint_actual_cap_path_bridge.md):
\[
 \begin{array}{lll}
 A_0>4,& |B_0|<A_0/5,&1/20\le\Re u\le21/100,\\
 A_0>24/5,& |B_0|<A_0/15,&1/6\le\Re u\le27/100.
 \end{array}
 \tag{16}
\]
For clarity, those estimates use only
\(\sinh(2\pi|\Im u|)<1/18\), and respectively
\(\sin(2\pi\Re u)>3/10\) or \(>6/7\).
They do not depend on a cap critical-point relation. The second
sine bound remains valid up to real part \(27/100<1/3\), so
the same calculation gives the slightly longer interval in (16).

The last term in (15) has positive real part. Put
\(q=-\pi\Im(e-u)\). Equations (12)--(13) give throughout both
segments
\[
       \frac{563}{4800}
          =\frac9{64}-\frac7{300}<q<\frac15.
\]
Since \(\coth q<1/q+q\) for \(q>0\), it follows that
\[
 0<\Im\cot\pi(e-u)\le\coth q
             <\frac{4800}{563}+\frac15<9.
 \tag{17}
\]
The bound for \(\coth\) follows by differentiating
\((1+q^2)\sinh q-q\cosh q\), whose derivative
\(q\sinh q+q^2\cosh q\) is positive.

Write \(F_{uu}=-A_*+iB_*\), with \(A_*>0\). From (16)--(17),
\[
 |B_*|<(5/2)A_*\ \text{on the left segment},\qquad
 |B_*|<2A_*\ \text{on the right segment}.
 \tag{18}
\]
Indeed \(1/5+9/4=49/20<5/2\), and
\(1/15+45/24=233/120<2\).
The ratios of imaginary to real displacement from \(u_c\) are
bounded by
\[
 m_L<\frac{1/120}{1/6-1/20}=\frac1{14},\qquad
 m_R<\frac{1/120}{6/25-1/1000-1/5}=\frac{25}{117}.
 \tag{19}
\]
For the second expression, when \(E\ge1/4\) use instead
\(b(E)-\xi>1/4-1/1000-21/100=39/1000\), the same denominator.
Both cone brackets are strictly positive:
\[
 1-m_L^2-5m_L>\frac{125}{196}>0,\qquad
 1-m_R^2-4m_R>\frac{1364}{13689}>0.
 \tag{20}
\]
Since the original \(F_u(e,u_c)=0\), the exact second-order integral
along either segment, using (18)--(20), proves
\[
                \Re F(e,a)<\Re S(e),\qquad
                \Re F(e,b(E))<\Re S(e).
 \tag{21}
\]
Compactness gives a uniform strictly positive minimum of these two
gaps. No numerical minimum is needed.

## 4. All real rows and all finite currents

The entire corridor (5) lies in the domain of
[the original bridge real-tail theorem](research_mixed_endpoint_bridge_real_tails.md).
Its lower cut is the same \(a=1/20\). Its upper force decreases
on every real \(x\ge E-1/100\) up to one half. Therefore that
very same monotonicity applies after the later cut
\(b(E)=E-1/1000\); all rows beyond \(b(E)\) and below one half
reduce to the second value in (21).
This is a restriction of the proved force interval, not an
estimate on a signed partial coefficient.

Every upper-half row has rate less than \(67/105\), whereas
the [original bridge phase floor](research_mixed_endpoint_bridge_phase_floor.md)
gives \(\Re S>1511/2000\), with reserve greater than \(1/10\).
Thus (21) and these sourcewise bounds pay the complete omitted
finite row inventory, including the final row, every revived row
past the private endpoint, both parities, and reciprocal zeros.
The original carrier \(e^{i\pi e l}\) is already in the rates.

For each base parameter keep exactly
\[
 \begin{gathered}
 L_N=\lceil Na\rceil,\quad M_N(E)=\lceil Nb(E)\rceil,\qquad
 a_N=(L_N-1/2)/N,\quad b_N=(M_N(E)-1/2)/N.
 \end{gathered}
 \tag{22}
\]
The retained indices are \(L_N\le l<M_N(E)\). The same original
regular row interpolation and \(N^{-2}\) nonzero symbol used in
the auxiliary-real curve theorem apply throughout the retained
strip \(a\le\Re u\le b(E)\). Here \(E-\Re u\ge1/1000\), so
there is no new factorial wall.

The signed-height contour proof of
[the deeper endpoint extension, Section 4](research_mixed_endpoint_cap_rectangle_deeper_extension.md)
now applies with these cuts and the independently proved gaps (21).
To record its actual comparisons, put \(H=-h_c\ge0\).
The main line is the lower line through the original saddle.
For \(H>0\), exact reflection gives on the opposite upper alias
\[
 \Re F(e,x+iH)-2\pi H
                  \le\Re S(e)-\pi(1+2E)H.
 \tag{23}
\]
The alias on the main side loses \(2\pi H\). The reflection uses
\[
 \Re F(e,x-iH)-\Re F(e,x+iH)
 =2\pi EH+\int_{-H}^{H}\Im J'(e-x+is)\,ds,
 \qquad \left|\int_{-H}^{H}\Im J'(\cdot)\,ds\right|\le\pi H,
\]
on \(0<E-x<1/2\), with the unchanged logarithmic branches.
All weighted vertical sides have convex rates after subtracting
the linear alias penalty, so their paid real and horizontal
endpoints pay the whole sides. The two unweighted joins are
also bounded by their paid endpoints through vertical convexity.
The main line is strictly horizontally concave, with its unique
maximum at \(u_c\).

If \(H=0\), use instead a small fixed symmetric rectangle.
On the real retained segment
\(\Im F_u=\Arg\sin\pi(e-x)+\pi E\in(-\pi/2,27\pi/100)\).
It consequently retains \(|\Im F_u|<\pi\) at sufficiently small
outer heights, and both complete cut sides keep (21).
Both horizontal aliases then have a strict positive loss.
For \(H>0\), the outer heights can be enlarged slightly beyond
\(\pm H\) while spending only a part of their strict gaps.
These constructions cover every base parameter, including the
boundary where the auxiliary height is zero.

The exact finite residue density is \(+N\). The regular row,
that density, and the local Gaussian give precisely
\(N^{-2}N N^{-1/2}=N^{-3/2}\) and the original nonzero amplitude.
All other groups have a uniform exponential loss after allocating
the finite-factorial tolerances. This proves (6) at complete color.
The original uniform Newton bound preserves the discarded-row
gaps on a fixed small ordinary-color disk. At each base point
fix the integer cuts and contours before varying parameters;
the local critical chart and all strict current gaps persist.
A finite cover and Cauchy's formula give the stated holomorphic
relative error and fixed mixed derivatives. No moving cutoff
is differentiated.

The theorem provides a complete endpoint coefficient on an actual
two-dimensional private corridor below the auxiliary-real curve.
It neither estimates the outer phase along a proposed path within
that corridor nor pays the outer-cap aliases and joins. Those are
separate source obligations.
