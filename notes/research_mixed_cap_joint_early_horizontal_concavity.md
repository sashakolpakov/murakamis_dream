# Joint concavity of the first-cap phase down to the early interval

Research deduction, 10 November 2026. The first-cap phase has a
negative definite real Hessian on the entire early rectangle, in
both the private and outgoing variables. This extends the calibrated
main horizontal contour from the plateau to outgoing real parts as
small as one tenth, provided its height stays at the original
reference height. It does not estimate the prescribed contour on
which the first two outgoing heights change together.

## 1. The original phase and its domains

Use the original primitives and endpoint branch from
[the early-contour theorem](research_mixed_cap_early_taper_complex_profiles.md).
Thus
\[
 g'(z)=\log(1-e^{-2\pi iz}),\qquad
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\qquad
 J'(z)=\log(2\sin\pi z).
\tag{1}
\]
Every logarithm has the continuation used in that source. Let
\(S(e)\) be its original complete-end coefficient action. For
\(\alpha=0,1\), corresponding to first type three or four, put
\[
 \Psi_\alpha(e,z)
 =S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),\qquad
 \Xi_\alpha(e,z)=\Psi_\alpha(e,z)-\frac\alpha2g(z).
\tag{2}
\]
The second phase includes the outgoing unselected halfweight.
Its use for the finite type-four source requires the original
negative outgoing reference height. The phase inequality below
is a statement about the holomorphic functions themselves.

The domains are
\[
 E=[27/100,49/100]+i[-11/200,1/25],\qquad
 Z_0=[1/10,11/50]+i[-27/250,21/1000].
\tag{3}
\]
All arguments in (2) stay in their original regular strips.
No correlation between the real and imaginary parts of \(z\)
is imposed in (3).

For a complex symmetric Hessian, \(-\Re H\succ cI\) means
that \(-\Re(v^THv)>c\|v\|^2\) for every nonzero real vector
\(v\). It controls horizontal real displacements.

## 2. A stronger endpoint curvature bound

**Lemma 1.** On \(E\), write \(q=\Re\cot\pi e\). Then
\[
             -\Re S''(e)/\pi>q+3/4.
\tag{4}
\]

*Proof.* The exact identity, with its branch already established
in Lemma 1 of the early-contour theorem, is
\[
 -S''(e)/\pi
  =\cot\pi e+
       \frac{2}{\sin\pi e\sqrt{2-e^{-2\pi ie}}}.
\tag{5}
\]
The square root has positive real part. Write \(e=u+iv\)
and \(w=2-e^{-2\pi ie}\). Since \(1/4<u<1/2\),
\[
 \Re w>2,\qquad 0<\Im w<4/3,
 \qquad |w|<10/3<4.
\tag{6}
\]
Here \(e^{2\pi v}\le e^{2\pi/25}<4/3\): the elementary
inequality \(\log(1+t)\ge 2t/(2+t)\) gives
\(\log(4/3)>2/7>2\pi/25\).
It follows that \(0<\arg\sqrt w<1/3\) and
\(|\sqrt w|<2\).

The real part of \(\sin\pi e\) is positive, and
\[
 |\tan\arg\sin\pi e|
   =|\tanh\pi v|\cot\pi u<\pi|v|<1/5.
\tag{7}
\]
Moreover \(|\sin\pi e|\le\cosh(\pi v)<21/20\).
For this last bound one may use \(\pi|v|<1/5\) and
\(\cosh t\le(1-t^2/2)^{-1}\), which gives
\(\cosh(\pi v)<50/49<21/20\).
The argument of \(\sin\pi e\sqrt w\) therefore has
absolute value less than \(8/15<3/5\), whose cosine is
greater than \(4/5\). Consequently
\[
 \Re\frac{2}{\sin\pi e\sqrt w}
       >\frac{2(4/5)}{(21/20)2}
       =\frac{16}{21}>\frac34.
\tag{8}
\]
Taking real parts in (5) proves (4). \(\square\)

## 3. Joint curvature on the early rectangle

**Theorem 2.** Both phases in (2) satisfy
\[
              -\Re\Xi_\alpha''\succ\frac\pi{13}I_2,
       \qquad -\Re\Psi_\alpha''\succ\frac\pi{13}I_2
                    \quad\hbox{on }E\times Z_0.
\tag{9}
\]

*Proof.* Put
\[
 s=-\Re S''/\pi,\quad q=\Re\cot\pi e,\quad
 p=\Re\cot\pi z,\quad C=\Re\cot\pi(e+z).
\tag{10}
\]
The first two variables have positive real cotangent parts. Direct
differentiation gives
\[
 -\Re\Xi_\alpha''/\pi
  =\begin{pmatrix}s+\alpha q-C&-C\\
                 -C&(1+\alpha/2)p-C\end{pmatrix}.
\tag{11}
\]
For the bare phase, replace \((1+\alpha/2)p\) by \(p\).
It suffices to prove (9) for the matrix with both additional
nonnegative diagonal terms omitted.

We first record the elementary estimates used below:
\[
 p>4/5;\qquad
 p>1\ \hbox{if }\Re z<9/50;\qquad
 C<6/13\ \hbox{whenever }C>0.
\tag{12}
\]
For their verification, write \(z=x+ih\), \(\theta=2\pi x\).
The height bound gives
\[
 \cosh(2\pi h)<5/4,\qquad
 p=\frac{\sin\theta}{\cosh(2\pi h)-\cos\theta}.
\tag{13}
\]
Indeed \(2\pi|h|\le27\pi/125<17/25\), and
\[
 \cosh t\le1+\frac{t^2}{2(1-t^2/12)}<5/4
            \quad\hbox{when }t^2<12/25.
\]
On \([\pi/5,11\pi/25]\), the positive function
\(\sin\theta+(4/5)\cos\theta\) is concave, so its minimum
is at an endpoint. At the first endpoint, use
\(\sin(\pi/5)>1/2\), \(\cos(\pi/5)>3/4\); at the
second use \(\sin(11\pi/25)>49/50\) and
\(\cos(11\pi/25)>1/6\). Both endpoint values exceed one.
Equation (13) then gives \(p>4/5\).

If \(x<9/50\), use the same concavity argument for
\(\sin\theta+\cos\theta\) on \([\pi/5,9\pi/25]\).
Its first endpoint is greater than \(5/4\), and its second
is greater than \(9/10+2/5>5/4\). This proves \(p>1\).
The estimates at these second endpoints follow from
\(\cos t\ge1-t^2/2\), \(\sin t\ge t-t^3/6\), and
\(3<\pi<22/7\), applied at \(3\pi/50\) and
\(7\pi/50\), respectively.

If \(C>0\), then \(37/100\le\Re(e+z)<1/2\), and
the cotangent formula implies
\[
 C\le\cot(37\pi/100)=\tan(13\pi/100)
   <\frac{5/12}{1-(5/12)^2/2}
   =\frac{120}{263}<\frac6{13}.
\tag{14}
\]
This completes (12).

When \(C\le0\), (11) without the extra diagonal terms is
\(\operatorname{diag}(s,p)\) plus a positive semidefinite
matrix. Lemma 1 and (12) give a lower eigenvalue bound exceeding
\(3/4\).

Suppose next that \(C>0\) and \(\Re(e+z)\ge9/20\).
Then
\[
 C\le\tan(\pi/20)<\frac16.
\tag{15}
\]
For example \(\pi/20<4/25\), and
\((4/25)/(1-(4/25)^2/2)=100/617<1/6\).
The two row diagonal-dominance margins are therefore greater
than \(3/4-1/3=5/12\) and \(4/5-1/3=7/15\).

In the remaining case \(\Re(e+z)<9/20\), one has
\(u<7/20\) and \(x<9/50\). The estimate from the
early-contour proof, \(\cosh(2\pi v)<16/15\), gives
\[
 q>\frac{15}{16}\cot(\pi u)
   >\frac{15}{16}\tan(3\pi/20)>\frac{27}{64},
 \qquad s>\frac{75}{64}.
\tag{16}
\]
Here the ratio to the real cotangent is bounded below by
\(1/\cosh(2\pi v)\), because \(\cos(2\pi u)<0\).
Using (12) and (14), the two row margins now exceed
\[
 \frac{75}{64}-\frac{12}{13}>\frac1{13},
             \qquad 1-\frac{12}{13}=\frac1{13}.
\tag{17}
\]
The real symmetric matrix is bounded below by the smaller
row margin in every case. Restoring its omitted nonnegative
diagonal terms proves both assertions of (9). \(\square\)

## 4. Calibration at the original height

Let \((e_*,z_*)=(b+ih_*,a+ic)\) be an actual reference
admitted by the
[complete first-cap theorem](research_mixed_first_cap_plateau_completion.md).
Then \(e_*\in E\), \(a\in[.22,.45]\), and
\(-.108\le c\le.021\). Let
\(L_\alpha(z)=\mathcal T_\alpha(z,-2)-\alpha g(z)/2\)
be the original allocated cap action. At the reference,
\[
 \Xi_\alpha(e_*,z_*)=L_\alpha(z_*),\qquad
 \partial_e\Xi_\alpha(e_*,z_*)=0,\qquad
 \partial_z\Xi_\alpha(e_*,z_*)=L_\alpha'(z_*).
\tag{18}
\]

**Corollary 3.** For every \(u\in[.27,.49]\) and
\(y\in[.1,.45]\),
\[
 \Re\Xi_\alpha(u+ih_*,y+ic)
 \le\Re L_\alpha(z_*)+\Re L_\alpha'(z_*)(y-a)
       -\frac\pi{400}\bigl((u-b)^2+(y-a)^2\bigr).
\tag{19}
\]

*Proof.* Theorem 2 covers \(y\le.22\). Lemma 1 of
[the plateau phase theorem](research_mixed_first_cap_plateau_phase.md)
covers \(.22\le y\le.45\), with lower Hessian bound
\(\pi/200\). Together they give this weaker common bound
on the full convex product
\(E\times([.1,.45]+i[-.108,.021])\). Integrate it twice
along the horizontal segment from \((e_*,z_*)\) to the
target, and use (18). \(\square\)

Thus a constant-height main horizontal contour is calibrated on
this larger outgoing interval using the same reference and complex
action. No new outgoing critical point is needed. This conclusion
does not bound the full finite cap there: the real private cuts,
horizontal aliases, vertical joins and true index endpoints still
need their own comparisons on any newly used target region.

It also does not justify the original moving-height taper. A
holomorphic phase with negative real horizontal Hessian has a
positive real vertical Hessian. Changing the next coordinate's
height can therefore increase the real part of the joint action,
even after the original complex linear terms cancel. The bound
(19) keeps both displayed heights fixed. Applying it after a
macroscopic height change would be a different assertion.

## Source bindings

| File | SHA-256 |
|---|---|
| research_mixed_cap_early_taper_complex_profiles.md | 6a7b8cd841d89690a9733c1005a2449ce808ba20a875c2d1f8d8ca0b0a769138 |
| research_mixed_first_cap_plateau_phase.md | 159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |

The proof uses symbolic differentiation and the displayed elementary
inequalities. It uses no new mathematical numerical evaluation,
saved-value recomputation, program import, test or compilation.
The frozen manuscripts and earlier proof notes are unchanged.
