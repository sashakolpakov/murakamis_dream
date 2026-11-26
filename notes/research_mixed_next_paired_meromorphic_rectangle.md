# An exact paired rectangle for the filtered next attachment

Research deduction, 8 November 2026. The two Fourier coefficients of
the next attachment can be represented by one meromorphic rectangle
whose only poles are the retained physical nodes. The deleted-node
ends then disappear by exact pole cancellation. This is a new
representation of the complete finite transfer, not deletion of
continuous arcs from either original coefficient.

The local geometric integral and the newly paid selected central
segment have exponentially small changes in this representation.
Consequently one explicitly oriented boundary remainder contains the
entire remaining problem. The theorem below does not bound that
remainder. A cardinal example proves why the deleted-node estimates
alone cannot bound its new vertical sides. No numerical evaluation or
change to a frozen source is used.

## 1. Exact finite source and the fixed old filter

Use
\[
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad
 P_j=(r;r)_j,\qquad p_j(Y)=(rY;r)_j,
\]
and the original complete sources
\[
 \begin{split}
 F_N(w,Y)&=F_{34,N}(w,Y),\qquad \deg_Y F_N\le D,\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
              \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
                  \qquad \beta=0,1,\\
 d_N(r^b)&=P_b^{-1},\qquad \deg d_N\le D.
 \end{split}                                                     \tag{1}
\]
The next complete transfer, before any final Gram incidence, is
\[
 \mathcal T_\beta[F]
 =N[Y^0](Fd_NC_{\beta,N})+N[Y^N](Fd_NC_{\beta,N})
 =\sum_{b=0}^{D}\frac{F(r^b)}{P_b}C_{\beta,N}(r^b,Z).
                                                                  \tag{2}
\]
This is [exact next attachment, Section 1](research_mixed_three_four_next_conditional_attachment.md).
The two coefficients occur for both next types. Root averaging is
applied once to the band \([-D,2D]\), not again after multiplying by
\(1+Y^{-N}\).

Retain precisely the old filter in
[low physical interval, Section 4](research_mixed_next_low_physical_interval.md)
and [paired localization, Section 5](research_mixed_next_low_cardinal_paired_localization.md).
Its fixed \(0<\delta<1/40\) and integer cutoffs are
\[
 A_N=\lceil23N/24\rceil,\qquad
 l_N=\lfloor\delta N\rfloor,\qquad B_N=\lceil11N/12\rceil.
                                                                  \tag{3}
\]
Write \(R_N^a\) for the first-coordinate deletion and set
\[
 \begin{split}
 \mathfrak l_{b,N}(Y)&=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu,\\
 \Pi_{\rm end}F&=\sum_{b\le l_N\ {\rm or}\ b\ge B_N}
                                    F(r^b)\mathfrak l_{b,N},\\
 F_N^{\rm mid}&=(I-\Pi_{\rm end})(F_N-R_N^a),\qquad
 E_N^{\rm all}=F_N-F_N^{\rm mid}.
 \end{split}                                                     \tag{4}
\]
Thus
\[
 F_N^{\rm mid}(r^b)=0\quad(b\le l_N\ {\rm or}\ b\ge B_N).
                                                                  \tag{5}
\]
All first-coordinate overlaps are included in (4). The complete
transfer of \(E_N^{\rm all}\) is already small, and the correction
has the proved unit-disk rate \(77/50\). The different \(8/9\)
filter is not used.

Work on the actual ordinary-next reference family of
[the complete selected-segment assembly](research_mixed_next_complete_prefix_selected_segment.md).
In particular
\[
 y_*\in O_4,\qquad -.102< h_*:=\Im y_*<-.001,\qquad
 .24<\Re y_*<.36.
                                                                  \tag{6}
\]
The outside coordinates and all their correlations are unchanged.
The output is near its actual ordinary value \(z_*\), and
\(Z=e^{-2\pi iz}\). Let \(\mathcal P_\beta^+(w,z)\) denote the
original next conditional action.

Choose the fixed local stationary segment
\[
 J_*=[\,y_*-\epsilon,\ y_*+\epsilon\,]
 \Subset[11/50,9/20]+ih_*
                                                                  \tag{7}
\]
of [the local next-source theorem](research_mixed_three_four_next_local_source.md).
The positive \(\epsilon\) is fixed before \(N\) and can be chosen
uniformly on the compact reference family. Also put
\[
 H=1/100,\qquad \gamma_1=[11/50,9/20]+iH.
                                                                  \tag{8}
\]
Paths and heights are held fixed at each base reference when the
outside parameters vary.

## 2. The single meromorphic rectangle, with its exact scalar

Define
\[
 K_N(y;w,z)=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}
                       {1-Y^N},
 \qquad Y=e^{-2\pi iy}.
                                                                  \tag{9}
\]
The numerator is holomorphic in finite \(y\); its negative powers
of \(Y\) have no finite poles. The only possible poles of (9) are
the physical nodes \(y=b/N\) modulo one. At a node deleted in
(5), the numerator has a zero, so that pole is removable. This
assertion uses only the polynomial zero and the simple zero of
\(1-Y^N\); no factorial or Fourier polynomial is divided out.

At a retained node \(B=r^b\),
\[
 (1-Y^N)'_{\,y=b/N}=2\pi iN,\qquad
 \operatorname*{Res}_{y=b/N}K_N
       =\frac{F_N^{\rm mid}(w,B)C_{\beta,N}(B,Z)}
                                      {2\pi iP_b}.
                                                                  \tag{10}
\]
This retains all exact support zeros in the conditional kernel.

For sufficiently large \(N\), set
\[
 L_N=\frac{l_N+1/2}{N},\qquad
 R_N=\frac{B_N-1/2}{N},\qquad
 \mathcal R_N=[L_N,R_N]+i[h_*,H].
                                                                  \tag{11}
\]
Both segments (7)--(8) lie strictly between its vertical sides.
Its interior real nodes are exactly
\(l_N<b<B_N\). Give \(\partial\mathcal R_N\) its counterclockwise
orientation: bottom rightward, right side upward, top leftward,
left side downward.

**Theorem 1.** For every level for which (11) contains (7)--(8),
every outside parameter, and both \(\beta\),
\[
 \boxed{\qquad
       \mathcal T_\beta[F_N^{\rm mid}]
          =\int_{\partial\mathcal R_N}K_N(y)\,dy .
       \qquad}                                                   \tag{12}
\]
There is no additional factor \(N\) outside this integral.

*Proof.* The residue theorem and (10) give exactly the sum in
(2), restricted to the retained nodes. Equation (5) makes that
sum equal to the complete transfer of \(F_N^{\rm mid}\).
The factor \(N\) in (9) cancels the \(N\) in the derivative of
its denominator, which proves the normalization in (12).
Both parities have the same simple physical poles. \(\square\)

Equivalently, cardinal interpolation gives the exact rational identity
\[
 \frac{N F(Y)}{1-Y^N}
       =-\sum_{b=0}^{D}F(r^b)\frac{r^b}{Y-r^b},
                         \qquad \deg F\le D.
                                                                  \tag{13}
\]
For \(F=F_N^{\rm mid}\), its only terms are the retained nodes.
Formula (13) is an alternative check of every residue in (10).

In relation to the old two full-period circles, (12) pairs their
opposite rational contours, then moves the side boundaries through
the regions whose poles are removable. It does not assert that
the original polynomial integrands vanish on those arcs.

## 3. The half-grid currents have no kernel debit

On either vertical side of (11), write \(y=t+ih\). Then
\(Nt\) is an integer plus one half, so
\[
              Y^N=-e^{2\pi Nh},\qquad
              |1-Y^N|=1+e^{2\pi Nh}.
                                                                  \tag{14}
\]
Consequently, with all finite factors still literal,
\[
 |K_N(t+ih)|
 \le
 \begin{cases}
 N|F_N^{\rm mid}d_NC_{\beta,N}|,&h\le0,\\
 N|F_N^{\rm mid}d_NY^{-N}C_{\beta,N}|,&h\ge0.
 \end{cases}                                                     \tag{15}
\]
At height zero the divisor is exactly two. There is no singular
junction or missing half residue. On a vertical side \(dy=i\,dh\);
the left side is traversed downward. All four weighted half-sides
remain in the oriented boundary (12).

Thus an actual source bound for the original unwrapped density on
the lower sides, or the selected density on the upper sides,
passes to (9) with only its original polynomial factor \(N\).
Equation (15) is not such a source bound by itself.

## 4. The two retained central arcs and their exponential errors

On the bottom, \(Y^N=e^{-2\pi iN\Re y}e^{2\pi Nh_*}\).
Therefore
\[
 K_N=N F_N^{\rm mid}d_NC_{\beta,N}
       +N F_N^{\rm mid}d_NC_{\beta,N}
                            \frac{Y^N}{1-Y^N}.
                                                                  \tag{16}
\]
The second multiplier is uniformly
\(O(e^{2\pi Nh_*})\) along that entire horizontal line. On the top,
\[
 -K_N=N F_N^{\rm mid}d_NY^{-N}C_{\beta,N}
       +N F_N^{\rm mid}d_NY^{-N}C_{\beta,N}
                            \frac{Y^{-N}}{1-Y^{-N}},
                                                                  \tag{17}
\]
whose last multiplier is \(O(e^{-2\pi NH})\).
The minus sign in (17) is precisely the reversed top orientation.

These multiplier statements need a bound on their actual sources
before they become small absolute errors. Such bounds are already
available on \(J_*\) and \(\gamma_1\), as follows.

On \(J_*\), all three complete factors have their proved original
packets. After the conditional index is eliminated, their combined
phase has a nondegenerate stationary point at \(y_*\) and a negative
real second derivative on a sufficiently small fixed segment.
This is the local proof in Sections 3--4 of
[the next-source theorem](research_mixed_three_four_next_local_source.md).
Its integrand thus has upper rate
\(\Re\mathcal P_\beta^+(-2,z_*)\), with polynomial prefactors;
small fixed parameter neighborhoods consume an arbitrarily small
rate tolerance. The local stability of the old filter, in
[low physical interval, Section 4](research_mixed_next_low_physical_interval.md),
gives the same conclusion for \(F_N^{\rm mid}\).
The factor \(e^{2\pi Nh_*}\), with \(h_*< -1/1000\), pays these
tolerances with a fixed strict gap.

On \(\gamma_1\), the complete selected-segment assembly bounds the
full \(F_N\) selected density pointwise. The selected central
correction of \(E_N^{\rm all}\) is pointwise small by
[paired localization, Sections 2--3 and 5](research_mixed_next_low_cardinal_paired_localization.md)
and its cited selected-plateau estimate. Subtraction gives the same
pointwise bound for \(F_N^{\rm mid}\). Both alternatives of the
Fourier weight remain in these estimates. Multiplication by the
last factor of (17) only improves their gap.

At an actual next-four output the proved nonzero \(d_N(Z)\)
packet removes the outgoing allocation locally, exactly as in
Section 3 of the selected-segment assembly; for a next three
there is no outgoing halfweight. No removal is made at an
independent output zero. These source bounds and (16)--(17)
therefore imply, on smaller fixed complex neighborhoods,
\[
 \begin{split}
 \int_{J_*}K_N\,dy
     &=I_{\rm geom,N}^{\rm mid}+\mathcal E_{0,N},\\
 -\int_{\gamma_1}^{\rightarrow}K_N\,dy
     &=G_{1,N}^{\rm mid}+\mathcal E_{1,N},
 \end{split}                                                     \tag{18}
\]
where the arrow denotes increasing real coordinate and
\[
 \begin{split}
 I_{\rm geom,N}^{\rm mid}
     &=N\int_{J_*}F_N^{\rm mid}d_NC_{\beta,N}\,dy,\\
 G_{1,N}^{\rm mid}
     &=N\int_{\gamma_1}F_N^{\rm mid}d_NY^{-N}C_{\beta,N}\,dy .
 \end{split}                                                     \tag{19}
\]
Both errors in (18) are exponentially smaller than
\(e^{N\mathcal P_\beta^+}\), including every fixed normalized
mixed derivative. This is a local assertion on the two indicated
arcs, not an estimate for the rest of the bottom or top.

The geometric integral has the original nonzero expansion
\[
 I_{\rm geom,N}^{\rm mid}
 =N^{-2-\beta/2}\mathcal A_\beta(w,z)
        e^{N\mathcal P_\beta^+(w,z)}
                    (1+O_{\rm hol}(N^{-1})),\qquad
                         \mathcal A_\beta\ne0.
                                                                  \tag{20}
\]
The filter does not change its coefficient, and
\(I_{\rm geom,N}^{\rm mid}-I_{\rm geom,N}\) is exponentially small.
The complete selected integral \(G_{1,N}^{\rm mid}\) is also
exponentially small by the same source estimates.

## 5. The exact remaining signed boundary and sufficient bound

Remove the oriented bottom segment \(J_*\) and the oriented
top segment \(-\gamma_1\) from \(\partial\mathcal R_N\).
Define the remaining signed chain
\[
 \mathfrak B_N=
 ([L_N,R_N]+ih_*)\setminus J_*
 +[R_N+ih_*,R_N+iH]
 -\bigl(([L_N,R_N]+iH)\setminus\gamma_1\bigr)
 -[L_N+ih_*,L_N+iH]
                                                                  \tag{21}
\]
and its actual finite-source integral
\[
                         \mathscr R_N=\int_{\mathfrak B_N}K_N\,dy.
                                                                  \tag{22}
\]
The two horizontal complements in (21) have increasing coordinate
before their displayed signs. The chain retains all four
vertical half-currents in (15).

Equations (12) and (18) give the exact decomposition
\[
 \mathcal T_\beta[F_N^{\rm mid}]
 = I_{\rm geom,N}^{\rm mid}+G_{1,N}^{\rm mid}
       +\mathcal E_{0,N}+\mathcal E_{1,N}+\mathscr R_N.
                                                                  \tag{23}
\]
Here the errors are defined by the exact differences in (18);
no approximation has been inserted into (22).

Let
\[
                         \Delta=\frac{59}{440000}.
\]
The old-filter theorem and paired localization give the transfer
and local correction errors with fixed gaps at least the
conservative multiples of \(\Delta\) stated there.
The selected-segment gap and the factors in (16)--(17) are larger
than the allowance below. After common fixed neighborhood
shrinkage and Cauchy costs, (23) implies
\[
 \boxed{\quad
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
  \{\mathcal T_\beta[F_N]-I_{\rm geom,N}-\mathscr R_N\}\right]
       =O_{j,k}(e^{-N\Delta/32}) .
 \quad}                                                          \tag{24}
\]
All paths in (21) remain fixed at their base heights when these
derivatives are taken; their half-grid real endpoints depend only
on \(N\). The finite source and its poles are holomorphic in the
outside parameters. No modulus halfweight is differentiated.

Thus the one remaining sufficient inequality is
\[
 \left|\mathscr R_N(w,z)\right|
 \le C N^B e^{N\{\Re\mathcal P_\beta^+(w,z)-\varepsilon\}},
                    \qquad \varepsilon>0,
                                                                  \tag{25}
\]
uniformly on fixed complex neighborhoods of the actual
ordinary-next family. Such a bound, with Cauchy on smaller
neighborhoods, would preserve the nonzero coefficient (20) in the
complete transfer. It need not bound the four components of (21)
separately. Equivalently it is enough to establish the corresponding
normalized fixed-jet bound directly. This note proves (24), not (25).

This reduction concerns the actual ordinary-next outputs.
It does not supply the separate terminal-third reference
comparisons or an ordinary closing theorem.

## 6. Why the deleted physical values do not bound the new sides

The obstruction is exact and does not rely on an asymptotic trial.
Take any retained node \(B=r^b\), \(l_N<b<B_N\), and choose the
degree-\(D\) polynomial \(F=\mathfrak l_{b,N}\). All its deleted
physical values vanish, and its only nonzero physical value is
\(F(B)=1\). Yet (13) gives
\[
                 \frac{N\mathfrak l_{b,N}(Y)}{1-Y^N}
                                =-\frac{B}{Y-B}.
                                                                  \tag{26}
\]
At either half-grid side at height zero, \(Y\) and \(B\) are
different unit roots of the relevant half-grid equation. Thus
\[
 \left|\frac{N\mathfrak l_{b,N}(Y)}{1-Y^N}\right|
       =\frac1{|Y-B|}\ge\frac12 .
                                                                  \tag{27}
\]
There is no exponential suppression. Moreover
\[
                |\mathfrak l_{b,N}(Y)|
                   =\frac{2}{N|Y-B|}\ge\frac1N.
                                                                  \tag{28}
\]
These bounds include both parities and every possible retained
node. Choosing a node a fixed angular distance from a side makes
the quantities in (26)--(28) bounded above by constant or
polynomial factors as well.

In particular there cannot be an estimate for the side values
depending only on the deleted physical values: its right side
would be zero for this example, while (27) is positive. Nor does
the presence of a whole interval of consecutive deleted zeros,
by itself, force an exponential side loss relative to the retained
values. Arbitrary scalar multiples preserve this obstruction.

The actual \(F_N^{\rm mid}\) has additional coherent source
structure, which the cardinal example does not model. That
structure may prove (25). Equations (26)--(28) show precisely
why the low/high physical deletion theorems alone cannot do so.
The new rectangle keeps the necessary coherent Cauchy observation
of all retained nodes, rather than replacing it by a positive
bound involving only neighboring deleted nodes.

