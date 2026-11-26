# The complete next-three transfer at its actual geometric references

Private research assembly, 9 November 2026. The exact Fourier
coefficients and the outgoing transition estimates bound the full
right physical contribution. The previously established transfer
decomposition then gives the original nonzero geometric asymptotic
for the whole conditional transfer at complete incoming color.
The result retains its specified reference family; it is not a
closing theorem for a knot or a two-boundary composition theorem.

## 1. Original transfer and reference

Fix an actual complete word in powers three and four beginning
\(343\), of length at least five. Let \(z_*\) be its original third
outgoing coordinate, and set
\[
 Z_*=e^{-2\pi iz_*},\qquad
 P_*=\mathcal P_0^+(-2,z_*),\qquad \Lambda=\Re P_*.
 \tag{1}
\]
Keep the complete prefix \(F_{34,N}(w,Y)\), the forced polynomial
\(d_N\), and the next conditional kernel
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa_N=q^{D^2/2},\quad M=\lceil N/2\rceil,\quad U=D-M,\\
 P_b=(r;r)_b,\qquad d_N(r^b)=P_b^{-1},\\
 C_{0,N}(Y,Z)=
   \sum_{j=0}^{D}\frac{Y^{-j}(rY;r)_j(rZ;r)_j}{(r;r)_j^2}.
 \end{gathered}
 \tag{2}
\]
The actual two-sector transfer is
\[
 \begin{split}
 \mathcal T_N(w,Z)
 &=N[Y^0](F_{34,N}(w,Y)d_N(Y)C_{0,N}(Y,Z))\\
 &\quad+N[Y^N](F_{34,N}(w,Y)d_N(Y)C_{0,N}(Y,Z))\\
 &=\sum_{b=0}^{D}\frac{F_{34,N}(w,r^b)}{P_b}
                                  C_{0,N}(r^b,Z).
 \end{split}
 \tag{3}
\]
All equalities and normalizations are those of the original
conditional attachment. Both Fourier sectors are included.

## 2. Statement

**Theorem.** At the references (1), for all sufficiently large
levels of both parities, the complete transfer satisfies
\[
 \boxed{\quad
 \mathcal T_N(-2,Z_*)
   =N^{-2}\mathcal A_0(-2,z_*)e^{NP_*}
                    (1+O(N^{-1})),
 \qquad \mathcal A_0(-2,z_*)\ne0.
 \quad}
 \tag{4}
\]
The action and coefficient are exactly those of the original local
geometric integral. The assertions have the same uniform reference
scope as the source estimates used below. In particular,
\[
        \lim_{N\to\infty}\frac1N\log|\mathcal T_N(-2,Z_*)|
                   =\Lambda
 \tag{5}
\]
for every reference in the stated family.

This is a theorem at complete incoming color \(w=-2\). Length-four
words, a terminal third vertex, and a next vertex of type four are
outside the reference hypotheses.

## 3. The whole right physical sum

Write \(C_{b,N}(Z)=C_{0,N}(r^b,Z)\), and retain the exact radical
functional and outgoing polynomial
\[
 \begin{split}
 \mathcal L_N(F)&=\phi_N[R_N^3e_M Q_N^{\rm full}F],\\
 F_N^+(X,Z)&=
       \sum_{b=M}^{D}(-q)^b C_{b,N}(Z)\frac{e_b(X)}{e_M(X)}
       =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2),\\
 \mathcal O_{N,k}&=\mathcal L_N(T_k(-\,\cdot/2)),\\
 \mathcal R_N^+(-2,Z)&=
       \frac1{\kappa_N^2N}\mathcal L_N(F_N^+(\cdot,Z))
       =\frac1{\kappa_N^2N}\sum_{k=0}^{U}f_{k,N}(Z)\mathcal O_{N,k}.
 \end{split}
 \tag{6}
\]
The quotient \(e_b/e_M\) is an ordinary polynomial, including at
the zeros of \(e_M\). The kernel \(Q_N^{\rm full}\) and the
functional \(\phi_N\) retain the entire original Hermite trace.
Equation (33) of
[the action-weighted source theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md)
identifies \(\mathcal R_N^+\) with the original physical sum over
all \(M\le b\le D\), including the final terminating row.

Let \(\mathcal D(t,Z_*)\) be the exact positive-transition upper
rate, and let \(\Gamma(\delta)\) be the real action in the whole
outer Fourier theorem. The
[endpoint-dominance theorem](research_mixed_next_positive_transition_endpoint_dominance.md)
and the
[physical half-input anchor](research_mixed_next_physical_half_input_action_anchor.md)
give
\[
 \mathcal D(t,Z_*)+\Gamma(1/2-t)
       \le E_0(Z_*)+\Gamma(1/2)
       \le\Lambda-g_0,\qquad
 g_0=\frac1{2\cdot10^{13}},\quad 0\le t\le1/2.
 \tag{7}
\]
All rates in this inequality have their original calibrated constants.

Split (6) at \(k=\lceil15N/32\rceil\). Below this index,
\(\delta=1/2-k/N>1/32\), so the whole Fourier asymptotic gives
\[
 |\mathcal O_{N,k}|\le C N^{-1}e^{N\Gamma(1/2-k/N)}.
 \tag{8}
\]
The positive-transition theorem gives
\[
 |f_{k,N}(Z_*)|\le CN^A e^{N\mathcal D(k/N,Z_*)}.
 \tag{9}
\]
Equations (7)--(9) bound the absolute sum over these modes,
including the original factor \(1/N\) in (6), by
\(CN^B e^{N(\Lambda-g_0)}\). The at most \(N\) frequencies
contribute only a polynomial factor.

For all \(k\ge\lceil15N/32\rceil\), the
[terminal-mode theorem](research_mixed_next_combined_action_terminal_mode_payment.md)
already bounds the whole attached block, with the same original
coefficients and scalar, by \(C e^{N(\Lambda-1/1000)}\).
No relative Fourier asymptotic near \(\delta=0\) is needed.
Absorbing the fixed polynomial factors in the first block proves
\[
             |\mathcal R_N^+(-2,Z_*)|
                 \le C e^{N(\Lambda-g_0/2)}.
 \tag{10}
\]
Every original outgoing row and every Fourier mode is included.
No positivity of a signed coefficient or of the whole observation
has been assumed.

## 4. Return to the complete transfer

Equation (32) of the action-weighted source theorem retains the exact
local geometric integral and the complete remainder:
\[
 \mathcal T_N(-2,Z_*)
     =I_{{\rm geom},N}+\mathcal R_N^+(-2,Z_*)
                     +O(e^{N(\Lambda-\epsilon_0)}),
 \qquad \epsilon_0>0.
 \tag{11}
\]
Its proof includes both original Fourier sectors, the transformed
cutoff forcing, the restored high physical band, and every previously
estimated contour contribution. No asymptotic error of the local
integral is assigned an exponential gap.

The
[local finite-source theorem](research_mixed_three_four_next_local_source.md),
with \(\beta=0\), gives for that integral
\[
 I_{{\rm geom},N}
    =N^{-2}\mathcal A_0(-2,z_*)e^{NP_*}(1+O(N^{-1})).
 \tag{12}
\]
Its coefficient is nonzero with the original determinant branch.
Equations (10)--(12) leave an additional relative error
\(O(N^2e^{-N\min(\epsilon_0,g_0/2)})\), which is absorbed
in the relative \(O(N^{-1})\) error in (12). This proves
(4), and then (5).

## 5. Scope of the result

The whole conditional transfer now has the leading term previously
proved only for its local geometric integral. Its outgoing coordinate
is still open: obtaining an ordinary knot invariant requires the
original right-boundary observation and estimates for its complete
closing contour. Composition also requires the appropriate uniform
boundary estimates. Neither follows by substituting (4) into an
uncontrolled boundary sum.

In particular, this theorem does not assert the volume identity for
every chain beginning \(343\), for all short-twist assignments, or for
all but finitely many assignments of an arbitrary tangle template.

## Source versions

- Exact full transfer and attached polynomial:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Complete Fourier observation:
  8c0f4853c05443eb76d821bca6d7248f6c00e19177a796e530e4b4cd24d93ac6.
- Positive transition with all outgoing rows:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Physical half-input action anchor:
  3ba93da54e86226990fe844cd245b8a973650ca84c0ca0088e9cdc579594d967.
- Endpoint dominance and the full finite attachment:
  85d5c740d1c8c3481f5d6be5dd29d826879a366f5d07a079700cb4cbd7c92804.
- Terminal attached block:
  7a0a060b8313d250d7b0e49d181f5242f4a47b0a3d56d19d542f60497f323587.
- Original nonzero local source:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.

No mathematical numerical evaluation is used in this assembly.
