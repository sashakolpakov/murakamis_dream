# The complete conditional asymptotic on the deepest incoming face

Research assembly, 8 November 2026. The original conditional finite
sum has its nonzero geometric asymptotic on the entire deepest
incoming face needed for the proposed displaced contour. The
physical rows near the numerator wall are retained in the contour
when its critical height is positive. Their individual real
moduli need not be bounded by the critical action.

The statement concerns this full parameter face and a fixed
complex neighborhood of it. It does not establish a complete
source theorem on the whole strip between this face and the
real incoming arc, or an asymptotic for the product with the cap.

## 1. Statement with the original normalization

Let
\[
\begin{gathered}
 a=x-\frac{9i}{125},\qquad \frac12\le x\le\frac7{10},\\
 y=z+iH,\qquad \frac{11}{50}\le z\le\frac9{20},\qquad
                         0\le H\le\frac1{100},\\
 r=e^{-2\pi i/N},\qquad X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},
 \qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j.
\end{gathered}                                                     \tag{1}
\]
Write \(\mathcal F\) for the compact parameter set in the first
two lines. Keep the entire literal finite polynomial
\[
                C_{1,N}(X,Y)=
           \sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
                                                               \tag{2}
\]
Its original phase and selected stationary value are
\[
\begin{split}
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 g'(q)&=\Log(1-e^{-2\pi iq}),\qquad
 Q_t(t_*;a,y)=0,\qquad \Theta(a,y)=Q(t_*;a,y).
\end{split}                                                       \tag{3}
\]
The logarithmic lifts and additive constant are those of the
original finite source. The
[negative-height branch theorem](research_mixed_conditional_negative_height_branch.md)
fixes the simple upper exponential root and proves
\[
                  \frac1{16}<\Re t_*<1-x,\qquad
                         -\Re Q_{tt}(t_*;a,y)>0.
                                                               \tag{4}
\]

**Theorem.** There is a fixed open complex neighborhood
\(\mathcal V\) of \(\mathcal F\) on which
\[
 \boxed{\quad
 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
     =N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                       \bigl(1+O_{\mathrm{hol}}(N^{-1})\bigr),
 \qquad \mathcal B(a,y)\ne0 .
 \quad}                                                         \tag{5}
\]
The relative error is uniform on a smaller fixed neighborhood,
as are all its fixed mixed parameter derivatives. The conclusion
holds along all integer levels, including both parities.
The leading coefficient is explicitly
\[
\begin{gathered}
 a_0(q)=\sqrt{2\sin\pi q}\,e^{-i\pi q/2},\\
 \mathcal B(a,y)=
 \frac{\sqrt{2\pi}\,a_0(a+t_*)a_0(y+t_*)}
 {a_0(t_*)^3a_0(a)a_0(y)\sqrt{-Q_{tt}(t_*;a,y)}} .
\end{gathered}                                                     \tag{6}
\]
The branches in (6) continue from the original regular strip.
The Gaussian square root has positive real part on the base
set. No additional peripheral factor or power of \(N\) has
been removed.

## 2. Why the two contour constructions cover the entire face

Put \(h_*=\Im t_*\) and \(\eta_0=9/125\). The
[deepest-face radius guard](research_mixed_conditional_deep_face_radius_guard.md)
proves on all of \(\mathcal F\) that
\[
                         h_*<\eta_0,
                                                               \tag{7}
\]
with a uniform positive margin. That proof uses the exact
critical equation, two elementary force comparisons and its
original imaginary logarithmic equation. It does not assume
a finite-source asymptotic.

Partition the compact base set into the two closed subsets
\[
     \mathcal F_-=\{(a,y)\in\mathcal F:h_*\le0\},\qquad
     \mathcal F_+=\{(a,y)\in\mathcal F:h_*\ge0\}.
                                                               \tag{8}
\]
On \(\mathcal F_-\), the
[wall-gap completion theorem](research_mixed_conditional_wall_gap_completion.md)
proves (5). Its boundary-phase argument puts the real wall
rate strictly below the actual critical action whenever
\(h_*\le0\). The physical wall rows, upper cut and all
connecting contours are then controlled in the original
prewall representation.

On \(\mathcal F_+\), (7) supplies precisely the hypothesis
\(0\le h_*<\eta_0\) of the
[half-cut source theorem](research_mixed_conditional_half_cut_below_incoming_zero.md).
That theorem also proves (5), but uses a different exact
partition of the same finite sum. It retains every row
below one half rather than ending the retained interval
before the numerator wall.

On its horizontal critical line, the incoming argument
\(a+t\) has strictly negative imaginary part. The proved
lower-half-plane factorial expansion therefore applies
even where its real part crosses one. The real phase
decreases beyond the wall, so the main contour has just
the original nondegenerate maximum. At the half cut, the
unweighted vertical connector decreases from its already
controlled real endpoint.

The finite contour remainders use the exact period factor
\[
                  \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).
                                                               \tag{9}
\]
Both terms are retained. The estimates include the real
zero of this factor, every weighted vertical side and both
horizontal Fourier remainders. The interpolation remains
the original holomorphic numerator factorial. Artificial
poles of a separately shifted chart are canceled in the
exact identity before a contour is moved.

Thus both parts of (8) have complete-source proofs. Both
include the original density \(+N\), the same selected
critical branch and the same nonzero symbol (6). At
\(h_*=0\) their conclusions agree for the same finite
polynomial. Their open complex neighborhoods cover the
compact set \(\mathcal F\). Taking a smaller neighborhood
and common constants gives (5) uniformly. Cauchy's formula
gives the stated derivative conclusions. This proves the
theorem.

## 3. The lower bound and the remaining composition problem

Because \(\mathcal B\) is continuous and nonzero on the
compact base set, (5) gives, for all sufficiently large
\(N\), the explicit form of lower estimate
\[
 |C_{1,N}(X,Y)|
       \ge \frac{|\mathcal B(a,y)|}{2N}
                                e^{N\Re\Theta(a,y)}.
                                                               \tag{10}
\]
This is a lower bound for the whole conditional sum.
It is obtained from its surviving nonzero stationary
coefficient after all other parts of the original cycle
have been bounded. It does not require positivity of
the original complex summands.

In particular, a failure to pay every real wall row by
one constant action floor is no longer an obstruction to
this face theorem. Such rows belong to the retained cycle
in the positive-height construction.

The next composition still needs the corresponding complete
cap estimate and control of the connecting incoming paths,
with the original outside weights and geometric action.
The theorem on the real incoming arc and (5) on the deepest
face do not by themselves prove a relative asymptotic at
every intermediate height: holomorphy alone cannot provide
the missing uniform estimates there. No new knot-family
or finite-exceptions theorem is inferred from (5).
