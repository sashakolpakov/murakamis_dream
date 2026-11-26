# Exact incoming transport with a moving finite cut

Research deduction, 7 November 2026. Moving the complete incoming
contour creates no boundary at the artificial half face. Moving a
truncated conditional sum does create boundary currents: every change
of its integer cut contributes one complete row on a vertical segment.
Here these currents are written exactly and bounded on a fixed thin
negative incoming strip. The original conditional ends and decaying
aliases retain their gaps on that strip as well.

The thickness is obtained by uniform continuity of specified finite-source
upper rates. It is not asserted to reach the actual incoming height.
No numerical evaluation is used.

## 1. Complete source and the deformation measure

Keep the ordinary-next canonical family, selected coordinate and
outgoing plateau of
[the selected right-segment theorem](research_mixed_second_selected_first_three_right_segment.md).
Write
\[
\begin{gathered}
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 y\in P+i/100,\quad P=[11/50,9/20],\quad Y=e^{-2\pi iy},\\
 z=u+i\Im z_*,\quad u\in P,\quad Z=e^{-2\pi iz},\quad
 \beta\in\{0,1\},\\
 W_{\beta,N}(Y,Z)=d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).
\end{gathered}                                                    \tag{1}
\]
There is no outgoing halfweight when \(\beta=0\). Otherwise the
factor \(|d_N(Z)|^{1/2}\) remains external to the holomorphic
integrals below.

For \(X=e^{-2\pi ia}\), define the complete row densities
\[
\begin{split}
 f_{j,N}(a)&=U_{0,N}(w,X)
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\,
                                W_{\beta,N}(Y,Z),\\
 f_N(a)&=\sum_{j=0}^{D}f_{j,N}(a),\qquad
 U_{0,N}(w,X)=\sum_{i=0}^{D}
                       H_N(w,r^{-i})p_i(X)/P_i .
\end{split}                                                     \tag{2}
\]
Each \(H_N\) is whole. No incoming physical termination is imposed
at a nonphysical \(a\). Each row and their sum are entire and
one-periodic in \(a\). In fact \(X^{-j}p_j(X)\) has band
\([-j,0]\), so the incoming band of \(U_0C_1\) is contained
in \([-D,D]\).

The [exact next attachment, equation (5)](research_mixed_three_four_next_conditional_attachment.md)
has density \(N^2\,da\,dy\). With the other variable held fixed,
its incoming density is \(Nf_N(a)\,da\). Increasing \(a\)
parametrizes the \(X\)-circle clockwise, but
\(da=-dX/(2\pi iX)\); thus \(\int_0^1 f_N(a)\,da\)
is the constant term with positive sign. No scalar is changed here.

For any real \(A<B\) and real \(h\), finite-source holomorphy
gives
\[
 \int_{A+ih}^{A}f_N\,da+\int_A^B f_N\,da
   =\int_{A+ih}^{B+ih}f_N\,da+\int_{B+ih}^{B}f_N\,da .       \tag{3}
\]
The two vertical integrals cancel by periodicity only when their
real coordinates differ by an integer and both sides are retained.
For a proper subarc the last vertical side is compulsory. The
complete-period and coupled-graph versions are already proved in
[conditional torus composition](research_mixed_conditional_torus_composition.md)
and [coupled outer graphs](research_mixed_coupled_outer_graph.md).
Equation (3) neither assumes nor continues a critical-point packet.

## 2. Exact currents from the integer cut

Use exactly the positive \(\varepsilon\), lower cut and upper cut
of [the conditional end-range theorem](research_mixed_next_selected_first_wall_rows.md):
\[
 L_N=\lfloor N/16\rfloor+1,\qquad
 K_N(x)=\lceil N(1-x-\varepsilon)\rceil,
 \qquad \frac12\le x\le\frac7{10}.                         \tag{4}
\]
For sufficiently large \(N\), \(L_N<K_N(x)<N\).
The convention in (4) is right-continuous: for an integer \(j\),
\[
 j<K_N(x)\quad\Longleftrightarrow\quad
 x<x_j:=1-\varepsilon-j/N .                                  \tag{5}
\]
At \(x=x_j\), row \(j\) has already left the central group.

Let the cut label \(x\) and the holomorphic argument \(a\) be
distinct in
\[
 f_N^{\rm mid}(x;a)=\sum_{j=L_N}^{K_N(x)-1}f_{j,N}(a).
                                                                  \tag{6}
\]
For \(1/2\le A<B\le7/10\), set
\[
\begin{split}
 I_N(h)&=N\int_A^B f_N^{\rm mid}(x;x+ih)\,dx,\\
 V_N(x;h)&=N\int_{x+ih}^{x}f_N^{\rm mid}(x;a)\,da,\\
 J_N(A,B;h)&=N\sum_{\substack{L_N\le j\le D\\ A<x_j\le B}}
                     \int_{x_j+ih}^{x_j}f_{j,N}(a)\,da .
\end{split}                                                     \tag{7}
\]
All vertical differentials are the actual complex differential.
In particular no factor of \(i\), sign, or residue density is
discarded when a modulus is later taken.

**Proposition 1.** The exact identity is
\[
 \boxed{\quad V_N(A;h)+I_N(0)
       =I_N(h)+V_N(B;h)+J_N(A,B;h).\quad}                     \tag{8}
\]
It holds for every finite level and every height for which these
definitions are used, independently of any source estimate.

For a direct proof, fix one row. Its retained real interval is
\([A,\min(B,x_j))\), unless that interval is empty. Apply the
rectangle identity (3) to that row. If it leaves the sum before
the right endpoint, its right vertical side is the corresponding
term in \(J_N\). If it survives, that side is part of \(V_N(B;h)\).
Summing proves (8). If \(x_j=B\), the canonical cut at \(B\)
omits the row, so its side belongs to \(J_N\); this explains
the closed right endpoint in (7). A row with \(x_j=A\) is
absent throughout and contributes nothing. Equivalently one may
use the left-limit cut at \(B\) and the open jump interval
\((A,B)\); the same term merely changes its label.

The complementary row group has the opposite jump current.
Adding its identity to (8) cancels \(J_N\) exactly and recovers
(3), multiplied by \(N\). Thus neither a signed whole-source
bound nor a contour identity for a fixed cut licenses omitting
the currents in (7).

This rowwise argument applies to any finite holomorphic row
decomposition and any finite sequence of integer-cut jumps.
A jump adding a row has the opposite sign. It is independent
of the powers in an original matrix word. The bounds proved
next, however, concern precisely the source (1)--(2).

## 3. A fixed strip where every jump row is paid

The whole-disk physical row rate of the conditional factor is
\[
\begin{split}
 F_{x,h}(t)&=L(t)+I_{x,h}(t)-3J(t)-2\pi ht,\\
 I_{x,h}(t)&=\int_0^t
             \log|1-e^{2\pi h-2\pi i(x+s)}|\,ds,\qquad
 L(t)=-2J((1-t)/2).
\end{split}                                                     \tag{9}
\]
The last term is the exact modulus of \(X^{-j}\). Uniform
zero-safe finite product bounds give this rate for every
\(j<N\), with a polynomial cost and an arbitrary prescribed
tolerance, on \(|Y|\le1\). The bound on \(p_j(Y)\) here uses
its actual integer degree; no complex-index polynomial argument
is made. The numerator upper estimates and their uniformity near
complex zeros are the complete-product estimates used in
[the continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md)
and [the joint whole-source extension](research_mixed_half_face_joint_source_packet.md).
Equivalently, truncate the logarithm from below in the upper
Riemann-sum comparison and then use its uniform integrability;
no lower bound on a possibly zero numerator is needed.

For completeness the integrated numerator rate in (9) is jointly
continuous through \(h=0\), uniformly in \(x,t\) on compact
sets. Away from a zero this is ordinary uniform convergence.
Near a zero use
\[
 |1-Re^{i\theta}|^2=(1-R)^2+4R\sin^2(\theta/2),\qquad
                              R=e^{2\pi h}.
                                                                  \tag{10}
\]
For \(R\) in a fixed neighborhood of one, the negative part
is bounded by an integrable constant plus \(|\log|\theta||\),
and the positive part is uniformly bounded. Splitting the circle
into a small zero neighborhood and its complement proves uniform
\(L^1\) convergence. Every partial integral therefore converges
uniformly. The chirp in (9) is continuous too.

The cap requires its own source argument. On compact physical
private-index intervals its complete coefficient has the all-real
rate \(J(e)+\lambda(e)\). Its positive row rate is consequently
\(\lambda(e)+I_{x,h}(e)\). At real incoming values
\(x\in[1/2,7/10]\), the proof of
[complementary real colors, Section 2](research_mixed_three_four_complementary_real_colors.md)
bounds these rows by
\[
                             B_0=1549/1500.                    \tag{11}
\]
Uniform continuity of the specified integrals extends this bound
to \(B_0+\xi\), for any \(\xi>0\), on a sufficiently thin
negative strip. The two true private ends remain separate: their
positive row sum has rate \(3/5\) throughout \(|X|\le1\).
Thus the same \(B_0+\xi\) ceiling holds for the whole cap,
uniformly for every real ordinary color. This argument uses neither
a global unit-circle supremum of the cap nor a maximum principle
to infer a radial contraction of its signed value.

The end-range theorem supplies a common real-row reserve
\[
 B_0+F_{x,0}(t)<77/50-193/12000                                \tag{12}
\]
on its lower and upper paid collars, after enlarging the weaker
of their two bounds. In particular it applies to every jump row:
\[
                t=j/N=1-x_j-\varepsilon
                         \ge1-x_j-2\varepsilon .              \tag{13}
\]
Equations (9)--(12) imply that there is a fixed \(\eta_0>0\)
such that throughout \(-\eta_0\le h\le0\), for any subset
\(S(x)\) of either paid physical collar,
\[
 \sup_{|Y|\le1}
 \sum_{j\in S(x)}
 \left|U_{0,N}(w,X)
             \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\tau N^{B_\tau}
       e^{N\{77/50-193/24000+\tau\}} .                       \tag{14}
\]
Here \(X=e^{-2\pi i(x+ih)}\). Choose the cap and conditional
continuity allowances to sum to less than \(193/24000\).
The common finite-product tolerance is then chosen afterwards.
The number of rows is at most \(N\); every complete endpoint
coefficient is retained before taking its modulus.

Each row polynomial in (14) has outgoing degree at most \(D\).
Consequently the degree-based selected comparison in
[the final-arc theorem, Section 3](research_mixed_next_selected_final_first_arc.md),
which traces the exact proof in
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md),
applies to it. Its only prefix input is the whole-disk ceiling
\(77/50\), with all actual weights and the original marginal.
After one total tolerance and the polynomial factors, this yields
\[
 \boxed{\quad
 |J_N(A,B;h)|\,|d_N(Z)|^{\beta/2}
       \le C N^B e^{N\{\Lambda_{123}(z)-1/2000\}}
       \qquad(-\eta_0\le h\le0).
 \quad}                                                       \tag{15}
\]
Indeed there are at most \(N\) vertical integrals, each of
bounded length, and the original extra density is \(N\).
Both alternatives of the selected weight \(d_N(Y)Y^{-N}\)
remain in this comparison. The same estimate bounds the full
positive sum of the moduli of these current integrals. It is
not a cancellation estimate for that sum.

The physical groups \(j<L_N\) and \(j\ge K_N(x)\) obey
the same calibrated bound throughout this thin strip, including
on both endpoint vertical segments. The statement includes
\(j=0,N-1\), all numerator zeros, and both level parities.

## 4. The exact real-index reduction also survives this strip

Keep the half-grid cuts
\[
 \ell_N=(L_N-1/2)/N,\qquad
 u_N(x)=(K_N(x)-1/2)/N .                                     \tag{16}
\]
For fixed cut label \(x\), the retained interpolant is
\[
 T_N(s;a,y)=e^{2\pi iNas}
       \Pi_N(a+s)\Pi_N(y+s)E_N(a)E_N(y)E_N(s)^3 .             \tag{17}
\]
Its original phase is
\(Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias\).
The exact rectangle identity of
[the conditional alias theorem, equation (14)](research_mixed_next_far_half_conditional_aliases.md)
continues to hold at \(a=x+ih\):
\[
 \sum_{j=L_N}^{K_N(x)-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}
   =N\int_{\ell_N}^{u_N(x)}T_N(t;x+ih,y)\,dt
                                  +\mathcal A_N(x;h,y).       \tag{18}
\]
All four vertical half-sides and both horizontal remainder sides
of its fixed index rectangle \(|\Im s|\le2\) remain in
\(\mathcal A_N\).

The real parts of all primitive arguments stay in the same
compact regular strips: in particular
\(x+\Re s<1-3\varepsilon/4\). The phase change caused by
\(a=x\mapsto x+ih\) is uniformly small on this compact
rectangle. The exact cotangent remainder penalties do not change.
The old proof bounds each vertical remainder by its paid real
cut, and each horizontal remainder by its separate strict rate.
Perturbing these specified weighted rates, and using the cap
bound (11) with its small allowance, therefore preserves their
strict gaps after reducing \(\eta_0\) once more. This is a
continuity argument for the original complete current upper
bounds, not continuation of a sampled sum or a homogeneous
factorial approximation.

Thus every omitted physical group and every error in (18),
after multiplication by the complete remaining factors in (1),
has a common finite gap, which may be weakened to \(1/4000\).
All incoming factors \(N\), all finite row counts and bounded
current lengths are retained in the polynomial prefactor.

Combining this fact with (8), the central real-index double
integral may be displaced through this thin strip with the
endpoint vertical integrals retained and an exponentially smaller
error. The new vertical currents caused by its moving integer
cut are precisely those in (7), already paid by (15). At an
integer alignment of a wall, the endpoint convention of Section 2
accounts for the row once. No parity-specific deletion is made.

## 5. Scope and the remaining depth

All statements are uniform over the stated ordinary-next family,
all real ordinary colors and both parities. Fixed ordinary-color
derivatives cost only polynomial factors, by applying the original
coefficient bounds or Markov before summing the positive row bounds.
Small fixed complex neighborhoods of complete color and fixed local
outside-parameter derivatives follow with a smaller reserve from
the sourcewise bounds and Cauchy's formula. The cut labels, row
sets, endpoints and vertical segments are fixed while taking those
derivatives. The outgoing modulus halfweight is kept external;
no finite weight is divided out.

The exact identities (3), (8) hold much more generally than these
estimates. Their finite algebra applies to every holomorphic
source and all ordinary derivatives. The calibrated thin-strip
estimate here uses the specific whole cap, conditional rows and
ordinary-next source plane in (1). It is not an estimate for an
arbitrary new boundary state or arbitrary short word.

In particular \(\eta_0\) has not been compared with
\(-\Im a_*\). Moving the full original connector to a distant
real endpoint is legal for the whole finite source by (3), but
its displaced horizontal path and far vertical side require their
own bounds. The central integral itself is not estimated here.
Neither the actual half-face affine comparison nor a whole later
Fourier sector is concluded.
