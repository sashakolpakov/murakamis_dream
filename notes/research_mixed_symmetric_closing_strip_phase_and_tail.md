# A larger closing phase strip and a sharper full outgoing tail

Private written source deduction, 9 November 2026. The original
inner-three phase extends to height $7/10$, with its calibrated
constant and logarithmic charge. On the lower positive rectangle
its action exceeds $321/200$. Retaining the degree of each
deleted outgoing Newton row gives a full traced-tail bound below
$623/400$ there.

These are a phase-domain extension and an estimate for an exact
difference of finite kernels. They do not extend the shortened
inner packet. The remaining original currents are listed at the
end. No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, or frozen-source edit is used.

## 1. The original phase on a taller rectangle

Keep the original complete edge phase and inner phase

\[
 \psi_t(t,u)=-\pi^{-1}\operatorname{arsinh}
                  \{\tan(t/2)\cos(u/2)\},\qquad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
 \tag{1}
\]

All constants and branches are those of
[the original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md).
Define

\[
 \mathcal V=\{u:|\Re u|\le\pi/2,\ |\Im u|\le7/10\},\qquad
 \mathcal V_+=\{\beta-iK:0\le\beta\le\pi/2,
                                      0\le K\le7/10\}.
 \tag{2}
\]

**Proposition 1.** The original selected critical point $t(u)$
and stationary action $S(u)=S_3(0,u)$ extend holomorphically to
a neighborhood of $\mathcal V$. They retain

\[
 \begin{gathered}
 0<\Re t<\pi/2,\quad -1<\Im t<0,\qquad
 c=\cos(t/2)=p+iq,\\
 p>3/4,\quad 1/6<q<1/3,\quad
 |c|^2<127/144<(16/17)^2,\qquad
 \Phi_{tt}(t(u),u)\ne0,\\
 S'(u)=-\pi^{-1}\operatorname{arsinh}
                         \{c(u)\tan(u/2)\},\qquad
 S(0)=S_3(0,0).
 \end{gathered}
 \tag{3}
\]

In particular the complete first edge $K_N(t(u),0)$ still
has its original nonzero packet on a fixed neighborhood of
this critical image, by the already proved free-pair theorem.
No conclusion about $K_N(t(u),u)$ follows from that statement.

*Proof.* Put $C=\cos(u/2)$. The image of (2) lies strictly
inside the enlarged parameter rectangle

\[
 \mathcal C_1=\{C:1/\sqrt2\le\Re C\le17/16,
                                      |\Im C|\le2/7\}
 \tag{4}
\]

apart from the harmless lower real boundary. Indeed the positive
series give

\[
 \cosh(7/20)
 \le1+\frac{49/800}{1-49/4800}
 =\frac{5045}{4751}<\frac{17}{16},\qquad
 \sinh(7/20)
 \le\frac{7/20}{1-49/2400}
 =\frac{840}{2351}<\frac38.
 \tag{5}
\]

The strict comparisons in (5) are $80720<80767$ and
$6720<7053$. Since $1/\sqrt2<3/4$,

\[
 |\Im C|\le2^{-1/2}\sinh(7/20)<9/32<2/7.
 \tag{6}
\]

Use the same distinguished root $v=2c=x+ib$ of

\[
 v^3-2iv^2-3v+2i-2C=0.
 \tag{7}
\]

The original proof shows that this is the unique root with
$x>3/2$ on the simply connected half-plane $\Re C>1/2$.
Its imaginary equation is

\[
 2\Im C=(3b-2)x^2-b^3+2b^2-3b+2.
 \tag{8}
\]

At $b=1/3$ the right side is less than $-115/108<-4/7$;
at $b=2/3$ it is $16/27>4/7$. Thus the same connected
barrier argument, starting at the original complete root,
gives $1/3<b<2/3$ throughout (4).

All subsequent real and modulus guards of the cubic proof
use only this $b$-interval, $x>3/2$, and the real bounds
in (4). They therefore give, without changing any constants,

\[
 x<15/8,\qquad |v|^2<127/36<4,
 \qquad0<\Re\{2\arccos(v/2)\}<\pi/2,
 \qquad-1<\Im\{2\arccos(v/2)\}<0.
 \tag{9}
\]

For clarity, the height argument is unchanged: if
$H=-\Im t\ge1$, its exact identity
$x^2=4(1+s)-(1+s^{-1})b^2$, $s=\sinh^2(H/2)$,
and $s>(25/48)^2$ imply
$\Re C>2\sqrt3/3>17/16$, a contradiction.
No new root is selected in (9).

The logarithmic check also survives the enlarged imaginary
bound. Write $T=\tan(t/2)$. The original ratio estimate is

\[
 \frac{\Re T}{-\Im T}>\frac7{8\sqrt2}.
\]

Consequently (4) implies

\[
 \Re(CT)>
 \left(\frac7{16}-\frac27\right)(-\Im T)
 =\frac{17}{112}(-\Im T)>0.
 \tag{10}
\]

Both principal returns stay away from their cuts. The exact
exponential identity of the cubic proof and connected
continuation from $C=1$ therefore retain the full equation

\[
 \operatorname{arsinh}T+\operatorname{arsinh}(CT)
                         =i(3t/2-\pi).
 \tag{11}
\]

Its Hessian identity from that proof remains valid, with the
same nonzero cubic derivative and nonzero principal cosh.
Thus the reduced Hessian in (3) is nonzero.

Finally, on $\mathcal V$,

\[
 |\Re\tan(u/2)|\le1,\qquad
 |\Im\tan(u/2)|\le\tanh(7/10)<7/10.
\]

The first estimate uses $\cos\Re u\ge0$, and the second
uses the same sign in the exact half-angle denominator.
It follows that

\[
 |\Im\{c\tan(u/2)\}|
 <\frac{15}{16}\frac7{10}+\frac13=\frac{95}{96}<1.
 \tag{12}
\]

The principal return in (3) is holomorphic throughout a
neighborhood of this simply connected rectangle. Integrating
it with the original value $S_3(0,0)$ gives precisely the
continued stationary action. No additive period is reset.

The image in (9) is a compact subset of the domain of
[the free-pair theorem](research_pair_free_boundary_kernel.md),
namely $0<\Re t<\pi/2$, $-107/100<\Im t<0$,
and $|\cos(t/2)|<1$. Its full first-edge assertion follows
with every original row and both parities. \(\square\)

## 2. A uniform lower action on the lower rectangle

**Proposition 2.** With exactly the complete action normalization
in (3),

\[
                         \Re S(u)>\frac{321}{200}
                                      \qquad(u\in\mathcal V_+).
 \tag{13}
\]

*Proof.* The adopted
[complete-action lower bound](research_inner_three_complete_action_lower_bound.md)
is $M_3=\Re S(0)>46/25$. Follow the real path $0\to\beta$,
then the downward vertical to $\beta-iK$.
The entire path lies in the domain just proved.

On the real path $w=c(x)\tan(x/2)$ satisfies
$\Re(w^2)\ge0$. Integrating the principal derivative gives
$|\operatorname{arsinh}w|\le|w|\le(16/17)\tan(x/2)$,
as in the original action-floor proof. Hence its real loss is

\[
 D_{\rm real}
 \le-\frac{32}{17\pi}\log\cos(\beta/2)
 \le\frac{16\log2}{17\pi}<\frac{448}{2125}.
 \tag{14}
\]

Here $\pi>25/8$ and $\log2<7/10$; the latter follows
directly from
$e^{7/10}>1+7/10+49/200+343/6000=12013/6000>2$.

On the vertical write $u=\beta-iy$, $c=p+iq$, and
$w=c\tan(u/2)=X+iY$. For $\beta>0$, $X>0$, and

\[
 Y=\frac{q\sin\beta-p\sinh y}{\cos\beta+\cosh y}.
 \tag{15}
\]

If $Y\le0$, the principal return has nonpositive
imaginary part and gives no downward loss. If $Y>0$,
then $Y/X\le q/p<4/9<1$. The original elementary
bound

\[
 \Im\operatorname{arsinh}(X+iY)
 =\int_0^Y\Re\{1+(X+iv)^2\}^{-1/2}\,dv\le Y
\]

therefore applies. In (15) the denominator is at least one.
Using $q<1/3$, $p>3/4$, and $\sinh y\ge y$ yields

\[
 \bigl(\Im\operatorname{arsinh}w\bigr)_+
 \le\left(\frac13-\frac{3y}{4}\right)_+.
 \tag{16}
\]

At $\beta=0$ the imaginary part is nonpositive directly,
so (16) remains valid. Since
$\partial_y\Re S(\beta-iy)=-\pi^{-1}\Im\operatorname{arsinh}w$,
the total vertical loss is at most

\[
 D_{\rm vert}\le\frac1\pi\int_0^{4/9}
                    \left(\frac13-\frac{3y}{4}\right)dy
             =\frac2{27\pi}<\frac{16}{675}.
 \tag{17}
\]

The exact rational comparison is

\[
 \frac6{25}-\frac{448}{2125}-\frac{16}{675}
   =\frac{314}{57375}>\frac1{200},
\]

where $62800>57375$. Subtracting (14),(17) from
$M_3>46/25$ proves (13). \(\square\)

## 3. Retaining the actual outgoing row degree

Use the full physical algebra, trace, crossing, and kernels
of [the outgoing-tail restoration theorem](research_mixed_next_outgoing_tail_trace_restoration.md):

\[
 \begin{gathered}
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
 c_a=2\cos((2a+1)\pi/N),\qquad z_u=-2\cos u,\\
 Q_N^{\rm full}(u)=\phi_N[R_N^3K_N(-2,x)K_N(x,z_u)],\\
 Q_N^{\rm sh}(u)=\phi_N[R_N^3K_N(-2,x)K_N^<(x,z_u)],\qquad
 \Delta_N=Q_N^{\rm full}-Q_N^{\rm sh}.
 \end{gathered}
 \tag{18}
\]

Both traces in (18) are full Hermite traces. Only the outgoing
edge is shortened in the second line.

**Theorem 3.** For each fixed $K_0<\infty$, there are fixed
$C,A$ such that, at both parities,

\[
 \boxed{\quad
 |\Delta_N(u)|\le C N^A
   \exp N\left\{2b_2+\frac K2+\frac{K^2}{4\pi}\right\},
 \qquad K=|\Im u|\le K_0 .
 \quad}
 \tag{19}
\]

The same bound controls the sum of the absolute terms of
the exact contractions below, uniformly in $\Re u$.
Thus on $\mathcal V_+$, for all sufficiently large levels,

\[
                    |\Delta_N(u)|
                    \le C e^{N(\Re S(u)-1/25)}.
 \tag{20}
\]

*Proof.* Retain literally the original radical contraction
coefficients $b_{ra}$, with $|b_{ra}|\le2$. At both parities
the radical part of the outgoing difference is

\[
 \Delta_N^{\rm rad}(u)=
 \sum_{r=0}^{m-1}e_{D-r}(z_u)
       \sum_{a=0}^{r}b_{ra}R_N(c_a)^3K_N(-2,c_a).
 \tag{21}
\]

At even levels this is the complete difference. At odd levels
the additional original middle and simple-node term is

\[
 e_m(z_u)\left[
  \sum_{a=0}^{m-1}(-1)^{m+a}2\cos((m-a)\pi/N)
                  R_N(c_a)^3K_N(-2,c_a)
                   +C_{N,3}K_N(-2,-2)\right].
 \tag{22}
\]

In particular no middle row is treated as radical, and the
last term in (22) has its exact scalar $R_N(-2)^3=C_{N,3}$.
The physical first normals have already been consumed by the
proved identities (21),(22), rather than discarded.

The original radical Fourier theorem gives coefficient norm
at most $\sqrt{N-1}$ for $e_{D-r}(-2\cos u)$.
Its actual polynomial degree is $D-r$, so all its angular
frequencies have modulus at most $D-r$. Keeping this degree
instead of replacing it by $D$ gives

\[
 |e_{D-r}(z_u)|\le\sqrt{N-1}\,e^{(D-r)K}.
 \tag{23}
\]

The physical row estimate (6) in
[the slit-plane theorem](research_mixed_next_first_short_edge_slit_plane_bound.md)
applies at the fixed anchor $w=-2$, uniformly for all ordinary
row indices, including both endpoint-index regimes:

\[
 K_N(-2,c_a)=F_{a,N}(-2)>0,\qquad
 F_{a,N}(-2)\le C N^A e^{N\Psi_{a/N}(-2)},
\]

\[
 \Psi_x(-2)=\int_0^x2\operatorname{arsinh}(\cot\pi s)ds,
 \qquad\Psi_{1/2}(-2)=\psi(0,0)=2b_2.
 \tag{24}
\]

This is the full row, with its original normalization. Its
profile increases with $x$, so $a\le r$ allows its
replacement by $\Psi_{r/N}(-2)$ in an upper bound.
Put $v_r=\pi-2\pi r/N\in[0,\pi]$. The change of variable
$v=\pi-2\pi s$ gives exactly

\[
 2b_2-\Psi_{r/N}(-2)
 =\frac1\pi\int_0^{v_r}\operatorname{arsinh}(\tan(v/2))dv
 \ge\frac{v_r^2}{4\pi}.
 \tag{25}
\]

The last inequality follows from
$\frac{d}{dv}\operatorname{arsinh}(\tan(v/2))
=\frac12\sec(v/2)\ge1/2$; the endpoint singularity at
$v=\pi$ is integrable. Equation (25) is also valid for the
zero row $r=0$, without an endpoint asymptotic substitution.

Combine (23)--(25) and use the exact relation
$(D-r)/N=1/2+v_r/(2\pi)-1/N$. Each term in (21) has rate
at most

\[
 \begin{split}
 2b_2+\frac K2+\frac{Kv_r}{2\pi}-\frac{v_r^2}{4\pi}
 &=2b_2+\frac K2+\frac{K^2}{4\pi}
                              -\frac{(v_r-K)^2}{4\pi}\\
 &\le2b_2+\frac K2+\frac{K^2}{4\pi}.
 \end{split}
 \tag{26}
\]

The omitted exact $-K/N$ only improves this upper bound.
All remaining coefficients have bounded modulus and there
are only polynomially many terms.

For (22), the exact odd identity proved in
[the incoming-color theorem, (9)](research_mixed_next_incoming_color_kernel_upper_bounds.md)
is

\[
 e_m(x)=(-1)^m\{U_m(x/2)-U_{m-1}(x/2)\}/N,
                  \qquad\|e_m\|_{[-2,2]}\le1.
\]

Its degree is $m$, hence
$|e_m(z_u)|\le2(m+1)e^{mK}$. Every complete physical
kernel in (22), including $K_N(-2,-2)$, has rate at most
$2b_2$: this follows either from (24) at the last odd
ordinary row, or from the original termwise real-kernel bound.
Thus the full additional term has rate at most
$2b_2+K/2$. This proves (19) with both parity inventories
unchanged.

For $K\le7/10$, $b_2<7/12$ and $\pi>3$ give

\[
 2b_2+\frac K2+\frac{K^2}{4\pi}
 <\frac76+\frac7{20}+\frac{49}{1200}
 =\frac{623}{400}<\frac85.
 \tag{27}
\]

By (13), its gap below $\Re S$ is greater than $19/400$.
After reserving $1/25$, the remaining $3/400$ absorbs
all polynomial factors in (19). This proves (20). \(\square\)

## 4. What this removes, and what it does not

The full first-edge packet on the continued critical image
is licensed by Proposition 1. Theorem 3 pays the entire
full-versus-short outgoing difference on $\mathcal V_+$.
Consequently, on any compact subset of that rectangle where
one independently proves the original nonzero shortened
packet with a uniformly nonzero coefficient, (20) restores
the full packet with the same coefficient and normalization.
No outer radical observation is used in this implication.

The original shortened source still requires the following
finite-contour work beyond its adopted domain.

- The mixed two-angle edge packet and the signed central
  angular source were proved with smaller outgoing heights.
  Their original factorial cuts, endpoint groups, aliases,
  central interpolation, and full sampling denominator must
  be controlled on a new domain; phase holomorphy alone does
  not supply this extension.
- On the high and vertical portions of the right current,
  an available edge envelope has the two candidate rates
  $\Re\psi(t,u)$ and $(H+K)/2$. After attachment to
  the first edge and exact crossing, the latter is
  $\Re\psi(t,0)+(H+K)/2+3aH/(2\pi)-H$.
  Proposition 2 does not prove that this expression lies
  below $\Re S(u)$ on the larger rectangle.
- The subsequent low horizontal and far slit tail retain
  the second-edge degree cost $K/2$, including their
  original endpoint and alias currents. Their earlier
  comparisons used $K\le2/5$ and are not extended by
  (19). That theorem controls the traced outgoing deletion,
  not the uncontracted low-horizontal integrand.

In particular neither the whole shortened packet nor the
complete closing asymptotic is asserted. The actual geometric
middle point has $K_g>17/30$, by the adopted closing-height
theorem, but no upper bound $K_g\le7/10$, or inclusion of
that point in (2), is proved here. The source identity and
the domain test remain separate requirements.

## Frozen source bindings

- Original cubic, charge, Hessian, and action normalization:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Complete single-three source:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Complete first-edge packet:
  e62ae0c2701388a7e9bf3ad171d7005b845098542e48dffb1a36c4bc95ee745f.
- Original action-floor integration and principal-return inequality:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Original complete lower action $M_3>46/25$:
  dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42.
- Exact full outgoing-tail contraction and both parity sources:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.
- Original radical Fourier coefficients and consumed normals:
  1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
- Full physical row profiles, including zero and last rows:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact odd middle polynomial:
  9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
- Actual closing-height lower bound:
  c12acffe796dae3ad3e7990cd302020a7ff289e75f2e5c8b997836aa826764d3.
