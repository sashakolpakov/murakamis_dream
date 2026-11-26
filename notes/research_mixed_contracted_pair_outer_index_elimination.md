# Exact outer-index elimination for the contracted pair's physical tails

Research deduction, 7 November 2026. The complete physical-tail
comparison for the contracted three-four source reduces exactly to
two real variables. Each outer variable has a finite algebraic
stationary-candidate list, including every endpoint and every
candidate branch. This is a reduction of the original upper rate,
not a proved negative comparison or a numerical protocol.

Use the source, three-face polytope \(\Omega\), and supported-row
upper rate \(E\) in
[the contracted rectangle theorem](research_mixed_contracted_pair_rectangle.md).
Initially \(X=Y=K\), the actual alternating wire exponential.
The formulas below also hold for fixed \(0<|X|,|Y|<1\).
All occurrences of \(J\) are its continuous real primitive on
\([0,1]\), with the original normalization.

## 1. Separate the two outer coordinates exactly

For \(t,p\ge0\), \(t+p\le1\), put
\[
\begin{split}
 C(t,p)&=-\tfrac12\log|XY|+J(t+p)-2J(t)-3J(p),\\
 S_t(s)&=J(s+t)+s\log|X|-\mathcal I_X(s),
                       &&0\le s\le1-t,\\
 Q_p(q)&=J(p+q)-J(q)+q\log|Y|-\mathcal I_Y(q),
                       &&0\le q\le1-p,\\
 \mathcal I_X(s)&=\int_0^s\log|1-Xe^{-2\pi iv}|\,dv.
\end{split}
 \tag{1}
\]
Then \(E=C+S_t+Q_p\). Only the two outer coordinates have
been separated; the shared term \(J(t+p)\) and its original
support \(t+p\le1\) are unchanged.

## 2. At most two interior candidates for the first outer index

Write \(X=\rho e^{i\phi}\), with \(0<\rho<1\).
On the interior of a nontrivial interval \([0,1-t]\),
\[
 S_t'(s)=\log
 \frac{\rho\,|1-e^{-2\pi i(s+t)}|}
                    {|1-Xe^{-2\pi is}|}.
 \tag{2}
\]
Every stationary point therefore satisfies
\[
 A_t\cos(2\pi s)+B_t\sin(2\pi s)=1-\rho^2,
 \quad
 \begin{cases}
 A_t=2\rho\cos\phi-2\rho^2\cos(2\pi t),\\
 B_t=2\rho\sin\phi+2\rho^2\sin(2\pi t).
 \end{cases}
 \tag{3}
\]
This equation is equivalent to (2) being zero at such an interior
point: all quantities whose squares were taken are strictly
positive there. If \(t=1\), the domain is the singleton \(s=0\)
and no derivative is used.

For an explicit complete construction let
\(R_t^2=A_t^2+B_t^2\) and \(d=1-\rho^2>0\).
There are no candidates if \(R_t^2<d^2\). Otherwise the
possible pairs \((\cos(2\pi s),\sin(2\pi s))\) are
\[
 \frac d{R_t^2}(A_t,B_t)
 \ \pm\ \frac{\sqrt{R_t^2-d^2}}{R_t^2}(-B_t,A_t).
 \tag{4}
\]
Retain every representative \(s\) in the interval being
maximized. When equality holds in \(R_t^2=d^2\), (4) is a
single candidate. The case \(R_t=0\) belongs to the no-root
case, so no zero denominator is introduced. Thus each subinterval
requires its two endpoints and at most two interior candidates.

## 3. At most four interior candidates for the last outer index

Write \(Y=\sigma e^{i\psi}\), with \(0<\sigma<1\).
For \(0<q<1-p\),
\[
 Q_p'(q)=\log
 \frac{\sigma\,|1-e^{-2\pi i(p+q)}|}
 {|1-e^{-2\pi iq}|\,|1-Ye^{-2\pi iq}|}.
 \tag{5}
\]
Set \(\theta=2\pi q\), and define
\[
 A_p=1+\sigma^2-\sigma^2\cos(2\pi p)+2\sigma\cos\psi,
 \qquad B_p=\sigma^2\sin(2\pi p)+2\sigma\sin\psi.
 \tag{6}
\]
Squaring (5) and cancelling the common factor two gives exactly
\[
 -(1+\sigma\cos\psi)+A_p\cos\theta+B_p\sin\theta
       -\sigma\cos\psi\cos(2\theta)
       -\sigma\sin\psi\sin(2\theta)=0.
 \tag{7}
\]
Equivalently \(z=e^{i\theta}\) is a unit-circle root of
\[
 -\sigma e^{-i\psi}z^4+(A_p-iB_p)z^3
 -2(1+\sigma\cos\psi)z^2
                  +(A_p+iB_p)z-\sigma e^{i\psi}=0.
 \tag{8}
\]
The leading coefficient is nonzero. Hence there are at most four
distinct candidates on one period. Keep all unit-circle roots whose
representatives belong to the open interval being maximized, and
also keep its endpoints. Repeated roots need not be discarded by
a sign-change test. No assertion that every root of (8) lies on
the unit circle is used.

At \(p=0\), numerator and denominator in the first ratio of
(5) cancel on \((0,1)\); equation (7) is still equivalent there.
Any extra zero introduced by squaring at \(q=0\) or \(q=1\)
is merely an endpoint already retained. At \(p=1\), the entire
domain is the singleton \(q=0\). Thus factorial ends and
degenerate fibers do not require an omitted limiting branch.

The functions in (1) are continuous on their closed intervals and
differentiable in the interiors just used. The extreme-value theorem
and Fermat's condition therefore prove that these endpoint and
stationary lists give the exact maxima, also on each component of
a finite union of closed subintervals. This conclusion does not
assume concavity of the physical real-index functions.

## 4. The full physical complement becomes a two-variable envelope

Let \(I_3=[1/4,9/20]\) and \(I_4=[1/5,21/50]\).
Define the four exact one-variable maxima
\[
\begin{split}
 S(t)&=\max_{[0,1-t]}S_t,&
 S_{\rm out}(t)&=\max_{[0,1-t]\setminus\operatorname{int}I_3}S_t,\\
 Q(p)&=\max_{[0,1-p]}Q_p,&
 Q_{\rm out}(p)&=\max_{[0,1-p]\setminus\operatorname{int}I_4}Q_p.
\end{split}
 \tag{9}
\]
The restricted sets are at most two closed intervals, with all
support endpoints clipped to their actual fibers. Maxima over an
empty set can be assigned \(-\infty\). Sections 2--3 give finite
exact candidate descriptions for every maximum in (9).

For \(T=\Omega\setminus\operatorname{int}(I_3^2\times I_4^2)\),
one has the identity
\[
 \max_T E
 =\max_{\substack{t,p\ge0\\t+p\le1}}\left[C(t,p)+
 \begin{cases}
 S(t)+Q(p),&(t,p)\notin\operatorname{int}(I_3\times I_4),\\
 \max\{S_{\rm out}(t)+Q(p),\ S(t)+Q_{\rm out}(p)\},
                      &(t,p)\in\operatorname{int}(I_3\times I_4).
 \end{cases}\right].
 \tag{10}
\]
For the first case the entire outer fiber belongs to \(T\).
For the second, its precise restriction is the union of the event
that \(s\) is outside its central interval and the event that
\(q\) is outside its central interval. Separability in (1)
proves (10). In particular the two removed tails are combined by
a maximum, without either subtracting their intersection or omitting
it. All boundary fibers are included in the first case.

Equation (10) is an exact dimension reduction of the original
supported-row upper rate. It keeps the shared physical support,
all coordinate ends, all stationary branches and the original
external cardinal contribution. It does not establish that its
value is below the calibrated action, nor control the nonmain
four-index currents. No candidate values, roots, analytic functions
or parameter grids have been evaluated for this deduction.

## 5. A proved far tail and a compact remaining rectangle

Now fix \(X=Y=K\). The original reference bounds give
\(3/5<\rho=|K|<5/8\). The inherited
[three-vertex high-index barrier](research_three_vertex_alternating_reference_complement.md),
Lemma 1, applies to \(E_s=S_t'(s)\) without change: it is
negative whenever \(s\ge9/20\). Thus decreasing any larger
\(s\) to \(9/20\) increases \(E\) and preserves all support
inequalities. Likewise the high-index argument in
[the four real-complement theorem](research_power_four_real_complement.md),
Section 2, applies literally to \(E_q=Q_p'(q)\). It is
negative for \(q\ge2/5\), independently of its supported
neighbor \(p\). In particular any \(q>21/50\) can be
decreased to \(21/50\).

These particular cut values preserve membership in \(T\):
the new outer coordinate is on its central-box boundary, not in
its interior. An unrestricted outer maximum may use the stronger
\(q\le2/5\) reduction, but that reduction is not used to
forget a tail label here.

**Proposition 2.** On the entire physical region \(p\ge5/6\),
\[
                       E<\frac{2261}{1500}<M-\frac1{200},
 \tag{11}
\]
where \(M\) is the original calibrated critical action in the
contracted rectangle theorem.

*Proof.* First reduce \(s\) to at most \(9/20\) as above;
this leaves \(p\ge5/6\). The support implies
\(0\le t,q\le1/6\). The primitive satisfies
\(J\ge0\) on \([1/2,1]\) and is decreasing on \([5/6,1]\).
Hence
\[
             J(p+t)+J(p+q)-3J(p)\le-J(p)\le0.
\]
The elementary bound \(|J|<1/6\) on \([0,1]\), used in
[the full source strip bounds](research_mixed_boundary_strip_bounds.md),
therefore bounds the remaining three terms by
\(J(s+t)-2J(t)-J(q)<2/3\).

For \(v\ge0\), the external contribution obeys
\[
 L(v):=v\log\rho-\mathcal I_K(v)
 \le v\log\frac{\rho}{1-\rho}\le v\log\frac53.
 \tag{12}
\]
Also \(-\log\rho<\log(5/3)<13/25\). For the last
comparison, the first four positive exponential-series terms give
\(e^{13/25}>1+13/25+(13/25)^2/2+(13/25)^3/6>5/3\).
Consequently
\[
 E<\frac23+\left(1+\frac9{20}+\frac16\right)\frac{13}{25}
       =\frac{2261}{1500}.
\]
The original complete vertex packets give
\(M>6562/10000+8562/10000=3781/2500\), so the gap is
larger than \(19/3750>1/200\). This bound includes the
continuous support faces and the corner \(p=1,t=q=0\);
it makes no logarithmic derivative evaluation there. \(\square\)

Two further monotonicities reduce the rest of the physical domain.
At an interior supported point,
\[
\begin{split}
 E_t&=\log\frac{\sin\pi(s+t)\sin\pi(t+p)}{\sin^2\pi t},\\
 E_p&=\log\frac{\sin\pi(t+p)\sin\pi(p+q)}{2\sin^3\pi p}.
\end{split}
 \tag{13}
\]
For \(t\ge1/2\), each numerator sine in the first line is
at most \(\sin\pi t\); thus decreasing \(t\) to \(1/2\)
does not decrease \(E\). For \(1/2\le p\le5/6\), the
second line is at most \(-\log(2\sin\pi p)\le0\), so
decreasing \(p\) to \(1/2\) likewise increases or preserves
the rate. Both operations preserve support and leave the changed
internal coordinate outside its central interval. Continuity covers
the endpoints where a numerator sine vanishes.

Handle \(p\ge5/6\) by Proposition 2 first. For every other
tail point, perform the outer reductions, then the \(t\) and
\(p\) reductions in (13) when needed. Each step preserves
\(T\). The resulting point lies in
\[
 R=[0,9/20]\times[0,1/2]\times[0,1/2]\times[0,21/50],
 \qquad T_R=R\setminus\operatorname{int}(I_3^2\times I_4^2).
 \tag{14}
\]
The whole rectangle \(R\) lies in \(\Omega\): its first
and last sum coordinates are at most \(.95\) and \(.92\),
and \(t+p\le1\), with equality only when \(t=p=1/2\).
Thus the exact remaining upper comparison is bounded by
\[
             \max_T E\le
             \max\left\{\frac{2261}{1500},\ \max_{T_R}E\right\}.
 \tag{15}
\]
The first entry is now strictly below the actual action. The second
entry is not assigned a sign here.

## 6. The outer low tails over central internal coordinates

There are useful further analytic boundary reductions on (14).
For every \(0\le t\le1/2\),
\[
                \max_{0\le s\le1/4}S_t(s)
                        =\max\{S_t(0),S_t(1/4)\}.
 \tag{16}
\]
To prove this, let \(F(\theta)=A_t\cos\theta+B_t\sin\theta-d\)
be the stationary expression in (3), with
\(0\le\theta\le\pi/2\), \(d=1-\rho^2\).
The original \(K\) has \(\Im K>1/2\): this follows already
from \(\rho>3/5\), \(.18<\Re x_0<1/4\), and
\(\sin(2\pi\Re x_0)>\sin(\pi/3)>5/6\).
Thus \(B_t=2\Im K+2\rho^2\sin(2\pi t)>1>d\), so
\(F(\pi/2)>0\). If \(A_t<0\), then \(F\) is strictly
increasing on this interval. If \(A_t\ge0\), it is concave,
so its nonnegative set is an interval containing \(\pi/2\).
In either case its sign can only change from negative to positive.
By (2)--(3), \(S_t'\) has that same sign wherever it is finite.
Hence it has no interior maximum larger than both endpoints.
The possibly singular endpoint \(s=t=0\) is handled by continuity.

If \(1/5\le p\le21/50\), then \(Q_p\) is strictly increasing
on \([0,1/5]\). Indeed the original parameter inequalities give
\[
 \frac{\rho}{|1-K|}>\frac{163}{250},\qquad
 |1-Ke^{-2\pi iq}|\le|1-K|\quad(0\le q\le1/5).
\]
For fixed \(p\), the sine ratio in (5) decreases with \(q\).
At \(q=1/5\), its numerator is at least \(\sin(19\pi/50)>37/40\),
while \(\sin(\pi/5)<3/5\). The former follows from
\(\cos(3\pi/25)\ge1-(3\pi/25)^2/2>37/40\), using
\(\pi<22/7\). Therefore the argument of the logarithm in
(5) is greater than
\[
                        \frac{163}{250}\frac{37}{24}
                                 =\frac{6031}{6000}>1.
 \tag{17}
\]
The physical endpoint \(q=0\) follows by continuity.

Consequently, when \((t,p)\in I_3\times I_4\), all outer-exit
parts of \(T_R\) are bounded by the five faces
\[
                s\in\{0,1/4,9/20\},
                   \qquad q\in\{1/5,21/50\},
 \tag{18}
\]
with the other outer variable unrestricted in its interval in (14).
These reductions do not remove the internal low tails
\(t<1/4\), \(p<1/5\), or their upper boundary strips.
They preserve the original rate and require no new function values.

## 7. The unique conditional optimizer in the shared type-three index

Fix \(0<s,p<1\) and any \(0\le q\le1-p\).
The exact supported \(t\)-fiber is
\([0,L]\), where \(L=1-\max(s,p)>0\). On its interior,
the first derivative is the first line of (13), and
\[
 E_{tt}=\pi\{\cot\pi(s+t)+\cot\pi(t+p)-2\cot\pi t\}<0.
 \tag{19}
\]
Both shifted arguments lie strictly between \(t\) and one,
and the cotangent is strictly decreasing there. Moreover
\(E_t\to+\infty\) as \(t\downarrow0\), and
\(E_t\to-\infty\) as \(t\uparrow L\). Thus the fiber has
exactly one stationary point, and it is its unique global maximum.
This assertion does not require \(s,t,p\) to lie in their
central rectangles.

It has an explicit algebraic description. Put
\[
 u=\cot\pi s,\qquad v=\cot\pi p,\qquad
 w_+=-\frac{u+v}{2}
       +\sqrt{\frac{(u-v)^2}{4}
                         +\sqrt{(1+u^2)(1+v^2)}}.
 \tag{20}
\]
Then the maximizing coordinate is
\[
                  t_{\max}=\frac1\pi\operatorname{arccot}w_+,
               \qquad 0<\operatorname{arccot}w_+<\pi.
 \tag{21}
\]
Indeed, writing \(w=\cot\pi t\), the equation \(E_t=0\)
and positivity of the supported sines give
\[
 (u+w)(v+w)=\sqrt{(1+u^2)(1+v^2)},
                         \qquad u+w>0,\quad v+w>0.
 \tag{22}
\]
The positive square root in (20) gives
\(w_+>-\min(u,v)=\cot\pi L\), hence \(0<t_{\max}<L\).
The other quadratic root is strictly below \(-\max(u,v)\)
and violates both positivity conditions in (22). It is not a
second physical branch. On any closed subinterval of the supported
fiber, the maximum is therefore obtained by clipping \(t_{\max}\)
to that interval. For a union of subintervals, retain each clipped
candidate and take the largest value.

The boundary fibers have elementary descriptions and are not
discarded. If \(s=0\) and \(0<p<1\), the unique maximum is
\(t=(1-p)/2\); if \(p=0\) and \(0<s<1\), it is
\(t=(1-s)/2\). These follow by cancelling the common sine
in (13), before solving \(\sin\pi(t+p)=\sin\pi t\), or its
transposed equation. If \(s=p=0\), the rate is independent
of \(t\). If \(s=1\) or \(p=1\), support forces \(t=0\).

This is a further exact conditional maximization formula for the
same physical rate. It does not justify maximizing incompatible
outer candidates simultaneously, and supplies no sign for the
remaining compact tail comparison in (15).
