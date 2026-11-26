# A fixed two-center diagnostic for the following-reference action

Protocol, 7 November 2026. This is a two-point diagnostic of the
original cap-initialized half-chain \(34\). It encloses the absolute
pre-Gram action at the two prescribed external centers, then compares
it with the proved complete seam and complementary-contour ceilings.
It is neither a parameter cover nor a whole-source theorem at those
centers. No mathematical evaluation is authorized until the root and
an independent peer have reviewed this protocol and its standalone
checker, and all final bytes are frozen in a manifest.

There is one run at one precision, two prescribed external points,
one fixed initial point for each, one fixed proposal count, one fixed
inclusion radius, and one exclusive output. Failures and inconclusive
comparisons must be retained. No refinement, retry, alternate center,
optimization, root search or automatic replay is permitted.

## 1. The complete half-chain action and its original equations

Use the original primitives of
[actual cap-phase entrance](research_mixed_alternating_cap_phase_entrance.md),
with \(J'=\Log(2\sin\pi z)\), \(g=J+i\pi(z-z^2)/2\).
The five unknowns, in this fixed order, are
\[
                         v=(e,a,u,t,z).
\]
For the external leg \(c\), define
\[
\begin{split}
 E(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)
                          +i\pi eu-i\pi(e-e^2)/2,\\
 P(v)&=E(e,u)+g(e+a)+g(a+t)+g(t+z)
                     -2g(a)-3g(t)-g(z)+2\pi iat,\\
 G(z,c)&=g(z+c)-2g(z)-2g(c)+2\pi izc,\\
 H(v;c)&=P(v)+G(z,c).
\end{split}                                                     \tag{1}
\]
This is exactly the original \(E+V_0+G+V_1+G\) action.
The requested value is \(\Re P(v_*(c))\), equivalently
\(\Re[H(v_*(c);c)-G(z_*(c),c)]\). Its constant is not reset
to a bulk value, and the final Gram action is explicitly subtracted.

Writing \(j=J'\), the original five equations are
\[
\begin{split}
 H_e&=-j(e-u)+j(e+a)+i\pi(u-a),\\
 H_a&=j(e+a)+j(a+t)-2j(a)+i\pi(t-e),\\
 H_u&=2\Log\cos\pi u+\Log\sin\pi(e-u)
                                      -3\Log\sin\pi u+i\pi e,\\
 H_t&=j(a+t)+j(t+z)-3j(t)+i\pi(a-z+t-1/2),\\
 H_z&=j(t+z)+j(z+c)-3j(z)+i\pi(c-t+z-1/2).
\end{split}                                                     \tag{2}
\]
All logarithms are the original regular-strip branches. Their zeros,
not zeros of exponentiated substitutes, are certified.

The Jacobian is obtained by differentiating (2). If
\(C(v)=\pi\cot\pi v\) and
\(D(u)=\pi(2\tan\pi u+3\cot\pi u)\), its nonzero entries are
\[
\begin{array}{c|l}
 ee&-C(e-u)+C(e+a)\\
 ea=ae&C(e+a)-i\pi\\
 eu=ue&C(e-u)+i\pi\\
 aa&C(e+a)+C(a+t)-2C(a)\\
 at=ta&C(a+t)+i\pi\\
 uu&-D(u)-C(e-u)\\
 tt&C(a+t)+C(t+z)-3C(t)+i\pi\\
 tz=zt&C(t+z)-i\pi\\
 zz&C(t+z)+C(z+c)-3C(z)+i\pi .
\end{array}                                                     \tag{3}
\]
The variable order in (2)--(3) is always \((e,a,u,t,z)\).

## 2. Two fixed points and one enclosure rule

The complete inventory is, in the indicated order,
\[
 c_3=7/20-i/100,\qquad c_4=3/10-13i/250.                \tag{4}
\]
These are the centers of the original typed disks. At each point
start independently from the same exact rational proposal
\[
 v_0=(2/5+i/100,\ 7/20-i/100,\ 23/100+i/20,\
                   3/10-13i/250,\ 3/10-13i/250).      \tag{5}
\]
Use 256-bit ball arithmetic and exactly 24 Newton proposal iterations.
After each iteration round every complex component to the exact
rational represented by its binary64 midpoint. These are proposals
only. There is no early success stop or change of the iteration count.
If an iteration cannot produce finite proposals, retain that case's
failure and proceed only to the other already prescribed case with
its original initial point; this is not a retry of the failed case.

Round the final point Jacobian inverse in the same fashion to an exact
rational matrix \(Y\). Perform exactly one inclusion test, with
complex disk radius \(r_0=2^{-30}\) in every coordinate. The
derivative enclosure uses Cartesian squares containing those disks.
Require \(Y\) invertible and, for every row,
\[
 \sum_j|(I-YH''(D))_{ij}|<1,\qquad
 |(Y\nabla H(v_0;c))_i|
    +r_0\sum_j|(I-YH''(D))_{ij}|<r_0.                 \tag{6}
\]
The fixed-point theorem then certifies a unique original-log zero
in that product of disks. The checker additionally verifies its
containing squares lie in the original common chamber:
\[
\begin{split}
 &.33<\Re e<.47,\quad -.09<\Im e<.08,\\
 &.21<\Re u<.25,\quad .01<\Im u<.10,\\
 &.23<\Re a,\Re t,\Re z<.45,
                      \quad |\Im a|,|\Im t|,|\Im z|<.12.
\end{split}                                                     \tag{7}
\]
It checks \(a\in\operatorname{int}D_3\) and
\(t,z\in\operatorname{int}D_4\), using center distance plus
the complex disk radius; all factorial and endpoint primitive
arguments in (1)--(2) must have real part strictly between zero and
one. The auxiliary sine/cosine arguments stay in their original
positive-strip continuations. It also records and checks
\(t,z\in\operatorname{int}O_4\), including their reduced
disk and height bounds, and \(1/2<e^{2\pi\Im z}<1\).

The established cap-initialized half-chain theorem gives existence
on both full typed input disks and uniqueness in (7). Thus the
certified zero is the actual \(34\) half-chain branch at (4).
This does not promote all independent incoming and outgoing boxes
to an actual reference family.

## 3. Exactly the requested rate comparisons

For each successfully certified root enclosure, evaluate outward
the original \(P,H,G\) of (1), and the radius
\(R=e^{2\pi\Im z}\). The primitive implementation is copied
explicitly, not imported or executed, from the reviewed
[six-variable diagnostic checker](../experiments/check_mixed_three_four_half_face_witnesses.py):
\[
 J(v)=\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi iv})}{2\pi i}
                                      +\frac{i\pi}{2}v(1-v).
                                                               \tag{8}
\]
Every argument in this evaluation is in the verified original strip.

The only two comparison margins are
\[
 \Re P-7/4,\qquad \Re P-\mathfrak C(R),                 \tag{9}
\]
where the already proved full-source ceiling is
\[
 \mathfrak C(R)=\frac{17539}{9600}-\frac{23}{64000}
                   -\frac6{25}\beta(R)+\frac{\beta(R)^2}{20},
 \qquad \beta(R)=\frac12\log\frac2{1+R^2}.            \tag{10}
\]
Retain the entire outward intervals, not midpoint signs. A margin
has verdict `positive` only when its lower endpoint is positive,
`negative` only when its upper endpoint is negative, and otherwise
`inconclusive`. A case proves its two-point diagnostic comparison
only when both margins are positive. A negative margin concerns
this sufficient ceiling comparison, not the actual finite source.
All cases and both margins are retained regardless of the first result.

Even two positive cases do not prove a uniform comparison on either
typed disk, a complete packet at the centers, a new attachment
asymptotic, or a knot-family result. They supply certified information
for choosing a later separately reviewed uniform proof route.

## 4. Frozen inputs and exclusive output

Checker: `experiments/check_mixed_three_four_following_action_centers.py`.
Manifest: `repro/protocols/research-mixed-three-four-following-action-centers.json`.
Output: `repro/results/research-mixed-three-four-following-action-centers-attempt01.json`.

Before execution the manifest must bind this protocol, the checker,
the exact finite-source and action references, the full original
half-chain existence/uniqueness theorem, the radial majorant, and
the original open-endpoint and ordinary bidisk certificates with
their completed independent replays. Every dependency listed by
the primary/replay records is bound and verified transitively.
Archived provenance records may be hashed without being promoted
to completed theorems. The manifest records the two independent
review approvals and all fixed settings (4)--(6).

The output saves every exact rational proposal center and inverse,
the original gradient residuals and inclusion rows, all five root
coordinate boxes, \(P,H,G\), the radius, both ceilings and both
margins, finite/inclusion/domain checks, operation counts, input
hashes, completed and unprocessed inventories, and every exception.
The output is opened exclusively and never overwritten. Inputs and
manifest are rehashed at the end; any change invalidates the run.
Only the root may execute the one reviewed frozen run. No computation
is authorized by creating or statically reviewing these files.
