# The zero-lift conditional root on the real second arc

Private written proof, 11 November 2026. Author-frozen for separate
proof and direct-source review; not adopted.

When both incoming and outgoing coordinates lie on the upper unit
semicircle, the original conditional cubic can have two upper roots.
The logarithmic equation still singles out one root throughout the
real rectangle needed for the unfinished first arc. Its logarithmic
coordinate lies below the real axis and strictly before both numerator
walls. The proof works with the original logarithms and does not
choose a root by its imaginary part alone.

## 1. Original equation and domain

Keep the original own-four conditional phase
\[
 Q(s;a,q)=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),
 \quad 0<\Re w<1.                                             \tag{1}
\]
All logarithms and primitive constants are those in the
[unit-incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md).
Set
\[
 {\cal R}=\{(a,q):1/2\le a<1,\quad 1/2\le q<(1+a)/2\},
 \qquad d=\min(1-a,1-q).                                     \tag{2}
\]
In particular the entire closed rectangle
\[
                 [1/2,7/8]\times[1/2,18/25]                  \tag{3}
\]
lies in \({\cal R}\).

**Theorem.** For every \((a,q)\in{\cal R}\), there is exactly one
solution of
\[
                              Q_s(s;a,q)=0                   \tag{4}
\]
in the vertical strip \(0<\Re s<d\).
It satisfies \(\Im s<0\) and \(Q_{ss}\ne0\).
The solution is locally holomorphic in the parameters.
On every compact subset of \({\cal R}\), all its strip, height
and simplicity margins are uniform.

Consequently the cubic
\[
 v(v-X)(v-Y)-X(v-1)^3=0,\qquad
       X=e^{-2\pi ia},\quad Y=e^{-2\pi iq},\quad v=e^{2\pi is}
 \tag{5}
\]
has a distinguished simple root with
\[
             |v|>1,\qquad 0<\arg v<2\pi d,\qquad Q_s=0.
 \tag{6}
\]
The theorem asserts uniqueness for the original zero logarithmic
lift within this strip. It makes no assertion that (5) has only
one root in the upper half-plane.

## 2. The imaginary part selects a unique negative height

Write \(s=t+i\eta\), with \(0<t<d\), and let
\[
                Q_s(s;a,q)=A(t,\eta)+iI(t,\eta).
\]
The original primitive has
\[
 g''(w)=\pi\cot\pi w-\pi i,\qquad
 Q_{ss}=\pi\{\cot\pi(s+a)+\cot\pi(s+q)-3\cot\pi s\}+\pi i.
 \tag{7}
\]
For real \(u,\eta\),
\[
 \Re\cot\pi(u+i\eta)=
       \frac{\sin 2\pi u}{\cosh 2\pi\eta-\cos 2\pi u}.          \tag{8}
\]
Here \(0<t<d\le1/2\), while
\[
                     1/2<a+t<1,\qquad1/2<q+t<1.
\]
The own cotangent in (7) is positive and both shifted cotangents
are negative. Therefore
\[
                         \Re Q_{ss}<0                        \tag{9}
\]
at every finite height in this strip. By holomorphy,
\[
                        \partial_\eta I=\Re Q_{ss}<0.         \tag{10}
\]

At height zero, the original strip logarithm has argument
\(\pi(1/2-u)\) for \(0<u<1\). Thus
\[
                       I(t,0)=\pi(t+a-q-1/2)<0.              \tag{11}
\]
Indeed \(t+a<1\) and \(q\ge1/2\).
As \(\eta\to-\infty\), each logarithm in \(Q_s\) tends to zero,
so
\[
                       I(t,\eta)\longrightarrow2\pi a>0.   \tag{12}
\]
Continuity, (10) and (11) give exactly one height \(\eta(t)<0\)
with \(I(t,\eta(t))=0\).
The real implicit-function theorem gives a real analytic function
\(\eta(t)\) on \(0<t<d\).
For positive heights \(I<I(t,0)<0\), so no zero of (4) is missed
by this negative-height curve.

## 3. The real part is strictly decreasing on that curve

Write \(Q_{ss}=U+iV\) along \(s=t+i\eta(t)\).
Equation (9) says \(U<0\).
Differentiating \(I(t,\eta(t))=0\) and using the Cauchy--Riemann
equations gives
\[
                  \eta'(t)=-V/U,\qquad
 \frac{d}{dt} A(t,\eta(t))=U-V\eta'(t)
                         =\frac{U^2+V^2}{U}<0.               \tag{13}
\]
Thus at most one point of this curve can satisfy \(A=0\).
It remains to establish that its real part changes sign between
the two ends of the interval. The following boundary estimates
supply existence as well as uniqueness.

For \(0<\rho<1\), define
\[
                  \alpha_\rho(u)=
                    \Arg(1-\rho e^{-2\pi iu}).
\]
The disk stays away from the negative real axis. Its argument obeys
\[
\begin{array}{ll}
 0\le\alpha_\rho(u)\le\pi(1/2-u),&0<u\le1/2,\\
 \pi(1/2-u)\le\alpha_\rho(u)\le0,&1/2\le u<1,
\end{array}                                                    \tag{14}
\]
and \(\alpha_\rho(0)=\alpha_\rho(1)=0\).
These inequalities follow either from the argument of
\(1-e^{-2\pi iu}\), or by differentiation in \(\rho\):
\[
 \partial_\rho\alpha_\rho(u)=
                \frac{\sin 2\pi u}{|1-\rho e^{-2\pi iu}|^2}.
\]
The radius-one limit for \(0<u<1\) is exactly
\(\pi(1/2-u)\).

Fix \(\eta<0\), so \(\rho=e^{2\pi\eta}\in(0,1)\).
At the left boundary \(t=0\), (14) gives
\[
\begin{split}
 I(0,\eta)
 &=\alpha_\rho(a)+\alpha_\rho(q)+2\pi a\\
 &\ge\pi(1+a-q)>0.                                           \tag{15}
\end{split}
\]
At the right boundary there are two cases.

If \(a\ge q\), then \(d=1-a\), the incoming shifted argument
equals one, and the other equals \(1-a+q\). Therefore
\[
\begin{split}
 I(d,\eta)
 &=\alpha_\rho(1-a+q)-3\alpha_\rho(1-a)+2\pi a\\
 &\ge\pi(a-q-1/2)-3\pi(a-1/2)+2\pi a\\
 &=\pi(1-q)>0.                                               \tag{16}
\end{split}
\]
If \(q\ge a\), then \(d=1-q\), and instead
\[
\begin{split}
 I(d,\eta)
 &=\alpha_\rho(1-q+a)-3\alpha_\rho(1-q)+2\pi a\\
 &\ge\pi(q-a-1/2)-3\pi(q-1/2)+2\pi a\\
 &=\pi(1+a-2q)>0.                                           \tag{17}
\end{split}
\]
The last strict inequality is precisely the upper bound on \(q\)
in (2). At an endpoint with argument one, using the lower
bound \(-\pi/2\) in (14) only weakens its actual value zero.
Thus (16)--(17) also cover \(a=q\).

The heights \(\eta(t)\) cannot tend to negative infinity at either
end: (12) is uniform in \(0\le t\le d\), since all logarithm
arguments tend uniformly to one. If a sequence approaching either
end had a subsequential height limit strictly below zero,
continuity would contradict (15) or (16)--(17).
It follows that
\[
                   \eta(t)\longrightarrow0
                          \quad\text{as }t\to0^+\text{ or }d^-.
 \tag{18}
\]

At the left end \(s\to0\), the own logarithm \(g'(s)\) has
real part tending to \(-\infty\). Its two shifted logarithms
remain finite because \(a,q\in(0,1)\).
Hence
\[
                     A(t,\eta(t))\longrightarrow+\infty
                                      \quad(t\to0^+).         \tag{19}
\]
At the right end, at least one shifted argument tends to one
and its logarithm has real part tending to \(-\infty\).
The own logarithm remains finite since \(0<d\le1/2\).
The other shifted logarithm either remains finite or also
tends to \(-\infty\). Thus
\[
                     A(t,\eta(t))\longrightarrow-\infty
                                      \quad(t\to d^-).        \tag{20}
\]
The incoming chirp is purely imaginary in \(Q_s\) and contributes
nothing to (19)--(20).

Equations (13), (19) and (20) prove existence and uniqueness in
(4). Equation (9) proves nondegeneracy.

## 4. The original lift and uniformity

Exponentiating (4) gives exactly (5), by the identity in the
unit-incoming source. None of the factors \(v,v-X,v-Y,v-1\)
vanishes at this point, since all three logarithm arguments
remain in the strict regular strips. Differentiating that exact
exponential identity at a root shows that \(Q_{ss}\ne0\) also
makes the corresponding polynomial root simple.

All three real arguments \(t,a+t,q+t\) lie strictly between
zero and one. The holomorphic implicit-function theorem thus
continues this solution to a neighborhood of each parameter pair.
Its local continuations agree on the real domain by uniqueness.
In particular the solution is continuous there, including across
the line \(a=q\); the auxiliary minimum \(d\) need not be
differentiable for this conclusion.

For any compact subset of (2), continuity and strictness give
positive lower bounds for
\[
       \Re s,\quad d-\Re s,\quad-\Im s,\quad |Q_{ss}|.
\]
The height is bounded in modulus as well. A finite subcover
therefore gives a common complex parameter neighborhood on
which the same branch and all its original strip margins persist.
This proves the theorem's uniform statements.

At \(a=q=1/2\), this is the old branch selected from the lower
outgoing semicircle. The
[extra-upper-root observation](research_mixed_real_unit_pair_extra_upper_root.md),
Section 3, verifies that the old nonreal upper root has original
lift zero at that boundary, whereas the real root that enters the
upper half-plane has lift \(-2\pi i\).
The old root's logarithmic real part lies strictly in \((0,1/2)\);
the uniqueness just proved identifies it with (4).
The connected real domain (2) continues that same zero-lift branch.
Its modulus property \(|v|>1\) follows from \(\Im s<0\).

## 5. What this does and does not supply

The original conditional critical action
\[
                            \Theta(a,q)=Q(s(a,q);a,q)
\]
is now defined on a fixed neighborhood of the entire rectangle
(3), using its original constants and logarithmic lift.
The second derivative is nonzero there after a sufficiently
small neighborhood is chosen.

A finite-source bound still needs estimates for the original
integration current and every complementary current, including
physical rows across both numerator walls. This theorem gives
no upper bound for their rates and no lower bound for the
complete polynomial. In particular the extra root on another
lift has not been discarded from sampling corrections.

The result repairs the branch-selection obstruction on the
missing middle first arc. It does not by itself close that arc,
complete the second period, or enlarge the proved knot family.

## Direct source versions

| Direct source | SHA-256 | Implication used |
|---|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 | Original phase, strip logarithms and exact exponential critical equation |
| research_mixed_real_unit_pair_extra_upper_root.md | 392abdd352cd4c477deb7277ac3262db494cc80b3f34a6a8db02b600da167beb | Original zero lift of the old branch at \(a=q=1/2\), distinguished from the new \(-2\pi i\) root |

The complete final proof and both directly used source implications
have been read back in full, and both source hashes match.
Separate proof and direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic,
test, import, compilation, or frozen-source edit is used.

