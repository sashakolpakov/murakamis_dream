# The combined original actions and a paid terminal mode block

Private written source deduction, 9 November 2026. The original
outgoing action and continued charged inner action give an exact
real stationary equation, with a separate additional phase equation
required for complex gluing. Their elementary endpoint bounds also
pay an actual finite block: every Chebyshev mode with
\(k/N\ge15/32\) in the complete attached outgoing polynomial is
exponentially below the original reference action.

The finite block estimate uses the full real inner-source bound.
It does not require a global quantum packet along the continued
charged curve. The remaining modes and the full reference transfer
are not paid by this note. No mathematical numerical evaluation,
saved-value arithmetic, or frozen-source edit is used.

## 1. The two original actions

Retain the actual references of complete words in the original
powers three and four beginning \(343\), of length at least five.
Write
\[
 Z_*=e^{-2\pi iz_*},\qquad
 \frac3{10}\le\Re z_*\le\frac{39}{100},\qquad
 -\frac3{100}\le\Im z_*\le\frac1{50},\qquad |Z_*|\le\frac87 .
 \tag{1}
\]
Their unchanged geometric action is \(\Lambda>419/200\).
Use the original terminal-normalized outgoing critical value
\[
 \widetilde{\mathcal S}(a,z_*),\qquad
 \mathcal E(a,Z_*)=\Re\widetilde{\mathcal S}(a,z_*),
              \qquad \frac12\le a\le1 ,
 \tag{2}
\]
of [the terminal normalization theorem](research_mixed_next_outgoing_action_terminal_normalization.md).
In particular its additive constant is fixed by
\(\mathcal E(1,Z_*)=0\). Its selected finite-ratio root is
\[
 \mathcal L(a,Z_*)=\frac{T(a,z_*)-Y}{1-Y},\qquad
 Y=e^{-2\pi ia},\qquad T=e^{2\pi is(a,z_*)},
 \tag{3}
\]
The quotient in (3) is used for \(a<1\); its continuous terminal
limit is \(\mathcal L(1,Z_*)=0\).
For \(a<1\), the calibrated derivative is
\[
             \partial_a\mathcal E(a,Z_*)=\log|\mathcal L(a,Z_*)|.
 \tag{4}
\]
Beyond the original middle interval, (2) means the explicitly
continued phase with its original upper primitive; it is not a
new saddle-contour assertion.

For the full inner-three action \(S(u)=S_3(0,u)\), use
[the selected charged curve](research_mixed_next_selected_charged_curve_full_interval.md):
\[
 \begin{split}
 \Psi_\delta(u)&=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\\
 u_\delta&=a_\delta-ih_\delta,\qquad
       \Psi_\delta'(u_\delta)=0,\\
 \Gamma(\delta)&=\Re\Psi_\delta(u_\delta),\qquad
        0\le\delta\le\frac12.
 \end{split}
 \tag{5}
\]
The original logarithmic branch is retained. The proved relations are
\[
 \Gamma(0)=M_3,\qquad
 \Gamma'(\delta)=-h_\delta<0\quad(\delta>0),\qquad
 M_3-\Gamma(\delta)\ge\frac{\pi\delta^2}{900}.
 \tag{6}
\]
The last inequality is
[horizontal descent, equation (10)](research_mixed_next_charged_curve_horizontal_descent.md).

Define the combined real action
\[
 \mathcal B(a,Z_*)=\mathcal E(a,Z_*)+\Gamma(1-a),
                   \qquad\frac12\le a\le1 .
 \tag{7}
\]
Equivalently the original mode fraction is \(t=a-1/2\), and
the inner charge is \(\delta=1/2-t=1-a\).

## 2. Exact stationary equations and their scope

For \(1/2<a<1\), differentiation of the calibrated actions gives
\[
 \boxed{\quad
 \partial_a\mathcal B(a,Z_*)
       =\log|\mathcal L(a,Z_*)|+h_{1-a}.
 \quad}
 \tag{8}
\]
Thus every interior stationary point of this real envelope satisfies
\[
                   |\mathcal L(a,Z_*)|=e^{-h_{1-a}}.
 \tag{9}
\]
No phase equation follows from (9).

For precision, a formal joint holomorphic action using these
same primitives is
\[
 \mathcal A(a,u,s;z_*)=
 \widetilde Q(s;a,z_*)+S(u)+\frac{3iu^2}{4\pi}-i(1-a)u .
 \tag{10}
\]
Here \(\widetilde Q\) is exactly the continued phase in equation
(10) of terminal normalization. At its selected \(s\)-root,
the original derivative \(\ell(a,z_*)=\partial_a\widetilde Q\)
has \(e^\ell=\mathcal L\). The three complex stationary equations
of (10) are
\[
 \widetilde Q_s=0,\qquad
 S'(u)+\frac{3iu}{2\pi}-i(1-a)=0,\qquad
                     \ell(a,z_*)+iu=0 .
 \tag{11}
\]
The last equation requires
\[
                       \mathcal L(a,Z_*)=e^{-iu}
 \tag{12}
\]
and its original zero logarithmic lift. At \(u=u_{1-a}\),
equation (9) is only the real part of this last condition.
It lacks the equality of arguments and the charge check.

The actual next-vertex gluing source has a different established
stationary presentation:
\[
 \partial_y\{\mathcal P_{34}(-2,y)-g(y)
                         +\psi_0(y,z_*)\}=0,
 \tag{13}
\]
as proved in
[the next local source, equations (9)--(13)](research_mixed_three_four_next_local_source.md).
The [actual half-input source](research_mixed_next_actual_half_input_outgoing_ceiling.md)
has \(y=t_2^*\) with real part between \(24/100\) and
\(36/100\), whereas the variable \(a\) in (7) is real and at least
\(1/2\). Neither (9) nor (11) identifies those configurations
on these domains. An analytic gluing identification would require
additional original-sheet and action identities.

There is a further finite-source reason not to identify (10)
automatically with a contributing saddle. The proved coefficient
ceiling \(\mathcal E(1/2+k/N,Z_*)\) arises by degree truncation
and cardinal interpolation. It is not a complex asymptotic for
the \(k\)-th coefficient. With the original radical quotient
\[
 P_b^{\rm rad}(X)=
       \prod_{h=M}^{b-1}\frac{c_h-X}{s_{h+1}^2},
 \qquad s_j=2\sin(\pi j/N),\qquad M=\lceil N/2\rceil,
 \tag{14}
\]
the diagonal row \(b=M+k\), \(k\ge1\), has exact coefficient
\[
 [T_k(-X/2)]P_{M+k}^{\rm rad}(X)
                 =\frac{2}{\prod_{h=M}^{M+k-1}s_{h+1}^2}.
 \tag{15}
\]
This follows by comparing leading powers of \(X\).
When \((M+k)/N\to a\), its rate is \(-2J(a)\), where
\[
                    J(a)=\int_0^a\log(2\sin\pi v)\,dv,
                    \qquad J(1/2)=0.
\]
The full coefficient still contains every row \(b\ge M+k\).
Equation (15) is not a claim that this diagonal row dominates.
It displays information absent from the ceiling used in (7).

## 3. A whole-interval phase saving

The adopted original outgoing chord is
\[
 \mathcal E(1/2+t,Z_*)\le
       \mathcal E(1/2,Z_*)-\frac{205}{1134}t,
                         \qquad0\le t\le1/2;
 \tag{16}
\]
see [the sharper tail and ellipse theorem](research_mixed_next_outgoing_sharper_tail_and_ellipse.md).
Set \(c_0=205/1134\) and \(\kappa_0=\pi/900\).
Since \(\kappa_0<c_0\), the real quadratic
\[
                    -c_0t-\kappa_0(1/2-t)^2
\]
decreases on this interval. Combining (6) and (16) therefore gives
\[
 \boxed{\quad
 \max_{1/2\le a\le1}\mathcal B(a,Z_*)
       \le M_3+\mathcal E(1/2,Z_*)-\frac{\pi}{3600}.
 \quad}
 \tag{17}
\]
This is an upper bound for the combined selected actions. It
does not assert that their actual maximum occurs at \(a=1/2\),
nor that the saving in (17) exceeds the actual attachment excess.
It does not replace the separate finite-source requirements for a
global charged packet.

## 4. A quantitative terminating-input action bound

There is a stronger bound close to the terminating input which
does not use any charged packet. Retain the exact half-line root
of terminal normalization:
\[
 \begin{gathered}
 \sigma_a=2\sin(\pi a),\quad \tau_a=\sigma_a^{3/2},
 \quad \vartheta=(\pi a-\pi/2)/2,\\
 V=3e^{i\vartheta}+2e^{-3i\vartheta}+Z_*e^{5i\vartheta},\\
 \tau_a^2m^2-Vm+1=0,\qquad |\tau_am|<1,\qquad
                         |\mathcal L|=\sigma_a|m|.
 \end{gathered}
 \tag{18}
\]
For \(a<1\), \(m\ne0\) and
\[
 \frac1{|m|}
       =|V-\tau_a^2m|
       <|V|+\tau_a
       <\frac{43}{7}+3=\frac{64}{7}<10.
 \tag{19}
\]
We used \(|Z_*|\le8/7\) and \(2^{3/2}<3\).
Consequently
\[
                         |\mathcal L(a,Z_*)|>\sigma_a/10 .
 \tag{20}
\]
The original terminal normalization fixes the action integral,
so with \(\delta=1-a\) one obtains
\[
 \begin{split}
 \mathcal E(1-\delta,Z_*)
 &=-\int_{1-\delta}^{1}\log|\mathcal L(v,Z_*)|\,dv\\
 &\le -J(\delta)+\delta\log10\\
 &\le\delta\left\{1+\log\frac5{2\delta}\right\},
                              \qquad0<\delta\le1/2 .
 \end{split}
 \tag{21}
\]
The middle line uses sine symmetry and \(J(1)=0\); the last
uses \(2\sin(\pi x)\ge4x\) on \(0\le x\le1/2\).
The right side of (21) tends to zero at \(\delta=0\) and
increases on this interval.

For \(0\le\delta\le1/32\), (21) gives
\[
                   \mathcal E(1-\delta,Z_*)<\frac{11}{64}.
 \tag{22}
\]
Indeed \(\log80<9/2\). An exact witness is \(e>8/3\) and
\(\sqrt{8/3}>8/5\), so
\[
 e^{9/2}>
       \left(\frac83\right)^4\frac85
       =\frac{32768}{405}>80.
 \tag{23}
\]
The complete-action upper bound
[proved here](research_inner_three_complete_action_upper_bound.md)
is \(M_3<121/63\). Therefore
\[
 \Lambda-M_3-\frac{11}{64}>
       \frac{419}{200}-\frac{121}{63}-\frac{11}{64}
       =\frac{251}{100800}>\frac1{500}.
 \tag{24}
\]
Together with \(\Gamma(\delta)\le M_3\), this proves the actual
selected-action inequality
\[
       \mathcal B(a,Z_*)<\Lambda-\frac1{500},
                           \qquad31/32\le a\le1 .
 \tag{25}
\]
All these inequalities are uniform on the actual reference family.

## 5. The corresponding full finite mode block is paid

Use the exact attached polynomial and observation of
[the action-weighted Green theorem, equations (29)--(33)](research_mixed_next_outgoing_action_weighted_green_ellipse.md):
\[
 \begin{split}
 D&=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\\
 q&=e^{\pi i/N},\quad r=q^{-2},\quad
       \kappa_N=q^{D^2/2},\quad
       \alpha_{b,N}(Z)=(-q)^bC_{0,N}(r^b,Z),\\
 F_N^+(X,Z_*)&=\sum_{b=M}^{D}\alpha_{b,N}(Z_*)P_b^{\rm rad}(X),\\
 F_N^+(X,Z_*)&=\sum_{k=0}^{U}f_{k,N}(Z_*)T_k(-X/2),\\
 \mathcal L_N(F)&=\phi_N[R_N^3e_MQ_N^{\rm full}F].
 \end{split}
 \tag{26}
\]
The sign change from \(T_k(X/2)\) in that source is exactly
\((-1)^k\) and does not change any modulus estimate.
The outgoing normalization is already attached in \(F_N^+\):
\[
 |f_{k,N}(Z_*)|
       \le CN^A\exp N\mathcal E(1/2+k/N,Z_*),
                       \qquad0\le k\le U .
 \tag{27}
\]
No separate cost for the complete boundary coefficient
\(\alpha_{M-1,N}\) is added.

The [full whole-frequency observation theorem](research_full_single_vertex_whole_frequency_cosine_bound.md)
in particular gives
\[
       |\mathcal L_N(T_k(-X/2))|
                       \le C'N^{A'}e^{NM_3}
                          \qquad0\le k\le U .
 \tag{28}
\]
This uses the full inner source, not a sum of pointwise packet
remainders. Equivalently it follows directly from the complete
all-node bound with the original consumed-normal weights.

Let
\[
 \mathcal K_N^{\rm term}
   =\{\lceil15N/32\rceil,\ldots,U\},
 \tag{29}
\]
with the usual empty-set convention. For each of these modes,
\(1/2+k/N\ge31/32\). Equations (22),(24),(27)--(28) prove
\[
 \boxed{\quad
 \sum_{k\in\mathcal K_N^{\rm term}}
   |f_{k,N}(Z_*)\,\mathcal L_N(T_k(-X/2))|
       \le C''N^{A''}e^{N(\Lambda-1/500)} .
 \quad}
 \tag{30}
\]
The original scalar \(1/(\kappa_N^2N)\) has modulus \(1/N\).
It preserves this payment; after absorbing polynomial factors,
one may for example retain a finite gap \(1/1000\).

This is an exact block of the complete remaining observation.
The top degree \(U\), its special terminal coefficient and both
level parities are included. The exact transfer can consequently
be written with the still unpaid modes \(k<\lceil15N/32\rceil\),
the already proved geometric contribution and the already paid
errors. No transformed forcing, endpoint value, or Hermite normal
is removed by an unproved cancellation. In particular this is
a finite-source consequence of (22), independent of any global
quantum assertion for \(\Gamma\).

## Frozen sources

- Original outgoing terminal normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Actual action-weighted Green insertion and complete transfer:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Sharper outgoing action chord:
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Charged horizontal descent:
  c069665bd0780f72990ba55680a756d780c577c895ba4272e91af43e00c9ac7f.
- Complete inner-action upper bound:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Full whole-frequency observation:
  24ed707af29a5a15e5f2302210ae492d8256c5b5548145dce31de19dbbd2c489.
- Original actual next-vertex stationary source:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.
- Actual reference and half-input source:
  ecf0b292a5fcc7ecf962ac74f77a0a6293cf49008035c7f3672da7182999134a.

