# Four scalar bounds for the next-four ordinary half row

Research deduction, 6 November 2026.

The ordinary half-row phase separates exactly for a next-four block,
while its outgoing halfweight changes the outgoing maximum. A uniform
curvature bound controls that maximum by a clipped quadratic about
the actual outgoing reference. Its gradient simplifies using the
original outgoing marginal. Together with the cap and incoming
curvatures this gives four explicit scalar upper bounds for the
cap-main and cap-left-cut half-row profiles.

No sign for the four bounds is proved here. No root, source evaluation,
or interval cover is run. The remaining ordinary-left-cut and
cap-left/ordinary-main comparisons are separate.

## 1. Exact separation with the original outgoing halfweight

Use all notation and actual first-four/next-four references of the
[finite reduction](research_mixed_selected_four_four_finite_reduction.md).
In particular
\[
 H=1/100,\quad z=y+iH,\quad b=v+ih_b,\quad y,v\in P=[.22,.45],
 \quad -.102<h_b<-.001.
 \tag{1}
\]
The original bare phase is
\[
 Q_4(s;z,b)=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs.
 \tag{2}
\]
Set
\[
 q(w)=g(w+1/2)-g(w),\qquad b_*=v_*+ih_b,\qquad
 p=g'(s_*+b_*)-\tfrac32g'(b_*),\quad p_R=\Re p.
 \tag{3}
\]
The real part of \(g(1/2)\) is zero, so the allocated half-row
profile is exactly
\[
 B_R(y,v)=\Re q(y+iH)+\Re q(v+ih_b)
                        -\tfrac12\Re g(v+ih_b)-\pi H.
 \tag{4}
\]
The constant \(-\pi H\) is the original incoming chirp.
The outgoing subtraction in (4) is present before taking a maximum,
and the original outgoing tangent is \(p_R(v-v_*)\).

Write
\[
 j(v)=\Re q(v+ih_b)-\tfrac12\Re g(v+ih_b).
 \tag{5}
\]
Its exact derivatives, on the original lifts, are
\[
 \begin{split}
 j'(v)&=\log|1+B_v|-\tfrac32\log|1-B_v|,
                       \qquad B_v=e^{-2\pi i(v+ih_b)},\\
 -j''(v)&=2\pi\Re\frac1{\sin2\pi(v+ih_b)}
                         +\frac\pi2\Re\cot\pi(v+ih_b).
 \end{split}
 \tag{6}
\]
No quotient logarithm is assigned a new branch.

## 2. A quantitative outgoing maximum with a clipped gain

**Lemma 1.** On the full domain (1),
\[
                         -j''(v)>41/10.
 \tag{7}
\]

Put \(a=\sin(2\pi v)>3/10\) and \(C=\cosh(2\pi h_b)<49/40\).
The elementary identity is
\[
 \Re\frac1{\sin2\pi(v+ih_b)}
                   =\frac{Ca}{a^2+C^2-1}>\frac{28}{45}.
 \tag{8}
\]
For \(0<a\le1\) the expression decreases with \(C\). At
\(C=49/40\), its dependence on \(a\in[3/10,1]\) has only
an interior maximum, and its endpoint values are \(28/45\)
and \(40/49\). This proves (8). The same sine and hyperbolic
bounds give
\[
 \Re\cot\pi(v+ih_b)
  =\frac{\sin2\pi v}{\cosh2\pi h_b-\cos2\pi v}
  >\frac{12}{89}>\frac9{70}.
 \tag{9}
\]
Here \(\sin(.1\pi)>3/10\) follows from the sine cubic and
\(\pi>157/50\); the bound \(\cosh(.204\pi)<49/40\) is
already proved in the endpoint deductions. Equations (6)--(9) imply
\[
 -j''>\pi\left(\frac{56}{45}+\frac9{140}\right)
 >\frac{258893}{63000}>\frac{41}{10}.
 \tag{10}
\]

For \(l\le0\le r\), define the exact clipped quadratic gain
\[
 \Gamma_\mu(P;l,r)=P\,t-\frac\mu2t^2,\qquad
 t=\min\{r,\max\{l,P/\mu\}\}.
 \tag{11}
\]
The reference-gradient cancellation is
\[
 \begin{split}
 D_*:=j'(v_*)-p_R
 &=\Re\{g'(b_*+1/2)-g'(s_*+b_*)\}\\
 &=\log\left|\frac{1+B_*}{1-S_*B_*}\right|,
 \qquad S_*=e^{-2\pi i s_*},\quad B_*=e^{-2\pi i b_*}.
 \end{split}
 \tag{12}
\]
Both contributions involving \(g'(b_*)\) cancel only after the
outgoing halfweight and the original marginal have been retained.
Since \(v_*\in(.24,.36)\), its displacement interval contains zero.
Taylor's integral inequality and Lemma 1 prove
\[
 \begin{split}
 \max_{v\in P}\{j(v)-p_R(v-v_*)\}
 &\le\mathcal O^+_*,\\
 \mathcal O^+_*&=
 \Re q(b_*)-\tfrac12\Re g(b_*)
       +\Gamma_{41/10}(D_*;\ .22-v_*,\ .45-v_*).
 \end{split}
 \tag{13}
\]
The clip includes both possible boundary maxima. Formula (13) needs
no scalar cubic solution or target grid.

## 3. Incoming and private curvatures at the selected height

Let \(\nu=1\) denote the factorial alternative and \(\nu=0\)
the forced alternative. Put
\[
 W_\nu(y)=-\nu\Re g(y+iH)-2\nu\pi H,\qquad
 F_\nu(x,y)=\Re\Psi(x+ih_e,y+iH)+\Re q(y+iH)-\pi H+W_\nu(y).
 \tag{14}
\]
The incoming function is the same real function as in the
[next-three half-row deduction](research_mixed_selected_four_three_half_row_majorant.md),
at the present height \(H=.01\). The extra ordinary own factorial
has zero real part at \(s=1/2\). It does not alter (14).

On \([.3,.4]\times P\), the proved curvature bounds are
\[
 -\nabla^2F_\nu\succ
 \operatorname{diag}(28/5,\mu_\nu),\qquad
 \mu_1=7,\quad\mu_0=33/5.
 \tag{15}
\]
At the real cap-left cut \(e_0=.27\), define
\(F_{\nu,e_0}(y)\) by replacing \(x+ih_e\) with \(e_0\).
Then
\[
 -F_{\nu,e_0}''>\widehat\mu_\nu,\qquad
 \widehat\mu_1=69/10,\quad\widehat\mu_0=13/2.
 \tag{16}
\]
These transfers do not use the next-three ordinary height bounds.
For completeness, the cap Hessian decomposition gives
\[
 -\pi^{-1}\Re\Psi''
 =\operatorname{diag}(\sigma+u_e,u_z)
           -C_{ez}\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{17}
\]
The [original private curvature theorem](research_mixed_private_cap_curvature_bound.md) gives
\(\sigma>68/45\), while \(u_e>3/10\), \(u_z>9/70\)
on the stated main rectangle. Its summed real part is at least
\(.52\), so \(C_{ez}\le0\). Also
\(\cosh(2\pi H)<101/100\), which gives
\(-\Re q''>200\pi/101\) on \(P\), by the same elementary
endpoint argument as in the cited half-row proof. These facts give
(15). At \(e_0=.27\), use \(C_{ez}<1/30\) instead;
\(u_z-C_{ez}>2/21\) gives (16).
All these numerical inequalities hold at \(H=.01\) using the same
strict witnesses as for \(H=7/625\).

The original [private upper barrier](research_mixed_selected_boundary_optimizer_bounds.md)
and [private lower barrier](research_mixed_selected_boundary_height_envelope.md) restrict the maximum
in \(x\) to \([.3,.4]\). Their derivatives depend only on
the cap and the incoming target; every other term in (14) is
independent of \(e\). They therefore apply to both alternatives
here. The real cap cut itself remains at height zero.

## 4. Four explicit scalar upper bounds

Retain \(z_*=a+ic\), \(z_H^*=a+iH\), \(E_*=e^{-2\pi i e_*}\),
\(Z_*=e^{-2\pi i z_*}\), and \(\lambda=e^{2\pi(H-c)}\).
The two main trial gradients are
\[
 \begin{split}
 A&=\log\left|\frac{1-\lambda E_*Z_*}{1-E_*Z_*}\right|,\\
 P_\nu&=\log\left|
 \frac{(1-\lambda E_*Z_*)(1+\lambda Z_*)}
                         {(1-\lambda Z_*)^{2+\nu}}\right|.
 \end{split}
 \tag{18}
\]
The first equality uses the actual equation
\(\Psi_e(e_*,z_*)=0\). At \(e_0=.27\), let
\(E_0=e^{-2\pi i e_0}\), and define
\[
 P_{\nu,e_0}=\log\left|
 \frac{(1-\lambda E_0Z_*)(1+\lambda Z_*)}
                         {(1-\lambda Z_*)^{2+\nu}}\right|.
 \tag{19}
\]
Define the relative cap actions
\[
 \Delta_0=\Psi(e_*,z_H^*)-\Psi(e_*,z_*),\qquad
 \Delta_L=\Psi(e_0,z_H^*)-\Psi(e_*,z_*).
 \tag{20}
\]
In particular
\[
 \Delta_0=g(e_*+z_H^*)-g(e_*+z_*)-g(z_H^*)+g(z_*),
 \tag{21}
\]
so no private critical action is evaluated in the main test.
The cut difference retains the fixed canonical action at \(e_0\)
and the actual action at \(e_*\), on their original branches.

Put
\[
 \begin{split}
 R_\nu={}&\Re q(z_H^*)+\Re q(b_*)-\pi H+W_\nu(a)
                 -\Re Q_4(s_*;z_*,b_*)+\Re g(z_*),\\
 G_b={}&\Gamma_{41/10}(D_*;\ .22-v_*,\ .45-v_*),\\
 \mathcal H^{(4)}_{0,\nu}={}&
 \Re\Delta_0+R_\nu+G_b
 +\Gamma_{28/5}(A;\ .3-\Re e_*,\ .4-\Re e_*)\\
 &+\Gamma_{\mu_\nu}(P_\nu;\ .22-a,\ .45-a),\\
 \mathcal H^{(4)}_{L,\nu}={}&
 \Re\Delta_L+R_\nu+G_b
 +\Gamma_{\widehat\mu_\nu}(P_{\nu,e_0};\ .22-a,\ .45-a).
 \end{split}
 \tag{22}
\]

**Proposition 2.** With the profiles and the original outgoing
tangent of the finite reduction, for \(i=0,L\) and \(\nu=0,1\),
\[
 \sup_{y,v\in P}
 \{A_i(y)+B_R(y,v)+W_\nu(y)-M-\ell_b(v)\}
                    \le\mathcal H^{(4)}_{i,\nu}.
 \tag{23}
\]

First apply (13) to the separated outgoing target. Next use (15)
or (16) about the actual incoming real coordinate \(a\), and,
for the main profile, the actual private real coordinate \(\Re e_*\).
The gradients are exactly (18)--(19). Maximizing the resulting
diagonal quadratic over the containing displacement intervals
produces the gains in (22). Finally
\[
 M=\Re\Psi(e_*,z_*)+\Re Q_4(s_*;z_*,b_*)
                         -\Re g(z_*)-\tfrac12\Re g(b_*).
 \tag{24}
\]
The final term in (24) cancels the same reference term in (13),
giving \(R_\nu\) exactly. This cancellation occurs after retaining
the halfweight in the outgoing value, gradient and curvature.
It proves (23) with the original calibrated action and tangent.

All four quantities in (22) depend only on the same actual endpoint
parameter and rational maps used in the next-four central proof.
In particular they use the own-four outgoing map \(B_*(U)\),
the next-four coordinate ranges and reduced disks, both coupled
sum restrictions, and the next-external \(K_3\cup K_4\) condition.
The original regular-strip primitives and the fixed canonical
left-cut action can be evaluated by the branch conventions in the
[half-row evaluation specification](research_mixed_selected_half_row_evaluation_design.md).
Its next-three outgoing map, height and exact arccos optimizer are
not substituted for the next-four formulas here.

A concrete sufficient scalar test for the two half-row pairs is
\[
 \max_{\substack{i\in\{0,L\}\\\nu\in\{0,1\}}}
                       \mathcal H^{(4)}_{i,\nu}(U)<-\delta
 \quad\text{on the admitted actual-reference family},\qquad\delta>0.
 \tag{25}
\]
No sign or computation of (25) is asserted. A successful bound would
settle the two independent pairs \((0,R),(L,R)\) in the five-pair
finite reduction, along with their already dominated cap-right and
alias counterparts. The three independent pairs
\((0,L),(L,0),(L,L)\) would remain. Thus (25), even if established,
would not give a complete selected finite-source or filling theorem.
