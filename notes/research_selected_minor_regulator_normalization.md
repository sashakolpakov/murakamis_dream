# Regulator normalization of the source-selected action

Private written proof, 18 November 2026.

The actual canonical minor has a preferred peripheral action by [L].
This note fixes its regulator normalization at its own Alexander
attachment. The normalization is not borrowed from an unspecified
classical saddle or from an averaged quantum cut. The classical
regulator identities themselves are already established in [Q, C].

## 1. Source, peripheral marking, and continuation scope

Use the actual selected minor of [L], in its stated simple two-branch
node scope. Write
\[
 Y=\alpha+z,
 \qquad M=-\sqrt Y,
 \qquad \ell=e^{Y S_g'(Y)},
 \qquad S_g(\alpha)=0,
 \qquad \ell(\alpha)=1.
 \tag{1}
\]
Here \(\alpha\ne0,1\) is the simple Alexander root, and \(\ell\)
is the preferred longitude eigenvalue on the retained \(M\)-eigenline.
The writhe correction and the inverse eigenline used during vector
transport are already included in [L]. They are not changed below.

Choose a logarithm \(u=\log M\) near this attachment, and the unique
local longitude logarithm \(v=\log\ell\) with \(v(\alpha)=0\).
The exact selected-action identity of [L] is
\[
                            dS_g=2v\,du.
\tag{2}
\]
The selected classical representation and its crossing coordinates
are the ones obtained from the same source in [L]. In particular its
analytic occupations and transfers tend to zero as \(z\to0\).

A continuation below means continuation of this same representation,
ordered peripheral eigenline, and logarithmic germ. On its logarithmic
cover, continue \(S_g\) by (2) from the value in (1). Whenever the
canonical minor itself continues with this action, this is its action
continuation by uniqueness on overlaps. The present note does not
assert existence of a quantum-minor continuation to every point of
the algebraic component.

Let \(\beta\) be the actual signed crossing Bloch sum of [Q, C],
evaluated at this representation. We use the convention
\(\delta[t]=t\wedge(1-t)\), and the preferred peripheral marking gives
\[
                           \delta\beta=-2M\wedge\ell.
\tag{3}
\]
The sums, normalizations, and the ordered eigenvalue in (3) are fixed;
one cannot substitute a Weyl-inverted longitude while retaining (2).

**Theorem.** On every connected continued branch just specified,
\[
 \boxed{\quad
        \operatorname{Im}S_g
           -2\operatorname{Re}u\,\operatorname{Im}v
                         =D(\beta).
       \quad}
\tag{4}
\]
Here \(D\) is the Bloch--Wigner regulator. Formula (4) retains the
logarithmic sheet of the selected source and has no undetermined
real additive constant.

If this continued representation approaches the oriented complete
geometric representation and the crossing regulator has its audited
complete limit [C], then
\[
                 \lim\operatorname{Im}S_g
                       =\operatorname{Vol}(\mathcal M),
\tag{5}
\]
provided the continued longitude logarithm remains finite. The
meridian limit may be either lift \(M=1\) or \(M=-1\).
The opposite geometric orientation gives the opposite volume.
These assertions neither select the geometric component nor give
its coefficient in the physical finite-color cycle.

## 2. The differential and its sign

On a local logarithmic chart of \(t\ne0,1\), the defining expression
\[
 D(t)=\operatorname{Im}\operatorname{Li}_2(t)
                       +\log|t|\arg(1-t)
\]
has differential
\[
 dD(t)=\log|t|\,d\arg(1-t)
                         -\log|1-t|\,d\arg t.
\tag{6}
\]
Indeed differentiating the dilogarithm gives
\(-\log(1-t)\,d\log t\); its imaginary part cancels the
\(d\log|t|\arg(1-t)\) term from the second summand.
Consequently the alternating additive rule
\[
 f\wedge g\longmapsto
       \log|f|\,d\arg g-\log|g|\,d\arg f
\]
applied to (3) gives
\[
 dD(\beta)=2\operatorname{Re}v\,d\operatorname{Im}u
                    -2\operatorname{Re}u\,d\operatorname{Im}v.
\tag{7}
\]
No dilogarithmic branch choice enters (7).

Write \(u=u_R+i u_I\) and \(v=v_R+i v_I\). Equation (2) yields
\[
 d\operatorname{Im}S_g=2v_I\,du_R+2v_R\,du_I.
\]
Subtracting \(d(2u_Rv_I)\) proves
\[
 d\bigl(\operatorname{Im}S_g-2u_Rv_I-D(\beta)\bigr)=0.
\tag{8}
\]
Thus a real constant remains to be fixed. The following source
limit fixes it, rather than leaving it as a choice of action sheet.

## 3. The actual Alexander anchor

At one positive crossing let \(A=e^a,B=e^b,C=e^n\), in the
occupation and transfer conventions of [L, Q]. Its symbol is
\[
 \beta_+=[B]+[C]+[Y/A]-[BC]-[YC/A].
\tag{9}
\]
At a negative crossing it is
\[
 \beta_-=[A]+[C]+[Y/B]-[AC]-[YC/B].
\tag{10}
\]
Every \(a,b,n\) tends to zero on the actual selected source branch.
Since \(Y\to\alpha\ne0,1\), the five arguments at either sign
tend respectively to \(1,1,\alpha,1,\alpha\). The regulator is
continuous at \(1\), with \(D(1)=0\), and the two \(\alpha\)
terms cancel. Thus, crossing by crossing,
\[
                         D(\beta_\pm)\longrightarrow0.
\tag{11}
\]
The notation that the symbol tends to \([1]\) means this regulated
limit; no forbidden nondegenerate pre-Bloch generator is introduced.
There are only finitely many crossings, hence \(D(\beta)\to0\).

Also \(S_g\to0\), \(v\to0\), and \(u\) has a finite limit by
(1). Taking this limit in (8) shows its constant is zero and proves
(4) on the initial branch.

This calculation uses the original highest-cut field limit. It
does not replace that cut by a normalized average. In particular
the old coefficient potential called \(S_{\rm flat}\) in [Q] is
not identified with \(S_g\) merely because their derivatives can
be put on matching logarithmic sheets. The retained framing and
integer logarithmic characters in that potential must first be
matched. Equations (1), (2), and (11) avoid that ambiguity entirely.
The preferred framing has already been paid in [L], and the present
real constant is fixed by the selected source itself.

## 4. Classical frame regularization and logarithmic continuation

The crossing expressions are initially used on regular Gauss charts.
Forced zero fields at the highest cut can make individual arguments
equal to \(1\). They are interpreted using the continuous regulator
as in (11). This is a classical regularization, not a modification of
any quantum summand.

For completeness, the frame independence needed at such limits can
also be read directly from (3). Fix an augmented representation and
vary its generic coordinate frame, carrying the intrinsically marked
peripheral eigenline with it. Its coordinate position need not remain
fixed. The closed representation has matching cut positions and
momenta in every such frame, so the classical telescoping identity
(3) applies; no averaged quantum cut is introduced. The meridian and
longitude eigenvalues remain fixed. Hence (7) is
zero in every frame direction. The admissible generic frames form a
connected open set: the exclusions are finitely many proper complex
algebraic conditions in the connected frame variety. Two admissible
points can be joined through overlapping affine charts by generic
piecewise complex lines avoiding their finitely many excluded points.
Thus \(D(\beta)\) is constant under these frame changes.

Approaching a degenerate frame gives the same value whenever the
crossing shape limits exist, since \(D\) extends continuously to
\(0,1,\infty\), with value zero there. This justifies calculating
(11) in the actual highest frame and calculating the complete limit
in a generic frame of the same representation. It preserves the
intrinsic chosen eigenflag; no Weyl interchange is involved. In
particular this does not assert that frames fixing one coordinate
flag can approach a distinct coordinate flag.

Continue the chosen logarithms and action along a path in the
regular augmented component. Equations (2) and (7) continue on each
chart, so (8) remains zero on all overlaps. Crossing a removable
shape degeneration uses the same continuous regulator limit.
Consequently (4) persists along the entire specified lift.

In particular, a longitude logarithm must not be recentered to zero
after continuation. At a complete lift it can be an odd multiple of
\(\pi i\). If one rewrites a branch using a different logarithm,
the action must receive its corresponding logarithmic character;
the boundary term in (4) records this change. A real action period
is not determined by (4), but no free imaginary constant survives
the source anchor. Statements comparing two endpoints always use
the same continued lift from (1).

## 5. The marked regulator-line norm

Put
\[
 \mathcal R_g=S_g-uv,\qquad U=2u,\qquad V=2v,
 \qquad \mathcal P_g=\exp\!\left(\frac{2\mathcal R_g}{\pi i}\right).
\tag{12}
\]
Direct calculation from (2), with the actual preferred eigenvalues,
gives the regulator connection
\[
 d\mathcal R_g=v\,du-u\,dv
                         =-\frac{U\,dV-V\,dU}{4}.
\tag{13}
\]
In the logarithmic trivialization, the invariant norm used in [Q]
has the explicit form
\[
 \log\|\mathcal P_g\|
    =\log|\mathcal P_g|
       -\frac2\pi(u_Rv_I-v_Ru_I).
\tag{14}
\]
Since \(\log|\mathcal P_g|=2\operatorname{Im}\mathcal R_g/\pi\),
formula (4) proves
\[
 \boxed{\qquad \log\|\mathcal P_g\|=\frac2\pi D(\beta).\qquad}
\tag{15}
\]
The right side is independent of the compatible logarithm labels.
Thus (14) also checks the norm's invariance when the corresponding
regulator-line trivializations are changed. This is the norm of
the action period attached to the actual canonical minor, not the
absolute value of the original finite quantum invariant.

## 6. The geometric complete limit and its exact scope

Suppose the same continued augmented representation tends to the
oriented complete geometric representation. The full signed crossing
chain of [C], with the preferred peripheral degree-one normalization,
identifies its complete Bloch class with the fundamental class.
It follows that
\[
                          D(\beta)\longrightarrow
                                      \operatorname{Vol}(\mathcal M).
\tag{16}
\]
This uses that complete-chain theorem, not the peripheral wedge
alone. Component membership does not determine the sign: the
oriented geometric endpoint is specified in (16).

[C] states its chain calculation at \(M=1\). The other lift gives
the same crossing value. Indeed twist an \(SL_2\) representation by
the sign character of the knot abelianization. Every meridian changes
sign and the preferred longitude does not. The partial meridian
products acquire alternating scalar signs, so their Gauss diagonal
ratios \(K_j\) change sign together with \(x_0\). The occupations
\(A_j=x_0/K_j\), transfer ratios, and \(Y=x_0^2\) are unchanged.
Therefore (9), (10) are unchanged. This compares the two classical
lifts only; it is not a sign change of the selected quantum state.

At either complete lift \(\operatorname{Re}u=\log|M|\to0\).
On a path with a finite continued \(v\), the boundary term in (4)
tends to zero. Combining (4) and (16) proves (5) and
\[
 \lim\log\|\mathcal P_g\|=\frac2\pi\operatorname{Vol}(\mathcal M).
\tag{17}
\]
For the exponential of this action alone, at \(h=2\pi i/N\),
\[
 \frac{2\pi}{N}\log|e^{S_g/h}|=\operatorname{Im}S_g.
\tag{18}
\]
Its geometric complete limit is consequently the volume.

The path to the geometric endpoint, continuation of the full minor
or original cutoff along it, transport of the original physical
chain, and the coefficient and noncancellation of this contribution
in the finite invariant are separate requirements. None is supplied
by (15)--(18). The new comparison here is the source anchor that
identifies the already selected local action with the normalized
regulator; the classical regulator and fundamental-class conclusions
carry no novelty claim.

## 7. Complete written proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| L | notes/research_selected_minor_preferred_longitude.md | 50448b8688d3a7b2f4245787f6ddc07eb7afecaf94391c11c0b735ea6afdbb9c |
| Q | notes/quantum_longitude_and_regulator_action.md | e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7 |
| C | notes/crossing_fundamental_cycle.md | 0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f |

L supplies the actual selected action, representation, occupation
limit, and preferred peripheral marking. Q supplies the signed
classical crossing sum, its preferred wedge and regulator-line norm;
its averaged finite-cut presentation is not used. C supplies the
oriented complete fundamental-chain comparison. The source anchor,
real normalization, differential signs, logarithmic bookkeeping and
lift comparison are proved above. All three complete texts were read
and all used implications checked. No numerical audit is a premise.

Only written mathematics, text reads and hash checks were used.
Frozen manuscripts and public documentation are unchanged.
