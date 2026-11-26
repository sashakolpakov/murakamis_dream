# No competing interior cap saddle on the original prewall sheet

Research deduction, 8 November 2026. The original reduced cap
phase has exactly one critical point on its entire prewall
vertical strip, not merely on the compact rectangle containing
the known geometric point. Every nonzero integer Fourier shift
of that phase has no critical point on the strip. The selected
phase is strictly horizontally concave throughout its lower
half, and its real part grows at lower imaginary infinity.

These are actual properties of the original cubic and analytic
phase. They eliminate interior saddle competition on this
sheet. They do not continue the complete finite-source packet
to a region where that packet has not been proved, nor do they
by themselves preserve a thimble coefficient when a contour
meets the boundary of its controlled source region.
No numerical evaluation is used.

## 1. Original branch and global prewall phase

For real \(1/2\le a\le7/10\), set
\[
 X=e^{-2\pi ia},\qquad v=1-a,\qquad
 \mathcal S_a=\{e\in\mathbb C:0<\Re e<v\},\qquad
 p=e^{2\pi ie}.
                                                               \tag{1}
\]
The map \(e\mapsto p\) identifies this strip with the sector
\(0<\arg p<\arg X=2\pi v\). In particular \(p\) is upper,
nonzero, and different from \(X\).

The endpoint quadratic on its original sheet is
\[
 (p-5)\omega^2+2(p+1)\omega+p-1=0.
                                                               \tag{2}
\]
For every upper \(p\), it has exactly one upper root
\(\omega(p)\). This is the global upper-root argument in
[the above-curve source theorem, Section 2](research_mixed_endpoint_region_above_real_curve.md):
the discriminant \(16(2p-1)\) and leading coefficient
do not vanish there; a real root would make \(p\) real;
near \(p=1\), the two roots enter opposite half-planes.
Consequently this upper root is a single holomorphic function
on the upper \(p\)-half-plane.

It never vanishes there. Also \(p-\omega(p)\ne0\): inserting
\(p=\omega\) in (2) gives \((\omega-1)^3=0\), a real point.
The function
\[
 \mathcal L_a(e)=
            \frac{\omega(p)(p-X)}{p-\omega(p)}
                                                               \tag{3}
\]
is therefore holomorphic and nonzero on all of \(\mathcal S_a\).

At the original cap critical point, the
[original incoming-transport theorem](research_mixed_half_face_general_incoming_transport.md)
identifies (3) with \(e^{\Psi_e}\), using the zero logarithmic
lift of
\[
 \Psi(e,a)=S(e)+J(a+e)-J(a)-i\pi ae .
                                                               \tag{4}
\]
Because \(\mathcal S_a\) is simply connected, (3) has a unique
holomorphic logarithm agreeing with that original derivative
near the critical point. Integrating this logarithm, with the
original critical value fixing the additive constant, defines
the holomorphic continuation of (4) throughout \(\mathcal S_a\).
We continue the original phase, rather than choosing a fresh
principal logarithm independently at each point.

This definition concerns the action sheet. Some individual
auxiliary primitive arguments can leave their initial real-part
strips away from the critical point. Equation (3) supplies the
analytic continuation through those coordinate boundaries;
it does not assert a nonzero finite factorial symbol there.

## 2. The three cubic branches have distinct half-plane roles

An exponentiated stationary point of (4) obeys
\[
 f_X(\omega)=(6-X)\omega^3-(5+2X)\omega^2
                                  +(4-X)\omega-1=0,
 \qquad
 p=\frac{5\omega^2-2\omega+1}{(\omega+1)^2}.
                                                               \tag{5}
\]
Its discriminant is
\[
                         64(X^3-17X^2+19X-7).
                                                               \tag{6}
\]
For nonreal \(X\) on the present unit arc, the imaginary part
of the cubic factor in (6) is
\(2\Im X(2(\Re X)^2-17\Re X+9)>0\).
At \(X=-1\), it is nonzero as well. No cubic roots coalesce,
and \(6-X\ne0\) prevents escape to infinity.

Here is the full sign inventory, extending the selected-root
identification in the incoming-transport theorem:
\[
 \begin{array}{c|c|c}
 \text{branch for }1/2<a\le7/10&\Im\omega&\Im p\\ \hline
 \text{selected original branch}&+&+\\
 \text{continuation of the half-face real root}&+&-\\
 \text{continuation of the lower half-face root}&-&-
 \end{array}                                                     \tag{7}
\]
To check it, at \(X=-1\) the unique real root satisfies
\(1/5<\alpha<1/4\). Its two derivatives are
\[
 \omega_X(\alpha)=
       \frac{\alpha(\alpha+1)^2}{f_{-1}'(\alpha)}>0,\qquad
 \frac{dp}{d\omega}(\alpha)=
       \frac{4(3\alpha-1)}{(\alpha+1)^3}<0.
                                                               \tag{8}
\]
Thus as \(X\) enters its upper arc, this root has upper
\(\omega\) and lower \(p\). The original complex pair has
the other two sign pairs in (7).

No real \(\omega\) can occur on the nonreal \(X\)-arc, since
\[
 X=\frac{6\omega^3-5\omega^2+4\omega-1}
                  {\omega(\omega+1)^2}
\]
would be real. The excluded values \(0,-1\) are not cubic roots.
Nor can a nonreal \(\omega\) have a real \(p\) on this arc.
If \(p\ge1/2\), (2) has real roots, including the linear
case \(p=5\). If \(p<1/2\), its nonreal roots satisfy
\[
 |\omega|^2=\frac{1-p}{5-p},\qquad
 \Re\omega=\frac{p+1}{5-p}.
\]
The critical equation gives \(X=1+p-p/\omega\), and hence
\[
                         |X|^2=1-\frac{4p^3}{1-p}.
                                                               \tag{9}
\]
On the unit circle this forces \(p=0\) and \(X=1\), excluded
here. These facts prove that none of the signs in (7) can change.
At \(X=-1\) itself only the selected root has upper \(p\);
the real root has real \(p>1/2\).

It follows that exactly one root of (5) can belong to the
entire prewall strip (1). The original no-wall guards put
that selected root strictly inside it, and its original
logarithmic lift is zero. Consequently
\[
 \boxed{\quad
 \Psi_e(e,a)=0\text{ has exactly the one original solution }
 e=e_*(a)\text{ on }\mathcal S_a .
 \quad}                                                         \tag{10}
\]
This excludes other finite critical values on this analytic
sheet. It does not compare the values of phases defined on
the two different lower-\(p\) sheets.

## 3. No nonzero Fourier alias has an interior saddle

For each integer \(m\), retain the shifted action
\[
                       \Psi_m(e,a)=\Psi(e,a)+2\pi i m e.
                                                               \tag{11}
\]
If \((\Psi_m)_e=0\), exponentiation again gives
\(\mathcal L_a(e)=1\), and hence the very same cubic (5).
By (7)--(10), its sole possible point in \(\mathcal S_a\)
is \(e_*(a)\). At that point the original derivative is
\(\Psi_e=0\), so it solves (11) only when \(m=0\).
Therefore
\[
               (\Psi_m)_e\ne0
                \quad\hbox{on }\mathcal S_a,\qquad m\ne0.
                                                               \tag{12}
\]
The integer lift is retained; the exponentiated equation
alone would not prove this assertion.

On every compact family inside the prewall strips there
is a constant \(c>0\) such that
\[
                 |(\Psi_m)_e|\ge c(1+|m|),\qquad m\ne0.
                                                               \tag{13}
\]
For finitely many \(m\), this follows from (12), continuity
and compactness. For the remaining integers it follows
from \(2\pi|m|-|\Psi_e|\). Thus there is no interior
stationary transition from the original zero mode to
a nonzero lattice mode on this sheet.

Equation (13) concerns the analytically continued actions.
Using it in a finite-source integration by parts still
requires a proved amplitude estimate on the actual contour,
and retains the boundary terms. It is not an alternative
proof of the complete tall-alias current bounds.

## 4. Lower-half concavity and no lower-infinity escape

The original derivative identity, continued on the same
sheet, is
\[
 -S''(e)=\pi\cot\pi e+
        \frac{2\pi}{\sin\pi e\sqrt{\,2-e^{-2\pi ie}\,}}.
                                                               \tag{14}
\]
It is holomorphic for \(0<\Re e<1/2\): the sine and square
root have no zero there, and the root keeps positive real
part. Equality follows from the original germ and analytic
continuation.

For \(e=E-iH\), \(0<E<1/2\), \(H\ge0\), the sine argument
lies in \((-\pi/2,0]\), whereas the argument of the square
root lies in \([0,\pi/4)\). The sum stays strictly between
\(-\pi/2\) and \(\pi/2\). Its reciprocal therefore has
positive real part, as does \(\cot\pi e\) when \(E<1/2\).
Since \(1/2<a+E<1\) in the prewall strip,
\[
 \boxed{\quad
 -\Re\Psi_{ee}(e,a)
    =-\Re S''(e)-\pi\Re\cot\pi(a+e)>0
       \quad(0<E<v,\ \Im e\le0).
 \quad}                                                         \tag{15}
\]
Thus \(\Re\Psi\) is strictly concave along each horizontal
line and strictly convex along each vertical line throughout
the lower prewall strip. The assertion is not limited to
the previously certified source rectangles.

The real part also grows at lower imaginary infinity, locally
uniformly away from the two real strip boundaries. Indeed,
as \(p\) tends to infinity in a closed upper sector, (2) gives
\[
 \omega(p)=-1+O(|p|^{-1/2}),\qquad
 \mathcal L_a(e)=-1+O(|p|^{-1/2}).
\]
Consequently the continued logarithm has a finite limit
\(i(2k+1)\pi\), for one integer \(k\), with error
\(O(e^{-\pi H})\). The limit is independent of \(E\) and \(a\)
by continuity on the connected parameter strip.

Its sign is fixed without a phase evaluation. On the vertical
line through \(E_*(a)\), the derivative is zero at the actual
critical height \(h_*(a)<0\). By (15),
\(\partial_h\Im\Psi_e=\Re\Psi_{ee}<0\); lowering \(h\)
therefore makes \(\Im\Psi_e\) strictly positive.
Hence \(2k+1\ge1\). Integrating the exponentially small
error gives, on every compact real substrip,
\[
                  \Re\Psi(E-iH,a)\ge\pi H-C
                    \qquad(H\ge H_0).
                                                               \tag{16}
\]
The original branch could fix the integer more sharply,
but that is unnecessary for (16).
A path with bounded upper action cannot escape through
lower imaginary infinity while its real coordinate stays
in such a compact substrip.

## 5. What remains for the original cycle coefficient

The complete cap near the exact later incoming point is proved
in [the local complete assembly](research_mixed_cap_later_point_complete_packet.md).
Its coefficient includes the nonzero original endpoint symbol,
the Gaussian square root and the actual zero-mode density \(+N\).
The exact outer residue identity also retains both horizontal
aliases, all four weighted side pieces, the two physical end
ranges and every unweighted main join.

The present lemma rules out two proposed ways that its interior
contribution might change: there is no second finite saddle on
the original prewall sheet, and no nonzero integer Fourier mode
can become stationary there. Equation (16) additionally rules out
finite-action escape to lower infinity in a compact real strip.

It does not verify the controlled relative-cycle transport in
[the dominant-saddle theorem](research_dominant_saddle_transport.md).
For this source the remaining issue is concrete: the original
main cycle must reach and leave the unique critical neighborhood
through a region where the complete \(C_N\) amplitude is controlled,
with the unused chains below \(M(a)\) by a common strict gap.
Finite endpoints, the real strip boundaries and boundaries
of that proved amplitude region must all remain paid.
A bound on the canonical phase alone does not bound an
unproved continuation of the finite amplitude.

The [fixed-departure obstruction](research_mixed_cap_fixed_departure_global_obstruction.md)
is exactly such a boundary issue: a specified available source
point can rise above the selected action although there is no
competing interior critical point. Its failure is not an
ordinary saddle-to-saddle Stokes transition.
The uniform left component and complete right/alias estimates
already control their stated original currents. What is still
needed globally is a compatible paid connection of the zero
mode through the actual source region, or an equally explicit
relative-cycle construction with the same complete bounds.

Thus the selected coefficient cannot be removed by an interior
saddle exchange on this sheet; preserving it for the full finite
cap still requires the boundary/source control just described.
No whole real-arc cap asymptotic or filling-family extension
is inferred from this no-competition theorem.

