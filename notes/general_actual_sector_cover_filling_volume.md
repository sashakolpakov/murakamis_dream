# Full volume from finite covers of the actual source sectors

31 October 2026. A sufficient theorem for a fixed marked plat. Universal applicability to every eligible plat remains open.

## 1. The theorem and its geometric scope

Fix an original certified simple-white augmented plat $D$, with $R$ ports,
its prescribed MAIN mark, and a fixed choice of half twists giving one main
knot component. Retain the original two protected face variables at zero
and every ordinary coefficient target $d=N-1$. Let

$$
\Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}
$$

be its complete augmented volume rate. The certification and geometric
normalization are those of the [complete source theorem](general_fejer_endpoint_source_volume.md)
and the [whole-CROSS filling theorem](general_all_cross_long_filling_volume.md).

At each port use the actual local labels CROSS, LEFT and RIGHT. A one-sided
label whose overloaded middle is protected has zero source and is omitted.
A **branch** $B$ assigns a nonempty subset $S_{B,e}$ of the remaining labels
to each port. Thus it denotes a Cartesian set of actual label strings.

For positive shared ordinary radii $L$, put

$$
\begin{aligned}
X_e(L)&=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),\\
A_{e,L}(L)&=\max\{\log c_e,\ Q(x_e,b_e,y_e)+\tfrac12\log c_e\},\\
A_{e,R}(L)&=\max\{\log b_e,\ Q(x_e,c_e,y_e)+\tfrac12\log b_e\},\\
G_B(L)&=\sum_e\max_{s\in S_{B,e}} A_{e,s}(L)
                  -\sum_{f\text{ ordinary}}\log L_f,
\qquad A_{e,C}=X_e.
\end{aligned}\tag{1}
$$

Here $x_e,b_e,c_e,y_e$ are the original face coordinates, so a face appearing
at several ports has one common radius. The function $Q$ is the original
half-degree triangle potential, with its absolute normalization.

**Theorem.** Suppose a finite collection of branches covers every allowed
non-CROSS string, and each branch has a positive shared vector $L^B$ with

$$
G_B(L^B)<\Phi_D.\tag{2}
$$

Then there is a diagram-dependent $T$ such that, for every independently
chosen fixed signed full-twist vector satisfying $|p_e|>T$, the original
invariant obeys

$$
\boxed{\displaystyle
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|K_N\bigl(K_D(\mathbf p)\bigr)\right|
 =\operatorname{Vol}\bigl(S^3\setminus K_D(\mathbf p)\bigr).}
\tag{3}
$$

The limit includes both level parities. The twist vector and diagram are
fixed before $N$ tends to infinity. The right side is the smooth filled
hyperbolic volume, rather than the complete augmented volume $2\pi\Phi_D$.
All original framing and peripheral factors remain in the invariant.

## 2. Why a cover suffices

The global weighted local estimates used in the
[anchored theorem](general_anchored_shared_radius_filling_volume.md) hold
at every real spectral value and every face phase. Their rates are precisely
the three functions in (1), with the recorded odd central convention.
They are weighted value bounds; no coefficientwise one-sided majorant is
asserted.

Assign each non-CROSS string to one branch containing it. For a string in
branch $B$, perform the ordinary coefficient estimate on the single shared
torus with radii $L^B$. The local rate at port $e$ is at most the maximum in
(1). Subtracting the original face targets gives $G_B(L^B)+o(1)$. The
replacement of $(N-1)/N$ by one costs $o(1)$ because the witnesses are fixed.

There are finitely many strings and witnesses for fixed $D$. Hence (2)
gives a common strict exponential gap on the whole real spectral cube.
Overlapping branches cause no multiplicity problem: each string is assigned
once, and even a finite overcount would not change its exponential rate.
The same conclusion holds at both level parities.

The remainder has spectral degree at most $N-1$ in each coordinate.
The cosine Bernstein estimate extends its gap to a fixed sufficiently thin
complex spectral strip. Apply the existing source Cauchy estimate and three
integrations by parts in each Fourier coordinate. These retain the original
endpoint identities and second-derivative boundary currents and give a
summable product of inverse-square charge weights on entire original
domains. Thus the **whole** non-CROSS filling period remains strictly below
$\Phi_D$ in exponential rate.

The whole-CROSS theorem gives a nonzero full period of rate
$\Phi_D-O(\sum_e p_e^{-2})$, equal to the actual filled volume divided by
$2\pi$. Taking every fixed $|p_e|$ sufficiently large makes this rate larger
than the remainder bound. The full invariant has the same rate, proving
(3). This uses the entire charge sum and the existing full-domain transfer,
not a sharply cut infinite Fourier sum.

## 3. Relation to the simpler criteria

The triangle inequality $Q(x,t,y)\geq\tfrac12\log t$ gives the useful
identities

$$
\begin{aligned}
\max(A_C,A_L,A_R)&=\max(X,\log b,\log c),\\
\max(A_C,A_L)&=\max(X,\log c),\\
\max(A_C,A_R)&=\max(X,\log b).
\end{aligned}\tag{4}
$$

Terms with protected middle coordinates are omitted. For example,
$Q_b+\frac12\log c\leq Q_b+Q_c=X$, which proves the second identity.
These identities simplify a union of actual labels. They do not turn the
comparison atoms inside $A_L$ or $A_R$ into independent source polynomials.

The anchored criterion uses one LEFT or RIGHT anchor and all labels at
every other port. It has at most $2R$ branches. Splitting those branches
into smaller actual label sets can lower their costs; each new branch may
use its own shared face vector. The [certificate separation theorem](actual_shared_radius_certificate_separation.md)
proves this is a strict improvement for one fixed original marked source:
an anchored certificate is impossible there, but forty finer branches pass.

The strongest finite version uses one branch for every individual
non-CROSS string $\sigma$. Its sufficient condition is

$$
\inf_{L>0}\left[\sum_e A_{e,\sigma_e}(L)
                          -\sum_f\log L_f\right]<\Phi_D
\qquad\text{for every }\sigma\ne C^R.\tag{5}
$$

If the infimum is strictly smaller, some finite positive witness exists;
attainment is unnecessary. Since there are finitely many strings, (5)
would establish (3) for that diagram. Whether (5) holds for **every** eligible
original plat is the remaining universal question. Acyclicity of overloaded
middle edges and the existing endpoint volume theorem do not by themselves
prove it: the one-sided comparison allows fractional perspective flows.

## 4. Checkable input and scope

The theorem admits finite certificates: the original source incidence and
mark, a combinatorial branch cover, one positive rational vector per branch,
and strict interval bounds compared with a feasible complete triangle flow.
Numerical optimization can locate the witnesses, but is not needed to
verify them. The [portable forty-branch verifier](../experiments/audit_actual_sector_cover.py)
implements this distinction.

This criterion includes the balanced all-width families and the independently
deep [bridge-gap extensions](general_simultaneous_bridge_gap_filling_volume.md).
It does not assert that every knot of bridge number $k$, or every presentation
with long twist regions, has the required original geometric certificate or
passes (5). Those are coverage questions to prove, not assumptions hidden in
(3).
