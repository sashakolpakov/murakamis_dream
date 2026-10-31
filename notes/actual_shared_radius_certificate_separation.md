# A strict separation between shared-radius certificate classes

31 October 2026. Exact rational certificates and rigorous interval bounds.
Internal independent proof/code reviews and fresh replays passed.

The [finite-cover theorem](general_actual_sector_cover_filling_volume.md)
allows a shared positive radius vector for each branch of genuine source
labels. Here one original marked source provably fails the simpler anchored
test but passes a forty-branch refinement. This separates the certificate
classes without asserting that an actual quantum invariant exceeds volume.

## 1. The original source and an impossible anchor

Take width $k=3$, the first original top-cap mark, and the zero-based word

$$
(1,3,0,2,4,1,3,0,2,4,1,3,0,2,4,1,3).\tag{1}
$$

The original compiler gives $17$ ports and $19$ white faces. Faces $0$ and
$16$ are protected; all other faces have target $d=N-1$. The white sphere
has $34$ distinct triangular cells and $51$ edges, each incident to two
cells. The marked edge is MAIN. The existing labeled simple-packing
certificate therefore applies to this actual source.

Write $X_e=Q(x,b,y)+Q(x,c,y)$ and
$H_e=\max(X_e,\log b,\log c)$, omitting protected logarithms.
The RIGHT anchor at zero-based port $12$ has quartet $(0,11,16,14)$.
Its retained triangle has only one ordinary coordinate, so

$$
A_{12,R}(L)=\max\left(\log L_{11},
              \tfrac12\log L_{11}+\tfrac12\log L_{14}\right).
$$

Use $H_e$ at every spectator, as in the anchored criterion. The
[rational anchor certificate](../experiments/actual_shared_radius_anchor_obstruction_certificate.json)
contains $84$ nonnegative rational variables. At spectators $2,4,7$ it
assigns mass $\lambda_e$ to the complete pair of triangle rows and mass
$1-\lambda_e$ to the pure-$b$ endpoint. Other spectators retain both complete
rows. At the anchor it assigns loads $\beta$ to face $14$ and $1-\beta$ to
face $11$, with $0\leq\beta\leq1/2$ and zero entropy.

Each weighted triangle row has total mass $\lambda_e/2$. Every ordinary
face target is exactly one after including the pure-middle and anchor
loads; protected loads are zero. The verifier checks these rational
identities, both spectator rows, and the original compiler and mark.

For every shared vector $L$, the triangle Fenchel formula and
$\max(a,b)\geq\lambda a+(1-\lambda)b$ give

$$
C_{12,R}(L)\geq E_{\mathrm{flow}}.
$$

All logarithmic terms cancel by the exact face equations. This is weak
duality; it requires neither an attained optimizer nor an interchange of
an infimum and a supremum. A separate positive rational vector $L^{\rm up}$
gives the complete upper bound

$$
\Phi_D\leq\sum_eX_e(L^{\rm up})-\sum_f\log L_f^{\rm up}.
$$

Arb arithmetic at 192 bits, with 8,192 Fourier terms and the explicit
Lobachevsky tail bound $1/(2M)$, proves

$$
\begin{aligned}
E_{\mathrm{flow}}&>19.95975965735,\\
\Phi_D&<19.92324700353,\\
\inf_{L>0}C_{12,R}(L)-\Phi_D&>0.025.
\end{aligned}\tag{2}
$$

The certified excess actually exceeds $0.03651$. No shared vector, including
an escaping limiting sequence, can pass this anchor. The anchored theorem
remains a valid sufficient theorem; its applicability is not universal.

The spectator mixtures are comparison atoms of $H_e$. They are not one
fixed genuine LEFT/CROSS/RIGHT source sector. Thus (2) does not disprove a
universal fixed-sector estimate or the volume conjecture.

## 2. A complete forty-branch cover for the same source

Set $B=\{2,4,7,12\}$. Cover all actual non-CROSS strings as follows.

* For each nonempty subset $J\subseteq B$, require RIGHT on $J$, allow
  CROSS/LEFT on $B\setminus J$, and allow all labels elsewhere. This gives
  $15$ branches.
* If no port of $B$ is RIGHT, choose any surviving one-sided label as an
  anchor, allow CROSS/LEFT at the other ports of $B$, and allow all labels
  elsewhere. Omitting protected-zero sides leaves $25$ branches.

Every non-CROSS string belongs to a branch; none of these branches contains
the all-CROSS string. Overlap in the second group is harmless, since each
string can be assigned to its first eligible anchor.

The [branch certificate](../experiments/actual_sector_cover_certificate.json)
contains one positive rational shared vector for each of these forty
branches. Protected coordinates remain exactly $0$ and $16$. Each branch
uses the actual local label bounds, including
$\max(A_C,A_L)=\max(X,\log c)$ on CROSS/LEFT spectators.

The same file contains a feasible complete triangle flow with $83$
nonnegative rational corner variables. Every original triangle row sums
to $1/2$ and every ordinary face sums to one. Its entropy is a lower bound
for $\Phi_D$, independently of any numerical packing calculation.

The [portable verifier](../experiments/audit_actual_sector_cover.py) checks
the exact original incidence, all face equations, the full branch-cover
list, and every shared-radius inequality. At 192-bit precision, using
2,048 Fourier terms and the explicit tails, it proves

$$
\begin{aligned}
\Phi_D&>19.90751095350,\\
\max_B G_B(L^B)&<19.85303956990,\\
\min_B\bigl[\Phi_D-G_B(L^B)\bigr]&>0.04.
\end{aligned}\tag{3}
$$

The smallest certified gap exceeds $0.05447$. The refined criterion
therefore succeeds on the same source where the anchored criterion is
impossible. This is strict inclusion of **fixed marked-source certificate
classes**; unmarked knots may admit other presentations or marks.

Giving the first $(1,3)$ layer odd exponents and every later box even
exponents makes the original standard plat a knot. The finite-cover theorem
then proves the full original volume limit for all seventeen independently
sufficiently long fixed signed parameters. This is not a theorem for all
three-bridge knots.

## 3. Rigorous evaluation

For a half-degree triangle allocation $\alpha$, use

$$
C(\alpha)=\frac1\pi\sum_j
 \left[\Lambda(\pi\alpha_j)+\Lambda(\pi/2-\pi\alpha_j)\right],
\qquad \sum_j\alpha_j=\frac12.
$$

A summand is exactly zero at $0$ and $1/2$. For positive weighted triangles,
$Q$ uses the original angle formula
$\theta_j=\arctan(w_j/\sqrt{\sum_{i<j}w_iw_j})$ and the Legendre identity;
a one-positive-coordinate triangle is exactly a half logarithm. Every
Lobachevsky evaluation uses its absolutely convergent Fourier series and
an enclosing tail ball of radius $1/(2M)$.

Both [anchor](../experiments/audit_actual_shared_radius_anchor_obstruction.py)
and [cover](../experiments/audit_actual_sector_cover.py) verifiers read saved
rational data. Numerical optimization helped locate witnesses but is absent
from verification. Independent code/proof review and fresh replays passed.

A general bound for every genuine fixed sector remains open. The endpoint
volume theorem does not imply it: the weighted comparison permits concave
fractional mixtures that need their own global estimate.
