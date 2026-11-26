# The first real collar in the next ordinary attachment

Research deduction, 7 November 2026. The existing complete first-collar
estimate applies to the three-vertex half-chain \(34(3+\beta)\) with
an actual following Gram parameter. Its last vertex is ordinary,
even though the half-chain has only three vertices. Removing the
fixed nonzero outgoing halfweight gives a strict bound for a genuine
part of the two-variable next-transfer contour, in both Fourier
sectors. No right ordinary endpoint source is needed in this argument.
No numerical evaluation is used.

## 1. The reference and the literal two-variable source

Let \(\beta\in\{0,1\}\), and let the external following leg \(c\)
range over one of the compact clipped sets
\[
                       K\in\{O_3,O_4,A_3,A_4\}
                                                               \tag{1}
\]
of [actual last-row domains](research_mixed_actual_last_row_reference_domains.md).
Use the unique original half-chain critical point for the word
\(34(3+\beta)\), including its final incidence \(G(z,c)\).
Write its retained coordinates as
\[
 a_*=t_1,\qquad y_*=t_2,\qquad z_*=t_3 .
                                                               \tag{2}
\]
The original endpoint and ordinary image theorems give
\[
 a_*\in A_3,\qquad y_*\in O_4,\qquad
 s_2\in O_4,\qquad s_3,z_*\in O_{3+\beta}.              \tag{3}
\]
The first endpoint has external parameter \(s_2\). The external
inputs of vertices two and three are respectively
\((a_*,s_3)\in A_3\times O_{3+\beta}\) and
\((y_*,c)\in O_4\times K\). These are the actual correlated
outputs of the original maps, not independent choices of their
private coordinates.

The complete conditional phase of each vertex uses the literal
row primitive
\[
 Q_\epsilon(s;a,b)
   =g(s+a)+g(s+b)-(2+\epsilon)g(s)-g(a)-g(b)+2\pi ias.
                                                               \tag{4}
\]
Let \(\psi_\epsilon(a,b)\) denote its original critical value,
and let \(\mathcal T_0(a,w)\) be the complete first-cap action.
At the reference the next conditional action is, with its original
constant,
\[
 \mathcal P_\beta^+(-2,z_*)
   =\mathcal T_0(a_*,-2)+\psi_1(a_*,y_*)
                      -g(y_*)+\psi_\beta(y_*,z_*).
                                                               \tag{5}
\]
This is the action in
[the next local-source theorem](research_mixed_three_four_next_local_source.md),
not the action after adding the final Gram or an ordinary right cap.

Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\),
\(Z=e^{-2\pi iz}\). The two complete next-transfer sectors have
literal density
\[
 D_{\sigma,N}(w;a,y,z)
  =U_{0,N}(w,X)C_{1,N}(X,Y)
       d_N(Y)Y^{-N\sigma}C_{\beta,N}(Y,Z),
             \qquad \sigma=0,1,                       \tag{6}
\]
and external factor \(N^2\) before two constant-term extractions.
There is no \(d_N(X)\) because the first retained coordinate has
type three. The density (6) retains the entire finite sources.

## 2. Why the original collar theorem applies here

Choose the fixed small collar \(0<\rho\le1/1000\) admitted in
[first-collar tangent cancellation](research_mixed_first_collar_horizontal_tangent.md),
Section 4. It may be decreased once, independently of \(N\).
Set \(h_*=\Im y_*<0\), \(H=7/500\), and
\(I_4=[.24,.363]\). The target region is
\[
\begin{split}
 a&=x\in[0,\rho],\qquad y=v+ik,\qquad v\in I_4,\\
 \sigma=0:&\quad h_*\le k\le0,\\
 \sigma=1:&\quad 0\le k\le H .
\end{split}                                                    \tag{7}
\]
The output first stays fixed at \(z=z_*\).

The completed theorem used below is
[three-row source assembly, Section 3](research_mixed_three_row_source_assembly.md),
equation (11), with cut \(h=3\) and first types \((3,4)\).
Its statement uses an open word of length at least four to ensure
that the vertex at the cut is ordinary. Here the final incidence
\(G(z,c)\) gives exactly that ordinary role. Its proof has no
dependence on a right endpoint elsewhere:

* The first-pair theorem uses the cap packet and cap floor at
  \(a_*\), the original cubic conditional branch along \(I_4\),
  and the complete first-pair row ceiling. Its hypotheses are
  precisely \(a_*\in A_3\), \(y_*\in O_4\), and the actual
  first-cap endpoint image in (3).
* [Enlarged four-height transport](research_mixed_four_enlarged_contour_transport.md),
  Sections 1--4, applies on edge three. Its first external leg
  is \(y_*\in O_4\); its own output is \(z_*\in O_{3+\beta}\).
  It retains every row, both Fourier upper alternatives and the
  \(9/500\) allowance on the whole paths (7).
* The half- and last-row comparisons in three-row assembly,
  Sections 1--2, remove the third-edge excess. Their sufficient
  domain is the whole typed external product \(O_4\times K\)
  with its original map output. Thus they apply uniformly for
  every \(c\in K\), not only to parameters realized by a longer
  complete-ended word.

All of these source and phase inputs have already been proved on
the stated compact domains. The only cancellation used after them
is original stationarity at \(y_*\). In particular no terminal
graph is substituted for the ordinary third map.

For clarity, the collar theorem estimates
\[
 |D_{\sigma,N}(w;a,y,z)|\,|d_N(Z)|^{\beta/2}.
                                                               \tag{8}
\]
Its two incidences each contain exactly
\(|d_N(Y)Y^{-N\sigma}|^{1/2}\); together they give the full
old-four weight in (6). At the fixed output there is only the
single halfweight displayed in (8).
The allocated action of (8) is
\[
 M_3=\Re\mathcal P_\beta^+(-2,z_*)
                                  -\frac{\beta}{2}\Re g(z_*).
                                                               \tag{9}
\]
Indeed the two conditional phases in (5) receive respectively
the outgoing half of \(g(y)\), and the incoming half of \(g(y)\)
plus the outgoing half of \(\beta g(z)\).
The second-coordinate tangents cancel exactly:
\[
 \Re\{\psi_{1,y}-\tfrac12g'(y_*)\}
  +\Re\{\psi_{\beta,y}-\tfrac12g'(y_*)\}=0 .
                                                               \tag{10}
\]
The last displacement is zero because \(z=z_*\).
There is no use of a periodic trace identity in (9)--(10).

## 3. A strict bound for the next density

The cited complete collar theorem gives, with
\(\kappa_*=1/2500000\) and any prescribed total tolerance \(\tau>0\),
\[
 |D_{\sigma,N}(w;a,y,z_*)|\,|d_N(e^{-2\pi iz_*})|^{\beta/2}
 \le C_\tau N^A
   \exp N\left\{M_3-\frac4{125}
                -\kappa_*(v-\Re y_*)^2+\tau\right\}.
                                                               \tag{11}
\]
It holds on a sufficiently small fixed ordinary-color disk about
\(-2\). The exact finite products, physical end rows, revived
high rows, fixed contour currents and both parities are included.

When \(\beta=1\), \(z_*\in O_4\) lies in the rectangle \(E_4\)
of [Fourier-weight continuation, Corollary 2](research_mixed_fourier_weight_continuation.md).
That theorem gives a nonzero uniform packet
\[
 d_N(e^{-2\pi iz_*})
    =N^{-1/2}a_0(z_*)^{-1}e^{-Ng(z_*)}(1+O(N^{-1})).
                                                               \tag{12}
\]
Dividing (11) by this particular nonzero halfweight adds only a
polynomial factor and the rate \(+\tfrac12\Re g(z_*)\).
Equation (9) then cancels that rate exactly. For \(\beta=0\)
there is nothing to divide.

**Theorem 1.** Uniformly over the ordinary half-chain families
(1)--(3), for both sectors and all targets (7),
\[
 |D_{\sigma,N}(w;a,y,z_*)|
       \le C N^A
          e^{N\{\Re\mathcal P_\beta^+(-2,z_*)-1/50\}}.
                                                               \tag{13}
\]
Choose the total tolerance in (11) below \(1/125\);
the unspent \(4/125-1/125\) reserve exceeds \(1/50\).
The source power \(N^2\) and the integration over any fixed
bounded portion of (7), with bounded contour Jacobian, change only
the polynomial prefactor.

There is a local derivative version. Fix a base \(c_0\in K\)
and keep all paths and height labels in (7) at that base.
The original collar theorem also allows the output real coordinate
in the full interval \(P=[.22,.45]\), with its original tangent
and quadratic loss; \(z_*\) is uniformly interior to that interval.
Its squared finite source has integral Laurent degrees \(O(N)\),
and its stated polynomial complex-extension argument is uniform
in the compact height labels. Apply that argument with a smaller
rate tolerance, then use the nonzero continuation (12).
The resulting bound holds on a fixed neighborhood of the output
and ordinary color. The action in (5) continues there by the
original nondegenerate critical equations. Shrinking the
neighborhoods once, Cauchy's formula gives
\[
 \left|\partial_w^j\partial_z^\ell
   \left[e^{-N\mathcal P_\beta^+(w,z)}
          D_{\sigma,N}(w;a,y,z)\right]\right|
           \le C_{j,\ell}N^{A_{j,\ell}}e^{-N/100}
                                                               \tag{14}
\]
for every fixed pair of orders, uniformly on (7).
This differentiates fixed-base sources, not a reference-dependent
moving integration path.

## 4. What portion of the complement has been paid

The bound applies to the original first real collar
\(a\in[0,\rho]\), while the second incoming real coordinate stays
in \(I_4\) and its height follows the allowed path for its
actual Fourier label. It permits both labels in the complete
two-variable contour and preserves the entire final conditional
kernel. It is a contour-density estimate, unlike the separate
[physical end-sector deletion](research_mixed_three_four_next_physical_end_sector.md).
Those two statements are not identified with one another.

The present theorem does not cover \(v\notin I_4\), the later
incoming taper and far-circle regions, or a terminal third vertex
whose output is private. The ordinary right endpoint is absent
throughout the proof. No full next-cycle, prescribed closing or
additional knot-family theorem follows from (13).
