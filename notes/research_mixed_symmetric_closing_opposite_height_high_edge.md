# The complete high edge with opposite angular heights

Private finite-source proof, 9 November 2026. This note extends the
high-edge upper envelope to upper outgoing angles. The saddle is
allowed to change wire half-planes. All original reciprocal-factorial
cuts, physical rows, caps and aliases are retained. On compact subsets
where the saddle exceeds the endpoint rate it also gives the original
nonzero edge packet.

No mathematical numerical evaluation, saved arithmetic, import,
compilation, test or frozen-source edit is used.

## 1. Source and statement

Keep the original sine products and Newton polynomials
\[
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_j(X)=S_j^{-2}\prod_{\nu<j}(c_\nu-X).
\]
The independent parameter box is
\[
 t=a-iH,\quad \pi/2\le a\le2\pi/3,\quad 1/10\le H\le1,
 \qquad u=\beta+iK,\quad0\le\beta\le\pi/2,\quad0\le K\le7/10 .
 \tag{1}
\]
The literal finite source is
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
 \tag{2}
\]
In particular no odd middle row is restored in (2). Set
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad D_0=A+B-AB,\quad
 W=AB/D_0,\qquad e=(H+K)/2.
 \tag{3}
\]
The phase \(\psi(t,u)\) is the original zero-charge critical value,
continued from \(K=0\) as specified below; put \(m=\Re\psi(t,u)\).

**Theorem.** For each fixed \(\tau>0\), uniformly on (1) at both
level parities,
\[
 |K_N^<(t,u)|\le C_\tau e^{N(\max\{m,e\}+\tau)}.
 \tag{4}
\]
On each compact subset of (1) on which \(m>e\), this improves,
on a fixed independent complex neighborhood of that subset, to
\[
 K_N^<(t,u)=N^{-3/2}
 \frac{e^{N\psi(t,u)}}{4\sqrt{D_0}\,W^{1/4}}
                  (1+O_{\rm hol}(N^{-1})).
 \tag{5}
\]
The roots and orientation are the continued original Gaussian ones.
All fixed normalized parameter derivatives obey the same error bound
on smaller neighborhoods. No relative statement is made across \(m=e\).

## 2. The two original cuts have strictly descending force

Write \(F(y;t,u)=b(y,t)+b(y,u)\) for the original sidewise factorial
phase. Its unchanged force is
\[
 e^{F_y}=
 \frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
      {(1-\cos2\pi y)^2}.
 \tag{6}
\]
The incoming cut starts at \(1/2-a/(2\pi)+iH/(2\pi)\); the outgoing
cut starts at \(1/2-\beta/(2\pi)-iK/(2\pi)\). Both run right.
The zero-angle outgoing cut is on the boundary, and at \(K=0\) the
nonempty outgoing cut is on the real wire.

Use \(\mu=13/10\), so \(\cosh K<\mu\), and write
\[
 C=\cosh H<8/5,\quad S=\sinh H,\quad d=\cos a\in[-1/2,0],
 \quad q=-\cos(2\pi\Re y),\quad s_q=\sqrt{1-q^2}
\]
on the incoming cut. Its own squared numerator is
\[
 O=C^2(q-d)^2+(C^2-1)(s_q-\sqrt{1-d^2})^2,\qquad
 |1-\cos2\pi y|=C+q. \tag{7}
\]
The original incoming-cut comparison maximizes \(O\) at \(d=-1/2\).
For \(q\le0\) it gives
\[
 O\le(q+1/2)^2(4C^2-1)/3;
\]
for \(q\ge0\) it gives
\[
 O\le q^2+A_Cq+B_C,\qquad
 A_C=(8C^2-5)/3,\quad B_C=(4C^2-1)/12. \tag{8}
\]
These are the exact inequalities of the
[independent cut proof](research_mixed_next_independent_rectangle_cut_guards.md)
and [lower high-edge theorem](research_mixed_symmetric_closing_high_edge_envelope.md).
They do not use the sign of the other height.

Put \(C_0=\cosh K\), \(S_0=\sinh K\), \(b=\cos\beta\),
\(s_b=\sin\beta\). In the present opposite-height case the other
squared numerator is
\[
 (Cq-C_0b)^2+(Ss_q+S_0s_b)^2.
 \tag{9}
\]
Completing the square in \(s_b\), using
\(b^2+2SS_0s_qs_b\le1+S^2S_0^2s_q^2\), proves, for \(q\ge0\),
\[
 (9)\le C^2C_0^2+\{1-S^2S_0^2\}q^2
       \le \lambda C^2+\{\lambda-(\lambda-1)C^2\}q^2,
 \qquad\lambda=169/100. \tag{10}
\]
The omitted cross term \(-2CC_0qb\) is nonpositive. The last
expression increases with \(C_0^2\), since
\(C^2-(C^2-1)q^2\ge1\).
For \(q=-v\le0\), the same completion, followed by \(b\le1\), gives
\[
 (9)\le C^2C_0^2+v^2+2CC_0v=(CC_0+v)^2
                                  \le\mu^2(C+v)^2. \tag{11}
\]
Thus the original negative-coordinate maximization still gives
\[
 |e^{F_y}|\le\frac{9\mu}{8\sqrt3}
              =\frac{117}{80\sqrt3}<1
 \tag{12}
\]
there; its exact cleared remainder is \((1-5v)^2\).

For \(q\ge0\), put \(V=C^2\) and
\(k=\lambda-(\lambda-1)V\le1\). Subtracting the product of (8),(10)
from \((C+q)^4\) gives
\[
 (1-k)q^4+(4C-kA_C)q^3
 +(6V-\lambda V-kB_C)q^2
 +V(4C-\lambda A_C)q+V^2-\lambda VB_C. \tag{13}
\]
On \(1\le C\le8/5\),
\[
 4C-A_C\ge31/25,\quad B_C<V/3,\quad
 4C-\lambda A_C\ge-5801/2500>-7/3.
\]
The last minimum is at an endpoint of a concave quadratic; its
two endpoint values are \(231/100\) and \(-5801/2500\).
Consequently (13) is strictly greater than
\[
 V\left\{\frac{1193}{300}q^2-\frac73q+\frac{131}{300}V\right\}
 \ge V\left(\frac{131}{300}-\frac{1225}{3579}\right)
 >V/12. \tag{14}
\]
The final rational comparison follows from
\(12(468849-367500)>1073700\).
Since \((C+q)^4\le16V^2\) and \(V\le64/25\),
\[
                         |e^{F_y}|^2<499/500. \tag{15}
\]
Indeed the relative loss exceeds \(25/12288>1/500\).

On the outgoing cut its coordinate \(q_0\) is nonnegative.
The original sign-independent own-cut estimate and the triangle
bound for the other cosine give
\[
 |e^{F_y}|
 \le \frac{\sqrt{2C_0^2-1}}{C_0+1}
            \frac{C_0+8/5}{C_0+1}
 <\frac{13\sqrt{238}}{230}<1. \tag{16}
\]
The first factor increases with \(C_0\), the second is at most
\(13/10\); the squared comparison is \(40222<52900\).
All starting zeros and zero-height limits are included by continuity.

## 3. One continued critical point, including real crossings

The same real-part and modulus bounds as in the lower high-edge
proof are insensitive to the outgoing-height sign:
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20,\quad
 \Re(1/A)>5/32,\quad\Im A>0,
\]
\[
 \Re B\ge1/2,\quad |B|<23/20,\quad |1-B|<13/20,\quad
 \Re(1/B)>20/23,\quad\Im B\le0.
 \tag{17}
\]
Therefore
\[
 \Re D_0>127/400,\qquad
 \Re(1/W)>19/736>0. \tag{18}
\]
The exact force factorization is
\[
 e^{F_y}-1=-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
 \qquad z_y=\tan\pi y.
 \tag{19}
\]
The unique finite algebraic critical point in the open full strip is
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0. \tag{20}
\]
All quantities stay in fixed compact sets away from their relevant
zeros and strip boundaries. Scaling \(K\) from zero retains
(12),(15),(16),(18). Thus \(y_*\) crosses no original cut or zero.
The continuous original logarithmic force belongs to \(2\pi i\mathbb Z\)
and starts at zero. Hence it remains zero, and
\[
                  F_y(y_*)=0,\qquad F(y_*;t,u)=\psi(t,u). \tag{21}
\]
The constant is the original one from the lower high-edge proof.
Equivalently its derivatives are the original principal returns:
\[
 d\psi=-\pi^{-1}\{\operatorname{arsinh}(\tan(t/2)\cos(u/2))\,dt
             +\operatorname{arsinh}(\tan(u/2)\cos(t/2))\,du\}.
 \tag{22}
\]
To check this identification throughout the box, write
\(c=\cos(t/2)\), \(C_1=\cos(u/2)\).
One has \(|\arg c|<\pi/4\), since
\(\tan(a/2)\tanh(H/2)<\sqrt3/2<1\), and
\(|\arg C_1|<7/20<\pi/4\). Together with \(\Re D_0>0\),
the continued principal coshes \(\sqrt{D_0}/c\) and
\(\sqrt{D_0}/C_1\) have positive real part. Thus the returns
do not reach their cuts, and (22) has the original zero lift.

For an optional precise real-transition guard, write
\(1/A=x-iy\), \(1/B=v+iy\) when \(\Im(1/W)=0\).
The outgoing imaginary magnitude is smaller than \(40/41\):
\[
 \Im(1/B)=\frac{2\sin\beta\,\sinh K}{(\cosh K+\cos\beta)^2}
 \le\frac{2\sinh K}{1+\sinh^2K}<40/41,
 \tag{23}
\]
using
\(\sinh K\le(7/10)/(1-49/600)=420/551<4/5\),
by the positive series and its decreasing successive ratios.
The expression increases with \(\beta\)
and with \(\sinh K<1\).
If \(x\le1\), put \(d=-\cos a\in[0,1/2]\).
The condition is \(C^2+d^2\ge2\), and
\[
 y=\frac{2\sqrt{1-d^2}\sqrt{C^2-1}}{(C-d)^2}.
 \tag{24}
\]
For fixed \(d\), this function has only a maximum as \(C\) varies:
its derivative has the sign of \(2-C^2-dC\).
At \(C^2+d^2=2\), it is at least one by
\(\Re A\le1/2\), or \(|1/A-1|\ge1\).
At the other possible endpoint \(H=1\), it is at least its value
at \(d=0\), since its logarithmic \(d\)-derivative has numerator
\(2-Cd-d^2>0\).
The positive series gives \(\sinh1<67/57<6/5\), so this last value
exceeds \(60/61>40/41\). This contradicts (23), and \(x>1\).
The disks \(|1/A-1|\ge1\), \(|1/B-1|\le1\) then give \(x+v>2\).
Strictness follows unless \(\Re A=\Re B=1/2\); in that case
\(v=2/\cosh^2K>1\) and \(x>1\) separately.
Thus any real crossing has \(0<W<1\), in particular \(y_*<1/4\).
The series bound used here follows by bounding the tail after
\(1+1/6\) with successive ratio at most \(1/20\).

## 4. The real row profile has exactly one maximum

This replaces the individual-factor argument, which does not extend
to the high first angle. Set
\[
 v=\sin^2(\pi x),\quad
 a_0=\Re A,\quad b_0=\Re B,\quad r=|A|^2,\quad s=|B|^2,
 \quad l=\frac{|A-v|^2}{v^2},\quad m_0=\frac{|B-v|^2}{v^2}.
 \tag{25}
\]
The derivative of the original real row profile is
\(\log(\sqrt{l m_0})\). For each factor,
\[
 \frac{d}{dv}\log\frac{|A-v|}{v}
       =\frac{a_0v-r}{v|A-v|^2}. \tag{26}
\]
We prove that the total logarithmic derivative is strictly negative
whenever \(l m_0\ge1\).

If the \(B\)-derivative in (26) is nonnegative, then \(v\ge1/2\)
and \(m_0\le1-1/(2v)\le1/2\).
Writing \(w=1/v\in[1,2]\), the incoming expression
\[
 l=1-(1+C\cos a)w+(C+\cos a)^2w^2/4
\]
is separately convex in \(C,\cos a,w\).
Its eight corner values, on
\([1,8/5]\times[-1/2,0]\times[1,2]\), are at most \(181/100\).
For example the maximal candidate is
\(1-w/5+121w^2/400\), with maximum \(181/100\) at \(w=2\);
the other first-angle endpoint is at most \(39/25\).
Thus \(l m_0\le181/200<1\), a contradiction.

It remains to consider \(a_0v-r\ge0\). Then \(l<1\), so
\(m_0>1\) whenever \(l m_0\ge1\). The exact high-angle constraints give
\[
 r\ge a_0^2,\qquad r\ge(3/4-2a_0)^2. \tag{27}
\]
For the second bound, write \(a_0=(1+C\cos a)/2\).
At fixed \(a_0\), \((C+\cos a)^2/4\) increases with \(C\ge1\);
the restriction \(\cos a\ge-1/2\) gives \(C\ge2-4a_0\).
For \(a_0\le1/4\) the minimum is therefore
\((3/4-2a_0)^2\); for \(a_0\ge1/4\) the first inequality
in (27) implies the second. Since \(r\le a_0v\), (27) yields
\[
 v\ge1/4,\qquad
 a_0\ge9/40\quad(v\le2/5),\qquad
 a_0>1/5\quad(v<23/40). \tag{28}
\]
These follow by decreasing the difference
\((3/4-2a_0)^2-a_0v\) in \(a_0\le1/4\).
At \(a_0=9/40,v=2/5\) it is zero; at
\(a_0=1/5,v=23/40\) it is positive.

The inequality \(m_0>1\) implies
\[
 v<s/(2b_0)<23/40,\qquad b_0\ge1/2. \tag{29}
\]
Indeed \(s/b_0=(\cosh K+\cos\beta)^2/
[2(1+\cosh K\cos\beta)]\) increases with \(\cos\beta\);
its derivative has the sign of
\(2-\cosh^2K+\cosh K\cos\beta>0\).
Its maximum is \((1+\cosh K)/2<23/20\).
On the whole interval in (28)--(29),
\[
             m_0\le M(v):=(23/(20v)-1)^2. \tag{30}
\]
To check (30), the outgoing squared factor increases with \(\cosh K\)
and is convex in \(\cos\beta\). At \(\cosh K=13/10\) the
\(\cos\beta=1\) endpoint exceeds the zero endpoint by
\((9-13v)/(10v^2)>0\).

Using \(l\ge1/m_0\) and \(1-a_0/v>0\), the total logarithmic
derivative, multiplied by \(v\), is at most
\[
 T=m_0(1-a_0/v)+(1-b_0/v)/m_0-2. \tag{31}
\]
This expression decreases with \(a_0,b_0\).
After replacing them by \(9/40,1/2\) when \(v\le2/5\),
or \(1/5,1/2\) when \(v\ge2/5\), it increases with \(m_0\ge1\).
For the first range the second derivative contribution has the
favorable sign since \(v<1/2\). For the second range its derivative
is at least \(1/2-3/23>0\).
It therefore suffices to substitute (30).

For \(1/4\le v\le2/5\), set \(x=20v\in[5,8]\).
The sign of (31) with these substitutions is the sign of
\[
 P(x)=-29x^4+5060x^3-125902x^2+997694x-2518569.
 \tag{32}
\]
This follows by multiplying
\((v-9/40)M(v)^2-2vM(v)+v-1/2\) by \(40x^4>0\).
Direct written differentiation gives
\[
 P''=-348x^2+30360x-251804<-30000,\qquad
 P(6)=-9501,\quad P'(6)=8294.
 \tag{33}
\]
For the first inequality \(P''\) increases on \([5,8]\) and
\(P''(8)=-31196\).
Taylor's upper quadratic therefore gives
\[
 P(x)\le-9501+8294(x-6)-15000(x-6)^2
                 <-9501+9000^2/60000<0. \tag{34}
\]

For \(2/5\le v<23/40\), it is enough to prove
\[
 A_{\rm req}(v):=v(1-M(v)^{-1})^2-\{2M(v)^2\}^{-1}<1/5 .
 \tag{35}
\]
Here \(M\ge1\). Put \(B_*=23/20\), so
\(M=(B_*-v)^2/v^2\) and
\(M'=-2B_*(B_*-v)/v^3\).
Differentiation gives
\[
 A_{\rm req}'=(1-M^{-1})^2
       +\frac{2M'}{M^3}\{v(M-1)+1/2\}. \tag{36}
\]
On \(v\in[2/5,1/2]\) the brace is at least \(vM\).
Consequently the second term is at most
\(-4B_*v^2/(B_*-v)^3<-1\), since
\(4(2/5)^2/(3/4)^3=1024/675>1\).
On \(v\in[1/2,23/40]\) the brace is at least \(M/2\);
the second term is at most
\(-2B_*v/(B_*-v)^3<-1\).
Thus (36) is negative. At the left endpoint,
\[
 M(2/5)=225/64,\qquad
 A_{\rm req}(2/5)=41602/253125<1/5. \tag{37}
\]
This proves (35), and hence strict negativity in (31).

Both individual negative derivatives already give the desired sign
in the remaining case. The force modulus starts at infinity as
\(v\downarrow0\), and at \(v=1\) equals
\[
 |1-A||1-B|<(21/20)(13/20)<1.
 \tag{38}
\]
Every crossing of one is strictly downward, by the result just proved.
There is exactly one. Numerator zeros have force zero and are used
only through integrable one-sided limits. The complete real profile
increases to one strict maximum and then decreases, so has no
interior local minimum.
If \(W\) is real, (20)--(21) identify its saddle with this maximum,
and its real second derivative is negative.

## 5. The main path in the saddle half-plane

The original sidewise real envelope \(\mathcal V\) is continuous
and subharmonic in either wire half-strip. Its cut-normal derivative
jumps by \(2\pi\), and starting-zero flux tends to zero.
The strict cut bounds of Section 2 exclude local minima on every cut.
The real row result supplies the bottom-boundary hypothesis.

The left-side rate is strictly increasing outward from zero.
The original one-leg formula is
\[
 \pi\ \pm\{\vartheta_r(s+v)+\vartheta_r(s-v)\},\qquad
 \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)).
 \tag{39}
\]
Here \(r=a/(2\pi)\le1/3\), or \(r=\beta/(2\pi)\le1/4\),
and the brace has absolute value at most \(2\pi r<\pi\).
Thus each left strict sublevel is connected or empty.

We check the right side in the saddle half-plane, rather than
asserting connectedness of its entire two-sided trace.
Write
\[
 \cos t=P_t+iQ_t,\quad \cos u=P_u-iQ_u,\quad
 -4/5<P_t\le0,\quad P_u\ge0,\quad
 0<Q_t<6/5,\quad0\le Q_u<4/5 .
 \tag{40}
\]
Between the two cut heights its derivative in the upward wire
coordinate has the sign, and exact argument representation,
\[
 g(C_v)=\Arg(P_u-C_v+iQ_u)-\Arg(P_t-C_v+iQ_t),\quad
 C_v=\cosh(2\pi v),
\]
\[
 \operatorname{sign}g(C_v)
 =\operatorname{sign}\{(Q_t-Q_u)C_v-(Q_tP_u-Q_uP_t)\}.
 \tag{41}
\]
This is the reflected version of the original mixed-side formula.
At a regular stationary point the aligned upper vectors can be written
\[
 P_t-C+iQ_t=\lambda e^{i\theta},\qquad
 P_u-C+iQ_u=\mu e^{i\theta}.
 \tag{42}
\]
Their real parts force \(\lambda\ge\mu\), with strict inequality
unless the vectors coincide; hence \(Q_t>Q_u\) in the strict case.
The crucial product inequality holds even though the individual
incoming right force need not be below one:
\[
 \lambda\mu=(C-P_t)(C-P_u)+Q_tQ_u
 < C^2+\frac45C+\frac{24}{25}<(C+1)^2. \tag{43}
\]
We used \(P_tP_u\le0\), \(P_u\ge0\), and (40).
The exact subtraction in the original mixed proof now yields
\[
 \Im(1/W)=
 -\frac{2\sin\theta(\lambda-\mu)
             ((1+C)^2-\lambda\mu)}
 {|1+P_t+iQ_t|^2|1+P_u+iQ_u|^2}<0.
 \tag{44}
\]
An upper stationary point in (41) is a minimum, because \(C_v\)
increases there. A lower local maximum can occur only with the
strict aligned vectors just considered; (44) then forces
\(\Im W>0\). It is absent in the lower half-plane containing
a lower saddle. Outside the cut-height interval the derivative
has its original fixed outward sign. A cut jump cannot create a
local maximum.
Coincident vectors give a real saddle. At \(Q_u=0\) the direct
one-leg limits give a minimum or monotone side: \(K=0\) puts its
minimum at zero, while \(\beta=0\) gives a flat outgoing leg before
its cut and a strictly increasing outward leg after it. These
limits introduce no omitted maximum.
Thus in the half-plane of a nonreal saddle every right strict
sublevel is connected or empty.

At large upper and lower heights the unweighted envelope is
\(2\pi|v|+O(1)\), uniformly. The original component/Jordan proof
therefore applies in the chosen half-strip. Every strict-sublevel
component at level \(m\) reaches a vertical side, since no bottom,
cut or interior minimum is possible. At most two components exist.
The two descending germs cannot rejoin in one component: a finite
crosscut would enclose an ascending germ with smaller boundary
values, contradicting subharmonicity. They consequently reach the
different sides. In particular \(m>0\), since the left-side
sublevel is nonempty.

The left side connects to its real endpoint below \(m\).
The right side, with no local maximum in this half-plane, connects
to its real endpoint below \(\max(m,e)\).
Small collars and a finite cover of the compact parameter box yield,
for every fixed \(\epsilon>0\), bounded-length main paths from
fixed interior real cuts \(\alpha\) to \(\gamma\), at rate at most
\(\max(m,e)+\epsilon\).
At a real saddle use the unique real maximum and its local Morse
deformation. This requires no denominator at a shrinking height.

On a compact set \(m>e\), both endpoints are strictly below \(m\).
The same construction has strict gaps away from the unique saddle;
the two descent sectors give its single left-to-right crossing.
The local orientation is continued from the original real branch,
including across the real-saddle charts.

## 6. Both full aliases, caps and physical endpoint groups

The original canonical interpolation is
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\quad
 T_N(y)=B_N(y,t)B_N(y,u). \tag{45}
\]
It equals the literal row at \(y=j/N\), and reciprocal reflection
makes it holomorphic throughout the open wire strip at finite height.
The shifted real arguments remain between \(-1/3\) and \(5/6\).
The original uniform factorial theorem gives the zero-safe
upper bound \(CN^A e^{N\mathcal V}\), including the initial row,
last retained row and every shifted zero.

The exact penalized side bounds, for either sign of the wire height,
are
\[
 \mathcal V(\pm iv)-2\pi v\le D_*:=\frac{aH+\beta K}{2\pi},
 \qquad
 \mathcal V(1/2\pm iv)-2\pi v\le e,
 \qquad e-D_*\ge H/6+K/4\ge1/60. \tag{46}
\]
These are the sign-independent one-leg formulas of the original
mixed proof, valid also for \(a/(2\pi)\le1/3\).
At deep height two, all eight original dilogarithm remainders have
arguments of modulus at most \(e^{1-4\pi}<1/10000\).
The sum of their coefficient moduli is \(4/\pi\).
The positive-series witness \(e^5>100\), together with \(\pi>3\),
therefore gives
\[
 \mathcal V(x\pm2i)-4\pi
       <D_*+4/(9999\pi)<e-3/200. \tag{47}
\]
No reflected primitive is omitted.

Choose fixed sufficiently small endpoint collars and midpoint cuts
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N,\qquad
 \zeta=e^{2\pi iNy}.
 \tag{48}
\]
The two complete alias paths run from \(\alpha_N\pm ih_c\)
to \(\alpha_N\pm2i\), across to \(\gamma_N\pm2i\),
and back to \(\gamma_N\pm ih_c\).
Uniform continuity transfers (46) to the interior columns.
The endpoint rates \(0,e\) and zero-safe continuity pay both
physical endpoint groups at rate \(e+\epsilon\).

The unchanged exact joined identity is
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
\end{split} \tag{49}
\]
Split \((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\) above the wire,
and move only the unweighted entire integral to the main path.
The exact added caps are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
       +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy. \tag{50}
\]
Both remaining alias denominators supply
\(2e^{-2\pi N|\Im y|}\) on their paths; the external midpoint
cap denominators have modulus at least one.
Thus all of (49)--(50) have the asserted upper rate, with their
original signs and factor \(N\). Fixed polynomial factors are
absorbed by choosing \(\epsilon<\tau/2\). This proves (4).

On compact subsets \(m>e\), every alias, cap and physical endpoint
group is strictly lower. Off the original cuts the unchanged symbol is
\[
 T_N(y)=\frac{e^{NF(y)}}{4N^2\sin^2(\pi y)}(1+O(N^{-1})).
 \tag{51}
\]
Using (20), the Gaussian of the single main crossing is
\[
 N\,N^{-2}N^{-1/2}
 \frac{\sqrt{2\pi}}{4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*)}}
       =N^{-3/2}\frac1{4\sqrt{D_0}\,W^{1/4}}.
 \tag{52}
\]
All remote margins persist on fixed independent parameter charts;
a finite cover gives the asserted neighborhood. Normalized Cauchy
estimates prove the fixed derivative claim. This proves (5).

In particular, at any point where \(m>e\), the exact row
Cauchy--Schwarz bound implies
\[
 m\le m_{\rm row}(t)+m_{\rm row}(u),
 \tag{53}
\]
where \(m_{\rm row}\) is the complete real-row entropy maximum
of the original finite products. This follows by taking the
exponential rate of (5), then the complete-row upper bound; it
does not replace the complex source by positive coefficients.
For \(m\le e\) the geometric sector is already below the endpoint
sector. Any attached inner action comparison remains separate.

## Frozen source bindings

- Original independent incoming-cut identities:
  7f3c6a64aab48f54e60dcf4c0c192f348f0d8e64c0f3547fd5783c9ef3b11ca5.
- Lower high-edge source, endpoint and height-two alias inventory:
  9451d127c809566902d4b629e949b6c87517b9ffc06ff27776e191573ec88c5f.
- Original mixed side identities, charge and main-path proof:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Taller central mixed source and original primitive calibration:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Original component/Jordan and subharmonicity argument:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Exact complete main/alias separation and caps:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Original deep-height primitive and reflected remainder:
  79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c.
- Zero-safe reciprocal-factorial bounds:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Exact full-row Cauchy bound used in (53):
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
