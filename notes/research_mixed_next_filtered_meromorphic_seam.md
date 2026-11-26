# Paid seam crossings for the paired meromorphic rectangle

Research deduction, 8 November 2026. The complete seam-density bound
also controls the filtered meromorphic integrand through its removable
physical poles, on a smaller fixed collar. Both vertical sides of the
paired rectangle may then be moved exactly to seam half-grids, and a
fixed short central-height part of each side is paid.

The original physical filter and both original horizontal heights
remain unchanged. The long lower and upper side pieces, and the
additional horizontal strips at those heights, remain unestimated.
No numerical evaluation or frozen-source edit is used.

## 1. Sources and the actual output scope

Keep all notation and the old \(11/12\) filter of
[the paired rectangle](research_mixed_next_paired_meromorphic_rectangle.md).
In particular
\[
 \begin{gathered}
 l_N=\lfloor\delta N\rfloor,\quad B_N=\lceil11N/12\rceil,\quad
 0<\delta<1/40,\qquad
 F_N^{\rm mid}(r^b)=0\quad(b\le l_N\ \hbox{or}\ b\ge B_N),\\
 Y=e^{-2\pi iy},\qquad
 K_N(y)=\frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}
                                                  {1-Y^N}.
 \end{gathered}                                                   \tag{1}
\]
The fixed \(\delta\) is not changed below.

Use the complete bounds of
[the seam theorem, Sections 4--5](research_mixed_next_complete_source_seam_collar.md)
and its [all-typed action corollary](research_mixed_next_all_typed_seam_collar.md).
Together they cover every actual ordinary and terminal next-three
or next-four reference. They give one sufficiently small fixed
disk \(|Y-1|\le\varepsilon\), on which both full filtered densities
\[
 D_{\sigma,N}^{\rm mid}
       =F_N^{\rm mid}(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z),
                   \qquad \sigma=0,1,
                                                                  \tag{2}
\]
have normalized exponential loss \(1/2000\) on fixed small complex
complete-color and actual-output neighborhoods, with fixed mixed
derivatives. Its all-real-color upper assertion is retained.

The filtered claim is a pointwise source theorem, not only the
paired integral correction. Its proof uses the already fixed
unit-disk rate \(77/50\) of \(F_N-F_N^{\rm mid}\), the original
degree bound outside that disk, and the respective limiting costs
\[
 301/150<207/100,\qquad
 373/200<2,\qquad 5121/2500<17/8.
                                                                  \tag{3}
\]
No separate Fourier-coefficient estimate is assumed.

For ordinary-next-three outputs of nonnegative height, the
all-typed corollary retains the favorable original height coupling
and proves the stronger action floor \(431/200\); this pays the
same typed-disk rate. Its argument concerns actual correlated
references, not an independent output plateau. The final use
with the paired rectangle remains on that reduction's ordinary
family; the local seam bound itself also holds at terminal outputs.

## 2. The quotient is holomorphic and small on a fixed seam collar

Choose fixed \(s,t>0\) sufficiently small that
\[
 2s<\min(\delta,1/12),\qquad
 0<t<1/4000,\qquad
 \{e^{-2\pi iy}:|\Re y|\le2s,\ |\Im y|\le2t\}
                 \Subset\{|Y-1|<\varepsilon\}.
                                                                  \tag{4}
\]
Existence follows from continuity at \(y=0\). This choice can be
made after the already fixed filter, without changing any deleted
node. For sufficiently large \(N\) put
\[
       s_N=\frac{\lceil Ns\rceil-1/2}{N},\qquad
       \mathcal Q_N=[-s_N,s_N]+i[-2t,2t].
                                                                  \tag{5}
\]
Then \(s/2<s_N<2s\).

Every physical node in \(\mathcal Q_N\) is deleted in (1).
Indeed a nonnegative node \(b/N<2s<\delta\) has \(b\le l_N\);
a negative node corresponds by periodicity to
\(b/N>1-2s>11/12\), hence \(b\ge B_N\).
The node zero is deleted as well. The denominator in (1) has
simple zeros at these nodes and its numerator vanishes there.
Thus \(K_N\) is holomorphic on a neighborhood of
\(\mathcal Q_N\), with every such singularity removable.
No nonzero lower bound for \(F_N^{\rm mid}\), \(d_N\), or a
conditional numerator is used.

On either vertical boundary, \(N\Re y\) is a half integer, so
\[
 |1-Y^N|=1+e^{2\pi N\Im y}.
\]
On the lower and upper horizontal boundaries, respectively,
\[
 |1-Y^N|\ge1-e^{-4\pi Nt},\qquad
 |1-Y^N|\ge e^{4\pi Nt}(1-e^{-4\pi Nt}).
\]
Consequently, for all sufficiently large \(N\),
\[
 |K_N(y)|\le
 \begin{cases}
 2N|D_{0,N}^{\rm mid}(y)|,&\Im y\le0,\\
 2N|D_{1,N}^{\rm mid}(y)|,&\Im y\ge0
 \end{cases}
                     \qquad(y\in\partial\mathcal Q_N).
                                                                  \tag{6}
\]
The factor two is unnecessary on the vertical boundaries.

The normalization \(e^{-N\mathcal P_\beta^+(w,z)}\) is independent
of \(y\). Apply the maximum modulus principle in \(y\) to its
product with \(K_N\), using the complete density bound (2) on
(6). The smaller fixed rectangle
\[
                    \mathcal Q=[-s/2,s/2]+i[-t,t]
                                                                  \tag{7}
\]
lies in \(\mathcal Q_N\) with a fixed positive boundary distance
for all large \(N\). Cauchy's formula in \(y,w,z\), on smaller
fixed neighborhoods when necessary, therefore proves:

**Theorem 1.** On every stated seam reference family and both
parities,
\[
 \partial_y^a\partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}K_N(y;w,z)\right]
                    =O_{a,j,k}(e^{-N/4000}),\qquad y\in\mathcal Q,
                                                                  \tag{8}
\]
for each fixed derivative order. The same bound holds on every
integer translate of \(\mathcal Q\).

Here polynomial factors, including the original \(N\) in (1),
have been absorbed by the smaller displayed loss. The all-real
ordinary-color version follows from the corresponding complete
density bounds on (6), maximum modulus in \(y\), and Markov on
the complete ordinary polynomial; it uses the complete-color
action normalization. No modulus halfweight is differentiated.

In particular the bound includes the removable point \(Y=1\).
A density estimate divided pointwise by \(1-Y^N\) at this point
would not justify (8); the pole cancellation and boundary argument
are essential.

Every fixed bounded-length path in (7), including a path crossing
deleted physical nodes, now has the same exponentially small
integral. Homotopies within the holomorphic collar preserve that
integral exactly, with the endpoint orientations unchanged.

## 3. Exact relocation of both sides, with the old heights fixed

For the rest of this note use the ordinary-next family and the
reference heights of the paired rectangle:
\[
          h_*=\Im y_*\in(-.102,-.001),\qquad H=1/100.
                                                                  \tag{9}
\]
The geometric bottom segment \(J_*\) and selected top segment
\(\gamma_1=P+iH\) are unchanged. The choice \(t<1/4000\) ensures
\[
                         h_*<-t<t<H.
                                                                  \tag{10}
\]
Thus the theorem does not require either entire side to fit
inside the small collar.

The original half-grid endpoints are
\[
 L_N=(l_N+1/2)/N,\qquad R_N=(B_N-1/2)/N.
\]
Replace them by
\[
                 \widetilde L_N=\frac1{2N},\qquad
                 \widetilde R_N=1-\frac1{2N},
 \qquad
 \widetilde{\mathcal R}_N
       =[\widetilde L_N,\widetilde R_N]+i[h_*,H].
                                                                  \tag{11}
\]
For large \(N\) this enlarges the old rectangle. Every physical
node added on the left has \(1\le b\le l_N\), and every one
added on the right has \(B_N\le b\le N-1\).
All its residues are zero by the old filter. The exact residue
identity consequently gives
\[
 \boxed{\quad
 \int_{\partial\widetilde{\mathcal R}_N}K_N\,dy
     =\int_{\partial\mathcal R_N}K_N\,dy
     =\mathcal T_\beta[F_N^{\rm mid}].
 \quad}                                                          \tag{12}
\]
Both boundaries are counterclockwise and \(K_N\) already contains
the original factor \(N\). This is a pole-free contour
substitution on the two added strips, not a suppression estimate
for their separate edges.

The new short side pieces
\[
 \begin{split}
 \mathcal J_{L,N}&=[\,\widetilde L_N-it,\ \widetilde L_N+it\,],\\
 \mathcal J_{R,N}&=[\,\widetilde R_N-it,\ \widetilde R_N+it\,]
 \end{split}                                                     \tag{13}
\]
are written upward. For all large \(N\), the first lies in
\(\mathcal Q\) and the second in \(1+\mathcal Q\).
The boundary traverses the right piece upward and the left
piece downward. Hence
\[
 \mathscr S_N
   =\int_{\mathcal J_{R,N}}K_N\,dy
                      -\int_{\mathcal J_{L,N}}K_N\,dy
                                                                  \tag{14}
\]
has the bound (8), with the same fixed normalized outside jets.
These two continuous seam crossings are paid separately; no
cancellation between them is needed.

## 4. The exact pieces that remain

Remove \(J_*\), the reversed top segment \(-\gamma_1\), and the
two oriented short pieces (13) from
\(\partial\widetilde{\mathcal R}_N\). Let
\(\mathscr R_N^{\rm long}\) be the integral of \(K_N\) on the
remaining signed chain. It consists precisely of:

* the bottom interval
  \([\widetilde L_N,\widetilde R_N]+ih_*\) outside \(J_*\),
  traversed rightward;
* the top interval
  \([\widetilde L_N,\widetilde R_N]+iH\) outside \(\gamma_1\),
  traversed leftward;
* the right lower and upper side intervals with heights
  \([h_*,-t]\) and \([t,H]\), traversed upward;
* the left intervals with those same heights, traversed downward.

In particular the bottom and top each acquire the two real-coordinate
strips
\[
       [\widetilde L_N,L_N],\qquad [R_N,\widetilde R_N]
                                                                  \tag{15}
\]
at their original heights \(h_*\) and \(H\). Neither those strips
nor the long side pieces are paid by the small seam disk.
Their occurrence is necessary in the exact substitution (12).

The two central integrals in the paired rectangle theorem depend
only on \(J_*\), \(\gamma_1\), their unchanged heights, and the
same filtered polynomial. Its exact local error identities
therefore remain valid. Equations (12)--(14) and that theorem's
normalized error \(\Delta/32\), where \(\Delta=59/440000\), give
\[
 \boxed{\quad
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
  \{\mathcal T_\beta[F_N]-I_{\rm geom,N}
                     -\mathscr R_N^{\rm long}\}\right]
       =O_{j,k}(e^{-N\Delta/64}) .
 \quad}                                                          \tag{16}
\]
This assertion covers both actual ordinary-next types.
The local quotient bound (8) also holds on the
terminal families, but (16) does not import the ordinary selected
central theorem into a terminal-third graph.

Thus the new source theorem pays the two fixed short seam
crossings after an exact side relocation. It does not shorten the
original prescribed vertical depth without introducing (15).
A strict estimate on the remaining signed
\(\mathscr R_N^{\rm long}\), or another valid paired deformation,
is still required to preserve the geometric term in the complete
next transfer. No whole next-boundary or knot-family conclusion
is asserted here.

