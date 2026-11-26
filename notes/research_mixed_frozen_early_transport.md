# Raising the remaining coordinates while early coordinates stay fixed

Research reduction, 4 November 2026. The endpoint estimate and the
transport implication below are proved from the stated inputs. The
local derivative hypothesis in Section 3 is open. Numerical diagnostics
are recorded separately and are not a proof of that hypothesis.

Use the original phases, selected contour, and cutoffs of
[the earlier selected contour](research_mixed_early_selected_transport.md).
Let \(E=[.1,.12]\), \(P=[.22,.45]\), and consider targets
\(x\in[.1,.45]^m\). Denote the set of early positions by
\(B=\{j:x_j\in E\}\). We assume \(B\ne\varnothing\).
All cyclic incidences, including repeated indices in lengths one and
two, retain their original meaning.

## 1. Why an isolated gap is left fixed

Let
\[
 I=\{j\notin B:j-1\in B\text{ and }j+1\in B\}.            \tag{1}
\]
These are the positions between two early positions. Both blocks
incident to such a position are already covered by the
[early block estimate](research_mixed_early_transition_support.md),
even if its own coordinate lies between .12 and .22.

There is also an explicit reason not to force it to increase. In the
three-cycle with types \((3,4,3)\), take the real targets
\[
                         (.1,.219,.1).                      \tag{2}
\]
Every contour height is zero, for every permitted selection. Keeping
the first and third coordinates fixed makes every height stay zero
as the middle coordinate varies. The derivative of the true rate is
therefore
\[
 \Re\{\partial_2\phi_{01}(.1,.219)
                    +\partial_1\phi_{10}(.219,.1)\}
                              <-\frac3{20}.                 \tag{3}
\]
The two original-logarithm root self-maps enclose this derivative
between \(-.158611\) and \(-.158610\). The selected correction
at zero height is zero, since \(\Re g(x)<0\) for
\(0<x<1/2\). Thus (3) applies whether the middle position is
selected or unselected. It disproves the unrestricted minimum-raising
argument, not the source bound or the volume identity.

We leave \(B\cup I\) fixed and raise only
\(A=\{0,\ldots,m-1\}\setminus(B\cup I)\).

## 2. The enlarged endpoint region is already controlled

Suppose every position in \(A\) belongs to \(P\), while the
positions in \(I\) may remain anywhere in \([.12,.45]\).
The full true rate has the same bound
\[
                         F_S(x)\le M-\frac{n_B}{1000}        \tag{4}
\]
as in the [early/plateau assembly](research_mixed_early_plateau_clusters.md),
where \(n_B\) counts blocks incident to \(B\).

Here is the complete additional argument. Treat every position outside
\(B\) as a plateau position for the incidence count. A position in
\(I\) has two early neighbors and hence no plateau/plateau block.
Every block incident to it has an endpoint in \(E\), with its other
real coordinate in \([.1,.45]\), so the stronger early block theorem
applies. Every actual plateau/plateau block has both endpoints in
\(A\), where their real coordinates are in \(P\). Thus every
local bound and every assigned credit in the early/plateau proof
remains valid. Neither the unique-credit count nor its four reset
fees change. This proves (4), including lengths one and two.

## 3. The local inequality still needed

Write \(N(j)=\{j-1,j,j+1\}\) for a closed cyclic neighborhood.
For this fixed set \(B\), define
\[
 d_j=
 \begin{cases}
 c_j,&j\notin S\text{ and }N(j)\cap B=\varnothing,\\
 0,&\text{otherwise},
 \end{cases}
 \quad c_j=\Im r_j,
 \qquad G_j=\partial_{z_j}\Phi.                            \tag{5}
\]
This is a coefficient of the height derivative, not the actual
target height. A selected height is constant along the proposed
path, because every moving coordinate is at least .12 and its fast
cutoff is already one. An unselected height whose neighborhood meets
\(B\) is also constant: the early cutoff is no larger than any
moving cutoff. No neighborhood disjoint from \(B\) contains an
isolated fixed position in \(I\), because both neighbors of such
a position lie in \(B\).

At a position \(i\in A\) attaining the minimum of the moving
coordinates, define
\[
 D_i^B=\Re G_i+
     \sum_{j\in(i-1,i,i+1)}
             \min\{-\tfrac{25}{3}d_j\Im G_j,0\}.           \tag{6}
\]
The sum has three terms with cyclic multiplicity. The missing
uniform hypothesis is
\[
 D_i^B\ge0\quad\text{whenever }i\in A\text{ is a moving
 minimum with }x_i\in[.12,.22].                             \tag{7}
\]
Unlike an isolated fixed position, such an \(i\) has at most one
early neighbor. Equation (7) is not implied by the existing 192
unselected or 78 constant-selected tests: neighboring heights may
now be fixed at intermediate fractions, and their coefficients
\(d_j\) may vanish for a different reason.

**Conditional proposition.** If (7) holds for every configuration
encountered, then all contributions with the fixed nonempty early
set \(B\) satisfy the finite bound
\[
                    C N^a e^{N(M-1/2000)}                  \tag{8}
\]
on this contour, including every original selection.

**Proof.** If \(A\) is empty, Section 2 applies immediately.
Otherwise raise its coordinates by
\(x_i(t)=\max\{x_i,t\}\), from their minimum to .22, while
leaving \(B\cup I\) fixed. Ties move together. Every responsive
unselected height has derivative \((25/3)c_j\) precisely when
its neighborhood meets the currently moving set. All other heights
have derivative zero.

For a selected moving coordinate, the previously proved inequality
\(-\Re g(x+ih)-2\pi h>3/40\), valid on
\([.1,.22]+i[0,.014]\), makes its true Fourier correction exactly
\(-2\pi h\). Its height is constant, so this correction is
constant. Selected coordinates not moving have both their real and
imaginary parts fixed. Thus the derivative of the full true rate
equals the derivative of \(\Re\Phi\).

Summing (6) over the currently moving positions can count a negative
height contribution more than once and can omit a positive one.
Consequently, almost everywhere along the path,
\[
             \frac{d}{dt}F_S(x(t))
                \ge\sum_{i\text{ moving}}D_i^B\ge0.        \tag{9}
\]
At the endpoint every position of \(A\) lies in \(P\), so (4)
bounds the endpoint and hence the initial rate. The entire path lies
in the established early cap and plateau polygons. The complete
finite-source estimates, a tolerance below \(1/(2000m)\), and
the fixed Jacobian bound give (8). \(\square\)

## 4. Diagnostic evidence and its scope

An initial bounded random test of the unrestricted flow found
negative derivatives when both neighbors were early; (2)--(3) give
a short rigorous instance of that obstruction. A second diagnostic
excluded those already controlled isolated positions. It tested
48,600 configurations covering all 243 five-position type/selection
patterns, with independently varying reference-height bounds. The
smallest observed value of (6) was approximately .02586. This is
evidence for testing (7) on complete domains. It proves neither
nonnegativity between the sampled points nor a new cyclic asymptotic.

The obstruction and endpoint incidence checks are reproduced by

```sh
python3 experiments/check_mixed_frozen_early_transport.py --precision 256
```

The separate diagnostic, whose output has no theorem-certifying status,
is reproduced by

```sh
python3 experiments/diagnose_mixed_frozen_early_transport.py
```
