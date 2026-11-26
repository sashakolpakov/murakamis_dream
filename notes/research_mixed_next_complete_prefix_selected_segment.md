# The complete first incoming integral on the selected central segment

Research assembly, 8 November 2026. The complete original \(34\)
prefix, multiplied by the next conditional source and the selected
old-four weight, is exponentially below the actual following affine
action on the whole selected central segment. The first incoming
integration is complete: its initial interval, taper, plateau,
right interval, corner union and final real arc are all included.

This pays one central segment of the selected coefficient. The
complement of its second-coordinate cycle and the complementary
unselected source are not estimated here. The reference family is
ordinary-next, not the terminal-third graph. No numerical evaluation
or change to an earlier proof is used.

## 1. Exact source, domains and allocation

Set \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\). Keep the literal polynomials
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{D}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{\beta,N}(X,Y)&=\sum_{j=0}^{D}
                  X^{-j}p_j(X)p_j(Y)/P_j^{2+\beta},\\
 F_N(w,Y)&=F_{34,N}(w,Y)
       =N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)].
 \end{split}
 \tag{1}
\]
Every endpoint coefficient and every conditional sum is complete.
The polynomial \(d_N\) has degree at most \(D\) and satisfies
\(d_N(r^b)=P_b^{-1}\) on the original grid.

Use exactly the canonical ordinary-next family in
[the selected plateau theorem](research_mixed_second_selected_first_three_plateau_completion.md)
and [the incoming corner union](research_mixed_next_selected_incoming_corner_union.md):
\[
 \begin{gathered}
 (a_*,u_*,y_*,v_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),\quad
 \beta\in\{0,1\},\\
 c=s_4^*\in K_3\cup K_4,\qquad
 h_a=\Im a_*\in(-9/125,0),\qquad h_z=\Im z_*,\\
 P=[11/50,9/20],\qquad
 y=\xi+i/100,\quad z=\zeta+ih_z,\qquad \xi,\zeta\in P,\\
 X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz}.
 \end{gathered}
 \tag{2}
\]
Both \(u_*,v_*\) are ordinary indices. The external parameter and
all coordinate correlations are unchanged. This includes the
actual third ordinary vertex of a longer word beginning \(343\)
or \(344\), including length four. It makes no replacement by
an independent containing box or a terminal third vertex.

Retain the exact incoming integrand and outgoing allocation
\[
 \mathcal F_N(a;w,y,z)=
 U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z),
 \qquad W_\beta(Z)=|d_N(Z)|^{\beta/2}.
 \tag{3}
\]
At \(\beta=0\), \(W_\beta=1\), including at zeros of \(d_N\).
There is no incoming Fourier halfweight. Both the factorial and
polynomial-forcing alternatives of the selected weight remain.

For clarity, the original affine action is
\[
 \begin{split}
 Q_\beta(t;y,z)
 &=g(t+y)+g(t+z)-(2+\beta)g(t)-g(y)-g(z)+2\pi iyt,\\
 F_*&=Q_1(u_*;a_*,y_*)+Q_\beta(v_*;y_*,z_*)
                           -g(y_*)-\tfrac\beta2g(z_*),\\
 p_R&=g'(v_*+z_*)-(1+\beta/2)g'(z_*),\\
 \Lambda_{123}(z)&=\Re\{T_0(a_*)+F_*+p_R(z-z_*)\}.
 \end{split}
 \tag{4}
\]
All constants and lifts are original. The source (1) contains no
final Gram incidence; none is introduced by the following assembly.

## 2. Every part of the first incoming period

Fix one base reference and keep all its heights and paths fixed.
Use the following increasing incoming contour, from zero to one.
The entries in the last column are conservative finite rate losses
for the product (3), including \(W_\beta(Z)\), relative to (4).

| Part | Oriented path | Source and available loss |
|---|---|---|
| Initial | \(0\to1/10\), on the real axis | [Initial interval](research_mixed_second_selected_first_three_initial_interval.md), \(1/800\) |
| Left taper | \(a(x)=x+ih_a(x-1/10)/(3/25)\), \(1/10\le x\le11/50\) | [Left transition](research_mixed_second_selected_first_three_left_transition.md), \(1/800\) |
| Plateau | \(11/50+ih_a\to9/20+ih_a\) | [Selected plateau](research_mixed_second_selected_first_three_plateau_completion.md), Theorem 1, joined to the complete unselected cap plane, \(1/800\) |
| Right interval | \(9/20+ih_a\to1/2+ih_a\) | [Right segment](research_mixed_second_selected_first_three_right_segment.md), \(1/800\) |
| Corner union | \(1/2+ih_a\to1/2\to7/10\) | [Complete corner union](research_mixed_next_selected_incoming_corner_union.md), \(1/1000\) for the exact union integral |
| Final arc | \(7/10\to1\), on the real axis | [Coherent far-arc theorem](research_mixed_next_coherent_cap_far_arc.md), Section 5, \(1/200\) |

The plateau entry uses the attached identity
\(T_0'(a_*)+p_L=0\) exactly as in Section 2 of its source:
the cap and first-conditional affine terms cancel, and unused
quadratic terms are nonpositive. Its all-real-color version follows
from the original unselected cap envelope, as explicitly explained
in Section 3 of
[the real-color lift](research_mixed_selected_first_prefix_real_color_lift.md).
No first-type-four source is substituted.

The corner entry is intentionally an estimate for an integral,
not an absolute bound on its two old pieces. Its exact Cauchy
replacement runs
\[
 1/2+ih_a\ \longrightarrow\ 7/10+ih_a\
                               \longrightarrow\ 7/10.
 \tag{5}
\]
The full product is bounded on both replacement pieces. The
artificial old endpoint at \(1/2\) is canceled before estimating.
The two possible original vertical pieces through the old pair
height concatenate with their oriented signs into this same union.

For fixed \(N,w,y,z\), (3) is entire and one-periodic in \(a\):
it is a finite integer Laurent polynomial in the nonzero
exponential \(X(a)\). Thus the displayed chain is exactly
equivalent to the increasing real period. Each component retains
the original density \(+N\,da\); on the taper the actual
differential is \(a'(x)\,dx\), and on an upward vertical piece it
is \(i\,dh\). Therefore
\[
 F_N(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)
       =N\int_{\Gamma_a}\mathcal F_N(a;w,y,z)\,da .
 \tag{6}
\]
This is a finite-source identity. It does not use physical root
quadrature or a pointwise smallness assertion for \(Y^{-N}\) on
a lower contour.

## 3. The complete prefix on the selected segment

**Theorem 1.** Uniformly on (2), at all sufficiently large levels
of both parities and every real ordinary color \(w\in[-2,2]\),
\[
 \boxed{\quad
 |F_N(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,W_\beta(Z)
 \le C N^B
       e^{N\{\Lambda_{123}(z)-1/2000\}} .
 \quad}
 \tag{7}
\]
All fixed ordinary-color derivatives have the same conclusion
with polynomial costs and a smaller fixed gap. A sufficiently
small fixed complex neighborhood of complete color also has
the bound, with a smaller common gap.

*Proof.* Apply the six complete source bounds in the table to
the six terms of (6). For the corner term use its exact integrated
bound directly. Path lengths and the factors \(N\) and \(a'(x)\)
have only polynomial costs; \(h_a\) lies in a fixed compact
containing interval. Allocate the finitely many source and color
tolerances within the smallest listed gap. Summation and the
triangle inequality give the more conservative loss \(1/2000\).
Every source entry retains all its physical rows, true ends,
revived rows, Fourier remainders and unweighted joins. \(\square\)

In particular let \(\gamma_1=P+i/100\), with increasing orientation,
and define the central selected contribution
\[
 G_{1,N}(w,Z)=
 N\int_{\gamma_1}F_N(w,e^{-2\pi iy})
           d_N(e^{-2\pi iy})e^{2\pi iNy}
           C_{\beta,N}(e^{-2\pi iy},Z)\,dy.
 \tag{8}
\]
The same bound (7), with a polynomial factor, holds for
\(|G_{1,N}|W_\beta\). This keeps both original densities \(+N\):
one in (6), the other in (8).

At each reference base, all contours stay fixed before taking
complex neighborhoods and derivatives. The component estimates
have such neighborhoods with strict reserves, including the
zero-safe numerator continuation used in the corner theorem.
Cauchy's formula gives fixed mixed derivatives of the literal
integer-weighted source and its integrals, at polynomial cost.
The external modulus halfweight is neither differentiated nor
divided out on the full target plateau.

Near an actual ordinary output \(z_*\), the next action
\(\mathcal P_\beta^+\) has
\[
 \Lambda_{123}(z_*)=
 \Re\mathcal P_\beta^+(-2,z_*)-\frac\beta2\Re g(z_*).
 \tag{9}
\]
For \(\beta=1\), its \(O_4\) output lies in the proved nonzero
factorial packet domain for \(d_N(Z)\); for \(\beta=0\) no
halfweight is present. Exactly as in
[paired localization, Section 3](research_mixed_next_low_cardinal_paired_localization.md),
one may therefore remove this last allocation locally, retain
all polynomial factors, and shrink the fixed neighborhoods.
Consequently all fixed normalized mixed derivatives of (8)
are exponentially small relative to
\(e^{N\mathcal P_\beta^+(w,z)}\), with some fixed positive gap.
This local removal does not divide through a weight zero elsewhere.

## 4. The remaining exact coefficient remainders

The next complete transfer is still
\[
 \mathcal T_\beta[F_N]
 =N[Y^0](F_Nd_NC_{\beta,N})+
                       N[Y^N](F_Nd_NC_{\beta,N}).
 \tag{10}
\]
Both sectors occur for both next letters, because the old final
letter is four. This is the exact identity in
[next conditional attachment](research_mixed_three_four_next_conditional_attachment.md);
no additional root-average multiplier belongs in it.

For a concrete remaining-contour notation take the increasing
one-period paths
\(\Gamma_0=[0,1]+i\Im y_*\) and
\(\Gamma_1=[0,1]+i/100\). Let \(J_*\Subset\Gamma_0\) be the
fixed local stationary segment in
[the local next-source theorem](research_mixed_three_four_next_local_source.md),
and let \(I_{\rm geom,N}\) be its integral of the complete
unselected source \(F_Nd_NC_{\beta,N}\), with factor \(N\).
It has the original nonzero local geometric expansion.
Define, with all orientations retained,
\[
 \begin{split}
 R_{0,N}&=N\int_{\Gamma_0\setminus J_*}
                         F_Nd_NC_{\beta,N}\,dy,\\
 R_{1,N}&=N\int_{\Gamma_1\setminus\gamma_1}
                         F_Nd_NY^{-N}C_{\beta,N}\,dy.
 \end{split}
 \tag{11}
\]
Arguments \(Y=e^{-2\pi iy}\), \(w,Z\) are unchanged in each
integrand. Then the exact identity is
\[
        \mathcal T_\beta[F_N]
          = I_{\rm geom,N}+G_{1,N}+R_{0,N}+R_{1,N}.
 \tag{12}
\]
The new theorem pays \(G_{1,N}\). It does not pay \(R_{0,N}\)
or \(R_{1,N}\). A strict bound for their **combined** remainder
against the original next action would suffice to preserve the
nonzero local term. Separate complete-coefficient suppression is
not imposed when a valid paired estimate is available.

The already proved
[paired filtering correction](research_mixed_next_low_cardinal_paired_localization.md),
Section 5, applies to its specific older \(11/12\) cardinal
filter near actual ordinary outputs. Its central corrections
and the sum of its complementary corrections are small. Thus
independent whole-low-sector suppression is not an additional
obligation in that filtered formulation. The remaining middle
polynomial still needs its complementary-source estimate.
This assertion does not transfer the \(77/50\) correction bound
to the distinct \(8/9\) filter, or turn a physical-index deletion
into deletion of a continuous contour interval.

## 5. Scope

The result is a complete first incoming integration, and a full
selected central second-coordinate estimate, on the ordinary-next
family (2). The terminal-third graph has a different private
output role and is not covered by this assembly. Its local
geometric contribution is known, but this ordinary-source bound
cannot be transferred to that graph without its own comparisons.

The result may be joined to an already eligible suffix with the
same outgoing halfweight and affine marginal. It does not control
that suffix outside its proved domains, complete either Fourier
cycle in (10), supply a full \(343\) or \(344\) boundary theorem,
or establish a new short-filling knot family.
