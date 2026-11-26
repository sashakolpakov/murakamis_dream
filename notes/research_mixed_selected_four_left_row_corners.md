# Four corner tests for the neighboring four-twist left cut

Research deduction, 6 November 2026.

At the actual ordinary index \(s_*\), the difference from the real
left cut \(s=1/8\) is strictly concave in each outer real target.
An elementary cotangent comparison proves this even when the
outgoing summed height has modulus as large as \(.204\).
Consequently four reference-only corner values bound the entire
pointwise difference from below.

The signs of those four values are not proved here. This note runs
no parameter sweep, source evaluation, root solve or interval cover.
It gives a sufficient test for removing both ordinary-left-cut
comparisons from the next-four finite reduction.

## 1. The literal trial and its target derivatives

Keep the actual first-four/next-four critical reference and profiles
of the [finite-source reduction](research_mixed_selected_four_four_finite_reduction.md).
Thus \(m\ge3\), every later type is three or four, and
\[
 H=1/100,\quad s_*=x_*+ih_s,\quad .24<x_*<.36,\quad
 -.102<h_s,h_b<-.001,\qquad P=[.22,.45].
 \tag{1}
\]
Let \(a_0=1/8\), \(z=y+iH\), and \(b=v+ih_b\).
Use the original own-four phase
\[
 Q_4(s;z,b)=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs.
 \tag{2}
\]
The unchanged index \(s_*\) lies on the original main contour
\([1/8,1/2]+ih_s\). Define
\[
 \Delta(y,v)=\Re\{Q_4(s_*;y+iH,v+ih_b)
                         -Q_4(a_0;y+iH,v+ih_b)\}.
 \tag{3}
\]
The outgoing halfweight occurs in both profiles, and cancels in
their difference. Therefore, pointwise on \(P^2\),
\[
                         B_0(y,v)-B_L(y,v)\ge\Delta(y,v).
 \tag{4}
\]
This uses one legitimate index trial; it makes no assertion about
the location of the true ordinary maximum.

The two outer factorial terms \(-g(z),-g(b)\) cancel in (3).
The original chirp is affine in \(y\). Since
\(g''(w)=\pi\cot\pi w-i\pi\), the remaining derivatives are
\[
 \begin{split}
 \partial_y^2\Delta
 &=\pi\Re\{\cot\pi(s_*+y+iH)-\cot\pi(a_0+y+iH)\},\\
 \partial_v^2\Delta
 &=\pi\Re\{\cot\pi(s_*+v+ih_b)-\cot\pi(a_0+v+ih_b)\}.
 \end{split}
 \tag{5}
\]

## 2. A uniform cotangent comparison

For real \(t,h\), put
\[
 A(t,h)=\Re\cot\pi(t+ih)
       =\frac{\sin2\pi t}{\cosh2\pi h-\cos2\pi t}.
 \tag{6}
\]

**Lemma 1.** If
\[
 x\in[.24,.36],\quad w\in[.22,.45],\quad
 |h|,|k|\le.102,
 \tag{7}
\]
then
\[
                         A(x+w,h+k)<A(a_0+w,k).
 \tag{8}
\]

Set \(t_0=a_0+w\) and \(t_1=x+w\).
Then \(t_1-t_0\ge.115\),
\(t_0\in[.345,.575]\), and \(t_1\in[.46,.81]\).
The original endpoint deductions already give
\[
 \cosh(.204\pi)<49/40,\qquad e^{.204\pi}<19/10.
 \tag{9}
\]
These are the same witnesses used in the
[next-four endpoint proof](research_mixed_first_four_next_four_endpoint_budget.md)
and [correlated outgoing-pair estimate](research_mixed_next_four_correlated_endpoint_budget.md).
The second bound implies \(e^{.408\pi}<361/100\).
Since \((r+r^{-1})/2\) increases for \(r\ge1\),
\[
 \cosh(.408\pi)
 <\frac{361/100+100/361}{2}
 =\frac{140321}{72200}<\frac{39}{20}.
 \tag{10}
\]
We also use the elementary bounds
\[
 \sin(.23\pi)>33/50,\qquad \cos(.23\pi)<19/25,
 \qquad
 \tan(.04\pi)<1/7,\qquad \tan(.075\pi)<243/1000.
 \tag{11}
\]
Explicit rational witnesses are given below.

There are three regimes.

If \(t_1\le1/2\), then \(w\le.26\) and
\(t_0\in[.345,.385]\). The positive real cotangent decreases
under any imaginary displacement, so
\[
 A(t_1,h+k)\le\cot(\pi t_1)\le\tan(.04\pi)<1/7.
 \tag{12}
\]
On the other hand \(\sin(2\pi t_0)\ge\sin(.23\pi)>33/50\)
and the denominator in (6) is less than \(49/40+1\).
Consequently
\[
 A(t_0,k)>\frac{33/50}{49/40+1}
                         =\frac{132}{445}>\frac14,
 \tag{13}
\]
which proves (8) in this regime.

If \(t_0\le1/2\le t_1\), the left side of (8) is
nonpositive and its right side is nonnegative. They cannot both
vanish, since \(t_1-t_0\ge.115\). This proves the strict comparison.

Finally suppose \(t_0\ge1/2\). Then
\[
 t_1\in[.615,.81],\qquad
 u=2\pi(t_1-1/2)\in[.23\pi,.62\pi].
 \tag{14}
\]
On this interval \(\sin u\ge\sin(.23\pi)>33/50\):
the other endpoint has sine \(\sin(.38\pi)>\sin(.23\pi)\).
Also \(\cos u\le\cos(.23\pi)<19/25\).
Since \(|h+k|\le.204\), equations (6), (10)--(11) give
\[
 A(t_1,h+k)
 =-\frac{\sin u}{\cosh2\pi(h+k)+\cos u}
 <-\frac{33/50}{39/20+19/25}
 =-\frac{66}{271}<-\frac{243}{1000}.
 \tag{15}
\]
For a negative real cotangent, an imaginary displacement increases
its value. Therefore
\[
 A(t_0,k)\ge\cot(\pi t_0)
          \ge-\tan(.075\pi)>-\frac{243}{1000}.
 \tag{16}
\]
This proves (8) in the remaining regime, including \(t_0=1/2\).

For the rational witnesses in (11), set \(r=3611/5000<.23\pi\).
The alternating sine and cosine estimates give
\[
 r-\frac{r^3}{6}+\frac{r^5}{120}-\frac{r^7}{5040}>\frac{33}{50},
 \qquad
 1-\frac{r^2}{2}+\frac{r^4}{24}<\frac{19}{25}.
 \tag{17}
\]
Monotonicity of sine and cosine up to \(\pi/2\) proves the
first two inequalities. For the tangent bounds use
\(\sin t\le t\), \(\cos t\ge1-t^2/2\), and \(\pi<22/7\):
\[
 \tan(.04\pi)<\frac{3850}{30383}<\frac17,\qquad
 \tan(.075\pi)<\frac{9240}{38111}<\frac{243}{1000}.
 \tag{18}
\]
These are rational comparisons. Together with
\(66/271>243/1000\), they complete the proof. \(\square\)

The lemma deliberately allows a larger height rectangle than (1).
It is a cotangent inequality on that rectangle, not a claim that
every point of it is an actual word reference.

## 3. Four reference-only corner values

Apply Lemma 1 first with \((h,k)=(h_s,H)\), and then with
\((h,k)=(h_s,h_b)\). Equations (5) give
\[
                    \partial_y^2\Delta<0,\qquad
                    \partial_v^2\Delta<0
                    \quad\text{on }P^2.
 \tag{19}
\]
For each fixed value of the other target, a concave function on an
interval has its minimum at an endpoint. Applying this twice proves
\[
 \min_{y,v\in P}\Delta(y,v)
   =\min_{\epsilon,\eta\in\{.22,.45\}}D_{\epsilon,\eta},
 \qquad D_{\epsilon,\eta}=\Delta(\epsilon,\eta).
 \tag{20}
\]
There is no target grid or target optimizer in (20).

For implementation, the four numbers have the exact expression
\[
 \begin{split}
 D_{\epsilon,\eta}={}&
 \Re\{g(s_*+\epsilon+iH)-g(a_0+\epsilon+iH)\\
 &\quad+g(s_*+\eta+ih_b)-g(a_0+\eta+ih_b)
                        -3g(s_*)+3g(a_0)\}\\
 &-2\pi\{\epsilon h_s+H(x_*-a_0)\}.
 \end{split}
 \tag{21}
\]
The last line is the real part of the original chirp difference
\(2\pi i(\epsilon+iH)(s_*-a_0)\). The actual index height
and the own-four coefficient \(-3g(s_*)\) are both retained.
Equivalently, one may share the common terms:
\[
 \begin{split}
 K_*&=-3\Re g(s_*)+3J(a_0)-2\pi H(x_*-a_0),\\
 I_\epsilon&=\Re\{g(s_*+\epsilon+iH)-g(a_0+\epsilon+iH)\}
                                      -2\pi\epsilon h_s,\\
 O_\eta&=\Re\{g(s_*+\eta+ih_b)-g(a_0+\eta+ih_b)\},\\
 \min_{\epsilon,\eta}D_{\epsilon,\eta}
                    &=K_*+\min_\epsilon I_\epsilon+\min_\eta O_\eta.
 \end{split}
 \tag{22}
\]
Here \(J(a_0)=\Re g(a_0)\). All primitive arguments lie strictly
in the original regular strip \(0<\Re w<1\); the largest possible
summed height modulus is \(.204\). The original primitive and its
centered enclosure therefore apply without a branch change.

**Proposition 2.** At every fixed actual reference in (1),
\[
 B_0(y,v)-B_L(y,v)\ge
        \min_{\epsilon,\eta\in\{.22,.45\}}D_{\epsilon,\eta}
                         \qquad(y,v\in P).
 \tag{23}
\]
This follows immediately from (4) and (20). In particular, the four
scalar inequalities
\[
                    D_{\epsilon,\eta}\ge0
                    \qquad(\epsilon,\eta\in\{.22,.45\})
 \tag{24}
\]
at every actual reference would prove \(B_L\le B_0\) pointwise.
Adding any cap profile and either complete Fourier rate preserves
that comparison, including the original outgoing tangent.
The main-cap/ordinary-left pair would then inherit the proved central
gap, while the cap-left/ordinary-left pair would be dominated by the
same cap-left/ordinary-main pair. Thus the five independent pairs in
the finite reduction would reduce to
\[
                         (0,R),\qquad(L,0),\qquad(L,R).
 \tag{25}
\]

Every input in (21) is determined by the same actual endpoint
parameter through the own-four rational maps \(S_*(U),B_*(U)\):
the latter supplies \(h_b\). The original coordinate rectangles,
reduced disks, coupled sums and next-external domain restrictions
remain in force for any future sufficient test on a containing
reference family. No independent choice of heights or word is made.

This note proves the corner reduction, not (24). A negative corner
value would only show that this fixed index trial fails to dominate
the cut; it would not refute domination by the full main maximum.
Moreover a retained necessary-superset point need not be realized
by a word. Neither kind of failed sufficient test is an actual-word
counterexample by itself.
