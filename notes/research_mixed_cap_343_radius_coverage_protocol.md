# One fixed radius-coverage test for the cap-initialized ordinary 343 family

Private protocol, 8 November 2026. **Unrun.** This specifies one
nonadaptive boundary cover for the original seven-variable \(343\)
half-chain. It can prove inclusion in, or exclusion from, the
additional radius domain of the completed lower-left source estimate.
No mathematical evaluation or saved-root calculation was used to
choose the settings below.

Only the root may execute the one frozen attempt, after separate
full source/proof and code reviews and inspection of the final
manifest. Creating these files does not authorize execution.
No center pilot, changed start, refinement, retry, continuation
from a preceding cell, or automatic replay is permitted.

## 1. Exact source and useful possible conclusions

Use the actual family and qualifications of
[the coverage audit](research_mixed_next_three_deep_radius_actual_coverage.md).
The variables, in this fixed order, are
\[
                  v=(e,a,u,p,y,s,z).
 \tag{1}
\]
They are the first cap private leg, first attached leg, cap
auxiliary coordinate, two legs of the four, and two legs of the
following ordinary three. The external input is \(b=s_4\).
The literal action is
\[
\begin{split}
\mathcal H(v;b)={}&E(e,u)+V_0(e,a)+G(a,p)+V_1(p,y)\\
                 &+G(y,s)+V_0(s,z)+G(z,b),
\end{split}
\tag{2}
\]
with the unchanged primitives, constants and chirps of
[cap-phase entrance, Section 1](research_mixed_alternating_cap_phase_entrance.md).
That theorem already gives a unique original-log zero,
holomorphic near both full closed typed disks \(D_3,D_4\).

Cover the complete boundaries of the smaller disks
\[
\begin{split}
 P_3&=\{|b-(7/20-i/100)|\le83/1000\},\\
 P_4&=\{|b-(3/10-13i/250)|\le3/50\}.
\end{split}
\tag{3}
\]
They are strictly inside \(D_3,D_4\), of radii \(9/100,8/125\),
and contain \(A_3,O_3,A_4,O_4\) in their respective types.
Thus a full-disk conclusion includes every relevant clipping
chord without omitting it.

The sole sign to decide is the harmonic function
\[
 m(b)=\Im y(b)+\frac{\log(10/7)}{2\pi}.
 \tag{4}
\]
It satisfies \(m\le0\) exactly when
\(|e^{-2\pi iy}|^2\le49/100\). For each disk separately:

* If every closed boundary cell has a certified strictly
  positive margin, the harmonic minimum principle proves
  \(m>0\) throughout that disk. All actual references with
  the external input in that disk are excluded from the
  deeper-radius hypothesis.
* If every cell has a strictly negative margin, the harmonic
  maximum principle proves \(m<0\) throughout that disk.
  The deeper-radius source estimate then covers every
  otherwise eligible actual reference with that input type.
* Mixed signs, any inconclusive cell, or any failed/unprocessed
  cell gives no whole-disk sign conclusion. Individual
  certified boundary signs are retained as half-chain
  information only. A point on a containing circle need not
  belong to an actual clipped input domain, and even a
  parameter in that domain need not be realized by a knot.

No action, dilogarithm, finite-source rate, or knot invariant
is evaluated. The exact right cap/suffix must still be
identified for any proposed individual knot instance.

## 2. Seven original logarithmic equations and their Jacobian

Put \(j(w)=\Log(2\sin\pi w)\), with the original regular-strip
branch. The gradients of (2) are exactly
\[
\begin{split}
f_e={}&-j(e-u)+j(e+a)+i\pi(u-a),\\
f_a={}&j(e+a)+j(a+p)-2j(a)+i\pi(p-e),\\
f_u={}&2\Log\cos\pi u+\Log\sin\pi(e-u)
                         -3\Log\sin\pi u+i\pi e,\\
f_p={}&j(a+p)+j(p+y)-3j(p)+i\pi(a-y+p-1/2),\\
f_y={}&j(p+y)+j(y+s)-3j(y)+i\pi(s-p+y-1/2),\\
f_s={}&j(y+s)+j(s+z)-2j(s)+i\pi(y-z),\\
f_z={}&j(s+z)+j(z+b)-2j(z)+i\pi(b-s).
\end{split}
\tag{5}
\]
These are zero-logarithm-lift equations, not exponentiated
substitutes. The first five are the original cap-\(34\)
equations with their external input now the variable \(s\).
The last two are the own-three block in
[ordinary localization, equation (6)](research_mixed_cyclic_critical_localization.md).

Write \(C(w)=\pi\cot\pi w\) and
\(D(u)=\pi(2\tan\pi u+3\cot\pi u)\). In the ordering (1),
the complete nonzero Jacobian entries are
\[
\begin{array}{c|l}
ee&-C(e-u)+C(e+a)\\
ea=ae&C(e+a)-i\pi\\
eu=ue&C(e-u)+i\pi\\
aa&C(e+a)+C(a+p)-2C(a)\\
ap=pa&C(a+p)+i\pi\\
uu&-D(u)-C(e-u)\\
pp&C(a+p)+C(p+y)-3C(p)+i\pi\\
py=yp&C(p+y)-i\pi\\
yy&C(p+y)+C(y+s)-3C(y)+i\pi\\
ys=sy&C(y+s)+i\pi\\
ss&C(y+s)+C(s+z)-2C(s)\\
sz=zs&C(s+z)-i\pi\\
zz&C(s+z)+C(z+b)-2C(z).
\end{array}
\tag{6}
\]
The sole external derivative is
\[
 f_b=\gamma e_6,\qquad
 \gamma=C(z+b)+i\pi
       =\frac{2\pi i}{1-e^{-2\pi i(z+b)}}.
 \tag{7}
\]
The vector \(e_6\) uses zero-based indexing. The shared output
\(y\) has zero-based index 4.

## 3. Fixed inventory, starts, precision and inclusions

There are exactly 512 closed angular cells on each circle,
in the order \(P_3\) then \(P_4\), with indices \(0\le k<512\):
\[
 I_k=[2\pi k/512,2\pi(k+1)/512],\quad
 \theta_k=(2k+1)\pi/512,\quad \omega=\pi/512.
 \tag{8}
\]
All cell endpoints, including the common periodic endpoint,
are retained. Arb encloses the exact sine, cosine and \(\pi\)
values. There is no sampled replacement for a cell.

Use 256-bit ball arithmetic throughout. Every cell starts
independently from the same exact rational proposal
\[
\begin{split}
v_0=(&2/5+i/100,\quad 7/20-i/100,\quad23/100+i/20,\\
     &3/10-13i/250,\quad3/10-13i/250,\quad
                         7/20-i/100,\quad7/20-i/100).
\end{split}
\tag{9}
\]
The first five entries are the old prescribed typed-center
proposal, and the last two are the type-three disk center.
No saved root value supplies or updates this proposal.
At the exact external circle midpoint perform exactly 24
Newton proposal steps. After each step round each coordinate
to the exact rational represented by its binary64 midpoint.
These values only propose a root; there is no early success
stop or certificate from their residual alone.

Round the final midpoint Jacobian inverse in the same way
to a fixed exact rational matrix \(A\). Require it nonsingular.
Use that same matrix in two prescribed disk inclusions:
radius \(r_0=2^{-30}\) for the midpoint, and radius
\(r_1=1/256\) for the whole external cell.
For the center \(v_k\), parameter enclosure \(B\), and
Cartesian squares \(\mathcal Q_r\) containing the seven
complex disks, require for every row
\[
 k_i=\sum_j|(I-Af_v(\mathcal Q_r;B))_{ij}|<1,\qquad
 |(Af(v_k;B))_i|+rk_i<r.
 \tag{10}
\]
The disk contraction follows by integrating the derivative
on complex line segments. The squares only enclose the
derivative domain; they do not change the norm in (10).
The second inclusion is uniform for every parameter in
the closed angular cell.

Both inclusions must pass the same original guards:
\[
\begin{gathered}
.33<\Re e<.47,\quad-.09<\Im e<.08,\\
.21<\Re u<.25,\quad.01<\Im u<.10,\\
.23<\Re a,\Re p,\Re y,\Re s,\Re z<.45,\qquad
|\Im a|,|\Im p|,|\Im y|,|\Im s|,|\Im z|<.12.
\end{gathered}
\tag{11}
\]
The complex disks for \(a,s,z\) lie inside \(D_3\);
those for \(p,y\) lie inside \(D_4\). Membership uses
center distance plus the disk radius. The full external
cell enclosure stays inside its original larger typed disk.
All single and shifted primitive arguments
\[
e,a,u,p,y,s,z,b,\quad
1/2-u,e-u,e+a,a+p,p+y,y+s,s+z,z+b
\]
have real parts strictly between zero and one.
In addition \(0<\Re u<1/2\) and \(0<\Re(e-u)<1/2\)
retain the original auxiliary sine/cosine branches.
The old common-chamber uniqueness identifies the certified
zero with (2). No root sheet is selected from polynomial
equations alone. No extra independent height box is imposed.

Every failed proposal, guard, inversion or inclusion is
recorded. Continue only to the next already prescribed
cell, using (9) anew. No failure changes a setting.

## 4. Neumann response and the harmonic margin on the whole cell

Use the uniform inclusion, with its same rational \(A\).
Put \(H=f_v(v_*(b);b)\), \(E=I-AH\),
\(k=\max_i k_i<1\), and
\[
                 M_A=\max_j|A_{j6}|.
\]
All maxima use outward upper endpoints. Differentiating
the original equations gives \(Hv'=-\gamma e_6\), whence
\[
 v'=-\gamma Ae_6+Ev',\qquad
 \|v'\|_\infty\le\frac{|\gamma|M_A}{1-k}.
 \tag{12}
\]
In particular
\[
 y'(b)=-\gamma A_{46}+\varepsilon,\qquad
 |\varepsilon|\le
 r_{\rm resp}:=\frac{|\gamma|k_4M_A}{1-k}.
 \tag{13}
\]
This is also the row form of
\(H^{-1}=A+E(I-E)^{-1}A\).
It uses no inverse of a wide interval Jacobian.
The denominator in (7) is checked nonzero on the full
uniform box.

For the circle center \(b_\nu\), the exact angular
derivative is \(b_\theta=i(b-b_\nu)\), of modulus
\(\rho_\nu\). Therefore
\[
 \frac{dm}{d\theta}
   =\Im[-\gamma A_{46}b_\theta]
        +[-\rho_\nu r_{\rm resp},\rho_\nu r_{\rm resp}].
 \tag{14}
\]
The sign is the imaginary part, not a real action derivative.
The external-circle enclosure, uniform root box and (13)
give an outward interval for (14). If \(L\) is an upper
bound for its absolute value, the full cell margin lies in
\[
              m_{\rm midpoint}+[-\omega L,\omega L].
 \tag{15}
\]
The midpoint margin uses the \(r_0\) root box and the
original constant in (4). Also record the direct \(r_1\)
height enclosure plus that constant. The cell's asserted
sign is taken from (15); the direct enclosure is an audit
bound, not a license for another adaptive test.

A margin is positive only if its lower endpoint is positive,
negative only if its upper endpoint is negative, and otherwise
inconclusive. Midpoint signs are recorded separately and do
not substitute for whole-cell signs. All 1,024 cells are
attempted regardless of earlier signs.
The per-disk conclusions are exactly those in Section 1.
When all 512 cells of one disk complete their validated
inclusions and transports, also record the minimum of the
exact outward lower endpoints in (15) and the maximum of
its exact outward upper endpoints. The harmonic minimum
and maximum principles make that pair an enclosure of
\(m\) on the entire disk, even when it straddles zero.
This aggregation performs only comparisons of bounds
already produced by the prescribed tests. It is withheld
if any cell fails or is unprocessed, and no conclusion
survives a provenance invalidation.

## 5. Frozen provenance, single output and review gate

Checker:
[check_mixed_cap_343_radius_coverage.py](../experiments/check_mixed_cap_343_radius_coverage.py).
Manifest: repro/protocols/research-mixed-cap-343-radius-coverage.json.
Exclusive output:
repro/results/research-mixed-cap-343-radius-coverage-attempt01.json.

The manifest binds this protocol and checker, all named
original branch/action/domain sources, the primary open-end
and ordinary-block certificates and their independent replays,
the common Hessian records, and their dependencies transitively.
It records the complete settings (3), (8)--(11), the exact
start (9), and separate root and peer review approvals.
Metadata/provenance validation does not replay any old
mathematical calculation. The checker imports no old checker.

The output retains every rational proposal and inverse,
both complete inclusion inventories and root boxes, all
guards, the exact external-cell labels, the Neumann row
constants, derivative and margin intervals, each sign,
all failures/exceptions and unprocessed cases, operation
counts, and initial/final dependency hashes. Actions,
dilogarithms, wide interval Jacobian inversions, adaptive
subdivisions, retries and saved-root evaluations have
explicit zero counts. The output is opened exclusively.
Changed input or manifest bytes invalidate the run.

Only a completed, fully validated, single-sign boundary
inventory licenses a whole-disk sign classification.
Mixed or inconclusive results require a separately designed
and reviewed future argument; they trigger no refinement
or second execution here.
