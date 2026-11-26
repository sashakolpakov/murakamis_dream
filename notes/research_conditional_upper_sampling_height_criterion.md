# When a taller sampling rectangle ceases to improve the bound

Private written deduction, 11 November 2026. The exact phase of
the conditional sum determines when its upper sampling correction
decays as the rectangle is made taller. For a four-twist conditional
factor this condition restricts the outgoing real coordinate.
It is therefore a necessary domain check before extending the
current second-contour argument beyond its real midpoint.

This note does not show that the finite sum grows at this rate.
It concerns the individual sampling correction used in one
particular contour decomposition.

## 1. Original phase and the two corrected rates

Let \(a=x+ic\), \(b=q+id\), \(s=t+i\sigma\), and assume
\[
 0<x,q,t<1,\qquad x+t<1,\qquad q+t<1.
 \tag{1}
\]
Heights \(c,d\) lie in fixed compact real intervals. All logarithms
are the original branches on \(0<\Re z<1\). With
\(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})\), define
\[
 Q_\epsilon(s;a,b)
 =g(s+a)+g(s+b)-(2+\epsilon)g(s)
                 -g(a)-g(b)+2\pi ias,\qquad \epsilon\in\{0,1\}.
 \tag{2}
\]
The cases \(\epsilon=0,1\) are the original three- and four-twist
conditional phases. The additive constants in \(g\) are fixed
as in the original finite source.

The upper and lower cotangent corrections carry penalties
\(2\pi\sigma\) and \(-2\pi\sigma\), respectively. Their real rates are
\[
 W_+(t,\sigma;a,b)=\Re Q_\epsilon(t+i\sigma;a,b)-2\pi\sigma
                                      \quad(\sigma\ge0),
 \tag{3}
\]
\[
 W_-(t,\sigma;a,b)=\Re Q_\epsilon(t+i\sigma;a,b)+2\pi\sigma
                                      \quad(\sigma\le0).
 \tag{4}
\]
These are the exponential rates of the original interpolant
multiplied by \(\cot(\pi Ns)+i\) and \(\cot(\pi Ns)-i\), respectively.
The exact residue identity still has its original zero-mode
integral, two horizontal corrections, and four vertical
half-corrections.

## 2. Uniform limits of the original arguments

For \(0<u<1\) and \(R>0\), put
\[
                    \alpha_R(u)=\operatorname{Arg}(1-R e^{-2\pi iu}),
 \tag{5}
\]
using the continuous strip branch. On a compact subinterval
of \(0<u<1\),
\[
 \alpha_R(u)=\pi-2\pi u+O(R^{-1})\quad(R\longrightarrow\infty),
 \qquad
 \alpha_R(u)=O(R)\quad(R\longrightarrow0).
 \tag{6}
\]
To prove the first identity, factor
\[
 1-R e^{-2\pi iu}
 =R e^{i(\pi-2\pi u)}
                    (1-R^{-1}e^{2\pi iu}).
\]
For sufficiently large \(R\), the sum of the two displayed
arguments lies in the original branch and the last logarithm
is \(O(R^{-1})\), uniformly on the compact subinterval.
The second identity follows directly from the convergent
logarithm series near one.

The imaginary part of the derivative of (2) is
\[
 \begin{split}
 I_\epsilon(t,\sigma)
 ={}&\alpha_{e^{2\pi(\sigma+c)}}(x+t)
       +\alpha_{e^{2\pi(\sigma+d)}}(q+t)\\
    &-(2+\epsilon)\alpha_{e^{2\pi\sigma}}(t)+2\pi x .
 \end{split}
 \tag{7}
\]
The heights \(c,d\) do not alter the last
term: it is the imaginary part of \(2\pi ia\).
Substitution of (6) gives
\[
 I_\epsilon(t,\sigma)
  =-\epsilon\pi-2\pi q+2\epsilon\pi t
                         +O(e^{-2\pi\sigma})
                          \quad(\sigma\longrightarrow+\infty),
 \tag{8}
\]
\[
 I_\epsilon(t,\sigma)
       =2\pi x+O(e^{2\pi\sigma})
                          \quad(\sigma\longrightarrow-\infty).
 \tag{9}
\]
All assertions are uniform on compact parameter sets satisfying
the strict real-part inequalities (1). In particular, no
numerator crosses a real-part wall as its height varies.

## 3. The criterion for tall rectangles

Since \(\partial_\sigma\Re Q_\epsilon=-I_\epsilon\),
equations (3)--(4) and (8)--(9) give
\[
 \begin{split}
 W_+(t,\sigma;a,b)
  &=\kappa_\epsilon(t,q)\sigma+C_+(t,a,b)
                                 +O(e^{-2\pi\sigma}),\\
 \kappa_\epsilon(t,q)
  &=\pi\{\epsilon(1-2t)+2q-2\},
                        \qquad \sigma\longrightarrow+\infty,
 \end{split}
 \tag{10}
\]
and
\[
 W_-(t,\sigma;a,b)
   =2\pi(1-x)\sigma+C_-(t,a,b)+O(e^{2\pi\sigma})
                        \quad(\sigma\longrightarrow-\infty).
 \tag{11}
\]
The constants exist because the errors in the derivative
formulas are integrable. They remain bounded on each fixed
compact parameter set. No value of either constant is needed.

**Proposition.** On such a nonempty compact parameter set,
the upper rate can be made uniformly smaller than any prescribed
real number by taking the upper height sufficiently large
if and only if
\[
                         \max\kappa_\epsilon(t,q)<0.
 \tag{12}
\]
The lower rate always tends uniformly to \(-\infty\) as its
height tends to \(-\infty\).

*Proof.* If (12) holds, (10) has a uniform strictly negative
linear coefficient and a bounded constant and remainder.
If (12) fails, compactness supplies a parameter with
\(\kappa_\epsilon\ge0\). At this parameter (10) either tends
to \(+\infty\) or to a finite limit. Increasing the height
therefore cannot achieve arbitrarily negative rates.
The lower assertion follows from (11), because
\(\max x<1\) on the compact set. \(\square\)

For \(\epsilon=0\), \(\kappa_0=2\pi(q-1)<0\); the strict strip
condition already supplies the required sign.
For \(\epsilon=1\), the upper condition is instead
\[
                              q<t+\frac12.
 \tag{13}
\]
At equality the rate has a finite limit, so arbitrarily large
loss cannot be obtained merely by making the rectangle taller.

## 4. Consequence for the current second-contour extension

The first four-twist conditional factor in the completed
\(4,4\) prefix uses the left private cut \(t=1/8\). At that
cut (13) becomes
\[
                               q<\frac58.
 \tag{14}
\]
For \(5/8<q<7/8\), and for incoming real parts with
\(0<x<7/8\), all strict strip conditions at this cut can
still hold. Nevertheless,
\[
 W_+(1/8,\sigma;a,b)
       =2\pi(q-5/8)\sigma+C_+(1/8,a,b)
                                  +O(e^{-2\pi\sigma})
                         \longrightarrow+\infty .
 \tag{15}
\]
This failure precedes the outgoing numerator wall \(q+t=1\).
It cannot be repaired by asserting that the factorial arguments
remain in their regular strip: they do remain there.

The negative-height main profiles may still have a useful
comparison with the real half face. Such a comparison does not
control (15). A proof on the later real interval must instead
bound a specified finite-height upper correction, change the
private decomposition with all resulting terms retained, or
use another exact representation of the finite sum.

The obstruction is to the particular tall-rectangle estimate.
It neither proves growth of the integrated correction after
cancellation nor disproves a smaller bound for the original
finite polynomial. It also makes no assertion about a
nonzero leading coefficient.

## Source and review scope

The only algebra used in the proof is the original phase (2)
and the cotangent penalties in (3)--(4). The latter agree with
[the asymmetric contour construction](research_mixed_horizontal_asymmetric_contour.md),
Sections 1 and 4, version
2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce.
Its allocated phase differs from (2) only by
\(-(\eta/2)g(a)-(\epsilon/2)g(b)\), where its left allocation
flag is \(\eta\in\{0,1\}\). These terms are independent of
\(\sigma\), so they change \(C_\pm\) but neither slope nor
criterion.
The argument above derives all new assertions directly; it
does not import that source's restricted-domain argument bounds.

The author has read the full proof and checked that source
convention. Independent full proof review is required before
adoption. No mathematical numerical evaluation, test, import,
compilation, or saved-value arithmetic was used.

