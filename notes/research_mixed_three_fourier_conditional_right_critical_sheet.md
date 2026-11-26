# A second original zero-mode critical point on negative incoming heights

Research deduction, 7 November 2026. On the nonpositive-height half
of the actual type-three containing rectangle, the other conditional
root is a genuine critical point of the original full-period zero
mode. Its incoming shifted factorial is below a positive wall and
its outgoing shifted factorial is above that wall. Keeping those two
different branches gives logarithmic lift zero.

This critical point is a horizontal minimum and a vertical maximum.
It therefore cannot be excluded as a nonstationary or purely alias
root when analyzing the remaining homogeneous period. No claim is
made that its descending contour occurs with nonzero coefficient in
that period, or that its action dominates. No numerical evaluation
is used.

## 1. Root geometry and two additional elementary bounds

Fix \(y=x_0=\xi+i\upsilon\), and let
\[
 a=x+ih,\qquad
 \frac{267}{1000}\le x\le\frac{433}{1000},\qquad
                    -\frac9{125}\le h\le0 .
 \tag{1}
\]
Use the original cotangents and selected left root
\[
 P=p+i\alpha,\quad Q=q-ib,\quad S_1=u-iv .
\]
The [actual-input theorem](research_mixed_three_conditional_actual_input_subdomain.md),
[left zero-mode theorem](research_mixed_three_fourier_conditional_left_zero_mode.md),
and [action-height deduction](research_mixed_three_fourier_conditional_action_height.md)
give
\[
 \begin{gathered}
 0<p<9/10,\quad 0\le\alpha<387/1000,\quad q>127/100,\\
 17/25<b<73/100,\qquad u,v>0,\quad |S_1|<1 .
 \end{gathered}
 \tag{2}
\]
Both roots solve
\[
             S^2+(P+Q)S-1+i(Q-P)=0 .
 \tag{3}
\]
In particular
\[
 S_2=-P-Q-S_1=-(p+q+u)+i(b-\alpha+v).
 \tag{4}
\]
Its original inverse cotangent \(s_2\) is chosen with
\(1/2<\Re s_2<1\). Equation (4) gives
\[
             3/4<\Re s_2<1,\qquad \Im s_2<0,
 \tag{5}
\]
because \(b-\alpha>293/1000\) and \(|S_2|>q>1\).

We will also use
\[
                         p>9/50,\qquad q<13/10 .
 \tag{6}
\]
Here are explicit witnesses. For the output, the actual-input proof
gives \(0<2\pi\xi<719/625<29/25\) and
\(\cosh(2\pi\upsilon)-\cos(2\pi\xi)>14201/20000\).
The alternating sine upper polynomial satisfies
\[
 \frac{29}{25}-\frac{(29/25)^3}{6}
          +\frac{(29/25)^5}{120}<\frac{23}{25};
\]
after multiplication by \(1171875000\), the left side minus
the right side has numerator \(-3101351\).
The polynomial is increasing on this interval. Hence
\[
                       q<\frac{18400}{14201}<\frac{13}{10}.
 \tag{7}
\]
For the incoming cotangent, the smallest numerator is
\(\sin(67\pi/500)\). Since \(\pi>3\),
\[
 \sin(67\pi/500)>
       \frac{201}{500}-\frac{(201/500)^3}{6}>\frac{39}{100}.
 \tag{8}
\]
The difference in the last inequality has numerator \(879399\)
over denominator \(750000000\). Also
\(2\pi|h|<396/875<23/50\), and the positive cosh series gives
\[
 \cosh(2\pi h)
 \le1+\frac{(23/50)^2}{2[1-(23/50)^2/12]}
 =1+\frac{3174}{29471}<\frac{111}{100}.
 \tag{9}
\]
Thus \(p>(39/100)/(211/100)=39/211>9/50\).

## 2. The two shifted factors are on different sides of their walls

The root identity is
\[
                 (P+S_1)(Q+S_1)=(P-i)(Q+i).
 \tag{10}
\]
Cotangent addition and (4) imply
\[
 \begin{split}
 \cot\pi(s_2+y)
   &=Q+\frac{Q^2+1}{P+S_1}
     =Q+\frac{(Q-i)(Q+S_1)}{P-i}
     =i\,\frac{S_1+2Q-i}{S_1+i},\\
 \cot\pi(s_2+a)
   &=P+\frac{P^2+1}{Q+S_1}
     =-i\,\frac{S_1+2P+i}{S_1-i}.
 \end{split}
 \tag{11}
\]
All denominators are nonzero by (2).

First, \(\Re\cot\pi(s_2+y)>q>0\). Indeed put
\(C=1-\alpha>613/1000\).
The real numerator of the middle fraction in (11), after
multiplication by \(p+iC\), is
\[
 p\{q(q+u)-(b+1)(b+v)\}
       +C\{q(b+v)+(b+1)(q+u)\}.
 \tag{12}
\]
Its first term is greater than \(-621/500\); its second is
greater than \((613/1000)(127/100)(59/25)\).
Their sum is greater than \(1488209/2500000>0\).
Since \(\Re(s_2+y)\in(.933,1.183)\), its positive cotangent
real part forces \(\Re(s_2+y)>1\). Equation (5) already gives
\(\Re(s_2+a)>1.017\). Both real shifted arguments are below \(3/2\).

We next prove \(\Im(s_2+y)>0\). The imaginary part of (3) at
\(S_1=u-iv\) gives
\[
 v=\frac{q-p-(b-\alpha)u}{2u+p+q}.
 \tag{13}
\]
In fact \(u<9/20\). Otherwise (2), (6), and (13) give
\[
 v<
 \frac{28/25-(293/1000)(9/20)}{2(9/20)+9/50+13/10}
       =\frac{19763}{47600}<\frac{21}{50}.
 \tag{14}
\]
The bound follows by increasing \(q\) and decreasing \(p\) and
\(b-\alpha\) in (13); the resulting fraction decreases with \(u\).
The real part of (3) would then satisfy
\[
 \begin{split}
 0&=u^2-v^2+(p+q)u+b(1-v)+\alpha(1+v)-1\\
 &>\frac{81}{400}-\frac{441}{2500}
       +\frac{261}{400}+\frac{493}{1250}-1
   =\frac{73}{1000}>0,
 \end{split}
 \tag{15}
\]
a contradiction.

For \(0\le u\le9/20\), the same monotonicities in (13) give
\[
 v<V(u):=\frac{28/25-(293/1000)u}{37/25+2u}.
 \tag{16}
\]
The imaginary part of the last expression for \(\cot\pi(s_2+y)\)
in (11) has positive denominator \(|S_1+i|^2\) and numerator
\[
                    u^2+v^2+2qu+2bv-1-2b .
 \tag{17}
\]
Because \(v<1\), increasing \(b\) decreases (17). Thus (17)
is strictly less than
\[
       D(u)=u^2+V(u)^2+\frac{13}{5}u
                               +\frac{34}{25}V(u)-\frac{59}{25}.
 \tag{18}
\]
Here \(V>0\), \(V'<0\), \(V''>0\), so
\[
            D''=2+2(V')^2+(2V+34/25)V''>0.
 \tag{19}
\]
At the two endpoints, \(V(0)=28/37<19/25\) and
\(V(9/20)<21/50\), giving
\[
          D(0)<-\frac{468}{625},\qquad
          D(9/20)<-\frac{2399}{10000}.
 \tag{20}
\]
Convexity proves negativity throughout. Hence
\(\Im\cot\pi(s_2+y)<0\), as required.
The incoming shifted height is negative directly from (1), (5).
We have proved
\[
 \boxed{\quad
 \begin{gathered}
 1<\Re(s_2+a),\Re(s_2+y)<3/2,\\
 \Im s_2<0,\qquad \Im(s_2+a)<0<\Im(s_2+y).
 \end{gathered}
 \quad}
 \tag{21}
\]
All inequalities are strict on the compact family (1), so they
persist on a fixed parameter neighborhood of that family.

## 3. The actual full-period zero-mode lift

The global factorial phases satisfy
\[
 g_-(z+1)=g_-(z),\qquad
 g_+(z+1)=g_+(z)-2\pi iz.
 \tag{22}
\]
These are the original
[upper/lower continuation identities](research_mixed_complex_horizontal_obstruction.md),
not freely chosen logarithmic sheets.
In the chart (21), the normalized phase of the literal row
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+y)
                              E_N(a)E_N(y)E_N(s)^2
 \tag{23}
\]
is therefore
\[
 \boxed{\quad
 \mathscr F_2(s)=
   g(s+a-1)+g(s+y-1)-2g(s)-g(a)-g(y)
           +2\pi ias-2\pi i(s+y-1).
 \quad}
 \tag{24}
\]
All \(g\)'s displayed in (24) have real argument strictly between
zero and one and use the original regular-strip branch.

The twice-periodized phase obtained by omitting the last term
in (24) has exponentiated derivative one at \(s_2\), by (3).
Its derivative has imaginary part strictly between zero and
\((4-2\xi)\pi<4\pi\): both shifted arguments in (24) have real
part below \(1/2\), the own argument has real part above \(3/4\),
and the original strip argument bounds apply at every height.
More explicitly the upper bound is
\[
 \pi(3-2\Re s_2-2x)+\pi(3-2\Re s_2-2\xi)
       +2\pi(2\Re s_2-1)+2\pi x=(4-2\xi)\pi.
 \tag{25}
\]
Each term in the imaginary part is positive before this upper
bound is applied. Its exact lift is consequently \(2\pi i\).
The final term in (24) subtracts \(2\pi i\), proving
\[
                         \mathscr F_2'(s_2)=0.
 \tag{26}
\]
Moreover
\[
 \Re\mathscr F_2''(s_2)
  =\pi\Re\{\cot\pi(s_2+a-1)+\cot\pi(s_2+y-1)
                                      -2\cot\pi s_2\}>0.
 \tag{27}
\]
The first two real parts are positive and the last one is
negative, solely from their real-coordinate strips.
This proves nondegeneracy with the vertical Gaussian direction.
The original nonreal factorial packets on (21) have nonzero
symbols; no numerator zero is divided out or substituted away.

## 4. What this adds to the homogeneous-period problem

The [particular-current theorem](research_mixed_three_fourier_conditional_particular_current.md)
fixes the exact homogeneous remainder, including its zero mode
and both signed vertical currents. Equation (26) identifies a
second genuine original zero-mode critical chart on the negative
incoming-height family. It is not a root with a nonzero logarithmic
lift that could be excluded from that analysis.

A sufficiently small symmetric vertical segment through \(s_2\)
has a nonzero Gaussian for the literal row (23), with conditional
power \(N^{-1/2}\) after its outside index density \(N\).
This local statement follows from (27) and the original
\(N^{-1}\) row symbol. It does not identify that segment as a
component of the prescribed homogeneous contour. Its coefficient,
its possible cancellation with other currents, and its action
comparison with the left critical point remain to be proved.

In particular the paid left half-path cannot by itself justify a
whole homogeneous asymptotic by asserting that its right-hand
complement has no original critical point. The exact upper shifted
factor in (24) is the reason that assertion would be false.
