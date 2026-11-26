# Paid regular transport on the remaining plateau-neighbor strip

Research deduction, 7 November 2026. The coupled regular transport
for a type-three first cap extends to neighbor real coordinates
\(.22\le z\le.28\), with derivative greater than \(1/200\).
Together with [the upper-neighbor theorem](research_mixed_first_three_regular_coupled_transport.md),
this pays the regular central/cut envelope on the entire early
first-minimum taper whenever \(z\ge.22\).

Both neighboring incidences, the original coefficient-radius
relations and both following regular branches are retained.
No source evaluation or new contour is used. Interior high physical
rows, neighbors below \(.22\), the following whole finite source
and the calibrated compensated boundary remain separate.

## 1. Source and a stronger low-neighbor height credit

Keep all source assumptions and the exact \(H_0,B,T\) of equations
(1)--(3), (10) of the upper-neighbor theorem. Here restrict
\[
 .22\le z\le.28,\qquad .1\le x\le.22,\quad d=x-.1,\qquad
 -7/40\le\lambda_a\le3/5,\quad0\le\lambda_b\le17/20.
 \tag{1}
\]
Thus \(a=x-i\lambda_a d\), \(b=z-i\lambda_b d\).
The following regular index retains
\(w\in[.22,.49]\), \(\zeta\in[-.108,.068]\).
It must independently be source-eligible. The adjoining real
maximizer is in \((.22,1/3)\), and is in \((.22,.3)\) if
\(\lambda_b\ge\max(\lambda_a,0)\), exactly as proved there.

On this strip the original neighbor force has the stronger bound
\[
 -\partial_h B(v,t;z,h)>\frac{17\pi}{10},
 \qquad .22\le v\le1/3,\quad -.102\le h\le0.
 \tag{2}
\]
Indeed its exact derivative divided by \(-\pi\) is
\[
 3\Re\cot\pi(z+ih)-\Re\cot\pi(v+z+ih)
                         -\Re\cot\pi(t+z+ih).
 \tag{3}
\]
Each shifted cotangent is less than \(1/5\): its real part is at
least \(.44\), and a real part above \(1/2\) only improves the
upper bound. The own cotangent exceeds \(7/10\).
For a fully rational witness, use
\[
 \cosh(.204\pi)<607/500,\quad
 \sin(.06\pi)<33/175,\quad
 \cos(.06\pi)>1-\frac12(33/175)^2.
 \tag{4}
\]
The exact cotangent quotient is therefore greater than
\[
 \frac{1-(33/175)^2/2}{607/500+33/175}>\frac7{10}.
 \tag{5}
\]
For the hyperbolic bound, \((.204\pi)^2<103/250\) and
\(\cosh t\le1+t^2/[2(1-t^2/12)]\) give
\(1+618/2897<607/500\). The other two estimates are the elementary
sine and cosine Taylor inequalities. Equations (3)--(5) prove (2).

Integrating (2) with the same actual \(\lambda_b\) gives the lower
support for the exact coupled derivative
\[
 H_0(e,v;x,\lambda_a)-\pi\lambda_b v
       +\lambda_bT(z,t)+\frac{17\pi}{10}\lambda_b^2d.
 \tag{6}
\]
At height zero the identity \(B(v,t;z,0)=-\pi v+T(z,t)\) is
unchanged. The \(v\)-dependence in (6) therefore still has the
old endpoint-minimum form, now with coefficient \(\lambda_b\)
itself. Use \(v=.22,.3\) in the first coefficient case, and
\(v=.22,1/3\) when \(0\le\lambda_b<\lambda_a\).
The original private endpoint reduction gives \(e=.27,.49\).
The added height credit is independent of either private index.

## 2. Retaining both following branches

The [exact following-index reduction](research_mixed_first_attached_following_index_elimination.md)
shows that the minimum of \(T\) is among its two previously
specified branches. For the branch \(w=.49\), \(w+z>1/2\),
so its original all-radius argument inequality gives \(T\ge0\).
For \(w=.22\), the minimizing height is \(\zeta=-.108\)
when \(z<.28\). Put \(r=e^{-.216\pi}\). On this branch
\[
 T(z)=\pi(-.56+2z)+
             \arg(1-r e^{-2\pi i(.22+z)}).
 \tag{7}
\]
It is strictly increasing in \(z\), because its derivative is
\[
 \frac{2\pi\{1-r\cos(2\pi(.22+z))\}}
             {1-2r\cos(2\pi(.22+z))+r^2}>0.
 \tag{8}
\]
At \(z=.22\) the argument in (7) is greater than \(\pi/25\).
The following rational witnesses suffice:
\[
 r>507/1000,\quad
 \sin(.12\pi)>1839/5000,\quad \cos(.12\pi)<93/100.
 \tag{9}
\]
Thus the tangent of that argument exceeds
\[
 \frac{932373}{7357550}>\frac{19}{150},
 \qquad
 \arctan(19/150)>
 \frac{1275641}{10125000}>\frac{22}{175}>\frac\pi{25}.
 \tag{10}
\]
The arctangent inequality is its first two alternating terms.
For the first witness in (9), \(.216\pi<679/1000\), and
the positive exponential series bounded after degree four gives
\[
 \begin{split}
 e^{679/1000}
 &\le1+\frac{679}{1000}
  +\frac{(679/1000)^2}{2}
  +\frac{(679/1000)^3}{6}
  +\frac{(679/1000)^4}{24}
  +\frac{(679/1000)^5}{120(1-(679/1000)/6)}\\
 &<1+\frac{679}{1000}
       +\frac{230521+52175+8857+1357}{10^6}
 <\frac{493}{250}<\frac{1000}{507}.
 \end{split}
 \tag{11}
\]
The remaining witnesses follow from the sine lower polynomial
and cosine upper polynomial at \(3(157/50)/25=471/1250\);
the sine is increasing and cosine decreasing on the present
interval. Direct rational comparison gives respectively
\(t-t^3/6>1839/5000\) and
\(1-t^2/2+t^4/24<93/100\).
Consequently both following branches satisfy
\[
                              T(z,t)>-\frac{2\pi}{25}.
 \tag{12}
\]
No following height has been discarded.

## 3. A global first-coordinate support for \(e=.49\)

The exact original-branch factorization from the upper-neighbor
proof holds at every \(x\) in (1), with
\[
 q_a=\tanh(\pi\lambda_a d),\quad
 C=\cot\pi x,\quad C_e=\cot\pi(.49+x),\quad
 C_v=\cot\pi(v+x),
 \tag{13}
\]
and
\[
 P_v(x)=\log\frac{\sin\pi(.49+x)\sin\pi(v+x)}{\sin^2\pi x}.
 \tag{14}
\]
Its constant imaginary part is still \(\pi(v-.49)\).
The logarithmic term is bounded below by \(-C^2q_a^2\).

The function \(d\cot\pi x\) is increasing on this interval.
Its derivative has the sign of
\(\sin(2\pi x)-2\pi(x-.1)\), which is decreasing in \(x\)
and is positive at \(.22\), using
\(\sin(.44\pi)>49/50\) and \(.24\pi<132/175\).
The inherited endpoint cotangent bound hence gives
\[
 C^2q_a^2\le\frac{213444}{10^6}\lambda_a^2,\qquad
 |q_aC|<3/10,\quad |q_aC_e|<1/5,\quad |q_aC_v|<1/5.
 \tag{15}
\]
Here \(|C_e|<4/5\), and \(|C_v|<4/5\):
the largest positive value is below \(\cot(.3\pi)<4/5\),
and the possible negative value has modulus less than \(1/5\).
Also \(|q_a|<1/4\).

For \(q_a>0\), the arctangent brace in the factorization is
at least \(q_aK_v(x)\), where
\[
 K_v(x)=\frac{97}{50}C+\frac{49}{50}(-C_e)
          -C_v+\frac1{50}\min(C_v,0).
 \tag{16}
\]
This uses \(\arctan t\ge t-t^3/3\): the first pair loses
at most \(3/100\) of its linear term, and either other
positive arctangent loses at most \(1/50\).
Oddness gives the same inequality after multiplication by
\(\lambda_a\) when \(q_a<0\).

The continuous piecewise-smooth function \(K_v\) decreases
with \(x\). Indeed both shifted sines exceed \(3/4\), whereas
\(\sin\pi x<16/25\); differentiation of (16) reduces to
\[
 \frac{99}{50}(64/75)^2<\frac{97}{50}.
 \tag{17}
\]
The same argument with unit coefficients shows that
\(2C-C_e-C_v\) decreases. At \(.22\) it is greater than
\(297/100\), uniformly over the three endpoint values of \(v\).
Therefore
\[
 P_v(x)>P_v^{\rm lower}+9(.22-x),
 \tag{18}
\]
where the constant floors \(P_v^{\rm lower}\) are those already
proved in the upper-neighbor theorem.
The three endpoint lower bounds for (16) are
\[
 \begin{array}{c|c|c}
 v&P_v^{\rm lower}&k_v\le K_v(x)\\ \hline
 .22&16/25&23/8\\
 .3&131/200&157/50\\
 1/3&16/25&647/200 .
 \end{array}
 \tag{19}
\]
They follow directly from
\(C>6/5\), \(-C_e>77/100\), and the three cotangent
bounds in the earlier proof.

Finally
\[
 \lambda_aq_a\ge\frac{7379}{2400}d\lambda_a^2
 \tag{20}
\]
by \(\tanh t\ge t-t^3/3\), \(|t|<1/4\), and
\(\pi>157/50\). Combining (14)--(20) gives
\[
 \begin{split}
 H_0(.49,v;x,\lambda_a)>
 P_v^{\rm lower}+9(.12-d)
 +\pi\lambda_a(v-.49)
 +\left(\frac{7379k_v}{2400}d
                     -\frac{213444}{10^6}\right)\lambda_a^2.
 \end{split}
 \tag{21}
\]

Add the neighbor terms from (6), replacing \(T\) only by (12).
This lower expression is affine in \(d\), with derivative
\[
 -9+\frac{7379k_v}{2400}\lambda_a^2
                       +\frac{17\pi}{10}\lambda_b^2<0.
 \tag{22}
\]
For example, \(k_v<13/4\), \(7379/2400<22/7\),
\(\lambda_a^2\le9/25\), and \(\lambda_b^2\le289/400\)
bound the two positive terms by a sum less than eight.
Thus its minimum occurs at \(d=.12\). This is a new
proved first-coordinate comparison for this stronger support,
not an application of the old affine-credit monotonicity.
At this endpoint the three quadratic coefficients in (21)
are greater than \(21/25,47/50,49/50\), respectively.

## 4. The other private endpoint has its own support

For \(e=.27\), replace \(C_e\) in (13) by
\(\cot\pi(.27+x)\). This is positive, and both shifted
cotangents are less than \(C\). Hence the arctangent brace,
after multiplication by \(\lambda_a\), is nonnegative for
every sign of \(\lambda_a\). Bound it below by zero.
The same logarithmic loss (15) remains valid.

Put
\[
 P_v^{27}(x)=
       \log\frac{\sin\pi(.27+x)\sin\pi(v+x)}{\sin^2\pi x}.
 \tag{23}
\]
The quantity \(2C-\cot\pi(.27+x)-C_v\) decreases with \(x\):
each shifted sine is at least the own sine, with strictness.
At the final endpoint it exceeds
\(12/5-1/30-1/5=13/6\). Thus
\[
 P_v^{27}(x)>\frac{87}{100}+6(.22-x).
 \tag{24}
\]
For the constant, \(\cos(.01\pi)>999/1000\),
\(\sin\pi(v+.22)>49/50\), and
\(\sin(.22\pi)<319/500\) make the ratio greater than \(12/5\).
The explicit logarithm witness is
\[
 \log(12/5)>
 2\left(\frac7{17}+\frac{(7/17)^3}{3}\right)
       =\frac{12824}{14739}>\frac{87}{100}.
 \tag{25}
\]
For all three values of \(v\), the linear term satisfies
\(\pi\lambda_a(v-.27)>-1/10\), and the logarithmic loss
is greater than \(-2/25\), since
\((213444/10^6)(9/25)<2/25\).
Consequently
\[
                  H_0(.27,v;x,\lambda_a)>
                       \frac{69}{100}+6(.12-d).
 \tag{26}
\]
After adding (6) and (12), this lower support also decreases
in \(d\), because
\(-6+(17\pi/10)\lambda_b^2<0\).
At \(d=.12\), uniformly even for \(v=1/3\), the neighbor
negative magnitude is less than \(13/20\):
\[
 \pi\left\{\frac{31}{75}\frac{17}{20}
       -\frac{51}{250}\left(\frac{17}{20}\right)^2\right\}
                              <\frac{13}{20}.
 \tag{27}
\]
The quadratic decreases on the whole coefficient interval,
so its displayed endpoint is the worst case. Equations
(26)--(27) pay this private endpoint with margin \(1/25\).

## 5. Final payment and exact finite-envelope scope

It remains to pay the three \(e=.49\) lower supports at
\(d=.12\). Their first quadratics are the same paid ones
in the upper-neighbor theorem: their minima at
\(v=.22,.3\) exceed \(21/50,14/25\), respectively.

At \(v=.22\), the most negative neighbor quadratic is
\[
 -\pi\frac{(.22+.08)^2}{4(51/250)}
       =-\frac{15\pi}{136}>-\frac7{20}.
 \tag{28}
\]
At \(v=.3\), it decreases through \(\lambda_b\le17/20\),
and its negative magnitude at that endpoint is
\[
                  \frac{17561\pi}{100000}<\frac{111}{200}.
 \tag{29}
\]
The first combined margin is greater than \(7/100\);
the second is greater than \(1/200\).

The endpoint \(v=1/3\) is needed only when
\(0\le\lambda_b<\lambda_a\le3/5\).
The neighbor quadratic decreases up to \(\lambda_b=\lambda_a\),
so substitution of that value gives the lower bound
\[
 \frac{16}{25}-\frac{57\pi}{100}\lambda_a
            +\left(\frac{49}{50}+\frac{51\pi}{250}\right)
                                                     \lambda_a^2
 >
 \frac{16}{25}-\frac95\lambda_a+\frac85\lambda_a^2
 \ge\frac{107}{800}>\frac1{200}.
 \tag{30}
\]
Equations (6), (12), (21)--(30), and the unchanged endpoint
reductions prove the claimed coupled slope \(>1/200\).

The real cap maximum and the real ordinary maximum can be
integrated by their original envelope theorem, as in the
upper-neighbor deduction. Following regular profiles may be
maximized only over their unchanged independently valid domain.
The original real cuts and paid aliases remain bounded by
the chosen real-main envelope at each target; no finite cut
has been moved, and no physical high row has been dropped.

Combining this theorem with the previously reviewed
\(z\ge.28\) estimate gives the uniform regular-envelope
slope \(>1/200\) for every \(z\ge.22\).
The actual cap marginal, both allocations at the moving neighbor,
the protected cut and relative-pinning fee are unchanged.
No calibrated plateau value is substituted for this envelope.
The cases \(z<.22\), first own type four, interior high physical
profiles, following complete-source eligibility and the final
compensated sign remain outside the conclusion.
