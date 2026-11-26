# The fixed later-point departure does not extend to the whole incoming arc

Research deduction, 8 November 2026. The departure used for the
complete main contour at the exact later point is above the actual
cap critical action when the incoming coordinate reaches \(7/10\).
This is a comparison of original phases on their selected sheets,
proved by algebraic and differential inequalities. No action, root,
finite sum, or saved certificate is evaluated.

Consequently that particular departure cannot be retained in a
pointwise descending contour for the whole real incoming arc.
The conclusion does not rule out an earlier or varying departure,
a different contour, or cancellation in the finite source.

## 1. The original phase and the two fixed private points

Retain precisely the original phase
\[
 \Psi(e,a)=S(e)+J(a+e)-J(a)-i\pi ae,\qquad
 M(a)=\Re\Psi(e_*(a),a),
 \tag{1}
\]
where \(e_*(a)\) is the selected cap critical point. Its original
zero lift and absolute constant are fixed by
[incoming phase transport](research_mixed_half_face_general_incoming_transport.md).
On \(1/2\le a\le7/10\), the
[actual-path theorem](research_mixed_endpoint_actual_cap_path_bridge.md)
gives
\[
 6/25<\Re e_*(a)<9/20,\qquad -3/50<\Im e_*(a)<0,
 \qquad \Re e_*(a)<1-a.
 \tag{2}
\]

Use the exact points of
[the later-point main contour](research_mixed_cap_later_point_main_contour.md):
\[
\begin{gathered}
 p_0=i\sqrt2,\quad e_0=\frac14-\frac{i\log2}{4\pi},
 \quad h_0=\Im e_0,\\
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\quad
 a_0=1-\frac{\Arg X_0}{2\pi},\quad e_*(a_0)=e_0,\\
 q_d=\frac{11}{12},\quad
 p_d=\frac{23}{144}+\frac{11\sqrt2}{12}i,\quad
 e_d=\frac{\Log p_d}{2\pi i},\quad
 K=|p_d|^2=\frac{35377}{20736}.
\end{gathered}
\tag{3}
\]
Thus \(23/100<\Re e_d<6/25\) and \(-3/50<\Im e_d<0\).
Both fixed points are in the original regular phase chamber
for every \(a\in[a_0,7/10]\). Define the real difference
\[
 D(a)=\Re\Psi(e_d,a)-\Re\Psi(e_0,a).
 \tag{4}
\]
This difference retains the exact incoming chirp in (1).

The logarithmic expansion and the two-sided remainder in equation
(8) of the cited main-contour proof imply, with \(d=1/12\),
\[
 D(a_0)\ge
 -\frac{d^2}{\pi}
 \left(\frac{1927\sqrt2}{23328}+\frac{25}{432}\right)
 >-\frac{39}{100000}.
 \tag{5}
\]
For the last inequality, \(\sqrt2<99/70\) and \(\pi>25/8\)
bound the positive quantity by
\[
 \frac{285273}{734832000}<\frac{39}{100000}.
 \tag{6}
\]
This uses the already proved two-sided logarithmic remainder,
not a new estimate of the critical action.

## 2. An exact lower bound for the incoming derivative

Write \(X=e^{-2\pi ia}=c+is\). The original multiplier gives
\[
 D'(a)=
 \log\frac{|1-X/p_d|}{|1-X/p_0|}.
 \tag{7}
\]
Put
\[
 Q_d=|1-X/p_d|^2
   =1+\frac1K-\frac{23c}{72K}
                         -\frac{11\sqrt2\,s}{6K},
 \qquad Q_0=\frac32-\sqrt2\,s .
 \tag{8}
\]
We claim
\[
             Q_d>\frac{32}{25}Q_0
             \qquad(a_0\le a\le7/10).
 \tag{9}
\]

To prove this with the unit-circle correlation retained, set
\[
 \alpha=\sqrt2\left(\frac{32}{25}-\frac{11}{6K}\right),
 \qquad \beta=\frac{23}{72K}.
 \tag{10}
\]
The elementary bounds \(3/2<K<7/4\) give
\[
       0<\alpha<5/14,\qquad \beta>23/126.
 \tag{11}
\]
For \(\vartheta=\Arg X\in[3\pi/5,\Arg X_0]\),
\(\cos\vartheta\ge-1/3\) and
\(\sin\vartheta\ge2\sqrt2/3>14/15\). Therefore
\[
 \frac{d}{d\vartheta}
       (\alpha\sin\vartheta-\beta\cos\vartheta)
 >-\frac5{42}+\frac{23}{126}\frac{14}{15}>0.
 \tag{12}
\]
Its minimum is attained at the actual endpoint
\(\vartheta=3\pi/5\), rather than at unrelated bounds on \(c,s\).

At that endpoint,
\[
 -c=\frac{\sqrt5-1}{4}>\frac{309}{1000},\qquad
 s=\sin(3\pi/5)>\frac{951}{1000},\qquad
 \sqrt2\,s>\frac{2219}{1650}.
 \tag{13}
\]
Here \(\sqrt5>559/250\) proves both first inequalities by
squaring, and \(\sqrt2>140/99\) gives the last.
Combining (8), (10), (12), and (13) yields
\[
 Q_d-\frac{32}{25}Q_0
 >
 \frac{16529}{20625}-\frac{1082543}{792000K}>0.
 \tag{14}
\]
After inserting the exact rational \(K\), the final sign is
the integer inequality
\[
 3173568\cdot35377-5\cdot1082543\cdot20736
                    =33256896>0.
 \tag{15}
\]
This proves (9). The inequality
\(\log x>2(x-1)/(x+1)\), for \(x>1\), now gives
\[
                       D'(a)>\frac7{57}.
 \tag{16}
\]

The length of this actual incoming interval has the lower bound
\[
                        \frac7{10}-a_0>\frac1{250}.
 \tag{17}
\]
Indeed \(a_0<87/125\) is equivalent to
\(\sin(27\pi/250)<1/3\). For \(z=27\pi/250\), use
\(1/3<z<297/875<7/20\) and the alternating sine estimate:
\[
 \sin z\le z-\frac{z^3}{6}+\frac{z^5}{120}
 <\frac{297}{875}-\frac1{162}
                      +\frac{16807}{384000000}<\frac13.
 \tag{18}
\]
For the last comparison,
\(297/875-55/162=-11/141750\), whereas
\(16807/384000000<1/20000<11/141750\).
Equations (5), (16), and (17) prove
\[
                  D(7/10)>\frac7{14250}-\frac{39}{100000}.
 \tag{19}
\]

## 3. A trial-height upper bound for the actual critical action

Here fix \(a=7/10\) and write
\[
 R(E,h)=\Re\Psi(E+ih,7/10),\qquad
 F(h)=\max_{6/25\le E\le3/10}R(E,h).
 \tag{20}
\]
On the lower open height interval \(-3/50<h<0\),
[the cap curvature theorem](research_mixed_cap_wall_action_gap.md)
gives \(-\Re S''>0\) on this private rectangle.
The real part of the outer cotangent is nonpositive because
\(47/50\le a+E\le1\). Hence
\[
                       R_{EE}<0,\qquad R_{hh}>0.
 \tag{21}
\]
The maximum of convex height profiles is convex. At the actual
critical height \(h_*=\Im e_*(7/10)\), the unique maximizing
real part is \(E_*=\Re e_*(7/10)\), interior by (2).
Criticality gives \(F'(h_*)=0\). Consequently
\[
                         M(7/10)\le F(h_0).
 \tag{22}
\]
This is an upper bound for the actual action with its original
constant. It is not an identification with a real-row maximum.

At \(E=1/4\), the original multiplier and the identity at \(a_0\)
give
\[
 R_E(1/4,h_0)
 =\frac12\log\{9-6\sqrt2\sin(3\pi/5)\}.
 \tag{23}
\]
The logarithm's argument is less than one by (13), and greater
than \(519/560\). For the latter use
\(\sqrt2<99/70\) and \(\sin(3\pi/5)<137/144\);
the sine bound follows from
\(\sqrt5<161/72\), since \(18756<18769\).
As \(-\log(1-u)\le u/(1-u)\),
\[
              -\frac1{25}<R_E(1/4,h_0)<0,
 \tag{24}
\]
because \((41/519)/2<1/25\).
Strict horizontal concavity therefore places the maximizer
in (20), at height \(h_0\), in \(6/25\le E<1/4\).

On this smaller interval the same exact curvature is bounded
quantitatively:
\[
                        -R_{EE}(E,h_0)>10.
 \tag{25}
\]
Here are explicit witnesses. The original identity is
\[
 -S''(e)=\pi\cot\pi e+
       \frac{2\pi}{\sin\pi e\sqrt{\,2-e^{-2\pi ie}\,}}.
 \tag{26}
\]
At height \(h_0\),
\(\cosh(2\pi h_0)=3/(2\sqrt2)<15/14\), so
\[
 \Re\cot\pi e>\frac{231}{250}.
 \tag{27}
\]
Indeed \(\sin(2\pi E)\ge\cos(\pi/50)>99/100\) and
\(\cos(2\pi E)\ge0\).
Also \(|\sin\pi e|<3/4\), since its square is at most
\(1/2+1/28<9/16\), and
\[
 |\sqrt{2-e^{-2\pi ie}}|<3/2.
 \tag{28}
\]
For (28), the square of \(|2-e^{-2\pi ie}|\) is
\(9/2-2\sqrt2\cos(2\pi E)\le9/2<(3/2)^4\).
The original argument bounds give
\[
 -3/10<\arg\sin\pi e\le0,\qquad
 0<\arg\sqrt{2-e^{-2\pi ie}}<\pi/8.
 \tag{29}
\]
For the second bound the number under the square root has
real part greater than one and imaginary part less than one.
The reciprocal product in (26) thus has real part greater
than \(28/45\). Equations (27)--(29) imply
\(-\Re S''>2\pi\).

Finally put \(s=1-a-E\in[1/20,3/50]\). Then
\[
 -\Re\cot\pi(a+e)
 =\frac{\sin(2\pi s)}
        {\cosh(2\pi h_0)-\cos(2\pi s)}
 >\frac{3/10}{15/14-9/10}=\frac74.
 \tag{30}
\]
The numerator uses \(\sin(\pi/10)>3/10\); the denominator
uses \(\cos(3\pi/25)>9/10\), directly from
\(3\pi/25<2/5\) and \(\cos x\ge1-x^2/2\).
Thus \(-R_{EE}>15\pi/4>10\), proving (25).

Taylor's inequality on \(6/25\le E\le1/4\), followed by
maximization of its quadratic, now gives
\[
 F(h_0)\le
 R(1/4,h_0)+\frac{R_E(1/4,h_0)^2}{20}
 <\Re\Psi(e_0,7/10)+\frac1{12500}.
 \tag{31}
\]

## 4. The obstruction and its precise scope

Combining (19), (22), and (31) proves
\[
\begin{split}
 \Re\Psi(e_d,7/10)-M(7/10)
 &>\frac7{14250}-\frac{47}{100000}\\
 &=\frac{121}{5700000}>\frac1{50000}.
\end{split}
\tag{32}
\]
This is the actual selected cap critical action at the actual
incoming endpoint \(a=7/10\), not a test of an unrealized
containing box. The finite endpoint source at \(e_d\) is available
from the above-curve and west-below-curve theorems, but that source
availability does not change the action comparison (32).

The later-point main contour retains \(e_d\) and has a strict
descending comparison near \(a_0\). It therefore cannot be
extended over the entire real incoming arc while keeping this
same departure and requiring every main-path point to have rate
at most \(M(a)\). Earlier departures, paths through a larger
source corridor, or a coupled contour remain possible.

No conclusion about the magnitude of a signed main integral,
the full finite cap, or the following selected product follows
from (32). In particular this note supplies no lower bound for
any finite oscillatory sum and makes no knot-family assertion.
