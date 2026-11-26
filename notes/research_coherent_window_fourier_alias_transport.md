# Coherent scalar window errors and their charged Fourier aliases

Private written proof, 16 November 2026.

Scalar compatibility removes the zero Poisson alias from the interior
part of the midpoint normal pairing. The other aliases admit a common
contour estimate with the original unit filling charge. Four actual
endpoint jets and the finite contour endpoint packets remain explicit.
The estimate requires one scalar error function controlled on both
signed height contours; separate one-sided representatives do not
supply this hypothesis.

This concerns the original coherent pairing, not an absolute bound on
its real profile. It does not by itself control the endpoint packets,
the remaining closing functional, or a global filled cycle.

## 1. Exact scalar compatibility and the endpoint polynomial

Use the centered coordinate
\[
 X_j=(j+\tfrac12)/N,\qquad
 a=k_0/N,\quad b=k_1/N,\quad k_0\le j<k_1,
 \qquad I=[a,b].                                      \tag{1}
\]
The length of the window is bounded above and below by fixed positive
constants. Integer endpoints may depend on \(N\), within fixed buffered
real intervals. This is the translated midpoint convention of the
pinned Fourier/normal identity.

Let the normalized value and normal errors satisfy the exact condition
\[
             d_j=f_N(X_j),\qquad e_j=f_N'(X_j),          \tag{2}
\]
for a single holomorphic function \(f_N\) near \(I\). In particular,
the prime is the derivative of the normalized value: if an unnormalized
scalar difference is \(e^{NS_N}f_N\), its normalized normal is
\(e^{-NS_N}\partial_X(e^{NS_N}f_N)-NS_N'f_N=f_N'\).
An independent normal channel is not replaced by this expression.
Condition (2) is a source hypothesis, to be checked for the actual
representatives under consideration.

Keep the entire original weighted spectator
\[
 A_N(X)=e^{NS_N(X)}\sin(2\pi X)\,P_N^{\mathrm{sp}}(X), \tag{3}
\]
where \(P_N^{\mathrm{sp}}\) includes the original quadratic filling
carrier, other factors and every shared parameter. The notation
\(P_N^{\mathrm{sp}}\) denotes this spectator, not the spectral relation.
Define
\[
 \begin{split}
 c_f(\xi)&=\sum_{j=k_0}^{k_1-1}
       [f_N'(X_j)-2\pi iN\xi f_N(X_j)]e^{-2\pi iN\xi X_j},\\
 \widehat A_N(\xi)&=\int_a^b A_N(X)e^{2\pi iN\xi X}\,dX,\\
 \mathfrak P_N[f,A]&=\pi N\int_{-1}^1 c_f(\xi)
                                      \widehat A_N(\xi)\,d\xi .
 \end{split}                                           \tag{4}
\]
This is exactly the pinned midpoint pairing applied to the error jets.
Translation of its uncentered coordinate introduces opposite unit
characters in its two Fourier factors, which cancel in (4).

Let \(L=b-a\), \(r=(X-a)/L\), and form the actual endpoint cubic
\[
 \begin{split}
 p_N(X)={}&f_N(a)(2r^3-3r^2+1)
       +Lf_N'(a)(r^3-2r^2+r)\\
     &+f_N(b)(-2r^3+3r^2)+Lf_N'(b)(r^3-r^2),\\
 g_N&=f_N-p_N .
 \end{split}                                           \tag{5}
\]
Thus \(g_N=g_N'=0\) at both endpoints. No endpoint datum in (5) is
assumed zero. The finite cubic packet \(\mathfrak P_N[p,A]\) is explicit
in these four data. For example, put
\[
 Z_N(\xi)=e^{-2\pi i\xi(k_0+1/2)}
       \frac{1-e^{-2\pi i\xi(k_1-k_0)}}{1-e^{-2\pi i\xi}},
 \qquad \mathcal D=-\frac1{2\pi iN}\partial_\xi .      \tag{6}
\]
All apparent singularities at integer \(\xi\) are removable. Then
\[
 c_p(\xi)=p_N'(\mathcal D)Z_N(\xi)
                    -2\pi iN\xi p_N(\mathcal D)Z_N(\xi).\tag{7}
\]
Here the displayed \(\xi\) multiplies after the polynomial differential
operator has acted. Formula (7), followed by (4), is one finite formula
for the endpoint cubic packet.

## 2. Exact alias cancellation

Extend \(g_N\) by zero outside \(I\), and write
\[
 \widehat g_N(\omega)=\int_a^b
                     g_N(y)e^{-2\pi i\omega y}\,dy .   \tag{8}
\]
The extension is \(C^1\) and piecewise analytic. Three integrations by
parts, retaining the endpoint second derivatives in the last one, give
\(\widehat g_N(\omega)=O_N((1+|\omega|)^{-3})\).

**Proposition 1.** For \(-1\le\xi\le1\), exactly
\[
 \boxed{\quad
 c_g(\xi)=-2\pi iN^2
    \sum_{m\in\mathbb Z\setminus\{0\}}
          m(-1)^m\widehat g_N\bigl(N(\xi-m)\bigr).
 \quad}                                                \tag{9}
\]
The series is absolutely and uniformly convergent in \(\xi\) for each
level. In particular its zero alias is identically absent.

**Proof.** Periodize the compactly supported function
\(g_N(y)e^{-2\pi iN\xi y}\) on a period of length \(1/N\), and evaluate
its Fourier series at \(1/(2N)\). Its Fourier coefficients are the
transforms in (8), and the centered evaluation gives \((-1)^m\).
The same operation on \(g_N'\) is legitimate with absolute convergence:
integration by parts gives
\(\widehat {g_N'}(\omega)=2\pi i\omega\widehat g_N(\omega)\),
because \(g_N\) vanishes at both ends. Subtracting the value term in
(4) leaves \(2\pi iN[(\xi-m)-\xi]=-2\pi iNm\), in addition to the
comb factor \(N\). This proves (9). The cubic subtraction ensures the
decay needed also for the derivative series. The \(m=0\) term vanishes
algebraically, before any estimate. \(\square\)

This is a cancellation for the interior function \(g_N\), not a claim
that the original finite-window pairing has no endpoint contribution.
The identity is \(c_f=c_p+c_g\), with (7) retained.

## 3. Finite contour packets for all aliases

Fix \(H>0\). Suppose the same \(f_N\) is holomorphic on a buffered
rectangle containing \([a,b]+i[-H,H]\). For \(\sigma=\pm1\), let
\[
 \begin{split}
 T_\sigma&=[a+i\sigma H,b+i\sigma H],\\
 V_\sigma&=[a,a+i\sigma H]-[b,b+i\sigma H],\\
 W_{\sigma,N}(y)&=-\sigma\,
       \frac{e^{2\pi i\sigma Ny}}{(1+e^{2\pi i\sigma Ny})^2},\\
 L_N(s)&=\int_{-1}^1e^{2\pi iN\xi s}\,d\xi
       =\frac{\sin(2\pi Ns)}{\pi Ns},\qquad L_N(0)=2.
 \end{split}                                           \tag{10}
\]
Segments have their displayed orientations. On each vertical endpoint
segment the real base is an integer multiple of \(1/N\); consequently
the denominator in \(W_{\sigma,N}\) has no zero there, including its
base. It has no zero on \(T_\sigma\) either.

For oriented chains \(Y,Z\), define the finite double integral
\[
 \mathcal J_\sigma(Y,Z)=\int_Y\int_Z
    g_N(y)A_N(z)W_{\sigma,N}(y)L_N(z-y)\,dz\,dy.        \tag{11}
\]
Assume \(A_N\) is holomorphic on the domains of the deformations below.
Choose a bounded-length contour \(\gamma_\sigma\) from
\(a+i\sigma h_{a,\sigma}\) to \(b+i\sigma h_{b,\sigma}\), with
\[
       0\le \sigma\Im z\le H\quad(z\in\gamma_\sigma),
       \qquad 0\le h_{a,\sigma},h_{b,\sigma}\le H.    \tag{12}
\]
Its homotopy from \(I\), including the endpoint segments, is within
the holomorphy domain of \(A_N\). Put
\[
 E_\sigma=[a,a+i\sigma h_{a,\sigma}]
                    -[b,b+i\sigma h_{b,\sigma}].       \tag{13}
\]
Thus integration over \(I\) equals integration over
\(\gamma_\sigma+E_\sigma\) for every holomorphic integrand in question.

**Proposition 2.** The exact decomposition is
\[
 \mathfrak P_N[f,A]=\mathfrak B_N+\mathfrak E_N,         \tag{14}
\]
where
\[
 \mathfrak B_N=-2\pi^2iN^3\sum_{\sigma=\pm1}
                       \mathcal J_\sigma(T_\sigma,\gamma_\sigma),
                                                               \tag{15}
\]
and the complete finite endpoint packet is
\[
 \boxed{\quad
 \mathfrak E_N=\mathfrak P_N[p,A]
   -2\pi^2iN^3\sum_{\sigma=\pm1}
     \{\mathcal J_\sigma(V_\sigma,I)
                  +\mathcal J_\sigma(T_\sigma,E_\sigma)\}.
 \quad}                                                        \tag{16}
\]
Every integral in (16) is literal; in particular no endpoint packet
is estimated by the bound for (15).

**Proof.** In (9), for \(\sigma=\operatorname{sgn}m\), Cauchy's theorem
gives
\[
 \widehat g_N(N(\xi-m))
   =\int_{T_\sigma+V_\sigma}
                g_N(y)e^{-2\pi iN(\xi-m)y}\,dy.        \tag{17}
\]
There is no source replacement in (17). In the open designated
half-plane the absolutely convergent geometric derivative is
\[
 \sum_{\operatorname{sgn}m=\sigma}
       m(-1)^m e^{2\pi iNmy}=W_{\sigma,N}(y).           \tag{18}
\]
The interchange of sum and the endpoint-segment integrals is also
valid. At either real base, \(g_N=O_N(|\Im y|^2)\). For \(|m|\ge2\),
the integral of this bound times
\(|m|e^{-2\pi N(|m|-1)|\Im y|}\) is summable in \(m\).
The two \(|m|=1\) terms are finite, even at \(\xi=\pm1\).
Thus (18) may be used in (17) down to the segment bases.

Substitute into (4), use (9), and integrate over \(\xi\). This gives
\(-2\pi^2iN^3\sum_\sigma\mathcal J_\sigma(T_\sigma+V_\sigma,I)\).
Deform only the \(T_\sigma\)-paired spectator integral from \(I\) to
\(\gamma_\sigma+E_\sigma\). The \(V_\sigma\)-paired integral is left
on its original real interval. Adding the cubic packet gives exactly
(14)--(16). This order retains the endpoint cross terms without
splitting or duplicating them. All apparent zeros of \(L_N\)'s
denominator are removable. \(\square\)

The endpoint packet is a finite number of explicitly oriented contour
integrals, rather than a conditionally interpreted infinite alias
remainder. If a proposed spectator homotopy crosses poles, its actual
residues must be added to (16); the holomorphic statement above does
not authorize their omission.

## 4. The unit-charge estimate

Assume, on the same fixed rectangle and derivative buffers,
\[
             |f_N|\le e^{-\kappa N+o(N)},\qquad\kappa>0.
                                                               \tag{19}
\]
The window-length bounds, (5), and Cauchy estimates imply the same
bound for \(p_N,g_N\), after subexponential factors. All hypotheses may
be uniform in shared parameters on fixed compacts.

**Theorem 3.** Under the preceding scalar and contour hypotheses,
\[
 |\mathfrak B_N|
 \le e^{-\kappa N+o(N)}
       \sum_{\sigma=\pm1}\int_{\gamma_\sigma}
                |A_N(z)|e^{-2\pi N|\Im z|}\,|dz|.      \tag{20}
\]
Polynomial factors in \(N\) are included in \(e^{o(N)}\). In particular,
if the actual spectator on these contours is
\(A_N=e^{N\Theta_N}a_N\), \(|a_N|\le e^{o(N)}\), and
\[
 \sup_{z\in\gamma_\sigma}
       \Re\{\Theta_N(z)+2\pi i\sigma z\}\le B+o(1),   \tag{21}
\]
then \(|\mathfrak B_N|\le e^{N(B-\kappa)+o(N)}\).
There is no comparison between \(\kappa\) and a complete-minus-parent
action deficit in this assertion. Equation (21) is an estimate for
the actual spectator and its admitted contour, not a consequence
of positivity alone.

**Proof.** On \(T_\sigma\),
\[
 |W_{\sigma,N}|\le
      \frac{e^{-2\pi NH}}{(1-e^{-2\pi NH})^2}.
\]
By its integral definition,
\(|L_N(z-y)|\le2e^{2\pi N|\Im(z-y)|}\). Conditions (10),(12) give
\(|\Im(z-y)|=H-|\Im z|\). Hence
\[
 |W_{\sigma,N}(y)L_N(z-y)|
 \le\frac{2}{(1-e^{-2\pi NH})^2}
                         e^{-2\pi N|\Im z|}.          \tag{22}
\]
Use (19), the fixed top lengths and (15) to prove (20). The fixed
contour lengths and (21) prove the last conclusion. \(\square\)

The charge can also be read before summing aliases. For
\(\sigma=\operatorname{sgn}m\), \(-1\le\xi\le1\), and (12),
\[
 2\pi\{(\xi-m)\sigma H-\xi\Im z\}
 \le -2\pi|\Im z|-2\pi(|m|-1)H.                       \tag{23}
\]
Thus the \(|m|=1\) aliases carry the unit charge, and higher aliases
have additional fixed-height decay. In the original angular variable
\(t=\pi-2\pi X\), its character is exactly
\[
 e^{2\pi i\sigma NX}=e^{i\sigma\pi N}e^{-i\sigma Nt}.
                                                               \tag{24}
\]
If the spectator contains its original carrier
\(C_{N,n}e^{inNt^2/(4\pi)}\), the resulting phase is
\(in t^2/(4\pi)-i\sigma t\), with the unit factor
\(C_{N,n}e^{i\sigma\pi N}\) retained. No quadratic carrier or alias
has been replaced by its modulus in the exact identities.

## 5. Original closing and the remaining assembly condition

For the ordinary positive window normalization of the pinned midpoint
identity, let \(\Lambda_N\) be the unchanged remaining closing,
including every shared color and normal. Then exactly
\[
 Z_{N,\mathrm{int}}
       =-\eta\pi^{-2}\Lambda_N(\mathfrak B_N+\mathfrak E_N).
                                                               \tag{25}
\]
A mirrored half normalization carries its corresponding original
factor of one half; neither (14) nor its pairing changes that
multiplicity. The exterior half-boundaries already present before
(4) are separate from the new explicit packet (16) and remain in
the full window identity. Bound (20) is before \(\Lambda_N\); a bound
after closing requires the actual joint integral estimate, not a
product of separately closed bounds.

For fixed products at one color, a common scalar representative and
the ordinary product rule give (2) for their product or scalar
difference, with the sum of their phase weights. This preserves all
mixed normals. It does not convert independent value/normal channels
into compatible scalar jets. Nor may one choose different holomorphic
completions for \(m>0\) and \(m<0\): a full-grid-null difference can
have a nonzero partial alias sum. The same \(f_N\) is required on both
top contours in (17).

The pinned short spectral repair now supplies one even, two-sided
scalar completion on each sufficiently short eligible cell. Its
own closed trace has no real repair interface. The present result
instead gives the exact charged decomposition whenever an interface
or a comparison is represented by compatible scalar jets, and shows
which actual endpoint data must accompany transport of its interior.
For neighboring cells, the four endpoint jets in (5), the oriented
chains in (16), and the original exterior sides have to be combined
using the actual chosen representatives. This note proves no automatic
cancellation or parent bound for that combination.

## Direct sources and author audit

The complete direct texts are:

* [Midpoint Fourier/normal pairing](research_leaf_interface_midpoint_fourier_pairing.md),
  SHA256 d24bf81b7ab841022ec72fb1e6af2d76e03aea057f749c0e60d350e200784083:
  exact interface, centered translation, original closing, shared
  product normals and retained exterior sides.
* [Short spectral window repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550:
  one actual two-sided scalar representative on a short cell and
  the retained adjacent-cell/exterior scope.

The Poisson identity, finite contour decomposition and charge estimate
are proved here. Only written mathematics and source-text/hash reads
are used. No mathematical program, numerical experiment, test or
compilation is run. Adopted and public files are unchanged.
