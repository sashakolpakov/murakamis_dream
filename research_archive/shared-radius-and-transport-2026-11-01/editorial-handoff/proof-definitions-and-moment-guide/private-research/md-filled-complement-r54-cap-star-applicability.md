# Applying the existing whole-star gap at the R54 singleton maximum

This note identifies the hypotheses of the existing cap/CROSS-star theorem on the original 54-circle example. The positive moment representation and the whole-star cancellation theorem are already available. The new deduction here is the exact applicability at the singleton capacity maximum, using the original rational flow and the two endpoint gaps. It does not prove that the resulting relative loss brings the source below the complete geometric action.

## 1. Existing results and their scope

The public [positive moment form](/private/tmp/murakamis_dream-publication/notes/research_flat_cap_positive_moment_form.md) gives the original protected cap weights as moments of a positive random variable. Its support is unbounded, and moments are finite only below the stated threshold. It is not a contraction or a comparison with hyperbolic volume.

The public [whole-star spectral gap](/private/tmp/murakamis_dream-publication/notes/research_cap_cross_shared_star_spectral_gap.md) is stronger than the earlier private fixed-spectrum moment argument. It treats a small complex disk around the cap spectrum \(+2\), with every neighboring CROSS spectrum on its full real fold and a thin fixed complex strip. It includes both parities and all remaining face phases.

In the notation of that theorem, the cap is
\[
 H_{\mathrm{cap}}(A,C;\sigma)
    =\sum_{j=0}^{\lfloor N/2\rfloor-1}
          (-1)^j b_j(\sigma)A^{d-j}C^j,\qquad d=N-1.    \tag{1}
\]
All other factors incident to \(A\) form the genuine central product \(P_N(A,Y)\). Its weighted rate is
\[
 \frac1N\log P_N(L_Ce^t,L_Y)\longrightarrow F(t).
\]
The substantive hypotheses are
\[
                  L_A=L_C,\qquad 0<F'(0)<\frac12.       \tag{2}
\]
Under these hypotheses the original extraction of \(A^d\) has a positive exponential loss relative to \(P_N(L_C,L_Y)\). The theorem does not say that its final shared Cauchy envelope is at most \(e^{N\Phi}\).

## 2. The literal R54 star and its derivative

For the original selected LEFT quartet
\[
                    (x,b,c,y)=(0,50,16,29),
\]
the protected vertices are \(50,29\), and the correct cap variables in (1) are
\[
                         A=L_{16},\qquad C=L_0.        \tag{3}
\]
The ordinary heavy cap face is \(16\), not \(0\).

The only other regions incident to face \(16\) are regions \(18\) and \(35\). Their original quartets are
\[
             (41,0,44,16),\qquad(29,41,16,44).
\]
They are both CROSS in the singleton source. The three spectator triangles containing face \(16\) are
\[
                 (41,0,16),\quad(41,16,44),\quad(29,44,16).
                                                        \tag{4}
\]
The fourth triangle in the product of the two regions does not contain \(16\), and is retained as a factor independent of \(A\).

Write \(Z=L_{41}\), \(W=L_{44}\). On the balanced face \(A=C=a>0\), direct differentiation of the original triangle rates gives
\[
 \nu=F'(0)
 =\frac1\pi\left[
   \arctan\frac{a}{\sqrt{a^2+2aZ}}
  +\arctan\frac{a}{\sqrt{aZ+aW+ZW}}
  +\arctan\sqrt{\frac aW}\right].                       \tag{5}
\]
All three terms are positive. If \(r=Z/a\), \(s=W/a\), condition \(\nu<1/2\) is equivalently
\[
 \frac1{\sqrt{(1+2r)(r+s+rs)}}+
 \frac1{\sqrt{(1+2r)s}}+
 \frac1{\sqrt{(r+s+rs)s}}<1.                            \tag{6}
\]
This follows by taking the cosine of the sum of the three acute angles; their sum is less than \(3\pi/2\), so its positive cosine is equivalent to a sum below \(\pi/2\).

Balancing only two arbitrarily chosen complete radii does not establish (6) or control the global action cost. The next argument selects the radii from the original constrained singleton maximum instead.

## 3. The rational witness forces an interior maximum

Use the spectator entropy \(E_T(u)\) from the [protected endpoint theorem](/private/tmp/md-filled-complement-protected-endpoint-geometric-gap.md). Its spectator demands at the two ordinary selected faces are
\[
                  \operatorname{load}(0)=1-u,\qquad
                  \operatorname{load}(16)=u,           \tag{7}
\]
and every other ordinary demand is one. Its spectator triangle rows all have mass \(1/2\).

The public exact certificate supplies a feasible flow with
\[
 u_{\mathrm w}=\frac{548219162717}{2\cdot10^{12}}
                  \in(0,1/2),\qquad
 E_T(u_{\mathrm w})>\Phi_T+\frac15.                    \tag{8}
\]
Every permitted spectator corner is strictly positive; the smallest certified corner load is
\[
                    \frac{29141577}{40000000000}>0.
\]
The two endpoint gaps give
\[
                         E_T(0)<\Phi_T,\qquad
                         E_T(1/2)<\Phi_T.              \tag{9}
\]
The compact joint polytope of \(u\) and spectator flows has a maximum. Equations (8)–(9) put every maximizing \(u_*\) in the strict interval \((0,1/2)\).

Every permitted spectator corner at a maximizer is positive. Otherwise move a short distance toward the strictly positive rational flow. A new zero corner contributes a positive term of order \(\epsilon\log(1/\epsilon)\). An old corner equal to \(1/2\) contributes a term of the same nonnegative sign when it leaves that endpoint. The derivatives at all other corners are finite. Consequently the total entropy increases, a contradiction. Singleton rows which are forced by the protected pair stay fixed and are excluded from this relative statement.

This argument uses the exact feasible rational flow, not a numerical optimizer or a claim that simple-sphere geometry automatically supplies a strict point for the modified singleton problem.

## 4. Common multipliers give the balance and degree condition

At the relative-interior maximum, finite-dimensional Lagrange multipliers exist for the original linear face and triangle constraints. Exponentiate the face multipliers to obtain shared positive curvatures \(L_f\), defined up to the usual harmless scale. Each spectator row is the maximizing triangle allocation for those weights.

Varying \(u\) in (7) gives the additional stationarity equation
\[
                         \log L_{16}-\log L_0=0.       \tag{10}
\]
Thus \(A=C\) is an exact equation at the maximum. The sum of the three triangle derivatives at face \(16\) is its same original load:
\[
                    F'(0)=\operatorname{load}(16)=u_*.
                                                        \tag{11}
\]
Equations (10)–(11) prove both hypotheses (2) nonnumerically. They also prove (6) for these exact maximizer weights. The certificate's connectivity check ensures uniqueness of the spectator multipliers up to scale, but uniqueness is not needed to apply the star theorem.

The original edge \(0\,16\) is a strand edge. Its triangle opposite the cap is \((41,0,16)\), which belongs to region \(18\). It supplies the supported \(A,C\) angular loss required by the public theorem. The remaining incident region is also CROSS, and its other original faces are retained. Thus all geometric-incidence and original-target hypotheses of that theorem have been checked.

For orientation only, the old locating computation has \(u_*\) approximately \(0.27411027\). This number is not used in (8)–(11) or in the applicability conclusion.

## 5. The missing absolute action budget

Let
\[
                  G_*=\max_{0\le u\le1/2}E_T(u).
\]
The exact certificate proves \(G_*>\Phi_T+1/5\). At the maximizing shared weights, the weighted envelope after extracting the cap's full \(A^d\) target is exactly \(G_*\), by triangle duality and \(A=C\).

Explicitly, write \(\mathcal T_{\mathrm{sp}}\) for all spectator triangles. The global Cauchy envelope is
\[
 \mathcal G(L)=
      \sum_{t\in\mathcal T_{\mathrm{sp}}}Q_t(L)
       +\log L_A-\sum_{f\ \mathrm{ordinary}}\log L_f .
                                                        \tag{12}
\]
The \(\log L_A\) term is the balanced cap rate and cancels the extracted \(A\)-target. At the maximizing flow and the common radii,
\[
                         \mathcal G(L)=G_*.            \tag{13}
\]
The existing star theorem gives some \(\eta(L)>0\), hence, after attaching the unchanged exterior at those same radii, a rate at most
\[
                              G_*-\eta(L).             \tag{14}
\]
To place this below the actual geometric action one needs
\[
                              \eta(L)>G_*-\Phi_T.       \tag{15}
\]
Neither positivity of \(\eta\), nor the scalar conditions (2), supplies (15). The existing proof chooses sufficiently small angular neighborhoods and analytic tubes to obtain a positive loss; it does not compare that loss with the excess in (8). Therefore the fixed-spectrum theorem and its stronger spectral-strip version apply rigorously to R54 but do not yet prove an absolute source or filled-period gap.

The global signed-circle representation theorems do not repair this step merely from the common multipliers. The published stationary classification explicitly leaves residual cap geometry and the global volume comparison separate. Here the dual flow has a cap in place of its original pair of positive triangle allocations; restoring the original triangles changes the two face demands. One cannot identify the scalar \(G_*\) with a volume of the original complete representation.

## 6. Relation to the endpoint theorem and existing coverage

The new protected-endpoint note contributes two original-target entropy bounds and their general-Morse smoothing adapter. It does not reprove the positive moment form or claim that the star theorem is new. The older star theorem controls coherent cancellation over interior degrees, but only relative to its specified weighted envelope. These statements address different parts of the problem.

Together they establish the exact applicability argument (8)–(11), and they isolate the additional quantitative inequality (15). No full-source bound, original invariant asymptotic, or actual filled-volume conclusion follows in this note.

