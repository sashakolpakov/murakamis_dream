# Fixed-reference phase control for the first cap on the full plateau

Research deduction, 5 November 2026. The original first-cap phase is
jointly horizontally concave on the entire existing private contour
rectangle and the full outgoing plateau. This gives the required
supporting plane for its fixed-reference zero-mode horizontal segment,
without constructing a critical point at any new outgoing target.
The full real tails still reduce to the two old cuts and the same
literal endpoint ceilings. Four explicit calibrated comparisons remain
for the complete finite cap: two real cuts and two horizontal aliases.
Their signs are not asserted here. No numerical execution is used.

## 1. Original source, reference and allocated phase

Use the literal polynomial
\[
 U_{\alpha,N}(w,X)=\sum_{i=0}^{N-1}
      \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\alpha}},
 \quad \alpha=0,1,\quad r=e^{-2\pi i/N},\quad X=e^{-2\pi iz}.
 \tag{1}
\]
Every private row is retained. The canonical retained-row interpolant,
its scalar factors and original logarithmic lift are precisely (4)
and (7) of [the complete-current cap criterion](research_mixed_cap_outer_contour_reduction.md).
Its endpoint packet is valid on
\[
 E_c=[.27,.49]+i[-.055,.04].
 \tag{2}
\]
Write \(S(e)=F(e,u_c(e))\) for the actual endpoint action and
\[
\begin{split}
 \Psi_\alpha(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),\\
 \Xi_\alpha(e,z)&=\Psi_\alpha(e,z)-\frac\alpha2g(z).
\end{split}
 \tag{3}
\]
The second line allocates one outgoing Fourier halfweight. Its
physical interpretation for \(\alpha=1\) uses the actual negative
outgoing height, not arbitrary positive auxiliary heights.

Fix an actual outgoing reference \(z_*=a+ic\), its private root
\(e_*=b+ih_*\), and the original cap action
\(L_\alpha(z)=\mathcal T_\alpha(z,-2)-\alpha g(z)/2\).
The target is \(z=y+ic\), with independent \(y\in P=[.22,.45]\).
The exact attached images have \(-.072<c<.021\) for type three
and \(-.108<c<-.020\) for type four. In particular all targets
belong to
\[
                        Z=P+i[-.108,.021].
 \tag{4}
\]
All primitive arguments are regular on \(E_c\times Z\): in
particular \(.49\le\Re(e+z)\le.94\). The enlarged product
does not enlarge the endpoint coefficient's domain (2).

## 2. A quantitative joint Hessian on the enlarged product

**Lemma 1.** On \(E_c\times Z\), both types satisfy
\[
                -\Re\Xi_\alpha''\succ\frac\pi{200}I_2.
 \tag{5}
\]
The same bound holds for the bare phase \(\Psi_\alpha\).

*Proof.* The complete endpoint certificate supplies throughout (2)
\[
 .17<\Re u_c<.28,\quad .001<\Im u_c<.1,
 \quad .01<\Re(e-u_c)<.32,
 \quad |\Im(e-u_c)|<.155.
 \tag{6}
\]
Here the strict lower difference follows from its real cut
\(\Re u_c<\Re e-.01\), not from independent rectangular
subtraction. Put
\[
 A=\Re(2\tan\pi u_c+3\cot\pi u_c),\qquad
 B=\Re\cot\pi(e-u_c).
 \tag{7}
\]
The cotangent and tangent formulas give \(A>2\):
\(\sin(2\pi\Re u_c)>4/5\),
\(|\cos(2\pi\Re u_c)|<1/2\), and
\(\cosh(2\pi\Im u_c)<5/4\) make each of the two real
parts greater than \(16/35\).

The elementary estimates
\[
 \cosh(.31\pi)<38/25,\qquad
 \cos(.22\pi)>77/100,\qquad
 \sin(.02\pi)>3/50
 \tag{8}
\]
imply \(B>1/42\) on (6), because its denominator is less
than \(38/25+1=63/25\). The numerator has its minimum at
the smaller real endpoint; the other endpoint gives
\(\sin(.64\pi)>3/50\).
For explicit rational proofs of (8), use \(3.14<\pi<22/7\).
The positive-series bound
\(\cosh x\le1+x^2/2+x^4/[24(1-x^2/30)]\) at
\(x=341/350\) is less than \(38/25\).
The lower cosine polynomial
\(1-x^2/2+x^4/24-x^6/720\) at \(x=121/175\)
is greater than \(77/100\). Finally
\(x-x^3/6\), using \(x>.0628\) and \(x<.063\),
is greater than \(3/50\).

The endpoint negative real Hessian is
\(\pi\{A\,du^2+B(de-du)^2\}\). Replacing \(A,B\)
by \(2,1/42\) gives a positive matrix whose determinant divided
by trace is \(1/43\). The accretive Schur argument from the
original cap criterion consequently gives
\[
                         -\Re S''>\pi/43.
 \tag{9}
\]
If \(\Re(e+z)<1/2\), then \(.27\le\Re e<.28\), so
the stronger difference range is
\(.01<\Re(e-u_c)<.11\). Its cosine exceeds \(77/100\);
(8) now makes its denominator less than \(3/4\), and
therefore \(B>2/25\). The same matrix argument gives the
stronger bound \(-\Re S''>2\pi/27\) in this small corner.

Set \(s=-\Re S''/\pi\), \(p=\Re\cot\pi z\),
\(q=\Re\cot\pi e\), and \(C=\Re\cot\pi(e+z)\).
Both \(p,q\) are positive, and \(p>9/70\), using
\(\sin(2\pi\Re z)>3/10\) and
\(\cosh(.216\pi)<4/3\). The negative real Hessian of (3),
divided by \(\pi\), is
\[
 \begin{pmatrix}
 s+\alpha q-C&-C\\
 -C&(1+\alpha/2)p-C
 \end{pmatrix}.
 \tag{10}
\]
If \(C\le0\), this is the positive diagonal
\(\operatorname{diag}(s+\alpha q,(1+\alpha/2)p)\) plus
a positive rank-one matrix. Its least eigenvalue exceeds \(1/43\).
If \(C>0\), the small corner just considered applies and
\(C\le\cot(.49\pi)=\tan(.01\pi)<1/30\).
The two Gershgorin row margins exceed
\[
 2/27-1/15=1/135,\qquad 9/70-1/15=13/210.
 \tag{11}
\]
Both exceed \(1/200\). Dropping the extra outgoing halfweight
only removes a nonnegative diagonal term; the same estimates with
its coefficient replaced by one prove the bare case as well.
This proves (5). \(\square\)

## 3. The complete zero-mode horizontal segment is paid

Let \(\kappa_*=1/2500000\), \(d=y-a\), and define
\[
 B_L(z_*;y)=\Re L_\alpha(z_*)+
                  \Re L_\alpha'(z_*)d-\kappa_*d^2.
 \tag{12}
\]
At \((e_*,z_*)\), the private marginal of (3) is zero and
its outgoing marginal is \(L_\alpha'(z_*)\). The horizontal
segment in the two variables from this reference to
\((x+ih_*,y+ic)\) stays in (2), (4). Twice integrating (5)
therefore proves
\[
\begin{split}
 \Re\Xi_\alpha(x+ih_*,y+ic)
 &\le \Re L_\alpha(z_*)+\Re L_\alpha'(z_*)d
                      -\frac\pi{400}\{(x-b)^2+d^2\}\\
 &\le B_L(z_*;y)-\frac\pi{400}(x-b)^2,
                 \qquad .27\le x\le.49.
\end{split}
 \tag{13}
\]
The last inequality uses \(\pi/400>\kappa_*\).
This supplies the whole main horizontal current at every outgoing
plateau target. It needs only the original reference critical point.
In particular no moving cap branch on \(P\), or finite packet at
such a moving branch, has been assumed.

## 4. What remains for the finite source

All four old contour sides remain within the endpoint packet (2).
The exact full-cap criterion may therefore be used with reference
plane (12), rather than a moving critical value. Its outstanding
calibrated comparisons are precisely
\[
\begin{split}
 \Re\Xi_\alpha(c_0,y+ic)&\le B_L(z_*;y)-\delta,
                      &&c_0=.27,.49,\\
 \Re\Xi_\alpha(x+.04i,y+ic)-.08\pi
                  &\le B_L(z_*;y)-\delta,
                      &&.27\le x\le.49,\\
 \Re\Xi_\alpha(x-.055i,y+ic)-.11\pi
                  &\le B_L(z_*;y)-\delta,
                      &&.27\le x\le.49.
\end{split}
 \tag{14}
\]
Here one seeks a strict uniform \(\delta>0\) on the actual
correlated outgoing references and all \(y\in P\).
The existing cut certificate only tests \(y=\Re z_*\).
The existing alias-curvature cover uses the attached outgoing
rectangles, not all of (4). Neither source may silently be enlarged
to assert (14).

The proof of Lemma 1 also gives vertical convexity in the private
coordinate on the whole enlarged product. Hence real-cut tests in
(14), the strict endpoint loss in (13), and the two horizontal alias
tests would control every join and half-grid vertical alias exactly
as in the original current decomposition. No additional target-root
condition is required.

All these are strongly concave real-target tests: the cuts have one
free target \(y\), and each alias has \((x,y)\). After subtracting
(12), their Hessians are bounded above by
\(-\mu I\) for any \(0<\mu<\pi/200-2\kappa_*\).
Thus the already validated clipped-gradient upper rule can eliminate
their entire target intervals at a fixed rational trial; a target
grid is unnecessary. This observation supplies no numerical sign
or completed cover.

## 5. The complete real tails on the full outgoing plateau

The tail extension uses the actual typed heights:
\(-.072\le c\le.021\) for \(\alpha=0\), and
\(-.108\le c\le-.020\) for \(\alpha=1\).
Write \(\lambda(s)=\Re S(s)\). The original full-row rate is
\[
 R_\alpha(s,z)=\lambda(s)+I_z(s)-\alpha J(s),\qquad
 I_z(s)=\int_0^s\log|1-e^{-2\pi i(z+t)}|\,dt.
 \tag{15}
\]
It is the rate of the literal cap summand, with all revived rows
retained. The compact real-index endpoint packet is independent of
the outgoing target; its product estimate is zero-safe when an
outgoing numerator vanishes.

**Lemma 2.** Uniformly over these typed heights and \(y\in P\),
the complete finite lower and upper private tails have upper rates
\[
 \max\{R_\alpha(.27,z),1/4\}+\eta,\qquad
 \max\{R_\alpha(.49,z),3/4\}+\eta,
 \tag{16}
\]
respectively, for every \(\eta>0\), with polynomial prefactors
and a fixed ordinary-color neighborhood. Both parities and fixed
ordinary derivatives are included.

*Proof.* Retain the exact scalar and endpoint inputs of
[the full real-tail theorem](research_mixed_outer_cap_real_tails.md).
For \(0<s\le.27\), one now has \(.22\le y+s\le.72\),
whose cosine of twice the angle is less than \(1/5\).
The smoothed radius \(v=e^{-2\pi|c|}\) exceeds \(1/2\).
Consequently
\(|1-ve^{-2\pi i(y+s)}|^2=1+v(v-2\cos2\pi(y+s))>1\).
The actual logarithm also has the nonnegative term \(2\pi c_+\).
The old inequalities \(\lambda'(.27)>27/50\),
\(\lambda''<0\), and \(J'(.27)<41/100\) still prove
\(R_\alpha'>13/100\) throughout the lower compact tail.

For \(s\ge1/2\), the exact endpoint identity
\(\lambda'-J'\le-\log4\) remains unchanged. At type four,
\(c<0\) makes the numerator modulus at most two, and hence
\(R_1'\le-\log2\). At type three, for every \(y\in P\),
\[
 \sin(\pi s)|\sin\pi(s+y)|\le\cos(.22\pi).
 \tag{17}
\]
Before \(s+y=1\), the product decreases from \(\cos\pi y\);
after that wall its magnitude is at most \((1-\cos\pi y)/2\le1/2\).
The exact same derivative identity therefore gives
\[
 e^{R_0'}\le e^{.021\pi}
       \sqrt{\cos^2(.22\pi)+\sinh^2(.072\pi)}<1.
 \tag{18}
\]
For example \(e^{.021\pi}<11/10\),
\(\cos(.22\pi)<4/5\), and \(\sinh(.072\pi)<1/4\)
already prove the strict last inequality.

For the bridge \(.49\le s\le.5\), retain
\(\lambda'(s)<-3/5\), \(J'(s)>3/5\).
The type-four numerator estimate again suffices. At type three,
\(.71\le s+y\le.95\), and the elementary bounds
\[
 \sin(.29\pi)<4/5,\quad
 e^{.021\pi}<15/14,\quad
 \sinh(.072\pi)<7/30
 \tag{19}
\]
give numerator modulus less than
\(2(15/14)\sqrt{16/25+49/900}=25/14<e^{3/5}\).
Thus \(R_0'<0\) on the bridge too. The exponential bound in
(19) follows from \(.021\pi<33/500\) and
\(e^x\le(1-x)^{-1}\). The hyperbolic sine bound follows from
\(.072\pi<23/100\) and
\(\sinh x\le x/(1-x^2/6)\). A fifth-degree upper sine
polynomial at \(.29\pi<319/350\) gives the first bound.
At numerator zeros, integrate on the adjoining intervals and use
the continuous integrated logarithm. No zero row is discarded.

It remains to include the true index endpoints. For \(s\le.01\)
the old literal Newton entropy estimate and
\(|p_i(X)|\le(1+e^{.042\pi})^i\) are unchanged, giving
rate below \(1/4\). For \(s\ge.99\), the exact product
\[
 p_i(X)=\frac{1-X^N}{\prod_{j=i+1}^{N}(1-r^jX)}
 \tag{20}
\]
has denominator angles in \([.21,.45]\). Minimizing over their
radial moduli bounds every factor below by \(19/20\): when its
cosine is positive use \(\sin(.42\pi)>19/20\), and otherwise
use one. Thus
\(|p_i(X)|\le2e^{2\pi Nc_+}(20/19)^{N-i}\).
The unchanged endpoint entropy ceiling is less than \(3/5\),
and the remaining reciprocal factorial has nonpositive rate here.
The resulting upper rate is at most
\[
 \frac35+\frac{21\pi}{500}+\frac1{100}\log(40/19)
                                  <\frac{37}{50}<\frac34.
 \tag{21}
\]
Use \(\pi<22/7\) and \(\log(40/19)<4/5\) for the first
strict inequality. The same zero-safe finite product estimates,
ordinary-color perturbation, and Cauchy argument as in the original
tail theorem now prove (16). \(\square\)

## 6. Literal endpoint ceilings and the exact remaining tests

The endpoint ceilings in (16) are below the desired supporting
plane for all outgoing plateau targets; they create no additional
comparison. To see this before the optional outgoing halfweight,
write \(T=\mathcal T_\alpha(\cdot,-2)\). At the actual reference,
\[
 T'(z_*)=J'(e_*+z_*)-J'(z_*)-i\pi e_*.
 \tag{22}
\]
The exact endpoint rectangles give
\(.579<\Re(e_*+z_*)<.829\),
\(|\Im(e_*+z_*)|<.159\),
\(.246<\Re z_*<.391\), and \(|\Im z_*|<.108\).
They imply \(\sin\pi\Re(e_*+z_*)>1/2\),
\(|\sin\pi z_*|<16/15\),
\(|\sin\pi(e_*+z_*)|<8/7\), and
\(|\sin\pi z_*|>2/3\). Consequently
\[
                    -1<\Re T'(z_*)<1.
 \tag{23}
\]
For the lower bound use \(\log(15/32)>-4/5\) and
\(\pi\Im e_*>-.17\); for the upper use
\(\log(12/7)<3/5\) and \(\pi\Im e_*<.12\).
These logarithm inequalities follow from the first four positive
terms of their exponential series. The two hyperbolic cosine
bounds follow from the same positive-series estimate as (8).

Since \(\Re T(z_*)>1\) and \(|y-a|<51/250\), the bare
plane is bounded below by
\[
 \Re T(z_*)+\Re T'(z_*)(y-a)-\kappa_*(y-a)^2
                         >79/100>3/4.
 \tag{24}
\]
Adding the actual outgoing halfweight changes the defect relative
to (12) by the nonpositive convex remainder
\(-\alpha\{\Re g(y+ic)-\Re g(z_*)-\Re g'(z_*)(y-a)\}/2\).
Thus both literal endpoint ceilings are paid after allocation too.

It follows that (14), together with the already proved zero-mode
bound (13), is a sufficient finite list for the **whole** cap's
supporting plane on \(P\). Lemma 2 controls every real tail;
vertical convexity controls all joins and vertical aliases; the
canonical interpolant retains the exact residue coefficient and
both parities. One total source/color tolerance gives the full cap
upper bound. This is a statement about the original finite sum,
not only a critical action or an inner error before an outer sum.

Combined with the ordinary and full terminal planes, such a pass
would extend [the plateau-slab theorem](research_mixed_terminal_three_plateau_slab.md)
to the entire unselected plateau for every word length ending in
three. The new proved ingredients are the joint curvature (5),
the full horizontal zero-mode bound (13), the complete tail reduction
(16), and the uniform endpoint budget (24). The signs of the two
calibrated cut and two horizontal-alias comparisons (14) remain open.
