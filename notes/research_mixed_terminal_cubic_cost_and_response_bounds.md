# Cubic scalar costs and correlated terminal response bounds

Research deduction, 6 November 2026. The original scalar factorial
curvature has a stronger lower bound on the whole relevant interval.
Its exact cubic conjugate improves both signs of horizontal force.
At the four saved canonical references this strengthens the main
factorial budget to a gap greater than \(1/100\), using the same
saved guards. A separate energy inequality bounds the coupled
response of the shared and terminal legs to the one external
parameter. No reference, primitive, optimizer or source evaluation
is performed. The phase inequalities below hold on the full typed
canonical families; their signs on those entire families remain open.

## 1. A uniform scalar curvature bound

Put \(g_h(x)=\Re g(x+ih)\), with the original primitive. For
\[
                    .18\le x\le.5,\qquad |h|\le.108,
\]
one has
\[
 g_h''(x)\ge K_h(.5-x),\qquad
 K_h=\frac{2\pi^2}{1+\cosh(2\pi h)}.
 \tag{1}
\]
The inequality is strict for \(x<.5\); both sides vanish at \(.5\).
Consequently the following rational constants can replace \(K_h\):
\[
 \begin{array}{c|c}
 \text{height range}&\text{valid lower coefficient}\\ \hline
 |h|\le.108&44/5\\
 |h|\le.061&19/2\\
 |h|\le.066&47/5\\
 |h|\le.01&49/5 .
 \end{array}
 \tag{2}
\]

To prove (1), set \(y=2\pi(.5-x)\) and
\(c=\cosh(2\pi h)\). Then
\[
 \frac{g_h''(x)}{.5-x}
       =2\pi^2\frac{\sin y}{y(c+\cos y)}.
 \tag{3}
\]
Here \(0\le y\le.64\pi<352/175\), and \(c<31/25\).
For \(0<u\le176/175\), the alternating sine and cosine
polynomials give
\[
 u\cos u-(1-3u^2/8)\sin u
 \ge u^3\left(\frac1{24}-\frac{7u^2}{240}
                                  +\frac{u^4}{576}\right)>0.
 \tag{4}
\]
The coefficient multiplying the sine upper polynomial is positive.
The last strict inequality already follows by dropping the last term:
\(1/24-7(176/175)^2/240=2129/175000>0\).
Thus \(y\cot(y/2)>2-3y^2/16>31/25>c\); the rational
reserve in the middle inequality at \(y=352/175\) is
\(43/30625\).

For \(F(y)=(c+1)\sin y-y(c+\cos y)\), this proves
\[
 F'(y)=2\sin(y/2)\{y\cos(y/2)-c\sin(y/2)\}>0
                         \quad(y>0).
 \tag{5}
\]
Since \(F(0)=0\), equation (3) proves (1), including its limiting
endpoint. The elementary estimate
\(\cosh z\le1+(z^2/2)/(1-z^2/12)\) proves the needed
cosh bounds. At the respective rational upper arguments
\(594/875,671/1750,363/875,11/175\), the reserves below
\(31/25,43/40,109/100,101/100\) are
\[
 \frac{3441}{9202775},\quad
 \frac{841437}{1451990360},\quad
 \frac{813393}{301857700},\quad
 \frac{294779}{36737900}.
 \tag{6}
\]
Finally \(157/50<\pi\) makes the reserves in the four
coefficients (2), in the same order, greater than
\[
       \frac9{2800},\quad\frac{67}{20750},\quad
                    \frac{183}{5225},\quad\frac{53}{5025}.
 \tag{7}
\]

## 2. Exact clipped cubic gains

Let \(x_*\in[.18,.5)\), \(d=.5-x_*>0\), and let
\(\phi_h(x;x_*)=g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)\).
Twice integrating (1) along the real segment gives, for either sign
of \(\delta=x-x_*\),
\[
 \phi_h(x_*+\delta;x_*)\ge
                  K\left(\frac{d\delta^2}{2}
                                      -\frac{\delta^3}{6}\right),
 \qquad K\le K_h.
 \tag{8}
\]
This also covers negative displacements; their cubic term increases
the cost rather than decreasing it.

For \(I=[L,R]\subset[.18,.5]\), a coefficient \(q\in\mathbb R\),
and \(K>0\), define
\[
 \mathcal G_K(q;x_*,I)=
 \max_{\delta\in[L-x_*,R-x_*]}
       \left\{q\delta-Kd\delta^2/2+K\delta^3/6\right\}.
 \tag{9}
\]
The polynomial in (9) is concave on \(\delta\le d\).
If \(q>Kd^2/2\), its maximizer is \(R-x_*\).
Otherwise its maximizer is the projection onto the stated interval of
\[
                     d-\sqrt{d^2-2q/K}.
 \tag{10}
\]
These assertions follow by differentiation. They retain the signed
maximum when \(x_*\notin I\); no artificial maximum with zero
is introduced. In particular a forced interval lying to the right
of its reference center remains valid.

Equations (8)--(10) bound the original scalar conjugate with no
one-dimensional numerical optimization or new primitive. Multiplying
the original cost by a nonnegative coefficient simply multiplies \(K\).
At coefficient zero use its exact affine support instead.

## 3. The terminal three-cost criterion on the full typed families

Keep the original action, complete Fourier alternatives and sole
incoming marginal from
[the one-parameter transport theorem](research_mixed_terminal_one_parameter_transport.md).
The canonical branch exists near each closed \(D_3,D_4\).
Use exactly its actual coordinates \((b_*,s_*,a_*,t_*,v_*)\),
the original endpoint image heights, and \(H=.01\).
Let \(T_\nu,A_s,A_{a,\nu},A_t\) retain their original definitions.

The full-input index barrier and pair-positivity repair in
[the full-input theorem](research_mixed_terminal_full_input_index_barrier.md)
permit every \(b_*\in D_3\cup D_4\). They drop the unnecessary
incoming half-reserve when its height lies outside the older range;
the zero incoming force means that all three useful node costs
remain unchanged. The terminal-index barrier gives \(t_R\ge.18\).
Hence, with \(A=\Re a_*\), \(s_R^*=\Re s_*\), \(t_R^*=\Re t_*\),
\[
 \begin{split}
 \sup D_\nu\le T_\nu
 &+\mathcal G_{44/5}(A_s;s_R^*,[.22,.5])\\
 &+\mathcal G_{(\nu+1/2)49/5}(A_{a,\nu};A,I_\nu)\\
 &+\mathcal G_{44/5}(A_t;t_R^*,[.18,.5]).
 \end{split}
 \tag{11}
\]
Here \(I_1=P=[.22,.45]\), and one may take either \(I_0=P\)
or the proved complete-weight forced restriction \(I_0=[.4,.45]\).
The latter requires the unchanged \(H=.01\) branch-domain theorem.
No factorial target is discarded. Tighter coefficients from (2)
can be used when their height guards are proved.

This is a uniform phase inequality on the canonical reference
families, not an assertion that its right side is everywhere negative.
The original coupled type-four source certificates have a separate
inverse-feasible reduced-input scope. A phase estimate on a full
\(D_\beta\) does not automatically enlarge that source scope.

## 4. Stronger consequences from the already saved main guards

Retain all the strict guards (1), (13) of
[the original curvature budget](research_mixed_terminal_joint_main_curvature_budget.md).
They give
\[
 A_s<141/1000,\quad d_s=.5-s_R^*>93/500,\quad |h_s|<.061,
 \qquad -A_t<51/200,\quad d_t>.15,\quad |h_t|<.066.
 \tag{12}
\]
Both forces have their previously proved signs. For the positive
\(s\) force enlarge the displacement interval to \([0,d_s]\).
Increasing the force only increases this one-sided gain. For
\(q=141/1000\), \(K=19/2\), and \(d_s\ge93/500\), one has
\(q<K(93/500)^2/2\). Formula (10) therefore gives an interior
maximizer \(d_s-\sqrt{d_s^2-2q/K}\), which decreases with \(d_s\)
and lies below \(93/500\). On that common displacement interval the
polynomial decreases pointwise with \(d_s\). Thus it suffices to
bound the concave cubic with
\[
 K=19/2,\quad d=93/500,\quad q=141/1000.
 \tag{13}
\]
Its tangent at \(\delta_0=29/250\) has slope \(-7/125000\).
On nonnegative displacements up to \(d\), its upper affine support is
\[
 \frac{2604577}{375000000}<\frac7{1000},
 \qquad
 \frac7{1000}-\frac{2604577}{375000000}
                         =\frac{20423}{375000000}>0.
 \tag{14}
\]

For the negative \(t\) force set \(v=-\delta\ge0\).
Increasing \(-A_t\), decreasing \(d_t\), and enlarging the interval
give the concave polynomial
\[
       (51/200)v-(47/5)(3/20)v^2/2-(47/5)v^3/6 .
 \tag{15}
\]
Its tangent at \(v_0=51/400\) has slope
\(-1887/1600000\). Its upper affine support on the whole half-line is
\[
 \frac{5745609}{320000000}<\frac9{500},
 \qquad
 \frac9{500}-\frac{5745609}{320000000}
                         =\frac{14391}{320000000}>0.
 \tag{16}
\]
The same center-based interval argument as in the original proof
permits these one-sided displacement restrictions.

Keep the original factorial selected gain \(<867/80000\) and
trial value \(T_1<-463/10000\). Equations (14), (16) prove
\[
 \sup D_1<
  -\frac{463}{10000}+\frac7{1000}+\frac9{500}
                         +\frac{867}{80000}
       =-\frac{837}{80000}<-\frac1{100}.
 \tag{17}
\]
The exact reserve beyond \(1/100\) is \(37/80000\).
Under the already saved full-\(P\) forced guards
\(T_0<-109/1000,\ 0<A_{a,0}<63/200,\ A>7/25\),
discard only its nonnegative selected cost. The same two gains give
\[
 \sup_{a_R\in P}D_0<
 -\frac{109}{1000}+\frac7{1000}+\frac9{500}
                              +\frac{1071}{20000}
          =-\frac{609}{20000}<-\frac1{100}.
 \tag{18}
\]
All guards used here occur in the existing four-reference diagnostic
and the completed main/common-height saved checks. This deduction
adds only exact rational inequalities. The private-left transfer
likewise inherits these improved budgets whenever its unchanged
saved guards hold, since its trial gains decrease and \(U_L<0\).
No assertion on new reference values is made.

## 5. A correlated response inequality without an inverse certificate

The same cost allocation also gives a useful response bound at every
actual canonical reference, before changing the height. Eliminate
the single private variable \(v\) locally from
\[
 F=Q_1(s;b,a)+\Phi_\epsilon(a;t,v)-g(a)-\tfrac\beta2g(b).
 \tag{19}
\]
This is the already existing stationary branch; its private Hessian
is invertible by the original strict concavity. Let \(G\) be its
three-variable complex symmetric Hessian in \((s,a,t)\).
The accretive Schur identity from
[stationary boundary energy](research_stationary_reduced_boundary_energy.md)
and the original simultaneous cost allocation imply
\[
 -\Re G\succeq D=\operatorname{diag}(m_s,m_a,m_t),\qquad
 m_s=g_{\Im s_*}''(s_R^*),\quad
 m_a=\tfrac32g_c''(A),\quad
 m_t=g_{\Im t_*}''(t_R^*).
 \tag{20}
\]
All three entries are positive by the original image ranges.
The incoming full-disk pair repair is valid here as well: it drops
only the external incoming reserve, while retaining the three costs
in (20). No selected-height branch coefficient enters (20), which
concerns the original unselected stationary action.

Only the \(s\) row has explicit \(b\) dependence. Thus, with
\[
       L=g''(s_*+b)+2\pi i,\qquad
       w=(s_*',a_*',t_*'),\qquad B=-G,
\]
the exact differentiated equations are \(Bw=L(1,0,0)^{\mathsf T}\).
Pair them with \(\bar w\) and take real parts. Completing the
square gives the correlated ellipsoid
\[
 m_s\left|s_*'-\frac{L}{2m_s}\right|^2
        +m_a|a_*'|^2+m_t|t_*'|^2
                    \le\frac{|L|^2}{4m_s}.
 \tag{21}
\]
In particular
\[
 |a_*'|\le\frac{|L|}{2\sqrt{m_s m_a}},\qquad
 |t_*'|\le\frac{|L|}{2\sqrt{m_s m_t}},\qquad
 |s_*'|\le\frac{|L|}{m_s}.
 \tag{22}
\]
These are derived from the original equations and positivity,
not from a numerical inverse proposal. They retain the simultaneous
response correlation. For any prescribed complex coefficients
\(\ell_s,\ell_a,\ell_t\), (21) gives, for example,
\[
 \Re(\ell_s s_*'+\ell_a a_*'+\ell_t t_*')
 \le \Re\frac{\ell_s L}{2m_s}
 +\frac{|L|}{2\sqrt{m_s}}
       \sqrt{\frac{|\ell_s|^2}{m_s}
                  +\frac{|\ell_a|^2}{m_a}
                  +\frac{|\ell_t|^2}{m_t}}.
 \tag{23}
\]
This can be inserted into the full-box centered value/force
transport identities, retaining their off-stationary residuals.
It avoids treating the three response components as independently
saturating their individual bounds.

There is also a general matrix proof of the factor \(1/2\) in
the off-diagonal estimates. With
\(C=D^{1/2}B^{-1}D^{1/2}\), accretivity implies
\(\Re C\succeq C^*C\), hence
\[
                   \|C-\tfrac12I\|\le\tfrac12.
 \tag{24}
\]
Its off-diagonal entries therefore have modulus at most \(1/2\).
The Schur and inverse identities use ordinary complex matrix
products; inserting conjugates into their algebraic Schur terms
would be incorrect.

These response bounds are uniform formulas, not a claim that the
responses are everywhere less than one or that a center rate extends
unchanged to the whole disk. Uniform scalar signs still require a
bound for the actual transported values and forces. Boundary-only
propagation must also retain the original centered compensation
\(\tfrac12\Re[(p-p^0)\overline{b-b^0}]\), or its proved response
alternative. The present deductions do not supply a nonzero finite
source amplitude or a whole-source contour estimate.
