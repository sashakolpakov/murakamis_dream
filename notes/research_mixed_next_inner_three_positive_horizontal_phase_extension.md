# The original inner three-phase to the positive far cut

Private phase theorem, 8 November 2026. The original inner phase
has its unique horizontal maximum at the selected critical point,
on the entire positive horizontal below any fixed angle less than
\(\pi\). Quantitative concavity reaches \(2\pi/3\); a separate
return comparison then gives a uniform negative derivative all
the way to the far cut.

This is a statement about the original calibrated phase. It does
not extend either finite edge packet beyond its proved source
domain, or pay a connector to the far real angular interval.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original branches on the enlarged angle box

Fix \(a_F<\pi\), with \(a_F\ge2\pi/3\), and consider
\[
 t=a-iH,\quad u=b-iK,\qquad
 0\le a\le a_F,\quad0\le H\le1,\quad
 0\le b\le\pi/2,\quad0\le K\le1/2 .
\tag{1}
\]
As in [the original horizontal phase theorem](research_mixed_next_inner_three_horizontal_concavity.md), put
\[
 c=\cos(t/2),\quad C=\cos(u/2),\quad
 A=c^2,\quad B=C^2,\quad D=A+B-AB .
\tag{2}
\]
The written elementary bounds \(\cosh1<8/5\) and
\(\cosh(1/2)<8/7\) from that source give
\[
 |1-A|=\frac{\cosh H-\cos a}{2}<\frac{13}{10},
 \qquad |1-B|<\frac47,\qquad
 |1-D|<\frac{26}{35}.
\tag{3}
\]
Thus \(D\) stays in the right half-plane. Both \(c\) and \(C\)
have positive real parts and nonnegative imaginary parts.

The principal-return cuts can be checked directly, without
extrapolating the old smaller-box argument estimates. For
\(0<a<\pi\),
\[
 T=\tan(t/2)
   =\frac{\sin a-i\sinh H}{\cosh H+\cos a}
\tag{4}
\]
has positive real part and nonpositive imaginary part.
Consequently \(CT\) has positive real part. Likewise
\(c\tan(u/2)\) has positive real part when \(b>0\).
At \(a=0\), a return with zero real part has modulus at most
\[
 |C|\tanh(H/2)<(8/7)(1/2)=4/7<1.
\]
At \(b=0\), the analogous exceptional return has modulus at most
\[
 |c|\tanh(K/2)<(8/7)(1/4)=2/7<1.
\]
Here \(|c|,|C|<8/7\) follows from
\(|\cos((a-iH)/2)|\le\cosh(H/2)\).
These boundary returns avoid the two principal
\(\operatorname{arsinh}\) cuts as well.

The functions
\[
 c\sqrt{1+C^2\tan^2(t/2)},\qquad
 C\sqrt{1+c^2\tan^2(u/2)}
\tag{5}
\]
have square \(D\), are nonzero and agree with the principal
\(\sqrt D\) at \((t,u)=(0,0)\). Connectedness and (3)
identify both with that root throughout (1). Therefore the
holomorphic one-form
\[
 d\psi=-\frac1\pi\{
   \operatorname{arsinh}(C\tan(t/2))\,dt+
   \operatorname{arsinh}(c\tan(u/2))\,du\},
 \qquad \psi(0,0)=-8J(1/4)
\tag{6}
\]
is closed: the two return cross derivatives are
\(-\sin(t/2)\sin(u/2)/(2\sqrt D)\).
The compact box has a convex complex neighborhood retaining
these guards, so (6) has a holomorphic primitive there.
It agrees with the original edge phase on the old box by its
derivatives and complete constant.

Keep exactly the original charge-one inner phase
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)
                       +\frac{3it^2}{4\pi}-it .
\tag{7}
\]
In particular neither a logarithmic charge nor an additive
constant is changed by this continuation.

## 2. Quantitative concavity through \(2\pi/3\)

When \(0\le a\le2\pi/3\), the sharper bounds are
\[
 |1-A|<21/20,\qquad |1-D|<3/5,\qquad
 |\arg\sqrt D|<\pi/8 .
\tag{8}
\]
For the last assertion, the disk of radius \(3/5\) centered at
one lies in \(|\arg D|<\pi/4\), because
\((3/5)^2<1/2=\sin^2(\pi/4)\).
Also
\[
 0\le\arg c<\pi/4,\qquad0\le\arg C<\pi/12 .
\tag{9}
\]
Indeed,
\(\tan(a/2)\tanh(H/2)<\sqrt3/2<1\), while
\(\tan(b/2)\tanh(K/2)<1/4<2-\sqrt3\).
Thus
\[
 -3\pi/8<\arg\frac{C}{c\sqrt D}<5\pi/24 .
\tag{10}
\]
The original derivative, with the root identified in (5), is
\[
 \Phi_{tt}
    =-\frac1{2\pi}\left(\frac1c+\frac{C}{c\sqrt D}\right)
                                  +\frac{3i}{2\pi}.
\tag{11}
\]
The second ratio has positive real part by (10). Since
\(|c|<8/7\), (9) also gives
\(\Re(1/c)>7/(8\sqrt2)>1/2\).
Consequently
\[
 \boxed{\quad
 \Re\Phi_{tt}(a-iH,u)<-\frac1{4\pi},
                  \qquad0\le a\le2\pi/3 .
 \quad}
\tag{12}
\]

## 3. Two monotonicity facts for the original returns

For \(0<a<\pi\), \(H>0\), fix \(T\) from (4), and let
\(C_0=x+iy\), \(x>0,\ y\ge0\). Then
\[
 Z=T^{-2}+C_0^2,\qquad \Im Z>0,\qquad
 \frac{T}{\sqrt{1+C_0^2T^2}}=\frac1{\sqrt Z}.
\tag{13}
\]
The identity includes the signs: \(T\sqrt Z\) has argument
strictly between \(-\pi/2\) and \(\pi/2\), and hence is the
principal root of \(1+C_0^2T^2\). Its square is that quantity.
It follows that
\[
 \partial_x\Re\operatorname{arsinh}(C_0T)
       =\Re(1/\sqrt Z)>0,\qquad
 \partial_y\Re\operatorname{arsinh}(C_0T)
       =-\Im(1/\sqrt Z)>0 .
\tag{14}
\]
The nonstrict limiting statements hold at \(H=0\).
For the actual \(C=\cos(u/2)\), one has
\(\Re C\ge1/\sqrt2\), \(\Im C\ge0\). Integrating (14)
along the two straight coordinate segments therefore proves
\[
 \Re\operatorname{arsinh}(CT)
    \ge\Re\operatorname{arsinh}(T/\sqrt2).
\tag{15}
\]

The second fact concerns a real multiplier
\(\gamma\in[1/\sqrt2,1]\). Its return increases strictly with
\(a\in(0,\pi)\) at every fixed \(0\le H\le1\).
To see the branch and sign explicitly, put
\[
 D_\gamma=\gamma^2+(1-\gamma^2)A .
\]
At \(H>0\), \(\Im A>0\), \(\Re A>-3/10\), and
\(\Re D_\gamma>0\). Moreover
\[
 \Im(A D_\gamma)
  =\Im A\{\gamma^2+2(1-\gamma^2)\Re A\}>0,
\tag{16}
\]
because the bracket is greater than or equal to
\[
 \gamma^2-\tfrac35(1-\gamma^2)
       =\tfrac85\gamma^2-\tfrac35\ge\tfrac15 .
\]
Now \(c\sqrt{D_\gamma}\) has argument in \((0,3\pi/4)\),
and its square has positive imaginary part by (16).
Its argument must therefore lie in \((0,\pi/2)\).
The same principal-return calculation as (5) gives
\[
 \partial_a\Re\operatorname{arsinh}(\gamma T)
          =\Re\frac{\gamma}{2c\sqrt{D_\gamma}}>0 .
\tag{17}
\]
At \(H=0\), every quantity in the last ratio is positive real.
This also covers the first return by taking \(\gamma=1\).

## 4. A uniform return bound at \(2\pi/3\)

At \(a=2\pi/3\), writing \(C_H=\cosh H<8/5\),
formula (4) gives the exact inequalities
\[
 |T|^2=\frac{C_H+1/2}{C_H-1/2}>\frac{21}{11},
 \qquad
 (\Re T)^2=\frac{3}{4(C_H-1/2)^2}>\frac{75}{121}.
\tag{18}
\]
For a complex \(z\) with positive real part, its principal
return satisfies
\[
 \sinh^2(\Re\operatorname{arsinh}z)
  =\frac{|z|^2-1+
       \sqrt{(|z|^2-1)^2+4(\Re z)^2}}2 .
\tag{19}
\]
This follows by writing \(z=\sinh(r+i\theta)\) with \(r>0\)
and solving the resulting quadratic for \(\sinh^2r\).
The right side increases in both \(|z|^2-1\) and
\((\Re z)^2\). Applying (18) first to \(z=T\), and then
to \(z=T/\sqrt2\), yields
\[
 \sinh^2(\Re\operatorname{arsinh}T)>\frac{15}{11},
 \qquad
 \sinh^2(\Re\operatorname{arsinh}(T/\sqrt2))
                           >\frac{\sqrt{601}-1}{44}.
\tag{20}
\]

All needed comparisons are exact series inequalities.
For \(0<r<\sqrt6\), successive terms of the positive
series for \(\sinh r\) have ratio at most \(r^2/6\),
and at least one ratio is smaller. Hence
\[
 \sinh r<\frac{r}{1-r^2/6}.
\]
In particular
\[
 \sinh(19/20)<\frac{2280}{2039}<\frac76,\qquad
 \sinh(3/5)<\frac{30}{47}<\frac23.
\tag{21}
\]
The squared bounds needed in (20) are
\[
 \frac{49}{36}<\frac{15}{11},\qquad
 \frac49<\frac5{11}
                  <\frac{\sqrt{601}-1}{44},
\tag{22}
\]
where the last strict inequality follows from
\(601>21^2\). Thus, at \(a=2\pi/3\),
\[
 \Re\operatorname{arsinh}T>\frac{19}{20},\qquad
 \Re\operatorname{arsinh}(T/\sqrt2)>\frac35 .
\tag{23}
\]
By (15),(17), for every \(2\pi/3\le a<\pi\) and every
parameter in (1),
\[
 \Re\{\operatorname{arsinh}T+\operatorname{arsinh}(CT)\}
                                      >\frac{31}{20}.
\tag{24}
\]
The charge in (7) gives
\[
 \partial_a\Re\Phi(a-iH,u)
   =-\frac1\pi\Re\{\operatorname{arsinh}T+
                         \operatorname{arsinh}(CT)\}
                                       +\frac{3H}{2\pi}.
\]
Since \(H\le1\), (24) proves
\[
 \boxed{\quad
 \partial_a\Re\Phi(a-iH,u)<-\frac1{20\pi},
                         \qquad2\pi/3\le a<\pi .
 \quad}
\tag{25}
\]
No global second-derivative sign beyond \(2\pi/3\) is used.

## 5. The full actual positive horizontal

Let \(t_*(u)=a_*(u)-iH_*(u)\) be the selected original
critical family from
[cubic continuation](research_mixed_next_inner_three_cubic_continuation.md),
and set \(s(u)=\Re S_3(0,u)\).
Its strict compact guards give \(0<a_*<\pi/2\) and
\(0<H_*<1\). Integrating (12) from its zero derivative
at \(a_*\), then (25), proves
\[
 \Re\Phi(a-iH_*,u)\le
 \begin{cases}
 s(u)-(a-a_*)^2/(8\pi),&0\le a\le2\pi/3,\\[2mm]
 s(u)-(2\pi/3-a_*)^2/(8\pi)
                 -(a-2\pi/3)/(20\pi),&2\pi/3\le a\le a_F .
 \end{cases}
\tag{26}
\]
The selected point is the unique maximum on the entire
positive horizontal. The phase increases before \(a_*\)
and decreases after it.

For example, let
\[
 a_{\max}=\max_{\mathcal U_+}a_*(u),\qquad
 a_R=\tfrac12(\pi/2+a_{\max}),\qquad
 \epsilon_R=\frac{(a_R-a_{\max})^2}{8\pi}>0 .
\tag{27}
\]
Then every fixed \(a_F\in[2\pi/3,\pi)\) satisfies
\[
 \Re\Phi(a-iH_*,u)\le s(u)-\epsilon_R,
                           \qquad a_R\le a\le a_F ,
\tag{28}
\]
uniformly on the actual outer family. In particular the
original far cut \(a_F=\pi-\pi/2000\) lies in this phase
domain.

The [complete positive-horizontal shortened-edge packet](research_mixed_next_shortened_edge_positive_horizontal_packet.md)
currently supplies the needed finite source through
\(a=\pi/2\). Equations (26)--(28) alone do not supply
that packet farther right, do not bound the full first edge
there, and do not justify a vertical drop to the real far
endpoint. Those finite-source and connecting-current
obligations remain separate.
