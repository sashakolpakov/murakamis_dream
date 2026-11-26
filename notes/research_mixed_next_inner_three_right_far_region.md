# The right far region of the unchanged shortened inner source

Private finite-source theorem, 8 November 2026. The full
short-by-short angular integrand is exponentially smaller than
the actual inner action on a fixed low rectangle near the right
angular end. This pays the horizontal from \(5\pi/6-i/10\)
to the original right half-grid boundary and the complete
joining vertical there.

No further Newton cutoff is made. No mathematical numerical
evaluation or frozen-source edit is used.

## 1. Original source and exact paths

Keep the source of
[the short-pair transfer theorem](research_mixed_next_inner_three_short_pair_source_transfer.md):
\[
 \begin{gathered}
 N\ge3,\quad D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 q=e^{\pi i/N},\quad\eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N^{<<}(t,u)=K_N^<(t,0)K_N^<(t,u),\\
 g_N^{<<}(t,u)=\sin t\,f_N^{<<}(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
 \end{gathered}                                                     \tag{1}
\]
For the actual family write
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
 \quad t_*(u)=a_*(u)-iH(u),\quad s(u)=\Re S_3(0,u).
                                                                    \tag{2}
\]
All actions use their original complete constants and
logarithmic charges.

The original far cutoff and half-grid endpoint are
\[
 a_F=\pi-\frac{\pi}{2000},\qquad
 m_N=\lfloor N/4000\rfloor,\qquad
 T_N=\pi-\frac{2\pi m_N}{N},\qquad
                         e^{iNT_N}=-\eta_N.
                                                                    \tag{3}
\]
Fix the previously chosen \(0<h_c\le1/2000\) of
[the complete inner endpoint proof](research_mixed_next_inner_three_far_samples_and_verticals.md),
and put
\[
                     a_0=\frac{5\pi}{6},\qquad h_f=\frac1{10}.
                                                                    \tag{4}
\]
Define the oriented right far path
\[
 \Gamma_{R,N}^{\rm far}:
 a_0-ih_f\ \longrightarrow\ T_N-ih_f\
                 \longrightarrow\ T_N-ih_c .
                                                                    \tag{5}
\]
The first segment points right and the second upward.

**Theorem.** Uniformly for \(u\in\mathcal U_+\), both level
parities, and all sufficiently large \(N\),
\[
 \boxed{\quad
 \sup_{\substack{a_0\le a\le T_N\\h_c\le h\le h_f}}
 |g_N^{<<}(a-ih,u)W_N(a-ih)|
                    \le C e^{N(s(u)-1/50)} .
 \quad}                                                           \tag{6}
\]
The same bound holds on the full half-grid column
\(T_N-ih,\ 0\le h\le h_f\). In particular
\[
 \frac{N^2}{\pi}\int_{\Gamma_{R,N}^{\rm far}}
             |g_N^{<<}(t,u)W_N(t)|\,|dt|
                    \le C e^{N(s(u)-1/50)} .
                                                                    \tag{7}
\]
Every original Fourier charge in the double-pole kernel
is retained. No derivative assertion is made.

## 2. A calibrated complete-end bound on the far real interval

The original first-edge phase satisfies
\[
 \psi(t,0)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)),
 \qquad J'(z)=\Log(2\sin\pi z),\quad J(0)=0 .
                                                                    \tag{8}
\]
For real \(0<a<\pi\),
\[
 \psi_a(a,0)=-\frac1\pi\operatorname{arsinh}(\tan(a/2))<0.
                                                                    \tag{9}
\]
These are the original formulas in
[the complete-edge source](research_internal_pair_complete_edge_gap.md)
and their unchanged continuation in
[the positive phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
Thus \(\psi(a,0)\le\psi(a_0,0)\) for \(a\ge a_0\).

Since \(J(1/2)=0\), the two arguments in (8) at \(a_0\)
give the exact identity
\[
 \psi(a_0,0)
   =-4\{J(11/24)+J(1/24)\}
   =-4\int_0^{1/24}\log\tan(\pi s)\,ds .
                                                                    \tag{10}
\]
Using \(\tan(\pi s)>\pi s\) in this integral,
\[
 \psi(a_0,0)
   <\frac16\left(1+\log\frac{24}{\pi}\right)
   <\frac{13}{24}.
                                                                    \tag{11}
\]
The last inequality uses only \(\pi>3\) and
\(\log8<9/4\). A written witness for the latter is
\[
 e^2>
     1+2+\frac{2^2}{2!}+\frac{2^3}{3!}+\frac{2^4}{4!}
       =7,\qquad
 e^{1/4}>1+\frac14=\frac54,
 \quad e^{9/4}>\frac{35}{4}>8 .
                                                                    \tag{12}
\]

For \(t=a-ih,\ 0<a<\pi,\ h\ge0\), the same original
principal return has imaginary part in \((-\pi/2,0]\).
Indeed
\[
 \tan((a-ih)/2)
       =\frac{\sin a-i\sinh h}{\cosh h+\cos a}
                                                                    \tag{13}
\]
has positive real part and nonpositive imaginary part,
so it avoids the return cuts. Consequently
\[
 \partial_h\Re\psi(a-ih,0)
       =-\frac1\pi\Im\operatorname{arsinh}
                      (\tan((a-ih)/2))<\frac12 .
                                                                    \tag{14}
\]
Integration, including \(h=0\), proves
\[
      2\Re\psi(a-ih,0)\le 2\psi(a,0)+h
                           <\frac{13}{12}+h
                   \qquad(a_0\le a<\pi).
                                                                    \tag{15}
\]
No additive constant or charge has been reset in this
height comparison.

## 3. Full finite source from the slit-plane estimates

Choose a fixed \(a_F'\) with \(a_F<a_F'<\pi\), for
example \(a_F'=\pi-\pi/4000\). For all sufficiently
large \(N\), the exact endpoint in (3) obeys
\(T_N\le a_F'\). Thus
\[
 \mathcal C=
 \{-2\cos(a-ih):a_0\le a\le a_F',\ 0\le h\le h_f\}
       \subset\mathbb C\setminus[2,\infty)
                                                                    \tag{16}
\]
is one fixed compact eligible set. The strict inclusion
also holds at height zero since \(a_F'<\pi\).

Apply the adopted
[slit-plane source theorem, equations (18) and (24)](research_mixed_next_first_short_edge_slit_plane_bound.md)
on (16), with
\[
                              \tau=\frac1{10000}
                                                                    \tag{17}
\]
for each factor. In angular notation its exact finite
conclusions are
\[
 \begin{split}
 |K_N^<(a-ih,0)|
      &\le C e^{N\{\Re\psi(a-ih,0)+\tau\}},\\
 |K_N^<(a-ih,u)|
      &\le C e^{N\{\Re\psi(a-ih,0)+K/2+\tau\}} .
 \end{split}                                                       \tag{18}
\]
The second line is the full coherent real-period
interpolation estimate followed by exact degree-\(U\)
outside continuation. It is not an own-phase packet
for this two-angle pair. Both formulas retain every
row \(0\le j\le U\) and both parities, including their
original polynomial normalization.

The product therefore has rate
\[
                2\Re\psi(a-ih,0)+K/2+2\tau.
                                                                    \tag{19}
\]
The sine in (1) is uniformly bounded on (16), and
the crossing modulus is exactly
\[
                  |e^{3iN(a-ih)^2/(4\pi)}|
                                  =e^{3Nah/(2\pi)} .
                                                                    \tag{20}
\]
For \(h\ge h_c>0\) the full denominator gives
\[
 |W_N(a-ih)|
       \le\frac{e^{-Nh}}{(1-e^{-Nh_c})^2}
       \le C e^{-Nh}.
                                                                    \tag{21}
\]
At the exact half-grid boundary the better identity is
\[
 W_N(T_N-ih)=
       \frac{-\eta_Ne^{-Nh}}{(1+e^{-Nh})^2},\qquad
                  |W_N(T_N-ih)|\le e^{-Nh},
                             \quad h\ge0 .
                                                                    \tag{22}
\]
This includes \(h=0\), with no pole on that column.
No statement is made at other real angular points
where the original trace kernel has poles.

Combining (15),(19)--(22), using \(K\le1/2\),
\(a<\pi\), and \(h\le1/10\), yields
\[
 \begin{split}
 2\Re\psi(a-ih,0)+K/2-h+\frac{3ah}{2\pi}+2\tau
  &<\frac{13}{12}+\frac14+\frac3{20}+\frac1{5000}\\
  &=\frac{89}{60}+\frac1{5000}.
 \end{split}                                                       \tag{23}
\]
This applies both on the rectangle in (6) and the entire
column in (22).

Finally the adopted
[stronger actual inner action floor](research_mixed_next_inner_three_action_floor_and_top_rows.md)
gives \(s(u)>3/2+853/63000\). The exact reserve beyond
the claimed gap is
\[
 \frac32+\frac{853}{63000}
       -\left(\frac{89}{60}+\frac1{5000}\right)-\frac1{50}
                         =\frac{394}{39375}>0 .
                                                                    \tag{24}
\]
Equations (18)--(24) prove (6). The length of (5) is
uniformly bounded; absorb the original \(N^2/\pi\)
factor into (24) to obtain (7).

## 4. What remains of the right connection

In the exact remaining-current inventory of
[the short-pair transfer theorem, equations (28)--(30)](research_mixed_next_inner_three_short_pair_source_transfer.md),
choose the right connection as a lower path
\[
 \Gamma_R^{\rm mid}:
       \pi/2-iH(u)\longrightarrow5\pi/6-i/10
                                                                    \tag{25}
\]
followed by the paid path (5). With the original orientation
and scalar, its full current becomes
\[
 \mathcal C_N^R(u)=
 -\frac{N^2C_{N,3}}{\pi i}
      \int_{\Gamma_R^{\rm mid}}g_N^{<<}(t,u)W_N(t)\,dt
              +O(e^{N(s(u)-1/50)}).
                                                                    \tag{26}
\]
No estimate for the integral in (26) is asserted here.
The source in that integral is still exactly the same
short-by-short product (1); in particular no optional
top-strip trace deletion has been inserted into this
contour formula. Within the right connection, (25) is
the sole segment left by this theorem.
