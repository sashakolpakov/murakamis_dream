# Exact cancellation of the paired rectangle's full period sides

Research deduction, 8 November 2026. The meromorphic rectangle for
the old filtered next attachment may have its sides at real
coordinates zero and one. Its two entire vertical currents then
cancel exactly by the period of the literal finite integrand,
including their long-depth portions. Only two full horizontal
complements remain.

This is an exact contour reduction. It does not bound the added
horizontal intervals or assert that either complementary
coefficient is small. No phase branch, numerical evaluation, or
change to a frozen source is used.

## 1. The original filtered quotient is exactly periodic

Keep the old filter and finite sources in
[the paired meromorphic rectangle](research_mixed_next_paired_meromorphic_rectangle.md).
For \(D=N-1\), \(r=e^{-2\pi i/N}\), write
\[
 \begin{gathered}
 F_N^{\rm mid}=(I-\Pi_{\rm end})(F_{34,N}-R_N^a),\qquad
 l_N=\lfloor\delta N\rfloor,\quad B_N=\lceil11N/12\rceil,\\
 F_N^{\rm mid}(w,r^b)=0
       \quad(b\le l_N\ \hbox{or}\ b\ge B_N),\qquad
                         0<\delta<1/40.
 \end{gathered}                                                   \tag{1}
\]
Neither the lower cutoff nor any part of this filter is changed.

Set
\[
 \begin{split}
 A_N(Y;w,Z)&=F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z),\\
 K_N(y;w,z)&=\frac{N A_N(e^{-2\pi iy};w,e^{-2\pi iz})}
                                  {1-e^{-2\pi iNy}},
                         \qquad \beta=0,1.
 \end{split}                                                     \tag{2}
\]
The notation \(A_N\) in this note denotes this Laurent polynomial,
not the first-coordinate integer cutoff of an earlier note.
Its \(Y\)-band is contained in \([-D,2D]\).

Every exponent in the finite factors and denominator of (2) is
an integer. Consequently
\[
                             K_N(y+1)=K_N(y)                     \tag{3}
\]
as a meromorphic identity, with no parity sign. This is a statement
about the literal finite source, not about a logarithm of its
asymptotic phase.

The possible poles in \(y\) are the real physical nodes
\(y=b/N\) modulo one. The zero in (1) cancels each deleted-node
pole, identically in the outside parameters. In particular the
nodes at \(y=0,1\) are removable. Away from height zero the lines
\(\Re y=0,1\) have no denominator zero. Hence the full vertical
sides used below are regular after the specified removals.

At each retained node the original residue is
\[
 \operatorname*{Res}_{y=b/N}K_N
       =\frac{F_N^{\rm mid}(w,r^b)C_{\beta,N}(r^b,Z)}
                                      {2\pi iP_b}.
                                                                  \tag{4}
\]
Indeed the derivative of the denominator is \(2\pi iN\) there;
this cancels the \(N\) in (2). The conditional support zeros and
both level parities remain literal.

## 2. Move the sides to zero and one, then cancel them

Fix the original ordinary-next reference heights
\[
          h_*=\Im y_*\in(-.102,-.001),\qquad H=1/100,
                                                                  \tag{5}
\]
and keep them fixed when the outside parameters vary.
The original rectangle has half-grid real endpoints
\[
 L_N=(l_N+1/2)/N,\qquad R_N=(B_N-1/2)/N.
\]
For all sufficiently large \(N\), enlarge it to
\[
                     \mathcal C=[0,1]+i[h_*,H].                  \tag{6}
\]
The added left strip contains only deleted nodes \(0\le b\le l_N\);
the added right strip contains only deleted nodes \(B_N\le b<N\)
and the removable period copy at one. There is no added residue.
The integrand is holomorphic near the boundary of (6), including
its two real seam points.

Let both rectangle boundaries have counterclockwise orientation.
The residue theorem, or the two pole-free strip deformations,
gives the exact equality
\[
 \int_{\partial\mathcal C}K_N\,dy
   =\int_{\partial([L_N,R_N]+i[h_*,H])}K_N\,dy
   =\mathcal T_\beta[F_N^{\rm mid}].
                                                                  \tag{7}
\]
Here
\[
 \mathcal T_\beta[F]
 =N[Y^0](Fd_NC_{\beta,N})+N[Y^N](Fd_NC_{\beta,N})
 =\sum_{b=0}^{D}\frac{F(r^b)}{P_b}C_{\beta,N}(r^b,Z).
\]
There is no additional extraction scalar outside the integrals
of \(K_N\).

On the right side of (6), \(y=1+ih\) is traversed from \(h_*\)
to \(H\). On the left side, \(y=ih\) is traversed from \(H\)
to \(h_*\). Their total is therefore
\[
 i\int_{h_*}^{H}K_N(1+ih)\,dh
       -i\int_{h_*}^{H}K_N(ih)\,dh=0
                                                                  \tag{8}
\]
by (3), including the removable value at \(h=0\).
No estimate, small seam width, or actual-height inclusion in a
local source collar is needed for (8).

**Theorem 1.** The complete filtered transfer satisfies
\[
 \boxed{\qquad
 \mathcal T_\beta[F_N^{\rm mid}]
       =\int_{[0,1]+ih_*}^{\rightarrow}K_N(y)\,dy
        -\int_{[0,1]+iH}^{\rightarrow}K_N(y)\,dy .
 \qquad}                                                         \tag{9}
\]
Both arrows denote increasing real coordinate. The minus sign on
the second integral is the counterclockwise top orientation.
All long and short vertical currents have canceled before taking
any absolute value.

The corresponding horizontal enlargements are exactly
\[
                 [0,L_N]\quad\hbox{and}\quad[R_N,1]
                                                                  \tag{10}
\]
at each unchanged height in (5). Equation (8) does not assert
smallness of their individual integrals. Replacing the old sides
by zero without adding (10) would change the source.

## 3. Direct Laurent-band check of both horizontal terms

The sign and normalization in (9) can also be checked without
the residue calculation. On its lower line \(|Y|<1\), so
\[
 \frac{N A_N(Y)}{1-Y^N}
       =N A_N(Y)\sum_{m\ge0}Y^{mN}.
\]
The series converges uniformly on that circle. Since the lowest
degree of \(A_N\) is at least \(-D>-N\), only \(m=0\) contributes
to the constant coefficient. The increasing \(y\) period is
the original Fourier average; hence
\[
      \int_{[0,1]+ih_*}^{\rightarrow}K_N\,dy
                                      =N[Y^0]A_N.                \tag{11}
\]

On the upper line \(|Y|>1\),
\[
             -K_N=N A_N(Y)\sum_{m\ge1}Y^{-mN}.
\]
Here the highest degree of \(A_N\) is at most \(2D<2N\), so only
\(m=1\) contributes. Consequently
\[
      -\int_{[0,1]+iH}^{\rightarrow}K_N\,dy
                                      =N[Y^N]A_N.                \tag{12}
\]
These identities apply to the two complete coefficients separately.
They do not replace a factor by its value on the root grid or
average the already multiplied \(1+Y^{-N}\) a second time.

Thus (9) is consistent with the original full-period representation.
Its utility here is to remove the auxiliary vertical-boundary
obligation of the filtered rectangle, while displaying the
horizontal intervals that replace it. It supplies no new
horizontal suppression.

## 4. The precise remaining two horizontal complements

Let \(J_*\) be the fixed local geometric segment on the lower
period and \(\gamma_1=P+iH\), \(P=[11/50,9/20]\), the selected
central segment. Define
\[
 \mathscr R_N^{\rm cyc}
   =\int_{([0,1]+ih_*)\setminus J_*}^{\rightarrow}K_N\,dy
       -\int_{([0,1]+iH)\setminus\gamma_1}^{\rightarrow}K_N\,dy .
                                                                  \tag{13}
\]
Every complementary interval, including (10), is retained with
its displayed orientation.

The original local approximation identities from Section 4 of
the paired rectangle theorem are unchanged:
\[
 \begin{split}
 \int_{J_*}K_N\,dy&=I_{\rm geom,N}^{\rm mid}+\mathcal E_{0,N},\\
 -\int_{\gamma_1}^{\rightarrow}K_N\,dy
                         &=G_{1,N}^{\rm mid}+\mathcal E_{1,N}.
 \end{split}                                                     \tag{14}
\]
The local bottom error has the factor \(Y^N/(1-Y^N)\);
the top error has \(Y^{-N}/(1-Y^{-N})\), with the signs in (14).
Their absolute estimates use the already proved complete local
geometric source and complete selected-segment source respectively.
Those hypotheses, rather than small multipliers alone, pay the
errors.

Combining (9) and (14) gives the exact decomposition
\[
 \mathcal T_\beta[F_N^{\rm mid}]
  =I_{\rm geom,N}^{\rm mid}+G_{1,N}^{\rm mid}
       +\mathcal E_{0,N}+\mathcal E_{1,N}
       +\mathscr R_N^{\rm cyc}.
                                                                  \tag{15}
\]
The original paired-rectangle boundary remainder equals
\(\mathscr R_N^{\rm cyc}\) exactly: the total residue integral
and both central arcs are unchanged in (7).

The old-filter transfer and central corrections are already paid.
The full selected central source is paid by
[the complete selected-segment assembly](research_mixed_next_complete_prefix_selected_segment.md).
Therefore the same explicit \(\Delta/32\) allowance as in the
paired rectangle theorem, with \(\Delta=59/440000\), proves
\[
 \boxed{\quad
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
   \{\mathcal T_\beta[F_{34,N}]-I_{\rm geom,N}
                         -\mathscr R_N^{\rm cyc}\}\right]
            =O_{j,k}(e^{-N\Delta/32}) .
 \quad}                                                          \tag{16}
\]
The assertion holds on fixed small complex complete-color and
actual-output neighborhoods of both ordinary-next types, at
both parities and every fixed derivative order.
All paths are fixed at their base heights. The cancellation
(8) is an identity of holomorphic outside-parameter functions,
so it also holds after these derivatives.

No terminal-third conclusion is imported from the ordinary
selected-segment theorem. The exact identities (7)--(12) hold
for every outside parameter; the source estimate (16) has the
stated ordinary-next scope.

The remaining sufficient estimate is now purely horizontal:
for some fixed \(\epsilon>0\),
\[
 |\mathscr R_N^{\rm cyc}|
    \le C N^B
       e^{N\{\Re\mathcal P_\beta^+(w,z)-\epsilon\}},
                                                                  \tag{17}
\]
uniformly on those neighborhoods, or directly with fixed
normalized jets. It is an estimate of the signed sum in (13);
no separate bound for its two coefficients is required.
The local geometric term retains its original nonzero
\(N^{-2-\beta/2}\) coefficient if (17) is established.

In comparison with
[the filtered seam consequence](research_mixed_next_filtered_meromorphic_seam.md),
its two paid short side pieces and its remaining long side pieces
are all included in the exact cancellation (8) after the added
strips are restored. That earlier local quotient bound remains
valid and can be used on future contour pieces inside its collar.
It is not needed to infer (8), nor does it pay the full-height
horizontal additions (10). The present reduction establishes no
whole next-transfer asymptotic or new knot-family theorem.

