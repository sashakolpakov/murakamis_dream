# Two crossings with both neighboring boundaries left open

Research theorem, 2 November 2026. The exact two-index formula makes it
possible to estimate a degree-two vertex of crossing power \(2\) or
\(-2\) before either neighboring boundary is closed. The proof keeps
the entire polynomial, both level parities, and every finite contour
correction. The frozen manuscripts are unchanged.

## 1. The full boundary polynomial

Use the Newton basis, crossing \(R\), and trace \(\phi_N\) of the
original complete root algebra. Define
\[
 P_N(u,v)=\sum_{i,j=0}^{N-1}\phi_N(R^2e_i e_j)
                     e_i(-2\cos u)e_j(-2\cos v).
\]
The [exact two-boundary calculation](research_degree_two_power_two_formula.md)
proves the identity
\[
 P_N(u,v)=N\sum_{i+j<N}
       q^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2}
                e_i(-2\cos u)e_j(-2\cos v),
 \quad q=e^{\pi i/N},\quad F_k=(q^2;q^2)_k.
 \tag{1}
\]
In particular this polynomial has degree at most \(N-1\) in each
of \(-2\cos u,-2\cos v\).

Let \(J(w)=\int_0^w\log(2\sin\pi s)\,ds\), with its holomorphic
branch on \(0<\Re w<1\) continued from the real interval. Let
\(b(x,u)\) be the canonical Newton phase, with
\(b(x,0)=J(2x)-4J(x)\). Set
\[
 W(x,y;u,v)=J(x+y)-2J(x)-2J(y)+b(x,u)+b(y,v)
                 +\frac{i\pi}{2}\bigl((x-y)^2+x+y\bigr).
 \tag{2}
\]
At \(u=v=0\), this becomes
\[
 W(x,y)=J(x+y)+J(2x)-6J(x)+J(2y)-6J(y)
                 +\frac{i\pi}{2}\bigl((x-y)^2+x+y\bigr).
 \tag{3}
\]
The exact selected point and its height are
\[
 z=\frac14+ih,\qquad h=\frac{\log3}{4\pi}.
 \tag{4}
\]
The first derivatives of (3) vanish at \((z,z)\). Its Hessian has
negative definite real part, as computed in the exact formula note.
Thus there are holomorphic functions \(x(u,v),y(u,v)\) continuing
this critical point. Put
\[
 S(u,v)=W(x(u,v),y(u,v);u,v),\qquad M=\Re S(0,0).
 \tag{5}
\]

**Theorem.** On a fixed complex bidisk about \(u=v=0\),
\[
 P_N(u,v)=N^{-3/2}A(u,v)e^{NS(u,v)}(1+O(N^{-1})),
 \tag{6}
\]
uniformly through all sufficiently large integer levels. The amplitude
is holomorphic and nonzero; the normalized error is holomorphic, with
the same order for fixed derivatives on smaller bidisks. Explicitly,
\[
 A(u,v)=
 \frac{2\pi\,a(x(u,v),y(u,v))}
      {\sqrt{\det[-W_{(x,y)(x,y)}(x(u,v),y(u,v);u,v)]}},
 \tag{7}
\]
where
\[
 a(x,y)=\frac{\sqrt2}{16}e^{-i\pi(x+y)/2}
       \frac{\sqrt{\sin\pi(x+y)}}{\sin^2(\pi x)\sin^2(\pi y)}.
\]
All square roots are the continued Gaussian and factorial branches.
There are positive constants \(c,B,b,C\) and a finite \(A_0\) with
\[
 |P_N(u+is,v+it)|\le CN^{A_0}
  \exp N\{M-c(1-\cos u)-c(1-\cos v)+B(s^2+t^2)\}
 \tag{8}
\]
for real \(|u|,|v|\le\pi\) and \(|s|,|t|\le b\).
The boundary Hessian is
\[
 S''(0,0)=-\frac{e^{i\pi/6}}{2\pi}I_2.
 \tag{9}
\]
Negative crossing power is obtained by coefficient conjugation.

The phase in this theorem is the direct phase of (1), including its
crossing normalization. The subsequent
[marked geometric comparison](research_degree_two_power_two_geometric_phase.md)
proves that it equals the original geometric action plus \(i\pi/2\)
(minus \(i\pi/2\) for negative crossing power). That proof
retains the logarithmic branches and absolute volume normalization;
the comparison is not inferred merely from matching critical equations.

## 2. Extreme indices are discarded before deforming a contour

Put \(\alpha=1/32\), \(\beta=15/32\), and retain
\(i/N,j/N\in[\alpha,\beta]\). This rectangle lies strictly inside
the triangular support \(i+j<N\), for all sufficiently large levels.
There is consequently no triangular endpoint in the retained sum.

The complete Hermite norm estimate bounds a low wire of normalized
index \(x\) at rate \(2g(x)\), where \(g(x)=J(2x)-4J(x)\).
The maximum is \(M_\infty=4G/\pi\), and a high wire has only
polynomial norm. These statements apply before the central trace
and include its first normal derivatives.
Symmetry and concavity of \(g\) give
\[
 \sup_{x\notin[\alpha,\beta],\,0\le x\le1/2}2g(x)
 =2g(\alpha).
\]
The exact constant comparison is
\[
 M-M_\infty-2g(\alpha)>\frac1{32}.
 \tag{10}
\]
It is one of the outward interval inequalities verified by the
certificate described in Section 5 below.
Every omitted assignment thus has a strict rate gap, uniformly over
all real boundary angles. Polynomially many assignments and the
fixed \(R^2\) trace cost only a polynomial prefactor. This estimates
the original omitted terms, rather than discarding part of the new
factorial expression on the basis of its values alone.
The omitted polynomial has separate degrees at most \(N-1\).
Its Chebyshev continuation from the real spectral square costs at
most \(N(|\Im u|+|\Im v|)\) in the exponent, with a polynomial
prefactor. Thus its strict gap persists on a sufficiently small
fixed complex bidisk.

## 3. Exact interpolation and the upper horizontal rectangle

Use \(G_N(Nx)\), \(G_N(Ny)\), \(G_N(N(x+y))\) for the sine
factorials in (1), and the canonical interpolants for its two
Newton factors. The resulting exact interpolant is
\[
 f_N(x,y;u,v)
 =N e^{\,i\pi N((x-y)^2+x+y)/2-i\pi(x+y)/2}
    \frac{G_N(N(x+y))}
         {G_N(Nx)^2G_N(Ny)^2}
       \mathcal B_N(x,u)\mathcal B_N(y,v).
 \tag{11}
\]
At \(x=i/N,y=j/N\), it is precisely the summand in (1).
It is holomorphic on a neighborhood of the product rectangles
\[
 \alpha\le\Re x,\Re y\le\beta,\qquad
 |\Im x|,|\Im y|\le h,
 \tag{12}
\]
for small complex \(u,v\). The factorial arguments have real parts
strictly between their original endpoints. The same statement holds
on slightly enlarged rectangles, so half-grid endpoints differing by
\(O(N^{-1})\) are permitted. For real boundary angles throughout
their whole periods, the reciprocal-factorial continuation establishes
the same holomorphy.

On (12) at small complex boundary angles, the uniform factorial
expansion is
\[
 f_N=N^{-5/2}a(x,y)e^{NW(x,y;u,v)}(1+O(N^{-1})).
 \tag{13}
\]
The exact one-sided summation identity in
[the wire-contour note](research_terminal_one_sided_wire_formula.md)
is applied in each variable. Its constant upper horizontal term has
coefficient \(N\); its upper and lower corrections each have an
exponential penalty \(2\pi h\). At a vertical endpoint with imaginary
part \(s\), the penalty is \(2\pi\max(-s,0)\).
The product of these identities is exact. It retains every horizontal
correction and every endpoint current.

On the upper horizontal product, \(x=\xi+ih,y=\eta+ih\).
The real Hessian of (3) is
\[
 \Re W''=\pi\Re\cot(\pi(x+y))
                \begin{pmatrix}1&1\\1&1\end{pmatrix}
  -\pi\operatorname{diag}\left(
       \Re(4\cot\pi x+2\tan\pi x),
       \Re(4\cot\pi y+2\tan\pi y)\right).
 \tag{14}
\]
The remaining quadratic term has purely imaginary Hessian.
Since \(\sinh(4\pi h)=4/3\),
\(\Re\cot(\pi(x+y))\le3/4\).

Here is an explicit lower bound on each diagonal factor. Put
\(\theta=2\pi\xi\) and \(c_0=\cosh(2\pi h)=2/\sqrt3\). Then
\[
 \Re(4\cot\pi x+2\tan\pi x)
 =\frac{\sin\theta(6c_0+2\cos\theta)}
            {\sin^2\theta+1/3}>\frac{12}{5}.
 \tag{15}
\]
Indeed \(\sin\theta\ge\sin(\pi/16)>3/16\) on the retained
interval and \(6c_0-2>49/10\). The function
\(s/(s^2+1/3)\) increases and then decreases on \(s>0\), so on
\([3/16,1]\) it is at least \(144/283\). Their product is greater
than \(12/5\).
Equations (14)--(15) give
\[
 \Re W''\le-\frac{9\pi}{10}I_2.
 \tag{16}
\]
Thus the real phase is strictly concave on the whole upper rectangle.
Its unique maximum is \(M\), attained at \((z,z)\), with a strict
gap outside every neighborhood of that point. The inequalities have
slack and persist at the actual half-grid boundaries.

## 4. The other horizontal terms

An upper correction acquires an additional penalty \(2\pi h\).
It remains to estimate terms with a lower horizontal variable.
Write \(s=\xi+\eta\), and let \(W_{++},W_{-+}\) denote the real
phases at heights \((h,h)\) and \((-h,h)\).
Directly from (3) and conjugation of \(J\) on its original strip,
\[
 W_{-+}-2\pi h-W_{++}
 =J(s)-\Re J(s+2ih)-\pi h+2\pi h(\xi-\eta).
 \tag{17}
\]
For \(0<s\le1/2\),
\[
 J(s)-\Re J(s+2ih)
 =\int_0^{2h}\arg\sin(\pi(s+iv))\,dv
 \le2\pi h(1/2-s).
 \tag{18}
\]
This uses
\(\arg\sin(\pi(s+iv))=\arctan(\cot(\pi s)\tanh(\pi v))\).
For \(1/2\le s<1\), the same integral is nonpositive.
In the first case (17) is at most \(-4\pi h\eta\); in the
second it is at most \(-\pi h+2\pi h(\beta-\alpha)\).
Both are at most \(-4\pi h\alpha\).
The estimate with the variables reversed is identical.

With both variables on the lower side, conjugation of the
nonpolynomial part gives
\[
 W_{--}-4\pi h=W_{++}-2\pi h.
 \tag{19}
\]
Consequently every nonconstant horizontal term has a strict gap
below \(M\). All Fourier terms are contained in the exact rational
correction kernels; no finite charge cutoff is used.

## 5. Endpoint currents

For one endpoint variable, take \(e\in\{\alpha,\beta\}\),
\(\sigma,\tau\in\{-1,1\}\), and \(0\le v,w\le1\). The eight
functions to bound are
\[
 \Re W(e+i\sigma hv,\,
       \alpha+(\beta-\alpha)w+i\tau h)
 -2\pi h\bigl(v\mathbf1_{\sigma<0}+\mathbf1_{\tau<0}\bigr)-M.
 \tag{20}
\]
Each is strictly less than \(-1/4\).
Interchanging the variables gives the other one-endpoint cases by
symmetry of \(W\). For two endpoint variables, the sixteen functions
are
\[
 \Re W(e+i\sigma hv,f+i\tau hw)
 -2\pi h\bigl(v\mathbf1_{\sigma<0}+w\mathbf1_{\tau<0}\bigr)-M,
 \quad e,f\in\{\alpha,\beta\}.
 \tag{21}
\]
Each is strictly less than \(-1/2\).
Additional upper horizontal correction penalties only improve these
bounds.

These are finite rigorous inequalities, established by

    python3 experiments/certify_two_crossing_internal_endpoints.py --output repro/results/research-two-crossing-internal-endpoints.json

The [saved certificate](../repro/results/research-two-crossing-internal-endpoints.json)
records every accepted dyadic rectangle and its upper bound. At the
center of each parameter rectangle the program evaluates (20) or
(21) with outward ball arithmetic. It encloses the two first
derivatives on the whole rectangle and applies the mean-value bound
\[
 F(v,w)\le F(v_0,w_0)
       +\sup|F_v|\,|v-v_0|+\sup|F_w|\,|w-w_0|.
\]
A rectangle is accepted only if this upper bound is strictly below
the stated negative constant. Otherwise it is bisected. The accepted
rectangles partition each initial unit square, so there is no
unsampled region. All inputs are rational, algebraic, or specified
logarithms at 140-bit working precision. The same run proves (10).

The phase is holomorphic on a neighborhood of (12). Uniform
continuity therefore preserves smaller strict gaps when the exact
half-grid endpoints replace \(\alpha,\beta\), and when \(u,v\)
are in a sufficiently small complex bidisk.

## 6. The nonzero expansion and the entire boundary estimate

Only the upper constant horizontal product remains at the selected
rate. Its coefficient is \(N^2\). Equations (13) and (16) give
ordinary two-dimensional complex Gaussian integration, uniformly on
a small boundary bidisk. More explicitly, for small complex \(u,v\)
move a fixed small product neighborhood of \((z,z)\) through its
continued critical point. This deformation lies inside the regular
factorial chart. Its connecting pieces stay outside a smaller
critical neighborhood, where the original strict gap persists by
continuity. The local real Gaussian directions therefore give the
holomorphic parameter expansion.
The factors are \(N^2\) from the two sums,
\(N^{-5/2}\) from the exact interpolant, and \(N^{-1}\) from the
Gaussian. This proves the power \(N^{-3/2}\), the amplitude (7),
and the holomorphic relative error in (6). All numerator factorial
factors and the Gaussian determinant are nonzero at the selected
point, so the amplitude is nonzero after shrinking the bidisk.

For real boundary angles, replace each Newton factor in (11) by
the uniform factorial bound from
[the boundary-decay theorem](research_uniform_factorial_and_boundary_decay.md).
Throughout (12) it inserts a positive loss
\[
 c_1(1-\cos u)+c_1(1-\cos v),
 \qquad
 0<c_1\le
 \frac{\sin(2\pi\alpha)}{4\pi\cosh^2(\pi h)},
\]
on every main, correction, and endpoint piece. The discarded wire
terms have the fixed gap (10), independently of real \(u,v\);
decreasing the angular constant absorbs them as well. This proves
(8) on the whole real boundary torus.

At zero boundary, the first parameter derivatives of the selected
point vanish by separate evenness. Directly differentiating the
Newton phase gives
\[
 b_{uu}(x,0)=-\frac{\tan(\pi x)}{2\pi}.
\]
Since \(\tan(\pi z)=e^{i\pi/6}\), the stationary value has Hessian
(9), with negative definite real part. Taylor's theorem and Young's
inequality give the quadratic imaginary-direction term in (8) near
the origin. Away from that neighborhood, the real estimate has a
fixed gap. The polynomial Bernstein--Walsh bound on finitely many
products of real spectral intervals preserves half that gap in a
sufficiently thin complex neighborhood. The separate degrees are
at most \(N-1\). Combining these two regions proves (8).

Coefficient conjugation proves the negative-power assertions with
the same real rate and boundary losses. No statement here changes
the original framing or primitive curves.
