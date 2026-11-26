# Prewall curvature for the lower-left corner phase

Private research deduction, 8 November 2026.  This note proves strict
horizontal curvature for the original first type-four phase on an explicit
height strip reaching the inward seam.  The correlation between the private
and outgoing heights is retained.  The critical-action consequence in §5
has explicit radius and real-part hypotheses; it is not a finite-source
deformation theorem.  No numerical evaluation is used.

## 1. Original phase and domain

Let
\[
 a=x-i\eta,\qquad \frac12\le x\le\frac7{10},\qquad
 0\le\eta\le\frac9{125},\qquad
 y=q-i\xi,\qquad 0\le q\le\frac{11}{50},\qquad
 \frac1{1000}\le\xi\le\frac{51}{500}.
 \tag{1}
\]
Actual applications retain the original correlations between these
parameters; the inequality below holds on this entire containing domain.
Write
\[
 s=v+i\sigma,\qquad \frac2{25}\le v<1-x,\qquad
 |\sigma|\le\frac{\log2}{2\pi}.
 \tag{2}
\]
Thus \(v<1/2\), \(1/2<x+v<1\), and \(0<q+v<1\).
The original phase, with its original logarithmic lift, is
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,
 \qquad g''(z)=\pi\cot(\pi z)-\pi i.
 \tag{3}
\]
This is the phase of the canonical finite row in
[the corner middle reduction](research_mixed_next_lower_left_corner_middle_reduction.md),
§§1–2.  At \(q=0\), the unshifted \(g(y)\) uses the original inward
continuation; it makes no contribution to the \(s\) derivatives.

Put
\[
 K(v,h)=\Re\cot\pi(v+ih)
       =\frac{\sin(2\pi v)}{\cosh(2\pi h)-\cos(2\pi v)}.
 \tag{4}
\]

**Theorem 1.**  On (1)–(2), the positive outgoing cotangent obeys
\[
 K(v+q,\sigma-\xi)
 <
 \left(3-\frac1{540000}\right)K(v,\sigma).
 \tag{5}
\]
When the left side is nonpositive this inequality is automatic.  Since
\(K(x+v,\sigma-\eta)<0\), it follows that
\[
 -\Re Q_{ss}(s;a,y)
 >
 \frac{\pi}{540000}K(v,\sigma)>0.
 \tag{6}
\]
In particular the original real phase is strictly concave horizontally and
strictly convex vertically throughout this prewall strip.

## 2. Exact scalar witnesses

Set
\[
 d_0=\frac{51\pi}{250},\qquad \theta=2\pi v,\qquad c=\cos\theta.
 \tag{7}
\]
We shall use
\[
 c\le\cos\frac{4\pi}{25}<\frac{877}{1000}.
 \tag{8}
\]
Indeed \(\pi>157/50\) gives \(4\pi/25>1/2+3/1250\).
Concavity of cosine and the alternating Taylor bounds at \(1/2\) give
\[
 \cos\frac{4\pi}{25}
 <
 \frac{337}{384}-\frac3{1250}\frac{23}{48}
 =
 \frac{337}{384}-\frac{23}{20000}
 <
 \frac{877}{1000}.
 \tag{9}
\]
The last difference is \(131/240000>0\).

Also \(d_0<2/3\).  In the positive series for \(\cosh t-1\), the ratios of
successive terms after the quadratic term are at most \(t^2/12\).  Hence
\[
 \cosh d_0-1
 <
 \frac{(2/3)^2/2}{1-(2/3)^2/12}
 =\frac3{13},
 \qquad \cosh d_0<\frac{16}{13}.
 \tag{10}
\]
The first three positive terms in the series
\(\log2=2\sum_{j\ge0}(1/3)^{2j+1}/(2j+1)\), together with
\(\pi<22/7\), give
\[
 \log2-d_0>
 \frac{842}{1215}-\frac{561}{875}
 =\frac{11027}{212625}>\frac{31}{600}.
 \tag{11}
\]
The final cross-product difference is \(24825>0\).  Consequently
\[
 3\cosh(\log2-d_0)-\frac54
 >
 \frac74+\frac{961}{240000}
 =
 \frac{877}{500}+\frac1{240000}.
 \tag{12}
\]

## 3. Cotangent maxima and nonpositive private heights

Write
\[
 C=\cosh(2\pi\sigma),\qquad
 1\le C\le\cosh(\log2)=\frac54.
 \tag{13}
\]
The derivative of \(\sin\theta/(C-\cos\theta)\) has the sign of
\(C\cos\theta-1\).  Thus if \(Cc\le1\), its positive part decreases
as the real coordinate increases from \(v\) to \(1/2\).
If \(Cc>1\), its positive global maximum is \(1/\sqrt{C^2-1}\).
In the latter case \(c>0\), and its ratio to \(K(v,\sigma)\) is at most
\[
 \frac{C-c}{\sqrt{C^2-1}\sqrt{1-c^2}}
 <
 \frac{(5/4-c)c}{1-c^2}
 \le\frac{63}{38}<2.
 \tag{14}
\]
Here \(C>1/c\) was used in the denominator.  The rational function on the
right increases for \(0<c<1\): its derivative has numerator
\[
 \frac54-2c+\frac54c^2
 =\frac54\left(c-\frac45\right)^2+\frac9{20}>0.
\]
Now use (8), weakened to \(c<9/10\), and substitute \(9/10\).

Suppose \(\sigma\le0\).  If \(v+q\ge1/2\), the outgoing cotangent is
nonpositive.  Otherwise replacing \(\sigma\) by the more negative
\(\sigma-\xi\) decreases its positive value.  Applying the preceding
angular comparison at height \(\sigma\) bounds the outgoing cotangent
by \(K(v,\sigma)\) when \(Cc\le1\), and by \(2K(v,\sigma)\) when
\(Cc>1\).  Both bounds are stronger than (5).

## 4. Positive private heights

Let
\[
 \tau=2\pi\sigma,\qquad d=2\pi\xi,\qquad
 C_{\rm own}=\cosh\tau,\qquad
 C_{\rm out}=\cosh(\tau-d),\qquad 0<d\le d_0.
 \tag{15}
\]
Only \(v+q<1/2\) needs consideration.

First suppose \(0\le\tau\le d_0\).  The positive outgoing cotangent is
at most its real-height value, which decreases with its real coordinate.
Its ratio to the own cotangent is therefore at most
\((C_{\rm own}-c)/(1-c)\).  By (8) and (10),
\[
 3-C_{\rm own}-2c>
 \frac{23}{13}-\frac{877}{500}
 =\frac{99}{6500}.
 \tag{16}
\]
Since \(1-c\le2\), this ratio is less than \(3-99/13000\), proving (5)
in this case.

It remains to consider \(d_0\le\tau\le\log2\).  Then
\[
 1\le C_{\rm out}\le C_{\rm own}\le\frac54,\qquad
 C_{\rm out}\ge\cosh(\tau-d_0).
 \tag{17}
\]
If \(C_{\rm out}c>1\), the global maximum argument of (14), using
\(C_{\rm own}\le5/4\) in the numerator and \(C_{\rm out}>1/c\) in the
denominator, again bounds the ratio by \(63/38\).
If \(C_{\rm out}c\le1\), angular monotonicity bounds the ratio by
\[
 \frac{C_{\rm own}-c}{C_{\rm out}-c}.
 \tag{18}
\]
The function \(3\cosh(\tau-d_0)-\cosh\tau\) decreases on
\([d_0,\log2]\).  To verify this explicitly, put \(r=\tau-d_0\).
The elementary bounds \(\log2<7/10\) and
\(d_0>51/80\) imply \(0\le r<1/16\).  Hence
\(3\sinh r<6r<3/8\), whereas \(\sinh\tau\ge\tau\ge d_0>51/80\).
The inequality \(\sinh r<2r\) here follows by integrating
\(\cosh r<2\) on this short interval.
Equations (8), (12), and (17) now give
\[
 3C_{\rm out}-C_{\rm own}-2c>\frac1{240000}.
 \tag{19}
\]
Since \(C_{\rm out}-c\le9/4\), the ratio (18) is less than
\[
 3-\frac1{240000(9/4)}
 =3-\frac1{540000}.
 \tag{20}
\]
This completes (5).  Taking real parts of the exact second derivative
in (3), and using the negative incoming cotangent, proves (6).
No Hessian after elimination of a critical variable is used.

## 5. Conditional comparison of a critical action

Fix the parameters (1).  **Suppose**, in addition, that the original
critical point \(s_*\) is simple, has zero logarithmic lift, and satisfies
\[
 \frac2{25}<\Re s_*<1-x,\qquad
 \frac12<|e^{2\pi i s_*}|<2.
 \tag{21}
\]
These are explicit hypotheses.  This note does not establish the new
lower-radius or real-part guards on the full parameter domain (1).

Let \(\widehat R(v,\sigma)\) be the continuous original upper rate of
[the corner middle reduction](research_mixed_next_lower_left_corner_middle_reduction.md),
§2, and set
\[
 m(\sigma)=
 \max_{\,2/25\le v\le1-x}\widehat R(v,\sigma),
 \qquad |\sigma|\le\frac{\log2}{2\pi}.
 \tag{22}
\]
In the open prewall interval this is \(\Re Q(v+i\sigma;a,y)\).
At \(v=1-x\), the exact numerator period/reflection formula gives the
continuous zero-safe boundary rate.  Away from \(\sigma=\eta\), the
vertical convexity of Theorem 1 extends there by a one-sided limit.
At \(\sigma=\eta\), its incoming-numerator height derivative has an
upward jump of \(\pi\): the original numerator argument tends to \(0\)
below that height and to \(-\pi\) above it.  The boundary profile is
therefore convex as well.  When \(x=1/2\), weak convexity at the
half-index boundary is sufficient.

Thus \(m\), being a maximum of convex height profiles, is convex.
By (6) and (21), \(s_*\) is the unique horizontal maximum at its own
height.  This maximum lies in the regular interior, so \(m\) is
differentiable there and
\(m'(\Im s_*)=-\Im Q_s(s_*;a,y)=0\).
It follows that
\[
 \Re Q(s_*;a,y)\le m(\sigma_0)
 \quad\text{for every }\quad
 |\sigma_0|\le\frac{\log2}{2\pi}.
 \tag{23}
\]

In particular the original reference height
\(h_s\in[-51/500,-1/1000]\) lies in this strip by (11).
At \(a_L=1/2+ih_a\), the complete main-profile comparisons in
[the first right-horizontal theorem](research_mixed_next_lower_left_incoming_right_horizontal.md),
§§2–4, bound \(m(h_s)\) after attaching the original complete cap plane
and each of the next type-four controlling profiles.  Equation (23)
can therefore supply the critical-action comparison once (21) is
proved for the relevant branch.  No finite source factor is replaced
by its phase in this statement.

The exact real middle integral still requires an admissible deformation,
both unweighted joins, and the postwall upper-rate comparison.  Those
source obligations, and the guards (21), are not conclusions of this
note.
