# A fixed canonical reference for a later second-selection diagnostic

Research design, 6 November 2026. This supplies a principled fallback
reference target, not a computed point or a new source estimate.
The primary arithmetic route is a systematic pass over the saved
shorter-reference cover. The construction below is distinct: it would
validate one canonical prefix for each of two fixed types, without
claiming realization by a particular complete word. No root or parameter
evaluation is performed or authorized by this note.

## 1. A prescribed external coordinate

Use the [original reference curve](research_mixed_second_selected_reference_curve.md)
with \(\alpha=1\), second type four, and \(\beta=0\) or \(1\).
The seven prefix coordinates are
\[
                 (e,a,\xi,u,z,v,b),
 \qquad (a,u,z,v,b)=(r_1,s_2,r_2,s_3,r_3),
 \tag{1}
\]
and the fixed next external coordinate is prescribed to be
\[
                 c=\frac13,\qquad
                 C=e^{-2\pi ic}=-\frac12-\frac{i\sqrt3}{2}.
 \tag{2}
\]
This choice requires no search among auxiliary-cover cells.

The external coordinate lies strictly in every needed type-three
containing domain. In particular
\[
 \left|\frac13-\left(\frac7{20}-\frac{i}{100}\right)\right|^2
          =\frac{17}{45000}<\left(\frac{83}{1000}\right)^2.
 \tag{3}
\]
Thus \(c\in P_3\subset D_3\). It also has real part in
\((.267,.433)\), height in \((-.065,.068)\), and
\(\Re c-3\Im c=1/3<.608\), so it belongs to \(O_3\)
and \(K_3\). Its real part and height also lie in the containing
attached-three rectangle \((.278,.391)+i(-.072,.021)\).
This last inclusion does not assert that \(c\) is an actual attached
output of a suffix.

Section 4 of the reference-curve theorem therefore gives, for each
of the two fixed values of \(\beta\), a unique canonical seven-variable
prefix at (2). Existence is the proved coupled-map fixed-point theorem;
uniqueness and local holomorphy use its original accretive Hessian.
The original logarithmic equations, not merely their exponentials,
hold at this prefix.

## 2. An exact finite algebraic target

Keep \(W=e^{2\pi i\xi}\), with its positive sign, and the two
transfers of the reference theorem. For \(\alpha=1\), the
[saved canceled transport](research_mixed_second_selected_canceled_rational_transport.md)
gives
\[
                    C_\beta(W)=\frac{N_\beta(W)}{D_\beta(W)},
       \qquad N_\beta,D_\beta\in\mathbb Z[W],
 \tag{4}
\]
with coprime numerator and denominator and degrees
\[
       \deg N_0=\deg D_0=67,\qquad
       \deg N_1=\deg D_1=97.
 \tag{5}
\]
The full exact coefficients, factor powers, contents and derivatives
are retained in that note's
[exact rational record](../repro/results/research-mixed-second-selected-rational-transport-exact.json).
No new algebraic coefficient calculation is needed to define
\[
       {\cal P}_\beta(W)=2N_\beta(W)
                              +(1+\sqrt{-3})D_\beta(W),
       \qquad \sqrt{-3}=i\sqrt3.
 \tag{6}
\]
Its degrees are exactly 67 and 97: the leading coefficients of
\(N_\beta,D_\beta\) are nonzero real integers, so they cannot
cancel against the nonreal multiplier in (6).

The canonical prefix gives a root \(W_*\) of (6), with
\(\xi_*\in(.217,.234)+i(.027,.045)\), all original
denominators regular, and all original coordinate and pair-sum
conditions retained. The projection theorem in Section 4 of the
reference-curve note says \(C_\beta'(W_*)\ne0\). Therefore
\[
 {\cal P}_\beta'(W_*)=
       2D_\beta(W_*)C_\beta'(W_*)\ne0.
 \tag{7}
\]
The prescribed root is simple. This is a consequence of the original
Hessian and reference geometry, not an inference from approximate
polynomial roots.

Other roots of (6) need not belong to the canonical prefix domain.
In particular cancellation in (4) does not authorize ignoring an
original endpoint or transfer denominator. To identify a candidate
with \(W_*\), one must retain the original regularity, logarithmic
lift and domain conditions. The uniqueness theorem applies after
these conditions; it is not a statement that (6) has only one complex
root.

## 3. Possible bounded validation and its scope

A separately reviewed diagnostic could validate the two fixed
cases in (2), either by a local interval-Newton/Rouche enclosure
for (6), or by a local interval-Newton/Krawczyk enclosure for the
seven original logarithmic equations in (1). The latter keeps a
small system with the proved canonical Hessian rather than
isolating all unrelated roots of the degree-67 or degree-97 polynomial.
Any numerical proposal would be followed by an outward local
existence check and the original domain/lift checks. The fixed
initialization, iteration limits, precision, validation radius and
failure protocol must be specified before an execution; none is
silently selected here.

Such a validated enclosure would contain a genuine canonical-prefix
reference. The theorem's uniqueness would identify it independently
of the method used to propose its center. It would not prove that
the fixed external value \(c=1/3\) is generated by a prescribed
finite mixed suffix, nor would it prove any central scalar sign.

The systematic saved-cell route has a different purpose: it
encloses the whole necessary reference family, passing or excluding
each saved cell by the same original filters. A cell of the old
first-four/next-four cover need not contain any admissible longer
prefix. Conversely a single validated root of (6) would supply a
sound local diagnostic target but would not replace a full-domain
comparison. Neither route permits automatic replacement point tests
after an inconclusive or excluded diagnostic.
