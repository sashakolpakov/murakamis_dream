# Why a private-row triangle bound cannot replace the coherent cap

Research deduction, 5 November 2026. At every actual type-four endpoint
image, the sum of the absolute private-row contributions to the first
cap has an exponentially larger rate than the cap itself. This is a
uniform obstruction to using that triangle bound near the reference.
It is not an obstruction to the already proved cap packet, or to the
original open-source asymptotic. No new roots, parameter cover or
numerical optimization are used.

## 1. The literal sum and the original image

Use the exact finite source and normalization of
[the complete first-cap theorem](research_mixed_complete_first_cap_packet.md).
At the complete ordinary color,
\[
\begin{split}
 U_{1,N}(-2,X)&=\sum_{i=0}^{N-1}A_{i,N}(X),\\
 A_{i,N}(X)&=
     \frac{H_N(-2,r^{-i})p_i(X)}{P_i^2}
     =D_N(i/N)^{-1}\mathcal C_N(i/N,-2)
                         \frac{p_i(X)}{P_i},\\
 r&=e^{-2\pi i/N},\qquad
 P_i=(r;r)_i,\qquad p_i(X)=(rX;r)_i,\\
 T_N(X)&=\sum_{i=0}^{N-1}|A_{i,N}(X)|.
\end{split}                                                   \tag{1}
\]
The last expression is the actual absolute private-row sum, not an
upper bound obtained by replacing its inner endpoint coefficient.
All private indices and both level parities are retained.

Let \(K_4\) be the compact union of the two original type-four
attached endpoint images, with the separately certified one-vertex
image included, as in the complete cap theorem. Set
\(X=e^{-2\pi iz}\), \(z\in K_4\). The
[exact endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give, uniformly on these images,
\[
\begin{split}
 .246<\Re z<.350,&\qquad -.108<\Im z<-.020,\\
 .333<\Re e_*(z)<.363,&\qquad -.051<\Im e_*(z)<-.019.
\end{split}                                                   \tag{2}
\]
Here \(e_*(z)\) is the original private critical coordinate.
The image theorem includes all saved endpoint maps and the
one-vertex points; (2) is not inferred from samples.

With the original primitive \(J'(v)=\operatorname{Log}(2\sin\pi v)\),
put \(g(v)=J(v)+i\pi(v-v^2)/2\), and use the full endpoint
phase \(S(e)=S(e,-2)\). The actual cap phase and its selected
rate are
\[
 \Psi_1(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-g(e),\qquad
 M_1(z)=\Re\Psi_1(e_*(z),z),\qquad
 \Psi_{1,e}(e_*(z),z)=0.                                 \tag{3}
\]
The complete cap packet is
\[
 U_{1,N}(-2,e^{-2\pi iz})
   =N^{-3/2}\mathcal B_1(z,-2)e^{N\Psi_1(e_*(z),z)}
                        (1+O(N^{-1})),
 \qquad \mathcal B_1\ne0,                               \tag{4}
\]
uniformly on \(K_4\).

## 2. A strict vertical increase to a real private row

Write \(e_*=x_*+ih_*\). The entire vertical segment
\(e=x_*+iy\), \(h_*\le y\le0\), lies in
\([.27,.49]+i[-.055,.04]\). The complete endpoint rectangle
packet and Lemma 1 of
[the cap contour reduction](research_mixed_cap_outer_contour_reduction.md#3-curvature-and-the-lower-real-half)
apply throughout this segment. In particular the original endpoint
Schur calculation proves \(-\Re S''(e)>0\) there.
Also (2) gives
\(.579<\Re(e+z)<.713\), so \(\Re\cot\pi(e+z)<0\).
Consequently
\[
 -\Re\Psi_{1,ee}(e,z)
 =-\Re S''(e)-\pi\Re\cot\pi(e+z)+\pi\Re\cot\pi e
                       >\pi\Re\cot\pi e>\frac\pi6.
                                                               \tag{5}
\]
For the last inequality, \(.333<x_*<.363\) gives
\(\sin(2\pi x_*)>1/2\). Moreover \(|y|<.051\), so
\(2\pi|y|<1/2\), \(\cosh(2\pi y)<2\), and
\(\cosh(2\pi y)-\cos(2\pi x_*)<3\). Apply the exact
real-cotangent formula with this positive denominator. These are
uniform analytic bounds on the whole vertical segment.

The function \(f(y)=\Re\Psi_1(x_*+iy,z)\) has
\(f'(h_*)=0\) and \(f''(y)>\pi/6\). Integrating twice,
\[
 \Re\Psi_1(x_*,z)-M_1(z)
       >\frac\pi{12}h_*^2
       >\frac{361}{4000000}>\frac1{12000}.               \tag{6}
\]
Here \(|h_*|>19/1000\) and \(\pi>3\). This is an increase
in the real private-row rate, not a competing critical point.

## 3. The real row has its stated finite-source rate

For each \(N\), choose a physical index \(i_N\) nearest to
\(Nx_*\), and put \(e_N=i_N/N\). For all sufficiently large
levels, \(e_N\) lies in a compact real subinterval of the
proved endpoint rectangle. The exact retained-row interpolation in
equations (4) and (7) of the cap contour reduction equals the
literal summand in (1) at \(e=e_N\). At type four its packet is
\[
 A_{i_N,N}(e^{-2\pi iz})
  =N^{-2}\,a(e_N,z)e^{N\Psi_1(e_N,z)}(1+O(N^{-1})),
                                                               \tag{7}
\]
where
\[
 a(e,z)=\mathcal A(e,-2)
       \sqrt{\frac{\sin\pi(e+z)}{\sin\pi z}}
       (2\sin\pi e)^{-1/2}e^{i\pi e/2}
                                                               \tag{8}
\]
has the original branches and is nonzero. Every sine argument stays
regular on this compact set. Since \(\Im z<0\), \(|X|<1\),
and no factor of \(p_{i_N}(X)\) vanishes. The original real
index endpoint packet already includes all Newton rows and their
odd-level zeros, so no omitted subrow or parity condition is used
in (7).

The symbol in (8) is uniformly bounded away from zero. The bounded
derivative of \(\Psi_1\), together with
\(|e_N-x_*|\le1/(2N)\), changes its exponential by only a
uniform fixed factor. Equations (6)--(7) therefore give constants
\(c>0,N_0\), independent of \(z\in K_4\), such that
\[
 T_N(e^{-2\pi iz})\ge |A_{i_N,N}(e^{-2\pi iz})|
        \ge cN^{-2}\exp N\{M_1(z)+1/12000\}
                    \qquad(N\ge N_0).                  \tag{9}
\]
This lower bound uses one actual physical summand of the absolute
sum. It is stronger than showing that a proposed upper estimate
looks too large.

**Theorem 1.** Uniformly on the original compact type-four outgoing
images, the private-row triangle norm has an exponential excess:
\[
 \liminf_{N\to\infty}
 \left\{N^{-1}\log T_N(e^{-2\pi iz})-M_1(z)\right\}
       \ge\frac1{12000},
 \qquad
 \frac{T_N(e^{-2\pi iz})}
      {|U_{1,N}(-2,e^{-2\pi iz})|}
       \ge c' N^{-1/2}e^{N/12000}                       \tag{10}
\]
for one \(c'>0\) and all sufficiently large levels. The
uniform interpretation of the first inequality follows directly
from (9); the second also uses the upper half of (4).

## 4. Consequence for a boundary comparison

At the original reference, every adjacent coherent residual edge
has value zero, and the pinned-completion occupation and quadratic
fees are also zero. Replacing the literal \(|U_{1,N}|\) in a
boundary product by \(T_N\) therefore introduces the positive
rate in (10) precisely where there is no adjacent completion loss
to pay it. Multiplication by the other nonzero local source factors
does not change that ratio. Such a replacement cannot prove a
boundary ceiling at the correct critical rate, even with arbitrary
polynomial prefactors.

The same warning applies to any still larger triangular envelope
for these private rows. This does not invalidate the Newton
envelopes as upper bounds, their use on discarded regions, or
their ordinary-color tube estimates. It says that a global
boundary sign argument must retain coherent cap control near the
reference, as the existing cap theorem already does. Its remaining
task is to combine that local control with the exact complementary
rows and adjacent interior energy.

The obstruction is stated at the complete ordinary color. Any
purported uniform color-neighborhood ceiling would include that
color and hence face the same obstruction; no extra moving-color
asymptotic is needed for this conclusion. It is not a counterexample
to the complete cap or to a whole open-chain invariant.
