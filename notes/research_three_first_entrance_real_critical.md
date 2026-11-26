# The first entrance critical point on a larger real output interval

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This extends the actual first-entrance critical branch to real output
displacements of magnitude at most `.009`. The incoming critical wire
stays inside the already proved complex source disk of radius `.005`.
Both endpoint sectors and the real endpoint derivative signs are
certified with their parameter correlations retained. The result
supplies a central contour; estimates on the rest of the original
Fourier period remain separate source arguments.

## 1. Original phase and statement

Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad R=\frac1{200},
 \qquad k_0=\frac{4\pi}{21}(2\sqrt3-3i),\qquad D=5+\sqrt{21}.
 \tag{1}
\]
Let \(S_1\) be the phase of the original prepared source
\(v(-2)^TA_N^2h(z)\), and let \(\Phi\) be the original L40
retained kernel phase. All action constants and logarithmic lifts are
those of the [first-entrance theorem](research_three_first_entrance_source.md).
For real \(|b|\le9/1000\), write
\[
 y=x_h+b,\qquad U(z,y)=S_1(z)+\Phi(z,y),\qquad
 z_c(y)=\operatorname{crit}_z U(z,y),\qquad
 S_2(y)=U(z_c(y),y).
 \tag{2}
\]

**Proposition 1.** The original critical branch extends holomorphically
to a neighborhood of this closed real output interval, and
\[
 |z_c(y)-x_h|<R,\qquad
 9.3<-\Re S_2''(y)<9.8,\qquad
 \left|S_2''(y)/k_0+\sqrt{21}\right|<.18.
 \tag{3}
\]
For \(\epsilon=\pm1\), set
\(d_\epsilon=\epsilon R-(z_c(y)-x_h)\). Uniformly on the interval,
\[
 \begin{split}
 \Re(k_0D d_\epsilon^2)
       -\frac{94}{125}|k_0|\,|d_\epsilon|^2
       &>\frac1{2\cdot10^6},\\
 \epsilon\Re(k_0D d_\epsilon)
       -\frac{94}{125}|k_0|\,|d_\epsilon|&>0.
 \end{split}
 \tag{4}
\]
These are inequalities on the correlated critical-point image, not on
an independent disk enclosing its displacement.

## 2. Exact system and outward enclosure

Retain the original cap phase \(C(x,\tau)\) and period
\(P=-2\pi i C_\tau\). The three complex unknowns are the old
cap wire \(x\), its trace angle \(\tau\), and the new wire \(z\).
They solve
\[
 P(x,\tau)=0,\qquad C_x(x,\tau)+\Phi_x(x,z)=0,
 \qquad \Phi_y(x,z)+\Phi_x(z,y)=0.
 \tag{5}
\]
The exact Jacobian is the matrix in equation (10) of the
[critical-branch note](research_three_entrance_critical_branches.md#2-the-next-critical-point-on-the-true-output-disk).
For either retained factor, the selected algebraic root is
\[
 X=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 \alpha=X^{-1}-1,\quad\beta=Y^{-1}-1,
 \quad\Delta=1-2(\alpha+\beta)+(\alpha-\beta)^2,
 \quad
 (U_c,V_c)=\frac12(1+\alpha-\beta-\sqrt\Delta,
                            1-\alpha+\beta-\sqrt\Delta).
 \tag{6}
\]
The indices are \(i\log U_c/(2\pi),i\log V_c/(2\pi)\).
The checker retains these roots and the individual cap logarithms;
it does not solve only the exponentiated equations.

Partition \([-9/1000,9/1000]\) into exact rational intervals.
For one interval with midpoint \(b_0\) and half-width \(p\),
propose rational centers for (5) at \(y=x_h+b_0\), and give the
three unknowns radii
\[
                       (.05p,.15p,.24p).
 \tag{7}
\]
The same rational inverse-Jacobian preconditioner at the central
root is used for every interval. Only the third equation depends
explicitly on the output. Its displacement from the midpoint value
is at most \(\sup|\Phi_{xy}(z,y)|p\). The weighted Newton map
is checked on the entire complex polydisk and output interval:
each row has contraction less than \(1/4\), and the displacement
plus contracted radius is strictly smaller than its radius.
Thus every parameter in the interval has an actual unique root
in the certified polydisk. Numerical root solving merely chooses
the rational proposals.

The author certificate accepts 260 intervals after 392 visits.
Their rational endpoints give an exact multiplicity-one cover.
It checks (3)--(4) on every root enclosure, as well as the following
branch conditions: the old and new wires stay in
\((.14,.20)+i(.09,.12)\); the cap stays in
\((0,1.8)-i(.97,1)\); each retained index has real part in
\((.25,.45)\), imaginary part in \((-.03,.03)\), and its
pair has real sum in \((.5,1)\). Both discriminants have positive
imaginary part, both selected roots are in the lower left quadrant,
all denominator products have modulus below one, and all individual
cap logarithms stay in their original right-half-plane branches.

The unsummed phase Hessian on this common convex chamber has
strictly negative real part, by the
[joint-concavity theorem](research_three_vertex_joint_concavity.md).
Consequently the full complex gradient is injective: its difference
at two points is the integrated Hessian times their displacement,
and that integrated matrix is strictly accretive after negation.
This identifies the local roots on overlaps and with the previously
proved central branch. The implicit function theorem and the strict
compact margins give the asserted holomorphic neighborhood.

The outgoing derivatives are evaluated from the original Schur
complements. If
\[
 H=S_1''(z_c)+\Phi_{xx}(z_c,y),
 \qquad
 S_1''=\Phi_{yy}(x,z_c)
 -\frac{\Phi_{xy}(x,z_c)^2}
 {C_{xx}-C_{x\tau}^2/C_{\tau\tau}+\Phi_{xx}(x,z_c)},
 \tag{8}
\]
then
\[
 z_c'(y)=-\frac{\Phi_{xy}(z_c,y)}H,
 \qquad S_2''(y)=\Phi_{yy}(z_c,y)
                         -\frac{\Phi_{xy}(z_c,y)^2}H.
 \tag{9}
\]
The period-to-angular-derivative factor in (5) is kept in (8).
Outward evaluation proves (3); no finite difference is used.

## 3. The central contour and its real endpoints

**Corollary 2.** The two straight segments from \(x_h-R\) to
\(z_c(y)\), and from \(z_c(y)\) to \(x_h+R\), form a valid
oriented saddle contour for the actual product of the incoming
packet and the retained kernel. At either endpoint,
\[
 \Re U(x_h+\epsilon R,y)
           <\Re S_2(y)-\frac1{4\cdot10^6},
 \qquad
 \epsilon\Re U_z(x_h+\epsilon R,y)<0.
 \tag{10}
\]

The incoming packet is uniform on the genuine closed disk of radius
\(R\). The new
[union-domain retained packet](research_three_vertex_real_input_union.md)
applies on this entire contour by exact symmetry in the two wire
variables: its real input can be \(y\), while its disk output is
\(z\). This symmetry holds in the literal finite root-product sum,
including its symmetric deleted square. It is not continuation of a
pointwise asymptotic.

On the true incoming disk the phase estimate is
\(|h_1'|\le1/2\). The Taylor bound in the
[input-rectangle theorem](research_three_vertex_input_rectangle.md),
with the two variables exchanged, gives
\[
 \left|\Phi_{xx}(z,y)/k_0+5\right|
       \le18(|z-x_h|+|y-x_h|)\le.252.
\]
Hence throughout both segments
\[
             |-U_{zz}(z,y)-k_0D|\le.752|k_0|.
 \tag{11}
\]
The older defect `.6` on the smaller bidisk is not used here.
The first inequality of (4) and (11) give
\(\Re[-U_{zz}d_\epsilon^2]>1/(2\cdot10^6)\).
Integrating from the critical point proves strict decrease along
each ray and the first inequality of (10). The second inequality
of (4), integrated once with (11), proves the second inequality
of (10). Thus the real derivative signs are established separately
from the endpoint action losses.

The two rays belong to opposite Gaussian convergence sectors at
the central output, as checked independently. They remain so by
continuity and their strict sector margins over the connected real
interval. A local rounding therefore gives the full oriented
Gaussian coefficient. Convexity of the geometric disk keeps both
segments inside the actual incoming source domain.

All inequalities persist on a fixed open neighborhood of the real
output interval and for sufficiently small ordinary outside-color
deformations of \(-2\). The same statements then hold with fixed
ordinary derivatives by Cauchy estimates. Bounds on the external
real annuli, the rest of the Fourier period, and restoration of the
original corner are not supplied by this corollary.

## 4. Reproduction

```sh
python3 experiments/certify_three_first_entrance_real_critical.py --precision 192
python3 experiments/replay_three_first_entrance_real_critical.py --precision 256
```

The author record is
[research-three-first-entrance-real-critical.json](../repro/results/research-three-first-entrance-real-critical.json).
The independent replayer imports no author code or numerical root
solver. It evaluates the cap using the original cosine/asinh
derivatives and obtains the retained Hessian from the unsummed
two-index Schur complement, with five exact symbolic identities.
For sharper interval bounds it splits each stored interval into
eight exact subintervals. One explicit Newton step proposes rational
centers, and a fresh outward self-map proves each refined enclosure.
The replay record retains the exact cover, all branch checks, both
endpoint sectors and derivative signs, and the outgoing curvature
bounds. This is a critical-branch and central-contour certificate,
not a replacement for the complementary finite-source estimates.
