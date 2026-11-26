# Three shared weight assignments for every even cyclic diagram

Let \(m\ge6\) be even. The original sphere has oriented triangles
\((N,v_j,v_{j+1})\), \((S,v_{j+1},v_j)\), with indices modulo \(m\).
North matching spokes are \(Nv_j\) for odd \(j\), and south matching
spokes are \(Sv_j\) for even \(j\). The original ordered homogeneous
coupons, in the argument order \((x,b,c,y)\), are
\[
 (N,v_{j-1},v_{j+1},v_j)\quad(j\ \mathrm{odd}),\qquad
 (S,v_{j+1},v_{j-1},v_j)\quad(j\ \mathrm{even}).           \tag{1}
\]
Mark the unmatched edge \(v_0v_1\); those two face weights are exactly
zero. All others have the original target \(d=N_{\!q}-1\), where
\(N_{\!q}\) is the quantum level. No tangle or crossing is inserted.

This note proves that three explicit whole shared vectors satisfy every
surviving anchored radius test, with a uniform action margin \(7/100\).
The conclusion holds for every fixed even \(m\); subsequent analytic
and geometric filling thresholds may depend on \(m\).

## The triangle potential used below

For nonnegative weights \(w=(w_1,w_2,w_3)\), not all zero, put
\[
 Q(w)=\max_{\substack{\alpha_i\ge0\\\sum_i\alpha_i=1/2}}
 \sum_{i=1}^3\left\{
  \frac{\Lambda(\pi\alpha_i)+\Lambda(\pi/2-\pi\alpha_i)}{\pi}
              +\alpha_i\log w_i\right\},\qquad
 \Lambda(t)=-\int_0^t\log|2\sin u|\,du.
\]
At a zero weight, restrict its \(\alpha_i\) to zero and give
\(\alpha_i\log w_i\) the value zero. If at least two weights are
positive, the unique maximizer is
\[
 \alpha_i=\frac1\pi\arctan\frac{w_i}{D},\qquad
 D=\sqrt{w_1w_2+w_2w_3+w_3w_1}.
\]
The entropy derivative is \(\log\cot(\pi\alpha_i)\), which gives
this formula by the Lagrange multiplier equation. If only one weight
is positive, \(Q(w)=\tfrac12\log w_i\).
In particular, \(Q(tw)=Q(w)+\tfrac12\log t\), and its derivative
with respect to \(\log w_i\) is \(\alpha_i\).
The [source normalization proof](actual_triangle_entropy_algebraic_balance.md)
identifies this function with the original triangle polynomial's rate.

The [geometric and topological proof](actual_cyclic_three_braid_volume.md)
constructs the labeled packing used below and identifies the original
filled diagram as a closed three-strand braid. The
[finite-sector theorem](general_morse_sector_cover_volume.md) supplies
the transfer from the inequalities proved here to the full invariant.

## 1. The action and the three vectors

Write
\[
 F(r)=Q(1,r,0),\quad a=\frac94,\quad C=\frac{27}4,\quad
 \theta=\frac\pi m,\quad
 k_j=\frac{\cos\theta}{\sin^2\theta}
       \{\cos\theta-\cos((2j-1)\theta)\}.              \tag{2}
\]
The complete marked curvature vector is \(N=S=1\), with rim weights
\(k_j\), and \(k_0=k_1=0\). These are curvatures, not Euclidean radii.
The complete geometric action is
\[
 \Phi_m=2\sum_{j=0}^{m-1}Q(1,k_j,k_{j+1})
                         -\sum_{j=2}^{m-1}\log k_j.
 \tag{3}
\]
This is the complete shared coefficient action and
\(2\pi\Phi_m\) is the volume of the original augmented complement.
It follows from its labeled simple-sphere packing, not from an
independent local-volume estimate.

Set
\[
 \lambda=\frac{a}{k_2}=\frac9{16\cos^2\theta},\qquad
 w_j=\lambda k_j,\qquad L_N=L_S=1.                    \tag{4}
\]
Call this symmetric whole vector \(W\). In particular,
\[
 w_2=w_{m-1}=a,\qquad
 c:=w_3=w_{m-2}=a(4\cos^2\theta-1)\in[9/2,C].
 \tag{5}
\]
The other two vectors are
\[
 W^{(1)}:\ w_2\ \text{replaced by }1,\qquad
 W^{(0)}:\ w_{m-1}\ \text{replaced by }1,              \tag{6}
\]
with every other weight unchanged. Use \(W^{(1)}\) for anchor
\(j=1,\mathrm L\), \(W^{(0)}\) for \(j=0,\mathrm L\), and \(W\) for
all other surviving anchors. Each vector retains both protected
zeros and every other shared occurrence of a face.

For a coupon define
\[
 X_j=Q(x_j,b_j,y_j)+Q(x_j,c_j,y_j),\quad
 H_j=\max(X_j,\{\log b_j:b_j>0\},\{\log c_j:c_j>0\}).
\]
For a positive overloaded middle, the one-sided rates are
\[
 A_{j,\mathrm L}=\max(\log c_j,Q(x_j,b_j,y_j)+\tfrac12\log c_j),
 \quad
 A_{j,\mathrm R}=\max(\log b_j,Q(x_j,c_j,y_j)+\tfrac12\log b_j).
\]
A protected overloaded middle gives no surviving anchor. The assertion is
\[
 A_{j,s}(L^{j,s})+\sum_{i\ne j}H_i(L^{j,s})
       -\sum_{f\ \mathrm{ordinary}}\log L_f^{j,s}
       <\Phi_m-\frac7{100}.                          \tag{7}
\]

## 2. A uniform bound for the change in complete action

For \(0<t\le1\), scale only the ordinary rim weights by \(t\) and put
\[
 P(t)=2\sum_jQ(1,tk_j,tk_{j+1})
                     -\sum_{j=2}^{m-1}\log(tk_j).
\]
Then \(P(1)=\Phi_m\). For the pole angle in the \(j\)-th triangle set
\[
 \alpha_j(t)=
 \arctan\frac1{\sqrt{t(k_j+k_{j+1})+t^2k_jk_{j+1}}}.
 \tag{8}
\]
The triangle \(j=0\) is monomial and has
\(\alpha_0(t)=\pi/2\). All other denominators are positive.
The original complete star equation is
\(\sum_j\alpha_j(1)=\pi\), so
\(\sum_{j\ne0}\alpha_j(1)=\pi/2\).

If \(D^2=t(u+v)+t^2uv\), differentiation gives
\[
 -\frac{d\alpha}{d\log t}
 =\frac{t(u+v)+2t^2uv}{2D(1+D^2)}
 \le \sin\alpha\cos\alpha\le\alpha.                  \tag{9}
\]
This includes a single zero rim entry. Integrating (9) from \(t\) to
one gives \(\alpha_j(t)\le\alpha_j(1)/t\). The logarithmic derivative
of \(Q\) at a positive weight is its triangle angle divided by \(\pi\).
Since each triangle has total angle \(\pi/2\),
\[
 \frac{dP}{d\log t}
 =2-\frac2\pi\sum_j\alpha_j(t)
 \ge 1-\frac1t.
\]
Therefore
\[
 P(\lambda)-\Phi_m
 \le \lambda^{-1}-1+\log\lambda
 \le D_0:=\frac{16}9-1+\log\frac9{16}<0.203,           \tag{10}
\]
because \(9/16<\lambda\le3/4\). This bounds the entire coupled
action change, independently of the number of triangles.

## 3. All anchors away from the marked edge

The elementary trigonometric identity
\[
 k_j=\frac{2\cos\theta}{\sin^2\theta}
                   \sin(j\theta)\sin((j-1)\theta)
\]
shows that, for \(3\le j\le m-2\),
\[
 \frac13\le\frac{w_{j-1}}{w_j}\le2,\qquad
 \frac13\le\frac{w_{j+1}}{w_j}\le2.                  \tag{11}
\]
Indeed the ratios reduce to
\(\sin((j-2)\theta)/\sin(j\theta)\) and
\(\sin((j+1)\theta)/\sin((j-1)\theta)\). They are monotone in \(j\).
At the extremes use
\(\sin(3\theta)/\sin\theta\le3\) and
\(\sin(4\theta)/\sin(2\theta)=2\cos(2\theta)\le2\).

The function \(Q\) is nondecreasing in each weight, including the
limit of a zero weight. Its logarithmic derivative lies between
zero and \(1/2\). Thus \(F\) is increasing, while
\(F(r)-\log r\) and \(F(r)-\tfrac12\log r\) are decreasing.
Dropping the positive pole entry and using homogeneity, (11) gives
\[
 \begin{split}
 X_j-\log\max(w_{j-1},w_{j+1})
   &\ge F(1/3)+F(2)-\log2=:B_{\mathrm{int}},\\
 Q(1,w_{j\pm1},w_j)-\tfrac12\log w_{j\pm1}
   &\ge F(2)-\tfrac12\log2=:C_{\mathrm{int}}.
 \end{split}                                       \tag{12}
\]
The constants satisfy \(B_{\mathrm{int}}>0.43\) and
\(C_{\mathrm{int}}>0.42\). Consequently \(H_j=X_j\) and
\(X_j-A_{j,s}\ge\min(B_{\mathrm{int}},C_{\mathrm{int}})\).

At \(j=2,m-1\), the rim outer weight is \(a\), and the middle weights
are \(0,c\), with \(c\le C\). Monotonicity of
\(Q(1,c,a)-\log c\) and \(Q(1,c,a)-\tfrac12\log c\) gives
\[
 \begin{split}
 X_j-\log c&\ge F(a)+Q(1,C,a)-\log C=:B_{\mathrm{near}}>0.28,\\
 Q(1,c,a)-\tfrac12\log c
       &\ge Q(1,C,a)-\tfrac12\log C=:C_{\mathrm{near}}>0.42.
 \end{split}                                       \tag{13}
\]
This proves \(H_j=X_j\) and bounds its sole surviving anchor loss.

At \(j=0,1\), \(X_j=F(a)\) and its only nonzero middle is \(a\).
The fixed inequality \(F(a)>\log a\) shows \(H_j=X_j\).
The anchor at these two coupons is treated in §4.

Thus every unanchored rate at \(W\) is its complete triangle rate.
Combining (10), (12), (13), and the sharper certified differences
\[
 B_{\mathrm{near}}-D_0>0.07,\quad C_{\mathrm{near}}-D_0>0.07,\quad
 B_{\mathrm{int}}-D_0>0.07,\quad C_{\mathrm{int}}-D_0>0.07        \tag{14}
\]
proves (7) for every anchor except \(0\mathrm L,1\mathrm L\).

## 4. The two boundary anchors

Consider \(1\mathrm L\), and replace \(w_2=a\) by \(1\).
Its anchored rate is now zero, while its complete rate is \(F(1)\).
Only the two triangle types containing \(v_2\) change. Since each
occurs once at each pole, the complete-action change from \(W\) is
\[
 T(c)=2\{F(1)-F(a)+Q(1,1,c)-Q(1,a,c)\}+\log a.
 \tag{15}
\]
It is increasing in \(c\): the derivative with respect to \(\log c\)
of the difference of the two \(Q\)'s is positive, because increasing
the other weight from \(1\) to \(a\) increases the triangle denominator
and decreases the angle at \(c\).

At coupon \(j=2\), the complete rate is \(F(1)+Q(1,1,c)\).
The excess of its envelope over this rate is
\[
 E(c)=\max(0,\log c-F(1)-Q(1,1,c))\le E(C).            \tag{16}
\]
The expression after zero is increasing, since the logarithmic
derivative of \(Q\) is less than \(1/2\).
At coupon \(j=3\), one middle is now \(1\), its outer rim is \(c\),
and its other middle \(z=w_4\) satisfies \(z/c\le2\).
It has no envelope excess, because
\[
 X_3-\log\max(1,z)
 \ge F(4/27)+F(2)-\log2>0.32.                        \tag{17}
\]
Here \(c\le27/4\), \(z\ge1\), and the same monotonicity as in (12)
was used. All other coupons are unchanged and have zero excess.

The total anchored cost is consequently at most
\[
 P(\lambda)+T(C)+E(C)-F(1).
\]
The fixed saving
\[
 S_0=F(1)-T(C)-E(C)>0.37,\qquad S_0-D_0>0.16           \tag{18}
\]
proves (7) for \(1\mathrm L\). Reflection \(j\mapsto1-j\), together
with exchange of the two pole labels, identifies the corresponding
rate expressions for \(0\mathrm L\) and \(W^{(0)}\). This equality
uses the displayed scalar symmetric \(Q\) formulas only; it does
not replace or reflect an ordered quantum coupon.

## 5. Certification of the fixed constants

The [portable verifier](../experiments/verify_cyclic_braid_constants.py)
encloses the fixed constants in (10), (12), (13), (17), and (18),
together with \(F(9/4)-\log(9/4)>0\). Run it from the repository root:

~~~sh
python3 experiments/verify_cyclic_braid_constants.py --check-reference
~~~

It uses only Python's standard library. All interval endpoints are
rational, with outward integer rounding. The
[stored bounds](../experiments/cyclic_braid_constant_bounds.json)
record each lower bound and its rational threshold. The program samples
no diagram sizes and uses no optimizer. Sections 2–4 prove the assertion
for every even size; this finite calculation certifies their constants.

For completeness, the analytic enclosures are as follows. Square roots
are enclosed by integer square roots after scaling. Repeatedly using
\[
 \arctan x=2\arctan\frac{x}{1+\sqrt{1+x^2}}
\]
reduces the argument to \([0,1/2]\). The alternating Taylor series then
has remainder bounded by its first omitted term. Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du
 =t\log(2\pi t)-t-
   \sum_{n=1}^{20}\frac{\zeta(2n)t^{2n+1}}{n(2n+1)}+R(t),
 \qquad 0<t<\tfrac12.
\]
Here \(\zeta(s)=\sum_{k\ge1}k^{-s}\) is the Riemann zeta function.
Euler's sine product gives this convergent expansion, and
\(1<\zeta(2n)<2\) gives the explicit remainder enclosure
\[
 -\frac{2t^{43}}{21\cdot43(1-t^2)}\le R(t)\le0.
\]
The shared interval engine supplies rational bounds for the logarithm,
\(\pi\), and the twenty zeta constants. At the maximizing angles,
\[
 Q(w)=\sum_{w_i>0}
       \{-J(\alpha_i)-J(1/2-\alpha_i)+\alpha_i\log w_i\}.
\]
This evaluates exactly the potential used in the proof, without a
normalization change. The monomial case is evaluated separately.

The resulting strict bounds include
\[
\begin{array}{c|c}
\text{quantity}&\text{certified bound}\\ \hline
D_0&<203/1000\\
F(9/4)-\log(9/4)&>0\\
B_{\mathrm{near}}&>28/100\\
C_{\mathrm{near}}&>42/100\\
B_{\mathrm{int}}&>43/100\\
C_{\mathrm{int}}&>42/100\\
F(4/27)+F(2)-\log2&>32/100\\
S_0&>37/100.
\end{array}
\]
The verifier also directly encloses the differences in (14) and (18).
It verifies that the positive branch of \(E(C)\) is the one used.

## 6. Filling and the knot condition

For cyclic boundary sides \(xb,by,yc,cx\), the untwisted pairs are
\((0,3),(1,2)\), and either signed half twist has pairs
\((0,2),(1,3)\). In the all-even opposite-offset diagram the main
curves are exactly the north-spoke circle, the south-spoke circle,
and the equatorial circle. Making one north box and one south box
odd merges these three into one. All other boxes remain even.
This gives an explicit knot pattern for every even \(m\), with
independent choices of signs at both odd boxes.

The global weighted one-sided envelope and the complete CROSS bound
now yield, at the original shared face targets,
\[
 \|S_{N_{\!q},\mathrm{full}}-S_{N_{\!q},\mathrm{CROSS}}\|_{[-2,2]^m}
 \le \exp\{N_{\!q}(\Phi_m-\eta)+o(N_{\!q})\},
 \qquad 0<\eta<7/100.                               \tag{20}
\]
The finite Hermite insertion bound of
[the finite filling norm](actual_uniform_filling_supremum_bound.md) preserves this exponent for
each fixed signed power vector. The nonzero all-CROSS theorem
[the Morse geometric-period theorem](actual_morse_cross_filling_period.md) and the original metric/action
identification [the original metric and action theorem](actual_morse_geometric_contribution.md) apply to this
same simple matched sphere. For independently sufficiently long
powers of the chosen parities, their filled action is within
\(\eta/2\) of \(\Phi_m\); the full error is exponentially smaller.
Hence the full original invariant has the hyperbolic-volume limit
of the original filled knot.

No fan is added. The proof establishes a family of original
presentations and makes no classification claim excluding other
Conway presentations of the same knots.
