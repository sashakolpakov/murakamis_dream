# One fixed diagnostic for the real-transform half-face criterion

Protocol, 7 November 2026. The comparison (17) in
[the physical-middle reduction](research_mixed_three_four_physical_middle_reduction.md)
is sufficient, but not necessary, for the desired remainder bound.
This diagnostic tests whether its mandatory real private cuts already
exceed the original geometric action. It does not search for a
successful contour or prove an upper bound for the whole sum.

No mathematical evaluation is authorized until the root and an
independent peer have read this protocol, the source formulas below,
and the final standalone checker. Their final hashes and every
inherited source must then be frozen in a manifest. There is one
prescribed run, one fixed precision, one initial point and one output.
All unsuccessful outcomes must be retained.

## 1. Original geometric action and its six equations

Use variables \(z=(e_L,a,u_L,e_R,b,u_R)\). Write
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 P_\epsilon(e,t,u)&=F(e,u)+J(e+t)-J(t)-i\pi et-\epsilon g(e),\\
 W(a,b)&=J(a+b)-J(a)-J(b)+i\pi ab,\\
 \mathcal F(z)&=P_0(e_L,a,u_L)+P_1(e_R,b,u_R)+W(a,b)-g(b),\\
 g(z)&=J(z)+i\pi z(1-z)/2 .
\end{split}                                                    \tag{1}
\]
These are exactly equations (1), (13) of the existing cap cut-gap
and two-vertex first-collar notes. The quantity to be enclosed is
\(M=\Re\mathcal F(z_*)\), with its original additive normalization.

For a node \((e,t,u)\), outside argument \(d\), and own flag
\(\epsilon\), the three original gradient equations are
\[
\begin{split}
 f_e={}&-J'(e-u)+J'(e+t)-\epsilon J'(e)
          +i\pi\{u-t+\epsilon(e-1/2)\},\\
 f_t={}&J'(e+t)+J'(t+d)-(2+\epsilon)J'(t)
          +i\pi\{d-e+\epsilon(t-1/2)\},\\
 f_u={}&2\log\cos\pi u+\log\sin\pi(e-u)
                         -3\log\sin\pi u+i\pi e .
\end{split}                                                    \tag{2}
\]
Use \(d=b,\epsilon=0\) on the left and \(d=a,\epsilon=1\)
on the right. Direct differentiation of (1) gives (2); the
off-diagonal node coupling in the full Jacobian is
\(\mathcal F_{ab}=\pi\cot\pi(a+b)+i\pi\).
All logarithms are the original regular-strip branches.

The checker uses the fixed rational initial point
\[
 (.4+.01i,\ .35-.01i,\ .23+.05i,\
  .35-.035i,\ .30-.052i,\ .23+.05i).
                                                               \tag{3}
\]
At 256-bit precision it performs exactly 24 Newton proposal
iterations, rounding each component after each iteration to an
exact rational represented by its binary64 midpoint. These iterations
are proposals only; their convergence is not a certificate.
There is no alternate initial point, adaptive iteration count,
line search, root search, or restart.

At the final proposed center \(z_0\), round the point Jacobian
inverse in the same way to an exact rational complex matrix \(Y\).
Perform one inclusion test on the product of six complex disks of
radius \(r=2^{-30}\). Cartesian interval squares containing those
disks are used only to enclose the derivative. Require \(Y\)
invertible, the original regular-strip and common-chamber tests,
and
\[
 \max_j\sum_k|(I-Y\mathcal F''(D))_{jk}|<1,\qquad
 |(Y\nabla\mathcal F(z_0))_j|
    +r\sum_k|(I-Y\mathcal F''(D))_{jk}|<r
                                                               \tag{4}
\]
for every \(j\).
The contraction map \(z\mapsto z-Y\nabla\mathcal F(z)\)
then has a unique zero in that disk product.

Check the private and auxiliary boxes
\[
 .33<\Re e<.47,\quad -.09<\Im e<.08,\qquad
 .21<\Re u<.25,\quad .01<\Im u<.10,
                                                               \tag{5}
\]
the two original attached disks
\[
 |a-(.35-.01i)|<.09,\qquad |b-(.30-.052i)|<.064,
                                                               \tag{6}
\]
and the shared regular rectangle
\(.23<\Re a,\Re b<.45,\ |\Im a|,|\Im b|<.12\).
The proved uniqueness in the original open-word chamber identifies
the certified zero with the prescribed ordinary \((3,4)\) solution.
An arbitrary zero of exponentiated equations is not sufficient.

If any proposal, branch, domain, or inclusion check fails, record
that failure and the unprocessed inventory. Do not change the
precision, radius, center, or number of steps.

## 2. Six fixed lower witnesses, independent of the private main height

At the half face, the first-cap envelope satisfies
\[
 \overline Q(1/2)\ge -7J(1/4).
\]
Both real private cuts occur in every five-profile envelope, no
matter which main height is chosen. Use exactly the six pairs
\[
 e\in\{27/100,49/100\},\qquad t\in\{1/5,1/4,3/10\}.
                                                               \tag{7}
\]
For each pair evaluate outward
\[
 B(e,t)=-7J(1/4)+\lambda(e)+J(e+t)-J(e)
                         -J(1/2-t)-3J(t),\qquad
 \lambda(e)=\Re F(e,u_c(e)).
                                                               \tag{8}
\]
Thus the left side of the proposed half-face inequality is at least
every \(B(e,t)\), for every allowed private main height.

The two \(u_c(e)\) values use the existing explicit formula
\[
 u_c(e)=\pi^{-1}\arctan
       \frac{i+\sqrt{1-2e^{2\pi ie}}}{2}.
                                                               \tag{9}
\]
Keep the root with positive real part and the original arctangent
branch. Check the known private strip, \(0<\Re u_c<e\),
\(\Im u_c>0\), and the original logarithmic lift.
No optimization or private-root proposal is performed.

If the lower endpoint of any \(B(e,t)-M\) is strictly positive,
the sufficient inequality is false for every choice of private
main height in this five-profile method. This would require
retaining transform cancellation or improving the decomposition.
It would not disprove the desired source estimate or volume limit.
If no difference is strictly positive, the result is inconclusive.
A negative witness does not prove an upper bound for the envelope.
All six prescribed witnesses must be saved even if the first refutes
the criterion.

## 3. Frozen inputs and a single output

Checker:
experiments/check_mixed_three_four_half_face_witnesses.py.
Manifest:
repro/protocols/research-mixed-three-four-half-face-witnesses.json.
Output:
repro/results/research-mixed-three-four-half-face-witnesses-attempt01.json.

The manifest binds this protocol, the checker, the original source,
the ordinary critical geometry, the phase definitions, the physical
middle reduction, and the author/replay records for the critical
maps and endpoint rectangle. Every dependency listed in those
records must be checked transitively against its current bytes.
The primary records must be complete and passed; their replay
input hashes must match their authors. Archived partial records,
if present only as provenance, are bound without being promoted
to completed theorems.

The output records the exact rational proposal centers and inverse,
the entire inclusion test, all six geometric coordinate boxes, the
action enclosure, the two explicit private critical points, every
witness and comparison, operation counts, input hashes and verdict.
Exceptions save the completed prefix and remaining inventory.
An existing output must never be overwritten. The run has no
parameter subdivision, new source cover, changed exclusions,
alternative private height, adaptive refinement, second attempt,
or automatic replay.
