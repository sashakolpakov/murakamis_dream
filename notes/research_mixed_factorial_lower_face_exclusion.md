# Excluding the original lower first-coordinate face

Research deduction, 6 November 2026. In the actual first-four,
next-three factorial height problem, the original face
\(\Re z=.22\) cannot contain a horizontal maximizer at any height
of the reset. The proof uses original phase derivatives and exact
univariate polynomial signs. It makes no numerical root or source
evaluation.

## 1. Original problem and necessary signs

Use the phase \(\mathcal F(e,s,z,b)\), the unchanged actual private
and ordinary heights, and the fixed outgoing affine subtraction in
the [height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The word has \(m\ge3\); the first vertex has type four and the next
vertex is an ordinary type-three vertex. The changing first height
and the proved whole-path restrictions are
\[
 \begin{gathered}
 c\le k=\Im z\le7/500,\qquad c>-7/100,\\
 .3<\Re e<.4,\quad -.051<\Im e<-.019,\\
 .2<\Re s\le.5,\quad .22\le\Re b\le.45,\qquad
 -.065<\Im s,\Im b<.068,\\
 .22\le\Re z<3/8 .
 \end{gathered}
 \tag{1}
\]
These are consequences of maximization on the original box.
In particular the lower \(z\) face in this note is an original
face, not an auxiliary coordinate restriction.

Write \(D_s=\Re\mathcal F_s\), \(D_z=\Re\mathcal F_z\).
At a hypothetical maximum on \(\Re z=.22\),
\[
                         D_s\ge0,\qquad D_z\le0.
 \tag{2}
\]
A small decrease of \(\Re s\) is allowed by (1), and a small
increase of \(\Re z\) is allowed. The outgoing affine term
depends only on \(b_R\), and the factorial correction
\(-2\pi k\) is constant during these variations.

Set
\[
 E=e^{-2\pi ie},\quad S=e^{-2\pi is},\quad
 Z=e^{-2\pi iz},\quad B=e^{-2\pi ib},\quad
 R=|Z|,\quad r=|S|,\quad r_b=|B|.
 \tag{3}
\]
The exact original derivatives, including \(2\pi izs\), give
\[
 e^{2D_s}=\frac{|1-SZ|^2|1-SB|^2}{R^2|1-S|^4},
 \qquad
 e^{2D_z}=\frac{|1-EZ|^2\,|1-SZ|^2/r^2}{|1-Z|^6}.
 \tag{4}
\]
The factors \(R^{-2}\) and \(r^{-2}\) are retained throughout.
No private or ordinary critical equation is replaced by an
exponentiated root choice.

**Theorem.** Every factorial maximizer in (1) satisfies
\[
                              \Re z>.22 .
 \tag{5}
\]

## 2. Elementary constants

The following strict bounds will be used:
\[
 \begin{gathered}
 |E|>29/40>18/25,\qquad
 13/20<r<307/200<31/20,\qquad r_b<307/200<31/20,\\
 16/25<R<11/10,\qquad
 \gamma:=\cos(.44\pi)=\sin(.06\pi)>187/1000,\\
 \cos(.24\pi)>91/125>18/25,\qquad
 \sin(.12\pi)>9/25,\quad
 \sin(.12\pi)<3/8,\quad \cos(.06\pi)>49/50 .
 \end{gathered}
 \tag{6}
\]
Here are rational witnesses, to specify all constants explicitly.
For \(0<x<3\),
\[
                 e^x\le1+x+\frac{x^2}{2(1-x/3)}.
 \tag{7}
\]
At \(x=9/28\) its right side is
\(1931/1400<40/29\), with difference \(1/40600\).
Since \(.102\pi<9/28\), this proves the bound for \(|E|\).
At \(x=107/250\) the right side is
\(493449/321500<307/200\), and
\(.136\pi<107/250\); this proves both ordinary upper-radius bounds.
At \(x=41/100\) it is less than \(20/13\), and
\(.13\pi<.41\), proving the lower bound for \(r\).
At \(x=11/25\) it equals \(4971/3200<25/16\);
\(.14\pi<.44\) then gives \(R>16/25\).
Finally \(.028\pi<11/125\), and (7) at \(11/125\)
is less than \(11/10\).

For the trigonometric bounds, put
\(s_-(x)=x-x^3/6\),
\(s_+(x)=x-x^3/6+x^5/120\), and
\(c_6(x)=1-x^2/2+x^4/24-x^6/720\).
Use \(157/50<\pi<22/7\) and the sine/cosine Taylor bounds:
\[
 \begin{array}{rcl}
 s_-(471/2500)-187/1000
   &=&8920963/31250000000,\\
 c_6(132/175)-91/125
   &=&108898117354/143614501953125,\\
 s_-(3/8)-9/25&=&159/25600,\\
 3/8-s_+(19/50)&=&152973901/37500000000,\\
 1-\tfrac12(33/175)^2-49/50&=&68/30625.
 \end{array}
 \tag{8}
\]
For the third line, \(.12\pi>3/8\); for the fourth,
\(.12\pi<19/50\). All arguments lie in intervals where
the corresponding sine or cosine is monotone.

## 3. Negative heights: the \(z\) derivative alone excludes the face

Suppose \(\Re z=.22\) and \(k\le0\), so
\(16/25<R\le1\).
The summed real parts satisfy
\[
 .52<\Re(e+z)<.62,\qquad .42<\Re(s+z)\le.72.
 \tag{9}
\]
Consequently
\(\cos(2\pi\Re(e+z))<-\cos(.24\pi)\).
For the second sum, the entire interval in (9) lies in
\([.28,.72]\), on which the cosine is at most
\(-\gamma\). This argument does not assume monotonicity
across the midpoint \(1/2\).

Using (6), define
\[
 \begin{split}
 A_-(R)&=1+2\frac{29}{40}\frac{91}{125}R
                         +\left(\frac{29}{40}\right)^2R^2,\\
 B_-(R)&=\left(\frac{200}{307}\right)^2
                  +\frac{187}{500}\frac{200}{307}R+R^2,\\
 D(R)&=1-\frac{187}{500}R+R^2>0 .
 \end{split}
 \tag{10}
\]
The exact factors in (4) obey
\[
 |1-EZ|^2>A_-(R),\qquad
 |1-SZ|^2/r^2>B_-(R),\qquad
                         |1-Z|^2<D(R).
 \tag{11}
\]
For example the second bound uses \(r^{-1}>200/307\) in
\(r^{-2}+R^2-2Rr^{-1}\cos(2\pi\Re(s+z))\).
Section 5 proves the exact polynomial inequality
\[
                 A_-(R)B_-(R)-D(R)^3>0
                       \quad(16/25\le R\le1).
 \tag{12}
\]
Thus (4) gives \(D_z>0\), contradicting (2). This excludes
the original lower face at every nonpositive height.

## 4. Positive heights: the two KKT signs are incompatible

Now \(k\ge0\), so \(1\le R<11/10\).
First evaluate \(D_s\) at \(\Re s=.47\), still with
\(\Re z=.22\), and hold the other coordinates fixed.
The angle bounds in (6) imply
\[
 \cos(2\pi\Re(s+z))>-3/8,\quad
 \cos(2\pi\Re(s+b))>-3/8,\quad
                         \cos(2\pi\Re s)<-49/50.
 \tag{13}
\]
The second assertion follows from \(\Re(s+b)\in[.69,.92]\).
Writing \(q=R^{-1}\le1\), equation (4) is bounded by
\[
 e^{2D_s}
 <\frac{(r^2+3r/4+1)(1+961r^2/400+93r/80)}
          {(1+r^2+49r/25)^2}<1
                 \quad(13/20\le r\le31/20).
 \tag{14}
\]
To verify the last strict inequality, its denominator minus
numerator is
\[
 r\,Q(r),\qquad
 Q(r)=-\frac{561}{400}r^3+\frac{1529}{1600}r^2
                         +\frac{62689}{40000}r+\frac{803}{400}.
 \tag{15}
\]
The cubic is strictly concave on this interval, and
\[
 Q(13/20)=2435829/800000>0,\qquad
 Q(31/20)=483153/320000>0.
 \tag{16}
\]
It is therefore positive throughout.
The already-proved conditional horizontal concavity makes \(D_s\)
decrease above \(\Re s=.47\). Hence a maximizer on the proposed
\(z\) face cannot have \(\Re s\ge.47\), because (2) requires
\(D_s\ge0\).

It remains to consider \(.2<\Re s<.47\).
Now \(\Re(s+z)\in(.42,.69)\), a subset of \([.31,.69]\);
its cosine is less than \(-\sin(.12\pi)<-9/25\).
Using coarser consequences of (6), put
\[
 A_+(R)=1+\frac{648}{625}R+\frac{324}{625}R^2,\qquad
 B_+(R)=\frac{400}{961}+\frac{72}{155}R+R^2 .
 \tag{17}
\]
The factors of (4) now satisfy
\[
 |1-EZ|^2>A_+(R),\qquad
 |1-SZ|^2/r^2>B_+(R),\qquad |1-Z|^2<D(R).
 \tag{18}
\]
Section 5 proves
\[
                  A_+(R)B_+(R)-D(R)^3>0
                             \quad(1\le R\le11/10).
 \tag{19}
\]
Equation (4) again gives \(D_z>0\), contradicting (2).
This proves (5) also at positive heights.

## 5. Exact polynomial certificates

For completeness, here are rational coefficient identities proving
both remaining univariate signs. Let
\[
 B_i^6(t)=\binom6i t^i(1-t)^{6-i},\qquad 0\le t\le1 .
 \tag{20}
\]
These seven nonnegative weights sum to one. For each sign define
\(P_\pm=A_\pm B_\pm-D^3\). The exact identities are
\[
 \begin{split}
 P_-\left(\frac{16}{25}+\frac9{25}t\right)
      &=\frac1{d_-}\sum_{i=0}^6n_{-,i}B_i^6(t),\\
 P_+\left(1+\frac1{10}t\right)
      &=\frac1{d_+}\sum_{i=0}^6n_{+,i}B_i^6(t),
 \end{split}
 \tag{21}
\]
where
\[
 \begin{gathered}
 d_-=3681601562500000000,\\
 (n_{-,0},\ldots,n_{-,6})=
 (991321801464503040,\ 1183469555166378720,\
 1313735427630808368,\ 1342820138521002837,\\
 \hspace{34mm}
 1208966929648843200,\ 817877224702668750,\
 24612243725625000),\\
 d_+=7207500000000000,\\
 (n_{+,0},\ldots,n_{+,6})=
 (3652386424980000,\ 3328100106229000,\
 2945251148587960,\ 2497781290377129,\\
 \hspace{34mm}
 1979041676411356,\ 1381734261025090,\
 697846003597380).
 \end{gathered}
 \tag{22}
\]
Every numerator and denominator is positive. These are exact
coefficient identities, not sampled values. One way to verify them
is to expand each transformed polynomial as
\(\sum_{j=0}^6p_jt^j\); its \(i\)-th Bernstein coefficient is
\(\sum_{j=0}^ip_j\binom ij/\binom6j\).
Consequently (12) and (19) hold on their entire closed intervals.

The theorem makes the original \(z\) coordinate interior throughout
this factorial path. Thus \(D_z=0\) is now available everywhere,
and the two \(z\)-fixed cases of the
[active-face response table](research_mixed_active_face_curvature_budget.md)
cannot occur in this application. The upper original \(s\) face
and the outgoing \(b\) faces have not been excluded here.
No six-pi curvature bound or full selected finite-source estimate
follows solely from this exclusion.
