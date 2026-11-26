# Factorial maxima during the boundary-height displacement

Research deduction, 6 November 2026. The factorial branch admits
stronger coordinate bounds on the positive part of the first-boundary
height displacement. Existing coordinate bounds also give an upper
bound for the direct height-curvature term throughout the displacement,
including its negative part. These do not bound the response of all the other
maximizing coordinates, or the complete finite quantum source.

## 1. The original optimization problem

Use the four-variable phase \(\mathcal F(e,s,z,b)\) and the
fixed outgoing affine subtraction from the
[height-envelope note](research_mixed_selected_boundary_height_envelope.md).
This is the first selected type-four coordinate of a mixed word of
length at least three, with an adjoining ordinary block.
The adjacent block has type \(3+\epsilon\), where
\(\epsilon\in\{0,1\}\). The first coordinate has height
\(k=\Im z\). The coordinate improvement in Section 2 assumes

\[
                         0\le k\le7/500.
 \tag{1}
\]

All other heights are their unchanged actual reference values.
Maximizing the factorial rate \(\Re\mathcal F-2\pi k\)
over the real variables gives the same horizontal maximizers as
\(\Re\mathcal F\). The subtraction in the outgoing \(b\)
coordinate does not alter the \(z\) derivative.

The already proved bounds give, at every such maximizer,

\[
 .3<\Re e<.4,\qquad .2<\Re s\le.5,
 \qquad .22\le x:=\Re z\le.45.
 \tag{2}
\]

Set \(E=e^{-2\pi i e}\), \(S_0=e^{-2\pi i s}\),
\(Z=e^{-2\pi i z}\), and \(R=|Z|=e^{2\pi k}\ge1\).
The actual private and ordinary heights imply

\[
 |E|<9/10,\qquad
 |S_0|^{-1}<
 \begin{cases}8/5,&\epsilon=0,\\19/10,&\epsilon=1.
 \end{cases}
 \tag{3}
\]

The rational witnesses for (3) are given in Section 8 of the
height-envelope note; its sharper ordinary heights, rather than
the height interval for an attached leg, are used here.

## 2. Stronger upper bounds on the first real coordinate

**Proposition 1.** Every factorial-branch horizontal maximizer
at a height in (1) satisfies

\[
 x<\begin{cases}1/3,&\epsilon=0,\\7/20,&\epsilon=1.
 \end{cases}
 \tag{4}
\]

*Proof.* The original derivative, including its chirp, is

\[
 \exp(\partial_x\Re\mathcal F)
   =\frac{|1-EZ|\,|1-S_0Z|}{|S_0|\,|1-Z|^3}.
 \tag{5}
\]

The triangle inequality and (3) bound its numerator by
\((1+9R/10)(R+8/5)\) or
\((1+9R/10)(R+19/10)\), respectively. At \(x=1/3\),
\(|1-Z|^2=1+R+R^2\). At \(x=7/20\),

\[
 |1-Z|^2=1+2\sin(\pi/5)R+R^2
                       >1+\tfrac76R+R^2,
 \tag{6}
\]

using \(\sin(\pi/5)>7/12\), proved by the elementary
cubic sine bound in the
[private-cap estimate](research_mixed_private_cap_curvature_bound.md).

Both squared derivative bounds are strictly below one. This is
verified for the entire range \(R\ge1\) by writing \(u=R-1\):

\[
\begin{split}
 &(1+R+R^2)^3-(1+\tfrac9{10}R)^2(\tfrac85+R)^2\\
 &\quad=u^6+9u^5+\tfrac{3519}{100}u^4
 +\tfrac{9171}{125}u^3+\tfrac{101413}{1250}u^2
 +\tfrac{24443}{625}u+\tfrac{6491}{2500}>0,\\[2mm]
 &(1+\tfrac76R+R^2)^3
                    -(1+\tfrac9{10}R)^2(\tfrac{19}{10}+R)^2\\
 &\quad=u^6+\tfrac{19}{2}u^5+\tfrac{2908}{75}u^4
 +\tfrac{2262689}{27000}u^3+\tfrac{8558021}{90000}u^2
 +\tfrac{1025183}{22500}u+\tfrac{376523}{270000}>0.
\end{split}
 \tag{7}
\]

Fix the other coordinates at a hypothetical maximum above its
claimed bound. Throughout the horizontal interval from that bound
to this maximum, (2) makes the real parts of \(e+z,s+z\)
lie strictly between one half and one, while \(x<1/2\).
Thus

\[
 \partial_x^2\Re\mathcal F
 =\pi\Re\{\cot\pi(e+z)+\cot\pi(s+z)-3\cot\pi z\}<0.
 \tag{8}
\]

The derivative is negative at the proposed cut by (5)--(7), and
remains negative above it by (8). A small decrease of \(x\)
would improve the objective, contradicting maximality. This argument
also excludes a maximum exactly on the cut. \(\square\)

## 3. The direct height curvature is less than five pi

Use the notation

\[
 a_0=\Re\{3\cot\pi z-\cot\pi(e+z)-\cot\pi(s+z)\}
 \tag{9}
\]

from the height-envelope Schur formula. The direct second derivative
with respect to \(k\), before accounting for motion of the real
maximizing point, is \(\pi a_0\).

**Proposition 2.** At every factorial maximizer throughout the original
height interval \(c\le k\le7/500\), for either adjacent type,

\[
                           0<a_0<299/60<5.
 \tag{10}
\]

*Proof.* Positivity follows from the positive real Hessian already
proved on the smaller box. The existing whole-interval restrictions
give \(.3<\Re e<.4\), \(.2<\Re s\le.5\), and
\(x<3/8\) for next type three, or \(x<.39\) and
\(\Re s<.44\) for next type four. These restrictions are
proved before the present estimate in Sections 8 and 12 of the
height-envelope note and in its cited optimizer bounds.
For the upper bound, the cotangent formula implies

\[
 a_0\le F(x):=3\cot\pi x+\tan\pi x+\tan\pi(x-1/10).
 \tag{11}
\]

Indeed \(\Re\cot\pi z\le\cot\pi x\) for \(x<1/2\).
By (2), \(1/2<\Re(e+z)<.4+x\); for a real part between
one half and one, adding an imaginary part decreases the absolute
value of the negative real cotangent. Therefore
\(-\Re\cot\pi(e+z)\le-\cot\pi(.4+x)
=\tan\pi(x-.1)\). If \(\Re(s+z)\le1/2\), its negative
real cotangent is nonpositive and is already bounded by
\(\tan\pi x\). Otherwise the same argument and
\(\Re s\le1/2\) give
\(-\Re\cot\pi(s+z)\le\tan\pi x\).

The function \(F\) is strictly convex on \([.22,3/8]\):
each of its three summands has strictly positive second derivative
there. For next type three it suffices to bound its two endpoint
values. At \(x=.22\),

\[
 \cot(.22\pi)<5/4,\quad \tan(.22\pi)<5/6,
 \quad \tan(.12\pi)<2/5,
 \qquad F(.22)<299/60.
 \tag{12}
\]

At \(x=3/8\),

\[
 F(3/8)=4\sqrt2-2+\tan(11\pi/40)
       <\frac{40}{7}-2+\frac65=\frac{172}{35}<\frac{299}{60}.
 \tag{13}
\]

For explicit rational witnesses, write
\(s_-(y)=y-y^3/6\),
\(s_+(y)=y-y^3/6+y^5/120\),
\(c_-(y)=1-y^2/2\),
\(c_+(y)=1-y^2/2+y^4/24\), and
\(c_6(y)=1-y^2/2+y^4/24-y^6/720\).
Taylor's inequalities for sine and cosine on the present interval,
monotonicity of tangent, and \(25/8<\pi<22/7\) reduce (12)--(13)
to the following positive rational differences:

\[
\begin{array}{rcl}
 s_-(11/16)-\tfrac45c_+(11/16)&=&29407/1966080,\\
 \tfrac56c_6(121/175)-s_+(121/175)
   &=&106520168419769/24816585937500000,\\
 \tfrac25c_-(66/175)-s_+(66/175)
   &=&2697331976/820654296875,\\
 \tfrac65c_6(121/140)-s_+(121/140)
   &=&27571084410193/1505907200000000.
\end{array}
 \tag{14}
\]

All cosine denominators are positive, and \(\sqrt2<10/7\)
follows by squaring. These verify every strict endpoint inequality
used for next type three.

For next type four, the stronger restriction \(\Re s<.44\)
instead gives

\[
 a_0\le F_4(x)=3\cot\pi x+\tan\pi(x-.1)+\tan\pi(x-.06).
 \tag{15}
\]

To justify the last term, if \(\Re(s+z)\le1/2\) its
negative real cotangent is nonpositive; otherwise use
\(\Re(s+z)<.44+x\) as before. This function is strictly
convex on \([.22,.39]\). At its lower endpoint,
\(F_4(.22)<F(.22)<299/60\). At its upper endpoint,
\(\tan(.11\pi)<\tan(.12\pi)<2/5\), while
\(\tan(.29\pi),\tan(.33\pi)<\sqrt3<7/4\). Thus
\(F_4(.39)<3(2/5)+2(7/4)=47/10<299/60\).
Convexity proves (10) for both types on the whole height interval.
\(\square\)

## 4. What this estimate leaves to prove

In normalized notation the effective curvature is
\(\mathcal K=a_0+(Cv)^TA^{-1}(Cv)\), where \(A\) is the
negative real Hessian divided by pi and \(C\) its corresponding
imaginary matrix. Proposition 2 bounds only the first summand.
It does not imply \(\mathcal K\le6\). The response term
still depends on the coupled stationary equations and the prescribed
outgoing tangent. The stronger coordinate bounds in Proposition 1
are restricted to positive heights, whereas Proposition 2 uses the
earlier coordinate bounds to cover the whole displacement. Neither
Fourier alternative's entire finite source is bounded by these
coordinate estimates alone.
