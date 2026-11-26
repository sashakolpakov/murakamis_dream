# The complete lower-left integral for a next type-four factor

Private research proof candidate, 8 November 2026. The entire first
incoming integration is now bounded on the shared interval
\([0,11/50]+ih_y\), with the complete next type-four factor attached.
The original cardinal correction and the denominator of the filtered
source satisfy the same required estimate. This removes that interval
from the remaining signed contour for this next type.

The theorem preserves the nonzero central contribution but does not
bound the other three remaining contours. It does not establish a
complete next transfer or an arbitrary short-filling theorem.
No numerical evaluation or frozen-source edit is used.

## 1. Original functions and integration cycle

Retain the actual ordinary-next reference family, action
\(\mathcal P_1^+(w,z)\), and affine plane \(\Lambda_{123}(z)\) of
[the lower central theorem](research_mixed_next_complete_lower_plateau.md),
with flags \((0,1,1)\). Both vertices after the first cap are
ordinary. Put
\[
\begin{gathered}
P=[11/50,9/20],\qquad J_L=[0,11/50],\\
y=q+ih_y,\quad q\in J_L,\quad -.102<h_y<-.001,\\
z=u+ih_z,\quad u\in P,\quad -.108\le h_z<0,\qquad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\end{gathered}                                                   \tag{1}
\]
All reference correlations and external typed inputs remain fixed.
At the actual output,
\[
\Lambda_{123}(z_*)=
 \Re\mathcal P_1^+(-2,z_*)-\tfrac12\Re g(z_*).                \tag{2}
\]

The complete finite functions are
\[
\begin{split}
F_N(w,Y)&=N\operatorname{CT}_X
                 [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
\mathscr D_{0,N}(w;y,z)&=F_N(w,Y)d_N(Y)C_{1,N}(Y,Z).
\end{split}                                                    \tag{3}
\]
Here \(U_{0,N}\), \(C_{1,N}\), and \(d_N\) are the original cap,
conditional kernel, and forced Fourier polynomial. In particular,
with \(r=e^{-2\pi i/N}\), \(p_j(V)=(rV;r)_j\), \(P_j=(r;r)_j\),
\[
C_{1,N}(X,Y)=
 \sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
\]
No conditional summation range is shortened in (3).

Use the same increasing-coordinate first cycle as the lower
central theorem:
\[
\begin{split}
\Gamma_a={}&[0,1/10]\\
&\cup\{x+ih_a(x-1/10)/(3/25):1/10\le x\le11/50\}\\
&\cup[11/50+ih_a,9/20+ih_a]
 \cup[9/20+ih_a,1/2+ih_a]\\
&\cup[1/2+ih_a,1/2]\cup[1/2,1],
\qquad -.072<h_a<0.
\end{split}                                                    \tag{4}
\]
The original exact constant-coefficient identity is
\[
F_N(w,Y)=N\int_{\Gamma_a}
 U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da.          \tag{5}
\]
It follows by deforming the full finite Laurent integrand in
the logarithmic cylinder. The orientation and factor \(N\)
are unchanged.

## 2. Every part of the first integration is bounded

**Theorem 1.** Uniformly on (1), for all real colors
\(-2\le w\le2\) and all sufficiently large levels of both parities,
\[
\boxed{\quad
|\mathscr D_{0,N}(w;y,z)|\,|d_N(Z)|^{1/2}
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}}.
\quad}                                                        \tag{6}
\]

*Proof.* The following statements all retain the entire following
product \(d_N(Y)C_{1,N}(Y,Z)\) and its outgoing halfweight.

The [initial and taper theorem](research_mixed_next_lower_left_incoming_initial_taper.md)
bounds the first two parts of (4), including their original
incoming measure, with deficit \(10^{-12}\).
The [central completion](research_mixed_next_lower_left_central_four_completion.md)
bounds the complete density on \(P+ih_a\) with deficit
\(10^{-11}\). Integrating it costs the polynomial factor
\(N|P|\). The
[right-horizontal theorem](research_mixed_next_lower_left_incoming_right_horizontal.md)
bounds the next horizontal part with deficit \(10^{-11}\).

Split the last real segment at \(7/10\). The
[incoming-corner completion](research_mixed_next_lower_left_incoming_corner_completion.md)
bounds the combined path
\([1/2+ih_a,1/2]\cup[1/2,7/10]\), with its orientation
and original measure, by a deficit \(10^{-10}\).
Its proof uses an exact replacement rectangle; no separate
absolute estimate on the two old corner sides is needed here.

On \([7/10,1]\), equation (24) of
[the original unselected right-tail theorem](research_mixed_next_unselected_incoming_right_tail.md)
gives the complete preceding-factor rate \(153/100\), uniformly
for \(|Y|\le1\). Since
\[
153/100<2383/1500,
\]
the [bounded-prefix attachment theorem](research_mixed_next_lower_left_bounded_prefix_four.md)
attaches the full next factor on the present interval, with
deficit \(1/100\). This bound also includes the real endpoint
and the original integration measure.

These pieces exhaust (4). Every following factor is independent
of \(a\), so each oriented integral estimate applies to (5)
with precisely the allocation in (6). Adding the finite number
of polynomial prefactors gives (6). \(\square\)

## 3. Fixed outside derivatives

The right-horizontal input was originally stated only as an
absolute real-color bound. Derivatives for the complete source
can instead be obtained after the exact assembly (5), using its
finite polynomial structure.

For fixed \(Y\), \(F_N(w,Y)\) has degree at most \(N-1\) in
the ordinary color \(w\). Indeed the original complete cap has
that degree, as recorded in
[all-real complementary bounds, Section 4](research_mixed_three_four_complementary_real_colors.md),
and constant-coefficient extraction in \(X\) does not increase it.
Its degree in \(Y\) is at most \(N-1\), directly from (3).
The next kernel has degree at most \(N-1\) in \(Z\), as does
\(d_N(Z)\). Consequently
\[
\mathscr H_N(w,Z;Y)=
       \mathscr D_{0,N}(w;y,z)^2d_N(Z)                       \tag{7}
\]
is a holomorphic polynomial of degrees at most \(2(N-1)\)
in \(w\) and \(3(N-1)\) in \(Z\). Moreover
\[
|\mathscr H_N|^{1/2}
=|\mathscr D_{0,N}|\,|d_N(Z)|^{1/2}
\]
at every point, including zeros of either factor.

Apply the elementary polynomial continuation argument of
[complex neighborhoods of horizontal bounds](research_mixed_horizontal_complex_extension.md)
to (7). Its ordinary Chebyshev estimate applies directly to
\(w\in[-2,2]\), and its logarithmic-arc estimate applies to
\(z\in P+ih_z\). The source bound is (6), with continuous
rate \(2\Lambda_{123}(z)-2\cdot10^{-12}\).
The reference and \(q\) are compact labels and are not
differentiated. The linear degree bounds are uniform.
Thus (6) extends to fixed small complex neighborhoods of
complete color and the actual output with any prescribed
smaller exponential deficit.

Only near that actual output do we remove the outgoing
halfweight. The original nonzero factorial packet for \(d_N(Z)\)
is uniform there and has logarithmic rate \(-\Re g(z)\).
Equation (2), the holomorphic action, and continuity then give
a fixed neighborhood on which
\[
\left|e^{-N\mathcal P_1^+(w,z)}
             \mathscr D_{0,N}(w;y,z)\right|
\le CN^B e^{-10^{-13}N}.                                    \tag{8}
\]
All paths, heights and reference labels are fixed at their
base values. Cauchy's formula on a smaller fixed neighborhood
gives every fixed mixed \(w,z\) derivative. Integration over
\(\gamma_L=J_L+ih_y\), with its original factor \(N\), adds only
a polynomial. In particular, for fixed nonnegative integers \(j,k\),
\[
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_1^+(w,z)}
 N\int_{\gamma_L}\mathscr D_{0,N}(w;y,z)\,dy\right]
 =O_{j,k}(e^{-10^{-14}N}).                                  \tag{9}
\]
No weighted derivative is inferred by division at an independent
outgoing zero.

## 4. The exact filter and its denominator

Keep the unchanged \(11/12\) filter, physical-node deletion,
and cardinal projection of the lower central theorem:
\[
\begin{split}
F_N^{\rm mid}&=(I-\Pi)(F_N-R_N^{\rm node}),\\
E_N^{\rm filt}&=F_N-F_N^{\rm mid},\\
K_N(y)&=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{1,N}(Y,Z)}
      {1-Y^N}.
\end{split}                                                    \tag{10}
\]
The notation \(E_N^{\rm filt}\) distinguishes this finite
correction from the reciprocal factorial used in earlier
conditional contour proofs. Its established disk bound is
\[
\sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
 \le CN^B e^{77N/50},\qquad -2\le w\le2.                    \tag{11}
\]
The source and exact correction identity are those in Section 3
of [the complete lower-right shoulder](research_mixed_next_complete_lower_right_shoulder.md).

Since \(77/50<2383/1500\), the bounded-prefix theorem applies
to (11) on the present lower-left interval, with the complete
next kernel and original forced shared weight. It gives
deficit \(1/100\), retaining \(|d_N(Z)|^{1/2}\).
This explicitly checks the new shared-variable domain; no
comparison from the old central interval is extrapolated.

Uniformly on \(\gamma_L\),
\[
|Y^N|\le e^{-\pi N/500},\qquad |1-Y^N|\ge1/2                \tag{12}
\]
for all sufficiently large \(N\), including the endpoint \(q=0\).
The exact difference is
\[
K_N-N\mathscr D_{0,N}
=N\,\frac{Y^NF_N-E_N^{\rm filt}}{1-Y^N}
                          d_N(Y)C_{1,N}(Y,Z).              \tag{13}
\]
The first numerator term uses (6), with the additional small
factor in (12). The second uses (11) and the just-checked
bounded-prefix theorem. Thus the original filter changes the
lower-left integral only by an exponentially bounded error
at the required rate.

For completeness the same outside derivative argument applies
to the correction product. The projection and node deletion
are linear in the \(Y\) coordinate and do not increase the
ordinary-color degree. Its squared product with \(d_N(Z)\)
has the same linear degree bounds in \(w,Z\) used in (7).
The denominator in (13) depends only on the fixed integration
variable and is bounded by (12). Polynomial continuation,
local removal of the actual outgoing packet, and Cauchy's
formula therefore give
\[
\boxed{\quad
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_1^+(w,z)}
                   \int_{\gamma_L}K_N(y)\,dy\right]
 =O_{j,k}(e^{-10^{-14}N}).
\quad}                                                        \tag{14}
\]
All original powers of \(N\), both Fourier forcing alternatives,
the filter cutoff and the finite interpolation are unchanged.

## 5. The enlarged lower interval and what remains

The established lower-central and shoulder theorem gives
\[
N\int_{[11/50,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
=N^{-5/2}\mathcal A_1(w,z)e^{N\mathcal P_1^+(w,z)}
                    (1+O_{\rm hol}(N^{-1})),
\]
with its original nonzero coefficient \(\mathcal A_1\).
Adding (9) proves the same expansion on the larger interval:
\[
\boxed{\quad
N\int_{[0,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
=N^{-5/2}\mathcal A_1(w,z)e^{N\mathcal P_1^+(w,z)}
                    (1+O_{\rm hol}(N^{-1})).
\quad}                                                        \tag{15}
\]
This is addition of specified original integrals. It does not
identify a full Fourier coefficient with this lower interval.

In the signed remainder from Section 4 of the shoulder theorem,
the lower-left term is now bounded by (14). For the next
type-four factor, the remaining three terms are
\[
\int_{[1/2,1]+ih_y}K_N(y)\,dy
 -\int_{[s,11/50]+iH}K_N(y)\,dy
 -\int_{[9/20,1-s]+iH}K_N(y)\,dy,\qquad H=1/100.              \tag{16}
\]
Here \(s>0\) is the same original upper seam cutoff.
Their signs, kernels, and selected Fourier coefficient remain.
No bound at the needed rate for their complete signed sum is
asserted here.

Write \(\mathscr R_N^{(3)}\) for (16). More precisely, if
\(\eta_{\rm old}>0\) is the error constant in equation (20) of
the shoulder theorem and
\(\eta_{\rm new}=\tfrac12\min\{\eta_{\rm old},10^{-14}\}\), then
\[
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_1^+(w,z)}
 \{\mathcal T_1[F_N]-I_{\rm geom,N}-\mathscr R_N^{(3)}\}\right]
 =O_{j,k}(e^{-\eta_{\rm new}N}).                              \tag{17}
\]
Here \(\mathcal T_1[F_N]\) is the original sum of the constant
and \(N\)-th Fourier coefficients, each with its factor \(N\),
and \(I_{\rm geom,N}\) is that theorem's original local
geometric integral. Equation (17) follows by adding (14) to
the existing exact decomposition and reducing the common
error constant. The coefficient or contour of
\(I_{\rm geom,N}\) is not changed.

For a next type-three factor, the present theorem does not apply:
the corresponding lower-left term is still among its outstanding
obligations. Arbitrary short-tangle attachments, and hence the
finite-exception theorem, remain open.
