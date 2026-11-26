# Original cut guards on an independent outgoing rectangle

Private written source-domain lemma, 9 November 2026. The two
reciprocal-factorial cut forces remain strictly below one on the full
independent outgoing rectangle, including the region where the outgoing
cosine has modulus greater than one. The original upper wire root and
its zero logarithmic charge continue throughout the stated first-angle
family. No numerical evaluation or frozen-source edit is used.

This lemma does not estimate a finite kernel or any inner or outer
current. It supplies cut and branch inputs for a separate contour
argument.

## 1. Independent parameters and original force

Let
\[
 u=\beta-iK,\quad 0\le\beta\le8/7,\quad 0\le K\le2/5,\qquad
 t=a-iH,\quad \pi/2\le a\le2\pi/3,\quad1/10\le H\le1.
 \tag{1}
\]
There is no condition \(K\le\beta/2\), and no selected outer
stationary equation is imposed.

Use exactly the sidewise factorial phases of
[the original cut theorem](research_mixed_next_selected_right_edge_cut_guards.md).
For \(0<\Re y<1/2\), their exponentiated derivative is
\[
 e^{F_y(y;t,u)}
   =\frac{(\cos(2\pi y)+\cos t)(\cos(2\pi y)+\cos u)}
                  {(1-\cos(2\pi y))^2},
 \qquad F(y;t,u)=b(y,t)+b(y,u).
 \tag{2}
\]
The upper cuts begin at
\[
 y=\frac12-\frac{a}{2\pi}+\frac{iH}{2\pi},
 \qquad
 y=\frac12-\frac{\beta}{2\pi}+\frac{iK}{2\pi},
 \tag{3}
\]
and run horizontally to the right boundary. If \(\beta=0\),
the second cut has no open interior segment. If \(K=0,\beta>0\),
it lies on the real bottom. All estimates below include the
appropriate boundary limits and starting zeros.

**Theorem.** On the incoming cut, the modulus \(\mathfrak f=|e^{F_y}|\)
satisfies
\[
 \mathfrak f\le
 \begin{cases}
 39/(32\sqrt3),&-\cos(2\pi\Re y)\le0,\\
 \sqrt{77/80},&-\cos(2\pi\Re y)\ge0 .
 \end{cases}
 \tag{4}
\]
On the outgoing cut,
\[
                  \mathfrak f\le13\sqrt{79}/150<1.
 \tag{5}
\]
The algebraic upper saddle stays simple, uniformly away from the
boundary of the upper half-strip. Its original logarithmic derivative
is zero and its value is the unchanged \(\psi(t,u)\).

## 2. The independent outgoing bounds

Write
\[
 \cos u=P+iQ_0,\qquad \mu=\frac{13}{12},\qquad
 \varepsilon=\mu^2-1=\frac{25}{144}<\frac15 .
 \tag{6}
\]
The positive hyperbolic-cosine series gives
\[
 \cosh K\le
 1+\frac{(2/5)^2/2}{1-(2/5)^2/12}
 =\frac{40}{37}<\frac{13}{12},
 \tag{7}
\]
where the last comparison is \(480<481\). Since
\(\cos\beta\ge1-\beta^2/2\ge17/49>7/30\), we have
\[
 |\cos u|\le\cosh K<\mu,\qquad
 P=\cos\beta\cosh K>7/30,\qquad P\le\mu,\qquad Q_0\ge0.
 \tag{8}
\]
These bounds hold on the whole rectangle, including its imaginary
axis. No assertion \(|\cos u|\le1\) is made.

## 3. The incoming cut, including its negative coordinate

Put
\[
 C=\cosh H,\quad S=\sinh H,\quad d=\cos a\in[-1/2,0],
 \quad q=-\cos(2\pi\Re y)\in[d,1],\quad s_q=\sqrt{1-q^2}.
 \tag{9}
\]
Then \(1\le C<8/5\), and on this cut
\[
 \cos(2\pi y)=-Cq-iSs_q,\qquad
 |1-\cos(2\pi y)|=C+q>0.
 \tag{10}
\]
The exact squared incoming numerator is
\[
 O=C^2(q-d)^2+(C^2-1)(s_q-\sqrt{1-d^2})^2.
 \tag{11}
\]
It is bounded above by its value at \(d=-1/2\).
Indeed, half its derivative with respect to \(a\) is
\[
 C^2(q-d)\sin a+(C^2-1)(\sin a-s_q)d.
 \tag{12}
\]
For \(q\le0\), the second term is nonnegative since
\(d\le q\le0\). For \(q\ge0\), that term is either
nonnegative or at least \((C^2-1)\sin a\,d\);
in the latter case (12) is at least
\(\sin a(C^2q-d)>0\). The comparison follows.

Suppose first \(-1/2\le q\le0\), and set \(v=-q\).
The other numerator obeys
\[
 |\cos(2\pi y)+\cos u|^2
 =S^2+v^2+|\cos u|^2+2CvP-2Ss_qQ_0
 \le S^2+v^2+\mu^2+2Cv\mu
 \le\mu^2(C+v)^2.
 \tag{13}
\]
For the last inequality subtract the middle expression from
the right side. The difference is
\[
 (\mu^2-1)(S^2+v^2)+2\mu(\mu-1)Cv\ge0.
 \tag{14}
\]
The exact factorization
\[
 s_q-\frac{\sqrt3}{2}
   =\frac{(1/2-q)(1/2+q)}{s_q+\sqrt3/2}
\]
in (11) gives
\(O\le(q+1/2)^2(4C^2-1)/3\).
Thus
\[
 \mathfrak f\le\frac{2\mu}{\sqrt3}
       \frac{C(1/2-v)(C+v)}{(C-v)^2}
 \le\frac{2\mu}{\sqrt3}
       \frac{(1/2-v)(1+v)}{(1-v)^2}
 \le\frac{9\mu}{8\sqrt3}=\frac{39}{32\sqrt3}<1 .
 \tag{15}
\]
The middle factor decreases with \(C\ge1\), since the
logarithmic derivative of \(C(C+v)/(C-v)^2\) has numerator
\(-v^2-3Cv\). The last rational inequality is
\((1-5v)^2\ge0\) after clearing denominators.
Strictness of the final bound follows from \(1521<3072\).

For \(0\le q\le1\), use
\(\sqrt3\sqrt{1-q^2}\ge(5/3)(1-q)\) in (11). This gives
\[
 O\le q^2+A_Cq+B_C,\qquad
 A_C=\frac{8C^2-5}{3},\qquad B_C=\frac{4C^2-1}{12}.
 \tag{16}
\]
By (8), the squared other numerator is at most
\[
                 q^2-\frac7{15}Cq+C^2+\varepsilon .
 \tag{17}
\]
In particular it is not replaced by the old unit-modulus estimate.
Put \(d_0=7/15\). The denominator minus the product of the
upper bounds (16)--(17) is exactly
\[
\begin{split}
 &(C+q)^4-(q^2+A_Cq+B_C)(q^2-d_0Cq+C^2+\varepsilon)\\
 &=[(4+d_0)C-A_C]q^3\\
 &\quad+[5C^2-B_C+d_0CA_C-\varepsilon]q^2\\
 &\quad+[C^2(4C-A_C)+d_0CB_C-\varepsilon A_C]q\\
 &\quad+C^2(C^2-B_C)-\varepsilon B_C .
\end{split}
 \tag{18}
\]
For \(1\le C\le8/5\), concavity in \(C\) and the two
endpoints give
\[
 (4+d_0)C-A_C\ge149/75,\qquad 4C-A_C\ge31/25 .
 \tag{19}
\]
Also \(0<A_C<(8/3)C^2\) and \(0<B_C<C^2/3\).
The quadratic coefficient in (18) is positive. Its linear
coefficient is greater than
\[
               C^2(31/25-8/15)=53C^2/75>0 .
 \tag{20}
\]
The constant term is greater than
\[
 \frac23C^4-\frac1{15}C^2\ge\frac35C^4.
 \tag{21}
\]
Thus (18) exceeds \(3C^4/5\). Since \(q\le1\le C\),
\((C+q)^4\le16C^4\), proving
\(\mathfrak f^2\le77/80\). This proves both parts of (4).

## 4. The outgoing cut

This cut's own real angle is \(\beta<\pi/2\). The original
nonnegative-coordinate calculation in
[the mixed-height source, (10)--(12)](research_mixed_next_shortened_edge_mixed_height_packet.md)
therefore applies, independently of \(P\le1\).
For completeness put \(C_0=\cosh K\), and
\(q_0=-\cos(2\pi\Re y)\in[\cos\beta,1]\subset[0,1]\).
The own numerator and denominator satisfy
\[
 |\cos(2\pi y)+\cos u|\le q_0\sqrt{2C_0^2-1},
 \qquad |1-\cos(2\pi y)|=C_0+q_0.
 \tag{22}
\]
For the other angle \(|\cos t|\le\cosh H<8/5\).
Since \(|\cos(2\pi y)|\le C_0\),
\[
 \mathfrak f\le
 \frac{q_0\sqrt{2C_0^2-1}(C_0+8/5)}{(C_0+q_0)^2}
 \le
 \frac{\sqrt{2C_0^2-1}}{C_0+1}
       \frac{C_0+8/5}{C_0+1}
 \le\frac{13\sqrt{79}}{150}<1 .
 \tag{23}
\]
Here \(q_0/(C_0+q_0)^2\) increases on \([0,1]\),
the first factor increases with \(C_0\), and the second is
at most \(13/10\). Using \(C_0<8/7\) gives the last bound;
its square is \(13351/22500<1\).
The formulas extend to \(K=0\), and the empty interior cut
at \(\beta=0\) creates no additional obligation. All starting
zeros and cut intersections are retained.

## 5. The original saddle and logarithmic charge

Write
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0.
 \tag{24}
\]
The unchanged incoming estimates give
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20,\quad\Im A>0 .
 \tag{25}
\]
For \(c=\cos\beta\) and \(C_0=\cosh K\), direct half-angle
identities give
\[
 \Re B>37/60,\quad |B|<25/24,\quad
 |1-B|=\frac{C_0-c}{2}<17/40,\quad\Im B\ge0,
 \tag{26}
\]
and
\[
 \Re(1/B)=\frac{2(1+cC_0)}{(C_0+c)^2}>
                         \frac{24}{25}.
 \tag{27}
\]
For (27), the derivative in \(c\) has the sign of
\(C_0^2-C_0c-2<0\). Its minimum on \(c\in[7/30,1]\)
is therefore at \(c=1\), where it is
\(2/(C_0+1)>24/25\). This replaces, rather than assumes,
the old inequality \(\Re(1/B)\ge1\).

Consequently
\[
 \Re D_0\ge1-|1-A||1-B|>\frac{443}{800},\qquad
 \Re(1/W)=\Re(1/A)+\Re(1/B)-1>\frac{93}{800},\qquad
 \Im(1/W)<0 .
 \tag{28}
\]
For the second inequality use \(\Re(1/A)>5/32\).
All these bounds are uniform on the compact family (1).
The strict imaginary sign comes from \(\Im A>0,\Im B\ge0\).
It follows that \(W\) stays in a compact subset of the upper
right quadrant. Therefore
\[
 y_*=\pi^{-1}\arctan\sqrt W
 \tag{29}
\]
has a fixed positive distance from the boundary of the upper
half-strip. The principal choices in (29) are unchanged.
The exact force factorization is
\[
 e^{F_y}-1
   =-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
               \qquad z_y=\tan(\pi y).
 \tag{30}
\]
The root \(z_y^2=-1\) is at infinite wire height.
Equation (29) is the unique finite algebraic upper root.

For every independent \(u\) in (1), start at \(a=\pi/2\)
and the original critical height \(H_*(u)\). This lies in
the original positive-horizontal source family on all of
\(\mathcal U_+\), which contains the outgoing rectangle.
Its original edge phase has zero wire charge.
First vary \(H\) to any desired value in \([1/10,1]\) at
\(a=\pi/2\), and then vary \(a\) to its desired value.
All bounds above hold along these parameter paths.
The force is one at the saddle, whereas (4)--(5) are
strictly below one on every original cut. Thus the saddle
crosses no original cut or numerator zero. Its continuous
logarithmic derivative takes values in \(2\pi i\mathbb Z\)
and stays zero. On the original closed primitive of
[the positive phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
this proves
\[
 F_y(y_*;t,u)=0,\qquad F(y_*;t,u)=\psi(t,u),\qquad
 -F_{yy}(y_*;t,u)=
           \frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0 .
 \tag{31}
\]
No argument is reset on the new region \(K>\beta/2\).

## 6. What still requires a source proof

The lemma supplies strict original cut descent and a simple
zero-charge wire root on (1). To obtain an upper finite-kernel
envelope one must still retain the bottom and side profiles,
the component argument, exact reciprocal-factorial interpolation,
both alias contours, the midpoint caps and every endpoint row.
At \(K=0,\beta>0\), the outgoing cut lies on the bottom; its
horizontal descent in (5) is available, not a blanket negative
normal-derivative assertion.

The later low first-angle horizontal
\(2\pi/3<a\le\arccos(-13/20)\) is outside (1). Its previously
proved cut estimates used stronger outgoing bounds and are not
extended by this note. Nor is a comparison of the resulting
edge envelope with the full inner action proved here.
The outer attached signed observation remains a separate task.

## Frozen source bindings

- Original force, incoming coordinate analysis and phase guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Original outgoing-cut inequality and reciprocal-factorial branches:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Original complete vertical source and exact charge continuation:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Original independent positive-horizontal source:
  2ec3d95d28876b2fb3c6129303b698c8f190f02fafe8b70023465b66b635be7e.
- Original positive phase and unchanged primitive:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
