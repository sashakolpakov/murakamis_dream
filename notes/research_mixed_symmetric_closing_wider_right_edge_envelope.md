# A wider real-angle upper envelope for the right edge

Private finite-source deduction, 9 November 2026. The complete
shortened edge upper envelope extends its outgoing real angle
from \(\pi/2\) to \(2\pi/3\), at the same outgoing height \(7/10\).
This is a pointwise bound for the original edge sum. It does not
yet bound the full inner trace or the remaining right outer
connecting current.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, or frozen-source edit is used.

## 1. Source and statement

Retain the original Newton polynomials and the exact cutoff
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}
               e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
The independent domain is
\[
 \begin{gathered}
 t=a-iH,\quad \pi/2\le a\le2\pi/3,\quad1/10\le H\le1,\\
 u=\beta-iK,\quad0\le\beta\le2\pi/3,\quad0\le K\le7/10 .
 \end{gathered}
 \tag{2}
\]
Let \(\psi(t,u)\) be the zero-charge edge critical value
continued from \(u=0\), with the original complete-edge constant.
Its existence and calibration on (2) are proved below. Put
\[
 m=\Re\psi(t,u),\qquad e=(H+K)/2,\qquad M=\max(m,e).
 \tag{3}
\]

**Theorem.** For every fixed \(\tau>0\), uniformly on (2), through
both level parities and for all sufficiently large \(N\),
\[
                    |K_N^<(t,u)|\le C_\tau e^{N(M+\tau)} .
 \tag{4}
\]
Every original row in (1), both physical endpoint groups, both
factorial cuts, both aliases and all connector orientations
are retained. No nonzero relative packet is asserted.

The proof uses the exact source construction of the
[taller high-edge theorem](research_mixed_symmetric_closing_high_edge_envelope.md).
The new issue is that \(\cos\beta\) can be negative. Sections
2--4 supply the additional cut and root guards rather than
assuming the older domain covers this case.

## 2. A common polynomial comparison on a cut

For the unchanged sidewise factorial phase
\(F(y;t,u)=b(y,t)+b(y,u)\), the exact force is
\[
 e^{F_y}=
 \frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
                         {(1-\cos2\pi y)^2}.
 \tag{5}
\]
On a cut belonging to a leg with real angle \(a_0\le2\pi/3\)
and height \(h_0\), write
\[
 C=\cosh h_0,\quad d=\cos a_0\ge-1/2,\quad
 q=-\cos(2\pi\Re y)\in[d,1],\quad s_q=\sqrt{1-q^2}.
 \tag{6}
\]
Its own squared numerator is
\[
 O=C^2(q-d)^2+(C^2-1)(s_q-\sqrt{1-d^2})^2.
 \tag{7}
\]
The original derivative comparison makes (7) largest at
\(d=-1/2\); its proof requires only \(C\ge1\) and \(d\le q\).
Consequently, for \(q\ge0\),
\[
 O\le q^2+A_Cq+B_C,\qquad
 A_C=(8C^2-5)/3,\quad B_C=(4C^2-1)/12.
 \tag{8}
\]
For \(q=-v\le0\), the original exact square-root
factorization gives
\[
 O\le(1/2-v)^2(4C^2-1)/3 .
 \tag{9}
\]

Write the cosine of the other leg as \(P+iQ\). Suppose
\[
 |P+iQ|\le\mu,\qquad P\ge-\mu/2,\qquad Q\ge0.
 \tag{10}
\]
For \(q\ge0\), expanding its squared numerator, whose mixed
terms are \(-2CqP\) and \(-2\sqrt{C^2-1}s_qQ\), gives
\[
 |\cos2\pi y+\cos(\text{other leg})|^2
 \le q^2+\mu Cq+C^2+\varepsilon,\qquad
                         \varepsilon\ge\mu^2-1.
 \tag{11}
\]
For \(q=-v\le0\), the same expansion gives
\[
 |\cos2\pi y+\cos(\text{other leg})|
                              \le\mu(C+v).
 \tag{12}
\]
Indeed its square is at most
\(C^2-1+v^2+\mu^2+2Cv\mu\); subtraction from
\(\mu^2(C+v)^2\) leaves
\[
  (\mu^2-1)(C^2-1+v^2)+2\mu(\mu-1)Cv\ge0.
\]

The denominator has modulus \(C+q\). For \(q\ge0\), its
fourth power minus the product in (8),(11) is
\[
 \begin{split}
 \mathcal D_{\mu,\varepsilon}(C,q)
  &=(C+q)^4-(q^2+A_Cq+B_C)
                      (q^2+\mu Cq+C^2+\varepsilon)\\
  &=Tq^3+Vq^2+Lq+J,\\
 T&=(4-\mu)C-A_C,\\
 V&=5C^2-B_C-\varepsilon-\mu CA_C,\\
 L&=C^2(4C-A_C)-\varepsilon A_C-\mu CB_C,\\
 J&=C^2(C^2-B_C)-\varepsilon B_C .
 \end{split}
 \tag{13}
\]
The notation \(J\) in this section is a polynomial coefficient,
not the factorial primitive.

## 3. Both strict cut guards

The elementary positive-series witnesses in the taller theorem
give \(\cosh H<8/5\) and \(\cosh K<13/10\).

### 3.1. The incoming cut

For this cut take
\[
                 1\le C\le8/5,\qquad
                 \mu=13/10,\quad\varepsilon=7/10.
 \tag{14}
\]
Condition (10) holds because
\(\cos u=\cos\beta\cosh K+i\sin\beta\sinh K\),
\(\cos\beta\ge-1/2\), and
\(\mu^2-1=69/100<7/10\).

If \(1\le C\le4/3\), all four coefficients in (13)
are positive. Here
\[
 T\ge71/135>0,\quad
 A_C/C\le83/36,\quad A_C/C^2\le83/48,\quad B_C<C^2/3.
 \tag{15}
\]
The inequality \(4C-A_C\ge61/27>2\) implies
\[
 L>C^2\left(2-\frac{581}{480}-\frac{26}{45}\right)>0.
 \tag{16}
\]
Also \(\mu CA_C<3C^2\), so \(V>0\), and
\[
                         J>\frac{13}{30}C^4>\frac1{10}.
 \tag{17}
\]
The constant estimate in (17) uses
\(J>(2/3)C^4-(7/30)C^2\).

For \(4/3\le C\le8/5\), the quadratic coefficient remains
positive:
\[
 V>\frac{569}{1200}C^2-\frac7{10}
                       \ge\frac{1544}{10800}>0.
 \tag{18}
\]
Moreover
\[
 -21/25\le T\le71/135<1,\qquad J>1.
 \tag{19}
\]
A direct combination of the other coefficients is
\[
 \begin{split}
 J+L+T
  =-\!2C^4+\frac{107}{30}C^3-\frac{181}{60}C^2
                         +\frac{337}{120}C+\frac{347}{120}.
 \end{split}
 \tag{20}
\]
This decreases on the stated interval. Its derivative is
at most
\[
 \frac{C^2}{30}-\frac{181C}{30}+\frac{337}{120}<0,
 \tag{21}
\]
using \(C\ge4/3\) in the first two cubic terms of the
derivative, and then \(C^2\le(8/5)C\).
At \(C=8/5\), (20) equals \(5821/5000\).
Consequently \(J+L>821/5000\), while \(J+T>4/25\).
Together with (19),(20), each of
\[
                    J,\quad J+L,\quad J+T,\quad J+L+T
\]
exceeds \(1/10\). Since \(0\le q\le1\) and \(V>0\),
equation (13) is at least the minimum of these four
quantities. Thus throughout (14)
\[
                   \mathcal D_{13/10,7/10}(C,q)>1/10.
 \tag{22}
\]
As \((C+q)^4\le(13/5)^4<50\), this proves
\[
                    |e^{F_y}|^2<499/500
                                     \qquad(q\ge0).
 \tag{23}
\]

For \(q=-v\le0\), equations (9),(12) and the original
rational maximum in the taller cut proof give
\[
 |e^{F_y}|\le\frac{9\mu}{8\sqrt3}
                 =\frac{117}{80\sqrt3}<1.
 \tag{24}
\]
This negative-coordinate bound does not require \(P\ge0\).

### 3.2. The outgoing cut

Now
\[
                 1\le C\le13/10,\qquad
                 \mu=8/5,\quad\varepsilon=39/25 .
 \tag{25}
\]
The other leg has \(a\le2\pi/3\), so (10) again holds.
For \(q\ge0\), the coefficients in (13) satisfy
\[
 T\ge7/25,\qquad V\ge1257/2500>1/2,\qquad
                         L\ge-3601/2500>-3/2.
 \tag{26}
\]
Here \(T\) is concave with the indicated minimum at an
endpoint. For the second inequality write
\[
 V=-\frac{64}{15}C^3+\frac{14}{3}C^2+\frac83C
                                     +\frac1{12}-\frac{39}{25}.
 \tag{27}
\]
Its derivative is negative for \(C\ge1\), since it is at
most \(-52C/15+8/3<0\). Evaluate at \(13/10\).
Similarly
\[
 L=-\frac83C^4+\frac{52}{15}C^3-\frac{187}{75}C^2
                                      +\frac2{15}C+\frac{13}{5}
 \tag{28}
\]
decreases on \(C\ge1\): the first two terms of its derivative
are at most \(-4C^2/15\), and the remaining derivative is
negative. Its value at \(13/10\) is the bound in (26).

The coefficient
\[
 J=\frac23C^4-\frac{131}{300}C^2+\frac{13}{100}
 \tag{29}
\]
increases on \(C\ge1\). For \(1\le C\le6/5\),
\[
 J\ge9/25,\qquad J+L\ge257/500.
 \tag{30}
\]
For the second assertion, the exact polynomial
\[
 J+L=-2C^4+\frac{52}{15}C^3-\frac{293}{100}C^2
                                      +\frac2{15}C+\frac{273}{100}
 \tag{31}
\]
decreases on this interval. Its derivative is negative:
bound its first two terms by \((12/5)C^2\le(72/25)C\)
and retain the negative term \(-(293/50)C\).
Its value at \(6/5\) is \(257/500\).
Since \(T,V>0\), (30) bounds (13) below by \(9/25\).

For \(6/5\le C\le13/10\), (29) gives
\(J\ge2209/2500>4/5\). Use the exact inequality
\[
                q^3\ge3q-2,\qquad0\le q\le1,
 \tag{32}
\]
whose difference is \((q-1)^2(q+2)\). Equations (26),(32)
then give
\[
 \begin{split}
 \mathcal D_{8/5,39/25}(C,q)
  &>\frac45+\frac7{25}(3q-2)+\frac12q^2-\frac32q\\
  &=\frac6{25}-\frac{33}{50}q+\frac12q^2
                         \ge\frac{111}{5000}.
 \end{split}
 \tag{33}
\]
Thus this bound holds on all of (25).
Since \((C+q)^4\le(23/10)^4<28\), it implies
\[
                    |e^{F_y}|^2<1999/2000
                                     \qquad(q\ge0).
 \tag{34}
\]
Indeed \(111/140000>1/2000\).

For the remaining coordinates \(q=-v\), \(0\le v\le1/2\),
maximize the rational factor in (9),(12) exactly. It has
its maximum at
\[
 v=\frac{C(3-2C)}{6C-1},\qquad
 \max_v\frac{(1/2-v)(C+v)}{(C-v)^2}
                         =\frac{(2C+1)^2}{16C(2C-1)}.
 \tag{35}
\]
This critical point lies in \([0,1/2]\) on (25).
Multiplication by the own square-root factor gives
\[
 \frac{(2C+1)^{5/2}}{16\sqrt3\,C\sqrt{2C-1}}.
 \tag{36}
\]
Its logarithmic derivative has the sign of
\(4C^2-6C+1\). This is negative on \([1,13/10]\):
the convex quadratic has negative values at both ends.
Therefore (36) is at most its value \(9/16\) at \(C=1\).
With \(\mu=8/5\) we obtain
\[
                           |e^{F_y}|\le9/10<1.
 \tag{37}
\]
All four guards (23),(24),(34),(37) include cut endpoints,
intersections and their one-sided limiting values.

## 4. Original critical point and logarithmic charge

Set
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0.
 \tag{38}
\]
The incoming bounds of the taller theorem remain
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20,\quad
 \Re(1/A)>5/32,\quad\Im A>0 .
 \tag{39}
\]
For \(d_0=\cos\beta\in[-1/2,1]\), \(C_0=\cosh K<13/10\),
\[
 \Re B>7/40,\quad |B|<23/20,\quad
 |1-B|<9/10,\quad \Im B\ge0,\quad \Re(1/B)>20/23.
 \tag{40}
\]
The last inequality follows directly from
\[
 \Re(1/B)=\frac{2(1+d_0C_0)}{(C_0+d_0)^2}.
 \tag{41}
\]
Its derivative in \(d_0\) has the sign of
\(C_0^2-C_0d_0-2\), a decreasing function. Hence any
interior critical point is a maximum; the minimum is
at an endpoint. At \(d_0=1\), (41) is
\(2/(C_0+1)>20/23\). At \(d_0=-1/2\), it is
\((2-C_0)/(C_0-1/2)^2\), decreasing in \(C_0\) and
greater than \(35/32>20/23\).

It follows that
\[
 \Re D_0>1-\frac{21}{20}\frac9{10}=\frac{11}{200},
 \qquad
 \Re(1/W)>\frac5{32}+\frac{20}{23}-1=\frac{19}{736},
 \qquad \Im(1/W)<0 .
 \tag{42}
\]
Thus \(W\) remains in a fixed compact subset of the upper
right quadrant, with original finite critical point
\[
                         y_*=\pi^{-1}\arctan\sqrt W .
 \tag{43}
\]
The principal square root and arctangent are those at \(u=0\).
The original identity
\[
 e^{F_y}-1
   =-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
                         \qquad z_y=\tan\pi y,
 \tag{44}
\]
gives the unique finite algebraic critical point in the
upper half-strip and its nonzero Hessian.

Keep \(t\) fixed and continue \(u\) from zero along its
straight segment. The entire path lies in (2). By the strict
cut guards, a force-one point cannot meet a cut or a numerator
zero. The continuous original logarithmic derivative, a
multiple of \(2\pi i\), therefore retains the value zero.
The taller theorem's calibrated base at \(u=0\) gives
\[
 F_y(y_*;t,u)=0,\quad F(y_*;t,u)=\psi(t,u),\quad
 -F_{yy}(y_*;t,u)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0.
 \tag{45}
\]
No additive phase or logarithmic period has been reset.

## 5. The complete upper path and its finite source

Use the original zero-safe envelope
\(\mathcal V(y)=\mathfrak b(y,t)+\mathfrak b(y,u)\).
Its endpoint values are
\[
                       \mathcal V(0)=0,\qquad\mathcal V(1/2)=e.
 \tag{46}
\]
It is continuous and subharmonic, with upward derivative
jump \(+2\pi\) across each upper cut. The starting-zero
flux is \(O(\rho|\log\rho|)\). These are the original
reflection and distributional statements, unaffected by
the larger real angle. The strict cut forces just proved
exclude local minima on both cuts.

On a regular real-wire point, each positive lower leg has
its original numerator argument in \((0,\pi)\); the incoming
leg always has positive height. The upward derivative
therefore excludes a bottom minimum. At \(\beta=0\) the
second argument is zero, and the first remains strict.
At \(K=0,\beta>0\), retain the real-cut one-sided limits
and the strict horizontal cut descent. These exhaust the
degenerate bottom faces of (2).

The exact one-leg side formulas used in the taller theorem
hold for every real leg angle in \([0,\pi)\), which still
contains (2). The left side increases from zero. The right
side decreases to \(\min(H,K)/(2\pi)\) and then increases;
the zero-angle side has derivative zero below its cut height
and \(\pi\) above it. Thus each strict side sublevel is
connected or empty. At large fixed upper height,
\[
 \mathcal V(x+iv)=2\pi v-\frac{aH+\beta K}{2\pi}+o(1)
 \tag{47}
\]
uniformly.

The original component/Jordan lemma therefore applies to
the nondegenerate saddle in (45). Every strict-sublevel
component reaches a vertical side, and the descending
germs reach different sides. The left endpoint is accessible
below \(m\); the right endpoint is accessible below
\(\max(m,e)\). Pushing into the strip and taking fixed small
endpoint collars gives an unweighted path at rate \(M+\epsilon\),
for any fixed \(\epsilon>0\). Compact finite parameter covers
make its lengths and heights uniform.

For clarity, the finite interpolation itself is unchanged:
\[
 \begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y)&=B_N(y,t)B_N(y,u).
 \end{split}
 \tag{48}
\]
Here \(G_N\) is the original reciprocal-factorial function.
At \(y=j/N\), \(T_N(j/N)\) is the exact summand in (1).
All shifted real arguments still range between \(-1/3\)
and \(5/6\): the former first-angle range already reached
\(2\pi/3\). The original reflection identity and zero-safe
uniform factorial estimates consequently give the same
holomorphic interpolation and the bounds
\[
 |T_N|\le CN^{-2}e^{N\mathcal V}
 \quad\hbox{on fixed compact paths},\qquad
 |T_N(j/N)|\le CN^A e^{N\mathcal V(j/N)} .
 \tag{49}
\]
Zeros improve an upper bound. The half-grid displacement
costs only \(O(\log N)\) in its factorial exponents,
uniformly through both endpoint rows.

Both penalized side bounds remain
\[
 \mathcal V(\pm iv)-2\pi v\le D_*,
 \quad \mathcal V(1/2\pm iv)-2\pi v\le e,
 \quad D_*=\frac{aH+\beta K}{2\pi}.
 \tag{50}
\]
Now \(e-D_*\ge(H+K)/6\ge1/60\).
At the original alias height two, every complete dilogarithm
remainder argument has modulus at most \(e^{1-4\pi}<1/10000\).
The original remainder coefficient sum \(4/\pi\) bounds their
total by \(1/600\), so
\[
                      \mathcal V(x\pm2i)-4\pi<e-3/200 .
 \tag{51}
\]
Thus both aliases have the same strict reserve as before.

Choose the original midpoint cuts and a fixed small collar height:
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\quad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N,\quad h_c>0.
 \tag{52}
\]
The paid alias paths are
\(\alpha_N\pm ih_c\to\alpha_N\pm2i
\to\gamma_N\pm2i\to\gamma_N\pm ih_c\).
With \(\zeta=e^{2\pi iNy}\), the exact identity is
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
 \tag{53}
\]
On midpoint columns, \(\zeta=-e^{-2\pi Nv}\), so the full
cap reciprocal has modulus at most one.
Splitting \((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\) above the
real line moves its whole unweighted term to the path already
constructed. Its added endpoint pieces retain the signs
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.
 \tag{54}
\]
They are paid by the same collars. The remaining rational
integrals have their full \(e^{-2\pi N|\Im y|}\) penalty,
not merely its leading Fourier term. Equations (46)--(54)
give \(CN^A e^{N(M+\epsilon)}\). Choose
\(\epsilon<\tau/2\), and absorb the polynomial factor to
prove (4).

## 6. What remains for the right closing connector

On an eligible lower inner contour, the first shortened edge
has rate \(\Re\psi(t,0)\). The theorem then bounds its full
cubic angular integrand by the larger of
\[
 \Re\{\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it\},
 \qquad
 \Re\psi(t,0)+(H+K)/2+3aH/(2\pi)-H .
 \tag{55}
\]
The new real-angle range in (2) is genuine finite-source
control of this edge. Neither rate in (55) has here been
compared with the actual inner action for outgoing
\(\Re u>\pi/2\). The signed central inner horizontal,
its center bridge, and the low/far first-angle currents
also require an enlarged-source assembly. In particular
(4) alone does not estimate the full \(Q_N(w,u)\), nor the
right outer current from \(\pi/2-iK_g\) to its far midpoint.
The complete crossing and outer sampling phases cannot
be dropped in making those subsequent comparisons.

## Frozen source bindings

- Taller high-edge complete source, cut comparisons and aliases:
  9451d127c809566902d4b629e949b6c87517b9ffc06ff27776e191573ec88c5f.
- Original independent cut/root base:
  7f3c6a64aab48f54e60dcf4c0c192f348f0d8e64c0f3547fd5783c9ef3b11ca5.
- Original vertical side limits and upper envelope:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Subharmonic component/Jordan proof:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Literal joined source and cap identity:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Complete lower primitive and reflected remainders:
  79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c.
- Uniform zero-safe factorial source:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
