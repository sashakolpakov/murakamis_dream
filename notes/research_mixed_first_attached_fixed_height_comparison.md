# A fixed-height joint comparison beside the first cap

Research deduction, 7 November 2026. The new complete contour envelope
admits an analytic comparison in the first retained real coordinate.
The central term is covered when the fixed ordinary index height is
nonpositive; its two real-cut terms are covered for either adjoining
type. Both first-cap branches are retained, including the type-three
true-index ceiling. The shared first-coordinate allocation is kept
before the comparison.

This pays the fixed-height switch only. It does not pay the switch
that changes the first or neighboring heights, the remaining high-row
stationary values, or the compensated boundary functional.

## 1. Same-target profiles and their exact allocation

Use the original phases and target domain of the
[complete adjoining contour envelope](research_mixed_first_attached_complete_contour_envelope.md).
Write
\[
 a=x+ih,\quad .1\le x\le.22,\quad -.108\le h\le.021,\qquad
 e\in[.27,.49],\quad s=v+i\eta,\quad v\in[.2,.49].
 \tag{1}
\]
In this note \(\eta\le0\). The second retained target \(b\), the
heights \(h,\eta\), the real private coordinates \(e,v\), and all
ordinary-color parameters stay fixed when \(x\) changes. The first
and second types are \(3+\alpha,3+\epsilon\).

The joint regular profile is exactly
\[
 \mathcal J_{\alpha\epsilon}(e,s;a,b)
   =\Psi_\alpha(e,a)-\frac{\alpha}{2}g(a)
                           +F_{\alpha\epsilon}(s;a,b),
 \tag{2}
\]
with the notation of that envelope. In particular both allocated
first-coordinate halfweights occur once, and the next coordinate
has its original \(\epsilon/2\) halfweight. The original cap
derivative and ordinary chirp give
\[
 \partial_a\mathcal J_{\alpha\epsilon}
  =g'(e+a)+g'(s+a)-(2+\alpha)g'(a)+2\pi i s.
 \tag{3}
\]
No reference marginal has been changed. The second target and its
allocation disappear from this derivative because they are fixed.

## 2. The chirp restores the common-radius comparison

**Lemma 1.** Throughout (1), for every \(\eta\le0\),
\[
 \Re\partial_a\mathcal J_{\alpha\epsilon}>
 \begin{cases}
  21/121,&\alpha=0,\\
  1/66,&\alpha=1.
 \end{cases}
 \tag{4}
\]
The derivative is the fixed-height derivative in \(x\).

*Proof.* Put \(r=e^{2\pi h}\), \(R=e^{2\pi\eta}\), and
\[
 B=|1-re^{-2\pi ix}|^2,\qquad
 A_0=1+r^2+\frac{12}{25}r,\qquad
 B_0=1+r^2-\frac9{25}r.
 \tag{5}
\]
The elementary bounds proved in the
[real-private half-stencil](research_mixed_cap_real_private_half_stencil.md)
give
\[
 \frac12<r<\frac{23}{20},\qquad
 \cos(2\pi x)>\frac9{50},\qquad B<B_0<2.
 \tag{6}
\]
They also give
\[
 \cos2\pi(e+x)<-\frac6{25}.
 \tag{7}
\]
The same cosine bound holds for \(v+x\in[.3,.71]\).
Indeed its maximum on that interval is at an endpoint;
\(\cos(.6\pi)=(1-\sqrt5)/4<-1/4\), while
\(\cos(1.42\pi)=-\sin(.08\pi)<-6/25\), the latter being
the identical sine witness used for (7).

The chirp term in (3) has real part \(-2\pi\eta=-\log R\).
Thus
\[
 \begin{split}
 \Re\partial_a\mathcal J_{\alpha\epsilon}
   =\log\frac{
     |1-re^{-2\pi i(e+x)}|\,
     |R^{-1}-re^{-2\pi i(v+x)}|}
                     {|1-re^{-2\pi ix}|^{2+\alpha}}.
 \end{split}
 \tag{8}
\]
This exact placement of \(R^{-1}\) is essential. Since \(R^{-1}\ge1\),
\[
 \begin{split}
 |1-re^{-2\pi i(e+x)}|^2&>A_0,\\
 |R^{-1}-re^{-2\pi i(v+x)}|^2
   &>R^{-2}+r^2+\frac{12}{25}R^{-1}r\ge A_0.
 \end{split}
 \tag{9}
\]
Consequently (8) is strictly larger than
\(\log A_0-(1+\alpha/2)\log B\).

For \(\alpha=0\), \(A_0-B>(21/25)r>21/50\), and
\(B<2\) implies \(A_0/B>121/100\). Therefore
\[
 \log(A_0/B)>\log(121/100)>\frac{21}{121}.
 \tag{10}
\]
For \(\alpha=1\), the exact polynomial calculation in the
half-stencil proof gives, on precisely the interval (6),
\[
 A_0^2-B_0^3>\frac r2>\frac14.
 \tag{11}
\]
Since \(B<B_0<2\), this implies \(A_0^2/B^3>33/32\).
The required lower bound is therefore
\[
 \log A_0-\frac32\log B
   =\frac12\log(A_0^2/B^3)
   >\frac12\log(33/32)>\frac1{66}.
 \tag{12}
\]
Both logarithmic estimates use only
\(\log(1+t)>t/(1+t)\). This proves (4). \(\square\)

This proof needs no stationarity in either private variable.
In particular it applies at the two fixed ordinary cuts \(v=.2,.49\)
with \(\eta=0\), and at every point of a fixed ordinary contour
whose height is nonpositive.

## 3. The type-three true-end cap branch is included

For \(\alpha=0\), the complete cap envelope retains the alternative
\(E_{\rm end}(h)\). At fixed \(h\) it is constant in \(x\).
The corresponding joint profile is
\[
                     E_{\rm end}(h)+\Re F_{0\epsilon}(s;a,b).
 \tag{13}
\]
Its derivative is
\[
 \begin{split}
 \Re\partial_a F_{0\epsilon}
 &=\log\frac{|R^{-1}-re^{-2\pi i(v+x)}|}
                         {|1-re^{-2\pi ix}|}\\
 &>\frac12\log(A_0/B)>\frac{21}{242}.
 \end{split}
 \tag{14}
\]
Thus it also increases. No dominance assumption for this endpoint
branch is needed. For \(\alpha=1\), the
[completed early cap theorem](research_mixed_cap_early_taper_envelope_transport.md)
already makes its true-end branch inactive on the actual
\(c\le h\le0\) tube; that actual-reference premise is retained here.

## 4. Consequence for the complete central and cut envelopes

Let \(\mathcal C_\alpha(a,\vartheta)\) denote the ungauged
complete allocated cap envelope in equation (21) of the adjoining
envelope theorem. Choose its angular constant uniformly on the
compact target family, so it does not vary with \(x\). Define
\[
 \begin{split}
 \mathcal M_\alpha(x)
   &=\mathcal C_\alpha(x+ih,\vartheta)
                         +B_{\alpha\epsilon}^{\,0}(x+ih,b;\eta),\\
 \mathcal K_{\alpha,c}(x)
   &=\mathcal C_\alpha(x+ih,\vartheta)
                         +\Re F_{\alpha\epsilon}(c;x+ih,b),
                 \qquad c\in\{.2,.49\}.
 \end{split}
 \tag{15}
\]
Here \(\eta\in[-.108,0]\) for the central bound, whereas both
cut bounds use their literal zero index height. Retain the actual
first-cap eligibility and its height restrictions. For type three,
an interval \([x_0,x_1]\subset[.1,.22]\) used below must satisfy
the positive-height cap condition
\(h\le(7/40)(x_0-.1)\). This is automatic when starting at an
actual early target and raising \(x\) while holding its height fixed.

For either function in (15), and every such \(x_0<x_1\),
\[
 \boxed{\quad
 \mathcal E(x_0)\le\mathcal E(x_1)
                 -\delta_\alpha(x_1-x_0),\qquad
 \delta_0=\frac{21}{242},\quad \delta_1=\frac1{66}.
 \quad}
 \tag{16}
\]
To prove this, integrate (4) for every fixed \(e,v\), or for the
fixed cut \(v=c\). For the second type-three cap branch use (14).
Then take the maxima over the unchanged compact private intervals
and, when present, the two cap alternatives. No differentiability
of a maximizing private coordinate is required. The angular term
is constant during this operation.

The fixed-height central comparison applies to every adjoining
own-four factor, since its original index height is negative. For
an adjoining own-three factor it covers only the nonpositive-index
height subfamily. The two cut comparisons apply to both adjoining
types, without a condition on their original index heights.

Equation (16) is a genuine reduction of these same-target scalar
comparisons toward \(x=.22\). The heights and second target at its
right endpoint are still the frozen ones used in (15), not silently
reset to their original reference values. The theorem neither pays
the other high physical-tail stationary values nor identifies
\(\mathcal E(.22)\) with the calibrated geometric action.
Simultaneous first-height and neighboring-height motion, the original
middle compensation and relative pinning fee remain separate. No
complete minimum-level or compensated boundary sign is asserted.
