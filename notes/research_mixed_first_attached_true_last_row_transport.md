# Transport of the true last row beside the first cap

Research deduction, 7 November 2026. The exact true-last-row
alternative in the complete adjoining source envelope has a
nondecreasing rate under the early first-height move, with the
neighboring target fixed. For own type four the statement below
requires the full, unattenuated attached-height coefficient; for
own type three it allows an additional fixed attenuation.

This concerns one endpoint of the high physical tail. It does not
bound its interior critical values or the change of the neighboring
height. The deduction is separate from the central/cut theorems.

## 1. Exact source endpoint and allocation

Keep the source and notation of the
[complete adjoining contour envelope](research_mixed_first_attached_complete_contour_envelope.md),
especially equations (17)--(18). The first and second own types
are \(3+\alpha,3+\epsilon\). For the same retained targets
\(a=x+ih\), \(b=z+ih_b\), the exact limiting last-row rate is
\[
 \mathcal R_{\alpha\epsilon}(1;a,b)
   =2\pi(-h)_++2\pi(h_b)_+
       -\frac{\alpha}{2}\Re g(a)-\frac{\epsilon}{2}\Re g(b).
                                                               \tag{1}
\]
The original finite-product estimate retains the actual final row,
its rounding, possible zeros and both level parities. Equation (1)
is its rate, not a new replacement for the finite polynomial.

The complete cap envelope is allocated by another
\(-\alpha\Re g(a)/2\). Its regular contribution together with
(1) is therefore
\[
 \mathcal L_\alpha(e;x)
 =\Re\Psi_\alpha(e,a)-\alpha\Re g(a)
                 +2\pi(-h)_+ +C_b,\qquad
 C_b=2\pi(h_b)_+-\frac{\epsilon}{2}\Re g(b),                    \tag{2}
\]
where \(e\in[.27,.49]\) is real.
The neighboring target \(b\) and ordinary color are fixed.
The exact first-cap marginal is
\(\Psi_{\alpha,a}=g'(e+a)-g'(a)\).

Take
\[
 a=x-i\lambda(x-.1),\qquad .1\le x\le.22,\qquad
                            \lambda=-c/.12.                  \tag{3}
\]
For own three, \(-.072<c<.021\), or any fixed attenuation of
such a coefficient. For own four in Section 3 require
\[
                  -.078<c<-.020,\qquad
                         1/6<\lambda<13/20.                 \tag{4}
\]
Thus (4) uses the actual coupled attached coefficient with no
additional attenuation. It applies to the actual minimum-cutoff
graph on a first-minimum segment where
\(L(x)\le L(z)\): the first coordinate has \(R(x)=1\) and its
height is exactly \(cL(x)\).
The actual \(m\ge3\) ordinary/Fourier-ended eligibility for (4)
is the one proved in Section 1 of the
[own-four moving comparison](research_mixed_first_four_moving_height_comparison.md).
No two-endpoint length-two claim is made.

## 2. Own-three regular and true-end cap alternatives

Put \(p_e=g'(e+a)-g'(a)\). The same-radius bound and the
original rotated-ratio argument in Section 3 of the
[moving-height reduction](research_mixed_first_attached_moving_height_reduction.md)
give
\[
 \Re p_e>\frac{21}{242},\qquad
 \begin{cases}
 \Im p_e\ge-\pi e,&h\le0,\\
 \Im p_e\le-\pi e,&h\ge0.
 \end{cases}                                                  \tag{5}
\]
These hold for the full \(e\in[.27,.49]\) and the stated
own-three heights, including effective fixed attenuations.

If \(\lambda\ge0\), differentiation of (2) gives
\[
 \mathcal L_0'(e;x)
 =\Re p_e+\lambda\Im p_e+2\pi\lambda
 \ge\Re p_e+\lambda\pi(2-e)>\frac{21}{242}.                    \tag{6}
\]
If \(\lambda\le0\), the \(2\pi(-h)_+\) term is zero and
\[
 \mathcal L_0'(e;x)
 =\Re p_e+\lambda\Im p_e
 \ge\Re p_e-\lambda\pi e>\frac{21}{242}.                       \tag{7}
\]
The endpoint \(x=.1\) uses the corresponding right derivative.
For \(\lambda=0\), (5) proves the same strict bound.

The complete cap also retains its true-index exponent
\[
                  E_{\rm end}(h)=\frac35+2\pi h_+
                                      +\frac{\log4}{100}.
                                                               \tag{8}
\]
Combined with (1), at \(\alpha=0\) it is exactly
\[
 \frac35+\frac{\log4}{100}+2\pi|h|+C_b.
                                                               \tag{9}
\]
Its derivative is \(2\pi|\lambda|\ge0\).
Thus the maximum of the regular alternatives (6)--(7) and
(9) is nondecreasing in \(x\). No strict uniform slope is
asserted for that complete maximum: (9) is constant if \(c=0\).
The unchanged regular angular-loss term does not affect these
derivatives, and the unpenalized true-end alternative is retained.

## 3. Own-four transport with the actual height coefficient

For own four use the proved cap half-stencil
\[
 H^{\rm cap}_1(e)
 =\Re[(1-i\lambda)
       \{g'(e+a)-\tfrac32g'(a)+\tfrac32 i\}]>\frac1{600}
                                                               \tag{10}
\]
from the
[complete cap-envelope transport](research_mixed_cap_early_taper_envelope_transport.md).
By (2)--(4),
\[
 \begin{split}
 \mathcal L_1'(e;x)-H^{\rm cap}_1(e)
 =-\frac12\Re g'(a)
        +\lambda\{2\pi-\tfrac32-\tfrac12\Im g'(a)\}.
 \end{split}                                                   \tag{11}
\]
On this lower-half early tube,
\[
 \Re g'(a)<\log2<\frac7{10},\qquad
                   0<\Im g'(a)\le\frac{2\pi}{5}.              \tag{12}
\]
The first inequality is the modulus bound
\(|1-re^{-2\pi ix}|\le1+r\le2\).
The second uses the original radial argument between zero and
\(\pi(1/2-x)\), with \(r=e^{2\pi h}\le1\).
Since \(\lambda>1/6\) and \(\pi>157/50\), equations (11)--(12)
imply
\[
 \mathcal L_1'(e;x)-H^{\rm cap}_1(e)
 >-\frac7{20}+\frac16\left(\frac{9\pi}{5}-\frac32\right)
 >\frac{171}{500}.                                           \tag{13}
\]
It follows that
\[
                    \mathcal L_1'(e;x)>\frac{1031}{3000}
                                              >\frac13.       \tag{14}
\]

The complete own-four cap true-end alternative is strictly
dominated, with its angular allowance included, on this actual
early tube by Proposition 1 of the cap-envelope transport theorem.
That pointwise domination is preserved by adding the same entire
row rate (1). Taking the maximum over \(e\) after integrating
(14) therefore proves
\[
 \mathcal L_1^{\rm complete}(x_0)
 \le \mathcal L_1^{\rm complete}(x_1)
                      -\frac{x_1-x_0}{3},
                       \qquad .1\le x_0<x_1\le.22 .           \tag{15}
\]
There is no assumption of differentiable maximizing private index.

The lower bound \(\lambda>1/6\) is essential to this proof.
Equation (15) is not asserted after an arbitrary additional
attenuation of the own-four reference coefficient. The actual
first-minimum segment in Section 1 needs no such attenuation.

## 4. Scope of the additional endpoint payment

The statements concern the exact \(u=1\) endpoint of the high-row
rate, after its complete cap alternative is included at the same
target. The adjoining own type \(\epsilon\) is arbitrary because
its \(b\)-dependent terms are constant during this comparison.

The contour envelope still includes every admissible interior
critical value of its quartic/sextic high-tail equation.
No endpoint maximum principle for that rate has been invoked.
Nor has the two-incidence neighboring-height term in equation (23)
of the moving-height reduction been paid. If the actual minimum
move changes \(b\)'s height, its derivative must be added to
(6), (7) or (14). The original complex marginal, middle
compensation and relative pinning fee remain unchanged.
No complete compensated boundary sign or whole-source conclusion
is inferred.

