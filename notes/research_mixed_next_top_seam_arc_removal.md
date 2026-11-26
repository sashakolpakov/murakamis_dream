# Removing the upper seam arcs from the cyclic paired remainder

Research deduction, 8 November 2026. The complete selected-source
bound on the upper radial tube pays two fixed endpoint arcs of the
original upper Fourier period at height \(1/100\). Applying it to
the literal filtered meromorphic kernel leaves one full lower
complement and two shorter upper intervals. All signs and the
original factor \(N\) are retained.

This is a further reduction of the remaining signed boundary.
It does not bound the lower complement or the two upper middle
intervals, and it does not establish a whole next-transfer
asymptotic. No numerical evaluation or change to a frozen source
is used.

## 1. Keep the original cycles and the old filter

Use the exact notation and ordinary-next reference family of
[the cyclic horizontal reduction](research_mixed_next_paired_cyclic_horizontal_reduction.md).
In particular,
\[
 \begin{gathered}
 F_N^{\rm mid}=(I-\Pi_{\rm end})(F_{34,N}-R_N^a),\qquad
 Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\qquad \beta=0,1,\\
 K_N(y)=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}{1-Y^N},\\
 \Gamma_0=[0,1]+ih_*,\qquad \Gamma_1=[0,1]+iH,\qquad
 h_*=\Im y_*\in(-.102,-.001),\qquad H=1/100 .
 \end{gathered}                                                   \tag{1}
\]
The filter is the older \(11/12\) filter, with the fixed lower
cutoff from that source. The later \(8/9\) filter is not substituted.
All paths in this note have increasing real coordinate unless a
minus sign is displayed. They remain fixed when the outside
parameters vary.

Let \(J_*\subset\Gamma_0\) be the unchanged local geometric segment,
and let
\[
                   \gamma_1=[11/50,9/20]+iH.                     \tag{2}
\]
The exact cyclic theorem gives
\[
 \begin{split}
 \mathcal T_\beta[F_N^{\rm mid}]&=\int_{\Gamma_0}K_N\,dy
                                      -\int_{\Gamma_1}K_N\,dy,\\
 \mathscr R_N^{\rm cyc}
 &=\int_{\Gamma_0\setminus J_*}K_N\,dy
                         -\int_{\Gamma_1\setminus\gamma_1}K_N\,dy .
 \end{split}                                                     \tag{3}
\]
There are no vertical currents in (3): they have already canceled
exactly by period one, after the removable seam poles and every
added horizontal interval were retained. We make no further
contour deformation here.

## 2. The two upper endpoint arcs are paid

The theorem and Section 5 of
[the complete upper radial seam bound](research_mixed_next_upper_radial_seam.md)
apply to the full original selected density and to the specified
old filtered density
\[
 \mathscr D_{1,N}^{\rm mid}(w,Y,Z)
       =F_N^{\rm mid}(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).
                                                                  \tag{4}
\]
Here the subscript \(1\) specifies the selected Fourier coefficient,
not the next letter; both values of \(\beta\) are retained.
On a fixed tube about \(Y=e^{2\pi h}\), \(0\le h\le H\), every
fixed normalized mixed outside derivative of (4) is
\(O(e^{-N/1000})\), on smaller fixed complex complete-color and
actual-output neighborhoods.

Choose once and for all a sufficiently small
\[
                            0<s<11/100                           \tag{5}
\]
such that the closed arcs
\[
        \gamma_{\rm L}=[0,s]+iH,\qquad
        \gamma_{\rm R}=[1-s,1]+iH                                \tag{6}
\]
lie strictly inside that tube. Such a fixed \(s\) exists by the
last section of the radial theorem, or directly from
\[
 |e^{-2\pi i(x+iH)}-e^{2\pi H}|
       \le 2\pi e^{2\pi H}\operatorname{dist}(x,\mathbb Z)
\]
for these two endpoint ranges. It is chosen before \(N\);
it is not identified with either physical cutoff of the filter.
The choice in (5) also keeps both arcs disjoint from (2).

The exact kernel identity on the upper line is
\[
                    -K_N(y)=
             \frac{N\mathscr D_{1,N}^{\rm mid}(w,Y,Z)}
                                      {1-Y^{-N}}.                \tag{7}
\]
It has the minus sign of the upper boundary in (3).
Since \(|Y^{-N}|=e^{-2\pi NH}\),
\[
             |1-Y^{-N}|\ge1-e^{-2\pi NH}\ge\frac12               \tag{8}
\]
for every sufficiently large level. This bound is independent
of angle and of the outside parameters. In particular there
is no real-node pole on either arc at height \(H>0\).

Define their contribution with its actual orientation:
\[
 \mathscr S_N^{\rm top}
       =-\int_{\gamma_{\rm L}}K_N\,dy
        -\int_{\gamma_{\rm R}}K_N\,dy
       =N\int_{\gamma_{\rm L}\cup\gamma_{\rm R}}
                \frac{\mathscr D_{1,N}^{\rm mid}}{1-Y^{-N}}\,dy .
                                                                  \tag{9}
\]
Equations (7)--(8), the fixed arc lengths and the radial theorem
give
\[
 \partial_w^j\partial_z^k
       \left[e^{-N\mathcal P_\beta^+(w,z)}
                         \mathscr S_N^{\rm top}\right]
                      =O_{j,k}(e^{-N/2000}) .                    \tag{10}
\]
The harmless additional \(N\) in (9) is absorbed by the loss
from \(1/1000\) to \(1/2000\). Differentiation acts only on the
outside-parameter functions; both arcs and the denominator in
(7) remain fixed. Thus (10) retains the same normalized
holomorphic jets and both level parities as the source theorem.
No estimate for the unselected density is used in this step.

## 3. The shorter remaining signed chain

Put
\[
 \boxed{\quad
 \mathscr R_N^{\rm short}
   =\int_{\Gamma_0\setminus J_*}K_N\,dy
       -\int_{[s,\,11/50]+iH}K_N\,dy
       -\int_{[9/20,\,1-s]+iH}K_N\,dy .
 \quad}                                                          \tag{11}
\]
This retains the whole original lower complement. The two
remaining upper intervals have precisely the signs inherited
from the counterclockwise rectangle. Splitting the original
upper intervals, without any deformation or residue calculation,
gives the exact identity
\[
                 \mathscr R_N^{\rm cyc}
                      =\mathscr R_N^{\rm short}
                                      +\mathscr S_N^{\rm top}.    \tag{12}
\]

**Theorem.** On fixed small complex complete-color and actual-output
neighborhoods for both ordinary-next types, and at both parities,
\[
 \boxed{\quad
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
  \{\mathcal T_\beta[F_{34,N}]-I_{\rm geom,N}
                              -\mathscr R_N^{\rm short}\}\right]
              =O_{j,k}(e^{-N\Delta/64}),\qquad
                         \Delta=\frac{59}{440000}.
 \quad}                                                          \tag{13}
\]
Indeed the cyclic theorem, equation (16), gives the same
expression with \(\mathscr R_N^{\rm cyc}\) and loss \(\Delta/32\).
Substitute (12) and use (10). The two fixed positive losses
leave the stated conservative allowance \(\Delta/64\).

The geometric term in (13) is the original unwrapped local
integral, with nonzero leading term
\[
 I_{\rm geom,N}
   =N^{-2-\beta/2}A_\beta(w,z)e^{N\mathcal P_\beta^+(w,z)}
                              (1+O_{\rm hol}(N^{-1})),
                    \qquad A_\beta\ne0.                          \tag{14}
\]
No final Gram is inserted. The original next-row scalar
\(\kappa_N^{4+\beta}N^{1+\beta}P_k^{1-\beta}\), when restored,
is unchanged.

The remaining sufficient inequality is a bound for the signed
sum (11):
\[
 |\mathscr R_N^{\rm short}|
     \le C N^B
       e^{N\{\Re\mathcal P_\beta^+(w,z)-\epsilon\}}
                                                                  \tag{15}
\]
for some fixed \(\epsilon>0\), uniformly on the stated
neighborhoods, or directly with normalized fixed jets.
Separate suppression of its three displayed integrals is not
required. No part of (15) is asserted here.

The radial theorem also has terminal-output source estimates.
They are used here only on the ordinary reference family already
eligible for (3), the central selected-source estimate, and (14).
This deduction therefore makes no terminal-next or knot-family
promotion. The lower endpoint portions at the unchanged negative
height \(h_*\), as well as both upper middle intervals in (11),
remain explicit and unpaid; a tube above the real seam does not
contain those lower portions.

