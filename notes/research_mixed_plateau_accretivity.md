# Accretivity on the larger mixed-source plateau

Research proof, 4 November 2026. Frozen manuscripts and completed
certificates are unchanged.

The full conditional packets already exist on the independent transition
products. This note proves strict real concavity of their effective phase
and evaluates the unaliased integral on the whole constant-height plateau
\([.22,.45]^m\). Selected aliases and curved taper portions remain separate.

## 1. A general conditional-phase criterion

Let \(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\),
with the original logarithmic branches, and put
\[
 V(s,a)=g(s+a)-g(s)-g(a).
 \tag{1}
\]
Suppose a connected parameter product has a global holomorphic zero-lift
root \(s=s(a,b)\) of the original conditional equation. Assume throughout
its closure that all three legs have real parts in \((0,1/2)\), their
pair sums lie in the original regular strip, and
\[
 |\Im\cot\pi s|<1,\qquad
 |\Im\cot\pi a|<1,\qquad |\Im\cot\pi b|<1.
 \tag{2}
\]
These are hypotheses on an already established root, not a construction
of that root.

For \(\cot\pi s=u+iv,\ \cot\pi a=p+iq\), \(u,p>0\), the exact
triangle identity is
\[
 \det(-\Re V''/\pi)
 =\frac{(u+p)^2-(pv-uq)^2}{(u+p)^2+(v+q)^2}>0.
 \tag{3}
\]
Both diagonal entries are positive: if
\(C=\Re\cot\pi(s+a)\), positivity of the determinant gives
\(C<up/(u+p)<\min(u,p)\).
Thus each pair form is positive definite.

For \(\eta,\epsilon\in\{0,1\}\), write the full block as
\[
 F(s,a,b)=V(s,a)+V(s,b)-\epsilon g(s)
              -\tfrac\eta2g(a)-\tfrac\epsilon2g(b)+2\pi ias.
 \tag{4}
\]
The extra own-leg terms have nonnegative negative real Hessians because
\(\Re g''(z)=\pi\Re\cot\pi z>0\). The bilinear term contributes only
an imaginary Hessian. Consequently \(H=-F''\) has positive Hermitian
real part, uniformly on any compact product satisfying these conditions.

Let \(\phi(a,b)=F(s(a,b),a,b)\). Since \(F_s=0\),
\[
 -\phi''=H_{oo}-H_{os}H_{ss}^{-1}H_{so}.
 \tag{5}
\]
For a complex outer variation \(v\), put \(w=-H_{ss}^{-1}H_{so}v\).
The first block of \(H(w,v)^T\) vanishes, so
\[
 \Re\{v^*(-\phi'')v\}=\Re\{(w,v)^*H(w,v)\}>0.
 \tag{6}
\]
This proves strict real concavity at fixed imaginary heights. It does
not assert concavity after substituting a curved height graph.

## 2. Applying the criterion to the full transition source

The [transition conditional theorem](research_mixed_transition_conditional_rectangles.md)
first establishes global holomorphy on each of the four independent
products with real parts in \([.22,.45]\), type-three heights
\([-.03,.02]\), and type-four heights \([-.057,.0141]\).
Its certified boundary roots obey
\[
 .20<\Re s<.46,\qquad |\Im s|<.17.
 \tag{7}
\]
Successive maximum and minimum principles for the real and imaginary
parts of that holomorphic root extend (7) to the entire products.
This ordering supplies joint root holomorphy before any phase-Hessian
or maximum-principle deduction.

For \(0<x<1/2\),
\[
 |\Im\cot\pi(x+ih)|<1
 \quad\Longleftrightarrow\quad
 \cos(2\pi x)<e^{-2\pi|h|}.
 \tag{8}
\]
The scalar inequalities
\[
 \cos(.4\pi)<e^{-.34\pi},\qquad
 \cos(.44\pi)<e^{-.114\pi}
 \tag{9}
\]
therefore prove (2) for all roots and outer legs in these products.

For an optional explicit common reserve, the same compact rectangles give
\[
 \begin{array}{c|cc}
 &\Re\cot&|\Im\cot|\\ \hline
 s&( .09,1.4)&<.98\\
 a,b&( .15,1.21)&<.42 .
 \end{array}
 \tag{10}
\]
The minimum of
\(\sin(2\pi x)/[\cosh(2\pi Y)-\cos(2\pi x)]\) on a real interval
occurs at an endpoint; its derivative changes sign only from positive
to negative. The largest absolute imaginary cotangent occurs at the
smallest real part and largest height here. In the relevant range its
height derivative is positive since
\(\cos(2\pi x)\cosh(2\pi Y)<1\).
These facts reduce (10) to the focused scalar checks.

Each pair has \(\Re\cot\pi(s+a)>-3.5\), because
\(.42<\Re(s+a)<.91\). Hence its trace, divided by \(\pi\), is less
than \(1.4+1.21+7<10\). Equation (3) gives the determinant lower bound
\[
 \frac{(1-.98^2)\,.24^2}{.24^2+1.4^2}.
\]
The checker verifies that \(\pi/10\) times this quantity exceeds
\(1/4000\). Consequently
\[
                 -\Re V''\succ I_2/4000 .
 \tag{11}
\]

The same qualitative criterion applies to the new
[asymmetric own-four products](research_mixed_asymmetric_low_conditional_packets.md).
Their already established holomorphic roots satisfy
\(.24<\Re s<.42,\ |\Im s|<.21\). The left outer real part is at least
\(.15\), the right at least \(.28\), and all outer heights have magnitude
at most \(.057\). The inequalities
\(\cos(.48\pi)<e^{-.42\pi}\) and
\(\cos(.30\pi)<e^{-.114\pi}\) prove (2).
Thus the effective phase is strictly real-concave on each such product
at fixed heights. No tangent inequality is extrapolated from a reference
outside a connected convex source domain.

## 3. Original cyclic multiplicities and the plateau phase

For a fixed cyclic word, sum (4) with
\(s=s_v,\ a=t_{v-1},\ b=t_v,\ \eta=\epsilon_{v-1},\
\epsilon=\epsilon_v\). The result is exactly the full phase
\(\mathcal F\) in the
[central integral theorem](research_mixed_central_outer_integral.md).
All shared outer terms and chirps have their original multiplicities.

Each inner variation appears in two pair forms, and each outer variation
in two pair forms. Thus (11), followed by the complex Schur argument,
gives
\[
 \Re[-\mathcal F'']\succeq I_{2m}/2000,\qquad
 \Re[-\Phi'']\succeq I_m/2000,
 \quad \Phi(\mathbf t)=\mathcal F(\mathbf s(\mathbf t),\mathbf t).
 \tag{12}
\]
These statements remain valid for length-one cycles and the parallel
incidences at length two, by pulling back and summing the pair quadratic
forms before identifying variables.

Let \(\mathbf t^*=\mathbf x^*+i\mathbf y^*\) be the original critical
point and \(M=\Re\mathcal F(z_*)\). On the whole constant-height plateau
\(B_+=[.22,.45]^m\), stationarity and (12) imply
\[
 \Re\Phi(\mathbf x+i\mathbf y^*)\le
 M-\|\mathbf x-\mathbf x^*\|^2/4000 .
 \tag{13}
\]
The line segment used here stays inside the fixed-height source product;
no derivatives of a taper graph enter the argument.

The plateau is realized by the exact periodic graph contour with
\[
 \chi_1(x)=
 \begin{cases}
 (x/.22)^2,&0\le x\le.22,\\
 1,&.22\le x\le.45,\\
 ((.5-x)/.05)^2,&.45\le x\le.5,\\
 0,&.5\le x\le1 .
 \end{cases}
 \tag{14}
\]
Apply the general periodic deformation proof in
[the graph-contour theorem](research_mixed_outer_graph_contours.md)
to \(t_v=x+i y_v^*\chi_1(x)\), or to the chosen selected constant
height times \(\chi_1\) when discussing a separate alias.
Every finite Laurent integrand pulled back to the angle variables is
entire and periodic; the piecewise \(C^1\) homotopy has cancelling period
ends and no omitted vertical currents. Since all height magnitudes are
at most \(.057\),
\[
 |h'_v|\le2.28,\qquad |1+i h'_v|\le\sqrt{1+2.28^2}<2.49,\qquad
 \frac{.057}{.22^2}<\pi .
 \tag{15}
\]
For fixed \(m\) the Jacobian has no exponential cost. The last bound
also preserves the left cotangent cone, using
\(-\log\cos(2\pi x)/(2\pi)\ge\pi x^2\) for \(x<1/4\).
This exact contour statement does not bound its remaining taper pieces.

## 4. The true unaliased finite integrand

For an unselected type-four coordinate, \(h<0\) and \(0<x<1/2\).
Writing \(R=e^{2\pi h}<1,\theta=2\pi x\), the defining integral gives
\[
 \Im\operatorname{Li}_2(Re^{-i\theta})
 =-\int_0^R\arg(1-t e^{-i\theta})\,\frac{dt}{t}<0.
 \tag{16}
\]
The argument is strictly positive, since
\(1-t\cos\theta+i t\sin\theta\) lies in the right upper quadrant.
Therefore \(\nu(x+ih)=-\Re g(x+ih)>0\), uniformly on the compact
type-four plateau at the actual negative heights.

The whole-polynomial estimate in
[the Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
then bounds the actual \(d_N\) by
\(C_\delta N^{-1/2}\exp N(\nu+\delta)\) for every fixed \(\delta>0\).
There is no need to assume a relative factorial asymptotic away from the
local chart. Multiplying this estimate by the full canonical conditional
packets gives, for the literal unaliased integrand,
\[
 |f_{\varnothing,N}(\mathbf t)|
 \le C_\delta N^A
       \exp N\{\Re\Phi(\mathbf t)+k\delta\},
 \qquad k=\sum_v\epsilon_v .
 \tag{17}
\]
Every original conditional row and actual Fourier polynomial remains.

On a compact plateau set separated from the critical point, choose
\(\delta\) smaller than the strict loss in (13), divided by
\(2\max(k,1)\). The absolute integral over that set is exponentially
smaller than \(e^{NM}\). The existing local contribution theorem
therefore supplies the whole unaliased plateau asymptotic:
\[
 \int_{B_++i\mathbf y^*}f_{\varnothing,N}(\mathbf t)\,d\mathbf t
 =\kappa^{m+k}
   \frac{(2\pi)^m a(z_*)}{\sqrt{\det[-\mathcal F''(z_*)]}}\,
   e^{N\mathcal F(z_*)}(1+O(N^{-1})).
 \tag{18}
\]
The nonzero coefficient, level power \(N^0\), Gaussian branch, and both
parities are exactly those of the established local theorem.
Equivalently, the added plateau region outside the old central cube
contributes only an exponentially smaller absolute integral.

This is a complete unaliased plateau statement. Selected aliases,
curved taper portions, and the remaining full-period complement are
not included. It yields no new full mixed-word knot volume theorem.

## 5. Reproduction

    python3 experiments/check_mixed_plateau_accretivity.py --precision 256

The checker verifies the determinant identity, explicit scalar reserves,
and current source provenance. Root existence, source packets, and the
Gaussian normalization are the cited proved inputs, not new conclusions
of the scalar computation.
