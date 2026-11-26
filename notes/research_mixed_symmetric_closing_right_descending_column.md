# The complete right descending column

Private written finite-source deduction, 10 November 2026. The actual
right outer hyperbola can be joined to the controlled low horizontal
by the column at real angle \(2\pi/3\). This requires checking the
inner source at smaller outgoing heights, rather than using its
continued action alone. The proof retains both full edges, every
inner trace correction, and the complete outer sampling multiplier.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. Original source and claim

Let \(u_g=\beta_g-iK_g\) be the original symmetric \(343\) geometric
point, and keep
\[
 M_g=\Re\Xi(u_g)>163/50,\qquad
 \Xi(u)=2S_3(0,u)+iu^2/\pi-iu,\qquad 17/30<K_g<7/10 .
 \tag{1}
\]
Put
\[
 a_0=2\pi/3,\quad h_0=1/10000,\quad K_T=3K_g/4,\quad
 \mathcal C=\{a_0-iK:h_0\le K\le K_T\},
 \tag{2}
\]
oriented from \(a_0-iK_T\) to \(a_0-ih_0\).
The complete original source is
\[
\begin{aligned}
 Q_N(w,u)&=\phi_N[R_N^3\mathcal K_N(w,x)\mathcal K_N(x,-2\cos u)]
          =\mathbf e(-2\cos u)^TJ_NM_N^3\mathbf e(w),\\
 F_N(u;\mathbf w)&=Q_N(w_L,u)Q_N(w_R,u),\\
 G_N(u;\mathbf w)&=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2},
                      \qquad \eta_N=(-1)^{N-1}.
\end{aligned}
 \tag{3}
\]
Write \(B(u)=(M_g-K/3)/2\) on (2).

**Theorem.** There are a fixed \(\epsilon>0\) and fixed ordinary
complex neighborhoods of \(w_L=w_R=-2\) such that, for both parities
and all sufficiently large \(N\),
\[
 \frac{N^2}{\pi}\int_{\mathcal C}
              |G_N(u;\mathbf w)W_N(u)|\,|du|
                   \le C e^{N(M_g-\epsilon)}.
 \tag{4}
\]
Every fixed mixed ordinary incoming derivative obeys the same
conclusion on smaller neighborhoods. The original signed current
has the additional scalar \(-C_{N,4}/i\), of modulus one.

## 2. Original cubic and the critical endpoint on the column

The wider cubic theorem already continues the original distinguished
root and unsquared logarithmic equation throughout
\[
 \pi/2\le\Re u\le2\pi/3,\qquad-7/10\le\Im u\le0.
\]
Write \(c=\cos(t_*/2)=p+iq,\ t_*=a_*-iH_*,\ C=\cos(u/2)\).
Its original bounds and equation are
\[
 3/4<p<7/8,\quad1/4<q<7/20,\quad
 1/10<H_*<1,\quad 1<a_*<2\pi/3,\quad
 C=4c^3-4ic^2-3c+i .
 \tag{5}
\]
The inequality \(a_*>1\) follows from
\(\cos(a_*/2)<7/8<\cos(1/2)\), as in the positive-path proof.

On the entire column including its zero-height limit,
\[
 C_R<13/20,\qquad 2C_I<31/60,\qquad
                       p<81/100,\quad q<21/64.
 \tag{6}
\]
For the first bound, \(C_R=\tfrac12\cosh(K/2)<13/20\).
For the second, \(2C_I=\sqrt3\sinh(K/2)\) increases with \(K\).
At \(K=K_T\), the original hyperbola comparison gives
the upper bound \(\sqrt2\sinh(K_g/2)<31/60\).
This is the exact positive-series comparison in the critical
payment theorem, not a value inferred from a new root.

For clarity the tighter root bounds do not require \(q>3/10\).
With \(x=2p,b=2q\), the imaginary cubic is
\[
 2C_I=(3b-2)x^2-b^3+2b^2-3b+2.
 \tag{7}
\]
It increases in \(b\) on the original wider box, since its
derivative is \(\Re(3v^2-4iv-3)>5\).
At \(b=2/3\) its value is \(16/27>31/60\); hence \(q<1/3\).
The real cubic then gives
\[
 C_R=p(4p^2-12q^2+8q-3)>p(4p^2-7/4).
 \tag{8}
\]
At \(p=81/100\) the last expression is
\(88533/125000>13/20\), so \(p<81/100\).
At \(b=21/32\), (7) now exceeds
\[
 19987/32768-6561/80000>3/5-1/12=31/60.
 \tag{9}
\]
Thus \(q<21/64\), as claimed. All continuations remain the
original selected branch.

Define the original critical endpoint function
\[
 J(a,H)=\Re\psi(a-iH,0)-H/2+3aH/(2\pi).
 \tag{10}
\]
Sections 2--6 of the critical payment theorem use only
\(3/4<p<81/100,\ q\le21/64\), and the original first-return
branch. They therefore apply to (6). More explicitly, when
\(H_*\le7/10\) the old low-height comparison gives \(J<123/100\).
When \(H_*>7/10\), increase \(q\) at fixed \(p\) to \(21/64\).
Both \(a,H\), and both derivatives \(J_a,J_H\), are positive
through that enlargement. Its constant-\(q\) curve remains
in \(7/5<a<5/3,\ 3/4<H<1\); the unchanged concavity and
center bounds in that source give
\[
                  J(a_*,H_*)<32/25-451/240000.
 \tag{11}
\]
The low-height case is stronger. The attached critical sector
therefore satisfies on the entire column
\[
 2E(t_*,u)+K/3
       =2J(a_*,H_*)+4K/3
       \le2J(a_*,H_*)+K_g
                        <M_g-451/120000,
 \tag{12}
\]
where \(E(a-iH,u)=J(a,H)+K/2\).

The endpoint reduction along the positive saddle path also
extends here. Its horizontal part at height \(H_*>7/10\)
has maximum at \(t_*\): the original critical equation gives
\(J_a(t_*)=X/\pi>0\), and \(J_{aa}=-\Re\sec(t/2)/(2\pi)<0\).
Along the subsequent \(1+i\) diagonal,
\[
 J'_{\rm diag}(0)=(X-Y-\pi/2)/\pi<0,\quad
 J''_{\rm diag}=(\Im\sec(t/2)-3)/\pi<0,
 \tag{13}
\]
where \(r_1=\operatorname{arsinh}(C\tan(t_*/2))=X+iY\).
To verify the first sign without the stronger lower bound on \(q\),
the original wider guards give
\[
 |\sinh r_1|^2
   =|C|^2|1-c^2|/|c|^2
       <(13/20)(4/5)/(5/8)=104/125<1.
 \tag{14}
\]
If \(Y\ge0\), then \(X<\operatorname{arsinh}1<\pi/2\).
If \(Y<0\) and \(X\ge Y+\pi/2\), (14) would contradict
\(\sinh^2X+\sin^2Y\ge\sinh^2X+\cos^2X\ge1\).
The last inequality follows by differentiation for \(X\ge0\).
This proves (13). The final horizontal at height \(7/10\),
when present, retains its separate upper rate \(123/100+K/2\).
Thus the high-path maximum is bounded by the maximum of that
already paid rate and the critical value in (12).

## 3. The two finite-source checks at small outgoing height

The positive-first-angle wider-edge theorem already allows
\(K=0\); its complete upper envelope is
\[
 |K_N^<(t,u)|\le C_\tau
 e^{N[\max\{\Re\psi(t,u),(H+K)/2\}+\tau]},
 \quad 0<a\le2\pi/3,\quad1/10\le H\le1.
 \tag{15}
\]
It retains the original interpolation, both full rational
aliases, all caps, and both physical endpoint groups.
Only the negative-first-angle swap and the axis join need a
new check when \(K<1/10\).

For the negative horizontal at first depth \(7/10\), exact
symmetry and evenness identify its second shortened edge with
the opposite-height edge at
\[
             t=2\pi/3-iK,\qquad u'=a+7i/10,
                     \quad0\le a\le\pi/2.
 \tag{16}
\]
The opposite-height proof remains valid for the fixed enlarged
incoming interval \(h_0\le K\le K_T\). Here are all uses of
its former lower bound \(1/10\).
Its two cut comparisons and its root and real-row profile
proofs use only
\(1\le\cosh K<8/5\), \(\sin(2\pi/3)\sinh K>0\), and the
unchanged upper bounds on the other leg. Every displayed cut
reserve is unchanged. Its root guards
\(\Re D_0>127/400,\ \Re(1/W)>19/736\) persist.
The real-transition test, the right-side product inequality,
and both connected-side sublevel arguments likewise use
only these same upper bounds and the strict positive first
imaginary numerator. That strictness is uniform for \(K\ge h_0\).
The original zero charge continues from \(K=1/10\) while
the strict cuts and simple root exclude a crossing.
The two complete alias estimates retain a fixed reserve:
their exact bound is \(e-D_*\ge K/6+(7/10)/4\ge7/40\).
All shifted real factorial arguments, exact midpoint caps,
and both parity endpoint stops are unchanged.
Consequently the complete envelope of that theorem holds
uniformly on (16), including \(a=0\).

For the axis join \(t=-ih,\ 7/10\le h\le1\), the proof of
the center-height-join theorem also extends to \(K\ge h_0\).
Its only changed numerical lower bound is
\[
 \Im B=\tfrac12\sin(2\pi/3)\sinh K
                       \ge(\sqrt3/4)\sinh h_0>0.
 \tag{17}
\]
All other root, cut, bottom and side inequalities persist:
the incoming cut has no open interior segment, the outgoing
bottom argument remains strictly in \((0,\pi)\), and the
right side decreases to its smaller cut height and then
increases. Its alias reserve is still
\(e-D_*\ge h/2+K/6\). The same finite compact-cover proof
therefore gives its axis envelope with uniform constants.
This argument also supplies the uniform positive-angle limit
needed at the initial endpoint of (15): the outgoing root
and bottom strictness remain uniform as that angle tends to
zero, while the disappearing incoming cut stays at the side.
No pointwise axis bound is used to infer a relative packet
on a complex neighborhood.

The phase comparisons in the axis theorem use only
\(0\le K\le7/10\); their real-limit and height-integration
proofs explicitly include \(K=0\).
They give, unchanged,
\[
 \max\{\Re\Phi(-ih,u),E(-ih,u)\}
                      <B(u)-179/8000
 \quad(7/10\le h\le1)
 \tag{18}
\]
on this smaller column. The original negative-horizontal
derivative is still \(<-1/(20\pi)\), by
\(|\tan((-a-7i/10)/2)|\le1\) and
\(|\cos(u/2)|^2<13/20\).
Thus the full negative central current and the axis join
retain fixed gaps. The far negative horizontal and its
midpoint vertical have the same source bounds as before.
For them the old equality \(\beta K/\pi=K_g/2\) is only
needed as an upper bound, and here
\[
                  \beta K/\pi=2K/3\le K_g/2.
 \tag{19}
\]

## 4. Complete inner inventory on the column

Use the exact two-short trace with \(U=\lfloor N/2\rfloor-1\),
and the original midpoint \(\Theta_N\), endpoint height \(h_c\),
crossing scalar \(C_{N,3}\), and full multiplier \(W_N(t)\).
Its lower path has successive pieces:

1. the far negative vertical and horizontal ending at \(-7i/10\);
2. the axis join to \(-i\max\{H_*,7/10\}\), when required;
3. the original positive saddle path of the wider-path theorem;
4. its right-face vertical down to \(2\pi/3-i/10\);
5. the original low and far positive pieces ending at
   \(\Theta_N-ih_c\).

The exact identity of the fixed-low remainder theorem writes
the two-short trace as the integral on this oriented path,
with scalar \(-N^2C_{N,3}/(\pi i)\), plus its explicit far
physical samples, first normals, and two midpoint verticals.
Both parity traces and the odd simple node remain unchanged.
The integrand is entire apart from the real sampling poles,
so these lower-half-plane deformations preserve that identity.

The wider positive-path Hessian signs, and hence its geometric
upper rate \(s(u)=\Re S_3(0,u)\), remain valid throughout the
present column. Their proof uses only the wider cubic box,
\(|\cos u|^2<1\), the positive first-angle rectangle, and
the strictly positive \(K\). All hold here; no use was made
of the hyperbola's lower height. Its high endpoint sector
is paid by (12)--(14). The low endpoint sector is
\[
                  123/100+K/2,
 \tag{20}
\]
and after attaching half the outer weight it is at most
\(123/100+K_g/2<79/50<M_g/2\).

The strict-edge and right-vertical theorem applies unchanged
to (15). On its open \(m>e\) region the original nonzero
Gaussian is obtained with its complete alias/cap gaps.
Its resulting row comparison
\[
             m\le\max\{e,m_{\rm row}(t)+m_{\rm row}(u)\}
 \tag{21}
\]
therefore still licenses the geometric low endpoint of the
right-face vertical. The vertical convexity proof uses the
same positive first-angle Hessian signs. Its two endpoints
are controlled by the positive saddle path and by the full
row bound at \(2\pi/3-i/10\).

For precision, every low/far comparison transfers with the
effective parameter
\[
                         K_0=4K/3\le K_g<7/10.
 \tag{22}
\]
Indeed at \(\beta=2\pi/3\), \(K=\pi K_0/(2\beta)\), and
half the outer rate is exactly \((K_0-K)/2=K/6\).
The row-curvature and low/far proofs use only
\(0\le K_0<7/10\), never the original lower bound on \(K_g\).
Their complete low/far current gap \(1/500\), and the far
physical-term gap \(1/20\), therefore remain available.
Their all-real incoming proofs retain the original first
normal samples and odd middle contribution.

Finally the right-edge restoration lemma applies on its
printed independent domain \(|\Re u|\le2\pi/3,\ K\le7/10\).
Its attached comparison uses
\[
 2E(K)+K/3=4b_2+K^2/(2\pi)+4K/3
                         \le4b_2+K^2/(2\pi)+K_g,
 \tag{23}
\]
so its full-to-two-short gap \(1/25\) remains valid.
This includes all revived radical rows and the odd
middle/simple contraction. No off-grid short/full equality
is substituted for that traced estimate.

It follows from this complete inventory that, for some fixed
\(\epsilon_1>0\) and every fixed sufficiently small rate
allowance \(\tau>0\),
\[
 \sup_{w\in[-2,2]}|Q_N(w,u)|
 \le C_\tau N^A
       \exp N\{\max(s(u),B(u)-\epsilon_1)+\tau\}.
 \tag{24}
\]
All constants are uniform on the compact column. The first
shortened edge in each current uses the all-real incoming
slit bound; its exponent is the original complete first-edge
action. Thus (24) is an upper bound, not a variable-incoming
nonzero packet.

## 5. Phase comparison and the actual outer current

Let \(d=\pi/2-\beta_g>0\). The original decreasing hyperbola
and the low-endpoint phase theorem give
\[
 \Re\Xi(a_0-iK_T)\le M_g-d^2/(8\pi).
 \tag{25}
\]
At the smaller height \(h_0\), the same written real-action
bound and principal-return height estimate give
\[
 \Re\Xi(a_0-ih_0)
       <451/141+4h_0/3<16/5<M_g-1/100.
 \tag{26}
\]
Here \(16/5-451/141=1/705>1/7500=4h_0/3\).
The low-endpoint theorem proves
\(\partial_K^2\Re\Xi(a_0-iK)>0\) on the entire wider
rectangle. Convexity therefore gives
\[
 \Re\Xi(u)\le M_g-\delta,\qquad
 \delta=\min\{d^2/(8\pi),1/100\}>0,\qquad u\in\mathcal C .
 \tag{27}
\]
Since \(2s(u)+K/3=\Re\Xi(u)\), (24) and (27) imply a
uniform strict bound \(|Q_N(w,u)|\le C e^{N(B(u)-\epsilon_2)}\)
for all real incoming colors and some \(\epsilon_2>0\),
after choosing \(\tau\) and absorbing polynomial factors.

The full source is an ordinary polynomial of degree at most
\(D<N\) in \(w\). Continue this all-real bound by a fixed
filled Bernstein ellipse whose logarithmic parameter is
smaller than \(\epsilon_2/4\). The polynomial degree and
coefficient count consume only a strictly smaller allowance.
This gives the same type of strict bound on a fixed complex
neighborhood of \([-2,2]\), uniformly before \(N\).

On \(\mathcal C\), \(K\ge h_0>0\), so the complete outer
sampling denominator is bounded and has rate \(-K\).
Together with its original crossing, the rate is \(K/3\).
Multiplying the two complete inner factors, integrating over
the bounded oriented column, and absorbing its sine and
original \(N^2/\pi\) proves (4). Cauchy on smaller ordinary
incoming neighborhoods proves all stated mixed jets.

This theorem pays the specific descending column. Combined
with the coupled-column low-horizontal theorem, it reaches
the earlier controlled far path. An assertion about the
whole closing integral still requires its existing exact
two-connector identity and the separately paid left current.

## Frozen direct sources

| Source | SHA-256 |
|---|---|
| research_mixed_symmetric_closing_wider_phase_hyperbola.md | e9eadfc87f49741345f33ac73f717a4e1698ccaca5c3ffb824d48bd0444a8cbb |
| research_mixed_symmetric_closing_right_low_phase_endpoint.md | e7260cfc08047322fe85b6c0d3b33ce65bb5ab8edff8d73e90bb478426bdec03 |
| research_mixed_symmetric_closing_critical_endpoint_payment.md | 57e2d4a3d246397dce0c4c66a797c3bc452f353aa509d0f7ebef1b0d18b2a247 |
| research_mixed_symmetric_closing_action_floor_163.md | f0bfaf90d7e331adf1df3ba59980dea76ebc8347b7244d2b52c4e1c692b5f825 |
| research_mixed_symmetric_closing_positive_first_angle_wider_edge.md | f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f |
| research_mixed_symmetric_closing_opposite_height_high_edge.md | 19aa75ce4c6c8b461e55295da4ce51c67bf4ee83d4550318773b01a302bdc74d |
| research_mixed_symmetric_closing_center_height_join.md | 943a40bd6addadc889b6a4b2629619d4ea6bb780fc5f9e6b25e67431a7ffa65a |
| research_mixed_symmetric_closing_wider_negative_inner_connection.md | 3567e939040545b1551a69e33564704c8e3b0540e3bd31b8b1c021d35460b7f3 |
| research_mixed_symmetric_closing_wider_positive_saddle_path.md | 6e362aec94c3ae00bab51e7d4c1d6928a6c4aff8fdcdbd68a475b7e9346d7e8c |
| research_mixed_symmetric_closing_wider_edge_packet_and_vertical.md | 5f4ed6a63f91c8ecd683aaf8a9b83233793248e6efa52dee20e7b74a77bafc26 |
| research_mixed_symmetric_closing_right_inner_low_and_far.md | 0bd7207c07dadcf7a448af7ad89e1df71925a824f81dabe696a0cdadbf3fb39e |
| research_mixed_symmetric_closing_fixed_low_remainder.md | 03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0 |
| research_mixed_symmetric_closing_right_edge_restoration.md | 7537a3c34ca00b665ae8dd95eb130cede3f6972389b7ff5ed8382737cec4fac8 |

All original phase, full-trace and finite-edge sources used above
were read. The smaller outgoing-height checks and fixed-column
critical comparison are proved here; they are not inferred from
a pointwise packet on the hyperbola.
