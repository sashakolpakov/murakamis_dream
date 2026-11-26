# Decreasing upper terminal regions of the shortened edge

Private source lemma, 8 November 2026. On the actual positive
outer family, the original upper factorial envelope decreases
horizontally throughout the last wire third, and along either
numerator-zero cut. The incoming angular depth is larger than
the outgoing depth. Consequently the wire half-boundary up to
the height of the outgoing zero is below the selected action.

No starting action bound is assigned to either numerator zero
or to the \(1/3\) face. Connecting the known saddle contour to
these decreasing regions remains a separate task.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Actual parameters, source and elementary guards

Use the actual branch of
[the cubic continuation theorem](research_mixed_next_inner_three_cubic_continuation.md)
on
\[
 u=b-iK,\quad0\le b\le\pi/2,\quad0\le K\le1/2,
 \qquad t=t(u)=a-iH,\quad0<a<\pi/2,\quad0<H<1.
 \tag{1}
\]
Put \(v_0=2\cos(t/2)=X+iB\) and \(A=\cos^2(t/2)\).
The already proved cubic guards include
\[
 X>3/2,\qquad1/3<B<2/3,\qquad
 \Re A>1/2,\qquad|A|<127/144 .
 \tag{2}
\]
Both \(\cos t\) and \(\cos u\) have nonnegative real and
imaginary parts, and those for \(t\) are strictly positive.
Their moduli satisfy
\[
 |\cos t|^2=|2A-1|^2
   <4(127/144)^2-1=\frac{43780}{20736}<\frac94,
 \qquad |\cos u|\le\cosh(1/2)<\frac87 .
 \tag{3}
\]
The last strict inequality also covers real or purely imaginary
outer parameters by the same upper bound.

Keep the canonical product \(T_N(y;t,u)=B_N(y,t)B_N(y,u)\)
and its exact sidewise real upper exponent
\(\mathfrak F=\mathfrak b(y,t)+\mathfrak b(y,u)\), as in
[the joined-contour theorem, equations (2)--(5)](research_mixed_next_shortened_edge_joined_contour.md).
Every reciprocal-factorial reflection term is retained.
On compact wire regions its uniform estimate is
\[
             |T_N(y;t,u)|\le C N^A e^{N\mathfrak F(y;t,u)} .
 \tag{4}
\]
Only an upper bound is used through a numerator zero or cut.

Away from those zeros, at fixed wire height \(\sigma\), the
horizontal derivative of the same upper envelope is
\[
 \partial_x\mathfrak F(x+i\sigma;t,u)
  =\log\left|
      \frac{(\cos(2\pi(x+i\sigma))+\cos t)
            (\cos(2\pi(x+i\sigma))+\cos u)}
           {(1-\cos(2\pi(x+i\sigma)))^2}\right|.
 \tag{5}
\]
This is the modulus of the original force. Changing the
sidewise logarithmic lift changes only the imaginary part
of this derivative. Its real integral remains valid across
the isolated zeros by continuity of the original logarithmic
primitive.

## 2. All upper heights to the right of \(1/3\)

For \(1/3\le x<1/2\), \(\sigma\ge0\), write
\[
 q_0=-\cos(2\pi x)\in[1/2,1),\qquad
 C=\cosh(2\pi\sigma)\ge1 .
 \tag{6}
\]
The wire cosine \(Z_y=\cos(2\pi(x+i\sigma))\) has
nonpositive real and imaginary parts. The angular cosines
have the opposite signs. Therefore their cross terms in
\(|Z_y+\cos z|^2\) are nonpositive. Also
\[
 |Z_y|^2=C^2+q_0^2-1,\qquad
 |1-Z_y|^2=(C+q_0)^2 .
 \tag{7}
\]
Equations (3),(7) imply that the squared modulus of the
full force in (5) is less than
\[
 \frac{(C^2+q_0^2+5/4)(C^2+q_0^2+15/49)}
                         {(C+q_0)^4}<1 .
 \tag{8}
\]
For the second inequality, the denominator minus numerator is
exactly
\[
 \left(4Cq_0-\frac{305}{196}\right)(C^2+q_0^2)
                  +4C^2q_0^2-\frac{75}{196}.
 \tag{9}
\]
Its nonconstant terms increase in \(C\ge1,\ q_0\ge1/2\);
the first coefficient is at least \(87/196>0\).
At \(C=1,q_0=1/2\), (9) equals \(919/784>0\).
This proves (8) without an evaluation of the selected root.

Hence the original sidewise upper envelope is strictly
decreasing in \(x\) on \([1/3,1/2]\), at every fixed
nonnegative wire height. The statement includes the limiting
half face and any intervening factorial zero by continuity.
On a fixed bounded height range there is a uniform force
gap below one. No action bound at the initial \(1/3\) face
is inferred.

## 3. Both numerator-zero horizontal cuts

Let \(z=\theta-iA_0\) be either \(t\) or \(u\). Its original
upper numerator zero is
\[
 y_z=\frac12-\frac{z}{2\pi}
          =x_z+\frac{iA_0}{2\pi},
 \qquad x_z=\frac12-\frac{\theta}{2\pi}.
 \tag{10}
\]
Consider the horizontal cut to its right:
\[
 y=x+\frac{iA_0}{2\pi},\qquad x_z\le x\le1/2 .
 \tag{11}
\]
It lies in the right wire half \(x\ge1/4\).
Set \(\phi=\pi-2\pi x\), so \(0\le\phi\le\theta\le\pi/2\),
and \(C=\cosh A_0\), \(S=\sinh A_0\).
Then
\[
 Z_y=-C\cos\phi-iS\sin\phi,\qquad
 \cos z=C\cos\theta+iS\sin\theta,\qquad
 |1-Z_y|=C+\cos\phi .
 \tag{12}
\]
The modulus of this leg's numerator is
\[
 |Z_y+\cos z|
 =2\sin((\theta-\phi)/2)
           \sqrt{\sin^2((\theta+\phi)/2)+S^2}.
 \tag{13}
\]
For fixed \(\phi\), both factors increase with
\(\phi\le\theta\le\pi/2\). At \(\theta=\pi/2\) their
squared product is
\[
 \cos^2\phi+2S^2(1-\sin\phi)
       \le\cos^2\phi(1+2S^2).
 \tag{14}
\]
Together with (12), this proves the exact uniform bound
\[
 \frac{|Z_y+\cos z|}{|1-Z_y|}
       \le\frac{\sqrt{2C^2-1}}{C+1}.
 \tag{15}
\]
For the other angular parameter \(z'\), the opposite-quadrant
signs give
\[
 |Z_y+\cos z'|^2\le|Z_y|^2+|\cos z'|^2,\qquad
 |1-Z_y|^2\ge1+|Z_y|^2,
 \tag{16}
\]
so its leg is at most \(\max(1,|\cos z'|)\).

On the \(u\) cut, \(C<8/7\); the function
\((2C^2-1)/(C+1)^2\) is increasing for \(C\ge1\).
Equations (3),(15),(16) bound the full force by
\[
       \frac32\frac{\sqrt{79}}{15}
              =\frac{\sqrt{79}}{10}<\frac9{10}.
 \tag{17}
\]
On the \(t\) cut, \(C<8/5\). One elementary witness for
this last bound is
\[
 \cosh1
 \le1+\frac12+\frac{1/24}{1-1/30}
 =\frac{179}{116}<\frac85 .
 \tag{18}
\]
Its full squared force is consequently less than
\[
 \frac{103}{169}\frac{64}{49}
       =\frac{6592}{8281}<\frac{81}{100},
 \tag{19}
\]
where the last rational comparison is \(659200<670761\).
Thus the full force is less than \(9/10\) on either cut.
For \(\theta=0\), that cut consists only of its half endpoint,
so no nonempty horizontal interval is asserted.

Equation (5) and continuity now show that on each nonempty
cut (11) the actual upper rate decreases, quantitatively:
\[
 \mathfrak F(x_2+iA_0/(2\pi);t,u)
 -\mathfrak F(x_1+iA_0/(2\pi);t,u)
 \le (x_2-x_1)\log(9/10),
 \quad x_z\le x_1<x_2\le1/2 .
 \tag{20}
\]
The initial zero and every later exact reciprocal-factorial
zero are retained. This is a statement about their common
continuous upper rate. It does not delete a reflection term
or assign a gap to the action at \(y_z\).

## 4. Ordered angular heights and a paid upper half-boundary

The positive outer half has
\(\Im\cos(u/2)\ge0\). The imaginary part of the original
cubic relation, with \(v_0=X+iB\), is
\[
 2\Im\cos(u/2)
      =(3B-2)X^2-B^3+2B^2-3B+2 .
 \tag{21}
\]
If \(1/3<B\le1/2\), its right side is increasing in \(B\):
its derivative is
\[
 3X^2-3B^2+4B-3
       >\frac{27}{4}-\frac34+\frac43-3>0.
 \tag{22}
\]
At \(B=1/2\) the right side of (21) is
\(7/8-X^2/2<-1/4\), a contradiction.
Hence
\[
                  \Im v_0=B>1/2 .
 \tag{23}
\]
Since
\[
 B=2\sin(a/2)\sinh(H/2),\qquad 0<a<\pi/2,
 \tag{24}
\]
one must have \(H>1/2\).
Indeed if \(H\le1/2\), then
\[
 B<\sqrt2\,\sinh(1/4)
   <\frac32\,\frac14\cosh(1/4)
   <\frac32\,\frac14\,\frac87
    =\frac37<\frac12 .
 \tag{25}
\]
This uses \(\sinh s<s\cosh s\) for \(s>0\).
The actual height ordering is therefore
\[
                            H>1/2\ge K .
 \tag{26}
\]

Here is the exact upper half-boundary rate. For one leg
\(z=\theta-iA_0\), put \(r_0=\theta/(2\pi)\), \(s_0=A_0/(2\pi)\),
and let \(L(r,\sigma)=\Re J_{\rm side}(r+i\sigma)\).
The original reflection identities give
\[
 L(r,-\sigma)=L(r,\sigma),\qquad
 L(-r,\sigma)=-L(r,\sigma)-\pi\sigma
                  \quad(r\ge0,\ \sigma\ge0).
 \tag{27}
\]
Also \(\Re J(1/2+i\sigma)=0\).
Consequently the original zero-safe upper rate at
\(y=1/2+i\sigma\) is exactly
\[
 \mathfrak b(1/2+i\sigma,z)
 =-L(r_0,s_0+\sigma)+L(r_0,|s_0-\sigma|)
                                  +\pi|s_0-\sigma| .
 \tag{28}
\]
This formula keeps the absolute value supplied by both
reciprocal reflection terms.

For \(0<\sigma<s_0\), differentiating (28) gives
\[
 \partial_\sigma\mathfrak b
 =\Arg\sin\pi(r_0+i(s_0+\sigma))
  +\Arg\sin\pi(r_0+i(s_0-\sigma))-\pi\le0 .
 \tag{29}
\]
For \(r_0>0\), both arguments are less than \(\pi/2\),
so the inequality is strict. For \(r_0=0\), the limiting
arguments give the nonstrict inequality. Continuity includes
both ends of the interval and the possible zero at \(\sigma=s_0\).
At \(\sigma=0\), the rate is \(A_0/2\).

By (26), both legs therefore decrease throughout
\(0\le\sigma\le K/(2\pi)\), and
\[
 \boxed{\quad
 \mathfrak F(1/2+i\sigma;t,u)\le\frac{H+K}{2}
      <\Re\psi(t,u)-\frac1{25},
 \qquad0\le\sigma\le K/(2\pi).
 \quad} \tag{30}
\]
The second inequality is the adopted
[endpoint action theorem](research_mixed_next_shortened_edge_endpoint_gap.md).
It uses the original calibrated action, not an independent
bound for its derivative or modulus.

The sidewise integrated logarithms are jointly continuous on
the compact set in (30), including all zero-height and
zero-argument endpoints. Thus there is a fixed \(\epsilon>0\)
such that
\[
 \mathfrak F(x+i\sigma;t,u)
       <\Re\psi(t,u)-\frac3{100},
 \qquad
 1/2-\epsilon\le x\le1/2,\quad
                0\le\sigma\le K/(2\pi).
 \tag{31}
\]
For the literal canonical source inside the wire half-strip,
(4) gives the corresponding pointwise finite bound with a
fixed polynomial prefactor, at both parities. In particular
bounded-length paths inside this region and at fixed positive
distance from wire height zero can be used with the exact
upper Fourier denominator. No bound for that denominator at
its real physical poles is inferred from (31).

## 5. What this supplies to a continued upper contour

The last wire third and both numerator-zero cuts are now
regions of strict horizontal decrease for the unchanged
upper factorial envelope. In addition, the right endpoint
at the height of the \(u\)-zero can be connected down toward
the real endpoint through the paid region (31), with the
original small external cap retained as needed.

These facts do not prove that the descending branch from
the selected saddle reaches either region below its action.
In particular the initial \(1/3\) profile and the two
numerator-zero actions remain uncalibrated here.
No omitted physical rows, canonical aliases, internal
joins, or outer normal derivatives are assigned a new
bound by such a starting-value assumption.
The remaining upper continuation in
[the complete lower-current reduction](research_mixed_next_shortened_edge_lower_continuation.md)
is still explicit. No full shortened-edge packet, complete
inner trace, outer signed-observation estimate, parameter
jets, or transfer noncancellation is asserted.
