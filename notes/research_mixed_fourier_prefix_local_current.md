# The literal Fourier-output source and local current for every four-ending prefix

Research consequence, 7 November 2026. The completed Fourier-boundary
existence theorem identifies an original critical point for every
nonempty positive three/four prefix ending in four. Its actual finite
source therefore has a nonzero local current, with power \(N^{-1}\)
independent of the word length or number of four-vertices. This is a
local-current theorem for each fixed word, not an asymptotic for the
whole finite source.

The all-word matrix identity already appears in
[exact wire contraction](research_mixed_wire_exact_contraction.md).
The [cap phase entrance theorem](research_mixed_alternating_cap_phase_entrance.md),
Section 5, gives local coefficients after sufficiently long alternating
tails. The consequence here removes that length restriction for
four-ending words and supplies their explicit original symbol and
normalization, using the newly proved critical existence.

## 1. The exact source and its scalar

Let \(\epsilon_j\in\{0,1\}\), \(1\le j\le m\), with
\(m\ge1\), and put \(k=\sum_j\epsilon_j\). Keep
\[
 r=e^{-2\pi i/N},\quad Q=r^{-1},\quad
 P_a=(r;r)_a,\quad
 \kappa=e^{\pi i(N-1)^2/(2N)},\quad Y=e^{2\pi iy},\quad
 c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N).
\tag{1}
\]
The function in question is exactly
\[
 G_{\boldsymbol\epsilon,N}(y,w)
   =v_N(w)^T A_{3+\epsilon_1,N}\cdots
                     A_{3+\epsilon_m,N}h_N(y).
\tag{2}
\]
Here \(v_N(w)\) is the original ordinary boundary vector, with
complete value \(w=-2\), and \(h_N(y)\) is the original half-band
cardinal vector. No observation functional is substituted.

For indices \(i_j,j_j\ge0\), let \(\Omega_N\) be the original
support
\[
 i_j+j_j<N\quad(1\le j\le m),\qquad
 j_j+i_{j+1}<N\quad(1\le j<m).
\tag{3}
\]
In particular all individual indices are less than \(N\). The exact
coefficient \(b_i(w)=(Sv_N(w))_i\) equals
\(\mathcal H_N(w,r^{-i})/P_i\), where \(\mathcal H_N\) is the
complete original Newton polynomial. Then
\[
\begin{split}
 G_{\boldsymbol\epsilon,N}(y,w)
 ={}&\kappa^{m+k}N^k c_y
 \sum_{\Omega_N}
 b_{i_1}(w)\frac{Y^{j_m}}{(Y;r)_{j_m+1}}\\
 &{}\times\prod_{j=1}^m
       \frac{P_{i_j+j_j}}{(P_{i_j}P_{j_j})^{\epsilon_j}}
 \prod_{j<m}
       \frac{Q^{j_j i_{j+1}}P_{j_j+i_{j+1}}}
                         {P_{j_j}^{\,2}P_{i_{j+1}}^{\,2}}.
\end{split}
\tag{4}
\]
Empty products have value one. Quotients in the output variable retain
their original removable continuation.

Indeed \(A_n=S^TB_nS\), \(f=Sh\), \(b=Sv\), and
\(\Gamma=SS^T\) give
\(G=b^TB_{3+\epsilon_1}\Gamma\cdots\Gamma B_{3+\epsilon_m}f\).
Equations (5) and (10) of exact wire contraction say that \(B_3\)
carries \(\kappa\), \(B_4\) carries \(\kappa^2N\), and
\(\Gamma\) carries no outside power of \(N\). Substitution proves
(4), including all its triangular zeros and chirps. It is valid at
both level parities and retains every derivative of the original
boundary polynomial. In particular the outside power is \(N^k\),
not \(N^{m-1}\).

## 2. Its literal interpolation, phase and symbol

Write \(s_j=i_j/N\), \(t_j=j_j/N\), and \(z=(s_1,t_1,\ldots,s_m,t_m)\).
Use the original primitives
\[
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\quad J(0)=0,\qquad
 \ell_t(y)=2\pi ity-I_Y(t)-\pi iy,\quad
 I_Y(t)=\frac{\operatorname{Li}_2(Ye^{-2\pi it})-\operatorname{Li}_2(Y)}{2\pi i}.
\tag{5}
\]
The endpoint factor has the exact interpolation
\[
 b_N(s,w)=D_N(s)^{-1}C_N(s,w),\qquad
 D_N(s)=\exp\!\left\{\frac{\pi i}{2}[N(s-s^2)-s]\right\}.
\tag{6}
\]
This is the off-grid identity of Section 6 of
[complex-index continuation](research_complete_boundary_complex_index.md),
as retained in Section 3 of
[the prepared-cap source](research_mixed_prepared_three_four_cap_source.md).
It is not inferred only from matching finitely many lattice values.
The whole coefficient \(C_N\), including revived off-grid Newton rows,
has its original packet
\(N^{-3/2}\mathcal A(s,w)e^{NS(s,w)}(1+O(N^{-1}))\), with
\(\mathcal A\ne0\), on the
[endpoint rectangle](research_mixed_endpoint_cap_rectangle.md).

Set
\[
\begin{split}
 F_{\boldsymbol\epsilon}(z;y,w)={}&S(s_1,w)
       -\frac{\pi i}{2}(s_1-s_1^2)
       +\sum_{j=1}^m\{g(s_j+t_j)-\epsilon_j[g(s_j)+g(t_j)]\}\\
 &+\sum_{j<m}\{g(t_j+s_{j+1})-2g(t_j)-2g(s_{j+1})
                                      +2\pi it_js_{j+1}\}
       +\ell_{t_m}(y).
\end{split}
\tag{7}
\]
Every action constant in (7) is fixed by (4)--(6).
Let \(\mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}\), with
the square root continued from its positive value for real \(0<z<1\).
The original leading row symbol is
\[
\begin{split}
 b_{\boldsymbol\epsilon}(z;y,w)
 ={}&\frac{e^{i\pi s_1/2+\pi iy}\mathcal A(s_1,w)}
               {\sqrt{(1-Y)(1-Ye^{-2\pi it_m})}}\\
 &{}\times\prod_{j=1}^m
 \frac{\mathfrak a(s_j+t_j)}
             {[\mathfrak a(s_j)\mathfrak a(t_j)]^{\epsilon_j}}
 \prod_{j<m}
 \frac{\mathfrak a(t_j+s_{j+1})}
             {\mathfrak a(t_j)^2\mathfrak a(s_{j+1})^2}.
\end{split}
\tag{8}
\]
The last square root is the exponential of half the sum of the two
logarithms prescribed by
[root-Pochhammer interpolation](research_root_pochhammer_interpolation.md),
equation (9). The sine-factorial factors use
[the exact complex interpolation](exact_factorial_interpolation_and_complex_contours.md).
On any compact domain where these original formulas apply, the
interpolated summand in (4), including its outside scalar, is
\[
 R_{\boldsymbol\epsilon,N}(z;y,w)
  =\kappa^{m+k}N^{-m-1}b_{\boldsymbol\epsilon}(z;y,w)
           e^{NF_{\boldsymbol\epsilon}(z;y,w)}(1+O(N^{-1})).
\tag{9}
\]
The count is explicit: the vertex factorial ratios contribute
\(N^{m/2-k}\), the \(m-1\) wire ratios contribute
\(N^{-3(m-1)/2}\), the endpoint packet contributes \(N^{-3/2}\),
and \(N^kc_y\) contributes \(N^{k-1}\). Their product is
\(N^{-m-1}\). The factor \(1-Y^N\) tends to one exponentially
on compact subsets of \(|Y|<1\); the remaining factor
\(e^{\pi iy}\) is retained in (8). All fixed derivatives of the
normalized error obey the same estimate on smaller domains.

## 3. The proved critical point is in these symbol domains

Now assume \(\epsilon_m=1\). The
[completed boundary critical-existence theorem](research_mixed_fourier_boundary_critical_existence.md)
gives the unique original critical point at \((y,w)=(x_0,-2)\)
for the phase before eliminating the endpoint auxiliary \(u\).
It is in \(U_0\times E_0\times Q_0^{2m-1}\), where
\[
 U_0=[.21,.25]+i[.01,.10],\quad
 E_0=[.33,.47]+i[-.09,.08],\quad
 Q_0=[.23,.45]+i[-.12,.12].
\tag{10}
\]
The first endpoint update is one of the original full typed-input maps.
The [endpoint-image theorem](research_mixed_open_word_endpoint_rectangles.md)
therefore places its private \(s_1\) strictly in
\(E_c=[.27,.49]+i[-.055,.04]\), where (6) has its complete packet.
For \(m=1\), the map used here is the type-four endpoint map with
the auxiliary inverse leg in \(D_3\), not the old two-ordinary-end
one-vertex witness. Its attached coordinate satisfies
\(-.108<\Im t_1<-.020\).

For \(m\ge2\), the last vertex is an original ordinary type-four
map with both external inputs in their typed disks, one being the
auxiliary Fourier inverse leg in \(D_3\). The full-bidisk bounds
proved before cyclic specialization in Section 1 of
[the critical-height theorem](research_mixed_cyclic_critical_height_bounds.md)
give
\[
              -.102<\Im t_m<-.001.
\tag{11}
\]
No longer-window or cyclic-only bound is used. Thus, in either case,
\(|Y|<1\) and \(|Ye^{-2\pi it_m}|<1\) strictly at the actual
root. These are exactly the two root-Pochhammer domain conditions.
All individual factorial arguments have real parts strictly between
zero and one. Vertex and wire sums do also: even the containing
rectangles (10) give real sums in \([.56,.92]\) for the first
vertex and in \([.46,.90]\) for the other incidences.

Consequently a small neighborhood of the actual root and a small
complex neighborhood of \((x_0,-2)\) preserve all original symbols,
their branches and their nonvanishing. No contour across an excluded
factorial boundary or a different dilogarithm lift is introduced.

The reduced critical point \(z_*(y,w)\) of (7) is holomorphic and
nondegenerate. To check its Hessian, write \(M=-\mathcal H''\)
for the unreduced Hessian, with its first block the scalar \(u\).
At the original critical point the existence theorem gives
\(\operatorname{Re}M\succ(6\pi/49)I\). Its complex Schur complement
\[
 \mathcal S=M_{zz}-M_{zu}M_{uu}^{-1}M_{uz}=-F''_{\boldsymbol\epsilon}
\tag{12}
\]
has the same accretivity floor: for any complex \(x\), set
\(v=(-M_{uu}^{-1}M_{uz}x,x)\). Then
\(Mv=(0,\mathcal Sx)\), so \(v^*Mv=x^*\mathcal Sx\), and
\(\operatorname{Re}(x^*\mathcal Sx)>(6\pi/49)\|x\|^2\).
This is a complex Schur argument, not an entrywise Schur complement
of the real parts. A smaller positive floor persists locally in
the original parameters.

## 4. The original local Fourier current

Fix the word. Choose a sufficiently small real \(2m\)-box about
the actual critical real coordinates, at their critical heights.
For nearby complex parameters translate this box by the holomorphic
critical displacement. This defines a holomorphic oriented local
cycle \(\mathscr C_*(y,w)\), wholly inside the symbol domain above.
The zero-frequency local current of the literal row interpolation is
\[
 \mathcal M_{\boldsymbol\epsilon,N}(y,w)
       =N^{2m}\int_{\mathscr C_*(y,w)}
                    R_{\boldsymbol\epsilon,N}(z;y,w)\,dz.
\tag{13}
\]
The factor \(N^{2m}\) is the lattice density, with no additional
wire normalization. Shrinking the box if necessary, (12) gives
a strict quadratic decay from the critical point along the real
directions, uniformly in the parameter neighborhood. Holomorphic
Gaussian integration in (9) therefore yields
\[
\begin{split}
 \mathcal M_{\boldsymbol\epsilon,N}(y,w)
  & =\kappa^{m+k}N^{-1}\mathcal B_{\boldsymbol\epsilon}(y,w)
       e^{N\Phi_{\boldsymbol\epsilon}(y,w)}(1+O(N^{-1})),\\
 \Phi_{\boldsymbol\epsilon}(y,w)&=F_{\boldsymbol\epsilon}(z_*(y,w);y,w),\\
 \mathcal B_{\boldsymbol\epsilon}(y,w)&=
 \frac{(2\pi)^m b_{\boldsymbol\epsilon}(z_*(y,w);y,w)}
          {\sqrt{\det[-F''_{\boldsymbol\epsilon}(z_*(y,w);y,w)]}}\ne0.
\end{split}
\tag{14}
\]
The Gaussian square root is determined by the original increasing
real-coordinate orientation and the accretive branch. Its power is
\(N^{2m}N^{-m-1}N^{-m}=N^{-1}\). The assertion holds at both
integer level parities, with all fixed ordinary-color and outgoing
Fourier derivatives of the normalized relative error on smaller
neighborhoods. Constants may depend on the fixed word; no uniform
relative error in the word length is asserted.

Equation (14) specializes to the already proved prepared \(34\)
local current, but it also applies to the one-letter prefix \(4\)
and every other four-ending positive word. It uses the complete
ordinary endpoint coefficient before the local outer integration.
It does not assert that (13) dominates (4), or that it can be
isolated from the full source without paying the other physical
regions, aliases, joins and support boundaries. Those comparisons,
an outgoing full-period envelope, and control of subsequent whole
message attachments remain separate. In particular neither a new
knot-family theorem nor finite-exception stability follows from
this local-current consequence.
