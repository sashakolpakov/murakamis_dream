# The high and vertical edge source on the taller closing rectangle

Private finite-source extension, 9 November 2026. The complete
shortened second edge has its original saddle-or-endpoint upper
envelope when the outgoing height is at most $7/10$, including
outgoing real angles up to $\pi/2$. The first angle covers the
whole high horizontal and its vertical down to height $1/10$.

Every physical row, reciprocal-factorial cut, alias, cap and
residue scalar is retained. The comparison after attaching this
edge to the inner angular current is stated separately and is
not proved here. No mathematical numerical evaluation, import,
compilation, saved-value arithmetic, or frozen-source edit is used.

## 1. Domain and complete source

Let
\[
 u=\beta-iK,\quad0\le\beta\le\pi/2,\quad0\le K\le7/10,\qquad
 t=a-iH,\quad\pi/2\le a\le2\pi/3,\quad1/10\le H\le1 .
 \tag{1}
\]
The parameters are independent. Put
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
 \tag{2}
\]
The critical value $\psi(t,u)$ below is the original zero-charge
edge phase, continued from $u=0$ without changing its constant.
Write
\[
 m(t,u)=\Re\psi(t,u),\qquad e(t,u)=(H+K)/2,\qquad
 M(t,u)=\max\{m(t,u),e(t,u)\}.
 \tag{3}
\]

**Theorem.** For every fixed $\tau>0$, uniformly on (1), through
both level parities and for all sufficiently large $N$,
\[
                  |K_N^<(t,u)|\le C_\tau e^{N(M(t,u)+\tau)} .
 \tag{4}
\]
This is a bound for the complete finite sum (2). It does not
assert a relative edge packet or a bound for its attached inner
current below the inner critical action.

## 2. Both original cut forces

For $0<\Re y<1/2$, retain the unchanged sidewise factorial phase
$F(y;t,u)=b(y,t)+b(y,u)$. Its exact force is
\[
 e^{F_y}=
 \frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
                         {(1-\cos2\pi y)^2}.
 \tag{5}
\]
The upper cuts start at
\[
 \frac12-\frac{a}{2\pi}+\frac{iH}{2\pi},\qquad
 \frac12-\frac{\beta}{2\pi}+\frac{iK}{2\pi}
 \tag{6}
\]
and run to the right. The second cut is empty in the open
strip when $\beta=0$, and is on the real bottom when $K=0$.

Set $\mu=13/10$ and write $\cos u=P+iQ$. The elementary series
bound
\[
 \cosh(7/10)
 \le1+\frac{49/200}{1-49/1200}
 =\frac{1445}{1151}<\frac{13}{10}
 \tag{7}
\]
uses $14450<14963$. Consequently
\[
 |\cos u|<\mu,\qquad0\le P\le\mu,\qquad Q\ge0,\qquad
 \varepsilon_0=\mu^2-1=\frac{69}{100}<\frac7{10}.
 \tag{8}
\]
The lower bound $P\ge0$, rather than a strictly positive
old lower bound, is all that is used.

On the incoming cut put
\[
 C=\cosh H<8/5,\quad S=\sinh H,\quad
 d=\cos a\in[-1/2,0],\quad
 q=-\cos(2\pi\Re y)\in[d,1],\quad s_q=\sqrt{1-q^2}.
\]
Then
\[
 \cos2\pi y=-Cq-iSs_q,\qquad
 |1-\cos2\pi y|=C+q,
\]
\[
 O:=|\cos2\pi y+\cos t|^2
   =C^2(q-d)^2+(C^2-1)(s_q-\sqrt{1-d^2})^2 .
 \tag{9}
\]
The original incoming-cut comparison shows that $O$ is
largest at $d=-1/2$. Its derivative proof depends only on
$C\ge1$ and $d\le q$, so is unchanged on (1).

For $q=-v\le0$, the other numerator satisfies
\[
 |\cos2\pi y+\cos u|^2
 \le S^2+v^2+\mu^2+2Cv\mu
 \le\mu^2(C+v)^2 .
 \tag{10}
\]
The last difference is
$(\mu^2-1)(S^2+v^2)+2\mu(\mu-1)Cv\ge0$.
The original exact factorization of $s_q-\sqrt3/2$ gives
$O\le(q+1/2)^2(4C^2-1)/3$. Thus the same rational
maximization, whose cleared remainder is $(1-5v)^2$, gives
\[
 |e^{F_y}|\le\frac{9\mu}{8\sqrt3}
             =\frac{117}{80\sqrt3}<1.
 \tag{11}
\]
The last comparison follows from $13689<19200$.

For $q\ge0$, the own-numerator bound is
\[
 O\le q^2+A_Cq+B_C,\qquad
 A_C=(8C^2-5)/3,\quad B_C=(4C^2-1)/12 .
 \tag{12}
\]
By (8), the other squared numerator is at most
$q^2+C^2+\varepsilon_0$: both its mixed terms
$-2CqP$ and $-2Ss_qQ$ are nonpositive. The denominator
minus the product of these bounds equals
\[
 \begin{split}
 &(C+q)^4-(q^2+A_Cq+B_C)(q^2+C^2+\varepsilon_0)\\
 &=(4C-A_C)q^3
 +(5C^2-B_C-\varepsilon_0)q^2\\
 &\quad+\{C^2(4C-A_C)-\varepsilon_0A_C\}q
       +C^2(C^2-B_C)-\varepsilon_0B_C .
 \end{split}
 \tag{13}
\]
On $1\le C\le8/5$,
\[
 4C-A_C\ge31/25,\qquad
 A_C/C^2\le129/64,\qquad0<B_C<C^2/3 .
 \tag{14}
\]
The first inequality follows from concavity and its two
endpoint values; the second follows from
$A_C/C^2=(8-5/C^2)/3$. Thus the cubic and quadratic
coefficients in (13) are positive. The linear coefficient
is at least
\[
 C^2\left(\frac{31}{25}-\frac7{10}\frac{129}{64}\right)
                  =-\frac{547}{3200}C^2,
\]
whereas its constant term is strictly greater than
\[
 \frac23C^4-\frac7{30}C^2\ge\frac{13}{30}C^4 .
 \tag{15}
\]
Since $q\le1$ and $C^2\le C^4$, the whole expression in
(13) exceeds
\[
 \left(\frac{13}{30}-\frac{547}{3200}\right)C^4
                  =\frac{2519}{9600}C^4>\frac14C^4.
 \tag{16}
\]
Also $(C+q)^4\le16C^4$. We obtain the strict uniform guard
\[
                         |e^{F_y}|^2<63/64
                         \qquad(q\ge0).
 \tag{17}
\]

On the outgoing cut put $C_0=\cosh K<13/10$ and
$q_0=-\cos(2\pi\Re y)\in[\cos\beta,1]\subset[0,1]$.
The original own-cut inequality gives
\[
 |\cos2\pi y+\cos u|\le q_0\sqrt{2C_0^2-1},\qquad
 |1-\cos2\pi y|=C_0+q_0 .
 \tag{18}
\]
The other numerator is at most $C_0+8/5$. Increasing
$q_0/(C_0+q_0)^2$ to its value at one, and then using the
increasing first factor and decreasing second factor below,
gives
\[
 \begin{split}
 |e^{F_y}|
 &\le\frac{\sqrt{2C_0^2-1}}{C_0+1}
                   \frac{C_0+8/5}{C_0+1}\\
 &<\frac{\sqrt{238}}{23}\frac{13}{10}
                   =\frac{13\sqrt{238}}{230}<1 .
 \end{split}
 \tag{19}
\]
The final squared comparison is $40222<52900$.
All these inequalities retain the starting zeros, cut
intersections, and the boundary limits specified after (6).

## 3. The same simple root and zero logarithmic charge

Put
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0 .
 \tag{20}
\]
The original incoming estimates, depending only on
$\pi/2\le a\le2\pi/3$ and $\cosh H<8/5$, give
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20,\quad
 \Re(1/A)>5/32,\quad \Im A>0 .
 \tag{21}
\]
For $c_0=\cos\beta\in[0,1]$ and $C_0=\cosh K$,
\[
 \Re B\ge1/2,\quad |B|<23/20,\quad
 |1-B|=(C_0-c_0)/2<13/20,\quad\Im B\ge0,
\]
\[
 \Re(1/B)=\frac{2(1+c_0C_0)}{(C_0+c_0)^2}>\frac{20}{23}.
 \tag{22}
\]
For the last inequality its derivative in $c_0$ has the
sign of $C_0^2-C_0c_0-2<0$, since $C_0^2<169/100<2$.
The minimum is therefore at $c_0=1$ and exceeds $20/23$.
Consequently
\[
 \Re D_0>1-\frac{21}{20}\frac{13}{20}
                   =\frac{127}{400},\qquad
 \Re(1/W)>\frac5{32}+\frac{20}{23}-1=\frac{19}{736},
 \qquad\Im(1/W)<0 .
 \tag{23}
\]
Thus $W$ lies in a fixed compact subset of the upper right
quadrant. The original root
\[
 y_*=\pi^{-1}\arctan\sqrt W
 \tag{24}
\]
is a positive distance from every boundary of the upper
wire half-strip. The exact force identity is still
\[
 e^{F_y}-1=
 -\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
                        \qquad z_y=\tan\pi y.
 \tag{25}
\]
The root $z_y^2=-1$ is at infinite height; (24) is the
unique finite algebraic upper root.

At $u=0$ the original independent-rectangle guard theorem
already identifies (24) throughout the first-angle family
in (1), with zero logarithmic derivative. Keep $t$ fixed
and move $u$ from zero along its straight segment to the
desired point. Equations (11),(17),(19),(23) hold on this
whole segment. A critical point has force one, so it
cannot cross an original cut, its starting zero, or a
numerator zero. The continuous original logarithmic
derivative takes values in $2\pi i\mathbb Z$ and remains
zero. Hence the original critical value continues with
\[
 F_y(y_*;t,u)=0,\qquad F(y_*;t,u)=\psi(t,u),\qquad
 -F_{yy}(y_*;t,u)=
       \frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0 .
 \tag{26}
\]
These are original branch and constant identities, not
just consequences of the exponential equation.

## 4. The complete unweighted upper path

Keep the original real zero-safe envelope
$\mathcal V(y)=\mathfrak b(y,t)+\mathfrak b(y,u)$.
Its real endpoint values are
\[
                       \mathcal V(0)=0,\qquad
                       \mathcal V(1/2)=e .
 \tag{27}
\]
The reflection proof from the original upper-continuation
theorem makes it continuous and subharmonic. Across either
upper cut its upward derivative jumps by $+2\pi$; the flux
at a starting zero is $O(\rho|\log\rho|)$ and tends to zero.
Equations (11),(17),(19) imply strict horizontal decrease
along both cuts, so no cut point is a local minimum.
Away from them the envelope is nonconstant harmonic.

At a regular real-wire point the incoming logarithmic
force has its original argument in $(0,\pi)$, since
$a>0,H>0$. When $\beta,K>0$, the outgoing force also
has argument in $(0,\pi)$. When $\beta=0$, its argument
is zero and the incoming force still gives a strict
negative upward derivative. For $K=0,\beta>0$, points
off the real outgoing cut have the corresponding limits;
the cut itself is covered by its strict horizontal
descent (19). These facts exclude local minima on the
open bottom, including every degenerate parameter face.

The exact one-leg side formulas in the prior vertical
envelope apply for every real leg angle in $[0,\pi)$.
They show that the left side strictly increases from
zero. On the right each leg decreases up to its own
cut height and has derivative at least $\pi$ above it;
before that height a leg of positive real angle has
derivative strictly greater than $-\pi$. The zero-real-angle
limit has derivative zero below its height and $\pi$
above it. Thus the sum decreases to $\min(H,K)/(2\pi)$
and then increases strictly. If $K=0$, it increases
from the real endpoint. Every strict side sublevel is
therefore connected or empty, for all height orderings.

At a sufficiently large fixed upper height,
\[
 \mathcal V(x+iv)=2\pi v-\frac{aH+\beta K}{2\pi}+o(1)
 \tag{28}
\]
is uniformly above all critical levels and critical points.
The original component/Jordan lemma now applies at level
$m$. Every strict-sublevel component reaches a vertical
side: otherwise its compact closure would have a minimum
on the excluded bottom, cuts, or harmonic interior.
There are at most two such components because each side
trace is connected. The two descending germs of the
nondegenerate saddle cannot lie in the same component:
the original finite-crosscut construction would enclose
an ascending germ in a Jordan loop at lower boundary
values, contradicting subharmonicity. Thus they reach
different sides. In particular the left strict-sublevel
trace is nonempty, so $m>0$.

The left side connects to its real endpoint below level
$m$. On the right, its decrease-then-increase property
connects to its real endpoint below $\max(m,e)$. Pushing
these paths into the open strip and using small uniform
endpoint collars therefore gives, for every fixed
$\epsilon>0$, a path from real cuts $\alpha$ to $\gamma$,
$0<\alpha<\gamma<1/2$, at rate at most $M+\epsilon$.
Finite parameter covers give uniform lengths and heights;
no global continuous choice of contour is required.

## 5. Both aliases, both endpoint groups, and the exact identity

Use the same canonical interpolation as the joined source:
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},
 \qquad T_N(y)=B_N(y,t)B_N(y,u).
 \tag{29}
\]
At $y=j/N$ it is the literal summand of (2). All shifted
real arguments still lie between $-1/3$ and $5/6$.
The reciprocal reflection identity therefore proves
holomorphy across the shifted factorial zeros throughout
$0<\Re y<1/2$, at all fixed finite heights. The same
uniform factorial theorem gives
$|T_N|\le CN^{-2}e^{N\mathcal V}$ on compact paths.
Its zero-safe endpoint version gives
\[
 |T_N(j/N)|\le CN^A e^{N\mathcal V(j/N)},\qquad0\le j\le U_N.
 \tag{30}
\]
The proof is unchanged: the displacement of the own
factorial from $j/N$ to $(j+1/2)/N$ changes $NJ$ by
$O(\log N)$ uniformly, and zeros only improve an upper
bound. The larger imaginary parameter bound remains
fixed and does not approach any real strip edge.

Both original penalized side bounds are
\[
 \mathcal V(\pm iv)-2\pi v\le
 D_*:=\frac{aH+\beta K}{2\pi},\qquad
 \mathcal V(1/2\pm iv)-2\pi v\le e .
 \tag{31}
\]
In (1),
\[
       e-D_*\ge H/6+K/4\ge1/60 .
 \tag{32}
\]
Both deep alias horizontals may still have height two.
Every argument of their complete dilogarithm remainders
has modulus at most $e^{\max(H,K)-4\pi}\le e^{1-4\pi}$.
The original positive-series witness $e^5>100$, together
with $\pi>3$, puts this below $1/10000$.
The sum of the absolute remainder coefficients is $4/\pi$,
so the total remainder is less than $4/(9999\pi)<1/600$.
Their polynomial parts have absolute value at most $D_*$.
It follows that
\[
                 \mathcal V(x\pm2i)-4\pi<e-3/200 .
 \tag{33}
\]
No reflection term has been removed.

Uniform continuity moves (31) to sufficiently small
interior endpoint columns. Choose a fixed $h_c>0$ and
the original midpoint cuts
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N .
 \tag{34}
\]
Both aliases use the full left-to-right paths
\[
 \Gamma_\pm:\quad
 \alpha_N\pm ih_c\longrightarrow\alpha_N\pm2i
 \longrightarrow\gamma_N\pm2i
 \longrightarrow\gamma_N\pm ih_c .
 \tag{35}
\]
Their penalized rates, the endpoint collars, and both
physical endpoint groups are at most $e+\epsilon$.

With $\zeta=e^{2\pi iNy}$, the unchanged residue calculation
is exactly
\[
 \begin{split}
 K_N^<={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy
        +N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy+C_N+E_N,\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
                           \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
                           \frac{T_N}{\zeta-1}\,dy,\\
 E_N={}&\sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
             +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
 \end{split}
 \tag{36}
\]
On each midpoint column $\zeta=-e^{-2\pi Nv}$, so its
full cap reciprocal has modulus at most one.
Split $(1-\zeta)^{-1}=1+\zeta/(1-\zeta)$ above the real
line. Move the entire unweighted term to the path from
Section 4. The two added endpoint segments, with their
original orientations, are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
                  +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy .
 \tag{37}
\]
They are in the same paid collars. The two remaining
rational integrals use (35); the exact denominators give
the full penalty $e^{-2\pi N|\Im y|}$ with a bounded
multiplier. Equations (30)--(37) and the unweighted path
give $|K_N^<|\le C_\epsilon N^A e^{N(M+\epsilon)}$.
Choose $\epsilon<\tau/2$ and absorb the fixed polynomial.
This proves (4), retaining every original residue factor
$N$, cap sign, physical cutoff and higher Fourier charge.

## 6. The attached comparisons remain separate

On a lower inner contour the first shortened edge has
its original slit upper rate $\Re\psi(t,0)$. Multiplying
(4) by that edge, the cubic crossing and the full inner
sampling kernel produces the larger of
\[
 \Re\Phi(t,u),\qquad
 E_{\rm end}(t,u)=
 \Re\psi(t,0)+\frac{H+K}{2}+\frac{3aH}{2\pi}-H .
 \tag{38}
\]
The second expression is not paid below $\Re S_3(0,u)$
by this theorem. Its high-horizontal and vertical
comparison, and the farther low first-angle connector,
remain required for a complete inner packet on the
taller rectangle.

The separate phase/action/tail theorem controls the
full-versus-short outgoing trace difference, and its
all-integer-power companion controls both edge deletions.
Neither of those exact traced bounds changes the
pointwise rates in (38). No full $Q_3$ packet, actual
closing-saddle inclusion, or closing asymptotic is inferred.

## Frozen source bindings

- Original independent cut algebra and zero-charge base:
  7f3c6a64aab48f54e60dcf4c0c192f348f0d8e64c0f3547fd5783c9ef3b11ca5.
- Original complete upper-envelope topology and source:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Original vertical source, degenerate side limits and deep aliases:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Mixed-height one-leg force and side formulas:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Component/Jordan and distributional subharmonicity proof:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Exact joined representation:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Complete lower primitive and its reflected remainders:
  79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c.
- Uniform zero-safe factorial source:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Larger calibrated phase/action and full outgoing tail:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Both exact all-integer-power edge deletions:
  f7abba0175c558ee9ca7f94799f9cd4d58adc249fea3f6b8c425e55a8136da66.
