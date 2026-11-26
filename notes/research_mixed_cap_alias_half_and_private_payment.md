# A failed cap half-stencil and a uniform private-alias payment

Research deduction, 7 November 2026. No functions, roots or saved
certificates are evaluated here. An exact point shows that requiring
every first-cap alias profile to satisfy the ordinary minimum-level
half-stencil is too strong. Nevertheless both private aliases admit
a uniform, strictly favorable comparison with the real-private
profile at the same early outgoing target. The comparison preserves
the whole neighboring action and the original alias penalties.
It is not yet a calibrated estimate for the complete left boundary.

## 1. Original phases and the proposed half-stencil

Keep the literal source and branches of the
[cap contour theorem](research_mixed_cap_outer_contour_reduction.md),
and the endpoint packet on
\[
 E_c=[27/100,49/100]+i[-11/200,1/25].                 \tag{1}
\]
In the notation of the
[fixed-reference cap phase theorem](research_mixed_first_cap_plateau_phase.md),
\[
\begin{split}
 \Psi_\alpha(e,z)
  &=S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),\\
 \Xi_\alpha(e,z)&=\Psi_\alpha(e,z)-\frac\alpha2g(z),
 \qquad \alpha\in\{0,1\},\\
 p_\alpha(e,z)&=\partial_z\Xi_\alpha(e,z)
       =g'(e+z)-(1+\alpha/2)g'(z).
\end{split}                                                   \tag{2}
\]
Here \(J'(w)=\Log(2\sin\pi w)\) and
\(g'(w)=\Log(1-e^{-2\pi iw})\) have their original lifts.
The cap's own type is \(3+\alpha\).

The ordinary
[minimum-level half-stencils](research_mixed_minimum_level_half_stencils.md)
use gauge \(\kappa=3/2\). Replacing the left ordinary factor
by the cap would require, among other conditions, the sign of
\[
 H_\chi(e,z;c)
 =\Re\left[(1+i\chi c/(3/25))
                    \{p_\alpha(e,z)+i\kappa\}\right],
 \qquad \chi\in\{0,1\}.                              \tag{3}
\]
This is only the cap-side half of that proposed transport argument.
It is not the derivative of the complete compensated boundary
functional. The aliases retain their fixed additive penalties, so
those penalties have zero outgoing derivative in (3).

## 2. An exact negative half at an original alias endpoint

Set
\[
 \alpha=1,\qquad e_0=\frac{49}{100}-\frac{11}{200}i,
 \qquad z_0=\frac{11}{50}-\frac1{50}i.
                                                               \tag{4}
\]
The private point belongs to the lower alias. The outgoing point
is on the boundary of the coarse attached-four height rectangle,
at the upper endpoint of the early interval. It is not asserted
to occur in the actual coupled reference image.

**Proposition 1.** At (4),
\[
                   H_0(e_0,z_0;-1/50)<-\frac1{140}.       \tag{5}
\]

*Proof.* Put \(r=e^{-3\pi/20}\) and \(R=e^{-\pi/25}\).
Directly from the original logarithms,
\[
\begin{split}
 A&=|1-e^{-2\pi i(e_0+z_0)}|^2
       =1+r^2+2r\sin(2\pi/25),\\
 B&=|1-e^{-2\pi iz_0}|^2
       =1+R^2-2R\sin(3\pi/50),\\
 \Re p_1(e_0,z_0)&=\frac14\log\frac{A^2}{B^3}.
\end{split}                                                   \tag{6}
\]
The following elementary bounds suffice:
\[
 r<\frac58,\qquad R>\frac{22}{25},\qquad
 \sin(2\pi/25)<\frac14,\qquad
 \sin(3\pi/50)<\frac{19}{100}.                         \tag{7}
\]
Here are rational witnesses, using \(157/50<\pi<22/7\).
The positive exponential polynomial through degree four at
\(471/1000<3\pi/20\) exceeds \(8/5\), proving the first
bound. For \(0<x<1\),
\[
 e^x\le1+x+\frac{x^2}{2(1-x)}.
\]
At \(x=22/175>\pi/25\), its right side is
\(197/175+242/26775<25/22\), proving the second bound.
For the third, set \(v=63/250>2\pi/25\). The alternating
sine bound gives
\[
 \sin(2\pi/25)<v-v^3/6+v^5/120
                  <v-19v^3/120<1/4.
\]
Finally \(3\pi/50<33/175<19/100\).

It follows that
\[
 A<\frac{109}{64},\qquad B>\frac{36}{25},\qquad
 \frac{A^2}{B^3}
   <\frac{185640625}{191102976}<\frac{34}{35}.           \tag{8}
\]
For the bound on \(B\), the function
\(1+R^2-(19/50)R\) is increasing for \(R\ge22/25\).
The final rational comparison in (8) has positive cross-product
difference \(79309\). Now
\(\log(34/35)<-1/35\); (6) proves (5). \(\square\)

Strictness and continuity preserve a negative value when the
private real coordinate is moved slightly inside its interval,
the outgoing real coordinate is slightly below \(.22\), and
the outgoing height is slightly below \(-.02\). Thus a proof
on the containing independent target rectangle cannot demand
\(H_0\ge0\) for every alias point.

This does not show that the displayed alias point maximizes its
profile, that it belongs to any actual reference fiber, or that
the maximum of the complete cap profiles has an unfavorable
transport derivative. In particular it is not a counterexample
to the full source estimate or to a joint cap-plus-ordinary
comparison.

## 3. The original alias penalties pay the private height change

The next statement uses the same phase, rather than a new cap
interpolation or independently selected private reference.

**Proposition 2.** For \(e\in E_c\), either \(\alpha\), and
\[
            \frac1{10}\le\Re z\le\frac{11}{50},         \tag{9}
\]
one has
\[
 -\frac{31\pi}{20}<\Im\Psi_{\alpha,e}(e,z)
                             <\frac{59\pi}{50}.        \tag{10}
\]
The bound holds at every finite outgoing height; uniform finite-source
statements below use compact height intervals. In particular, for
every \(x\in[27/100,49/100]\),
\[
\begin{split}
 \Re\Psi_\alpha(x-11i/200,z)-\frac{11\pi}{100}
     &<\Re\Psi_\alpha(x,z)-\frac{451\pi}{10000},\\
 \Re\Psi_\alpha(x+i/25,z)-\frac{2\pi}{25}
     &<\Re\Psi_\alpha(x,z)-\frac{9\pi}{500}.
\end{split}                                                   \tag{11}
\]
Both reserves exceed \(1/20\).

*Proof.* The original endpoint stationary equation and action give
\[
 S'(e)=-J'(e-u_c(e))+i\pi u_c(e).                       \tag{12}
\]
The [whole endpoint packet](research_mixed_endpoint_cap_rectangle.md),
with the bounds explicitly recorded in (6) of the
[cap phase theorem](research_mixed_first_cap_plateau_phase.md), gives
\[
 \frac{17}{100}<\Re u_c<\frac{28}{100},\qquad
           0<\Re(e-u_c)<\frac12.                      \tag{13}
\]
For any \(w\) with \(0<\Re w<1\),
\(\Re\sin\pi w>0\). The original branch therefore satisfies
\(-\pi/2<\Im J'(w)<\pi/2\), at every imaginary part.
Equations (12)--(13) imply
\[
                  -\frac{33\pi}{100}<\Im S'(e)
                                     <\frac{78\pi}{100}.
                                                               \tag{14}
\]
Also \(.37\le\Re(e+z)\le.71\), so the same argument
bound applies to \(J'(e+z)\). For \(e\in E_c\),
\(\cos(2\pi\Re e)<0\) and \(\sin(2\pi\Re e)>0\).
Thus \(1-e^{-2\pi ie}\) lies in the open first quadrant,
and \(0<\Im g'(e)<\pi/2\), with the original lift.
Finally,
\[
 \Psi_{\alpha,e}=S'(e)+J'(e+z)-i\pi z-\alpha g'(e).
                                                               \tag{15}
\]
Its imaginary part lies strictly between
\(-\pi(21/20+\alpha/2)\) and \(59\pi/50\), proving
(10) for both flags.

For any private height \(h\),
\[
 \Re\Psi_\alpha(x+ih,z)-\Re\Psi_\alpha(x,z)
             =-\int_0^h\Im\Psi_{\alpha,e}(x+iv,z)\,dv.
                                                               \tag{16}
\]
If \(h\le0\), subtracting the original \(2\pi|h|\)
penalty gives a decrease greater than \((41\pi/50)|h|\).
If \(h\ge0\), the decrease exceeds \((9\pi/20)h\).
Putting \(h=-11/200\) or \(1/25\) proves (11).
The common reserve exceeds \(1/20\) already using
\(\pi>3\). \(\square\)

The height-dependent version just proved controls a paid vertical
alias with its actual \(2\pi|h|\) penalty as well. Its reserve
tends to zero at \(h=0\); no fixed horizontal-alias reserve is
claimed at that endpoint. An unpenalized zero-frequency join is
not covered by this argument.

## 4. Exact joint-action and profile consequences

Define the real-private profile
\[
 A^{\rm real}_\alpha(z)
       =\max_{27/100\le x\le49/100}\Re\Psi_\alpha(x,z).
                                                               \tag{17}
\]
Taking maxima in (11) shows that the two original horizontal
aliases lie below (17), with their displayed reserves. The real
cut values are included in (17). Thus among these five regular
profiles, when the private main height is zero, both aliases are
strictly inactive throughout (9). This is a comparison of
profiles at the same target, not a comparison with the calibrated
cap plane at the original reference height.

More generally, add any identical real quantity
\(\Re\mathcal R(z,\mathbf w)\) to both sides of (11),
where \(\mathcal R\) is independent of the private coordinate
\(e\). The inequalities remain unchanged. In particular this
may contain the complete adjoining ordinary action, the outgoing
allocation \(-\alpha g(z)/2\), all original complex affine
marginals, and the identical middle compensation and relative
pinning fee. This proves alias suppression before separating the
two adjacent factors or discarding their shared stationarity.
No change of reference is involved.

The distinction from Proposition 1 is substantive: an inactive
alias may have a negative outgoing transport derivative and still
remain uniformly below the main profile. The exact penalty pays
its private height directly; no favorable sign of that outgoing
derivative is necessary.

## 5. Finite-source scope and what remains

The canonical retained-row interpolant in (4) of the cap contour
theorem remains regular on \(E_c\) and compact outgoing tubes
over (9): \(e,z,e+z\) all have real parts strictly between zero
and one. Its endpoint coefficient is unchanged. Consequently
(10)--(11) are bounds for the original regular alias phases;
they do not replace the cap by a differently interpolated finite
function. The existing real-color coefficient estimate can be
inserted in those same currents, retaining its angular loss and
the polynomial costs for each fixed color derivative and both
level parities.

The complete five-profile finite-source envelope in
[the boundary-window source theorem](research_mixed_boundary_window_real_color_envelopes.md)
was proved for outgoing real coordinate at least \(.22\), with
the later
[upper extension](research_mixed_cap_upper_target_extension.md)
reaching \(.5\). Its reduction of the compact physical tails
to the two real cuts is not silently extended below \(.22\).
In particular its lower-tail logarithm estimate uses
\(\cos(2\pi(y+t))<1/5\), which is not available on all of
the newly considered early strip. The true-index rows and exact
unpenalized joins must also retain their source estimates.

Thus (11) removes the need for a separately nonnegative cap-half
transport derivative for the private aliases whenever a valid
zero-private-height main comparison is used. The unresolved
deeper-boundary comparison is the calibrated joint main/cut and
physical-tail bound, with the actual outgoing taper and the
unchanged middle compensation. No complete boundary sign,
whole-word source theorem, or larger knot class follows here.
