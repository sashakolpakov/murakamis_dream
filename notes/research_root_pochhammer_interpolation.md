# An exact interpolation of a finite product at a root of unity

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The finite product in the traced three-crossing vertex can be
interpolated in its length without losing its exact lattice values.
The interpolation below also satisfies the original difference
equation away from the lattice. Its uniform holomorphic expansion
allows a contour argument for the moving saddle of that same finite
sum. It does not select a contributing saddle by itself.

## 1. The function and its exact difference equation

Fix an integer \(N\ge2\), put \(Q=e^{2\pi i/N}\), and write
\[
 Y=Xe^{-2\pi i s},\qquad
 \mathcal D=\{(s,X)\in\mathbb C^2:|X|<1,\ |Y|<1\}.
 \tag{1}
\]
All logarithms of \(1-X\), \(1-Y\), and their powers below are
defined by their convergent series in the unit disk. Set
\[
 \begin{split}
 L_N(s,X)
 &=s\log(1-Y^N)
   -\sum_{\substack{k\ge1\\N\nmid k}}
       \frac{X^k-Y^k}{k(1-e^{-2\pi i k/N})},\\
 \mathcal P_N(s,X)&=\exp L_N(s,X).
 \end{split}
 \tag{2}
\]
The first term is needed because the denominator of the series
vanishes at multiples of \(N\). It retains those terms, rather
than deleting them from the finite product.

**Proposition 1.** The function \(\mathcal P_N\) is holomorphic
and nonzero on \(\mathcal D\). It satisfies
\[
 \begin{split}
 \mathcal P_N(0,X)&=1,\\
 \frac{\mathcal P_N(s+1/N,X)}{\mathcal P_N(s,X)}
     &=1-Xe^{-2\pi i s},\\
 \mathcal P_N(\ell/N,X)
     &=\prod_{a=0}^{\ell-1}(1-XQ^{-a})
          =(X;Q^{-1})_\ell\qquad(\ell\in\mathbb Z_{\ge0}).
 \end{split}
 \tag{3}
\]
The empty product is one. In particular there is no parity
restriction on \(N\).

*Proof.* For \(N\nmid k\),
\[
 |1-e^{-2\pi i k/N}|
       \ge2\sin(\pi/N)\ge4/N.
 \tag{4}
\]
On a compact subset of \(\mathcal D\), both \(|X|\) and \(|Y|\)
are at most some \(\rho<1\). The series and all its fixed
derivatives therefore converge locally uniformly. Its exponential
has no zeros.

Under \(s\mapsto s+1/N\), \(Y\) is replaced by \(YQ^{-1}\),
while \(Y^N\) stays fixed. Hence
\[
 \begin{split}
 L_N(s+1/N,X)-L_N(s,X)
 &=\frac1N\log(1-Y^N)
                  -\sum_{\substack{k\ge1\\N\nmid k}}\frac{Y^k}{k}\\
 &=\log(1-Y).
 \end{split}
 \tag{5}
\]
The second equality includes the missing subseries
\(\sum_{a\ge1}Y^{aN}/(aN)=-N^{-1}\log(1-Y^N)\).
At \(s=0\), (2) is zero. Iterating (5) proves all of (3).
\(\square\)

The recurrence and its value at zero do not characterize a
holomorphic interpolation uniquely: multiplication by a nonzero
\(1/N\)-periodic function equal to one at zero preserves them.
Formula (2) specifies the interpolation used here. The asymptotic
estimates below are proved for that formula.

## 2. A uniform holomorphic expansion

Define the dilogarithm in the disk by
\(\operatorname{Li}_2(z)=\sum_{k\ge1}z^k/k^2\). For a
nonpositive integer \(j\), use
\(\operatorname{Li}_j(z)=\sum_{k\ge1}k^{-j}z^k\).
Let \(B_{2r}\) be the Bernoulli numbers, with \(B_2=1/6\).

**Proposition 2.** For every compact \(K\subset\mathcal D\) and
every fixed integer \(p\ge0\),
\[
 \begin{split}
 L_N(s,X)
 ={}&\frac{N}{2\pi i}
          \{\operatorname{Li}_2(Y)-\operatorname{Li}_2(X)\}\\
 &+\frac12\{\log(1-X)-\log(1-Y)\}\\
 &-\sum_{r=1}^{p}
    \frac{B_{2r}(2\pi i)^{2r-1}}{(2r)!\,N^{2r-1}}
       \{\operatorname{Li}_{2-2r}(X)
                     -\operatorname{Li}_{2-2r}(Y)\}
       +O_{K,p}(N^{-2p-1}).
 \end{split}
 \tag{6}
\]
Every fixed derivative has the same remainder order on a smaller
compact neighborhood.

*Proof.* Separate the series (2) at \(k=N/4\). By (4), its
tail is \(O_K(N^a\rho^{N/4})\) for some fixed \(a\), and the
same holds after any fixed number of derivatives. The resonant
term \(s\log(1-Y^N)\) is exponentially small with its fixed
derivatives as well.

For \(k<N/4\) use the convergent expansion
\[
 \frac1{1-e^{-u}}
 =\frac1u+\frac12+
       \sum_{r=1}^{p}\frac{B_{2r}}{(2r)!}u^{2r-1}
       +O_p(|u|^{2p+1}),\qquad u=\frac{2\pi i k}{N}.
 \tag{7}
\]
The remainder bound is uniform on \(|u|\le\pi/2\), after
removing the pole at zero. Multiplication by
\((X^k-Y^k)/k\) and summation bound the error by
\[
 \frac{C_{K,p}}{N^{2p+1}}
                  \sum_{k\ge1}k^{2p}\rho^k
          =O_{K,p}(N^{-2p-1}).
 \tag{8}
\]
Extending each remaining sum to all positive \(k\), including
multiples of \(N\), changes it by an exponentially small amount.
The series definitions then give (6), including its signs and
constant term. Work on a slightly larger compact neighborhood
and use Cauchy's formula for the derivative assertion.
\(\square\)

The version needed for the vertex uses length \(i+1\), with
\(z=i/N\). With \(Y_z=Xe^{-2\pi iz}\), (6) gives
\[
 \mathcal P_N(z+1/N,X)
 =\sqrt{(1-X)(1-Y_z)}
   \exp\left[
      \frac{N}{2\pi i}
          \{\operatorname{Li}_2(Y_z)-\operatorname{Li}_2(X)\}
       \right]\{1+O(N^{-1})\}.
 \tag{9}
\]
The square root means the exponential of half the sum of the
two specified logarithms. The estimate is holomorphic and uniform
on compact subsets of (1), with all fixed derivatives of the
normalized error. At \(z=i/N\) the left side is the exact original
denominator product; no error is introduced at its lattice values.

## 3. Application to the retained vertex

In the [traced-vertex sum](research_traced_three_vertex_endpoint.md),
the two denominator factors are
\((X;Q^{-1})_{i+1}\) and \((Y;Q^{-1})_{j+1}\).
Here \(X,Y\) denote the two independent external parameters,
rather than the dependent variable \(Y\) of (1).
Apply (2) to them separately, at \(s=(i+1)/N\) and
\(s=(j+1)/N\). Near the homogeneous point
\[
                   X=Y=(1+i\sqrt3)/4,\qquad
                         i/N=j/N=1/3,
 \tag{10}
\]
both applications lie strictly in their respective domains
\(\mathcal D\).

The numerator sine factorial has the exact interpolation \(G_N\)
from [the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
It satisfies \(G_N(k)=\prod_{a=1}^k2\sin(\pi a/N)\), with
its proved uniform holomorphic expansion for \(0<\Re(k/N)<1\).
Combining that function with (2) and the original finite phases
therefore gives an exact analytic interpolation of every summand
in a fixed neighborhood of \(i/N=j/N=1/3\). Its nonzero
leading density is the one computed in the traced-vertex proof.

This supplies an analytic function to integrate when deforming a
local lattice contour. Bounds on the complementary lattice points,
vertical contour sides and aliases remain necessary. In particular
(2) and (9) alone do not assert a nonzero contribution to the
full knot invariant.

The [focused checker](../experiments/check_root_pochhammer_interpolation.py)
verifies the recurrence coefficients and Bernoulli expansion
algebraically, then compares the interpolant with literal finite
products and the off-grid recurrence at both parities. Its
[record](../repro/results/research-root-pochhammer-interpolation.json)
separates those finite diagnostics from the uniform written proof.
