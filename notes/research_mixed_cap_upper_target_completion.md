# Complete cap support through the upper half endpoint

Research theorem, 7 November 2026. The original allocated first-cap
supporting plane extends from \([.22,.45]\) to \([.22,.5]\), at
the actual outgoing height. All retained currents, physical tails,
true index endpoints and Fourier halfweights are included. The bound
also retains strict decay in the real ordinary color. The only new
execution was a fixed exact recombination of the completed source
replay; there were no new analytic evaluations or source refinements.

## 1. Original source and actual-reference scope

Let the first type be \(3+\alpha\), \(\alpha\in\{0,1\}\), in
an original mixed open word of length \(m\ge2\). Keep its actual
attached endpoint outputs \(e_*=b+ih_*\), \(z_*=a+ic\), and
the original calibrated action
\[
 T(z)=\mathcal T_\alpha(z,-2),\qquad
 L_\alpha(z)=T(z)-\frac\alpha2g(z),\qquad
 p=L_\alpha'(z_*),\qquad \kappa=\frac1{2500000}.
 \tag{1}
\]
The attached coordinate \(z_*\) is not the external input of the
endpoint map. The actual-reference family is exactly the one in
[complete first-cap support](research_mixed_first_cap_plateau_completion.md):
the original coupled exclusions rule out both the ordinary-neighbor
case \(m\ge3\) and the separate endpoint case \(m=2\).
There is no enlargement to independent reference rectangles and no
exclusion of an independently varying target.

The literal cap remains
\[
 U_{\alpha,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})(rX;r)_i}{(r;r)_i^{1+\alpha}},
 \qquad r=e^{-2\pi i/N},\quad X=e^{-2\pi iz}.
 \tag{2}
\]
Put \(P^+=[.22,.5]\). For \(y\in P^+\), set
\[
 z=y+ic,\qquad d=y-a,\qquad
 B_L(y)=\Re L_\alpha(z_*)+\Re p\,d-\kappa d^2,
 \qquad
 B_T(y)=\Re T(z_*)+\Re T'(z_*)d-\kappa d^2.
 \tag{3}
\]
All height occurrences in (3) are the original attached height \(c\).
The source, logarithmic lifts, chirps, endpoint normalizations and
constant residue coefficient \(+N\) are unchanged.

## 2. All eight cut and alias families are paid

The [upper-target domain theorem](research_mixed_cap_upper_target_extension.md)
proves the full cap envelope on \(P^+\). It also proves, on the
original main height, the stronger main-current inequality
\[
 \Re\Xi_\alpha(x+ih_*,y+ic)
 \le \Re L_\alpha(z_*)+\Re p\,d
          -\frac\pi{400}\bigl((x-b)^2+d^2\bigr),
 \qquad .27\le x\le .49,
 \tag{4}
\]
where \(\Xi_\alpha=\Psi_\alpha-\alpha g(z)/2\).
In particular the main current is below \(B_L\).

The [current-transport proof](research_mixed_cap_upper_target_current_transport.md)
extends each old calibrated cut/alias defect from \(y=.45\) to
\(y=.5\) with the following fixed upper costs:
\[
 \begin{array}{c|cccc}
 \alpha&\text{left real cut}&\text{right real cut}
                       &\text{lower alias}&\text{upper alias}\\ \hline
 0&1/25&0&1/25&1/20\\
 1&0&0&0&\pi/250<11/875.
 \end{array}
 \tag{5}
\]
The cuts remain at real private coordinates \(.27,.49\), at height
zero. The lower and upper aliases remain at private heights
\(-.055,.04\), with their original penalties \(.11\pi,.08\pi\).
The proof keeps the same-radius original reference in the derivative
comparison; in particular it does not discard the alias chirp.

The sole fixed saved-data test has completed:

| Artifact | SHA256 |
|---|---|
| [Saved transport result](../repro/results/research-mixed-cap-upper-target-current-transport.json) | `464812348da2f11548e190599732ffe7e3cf1a4ca82ce6637d87fbbc0515cf4d` |
| [Exact saved-data checker](../experiments/check_mixed_cap_upper_target_saved_transport.py) | `283efd6fd78186eaf6a8e6d5f4fd1463af7e50326415ff0073800479b3b5e3ba` |
| [Fixed protocol](research_mixed_cap_upper_target_saved_transport_protocol.md) | `dd680cdd7cc6191c22da11e82a48957b4213dbdb61f1f1bff1d0178513fdc7d3` |

It covers all 21,032 original jobs from 5,258 endpoint cells and all
22,323 source leaves. There are 20,112 nonempty jobs and 920
excluded-only jobs; the latter supply no source sign. Every original
source tier, partition, family and actual-reference exclusion is
retained. All 400 input bindings are unchanged. The checker parses
each saved decimal ball outward, adds only (5), and preserves the
exact maximum and a witnessing job for every family. All eight
maxima are strictly negative; their common margin is greater than
\(1/200000\). No root, primitive, optimizer, source replay,
new parameter cell, refinement or retry was used.

Consequently every allocated real-cut and horizontal-alias profile
is below \(B_L(y)-1/200000\) on \(P^+\). The original estimate
already supplies this margin for \(y\le.45\); (5) and the saved
maxima supply it on the added strip. Together with (4) and private
height convexity, this pays every zero-mode join and both sign halves
of every vertical alias. In particular the zero-height kernel
endpoints have not been omitted.

## 3. The sharper true-index ceiling fits the extended plane

The original phase proof, Section 6 of
[the full plateau deduction](research_mixed_first_cap_plateau_phase.md),
establishes, independently of the target,
\[
 \Re T(z_*)>1,\qquad |\Re T'(z_*)|<1,
                 \qquad .246<a<.391.
 \tag{6}
\]
Thus \(|d|<127/500\) on \(P^+\), and
\[
 B_T(y)>1-\frac{127}{500}
                -\kappa\left(\frac{127}{500}\right)^2
                     >\frac{149}{200}.
 \tag{7}
\]
For the last inequality, the difference before the quadratic debit
is \(1/1000\), whereas
\(\kappa(127/500)^2<\kappa<1/1000\).

Use the actual true-index ceiling, rather than replacing it by
\(3/4\). The lower end has rate less than \(1/4\). At the upper
end the original zero-safe product estimate gives
\[
 E_{\mathrm{end}}
 \le\frac35+2\pi c_++\frac1{100}\log(40/19)
 \le\frac35+\frac{21\pi}{500}
                          +\frac1{100}\log(40/19)
 <\frac{37}{50}.
 \tag{8}
\]
Here \(c_+=\max(c,0)\le.021\), \(\pi<22/7\), and the
already used elementary bound \(\log(40/19)<4/5\) suffice.
On the enlarged interval the denominator angles in the exact upper
product range over \([.21,.5]\), so their same lower bound
\(19/20\) remains valid. The physical upper-half Newton estimate
uses only \(V_\theta\le0\), retaining every revived row; no
complete-color cancellation is substituted there. Equations (7)
and (8) leave a bare reserve greater than \(1/200\).

For \(\alpha=1\), allocation of the actual unselected halfweight
does not consume this reserve. Indeed \(-.108<c<-.020\). If
\(r_c=e^{2\pi c}\), the original elementary radius bound gives
\(r_c>1/2\), while \(\cos(2\pi y)<1/5\) on \(P^+\).
Therefore
\[
 |1-r_c e^{-2\pi iy}|^2
      =1+r_c^2-2r_c\cos(2\pi y)>1,
 \qquad \Re g'(y+ic)>0.
 \tag{9}
\]
The original normalization and real logarithm at \(1/2+ic\)
give \(\Re g(1/2+ic)=0\). Hence \(\Re g(y+ic)\le0\)
on \(P^+\). The absolute Fourier-polynomial bound in Section 5 of
[Fourier weight continuation](research_mixed_fourier_weight_continuation.md)
therefore supplies rate \(-\Re g(y+ic)/2\), including \(y=.5\).
It is an absolute bound, not a relative approximation at a possible
zero of the finite weight.

Horizontal convexity \(\Re g''(y+ic)\ge0\) through \(y=.5\)
now gives
\[
 \begin{split}
 B_L(y)-\left(E_{\mathrm{end}}-\frac12\Re g(y+ic)\right)
 ={}&B_T(y)-E_{\mathrm{end}}\\
 &+\frac12\{\Re g(y+ic)-\Re g(z_*)
                                      -\Re g'(z_*)d\}
 >{}&\frac1{200}.
 \end{split}
 \tag{10}
\]
There is no halfweight when \(\alpha=0\). Thus every true-index
endpoint has the same strict allocated reserve for both own types.

## 4. Whole finite source and real colors

**Theorem.** There is \(c_*>0\) such that for every
\(\tau>0\), uniformly on the actual-reference family of Section 1,
\(y\in P^+\), \(-\pi\le\theta\le\pi\), and both level parities,
\[
 \begin{split}
 &|U_{\alpha,N}(-2\cos\theta,e^{-2\pi i(y+ic)})|
             |d_N(e^{-2\pi i(y+ic)})|^{\alpha/2}\\
 &\hspace{1cm}\le C_\tau N^{A_\tau}
       \exp N\{B_L(y)-c_*(1-\cos\theta)+\tau\}.
 \end{split}
 \tag{11}
\]
Every fixed ordinary-color derivative obeys the same rate with a
possibly different polynomial prefactor. On a fixed sufficiently
small ordinary-color neighborhood of \(-2\), the analogous bound
holds with exponent \(B_L(y)+\tau\).

*Proof.* The upper-target envelope keeps a positive common angular
constant \(c_0\) on all five retained current families and both
compact physical tails. Sections 2--3 place the allocated current
maximum below \(B_L\) and the separate true-index ceiling below
\(B_L-1/200\). Since \(1-\cos\theta\le2\), take
\(c_* =\min(c_0,1/400)\). The two exponential terms of that
literal source envelope are then both bounded by the exponent in
(11). Its exact finite-row, contour and zero-safe bounds include
the full original polynomial. The absolute Fourier bound is color
independent. Allocate one total tolerance below \(\tau\), retain
the finite number of current terms, and absorb the remaining
polynomial factors. The inherited fixed-jet theorem gives the
ordinary-color derivatives. The same source estimates on a small
complex color neighborhood, with their small rate tolerance, give
the final assertion. No square root of the finite Fourier weight
or division by it is used. \(\square\)

The original nonzero local cap packet and its additively calibrated
phase remain unchanged. Equation (11) is a full-source upper bound
on an enlarged horizontal interval, not a moving-packet assertion
at every target. The slope \(p\) in (1) is still the full complex
marginal. A later height change \(v\) would retain the affine term
\(-\Im p\,v\), and requires its own source comparison even with
that term present.

In particular this theorem supplies no independent bound for a
macroscopic taper or reset of the outgoing height. The local reset
defect in Section 4 of the upper-target domain theorem remains
compatible with (11). A full boundary functional must retain and
pay that defect with its neighboring factors and occupation energy.
No whole mixed-word source theorem, new knot-family identity or
cofinite partial-filling theorem is inferred here.
