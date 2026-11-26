# A smaller left cutoff for the four-crossing conditional sum

Research proof, 5 November 2026. For an own-type-four conditional
factor, the controlled central interval can be extended from
\([3/20,1/2]\) to \([1/8,1/2]\). The original supporting plane
and its quadratic loss are unchanged. The upper side of the residue
contour moves to height \(5/4\), while the lower side stays at
\(-1/5\). All contour contributions remain controlled by that plane
or by the two real cuts.

The left real-row bound improves by more than \(1/80\), uniformly
over the permitted horizontal targets. This avoids requiring the
false independent-reference comparison at the old cutoff. It does
not establish the signs of all the remaining row comparisons.

## 1. The phase and the additional index strip

Use the primitive, branches and actual reference of the
[half-index contour theorem](research_mixed_half_index_contour.md).
The own type is four, so the allocated phase is
\[
 F(s;a,b)=g(s+a)+g(s+b)-3g(s)
       -(1+\eta/2)g(a)-\tfrac32g(b)+2\pi ias,
       \qquad \eta\in\{0,1\}.
 \tag{1}
\]
The outer variables range over
\[
 \mathcal P=[11/50,9/20]+i[-3/25,3/25].
 \tag{2}
\]
For the new curvature argument take
\[
 1/8\le\Re s\le3/20,\qquad
             -27/250\le\Im s\le17/250.
 \tag{3}
\]
All individual arguments and their sums in (1) remain in the original
regular strip. The proof below uses the full three-variable Hessian.
The separate two-variable pair forms need not both be positive on
this larger index strip.

Write
\[
 u=\Re\cot\pi s,\quad p=\Re\cot\pi a,\quad
 q=\Re\cot\pi b,\quad
 C_a=\Re\cot\pi(s+a),\quad C_b=\Re\cot\pi(s+b).
 \tag{4}
\]
The old outer cotangent bounds and elementary scalar estimates give
\[
 \frac{21}{20}<u<\frac52,\qquad
 \frac9{70}<p,q<\frac32,\qquad
 -\frac13<C_a,C_b<\frac{11}{20}.
 \tag{5}
\]
Here is an explicit verification of the new bounds. On (3),
\(\sin(2\pi\Re s)\ge\sqrt2/2>7/10\),
\(\cos(2\pi\Re s)\ge\cos(3\pi/10)>7/12\), and
\(\cosh(2\pi\Im s)<5/4\). Thus the denominator in the real
cotangent formula is less than \(2/3\), proving the lower bound
for \(u\). Its upper bound follows from
\(u\le\cot(\pi/8)=1+\sqrt2<5/2\).

The shifted real arguments lie between \(69/200\) and \(3/5\).
At a positive real cotangent, an imaginary displacement decreases
its value; at a negative one it increases it. Therefore
\[
 \cot(3\pi/5)\le C_a,C_b\le\cot(69\pi/200).
 \tag{6}
\]
The lower endpoint exceeds \(-1/3\), since
\(\tan(\pi/10)<770/2329<1/3\), using
\(\sin t\le t\), \(\cos t\ge1-t^2/2\), and
\(\pi<22/7\). For the upper endpoint, alternating sine and
cosine bounds at \(10833/10000<69\pi/200\) give
\(\sin(69\pi/200)>22/25\) and
\(\cos(69\pi/200)<12/25\). Its cotangent is consequently
less than \(6/11<11/20\). The bound
\(\cos(3\pi/10)>7/12\) follows, for example, from the
alternating cosine polynomial through degree six at \(33/35\).
The hyperbolic estimate is the one already proved in the fixed-contour
theorem.

## 2. The extra index factorial restores joint curvature

We first need a stronger diagonal estimate when a shifted cotangent
is positive:
\[
                  C_a>0\quad\Longrightarrow\quad p-C_a>3/10.
 \tag{7}
\]
Indeed, set \(t=\cot(\pi\Re a)\). Positivity of \(C_a\)
implies \(\Re a<3/8\), so
\(2/5<t<5/4\). For the latter upper bound, use
\(\tan v>v+v^3/3>4/5\) at
\(v=1727/2500<11\pi/50\).
The real cotangent formula and \(\cosh(2\pi\Im a)<4/3\)
give
\[
 p>\frac{6t}{t^2+7},\qquad
 C_a\le\frac{(1+\sqrt2)t-1}{1+\sqrt2+t}
       <\frac{(5/2)t-1}{5/2+t}.
 \tag{8}
\]
The difference between the last two rational expressions exceeds
\(3/10\). After multiplication by the positive denominator
\(10(t^2+7)(5/2+t)\), this assertion is
\[
 P(t):=-28t^3+\frac{125}{2}t^2-46t+\frac{35}{2}>0,
                         \qquad 2/5\le t\le5/4.
 \tag{9}
\]
Its derivative is
\(-84(t-2/3)(t-23/28)\). Hence its minimum is among the
values at \(2/5,2/3,5/4\); these are respectively
\(1827/250,341/54,95/32\), all positive. This proves
(7). The same proof applies to \(q-C_b\).

Since \(g''(z)=\pi\cot\pi z-\pi i\), the matrix
\(K=-\Re F''/\pi\) is exactly
\[
 K=\begin{pmatrix}
 3u-C_a-C_b&-C_a&-C_b\\
 -C_a&(1+\eta/2)p-C_a&0\\
 -C_b&0&\tfrac32q-C_b
 \end{pmatrix}.
 \tag{10}
\]
The chirp has zero real Hessian. Put
\(D_a=(1+\eta/2)p-C_a\), \(D_b=3q/2-C_b\).
Each exceeds \(9/70\): use (7) when the corresponding
\(C\) is positive, and (5) otherwise.

For either outer diagonal \(D=\lambda p-C\), where
\(\lambda\ge1\), its subtraction from the index Schur
complement costs
\[
 C+\frac{C^2}{D}
 \begin{cases}
 \le0,&C\le0,\\[1mm]
 <\displaystyle\frac{11}{20}+
           \frac{(11/20)^2}{3/10}=\frac{187}{120},&C>0.
 \end{cases}
 \tag{11}
\]
For \(C\le0\), the expression is \(C\lambda p/D\),
which proves its stated sign. Consequently
\[
 3u-C_a-C_b-\frac{C_a^2}{D_a}-\frac{C_b^2}{D_b}
 >3\frac{21}{20}-2\frac{187}{120}=\frac1{30}.
 \tag{12}
\]
Thus \(K\) is positive definite. Moreover,
\[
 \det K>\frac1{30}\left(\frac9{70}\right)^2,
                  \qquad \operatorname{tr}K<\frac{40}{3}.
 \tag{13}
\]
The trace estimate follows directly from (5), with both outer
coefficients bounded above by \(3/2\). For a positive
three-by-three matrix, the product of its two largest eigenvalues
is at most one quarter of its squared trace. Therefore
\[
 -\Re F''\succ\frac{729\pi}{58800000}I_3
       \succ\frac1{40000}I_3
       \succ\mu I_3,\qquad \mu=\frac1{1250000}.
 \tag{14}
\]
The factor \(\pi\) is retained in this conversion from \(K\)
to the phase Hessian. Combining (14) with the half-index theorem
proves the old common bound \(-\Re F''\succ\mu I_3\)
throughout
\([1/8,1/2]+i[-27/250,17/250]\), with the outer domain (2).

## 3. Keeping the original supporting plane

Let \((s_0,a_0,b_0)\) be the original actual reference and let
\(y_0=\Im s_0\). Define
\[
 \begin{split}
 M&=\Re F(s_0;a_0,b_0),\qquad
 p_a=\Re F_a(s_0;a_0,b_0),\quad p_b=\Re F_b(s_0;a_0,b_0),\\
 d_a&=\Re(a-a_0),\qquad d_b=\Re(b-b_0),\\
 B(a,b)&=M+p_ad_a+p_bd_b-\frac\mu2(d_a^2+d_b^2).
 \end{split}
 \tag{15}
\]
The outer heights stay fixed at their actual unselected values.
The original index equation is \(F_s(s_0;a_0,b_0)=0\).
Integrating the joint Hessian bound along the straight horizontal
segment from the reference gives
\[
 \Re F(v+iy_0;a,b)
 \le B(a,b)-\frac\mu2(v-\Re s_0)^2
 \le B(a,b),\qquad 1/8\le v\le1/2.
 \tag{16}
\]
Neither the reference constant nor its marginals have changed.

## 4. The complete enlarged contour

Use lower height \(-1/5\) and upper height \(5/4\). The
argument bounds from the
[asymmetric contour proof](research_mixed_horizontal_asymmetric_contour.md)
give, on the enlarged real interval and at every finite height,
\[
 -\frac{49\pi}{25}<\Im F_s(v+iy;a,b)<\frac{121\pi}{100}.
 \tag{17}
\]
For clarity, the four lower bounds after division by \(\pi\),
according to whether \(v+\Re a\) and \(v+\Re b\) are
above or below \(1/2\), are
\(-33/20,-49/25,-3/2,-181/100\). They follow from the
same original-log inequalities in that proof, with \(v\ge1/8\).
For the upper bound, the corresponding four bounds are
\(9/10,3/4,121/100,53/50\), with the ordering chosen by
which shifted arguments are below \(1/2\).

For \(y\ge1/2\), the sharper estimate is
\[
 -\Im F_s(v+iy;a,b)
       <\frac{33\pi}{20}+\frac{60}{7}e^{-2\pi y}.
 \tag{18}
\]
Indeed the limiting imaginary marginal is
\(\pi(-1+2v-2\Re b)\), whose minimum is
\(-33\pi/20\). The inverse-radius remainder estimate is
unchanged because the two outer height bounds have not changed.
Its integral from \(1/2\) to infinity is less than \(1/14\).

At the lower side, integrate (17) from \(-1/5\) to \(y_0\)
and subtract the original alias penalty \(2\pi/5\):
\[
 \Re F(v-i/5)-2\pi/5
 <\Re F(v+iy_0)-\frac{1893\pi}{25000}<B.
 \tag{19}
\]
At the upper side, integrate (17) to \(1/2\), then (18) to
\(5/4\), and subtract the penalty \(5\pi/2\). Since
\(y_0\ge-27/250\), this gives
\[
 \begin{split}
 \Re F(v+5i/4)-5\pi/2-\Re F(v+iy_0)
 &<\left(\frac{49}{25}\frac{76}{125}
            +\frac{33}{20}\frac34-\frac52\right)\pi+\frac1{14}\\
 &=-\frac{3541\pi}{50000}+\frac1{14}<-\frac7{50}.
 \end{split}
 \tag{20}
\]
The last inequality uses only \(\pi>3\).

For either real cut, the vertical upper alias has derivative
less than \(-\pi/25\), while the vertical lower alias has
derivative greater than \(79\pi/100\). This follows from
(17) after adding the respective Fourier penalties. Both are
therefore bounded by their real-cut values. The zero-mode joins
between height zero and \(y_0\) are bounded by their endpoints,
because (14) and the old Hessian bound give vertical convexity
throughout those joins.

Every factorial argument on this larger fixed rectangle still has
real part strictly between zero and one. The exact factorial
interpolation theorem used in the asymmetric proof permits every
fixed compact imaginary-height interval. Thus this deformation
crosses no interpolation pole, retains the original residues and
the central coefficient \(+N\), and keeps both level parities.
Polynomial prefactors and half-grid rounding use one prescribed
arbitrarily small exponential tolerance, as before.

## 5. The resulting three-row comparison

Let \(R(u)=\mathcal R_1(u;a,b)\) be the complete allocated
real-row rate from the asymmetric contour theorem. At actual outer
heights, the [right-tail theorem](research_mixed_right_tail_endpoint_bound.md)
still gives its maximum on \([1/2,1]\) at \(1/2\) or \(1\).
The left-tail derivative remains greater than \(1/2\) on
\((0,3/20]\), so its maximum on \([0,1/8]\) is at \(1/8\).
Consequently the same literal finite kernel, with its actual outer
halfweights, has the complete upper bound
\[
 C_\tau N^A\exp N\left\{
    \max\bigl(B,R(1/8),R(1/2),R(1)\bigr)+\tau\right\},
                                  \qquad \tau>0.
 \tag{21}
\]
The meaning of the fixed-height and physical Fourier hypotheses is
unchanged. In particular no estimate for derivatives transverse to
this real horizontal family is inferred.

The new left-row comparison is uniformly easier:
\[
                  R(1/8)<R(3/20)-\frac1{80}.
 \tag{22}
\]
This follows by integrating the already proved derivative bound
over an interval of length \(1/40\). Both rates have the same
outer allocations and are compared with the same plane (15).
For any family where the old left-cut excess is at most \(1/80\),
the new left cut is therefore controlled by that plane. No such
uniform excess bound over all actual references is assumed here.

The [positive old-cut example](research_mixed_left_cut_independent_reference_obstruction.md)
therefore need not be excluded by a new geometric condition merely
to make progress: the original contour itself admits this smaller
cut. The remaining tasks are the calibrated comparison at the new
cut, the remaining half-row region, and the last row, followed by
the full boundary assembly for the ordinary closure.
