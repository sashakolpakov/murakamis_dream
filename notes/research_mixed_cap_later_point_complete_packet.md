# The complete original cap near the exact later incoming point

Research assembly, 8 November 2026. The original type-three cap
has a nonzero asymptotic expansion on a fixed complex neighborhood
of the exact later incoming point and complete ordinary color.
The proof retains every physical row, both horizontal aliases,
all four weighted vertical currents, and every unweighted join.
The westward endpoint theorem supplies the previously conditional
source premise for its actual main path.

This is a local theorem for the whole cap polynomial. It is not
a theorem on the entire real incoming arc, the selected following
contraction, or a family of fillings. No numerical evaluation,
replay, or change to a frozen source is used.

## 1. Literal source, critical point, and statement

Keep the original finite polynomial
\[
 U_{0,N}(w,X)=
    \sum_{j=0}^{N-1}H_N(w,r^{-j})\frac{p_j(X)}{P_j},
 \qquad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j.
 \tag{1}
\]
The complete endpoint function and exact retained-row interpolation
are
\[
\begin{split}
 C_N(e,w)&=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\\
 \mathscr A_N(e,a,w)&=
       D_N(e)^{-1}C_N(e,w)\frac{\Pi_N(a+e)}{\Pi_N(a)},\qquad
 \Pi_N(z)=D_N(z)G_N(Nz).
\end{split}
 \tag{2}
\]
At \(e=j/N\), the second line is exactly the \(j\)-th row in
(1), with \(X=e^{-2\pi ia}\). All ordinary normals, marked
factorials, Newton terms, and primitive constants are those of
[the original outer-cap source](research_mixed_cap_outer_contour_reduction.md).
No endpoint coefficient is removed from a signed sum.

At complete ordinary color define
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\\
 \Psi(e,a,-2)&=S(e)+J(a+e)-J(a)-i\pi ae,
\end{split}
 \tag{3}
\]
where \(u_c\) is the original zero-lift critical branch.
The nearby ordinary-color phase replaces \(S(e)\) by its
original holomorphic continuation \(S(e,w)\).

Set
\[
\begin{gathered}
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\qquad
 a_0=1-\frac{\Arg X_0}{2\pi},\\
 e_0=\frac14-\frac{i\log2}{4\pi},\qquad h_0=\Im e_0.
\end{gathered}
 \tag{4}
\]
The exact original identities in
[the curve obstruction](research_mixed_cap_auxiliary_real_curve_obstruction.md)
give \(1/2<a_0<7/10\), \(\Psi_e(e_0,a_0,-2)=0\), and
\[
             \Psi_{ee}(e_0,a_0,-2)
                  =-4\pi\sqrt2+\frac{8\pi i}{3}\ne0.
 \tag{5}
\]
Let \(e_*(a,w)\) be its implicit local continuation, and put
\(\mathcal T(a,w)=\Psi(e_*(a,w),a,w)\),
\(M_0=\Re\mathcal T(a_0,-2)\).

**Theorem.** There is a fixed open complex neighborhood
\(\mathcal U\) of \((a_0,-2)\) such that
\[
 U_{0,N}(w,e^{-2\pi ia})
    =N^{-1}\mathcal B(a,w)e^{N\mathcal T(a,w)}
                      \bigl(1+O_{\rm hol}(N^{-1})\bigr),
 \qquad \mathcal B(a,w)\ne0.
 \tag{6}
\]
The limit includes both integer parities. If \(A(e,w)\) is the
original endpoint coefficient, then
\[
 \mathcal B(a,w)=
 \frac{\sqrt{2\pi}\,A(e_*(a,w),w)}
      {\sqrt{-\Psi_{ee}(e_*(a,w),a,w)}}
       \sqrt{\frac{\sin\pi(a+e_*(a,w))}{\sin\pi a}}.
 \tag{7}
\]
Every square root is the original Gaussian/factorial branch.
On each smaller fixed neighborhood and for every fixed
nonnegative \(j,k\),
\[
 \partial_a^j\partial_w^k
 \left[
   \frac{N e^{-N\mathcal T(a,w)}
          U_{0,N}(w,e^{-2\pi ia})}{\mathcal B(a,w)}-1
 \right]=O(N^{-1}).
 \tag{8}
\]
This is a statement in the ordinary color \(w\). It makes no
nonzero asymptotic claim at remote real colors.

## 2. Discharging the full main-path source premise

The main-contour proof uses the whole endpoint packet on a fixed
neighborhood of
\[
 \mathcal R_{\rm west}
   =\{E-i\eta:23/100\le E\le49/100,\quad0\le\eta\le3/50\}.
 \tag{9}
\]
This is now an established domain, not an assumed width of a
neighborhood of the critical path:

* For \(23/100\le E\le6/25\) and
  \(0\le\eta\le\eta_0(E)\), use
  [the region above the auxiliary-real curve](research_mixed_endpoint_region_above_real_curve.md).
  Its restriction to \(\eta\le3/50\) is sufficient.
* For the same real interval and
  \(\eta_0(E)\le\eta\le3/50\), use
  [the westward below-curve theorem](research_mixed_endpoint_west_below_curve.md).
  The correlated reciprocal-depth bound and both real-cut
  comparisons there pay every revived row and current.
* For \(6/25\le E\le49/100\), use
  [the assembled complete lower rectangle](research_mixed_endpoint_complete_lower_rectangle.md).

The two western depth ranges cover every point of their vertical
section; an empty below-curve section requires nothing. The
three sources are the identical finite function (2), with the
same original critical branch, additive action constant, nonzero
coefficient, and Gaussian square root. Their fixed open
neighborhoods give a fixed neighborhood of the compact set
(9), after a finite cover and a common ordinary-color shrink.
They agree on overlaps, including zero auxiliary height.
Consequently
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                         (1+O_{\rm hol}(N^{-1})),\quad A\ne0
 \tag{10}
\]
holds on that full neighborhood, with every fixed normalized
mixed derivative and both parities.

This proves premise (W) of
[the later-point main-contour theorem](research_mixed_cap_later_point_main_contour.md).
The early curve and its left join use the separate curve and
above-curve theorems on real parts from \(1/8\) to \(23/100\);
no extension of the rectangle (9) to that whole western range
is assumed.

## 3. Exact row partition and residue identity

Fix at the base \(a_0\) the cut from
[the upper-end theorem](research_mixed_cap_upper_end_currents.md):
\[
 b=\min\{49/100,1-a_0-\delta\}>1/4,\qquad
 0<\delta<1/100,\qquad a_0+b\le1-\delta.
 \tag{11}
\]
Its fixed collar and critical-point separation conditions are
those of that theorem. Any reduction of \(\delta\) required
by the long upper-right theorem is made once, before the cuts
are fixed. Put
\[
\begin{gathered}
 L_N=\lfloor N/8\rfloor+1,\qquad K_N=\lceil Nb\rceil,\\
 \ell_N=(L_N-1/2)/N,\qquad b_N=(K_N-1/2)/N.
\end{gathered}
 \tag{12}
\]
Thus (1) is the exact sum of the lower physical rows
\(0\le j<L_N\), the retained rows \(L_N\le j<K_N\), and
the upper physical rows \(K_N\le j<N\).
At nearby parameters these integer sets remain fixed.

On the rectangle with real sides \(\ell_N,b_N\) and heights
\(-1,+1\), the exact interpolation (2) is holomorphic:
the private and incoming real arguments lie strictly in
their original strips, and the nonreal extensions are the
specified canonical functions. The entire rectangle remains
valid after a sufficiently small fixed parameter shrink.
The counterclockwise residue formula is
\[
 \sum_{j=L_N}^{K_N-1}\mathscr A_N(j/N,a,w)
  =\frac1{2\pi i}\oint
     \mathscr A_N(e,a,w)\,\pi N\cot(\pi Ne)\,de.
 \tag{13}
\]
There are no additional private poles.

For precision, orient the upper boundary path as
\[
 \Gamma_N^+:\quad b_N\longrightarrow b_N+i
                    \longrightarrow\ell_N+i
                    \longrightarrow\ell_N,
\]
and the lower boundary path as
\[
 \Gamma_N^-:\quad\ell_N\longrightarrow\ell_N-i
                    \longrightarrow b_N-i
                    \longrightarrow b_N .
\]
Their union is the counterclockwise outer boundary.
The exact split \(\cot=-i+(\cot+i)\) above and
\(\cot=i+(\cot-i)\) below gives
\[
\begin{split}
 \sum_{j=L_N}^{K_N-1}\mathscr A_N(j/N,a,w)
  ={}&N\int_{\ell_N}^{b_N}\mathscr A_N(e,a,w)\,de\\
   &+\frac{N}{2i}\int_{\Gamma_N^+}
          \mathscr A_N(e,a,w)(\cot(\pi Ne)+i)\,de\\
   &+\frac{N}{2i}\int_{\Gamma_N^-}
          \mathscr A_N(e,a,w)(\cot(\pi Ne)-i)\,de .
\end{split}
 \tag{14}
\]
The constants give \(+N/2\) times the real integral on
each sign; hence the total zero-mode density is exactly
\(+N\). There are six weighted pieces in (14): two
horizontal aliases and four vertical sign-halves.
This identity does not delete a contour endpoint.

## 4. Complete source inventory and color scope

All of the following gaps refer to the same original
\(M_0\) at the base point. The quoted theorems also preserve
their bounds on fixed small complex neighborhoods where stated.

| Original source group | Estimate and color scope |
| --- | --- |
| Lower physical rows \(0\le j<L_N\) | Section 4 of the [main-contour theorem](research_mixed_cap_later_point_main_contour.md) gives a strict positive-sum gap, including the separate true lower end; all real ordinary colors and their fixed derivatives. |
| Upper physical rows \(K_N\le j<N\) | [Upper-end completion](research_mixed_cap_upper_end_currents.md) gives a strict positive-sum gap, including the prewall collar, every wrapped row and the true upper end; all real ordinary colors. |
| Upper and lower horizontal aliases at heights \(+1,-1\) | The [tall upper](research_mixed_cap_tall_upper_alias.md) and [tall lower](research_mixed_cap_tall_lower_alias.md) theorems give finite own-action gaps; all real colors, both parities and all auxiliary rows. |
| Both complete left vertical currents | [Later-point left currents](research_mixed_cap_later_point_left_currents.md) give gap \(1/160\) from height zero to each of \(+1,-1\); all real colors, without a large-height endpoint packet. |
| Short right vertical currents, heights \([0,1/25]\) and \([-3/50,0]\) | [Upper-end completion](research_mixed_cap_upper_end_currents.md), Section 4, gives strict gaps at complete ordinary color and on a fixed small complex color/incoming neighborhood. A remote-real-color contour estimate is not asserted. |
| Long right vertical currents | The [upper long side](research_mixed_cap_upper_right_long_side.md) gives gap \(1/500\) on heights \([1/25,1]\); the [lower long side](research_mixed_cap_lower_right_long_side.md) gives gap \(1/250\) on \([-1,-3/50]\). Both retain the literal whole auxiliary source and hold at all real colors. |
| Zero mode and every unweighted joining piece | The [main-contour theorem](research_mixed_cap_later_point_main_contour.md), now with (W) proved in Section 2, gives the nonzero local \(N^{-1}\) expansion near complete color. Its whole path and both endpoint joins remain in that integral. |

In particular the right sign-halves in (14) are each the
union of their short and long portions, with their original
orientations. No extra constant-mode contribution arises at
the splitting heights. All cited positive finite-source bounds
include both level parities, ordinary polynomial zeros, and
the full auxiliary rows that revive at a nonphysical index.

For the groups with all-real bounds, the reference exponent is
the complete-color \(M_0\), not an unproved far-color action.
Their fixed ordinary derivatives have polynomial costs before
summation. The short right currents and main asymptotic use
only the complete-color point and its proved small complex
neighborhood. This suffices for (6)--(8), and does not assert
a nonzero packet uniformly on the entire real color period.

## 5. The actual zero mode and all its joins

For clarity, the source-valid deformation of the first line
of (14) is the following path, with
\[
 e_L=\frac18-i\eta_0(1/8),\qquad
 t_d=\frac{11}{12\sqrt2},\qquad
 e_d=\frac{\Log(1-2t_d^2+2it_d)}{2\pi i}=E_d-i\eta_d:
\]

1. \(\ell_N\) to \(1/8\) along the real line, then vertically
   to \(e_L\);
2. the auxiliary-real curve from \(e_L\) to \(e_d\);
3. the vertical segment to \(E_d+ih_0\);
4. the horizontal segment through \(e_0\) to \(b_N+ih_0\);
5. the vertical segment to \(b_N\).

The complete source premise needed in pieces 3--5 is exactly
(9), now proved. The first two pieces use the curve and
above-curve source theorems. The main-contour proof gives the
real lower-cut gap \(1/80\), a strict gap on the entire early
curve, and the strictly subcritical departure at \(e_d\).
Vertical convexity pays piece 3; horizontal concavity gives
the unique maximum at the interior point \(e_0\) on piece 4.
Upper-end completion pays piece 5. The small real displacement
at \(\ell_N\) preserves its strict gap.

These are the unweighted constant-mode joins. They have not
been discarded in estimating the six weighted currents.
Every fixed part of this path away from the critical point
has a uniform strict gap. Its exact integral is the real
zero mode in (14), by holomorphy and equal endpoints.

On the path the original row symbol is
\[
 N^{-3/2}A(e,w)
    \sqrt{\frac{\sin\pi(a+e)}{\sin\pi a}}\,
       e^{N\Psi(e,a,w)}(1+O_{\rm hol}(N^{-1})).
 \tag{15}
\]
The interior critical point is nondegenerate by (5) and is
crossed with the original horizontal Gaussian orientation.
Its factor \(N^{-1/2}\), multiplied by the row \(N^{-3/2}\)
and the exact density \(+N\), gives \(N^{-1}\), with the
coefficient (7). This is the original conditional main theorem,
with its source premise explicitly discharged.

## 6. Assembly, derivatives, and the remaining scope

Take a common positive minimum of the finitely many strict
source gaps in Section 4 and of the main-path gaps away from
its saddle. Keep the integers in (12) and every base path
fixed before varying \(a,w\). The complete endpoint source
cover, the exact global interpolation, and the zero-safe
physical-row bounds preserve those estimates on one fixed
complex neighborhood of \((a_0,-2)\), after a common shrink.
The nearby saddle is treated in its implicit regular chart;
this does not require any macroscopic contour extrapolation.

Equation (1), its exact physical partition, and (14) therefore
give the main integral with exponentially smaller errors.
The original action and amplitude of that integral are
precisely (3)--(7). Absorbing the exponential errors into its
relative \(O(N^{-1})\) error proves (6). The amplitude is
nonzero because the original endpoint coefficient, Gaussian
Hessian, and the two sine factors are nonzero on the retained
critical chart. Shrink once more if needed.
Cauchy's formula on smaller fixed neighborhoods proves (8).
Neither the moving cut nor a reference-dependent path is
differentiated.

Every physical row and every residue current of the whole
original cap has now been included locally at this exact
incoming point. This conclusion does not continue the main
path or left-current comparison to all
\(a\in[1/2,7/10]\). It does not compare this cap times a
following conditional factor with a selected affine action,
and does not establish a new filling family.

