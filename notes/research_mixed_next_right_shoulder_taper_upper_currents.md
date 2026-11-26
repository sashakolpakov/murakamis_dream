# Positive-height currents on the right-shoulder incoming taper

Private research proof, 8 November 2026. The original type-four
conditional source has uniform index curvature on the small-index
part of the incoming taper, at every height above the original
main height. This supplies the missing positive alias and upper
vertical-current estimates on the right shoulder. Every finite
factor and the original cotangent density are retained. No
numerical evaluation is used.

## 1. Original parameters and source

Let \(P=[.22,.45]\), and retain the ordinary-next references and
their heights from the
[unselected first-a left taper](research_mixed_next_unselected_incoming_left_taper.md).
Write \(h_a\in[-9/125,0]\), \(h_s,h_y\in[-51/500,-1/1000]\).
The taper and the shoulder target are
\[
 a=x-i\eta_a,\qquad
 \eta_a=-h_a\,\frac{x-1/10}{3/25},\qquad
 \frac1{10}\le x\le\frac{11}{50},\qquad
 y=q+ih_y,\quad \frac9{20}\le q\le\frac12.
 \tag{1}
\]
In particular
\[
                 0\le\eta_a\le\frac35(x-1/10).
 \tag{2}
\]
Set
\[
 \ell(x,q)=\frac{39}{400}+\frac{x}{8}+\frac9{20}-q.
 \tag{3}
\]
Then \(3/50\le\ell\le1/8\), and
\[
             q+\ell=\frac{219}{400}+\frac{x}{8}.
 \tag{4}
\]
The range proved below is
\[
         \ell(x,q)\le u=\Re s\le\frac3{20},
                         \qquad \sigma=\Im s\ge h_s.
 \tag{5}
\]

Use precisely the original primitive and bare conditional phase
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias.
 \tag{6}
\]
The allocation \(F=Q-g(y)/2\) has the same index derivatives.
The logarithms are the original continuations from the regular
strip; no argument is reset modulo \(2\pi\).
All three varying real parts in (6) satisfy
\[
 0<u<1,\qquad 0<x+u<1,\qquad \frac12<q+u<1.
 \tag{7}
\]
Thus this small-index proof has no numerator-wall crossing.

The exact interpolation is the original
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                           E_N(a)E_N(y)E_N(s)^3.
 \tag{8}
\]
At \(s=j/N\) this is the full physical row
\[
       X^{-j}p_j(X)p_j(Y)/P_j^3,\qquad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy}.
 \tag{9}
\]
The canonical factors and this equality are the ones in the cited
left-taper proof and in
[the complete central shoulder source, Section 6](research_mixed_next_lower_right_shoulder_central_prefix.md).
We estimate (8) itself, not a different off-grid representative.

## 2. The all-height curvature

Put
\[
 C(z)=\Re\cot\pi z
     =\frac{\sin(2\pi\Re z)}
            {\cosh(2\pi\Im z)-\cos(2\pi\Re z)}.
 \tag{10}
\]

**Lemma 1.** On (1)--(5),
\[
       \Re Q_{ss}(s;a,y)
          =\pi\{C(a+s)+C(y+s)-3C(s)\}<0.
 \tag{11}
\]

*Proof.* First suppose \(\ell\le u\le1/8\). Equations (3)--(4)
give
\[
 u\ge3/50,\quad x+u\ge4/25,\quad
             14/25\le q+u\le5/8.
 \tag{12}
\]
Consequently
\[
 \sin2\pi u>11/30,\quad \cos2\pi u>7/10,\quad
 -\sin2\pi(q+u)>11/30,\quad \cos2\pi(x+u)<11/20.
 \tag{13}
\]
For the first and third bounds use
\(\sin(3\pi/25)>\sin(47/125)>
47/125-(47/125)^3/6>11/30\), with \(\pi>157/50\).
For the fourth, \(8\pi/25>1\) and
\(\cos1<1-1/2+1/24=13/24<11/20\).
The cosine bound for the own argument follows from
\(\cos(\pi/4)>7/10\).

For \(h_s\le\sigma\le51/500\),
\(\cosh2\pi\sigma<5/4\). One direct witness is
\(2\pi|\sigma|<13/20\) and
\[
 \cosh z\le1+\frac{z^2/2}{1-z^2/12}<5/4
                         \quad(0\le z\le13/20).
 \tag{14}
\]
The first inequality sums the positive series with all ratios
after its quadratic term bounded by \(z^2/12\).
Now (13) gives \(3C(s)>2\), while
\[
 C(a+s)\le\cot\pi(x+u)<\cot(4\pi/25)<2,\qquad C(y+s)<0.
 \tag{15}
\]
For the strict last comparison use \(4\pi/25>1/2\) and
\(\tan z>z\). Thus (11) holds on this height range.

For \(\sigma\ge51/500\), set \(A=\cosh2\pi\sigma\ge1\).
The exact height correlation gives
\[
 \cosh2\pi(\sigma-\eta_a)\ge e^{-2\pi\eta_a}A,\qquad
                     \cosh2\pi(\sigma+h_y)\le A.
 \tag{16}
\]
The second inequality uses \(0\le\sigma+h_y\le\sigma\).
We divide the taper into three ranges.

If \(x\le3/20\), then \(\eta_a\le3/100\) and
\(e^{-2\pi\eta_a}>33/40\). Indeed
\(\log(40/33)>14/73>(3/50)\pi\).
By (13)--(16),
\[
 3C(s)-C(y+s)>
       \frac{11/10}{A-7/10}+\frac{11/30}{A+1}
       >\frac1{(33/40)A-11/20}>C(a+s).
 \tag{17}
\]
All denominators are positive. After multiplying the middle
comparison by them, its numerator is
\[
 P_1(A)=\frac{21}{100}A^2-\frac{4931}{12000}A
                                      +\frac{1417}{6000}.
 \tag{18}
\]
Here \(P_1(1)=141/4000>0\) and \(P_1'(1)=109/12000>0\);
the derivative increases, so \(P_1(A)>0\) for every \(A\ge1\).

If \(3/20\le x\le1/5\), then \(\eta_a\le3/50\) and
\(e^{-2\pi\eta_a}>2/3\), since
\(\log(3/2)>2/5>(3/25)\pi\).
Also
\[
 u\ge53/800,\quad x+u\ge173/800,\quad
 \sin2\pi u>2/5,\quad -\sin2\pi(q+u)>2/5,\quad
                       \cos2\pi(x+u)<1/4.
 \tag{19}
\]
For the sine bound use \(53\pi/400>33/80\) and
\(33/80-(33/80)^3/6>2/5\).
For the incoming cosine use
\(\cos(173\pi/400)=\sin(27\pi/400)<1/4\).
The resulting sufficient comparison is
\[
 \frac{6/5}{A-7/10}+\frac{2/5}{A+1}
                              >\frac1{(2/3)A-1/4}.
 \tag{20}
\]
Its cleared numerator is
\[
 P_2(A)=A^2/15-13A/150+47/100.
 \tag{21}
\]
It is increasing for \(A\ge1\) and \(P_2(1)=9/20>0\).

Finally, if \(1/5\le x\le11/50\), retain the two sine
bounds in (19), and use \(x+u\ge109/400>1/4\).
Thus the incoming cosine is negative. The bound
\(e^{-2\pi\eta_a}>5/8\) follows from
\(\log(8/5)>6/13>(18/125)\pi\). It suffices that
\[
 \frac{6/5}{A-7/10}+\frac{2/5}{A+1}>
                                     \frac1{(5/8)A}.
 \tag{22}
\]
The cleared numerator is \(11A/40+7/10>0\).
This proves (11) for \(\ell\le u\le1/8\).

For \(1/8\le u\le3/20\), the simpler guards are
\[
 \sin2\pi u>7/10,\quad \cos2\pi u>1/2,\quad
 \cos2\pi(x+u)<1/5,\quad -\sin2\pi(q+u)>9/20.
 \tag{23}
\]
Here \(x+u\ge9/40\), so its cosine is at most
\(\sin(\pi/20)<1/5\); the last bound follows from
\(\sin(3\pi/20)>\sin(15/32)>9/20\).
At the heights in (14), these give \(3C(s)>14/5>C(a+s)\).
At larger heights use (16) and \(e^{-2\pi\eta_a}>5/8\).
The sufficient comparison is
\[
 \frac{21/10}{A-1/2}+\frac{9/20}{A+1}>
                                 \frac1{(5/8)A-1/5}.
 \tag{24}
\]
Its cleared numerator is
\[
                \frac{19}{32}A^2+\frac{259}{1600}A+\frac18>0.
 \tag{25}
\]
This completes the proof. \(\square\)

## 3. Original argument lifts and all small-index currents

The original branch identity is
\[
 \Im Q_s=
 \arg(1-e^{-2\pi i(a+s)})+
 \arg(1-e^{-2\pi i(y+s)})-
 3\arg(1-e^{-2\pi is})+2\pi x.
 \tag{26}
\]
For \(\sigma\le0\), the outgoing argument is negative, the
own argument is nonnegative, and the incoming argument is at
most \(\max\{\pi-2\pi(x+u),0\}\). Hence
\[
        \Im Q_s<\max\{\pi-2\pi u,2\pi x\}<9\pi/10.
 \tag{27}
\]
This bound holds down to the original lower alias height \(-1/5\).
For \(\sigma\ge h_s\), Lemma 1 implies
\(\partial_\sigma\Im Q_s=\Re Q_{ss}<0\). On precisely the same
continued logarithmic branches, its limit is
\[
 \lim_{\sigma\to+\infty}\Im Q_s
              =-\pi-2\pi q+2\pi u\ge-47\pi/25.
 \tag{28}
\]
Thus \(\Im Q_s>-47\pi/25\) at every finite height above \(h_s\).
No Fourier charge is changed in obtaining (28).

Write \(M(u)=\Re Q(u+ih_s;a,y)\). Integration of (27)--(28)
gives the two full horizontal alias comparisons
\[
 \begin{split}
 \Re Q(u-i/5)-2\pi/5
              &<M(u)-11\pi/50,\\
 \Re Q(u+8i)-16\pi
              &<M(u)-9603\pi/12500 .
 \end{split}
 \tag{29}
\]
The upper comparison uses \(-h_s\le51/500\). Both strict
losses are uniform. On a vertical cut, the weighted upper
profile has derivative
\[
        \partial_\sigma\{\Re Q(u+i\sigma)-2\pi\sigma\}
                                         <-3\pi/25,\quad \sigma\ge0.
 \tag{30}
\]
The weighted lower profile decreases as its downward height
increases, by (27). Both weighted vertical pieces are therefore
bounded by their real-cut value. The unweighted join between
\(h_s\) and zero is bounded by its two endpoints: its second
height derivative is \(-\Re Q_{ss}>0\).

These are bounds for the literal original profiles. They remain
valid after any factor independent of \(s\) is attached, including
the coherent cap, either full Fourier-weight alternative, its
allocated halfweight, and the following conditional kernel.
No bound for a signed endpoint sum is substituted for a
current-by-current bound.

## 4. Finite source and scope of the conclusion

Use the original retained rectangle with lower real cut
\(\ell(x,q)\), upper real cut \(1/2\), and alias heights
\(-1/5,8\). This note controls its horizontal portions with
\(u\le3/20\), its entire lower-real-cut weighted sides, and
the unweighted lower-cut join. No vertical side is inserted
at \(u=3/20\); this is a division of an estimate on the existing
horizontal contours.

For the exact physical lower index
\(L_N=\lceil N\ell(x,q)\rceil\), the cut is
\(\ell_N=(L_N-1/2)/N\). It differs from \(\ell\) by at most
\(1/(2N)\). All inequalities above are strict on their fixed
compact contour sets and persist with a smaller reserve under
this displacement. Every argument in (8) remains in a regular
canonical factorial strip. The exact factorial expansions
therefore bound \(|T_N|\) by its original \(Q\) rate with
polynomial cost and arbitrarily small common exponential
tolerance.

The exact half-grid cotangent remainders are bounded by a
polynomial times \(e^{-2\pi N|\sigma|}\); this includes the
real endpoint of a vertical side. Their factors are the
original ones from the finite residue decomposition, whose
main density is \(+N\). Combining them with (29) pays the
entire small-index lower and upper horizontal remainders
against the corresponding main-height profile, with for
example finite losses \(1/2\) and \(2\), respectively.
Equations (30) and (27) pay the weighted vertical pieces by
their real-cut values. The unweighted joining piece is paid
by the maximum of its real and main-height cut values.
All polynomial factors, including \(+N\), are absorbed only
after retaining these fixed strict reserves.

No physical row is removed by this argument. The literal
physical lower and upper rows, the main-height and real-cut
comparisons, and the portions \(u\ge3/20\) must retain their
separate source estimates. In particular this note does not
assert the complete shoulder transfer. Its new conclusion is
the missing uniform positive-height control on the original
small-index currents, including the range
\(1/8\le u\le2/15\) not covered by the old four-case alias bound.

At every fixed base reference, hold the cuts and contours fixed.
All factorial arguments stay in fixed regular neighborhoods;
the finite-height strict bounds persist on smaller outside
neighborhoods. Cauchy's formula supplies every fixed mixed
normalized derivative with polynomial cost. Multiplication
by a whole all-real-color cap preserves its previously proved
ordinary-color derivative bounds. No normal data, level parity,
or original phase factor is discarded.
