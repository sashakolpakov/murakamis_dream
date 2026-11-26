# A complete-current criterion for the original first-cap polynomial

Research deduction, 5 November 2026. The endpoint coefficient packet is
now available on a rectangle large enough to contain one candidate outer
cap contour. This note proves the local curvature and reduces a full cap
packet to explicit real-tail, cut, and horizontal-alias inequalities.
The horizontal alias inequalities are certified below; the real-cut
and real-tail inputs remain separate. No frozen source theorem is
changed, and no type-three gap is imported into the type-four source.

## 1. The literal source and its retained interpolation

Use the original notation from
[the exact open-word source](research_mixed_conditional_torus_composition.md):
\(q=e^{\pi i/N}\), \(r=q^{-2}\), \(P_i=(r;r)_i\), and
\(p_i(X)=(rX;r)_i\). The whole ordinary-color cap polynomial is
\[
 U_{\epsilon,N}(w,X)
 =\sum_{i=0}^{N-1}\frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\epsilon}},
 \qquad \epsilon\in\{0,1\}.                              \tag{1}
\]
It has degree less than \(N\). At a physical private index
\(e=i/N\), the specified complete-end continuation satisfies
\(H_N(w,r^{-i})=P_iD_N(e)^{-1}\mathcal C_N(e,w)\). Consequently
\[
 U_{\epsilon,N}(w,X)
 =\sum_{i=0}^{N-1}D_N(i/N)^{-1}\mathcal C_N(i/N,w)
                         \frac{p_i(X)}{P_i^\epsilon}.     \tag{2}
\]
This exact identity retains every original private row and the whole
Newton boundary polynomial. In particular the additional type-four
factor is \(1/P_i\) in the summed index, not in the outgoing index.

Put \(X=e^{-2\pi iz}\), and let
\[
 \mathcal R=[.27,.49]+i[-.055,.04].                       \tag{3}
\]
The [endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md)
supplies the complete ordinary-color packet for
\(\mathcal C_N(e,w)\) on a fixed neighborhood of this whole rectangle.
The exact retained-row interpolation is
\[
 A_{\epsilon,N}(e,z,w)=D_N(e)^{-1}\mathcal C_N(e,w)
 \frac{\widehat P_N(N(e+z))}
      {\widehat P_N(Nz)\widehat P_N(Ne)^\epsilon}.         \tag{4}
\]
At every retained integer row, (4) is precisely the summand in (2).
It is not a new interpolation of the cap's outgoing values. Every
factor uses its previously specified canonical factorial.

## 2. The actual outgoing domains and reduced phase

The [exact endpoint-image extraction](research_mixed_open_word_endpoint_rectangles.md)
gives the attached rectangles
\[
\begin{split}
 T_3&=(.278,.391)+i(-.072,.021),\\
 T_4&=(.246,.350)+i(-.108,-.020).                          \tag{5}
\end{split}
\]
The correlated outgoing sets needed here are the images of the four
certified endpoint maps, with the two one-vertex outgoing points added.
Denote these compact sets by \(K_3,K_4\); they are strictly inside (5).
For each outgoing value, its original private root \(e_*(z)\) and
auxiliary root \(u_c(e_*)\) are supplied by
[open-word localization](research_mixed_open_word_critical_localization.md).
They are not independent corner choices from (5).

Write \(S(e,w)\) and \(\mathcal A(e,w)\) for the actual endpoint
action and coefficient. At the complete color, with the original
normalized sine primitive and \(g(e)=J(e)+i\pi(e-e^2)/2\), define
\[
 \Psi_\epsilon(e,z)
 =S(e)+J(e+z)-J(z)-i\pi ez-\epsilon g(e),\qquad
 M_\epsilon(z)=\Re\Psi_\epsilon(e_*(z),z).                \tag{6}
\]
The phase for nearby ordinary colors replaces only \(S(e)\) by
\(S(e,w)\). All arguments in (4) are regular: for \(e\in\mathcal R\)
and either attached rectangle, \(.516<\Re(e+z)<.881\).

The symbol of (4) is
\[
 N^{-(3+\epsilon)/2}\mathcal A(e,w)
 \sqrt{\frac{\sin\pi(e+z)}{\sin\pi z}}
 (2\sin\pi e)^{-\epsilon/2}e^{i\epsilon\pi e/2}
 e^{N\Psi_\epsilon(e,z,w)}(1+O(N^{-1})).                  \tag{7}
\]
Indeed the order-one phase of the marked factorial ratio cancels
the order-one phase in \(D_N^{-1}\); the displayed remaining phase
is contributed by the own factorial. The original branches of all
square roots are retained.

## 3. Curvature and the lower real half

**Lemma 1.** Uniformly on (3) and compact subsets of either attached
rectangle, \(-\Re\Psi_{\epsilon,ee}>0\). In particular the horizontal
line through \(e_*(z)\) has its unique maximum there, and vertical
restrictions of \(\Re\Psi_\epsilon\) are strictly convex.

To prove this, use the original endpoint phase
\(F(e,u)=B(e,u)+i\pi eu\). Its negative real Hessian is
\(a\,du^2+b\,(de-du)^2\), with \(a,b>0\) whenever
\(0<\Re u<1/2\) and \(0<\Re(e-u)<1/2\). The full endpoint packet
certifies these inequalities for \(u=u_c(e)\) throughout (3).
For \(v=(1,u_c'(e))\), the second component of \(F''v\) is zero.
Thus
\[
 -\Re S''(e)=\Re[v^*(-F'')v]>0.                          \tag{8}
\]
Adding \(J(e+z)-\epsilon g(e)-i\pi ez\) preserves strictness:
\(\Re\cot\pi(e+z)<0\), while \(\Re\cot\pi e>0\).
Compactness supplies one positive lower curvature constant. The root
and its Gaussian branch are holomorphic near the correlated compact
outgoing image, by the original implicit equations and uniqueness.

There is an additional type-four real-tail reduction. For
\(z=x+ih\), set
\[
 I_h(s,x)=\Re[g(x+s-i|h|)-g(x-i|h|)]+2\pi h_+s,
 \qquad R_\epsilon(s,z)=\Re S(s)+I_h(s,x)-\epsilon J(s).
                                                               \tag{9}
\]
This is the original full-row upper rate after using the endpoint
packet, wherever that packet is uniform in the real index \(s\).
The periodic lower-half primitive in \(I_h\) retains the revived
Pochhammer rows with \(s+x>1\).

**Lemma 2.** \(R_1(s,z)\) is strictly concave for \(0<s<1/2\).
The real-index endpoint theorem gives \(0<\Re u_c(s)<s<1/2\);
the same Schur argument proves \(\Re S''(s)<0\). If \(s+x<1/2\),
\[
 \Re\cot\pi(s+x-i|h|)\le\cot\pi(s+x)<\cot\pi s.
                                                               \tag{10}
\]
If \(s+x\ge1/2\), the shifted real cotangent is nonpositive,
whereas \(\cot\pi s>0\). Hence
\(R_1''=\Re S''+\pi\Re\cot\pi(s+x-i|h|)-\pi\cot\pi s<0\).

In particular, if both real cuts in (3) are strictly below the
selected cap rate, all lower-half real tails are controlled by those
cuts at the level of (9). Indeed \(\Re e_*\) is between the cuts,
and vertical convexity gives
\(R_1(\Re e_*,z)\ge M_1(z)\). Strict concavity then forces the
left tail to increase toward its cut and the right tail to decrease
away from its cut. This assertion does not supply a finite-source
bound uniform at \(s=0\); that endpoint still needs its actual
uniform product estimate. No analogous type-three lower-half
concavity is inferred from this argument.

## 4. The remaining complete-contour tests

Let \(a=.27\), \(b=.49\), \(H_-=.055\), \(H_+=.04\). The
following are sufficient, uniformly on the correlated outgoing sets:

1. Every original row outside \([a,b]\), including rows revived off
   the outgoing physical grid, has an aggregate polynomial-times-
   \(e^{N(M_\epsilon-\delta)}\) upper bound for some \(\delta>0\).
2. The two real cut values satisfy
   \(\Re\Psi_\epsilon(c,z)<M_\epsilon(z)-\delta\), \(c=a,b\).
3. The two whole horizontal alias segments satisfy
\[
 \Re\Psi_\epsilon(x+iH_+,z)-2\pi H_+
       <M_\epsilon(z)-\delta,\qquad
 \Re\Psi_\epsilon(x-iH_-,z)-2\pi H_-
       <M_\epsilon(z)-\delta
 \quad(a\le x\le b).                                    \tag{11}
\]

These are complete-current conditions. Apply the exact cotangent
residue formula to (4), with half-grid cuts tending to \(a,b\).
The constant mode has coefficient \(+N\). Its horizontal integral
can be moved to \(\Im e_*\); Lemma 1 gives the unique maximum and
a fixed gap at both of its cut endpoints. Vertical convexity and
the real cut gaps control both joins. The alias rate on each half
vertical side is convex in height, so its maximum is at its real
or horizontal endpoint. Thus the real cut inequalities and (11)
also control every alias side. No residue, vertical current, or
wrapped mode has been silently removed.

If all three conditions hold, the entire polynomial (1) has the
nonzero local packet obtained from (7) by the outer Gaussian:
its power is \(N^{-1-\epsilon/2}\), and its coefficient is the
coefficient in (7) at \(e_*\), multiplied by
\(\sqrt{2\pi}/\sqrt{-\Psi_{\epsilon,ee}(e_*,z)}\).
For fixed ordinary-color derivative order \(k\) at the complete color,
the leading power is multiplied by \(N^k\): the critical envelope
derivative is \(\partial_w\Psi_*=-\tan(\pi u_c(e_*))/(4\pi)\),
by the original full-index packet. It is nonzero since
\(0<\Re u_c<1/2\). This assertion does not give a nonzero top
coefficient for arbitrary outgoing-index derivatives.
The same zero-safe ordinary-color perturbation preserves the strict
tail/current gaps on a smaller fixed joint neighborhood.

In the exact open torus contraction this remains the original
\(U_{\epsilon,N}\); its original factor
\(\{d_N(X)(1+X^{-N})\}^{\epsilon}\) is unchanged. The criterion
does not replace it by a fractional power or estimate the remaining
outer integral. It makes no open-word noncancellation claim until
its hypotheses, and the remaining whole-word contour, are proved.

There is a legitimate small-dimensional reduction for the cut and alias
tests. For either endpoint type and either external type, write the
already proved holomorphic endpoint map as
\((e(b),t(b),u(b))\), with external \(b\) in its complete typed disk.
For any fixed contour point \(c\),
\[
 D_c(b)=\Psi_\epsilon(c,t(b))-
                \Psi_\epsilon(e(b),t(b))                 \tag{11a}
\]
is holomorphic on a neighborhood of that entire disk. Its real maximum
is therefore attained on the boundary circle. This principle is used
only after the independent full-disk root existence theorem. Thus each
cut test has one real circle parameter, and each whole horizontal-alias
test has two real parameters: that circle parameter and its real contour
coordinate. The separate one-vertex cases remain compulsory.

For a future outward check, its exact external derivative is
\[
 D_c'(b)=
 [\Psi_{\epsilon,z}(c,t)-\Psi_{\epsilon,z}(e,t)]\,t'(b),
 \quad
 \Psi_{\epsilon,z}(e,z)=J'(e+z)-J'(z)-i\pi e.             \tag{11b}
\]
The derivative of the critical private coordinate drops out because
\(\Psi_{\epsilon,e}(e,t)=0\). The response \(t'(b)\) is given by
the original three-variable endpoint Jacobian, not a differentiated
floating root. These reductions specify a finite universal family;
they do not certify its sign or remove the distinct full real-row tails.

**Lemma 3 (both complete horizontal aliases).** For both types, the
inequalities (11) hold with upper and lower gaps greater than
\(3/20\) and \(6/25\), respectively, throughout the actual correlated
outgoing image, including the separate one-vertex points.

Write \(\Psi_{ee}=-A+iB\), where \(A>0\) by Lemma 1. The explicit
curvature certificate proves
\[
 K=A+\frac{B^2}{A}<24
       \quad\hbox{on }\mathcal R\times\overline T_{3+\epsilon}.
                                                               \tag{11c}
\]
This is a legitimate distinguished-boundary reduction. The function
\((A,B)\mapsto A+B^2/A\) is convex on \(A>0\): its Hessian is
\(2A^{-3}\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix}\), which is
positive semidefinite. The two components of the holomorphic function
\(-\Psi_{ee}\) are harmonic in either complex variable separately.
Consequently \(K\) is separately subharmonic. The maximum principle
reduces (11c) to the product of the two rectangle boundaries, after
global holomorphy and \(A>0\) have already been proved. There are
sixteen edge products per type, each with two real parameters.

No root is proposed in this check. With \(u=u_c(e)\), it uses
\[
 a=\pi(2\tan\pi u+3\cot\pi u),\quad b=\pi\cot\pi(e-u),
 \quad
 S''=-b+\frac{(b+i\pi)^2}{a+b},\qquad
 \Psi_{ee}=S''+\pi\cot\pi(e+z)-\epsilon\pi\cot\pi e
                                      +i\epsilon\pi.     \tag{11d}
\]
Every exact dyadic cell encloses these explicit functions and checks
\(A>0\), \(K<24\) outward. The complete cover has 32 products,
8,341 accepted cells, and 16,650 nodes. Saved mode checks the entire
same trees without proposing roots or refining failed cells.

For the real Hessian of \(\Re\Psi\), complete the square:
\[
 d^2\Re\Psi=-A\left(dx+\frac BA\,dy\right)^2+K\,dy^2
                                                        <24\,dy^2.
                                                               \tag{11e}
\]
Integrate along the straight segment from its original critical point
to any point of the convex outer rectangle. The critical gradient is
zero, hence
\[
 \Re\Psi(x+iy,z)-M_\epsilon(z)
                         \le12(y-\Im e_*)^2.             \tag{11f}
\]
The exact endpoint-image record gives \(-.051<\Im e_*<.037\)
for all four maps and both one-vertex points. Thus the upper alias
loses at least
\(2\pi(.04)-12(.091)^2>3/20\), and the lower loses at least
\(2\pi(.055)-12(.092)^2>6/25\). These two scalar margins are also
checked outward. This proves Lemma 3. It does not replace the remaining
real-cut or full-row tail inputs.

## 5. A genuinely inadequate smaller rectangle

The [saved fixed comparison](../repro/diagnostics/2026-11-05-type-four-cap-cut-obstruction/README.md)
uses the already certified actual one-vertex type-four root, with
outgoing coordinate equal to its private coordinate. It proves
\[
 \Re\Psi_1(.33,z)-\Re\Psi_1(e_*(z),z)>13/1000.            \tag{12}
\]
Thus the previously proved private rectangle starting at \(.33\)
cannot supply a real cut for this simple cap argument. This is only
a cutoff obstruction; coherent cancellation can still control those
rows. The larger endpoint packet (3) repairs the source-domain issue,
but does not by itself prove the three remaining tests above.

## 6. Reproduction of the alias bound

```sh
python3 experiments/certify_mixed_cap_outer_alias_curvature.py --precision 256
python3 experiments/certify_mixed_cap_outer_alias_curvature.py --precision 320 --input repro/results/research-mixed-cap-outer-alias-curvature.json --output repro/results/research-mixed-cap-outer-alias-curvature-replay.json
```

The author and saved replay bind the complete endpoint packet, exact
critical image extraction, and all inherited records. This certificate
evaluates only the explicit curvature (11d), not a sampled cap sum or
an approximation of an arbitrary open word.
