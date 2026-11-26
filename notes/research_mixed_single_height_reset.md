# The cost of moving one outer variable to the real axis

Research proof, 4 November 2026. This note estimates a change that occurs
in the blocks next to a small outer coordinate. One argument of a block
stays at its geometric reference value. The other is moved to the real
axis, and its real part may change anywhere in the right-half source
rectangle. The estimate includes that real readjustment.

## 1. Phase and parameter domains

For types \(\eta,\epsilon\in\{0,1\}\), let
\[
 \phi(a,b)=Q_\epsilon(s_*(a,b);a,b)
            -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \qquad
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias.
 \tag{1}
\]
Here \(g\) is the original dilogarithmic primitive and \(s_*\) is
the original zero-lift conditional root. These are the same functions
as in the [real supporting-plane theorem](research_mixed_real_outer_support.md).
Put
\[
 \begin{split}
 R_3&=[.30,.39]+i[-.03,.02],&
 R_4&=[.27,.33]+i[-.057,-.02],\\
 U_3&=[.22,.50]+i[-.03,.02],&
 U_4&=[.22,.50]+i[-.057,0].
 \end{split}                                                    \tag{2}
\]
The [complete right-square source theorem](research_mixed_unselected_right_taper_products.md)
supplies the same holomorphic phase on neighborhoods of all these
products, with its original finite-sum normalization.

For a reference \(r=(a_*,b_*)\in R_{3+\eta}\times R_{3+\epsilon}\),
write
\[
 \Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r).
 \tag{3}
\]

**Theorem 1.** Keep one coordinate equal to its reference value and
move the other coordinate \(j\) to a real number \(x\in[.22,.50]\).
Then
\[
           \Re\{\phi(z)-\Gamma_r(z)\}<7(\Im r_j)^2
                  \le 7(.057)^2=.022743.                     \tag{4}
\]
At a zero displacement the strict inequality in (4) is replaced by
equality; the non-strict upper bound holds in every case. The result
allows every ordered type pair and either choice of moving coordinate.

## 2. A directional Hessian bound

On each product in which the moving coordinate belongs to its \(U\)
rectangle and the fixed coordinate belongs to its \(R\) rectangle,
let \(h=\phi_{jj}\), \(A=-\Re h\), and \(B=\Im h\).
The certificate proves
\[
                         A>0,\qquad A^2+B^2<14A.             \tag{5}
\]
It suffices to check (5) on products of rectangle sides. To see this,
first complete the real square on each boundary product:
\[
 \Re\{h(u+iv)^2\}
   =-Au^2-2Buv+Av^2
   \le\frac{A^2+B^2}{A}\,v^2\le14v^2,
             \qquad u,v\in\mathbb R.                       \tag{6}
\]
For each fixed \((u,v)\), the left side is harmonic in both complex
parameters. Two maximum principles extend (6) to the full product.
The strict positivity of \(A\) extends by the same principle.
This argument does not assert that the quotient in (6) is harmonic.

For clarity, the derivative in (5) includes the motion of the inner
critical point. If
\[
 p=g''(s_*+a),\quad q=g''(s_*+b),\quad
 d=p+q-(2+\epsilon)g''(s_*),
\]
the two possibilities are
\[
 \phi_{aa}=p-(1+\eta/2)g''(a)-(p+2\pi i)^2/d,
 \qquad
 \phi_{bb}=q-(1+\epsilon/2)g''(b)-q^2/d.                    \tag{7}
\]
The checker uses affine Newton self-maps for the original logarithmic
equation, not numerical roots as certificates. Eight type/orientation
choices give 128 products of rectangle sides. Exact dyadic covers,
outward interval arithmetic and the strict tests (5) cover every
point of each product.

Along the straight segment from \(r\) to \(z\), only coordinate
\(j\) changes, by
\(w=x-\Re r_j-i\Im r_j\). The segment stays in the indicated
product. Taylor's integral remainder and (6) give
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
 =\int_0^1(1-t)\Re\{\phi_{jj}(r+tw)w^2\}\,dt
 \le7(\Im r_j)^2,                                       \tag{8}
\]
where \(r+tw\) means that only coordinate \(j\) is varied.
The strict version follows for nonzero displacement from (5).
This proves Theorem 1.

## 3. Meaning for the original finite source

The full conditional-source asymptotic applies throughout the target
products. Every type-four target is either an unchanged negative-height
reference or a real coordinate in \([.22,.5]\). The original
Fourier-polynomial upper bound therefore has rate \(-\Re g\) at
each such leg, including the possible equality of its two bounds at
one half. No relative asymptotic at that endpoint is needed.

Consequently, for every fixed \(\delta>0\), the allocated full finite
block obeys a uniform upper bound of the form
\[
 |\text{allocated block}|\le C_\delta N^A
       \exp N\{\Re\Gamma_r(z)+7(\Im r_j)^2+\delta\}.
 \tag{9}
\]
The unspecified fixed power \(A\) is harmless at this exponential
scale. An additional Fourier selection at the real coordinate has
modulus one and changes nothing in this upper bound. A selection at
the unchanged complex coordinate is not included.

The cost in (4) is positive. A global argument must pay for it from
the losses in adjacent blocks; this note alone is not a cyclic estimate.

## Reproduction

    python3 experiments/certify_mixed_single_height_reset.py --precision 256

For a replay of the saved cover without new root proposals:

    python3 experiments/certify_mixed_single_height_reset.py --precision 320 --input repro/results/research-mixed-single-height-reset.json --output /tmp/research-mixed-single-height-reset-review.json
