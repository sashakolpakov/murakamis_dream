# The first half of the original ordinary three/four contour

Research assembly, 7 November 2026. The seam collar, the real
small-angle interval, the left taper, the geometric plateau and
the right extension now form one continuous contour segment.
Its contribution has the original nonzero geometric asymptotic.
The complementary segment of the exact contour remains to be
estimated. No numerical evaluation is used.

## 1. A decomposition of the exact observation

Retain the source and notation of
[the ordinary pair theorem](research_mixed_three_four_ordinary_pair_target.md).
At complete ordinary colors, write
\[
 F_N(a)=U_{0,N}(-2,e^{-2\pi ia})V_{1,N}(-2,e^{-2\pi ia}),
 \qquad a_*=A+ic,\qquad
 \mathcal S=T_0(a_*)+P_1(a_*),\qquad M=\Re\mathcal S .
                                                               \tag{1}
\]
The exact finite functions make \(F_N\) an entire one-periodic
function of \(a\). Its Fourier band is contained in
\([-(N-1),N-1]\). Consequently the original observation is
\[
 Z_{34,N}(-2,-2)=\kappa_N^3N^2\int_0^1F_N(a)\,da,
                          \qquad |\kappa_N|=1.           \tag{2}
\]
This orientation agrees with the original positive-circle
constant coefficient: the substitution \(X=e^{-2\pi ia}\)
reverses the circle orientation and gives \(dX/(2\pi iX)=-da\).
Both signs cancel.

Define the first contour segment by
\[
 a_-(x)=
 \begin{cases}
 x,&0\le x\le1/10,\\
 x+ic(x-1/10)/(3/25),&1/10\le x\le11/50,\\
 x+ic,&11/50\le x\le1/2.
 \end{cases}                                                   \tag{3}
\]
It starts at zero, passes through the original plateau, and
ends at \(1/2+ic\). Set
\[
 I_{-,N}=\kappa_N^3N^2
                  \int_{a_-}F_N(a)\,da.                \tag{4}
\]
For definiteness choose the complementary segment
\[
 a_+(x)=x+2ic(1-x),\qquad1/2\le x\le1,
 \qquad I_{+,N}=\kappa_N^3N^2\int_{a_+}F_N(a)\,da .
                                                               \tag{5}
\]
The combined path has the same endpoints as the real interval.
Holomorphy gives the exact identity
\[
                         Z_{34,N}=I_{-,N}+I_{+,N}.       \tag{6}
\]
No sampling approximation, new scalar, or replacement of the
ordinary closing is involved. Other complementary paths with
the same endpoints give the same \(I_{+,N}\).

## 2. The proved first-half asymptotic

Let \(b_U,b_V\) be the original nonvanishing leading symbols
of the two local factors, and let
\[
 H=-(T_0+P_1)''(a_*),\qquad
 \mathcal A=
       \frac{\sqrt{2\pi}\,b_U(a_*)b_V(a_*)}{\sqrt H}\ne0 .
                                                               \tag{7}
\]
The square root is the original accretive Gaussian branch;
its orientation and normalization are those of equation (10)
in the ordinary pair note.

**Proposition 1.** Along every integer level, with both parity
cases retained,
\[
 I_{-,N}
   =\kappa_N^3N^{-3/2}\mathcal A e^{N\mathcal S}
                                      (1+O(N^{-1})).
                                                               \tag{8}
\]

*Proof.* Choose the fixed \(\rho\in(0,1/10)\) from the
original seam theorem, reducing it if necessary. The following
complete-source results apply to the exact segments of (3).

| Segment | Proved estimate |
|---|---|
| \(0\le x\le\rho\), height zero | [two-vertex seam collar](research_mixed_two_vertex_first_collar.md), gap \(1/20\) |
| \(\rho\le x\le1/10\), height zero | [real small-angle theorem](research_mixed_three_four_real_small_angle_source.md), gap \(1/320000\) |
| \(1/10\le x\le11/50\), taper in (3) | [complete left-taper theorem](research_mixed_three_four_left_taper_source_completion.md), gap \(1/160000\) |
| \(11/50\le x\le9/20\), height \(c\) | [original plateau asymptotic](research_mixed_full_unselected_plateau.md), with coefficient (7) |
| \(9/20\le x\le1/2\), height \(c\) | [right-strip theorem](research_mixed_three_four_moving_transform_cut.md), a fixed positive gap |

Each discarded segment bounds the complete product, including
its finite-index endpoints, contour joins and sampling
corrections. Their ordinary-color disks may be intersected,
although (8) only needs the complete colors.
The Jacobian of (3) is bounded on each segment. Thus their
combined contribution is
\[
 O\bigl(N^B e^{N(M-\gamma)}\bigr)
                                                               \tag{9}
\]
for a fixed \(\gamma>0\). The external \(N^2\) is included
in the polynomial prefactor in (9).

The plateau contributes (8), by the original one-dimensional
Gaussian theorem with the two local symbols \(N^{-1}b_U\)
and \(N^{-2}b_V\). The power is
\(N^2N^{-1}N^{-2}N^{-1/2}=N^{-3/2}\).
After division by its nonzero leading term, (9) is
exponentially small and can be absorbed in the relative
\(O(N^{-1})\) error. This proves (8). \(\square\)

## 3. The precise remaining obligation

Equations (6)--(8) locate the cancellation problem in one exact
complementary integral. For example, the estimate
\[
             I_{+,N}=o\!\left(N^{-3/2}e^{NM}\right)      \tag{10}
\]
would extend its leading asymptotic to the whole original observation
with relative error \(o(1)\). A bound
\(O(N^B e^{N(M-\eta)})\) with \(\eta>0\) would imply (10)
and retain the relative \(O(N^{-1})\) error in (8).
Neither estimate is asserted here.

A weaker argument could also suffice for the volume limit:
it would have to control the full sum in (6) from above and
show that its two contributions do not cancel at the geometric
exponential scale. Nonvanishing of \(\mathcal A\) alone
does not prove that statement.

The separate physical-root estimate for \(b/N\ge5/6\)
cannot simply be substituted for part of \(I_{+,N}\).
A partial root sum and an open contour segment have different
boundary and sampling terms. The same restriction applies to
the conditional half-face comparisons developed for the
middle physical sector.

Thus (8) establishes a complete part of the prescribed ordinary
observation, rather than a different Fourier closing. The
whole-pair theorem, its required full real boundary-color
estimates, and stability under arbitrary fixed short partial
fillings remain open. The finite-exceptions goal is unchanged.
