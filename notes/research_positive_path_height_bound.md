# A uniform height bound for positive path fillings

Research note, 3 November 2026.

Let the selected vertices form a finite nonempty path. Their original
degrees, including edges to complete outside vertices, are at most two,
and at least one outside edge is present. Suppose every selected
integer power is at least three. The positive solution exists by
[Theorem 15 of the corridor note, after mirroring](research_negative_corridor_variational_bounds.md).
We prove the uniform bound
\[
                            0<-\Im t_v<23/20.
\tag{1}
\]
It is independent of the path length and of all filling powers.
The proof reduces the assertion to an inequality on a compact
rectangle and verifies that inequality with outward interval arithmetic.
The resulting geometric energy comparison is given in
[Section 7 of the energy note](research_edge_cut_energy_comparison.md#7-consequences-of-a-uniform-height-bound).
Neither statement supplies a quantum lower bound.

## 1. Returns at a vertex of maximum height

Write \(t_v=a_v-iH_v\), where \(0<a_v<\pi\) and \(H_v>0\).
Both coordinates vanish at a complete outside vertex.
The original positive return and unit-charge equation are
\[
 r(t_v,t_w)=\operatorname{arsinh}
     \bigl(\tan(t_v/2)\cos(t_w/2)\bigr)=k_{v,w}+ig_{v,w},
 \qquad
 \sum_{w\sim v}r(t_v,t_w)=\frac{i n_vt_v}{2}-\pi i.
\tag{2}
\]
Here \(k_{v,w}>0\) and \(-\pi/2<g_{v,w}<\pi/2\).
Choose a selected vertex of maximum height, with coordinates \(a,H\).
Every neighbor has angle \(b-ih\), with \(0\le b\le\pi\) and
\(0\le h\le H\). Consequently \(c=\cos((b-ih)/2)\) belongs to
the quarter ellipse
\[
 D_H=\{X+iY:X,Y\ge0,\quad X^2/C^2+Y^2/S^2\le1\},
 \qquad C=\cosh(H/2),\quad S=\sinh(H/2).
\tag{3}
\]
Indeed \(X=\cos(b/2)\cosh(h/2)\) and
\(Y=\sin(b/2)\sinh(h/2)\), which imply (3).

Set \(A=\tan((a-iH)/2)\). Its real part is positive and its
imaginary part negative. Thus \(Ac\) lies in the right half-plane
for nonzero \(c\in D_H\). The function
\(r(c)=\operatorname{arsinh}(Ac)\), continued from that half-plane,
is holomorphic in the interior and continuous on the boundary.
For real \(\lambda\), the function
\(\Re r-\lambda\Im r=\Re((1+i\lambda)r)\) is harmonic, so its
maximum is attained on one of the three boundary pieces
\[
 \begin{array}{ll}
 c=C\cos(\pi u/2)+iS\sin(\pi u/2),&0\le u\le1,\\
 c=Cu,&0\le u\le1,\\
 c=iSu,&0\le u\le1.
 \end{array}
\tag{4}
\]
There are at most two incidences. Pad a degree-one vertex by the
allowed zero return \(r(0)=0\). Equation (2) requires their average
to equal
\[
                   R_n(a,H)=\frac{nH}{4}
                       +i\left(\frac{na}{4}-\frac{\pi}{2}\right).
\tag{5}
\]
It is therefore enough to find \(\lambda\) such that
\[
 \max_{c\in\partial D_H}(\Re r-\lambda\Im r)
       <\frac{nH}{4}-\lambda\left(\frac{na}{4}-\frac{\pi}{2}\right).
\tag{6}
\]
The maximum principle would give the same strict bound for the
average, contradicting (5).

## 2. A preliminary upper bound

The identity
\(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\) gives
\(k\le\operatorname{arsinh}|Ac|\). Also
\(|A|\le\coth(H/2)\) and \(|c|\le\cosh(H/2)\).
Taking real parts in (5) and using \(n\ge3\) gives
\[
 \frac{3H}{4}\le\operatorname{arsinh}
                   \frac{\cosh^2(H/2)}{\sinh(H/2)}.
\tag{7}
\]
Put \(y=H/4\). Multiplying the equivalent hyperbolic-sine
inequality by \(2\sinh(2y)\) shows that (7) requires
\[
 f(y)=\cosh(5y)-\cosh y-\cosh(4y)-1\le0.
\]
For \(y>0\),
\[
 f'(y)=4\{\sinh(5y)-\sinh(4y)\}
                         +\{\sinh(5y)-\sinh y\}>0.
\]
The certificate below verifies \(f(1/2)>0.24\).
Hence every maximum height satisfies \(H<2\).

## 3. The compact inequality and its certificate

**Lemma.** For every \((a,H)\in[0,\pi]\times[23/20,2]\)
there is a real \(\lambda\) with \(H-\lambda a>0\) such that
\[
 \max_{c\in\partial D_H}
   \{\Re\operatorname{arsinh}(Ac)-\lambda\Im\operatorname{arsinh}(Ac)\}
       <\frac{3H}{4}-\lambda\left(\frac{3a}{4}-\frac{\pi}{2}\right).
\tag{8}
\]
At \(a=0,\pi\), values mean the continuous limits from the interior.

Here are the formulas and subdivision rules for the finite interval
proof. For \(z=x+iy\) in the closed right half-plane, let
\(D_+=|z+i|\), \(D_-=|z-i|\). The branch in (2) satisfies
\[
 \Re\operatorname{arsinh}z
    =\operatorname{arcosh}\frac{D_++D_-}{2},\qquad
 \Im\operatorname{arsinh}z
    =\arcsin\frac{D_+-D_-}{2}.
\tag{9}
\]
Indeed, writing \(z=\sinh(k+ig)\) gives
\(D_\pm=\cosh k\pm\sin g\), including boundary limits.
The arguments of the inverse functions therefore belong to
\([1,\infty)\) and \([-1,1]\). Intersecting an enclosure with
these known ranges retains every possible value.

The
[certificate program](../experiments/certify_positive_path_maximum_height.py)
starts with 32 rational rectangles covering the normalized domain
\((a/\pi,H)\in[0,1]\times[23/20,2]\).
It chooses a rational slope for each trial rectangle, then verifies
throughout that rectangle that \(H-\lambda a>0\) and that the
lower bound for the right side of (8) exceeds the upper bound
on every boundary segment in (4).
All accepted inequalities use Arb with 100-bit precision and
outward rounding. The multiplier is evaluated as
\[
                         A=\frac{\sin a-i\sinh H}{\cos a+\cosh H},
\]
whose denominator is positive. Formula (9) uses real square roots
and monotone inverse functions. Numerical optimization proposes
slopes only; it cannot accept a rectangle.

Unverified boundary intervals are bisected. If a segment budget is
exhausted, the parameter rectangle itself is bisected and retried.
A parameter rectangle is accepted only after all three boundary
intervals have been covered by verified pieces.
The computation terminates with 1,712 accepted parameter rectangles
and 131,050 verified boundary segments. The
[result file](../repro/results/research-positive-path-maximum-height.json)
records their rational endpoints, rational slopes, positive margins,
segment counts and program hash.

Coverage follows from subdivision: an unaccepted rectangle is
replaced by its two halves, and no other rectangle is removed.
The final queue is empty. An additional exact check gives total
rational area \(17/20\), the area of the initial normalized domain.
The same exhaustive subdivision rule covers each boundary parameter.
Thus the verified strict inequalities prove the lemma.

For \(n\ge3\), the target support value in (6) exceeds that in
(8) by
\[
                              \frac{n-3}{4}(H-\lambda a)\ge0.
\tag{10}
\]
The one certificate therefore applies simultaneously to every
power \(n\ge3\).

## 4. The height theorem

**Theorem.** Every positive solution specified above satisfies
(1). The bound also holds on every component obtained by making
any collection of selected vertices complete.

**Proof.** Choose a vertex of maximum height. Section 2 excludes
\(H\ge2\). If \(23/20\le H<2\), the lemma and (10) exclude
the average required by (5). Therefore \(H<23/20\).
All remaining heights are at most this maximum.
Completing vertices splits the path into components of the same
type; apply the same argument to each nonempty component. \(\square\)

The compact exclusion uses only the degree bound, sign and branch
conditions, and the period equation. Existence for the stated integer
powers comes from the separate corridor theorem. No existence for
other powers or graphs is asserted.

To reproduce the certificate from the repository root, run:

~~~sh
python3 experiments/certify_positive_path_maximum_height.py
~~~

The required packages are python-flint, NumPy and SciPy.
NumPy and SciPy propose slopes; Arb performs every comparison used
in the proof.

## 5. The same bound during a positive fractional-charge deformation

The height estimate extends to an already existing positive solution
whose charges \(\chi_v\) belong to \([0,1]\). The period equation is now
\[
                 \sum_{w\sim v}r(t_v,t_w)
                         =\frac{i n_vt_v}{2}-\pi i\chi_v.
\tag{11}
\]
At each active vertex assume \(0<a_v<\pi\), \(H_v>0\), with the
same positive branch as before. Complete zero-angle vertices are
allowed. No assertion of existence for all such charge assignments
is part of this height estimate.

**Corollary.** Every solution just specified satisfies
\(H_v<23/20\), provided \(n_v\ge3\).

**Proof.** The quarter-ellipse argument and the coarse bound \(H<2\)
are unchanged, since the charge occurs only in the imaginary part of
the period equation. The strengthened
[certificate](../experiments/certify_fractional_path_maximum_height.py)
proves (8) with every support slope \(\lambda\le0\).
For the target at charge \(\chi\le1\), its support value exceeds
the unit-charge target by
\[
          -\lambda\frac{\pi(1-\chi)}2\ge0.
\tag{12}
\]
Increasing the power again contributes the nonnegative quantity
in (10). Thus the same strict separation excludes every
\(H\in[23/20,2]\), proving the claim. \(\square\)

The strengthened computation covers 1,650 parameter rectangles
and 130,146 boundary segments. It uses the same branch-safe
return enclosures as Section 3, with the additional exact check
that each rational slope is nonpositive. Its
[saved certificate](../repro/results/research-fractional-path-maximum-height.json)
records both the program hash and the hash of that shared
implementation. Its exhaustive subdivision has the same
coverage proof as before. To reproduce it, run:

~~~sh
python3 experiments/certify_fractional_path_maximum_height.py
~~~

This corollary bounds a positive deformation until it reaches a
boundary of the positive domain. Proving that no such boundary
is reached requires a separate continuation argument.
