# A fixed trial for the remaining upper-input ordinary left cut

Research deduction and bounded certificate protocol, 6 November 2026.
The existing ordinary-label height extension leaves only one label on
the actual typed input domains: the real left cut for an ordinary
type-three incoming reference with height above \(.03\). This note
reduces that entire remaining strip to 128 fixed midpoint comparisons.
Their signs have not been evaluated or asserted. There is no new root,
target optimizer, adaptive refinement or alternative trial.

## 1. Original difference and target domain

Keep the bare own-four phase
\[
 Q(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,
 \qquad g'(w)=\Log(1-e^{-2\pi iw}).
 \tag{1}
\]
Set
\[
 \begin{gathered}
 b=x+ik,\quad a=y+i/100,\quad x,y\in P=[.22,.45],\\
 .03\le k\le17/250=.068,\quad
 -.102\le h\le-.001,\quad s_h=1/4+ih,\quad l=1/8,\\
 \Delta(x,y,k,h)=\Re\{Q(s_h;b,a)-Q(l;b,a)\}.
 \end{gathered}
 \tag{2}
\]
The original main index interval \([1/8,1/2]+ih\) contains \(s_h\).
All other factors, original boundary halfweights and affine subtractions
are independent of this index. Thus a positive lower bound for (2)
removes the left-cut label pointwise with each terminal profile and
each full selected-weight alternative unchanged.

## 2. Four real corners and the highest incoming height

Write \(C(t,q)=\Re\cot\pi(t+iq)\). The real second derivatives of
\(\Delta\) are \(\pi[C(.25+w,h+j)-C(.125+w,j)]\), with
\((w,j)=(x,k)\) or \((y,.01)\). They are strictly negative.

For \(w\le.25\), the first cotangent is at most
\(\cot(.47\pi)=\tan(.03\pi)<1/10\). The second is greater than
\((7/10)/(5/4+1)=14/45\), since its real part is in
\([.345,.375]\), \(\sin(2\pi(.125+w))\ge\sqrt2/2>7/10\),
and \(\cosh(2\pi j)<5/4\).
For \(.25\le w\le.375\), their signs prove the comparison.
For \(w\ge.375\), put \(u=2\pi(.25+w-.5)\in[\pi/4,2\pi/5]\).
Here \(|h+j|\le.092\), so
\[
 C(.25+w,h+j)<-\frac{7/10}{5/4+3/4}=-7/20
 <-1/4<C(.125+w,j).
 \tag{3}
\]
The last inequality uses \(C(.125+w,j)\ge-\tan(.075\pi)>-1/4\).
These elementary bounds follow from
\[
 \tan(.03\pi)<
 \frac{33/350}{1-(33/350)^2/2}<1/10,\qquad
 \tan(.075\pi)<
 \frac{33/140}{1-(33/140)^2/2}<1/4,
 \tag{4}
\]
and \(\cosh z\le1+(z^2/2)/(1-z^2/12)<5/4\) for
\(0\le z\le3/5\). Both \(.184\pi\) and \(.136\pi\) are
less than \(3/5\). Separate concavity therefore reduces the minimum
to \(x,y\in\{.22,.45\}\).

Let \(A(t,q)=\Im g'(t+iq)=\Arg(1-e^{2\pi q-2\pi it})\).
Retaining the original chirp gives
\[
 \Delta_k=-A(.25+x,h+k)+A(.125+x,k)-\pi/4.
 \tag{5}
\]
At \(x=.22\), the first term is negative, while \(A(.345,k)<\pi/4\).
Indeed \(r=e^{2\pi k}<5/3\), and
\[
 r\{\sin(.69\pi)+\cos(.69\pi)\}<\frac56<1.
 \tag{6}
\]
The real and imaginary parts of \(1-re^{-.69\pi i}\) are positive;
(6) says its imaginary part is less than its real part. The radius
bound follows from the existing exact \(e^{.16\pi}<5/3\) witness,
and (6) uses \(\sin(.69\pi)\le1\), \(\cos(.69\pi)<-1/2\).
Consequently (5) is strictly negative.

At \(x=.45\), decreasing the height of a summed argument with real
part \(.70>.5\) increases its argument toward zero. Thus, since \(h<0\),
\[
 -A(.70,h+k)+A(.575,k)
 \le A(.575,k)-A(.70,k)<\pi/4.
 \tag{7}
\]
For the strict last bound, on \(t\in[.575,.70]\) one has
\(\cos(2\pi t)<0\), hence \(|\Im\cot\pi(t+ik)|<1\).
The identity \(A_t=\pi(\Im\cot\pi(t+ik)-1)>-2\pi\)
integrated over length \(1/8\) proves (7).
Again (5) is negative. The whole remaining incoming-height strip is
therefore bounded by its single endpoint \(k=17/250\):
\[
 \Delta(x,y,k,h)\ge
 \min_{\xi,\eta\in\{.22,.45\}}d_{\xi,\eta}(h),\qquad
 d_{\xi,\eta}(h)=\Delta(\xi,\eta,17/250,h).
 \tag{8}
\]

## 3. A uniform height correction

Only the main trial depends on \(h\), so
\[
 d'=-A(.25+\xi,h+.068)-A(.25+\eta,h+.01)
                         +3A(.25,h)-2\pi\xi .
 \tag{9}
\]
The original argument bounds give
\[
 -\pi\max(.5-2w,0)\le-A(.25+w,q)
                  \le\pi\max(2w-.5,0).
 \tag{10}
\]
Also \(A(.25,h)=\arctan(e^{2\pi h})\), with
\(1/2<e^{2\pi h}<1\). The lower radius bound follows from
\(.204\pi<2/3<\log2\). Hence
\[
                 11/8<3A(.25,h)<3\pi/4,
 \tag{11}
\]
where \(\arctan(1/2)>1/2-(1/2)^3/3=11/24\).
For the four corners, the lower estimate from (9)--(11) is at least
\(-24\pi/25+11/8>-3\pi/4\); the upper is at most
\(71\pi/100<3\pi/4\). Thus \(3\pi/4\) is a valid common
Lipschitz constant, derived for this new trial rather than inherited
from the old \(.3\) trial.

Partition \([-.102,-.001]\) into 32 equal closed intervals
\([h_j^-,h_j^+]\), with exact midpoint \(q_j\). The fixed sufficient
test is
\[
 d_{\xi,\eta}(q_j)-\frac{3\pi}{4}
                 \frac{h_j^+-h_j^-}{2}>0,
 \quad j=0,\ldots,31,\quad \xi,\eta\in\{.22,.45\}.
 \tag{12}
\]
If all 128 inequalities pass, their exact minimum is a strict uniform
gap. No additional guessed numerical margin is imposed.

## 4. Sole evaluation protocol and finite-source implication

The [standalone driver](../experiments/check_mixed_terminal_upper_input_left_cut.py)
is limited to the 128 expressions (12) at 160-bit precision. It uses
the original regular-strip formula
\[
            g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}
                              {2\pi i}.
 \tag{13}
\]
It evaluates the canceled original difference
\[
 \Re\{g(s_h+b)-g(l+b)+g(s_h+a)-g(l+a)
                   -3g(s_h)+3g(l)+2\pi ib(s_h-l)\}.
 \tag{14}
\]
There are six primitive calls per test, 768 total. All rational input
conversions are checked for outward containment; all primitive arguments
are checked against the original strip and dilogarithm cut. The exact
midpoint intervals, height corrections, whole-interval lower bounds,
counts and before/after bindings are saved. Every planned comparison is
attempted even if a previous lower bound is nonpositive. A failed sign
is inconclusive, not a negative source statement. An arithmetic exception
is archived separately with the completed prefix. No refinement, second
trial, optimizer, source root or automatic retry is permitted.

Together with the
[ordinary-label height extension](research_mixed_terminal_ordinary_label_height_extension.md),
success of (12) would remove all nonmain ordinary labels for every
actual incoming reference in \(K_3\cup K_4\), while all real targets
still range independently over \(P\). It would complete that pointwise
reduction, without proving any new terminal-profile sign or extending
the separately required finite-source hypotheses to a full auxiliary
disk. Until (12) passes, this final implication remains conditional.
