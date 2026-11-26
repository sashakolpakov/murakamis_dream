# The complete central part of the mixed cyclic integral

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The complete conditional-sum theorem is now available on a fixed product
of rectangles. This permits evaluating the entire central part of the
outer integral, rather than a small neighborhood chosen separately for
each word. The argument below proves strict concavity of the effective
phase on that whole product. The outer regions beyond the product and
the additional Fourier integrals remain separate.

## 1. The finite expression and its central region

Fix a cyclic word \(3+\epsilon_1,\ldots,3+\epsilon_m\), where
\(\epsilon_v\in\{0,1\}\), and put \(k=\sum_v\epsilon_v\).
Use the exact finite Laurent integrand \(f_{\varnothing,N}\) from
(3) of [the local contribution theorem](research_mixed_local_outer_contribution.md).
In particular it contains the original reciprocal-factorial polynomial
\(d_N\), and its scalar is \(\kappa^{m+k}N^{m+k}\). This is the
term without an additional frequency \(N\) at a four-crossing variable;
the other terms of the exact trace are not included in this notation.

Let \(z_*=(\mathbf s^*,\mathbf t^*)\) be the original critical point,
and write \(x_*=\Re\mathbf t^*\), \(y_*=\Im\mathbf t^*\). The
[type-three window theorem](research_mixed_type_three_window_strip.md)
and [type-four height theorem](research_mixed_cyclic_critical_height_bounds.md)
give
\[
\begin{array}{lll}
 .30<\Re t_v^*<.39,&-.03<\Im t_v^*<.02,&\epsilon_v=0,\\
 .27<\Re t_v^*<.33,&-.057<\Im t_v^*<-.001,&\epsilon_v=1.
\end{array}
\tag{1}
\]
Define the fixed central cube
\[
 B=[1/4,2/5]^m,\qquad
 J_N=\int_{B+i y_*}f_{\varnothing,N}(\mathbf t)\,d\mathbf t.
\tag{2}
\]
The critical point lies strictly inside this cube.

The primitive and the full phase are
\[
\begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 \mathcal F(\mathbf s,\mathbf t)
 &=\sum_v\left\{
 g(s_v+t_v)+g(t_v+s_{v+1})
 -(2+\epsilon_v)[g(s_v)+g(t_v)]+2\pi i t_vs_{v+1}\right\}.
\end{split}
\tag{3}
\]
The branches are those of the original factorial interpolation, on
\(0<\Re z<1\). For every \(\mathbf t\) in the independent rectangles
of [the central conditional theorem](research_mixed_central_conditional_rectangles.md),
let \(s_v(\mathbf t)\) be its original conditional root, and set
\[
 \Phi(\mathbf t)=\mathcal F(\mathbf s(\mathbf t),\mathbf t).
\tag{4}
\]
The roots obey
\[
 .20<\Re s_v<.44,\qquad |\Im s_v|<.15.
\tag{5}
\]
These bounds are certified on every distinguished boundary of the
parameter products. They hold throughout the products by applying the
maximum and minimum principles, one variable at a time, to the real and
imaginary parts of the holomorphic roots. This uses the global root
branch in Lemma 1 of the central conditional theorem.

## 2. A uniform positive Hessian

The following elementary estimate is useful because it does not depend
on the word length. Put
\[
 c_Y(x)=\frac{\sin(2\pi x)}
              {\cosh(2\pi Y)-\cos(2\pi x)},\qquad 0<x<1/2.
\tag{6}
\]
For \(|y|\le Y\), \(\Re\cot\pi(x+iy)\ge c_Y(x)>0\).
On any subinterval of \((0,1/2)\), the minimum of \(c_Y\) is
attained at an endpoint. Indeed, the sign of its derivative is the
sign of \(\cosh(2\pi Y)\cos(2\pi x)-1\); it can change only
from positive to negative.

Write \(\eta=\epsilon_{v-1}\), \(s=s_v\), \(a=t_{v-1}\), \(b=t_v\).
The contribution
\[
\begin{split}
 F_v(s,a,b)={}&g(s+a)+g(s+b)-(2+\epsilon_v)g(s)+2\pi ias\\
             &-(1+\eta/2)g(a)-(1+\epsilon_v/2)g(b)
\end{split}
\tag{7}
\]
sums exactly to (3). Every outer term is shared equally by its two
incident contributions, including when a short cycle identifies
some of the variables.

Let \(H_v=-F_v''\). Since
\(g''(z)=\pi\cot(\pi z)-i\pi\), its Hermitian real part is a real
symmetric matrix. For example, its \(s,a\) entry is
\(-\pi\Re\cot\pi(s+a)\); the extra \(2\pi i\) in (7) has no
real part. Subtracting the absolute off-diagonal row entries from
the diagonal gives the following lower bounds:
\[
\begin{split}
 r_s&\ge 2\pi\Re\cot(\pi s)
       -4\pi\max\{\cot\pi(\Re s+.25),0\},\\
 r_a&\ge \pi\Re\cot(\pi a)
       -2\pi\max\{\cot\pi(\Re a+.20),0\},
\end{split}
\tag{8}
\]
and the same bound as \(r_a\) holds for \(r_b\).
To check (8), a shifted cotangent with real part at least \(1/2\)
is nonpositive and cancels from the row margin. Below \(1/2\),
its real part is at most the real cotangent, which decreases with
the real part. The positive extra own-index terms for type four
can only increase the margins.

For all roots (5) and all outer coordinates in
\([.25,.40]+i[-.057,.057]\), the four bounds
\[
\begin{split}
 2\pi\min\{c_{.15}(.20),c_{.15}(.25)\}-4\pi\cot(.45\pi)&>19/20,\\
 2\pi\min\{c_{.15}(.25),c_{.15}(.44)\}&>19/20,\\
 \pi\min\{c_{.057}(.25),c_{.057}(.30)\}-2\pi\cot(.45\pi)&>19/20,\\
 \pi\min\{c_{.057}(.30),c_{.057}(.40)\}&>19/20
\end{split}
\tag{9}
\]
follow from the outward interval calculations supplied with this note.
The first two apply to \(r_s\), separated at \(\Re s=.25\);
the last two apply to an outer row, separated at \(\Re a=.30\).
All decimals in (9) denote the exact displayed rational numbers.

Strict diagonal dominance of the real symmetric matrix therefore gives
\[
 \Re H_v\succ\lambda I_3,\qquad \lambda=19/20.
\]
After identifying the shared variables and summing,
\[
 \Re[-\mathcal F'']\succeq
       \lambda\,\operatorname{diag}(I_m,2I_m).
\tag{10}
\]
One can also verify this directly on quadratic forms: each inner
variation occurs once and each outer variation twice. This proves
(10) for cycles of lengths one and two as well.

Let \(H=-\mathcal F''\) at \((\mathbf s(\mathbf t),\mathbf t)\).
The negative effective Hessian is its Schur complement,
\[
 -\Phi''=H_{tt}-H_{ts}H_{ss}^{-1}H_{st}.
\tag{11}
\]
For any complex vector \(v\), set \(w=-H_{ss}^{-1}H_{st}v\).
The first block of \(H(w,v)^T\) is zero. Consequently
\[
 \Re\!\left[v^*(-\Phi'')v\right]
   =\Re\!\left[(w,v)^*H(w,v)\right]
   \ge\lambda\|w\|^2+2\lambda\|v\|^2.
\tag{12}
\]
Thus the Hermitian real part of the effective Hessian is uniformly
positive on the whole product.

In particular the real function \(x\mapsto\Re\Phi(x+i y_*)\) is
strictly concave on \(B\). Since its full complex derivative vanishes
at \(\mathbf t^*\), integrating (12) on the line segment from \(x_*\)
to \(x\) gives
\[
 \Re\Phi(x+i y_*)\le
 M_*-\lambda\|x-x_*\|^2,\qquad M_*=\Re\mathcal F(z_*).
\tag{13}
\]

## 3. Evaluation of the whole central integral

On \(B+i y_*\), the complete conditional theorem and the factorial
symbol give the same asymptotic as (8) of the local contribution
theorem, uniformly on this entire compact region:
\[
 f_{\varnothing,N}(\mathbf t)=
 \kappa^{m+k}N^{m/2}(2\pi)^{m/2}
 \frac{a(\mathbf s(\mathbf t),\mathbf t)}
      {\sqrt{\det H_{ss}(\mathbf t)}}\,
 e^{N\Phi(\mathbf t)}(1+O(N^{-1})).
\tag{14}
\]
Here \(a\) is the original coefficient in (5) of that theorem;
every sine factor stays nonzero. The square roots are the branches
defined by Gaussian integration.

The use of the actual polynomial \(d_N\) in (14) is justified on the
whole central region. Every type-four height in (1) is negative and
every real coordinate lies in \([.25,.40]\). The criterion
\(-\Re g(t)>0\) from
[the reciprocal-factorial comparison](research_mixed_fourier_weight_continuation.md)
therefore holds uniformly. More quantitatively, its dilogarithm
integral gives
\[
 -\Re g(x-iy)\ge
 \frac{e^{-.114\pi}\sin(.8\pi)}{4\pi}>3/100
 \quad(.25\le x\le.40,\ 0\le y\le.057).
\tag{15}
\]
For the first inequality, put \(\rho=e^{-2\pi y}\) and
\(\theta=2\pi x\). The argument of \(1-te^{-i\theta}\) lies in
\([0,\pi/2]\), so it is at least its sine, which is at least
\(t\sin\theta/2\). Integrating the defining dilogarithm formula proves
the bound. Thus replacing \(d_N\) by the factorial expression has
uniform exponentially small relative error, rather than merely
agreement on the root grid.

**Theorem 1.** For every fixed cyclic three/four word,
\[
 J_N=
 \kappa^{m+k}\frac{(2\pi)^m a(z_*)}{\sqrt{\det[-\mathcal F''(z_*)]}}\,
 e^{N\mathcal F(z_*)}(1+O(N^{-1})).
\tag{16}
\]
The leading coefficient is nonzero and the conclusion holds along
both level parities.

*Proof.* Choose a small fixed box around \(x_*\) contained in \(B\).
The local contribution theorem evaluates its integral with the
coefficient in (16). On the rest of \(B\), (13)--(14) give an
exponential loss, since the distance to \(x_*\) has a positive lower
bound. The remaining factor in (14) is bounded on this compact set.
Adding the two integrals proves (16). The Gaussian determinant branch
is exactly that of the local theorem; no new choice is made. \(\square\)

More explicitly, the part of \(B\) whose Euclidean distance from
\(x_*\) is at least \(\rho\) has absolute integral at most
\[
 C N^{m/2}\exp\{N(M_*-\lambda\rho^2)\}.
\tag{17}
\]
This is an estimate for the original finite integrand.

The theorem leaves the regions with an outer real coordinate outside
\([1/4,2/5]\) untreated. It also leaves the full additional-frequency
integrals untreated; their already proved estimates on small local
regions do not imply estimates on the entire central cube. Finally,
no arbitrary cyclic trace is identified here with a knot invariant.

## 4. A sharper bound retaining the type of each variable

The accepted affine root enclosures in the central conditional
certificate give additional information:
\[
       \frac{507}{1000}<\Re(s_v+t_j)<1
                         \qquad(j=v-1,v).
\tag{18}
\]
The upper bound follows already from (5). For the lower bound, on
each accepted boundary cell the certificate encloses the root as
\[
 s=s_0+d_a(a-a_0)+d_b(b-b_0)+e,\qquad
          |\Re e|,|\Im e|\le r.
\tag{19}
\]
All centers, affine coefficients, parameter intervals and radii are
rational. Adding \(a\), or \(b\), to (19) and minimizing its real
affine part on the cell proves the strict lower bound by exact
rational arithmetic. The checker performs this calculation for
all 1,103 accepted cells, and checks that their binary addresses
cover all 64 distinguished-boundary pieces. The established
holomorphic root branch then extends the bounds to the full products
by the harmonic maximum and minimum principles.

Thus each shifted cotangent in (7) has strictly negative real part.
Its Hessian contribution is a nonnegative multiple of
\(|\delta s+\delta a|^2\), or \(|\delta s+\delta b|^2\).
The remaining diagonal terms are positive own-variable cotangents.
After summation and the same Schur argument as (12), this gives
\[
 \Re\!\left[v^*(-\Phi'')v\right]\ge
 \sum_j(2+\epsilon_j)\pi\Re\cot(\pi t_j)\,|v_j|^2.
\tag{20}
\]
This bound retains the larger diagonal coefficient at a four-crossing
variable. It can be combined with (12); neither estimate concerns
the exterior outer region.

## 5. Reproduction

Run

~~~sh
python3 experiments/check_mixed_central_outer_integral.py
~~~

The checker proves the four strict margins (9) and the reciprocal
factorial margin (15) with outward real-ball arithmetic, and extracts
(18) by exact rational arithmetic from the accepted root witnesses. The
conditional roots, full finite-source contours and type-three
localization are supplied by the separately recorded proofs and
certificates linked above. This small checker does not replace those
dependencies or estimate the exterior outer region.
