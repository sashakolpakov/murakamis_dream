# The high endpoint sector reduces to the selected critical value

Private written deduction, 10 November 2026. The part of the positive
inner contour strictly above height $7/10$ has no endpoint maximum
away from its original saddle. A sharper complete closing-action floor
is also available. The comparison at the saddle remains unproved.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. Original source and sharper return guards

Use the original hyperbola and cubic from
[the wider phase theorem](research_mixed_symmetric_closing_wider_phase_hyperbola.md):
\[
 u=\beta-iK,\quad K=\frac{\pi K_g}{2\beta},\quad
 \frac\pi2\le\beta\le\frac{2\pi}3,\quad
 \frac{17}{30}<K_g<\frac7{10},\quad
 t_*=a_*-iH_*,\quad c=\cos(t_*/2)=p+iq.
 \tag{1}
\]
Write $C=\cos(u/2)$, $v=2c=x+ib$, and
\[
 v^3-2iv^2-3v+2i-2C=0,\qquad
 \Delta=3v^2-4iv-3.
 \tag{2}
\]
The source gives $3/4<p<7/8$, $1/4<q<7/20$,
\(|c|<1\), \(\Re\Delta>5\), and the original unsquared returns.
On (1) one has the stronger bounds
\[
                         \frac3{10}<q<\frac13.
 \tag{3}
\]
Indeed
\[
 \Im C=\frac{\pi K_g}{8}
 \frac{\sin(\beta/2)}{\beta/2}
 \frac{\sinh(K/2)}{K/2}
\]
decreases with \(\beta\). Both factors have the asserted monotonicity
by differentiating, and $K$ decreases. Hence
\[
 2\Im C<\sqrt2\sinh(7/20)<\frac{15}{28}<\frac{16}{27},
 \tag{4}
\]
using the source's \(\sinh(7/20)<3/8\) and \(\sqrt2<10/7\).
The imaginary cubic is
\[
 2\Im C=(3b-2)x^2-b^3+2b^2-3b+2.
 \tag{5}
\]
At $b=2/3$ its right side is $16/27$. The original branch
starts below this barrier on \(\beta=\pi/2\); connected continuation
therefore retains $b<2/3$. Conversely $K>17/40$ and
\(\sin(\beta/2)\ge1/\sqrt2>7/10\) give
\(2\Im C>119/400\). At $b=3/5$, the right side of (5) is
\[
 -x^2/5+88/125<127/500<119/400.
\]
For the fixed actual $x$, its derivative in $b\in[1/2,7/10]$
is positive: it is $3x^2-3b^2+4b-3>5$.
Thus the actual $b$ exceeds $3/5$. This proves (3) without
selecting a new cubic root.

Let
\[
 r_1=\operatorname{arsinh}\{C\tan(t_*/2)\}=X+iY,
 \qquad Y_0=Y+\pi/2.
 \tag{6}
\]
These are the original principal returns, so $X>0$ and
\(-\pi/2<Y<\pi/2\). In particular $Y_0>0$. The exact identity
\[
 |1-c^2|^2=1-2p^2+2q^2+(p^2+q^2)^2
\]
decreases in $p^2$ and increases in $q^2$, since \(|c|<1\).
At $p^2=9/16,q^2=1/9$, it is
\(11425/20736<9/16\). Since \(|C|^2<13/20\) in the wider
source and \(|c|^2>9/16+9/100=261/400\),
\[
 |\sinh r_1|^2
   =|C|^2\frac{|1-c^2|}{|c|^2}
   <\frac{65}{87}<\frac34.
 \tag{7}
\]
Consequently
\[
                              X<\frac23Y_0.
 \tag{8}
\]
Here is an explicit elementary proof of this implication. If
$Y\ge0$ and $X\ge2Y_0/3$, then $X\ge\pi/3>1$, contrary
to (7). If $Y<0$, set $z=Y_0\in(0,\pi/2)$. Under the same
contrary inequality,
\[
 |\sinh(X+iY)|^2\ge\sinh^2(2z/3)+\cos^2z.
\]
For $z^2\ge2$ this is at least $8/9$. For $z^2\le2$, use
\(\cos z\ge1-z^2/2\ge0\) and the positive sinh series to obtain
\[
 \sinh^2(2z/3)+\cos^2z
 \ge1-\frac59z^2+\frac{307}{972}z^4
 \ge\frac{232}{307}>\frac34.
\]
This contradicts (7) in every case.

## 2. The high contour has only the critical endpoint test

Keep the original first-edge primitive and define
\[
 J(a,H)=\Re\psi(a-iH,0)-H/2+\frac{3aH}{2\pi},
 \qquad E(a,H;u)=J(a,H)+K/2.
 \tag{9}
\]
The positive path is exactly \(\gamma_+(u)\) of
[the source-controlled path theorem](research_mixed_symmetric_closing_wider_positive_saddle_path.md).
Its full finite source, including the two shortened kernels, all
edge groups and aliases, and the original double-pole multiplier,
is unchanged here.

**Proposition 1.** If $H_*>7/10$, then every point of
\(\gamma_+(u)\) of height strictly greater than $7/10$ satisfies
\[
                         E(a,H;u)\le E(a_*,H_*;u).
 \tag{10}
\]
With the path theorem's convention that $E_{\rm high}$ includes
height exactly $7/10$, the precise conclusion is
\[
 E_{\rm high}(u)\le
       \max\{E(a_*,H_*;u),123/100+K/2\}.
 \tag{11}
\]
If $H_*\le7/10$, all endpoint sectors on that path are already
bounded by $123/100+K/2$.

*Proof.* The holomorphic function whose real part is $J$ is
\(j(t)=\psi(t,0)+3it^2/(4\pi)-it/2\). The original stationary
equation gives
\[
 j'(t_*)=\frac{r_1+i\pi/2}{\pi},\quad
 J_a(t_*)=X/\pi>0,\quad J_H(t_*)=Y_0/\pi>0.
 \tag{12}
\]
On the critical-height horizontal from the axis to $t_*$,
\(J_{aa}=-\Re\sec(t/2)/(2\pi)<0\). Thus $J_a$ is positive
all the way to the saddle, and $J$ increases to its critical
value. On the subsequent right/up diagonal $t=t_*+(1+i)\sigma$,
its initial derivative is
\[
                \Re\{(1+i)j'(t_*)\}=(X-Y_0)/\pi<0
\]
by (8). Throughout that diagonal,
\[
 \Re\{(1+i)^2j''(t)\}
       =-\{3-\Im\sec(t/2)\}/\pi<-3/\pi,
 \tag{13}
\]
since $t$ lies in the positive lower source rectangle. Thus
$J$ decreases along the whole diagonal, including when it
stops at the right face above height $7/10$. These are precisely
the parts of the path strictly above that height. The possible
last horizontal at height $7/10$, and the case $H_*\le7/10$,
are covered by the adopted endpoint budget. This proves (10)--(11).
\(\square\)

On the outer hyperbola, the original outer crossing contributes
\(c_{\rm out}=(2\beta/\pi-1)K\), and exactly
\[
                   2E(a_*,H_*;u)+c_{\rm out}=2J(a_*,H_*)+K_g.
 \tag{14}
\]
Thus this proposition introduces no extra source hypothesis:
the only new endpoint payment needed is a strict comparison of
the right side of (14) with the original complete closing action.

## 3. Exact critical derivative, with its sign still open

Set $r=K/\beta$. Differentiating the same original cubic and
arccosine lift gives
\[
 t_*'(\beta)=\frac{(1+ir)\sin(u/2)}{\Delta\sin(t_*/2)},
 \qquad
 \pi\frac{d}{d\beta}J(a_*,H_*)
       =X\Re t_*'-Y_0\Im t_*'.
 \tag{15}
\]
In fact $t_*'$ lies strictly in the first quadrant. To check
the signs without a lift assumption, write
\(\sin(u/2)=A-iB\), $A,B>0$. Then
\[
 B/A=\cot(\beta/2)\tanh(K/2)<K/\beta=r,
\]
because \(\tan(\beta/2)>\beta/2\) and
\(\tanh(K/2)<K/2\). The numerator in (15) is first-quadrant
and has argument below \(\arctan r<7/15\).
By (3),
\[
 \Im\Delta=8p(3q-1)<0,\qquad
 |\Im\Delta|<7/10,\qquad\Re\Delta>5.
\]
Also \(\sin(t_*/2)\) lies in the lower right quadrant and has
argument greater than \(-\pi/4\), since
\(\Re(1-c^2)=1-p^2+q^2>0\).
The argument of (15) is therefore positive and less than
\[
          \pi/4+7/15+7/50=\pi/4+91/150<\pi/2.
\]
Consequently $a_*'>0$ and $H_*'<0$.

These two signs alone do not determine the sign of (15).
By (8), the stronger sector inequality
\[
                         \Im t_*'\ge\frac23\Re t_*'
 \tag{16}
\]
would suffice for strict decrease of the critical endpoint value.
Neither (16) nor the required critical endpoint payment is proved
here. In particular increasing $a_*$ and decreasing $H_*$
cannot themselves be substituted for that comparison.

## 4. A stronger complete closing-action floor

Let $M_g=\Re\Xi(u_g)$ retain its original complete normalization.
Then
\[
                            M_g>\frac{10937}{3375}.
 \tag{17}
\]
This uses no new kernel continuation. On the real segment
\(0\le x\le\pi/2\), the taller-strip original cubic has
\(1/4<q<1/3\). The lower inequality follows from its imaginary
equation at $b=1/2$, where the right side is negative; its
derivative in $b$ is positive. Its real equation is
\[
 \cos(x/2)=p(4p^2-12q^2+8q-3).
\]
If $p\ge7/8$, the right side is at least
\((7/8)(49/16-7/4)=147/128>1\). Hence $p<7/8$ on this
entire real segment.

For $w=c(x)\tan(x/2)$, its argument lies in
\([0,\arctan(4/9))\subset[0,\pi/6)\). On such a ray,
\[
                         \Re\operatorname{arsinh}w\le\Re w.
 \tag{18}
\]
Indeed $F(t)=\Re\operatorname{arsinh}(tw)$ satisfies
\[
 F''(t)=-t\Re\frac{w^3}{(1+t^2w^2)^{3/2}}\le0,
\]
because the argument of the quotient lies in
\([0,3\arg w]\subset[0,\pi/2)\), on the original principal
branch. Now $F(0)=0,F'(0)=\Re w$, proving (18).

The real action debit from zero to \(\pi/2\) is consequently
\[
 D_{\rm real}\le\frac{7\log2}{8\pi}<\frac{49}{250}.
 \tag{19}
\]
The last inequality uses exactly the written witnesses
\(\log2<7/10\), \(\pi>25/8\) from the taller-strip action
proof. That proof retains, at every height at most $7/10$,
the complete downward debit
\(D_{\rm vert}\le2/(27\pi)<16/675\).
The calibrated complete value $M_3>46/25$ therefore gives
\[
 \Re S(\pi/2-iK_g)
   >46/25-49/250-16/675=10937/6750.
\]
By the adopted horizontal concavity theorem the actual closing
point maximizes the original horizontal closing action. At its
right endpoint \(\Re\Xi(\pi/2-iK_g)=2\Re S(\pi/2-iK_g)\).
This proves (17).

For example, a uniform strict bound
\[
                         J(a_*,H_*)<17149/13500
 \tag{20}
\]
would now suffice in (14), because $K_g<7/10$.
Equation (20) is only a sufficient comparison, not a conclusion
of this note. Neither a complete remaining-current bound nor a
closed-knot asymptotic is inferred.

## 5. Frozen direct sources

The source files were read in the exact versions below. No source
file is changed by this deduction.

| Source | SHA-256 |
|---|---|
| `research_mixed_symmetric_closing_wider_phase_hyperbola.md` | `e9eadfc87f49741345f33ac73f717a4e1698ccaca5c3ffb824d48bd0444a8cbb` |
| `research_mixed_symmetric_closing_wider_positive_saddle_path.md` | `6e362aec94c3ae00bab51e7d4c1d6928a6c4aff8fdcdbd68a475b7e9346d7e8c` |
| `research_mixed_symmetric_closing_right_endpoint_sector_budget.md` | `f6dafa452dab15d307b7d2aad771b66409356ecf20aa441da38c01f45315c6b3` |
| `research_mixed_symmetric_closing_strip_phase_and_tail.md` | `fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795` |
| `research_mixed_symmetric_closing_horizontal_concavity.md` | `f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b` |
| `research_inner_three_complete_action_lower_bound.md` | `dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42` |
