# The complete incoming corner on the lower-left shared interval

Private research proof candidate, 8 November 2026. For a next
type-four factor, the original incoming corner is bounded on
\(0\le\Re y\le11/50\), at the actual negative shared height.
The two original sides are used as one oriented integral.
Their exact replacement by the bottom and right sides of a
rectangle preserves the complete finite source.

The proof combines a bound for the original critical action with
the finite deformation of the conditional middle integral. The
critical action is calibrated against individual original phase
profiles, rather than extracted from the modulus of a sum.
No numerical evaluation or change to a frozen source is used.

## 1. Actual reference and exact source

Keep the ordinary-next reference and all its correlations from
[the first right-horizontal theorem](research_mixed_next_lower_left_incoming_right_horizontal.md),
with flags \((0,1,1)\):
\[
\begin{gathered}
(a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\\
h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
\quad h_t=\Im t_*,\quad h_z=\Im z_*,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.108\le h_t,h_z<0,\\
y=q+ih_y,\quad 0\le q\le11/50,\qquad
z=u+ih_z,\quad u\in P=[11/50,9/20].
\end{gathered}                                                    \tag{1}
\]
Both conditional vertices are ordinary. The outside input is the
same original typed leg; no private terminal coordinate replaces it.
The first incoming target is \(a=x-i\eta\), with
\[
1/2\le x\le7/10,\qquad 0\le\eta\le9/125.                       \tag{2}
\]
Write \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\).
With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(V)=(rV;r)_j\), retain the original finite kernel
\[
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
\]
The exact density is
\[
D_N(a)=U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z),
\qquad -2\le w\le2.                                         \tag{3}
\]
Here \(U_{0,N}\) is the complete cap and \(d_N\) is the original
forced Fourier polynomial. The outside allocation is
\(|d_N(Z)|^{1/2}\), and the incoming integration measure is
\(+N\,da\). There is no selected factor \(Y^{-N}\).

Let \(\Lambda_{123}(z)\), \(T_0\), and \(p_L\) retain their
definitions and original phase constants in the right-horizontal
theorem. Put \(A=\Re a_*\), \(\kappa_0=1/2500000\), and
\[
B_*=\Re T_0(a_*)-\Re p_L(1/2-A)-\kappa_0(1/2-A)^2.
                                                               \tag{4}
\]
Thus \(B_*=B_U(1/2)\), with the original cap supporting plane.
The attached equation is \(T_0'(a_*)+p_L=0\).

Use the oriented paths
\[
\begin{split}
a_L&=1/2+ih_a,\\
\Gamma_{\rm old}
 &=[a_L,1/2]\ \cup\ [1/2,7/10],\\
\Gamma_{\rm new}
 &=[a_L,7/10+ih_a]\ \cup\ [7/10+ih_a,7/10].
\end{split}                                                     \tag{5}
\]

**Theorem.** Uniformly on the actual reference family (1), both
parities and all real ordinary colors satisfy
\[
|D_N(a)|\,|d_N(Z)|^{1/2}
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-10}\}},
\qquad a\in\Gamma_{\rm new}.                                  \tag{6}
\]
Consequently
\[
\left|N\int_{\Gamma_{\rm old}}D_N(a)\,da\right|
                  |d_N(Z)|^{1/2}
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-10}\}}.                    \tag{7}
\]
The theorem concerns the combined integral on the old sides.
It does not assert separate absolute bounds on those two sides.

## 2. A phase-by-phase calibration at \(a_L\)

Keep the original phase
\[
Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias.              \tag{8}
\]
Let \(\mathscr P(y,z)\) consist of the following real rates for
the next type-four factor:
\[
\begin{split}
&\Re Q(t;y,z),\qquad
       t=t_R+ih_t,\quad 1/8\le t_R\le1/2,\\
&E_1(1/8;y,z),\qquad E_1(1/2;y,z),\qquad \delta_y=-2\pi h_y.
\end{split}                                                     \tag{9}
\]
Here \(E_1(v;y,z)=\Re Q(v;y,z)\) for a real index \(v\),
using the original continuous physical rate. The last entry is
the complete-period rate; it bounds the actual last physical
index through the endpoint-uniform factorial estimate.

Sections 3–4 of the right-horizontal theorem prove, for every
\(s_R\in[1/20,1/2]\) and \(\varphi\in\mathscr P(y,z)\),
\[
B_*+\Re Q(s_R+ih_s;a_L,y)+\varphi
       -\Re g(y)-\tfrac12\Re g(z)
<\Lambda_{123}(z)-10^{-9}.                                  \tag{10}
\]
We specify this input because the finite bound for \(C_{1,N}\)
alone would not imply (10).

At the old face \(q=11/50\), equation (13) of that theorem
retains the cap quadratic loss
\[
\kappa_0(x-A)^2\ge
       \frac{3481}{2500000000000}>10^{-9}.
\]
Every next profile in (9) satisfies its original supporting
inequality there. The first main is clipped into
\([1/6,5/12]+ih_s\) without decreasing its value. The joint
derivative in \(q\), equation (19) of that theorem, then
transports the first main paired with the next main or either
real cut to the old face. For a next last profile, its
equations (21)–(22) use positive transport when \(|Y|\le7/10\)
and comparison with the next low profile when \(|Y|\ge7/10\).
Those are pointwise profile comparisons. They prove (10)
with the original shared allocation \(-\Re g(y)\).

## 3. The actual critical action satisfies the same bound

Let \(s_c(a,y)\) be the selected root of \(Q_s=0\), and set
\(\Theta(a,y)=Q(s_c(a,y);a,y)\). The
[root annulus](research_mixed_conditional_corner_root_annulus.md)
and [real-coordinate guard](research_mixed_conditional_corner_root_angle.md)
prove, throughout (1)–(2),
\[
2/25<\Re s_c<1-\Re a,\qquad
|\Im s_c|<\frac{\log2}{2\pi}.                                \tag{11}
\]
The root is simple and retains the original zero logarithmic
lift, including \(q=0\).

At \(a=a_L\), define
\[
m(\sigma)=
 \max_{2/25\le v\le1/2}\widehat R(v,\sigma;a_L,y),
\qquad |\sigma|\le\frac{\log2}{2\pi},                        \tag{12}
\]
where \(\widehat R\) is the original continuous numerator rate
of the corner reduction. Before the incoming integer it is
\(\Re Q\); at that integer it is its zero-safe boundary value.
The [prewall curvature theorem](research_mixed_next_lower_left_corner_prewall_curvature.md),
Section 5, applies because (11) now proves its root hypotheses.
It makes \(m\) convex, with its minimum at the critical height.
The old height \(h_s\) lies in this interval. Therefore
\[
\Re\Theta(a_L,y)\le m(h_s).
\]
Taking the maximum in (10) over the smaller interval in (12)
gives, for every profile in (9),
\[
B_*+\Re\Theta(a_L,y)+\varphi
        -\Re g(y)-\tfrac12\Re g(z)
<\Lambda_{123}(z)-10^{-9}.                                  \tag{13}
\]
The next profile is held fixed while the first maximum is taken.
This step makes no inference from cancellation in a finite sum.

## 4. Action and cap bounds on the replacement path

The cap-only transport in
[the selected incoming-corner proof, equation (18)](research_mixed_next_selected_incoming_corner_union.md)
gives, for every \(\tau>0\),
\[
|U_{0,N}(w,e^{-2\pi i(x+ih_a)})|
 \le C_\tau N^{B_\tau}e^{N(B_*+\tau)},
\qquad 1/2\le x\le7/10.                                    \tag{14}
\]
This cap statement is independent of \(y\), so its scope is
unchanged on the present lower shared interval. It includes
the full cap source, all real colors and both parities.
On the right vertical side,
[the seven-tenths cap theorem](research_mixed_cap_seven_tenths_vertical_bound.md)
gives the smaller rate \(3907/4500\). The
[original cap-plane floor](research_mixed_next_calibrated_cap_plane_floor.md)
proves \(3907/4500<7/8<B_*\). Thus (14), with upper rate
\(B_*+\tau\), holds on both new sides.

For \(q>0\), the
[algebraic action theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
proves
\[
\Re\Theta_a<0,\qquad \Im\Theta_a>0.                          \tag{15}
\]
Its hypotheses hold on the whole rectangle (2). At \(q=0\),
the same action and its derivatives extend continuously by the
root annulus theorem. The limiting weak inequalities in (15)
are sufficient. Moving rightward and then upward consequently
gives
\[
\Re\Theta(a,y)\le\Re\Theta(a_L,y),
\qquad a\in\Gamma_{\rm new}.                                \tag{16}
\]
No additional strict contraction is needed: (13) already has
a uniform strict reserve.

The complete next sum is bounded by its profiles (9):
\[
|C_{1,N}(Y,Z)|
\le C_\tau N^{B_\tau}
 \exp N\left\{\max_{\varphi\in\mathscr P(y,z)}\varphi+\tau\right\}.
                                                               \tag{17}
\]
This follows by combining the
[complete current theorem](research_mixed_next_lower_left_complete_currents.md),
the [low physical bounds](research_mixed_next_lower_left_low_physical_blocks.md),
and the [own-four upper physical bounds](research_mixed_next_lower_left_own_four_upper_rows.md).
The middle constant mode, both horizontal aliases, all four
weighted sides and both unweighted joins are included. The
upper physical indices use their half and last alternatives.
At \(q=0\), the canonical reciprocal factorial uses its original
seam continuation.

The distinct forced Fourier bounds, including their full forcing,
are
\[
|d_N(Y)|\le C_\tau N^{B_\tau}e^{N(-\Re g(y)+\tau)},\qquad
|d_N(Z)|^{1/2}
 \le C_\tau N^{B_\tau}e^{N(-\Re g(z)/2+\tau)}.                \tag{18}
\]
They follow from Section 3 of the low physical bounds. No
relative factorial approximation for \(d_N\) at the seam is used.

Define \(W_N(a)=U_{0,N}(w,X)d_N(Y)C_{1,N}(Y,Z)\).
Equations (13)–(18) imply
\[
|W_N(a)|\,|d_N(Z)|^{1/2}e^{N\Re\Theta(a,y)}
\le CN^B e^{N\{\Lambda_{123}(z)-\tfrac12\,10^{-9}\}},
\qquad a\in\Gamma_{\rm new},                               \tag{19}
\]
after choosing the finitely many tolerances inside the reserve
in (13).

## 5. Complete finite source and exact Cauchy identity

The [lower-left Gaussian deformation](research_mixed_next_lower_left_corner_gaussian_deformation.md)
gives an actual local contribution \(G_N(a,y)\), with
\[
G_N(a,y)=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                       (1+O_{\rm hol}(N^{-1})),\qquad
\mathcal B(a,y)\ne0.                                       \tag{20}
\]
It also bounds the rest of the original conditional sum by two
terms:
\[
\begin{split}
&|W_N(a)\{C_{1,N}(X,Y)-G_N(a,y)\}|\,|d_N(Z)|^{1/2}\\
&\quad\le CN^B |W_N(a)|\,|d_N(Z)|^{1/2}
                      e^{N(\Re\Theta(a,y)-\gamma)}
       +CN^B e^{N\{\Lambda_{123}(z)-1/1000\}},
\end{split}                                                  \tag{21}
\]
where \(\gamma>0\) is uniform. The first error comes from the
deformed main tails and the critical-height endpoints of its
unweighted joins. The second comes from the real endpoints,
physical ends and all weighted currents. Neither error is
silently divided by a possibly vanishing outside factor.

Use (19) for the local term (20) and the first error in (21).
The second error already has a larger deficit. This proves
(6) for the complete original density.

For each fixed \(N,w,y,z\), (3) is an entire function of \(a\):
its \(a\)-dependent factors are finite Laurent polynomials in
\(e^{-2\pi ia}\), which never vanishes at a finite \(a\).
Therefore Cauchy's theorem gives the exact identity
\[
N\int_{\Gamma_{\rm old}}D_N(a)\,da
   =N\int_{\Gamma_{\rm new}}D_N(a)\,da.                      \tag{22}
\]
The outside absolute halfweight is multiplied only after this
holomorphic identity. Both new path lengths are uniformly bounded,
and the original factor \(N\) costs only a polynomial. Equation
(6) thus proves (7), retaining both original orientations and
all finite coefficients.

## 6. Scope for further assembly

This removes the incoming corner only for a next type-four
factor on the shared lower-left interval. It can be combined with
the initial, tapered, central, right-horizontal and far-real
incoming estimates, because all following factors are independent
of \(a\) and the corner is used in its combined orientation.
That assembly must still retain the original Fourier filter and
the denominator of the shared-variable integral.

The theorem does not estimate the analogous next type-three
corner, the other shared-variable contours, or an arbitrary
short-tangle attachment. No new whole-knot volume identity follows
from (7) alone. The local nonzero coefficient in (20) is used
here for an upper bound; it is not a noncancellation theorem for
the complete transfer.
