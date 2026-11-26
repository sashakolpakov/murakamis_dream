# Ordinary own-three support at the left cutoff

Research certificate design, 5 November 2026. The proposed comparison
keeps the own-type-three cutoff at \(3/20\). The acceptance test covers
all horizontal plateau targets without a target grid, on the ordinary
boundary of each reduced reference bidisk. Only a completed six-face
record with status “passed” proves the universal assertion below.
A bounded pilot or a record with pending cells does not.

## 1. The original reference and target comparison

Let the two reduced disks be
\[
 P_3=\{z:|z-(7/20-i/100)|\le83/1000\},\qquad
 P_4=\{z:|z-(3/10-13i/250)|\le3/50\}.
 \tag{1}
\]
For external flags \((\alpha,\beta)\in
\{(0,0),(0,1),(1,1)\}\), take
\((A,C)\in P_{3+\alpha}\times P_{3+\beta}\).
The original own-three two-leg root satisfies
\[
 \begin{split}
 g'(s+t)+g'(s+A)-2g'(s)+2\pi iA&=0,\\
 g'(s+t)+g'(t+C)-2g'(t)+2\pi iC&=0.
 \end{split}
 \tag{2}
\]
Use its original zero lifts and the existence, uniqueness and
response supplied by the
[reduced-disk theorem](research_mixed_reduced_disk_conditional_packets.md).
The four individual arguments lie in
\(Q=[.23,.45]+i[-.12,.12]\).

The conditional orientations are
\((s_*,a,b,\eta)=(s,A,t,\alpha)\) and
\((t,C,s,\beta)\). In either orientation the allocated phase is
\[
 \begin{split}
 F(v;a,b)&=g(v+a)+g(v+b)-2g(v)
              -(1+\eta/2)g(a)-g(b)+2\pi iav,\\
 \phi(a,b)&=F(s_*;a,b).
 \end{split}
 \tag{3}
\]
In particular the own factorial power is two, the second outer
coefficient is one, and there is no second type-four halfweight.
The first halfweight is still present when \(\eta=1\).

Set \(Z=(a,b)=U+iH\), \(I=[11/50,9/20]\),
\(\ell=3/20\) and \(\kappa=1/2500000\). Define
\[
 \begin{split}
 B_Z(X)&=\Re\phi(Z)+\Re\phi'(Z)\cdot(X-U)
                                -\kappa\|X-U\|^2,\\
 D(Z,X)&=\Re F(\ell;X+iH)-B_Z(X),\qquad X\in I^2 .
 \end{split}
 \tag{4}
\]
All shifted real arguments at this cut lie in \((0,1)\).
Thus \(\Re F(\ell;X+iH)\) is exactly the complete allocated
real-row rate. The chirp and both actual outer allocations are
retained.

**Certificate assertion.** A complete run of the acceptance test in
Sections 2--4 proves, in both orientations and on all three products,
\[
                            D(Z,X)<-1/2000
                          \qquad(X\in I^2).
 \tag{5}
\]
This is an ordinary-reference assertion. The auxiliary first
type-four factorial allocation is a formal function if its height
is positive; its eventual physical Fourier interpretation retains
the actual unselected negative-height hypothesis.

The actual branch satisfies
\(-D_U^2\Re\phi\succ(\pi/8)I_2\).
The old matched-reference left-cut gap is \(1/1000\) on the
whole reduced product. Hence the
[reference-boundary principle](research_mixed_horizontal_tail_reference_boundary.md)
reduces (5) to
\[
 (\partial P_{3+\alpha}\times P_{3+\beta})
       \cup(P_{3+\alpha}\times\partial P_{3+\beta}).
 \tag{6}
\]
The maps \((A,C)\mapsto(A,t(A,C))\) and its other orientation
are locally invertible by the original nonzero response. Since
\(1/1000>1/2000\), the matched gap pays the possible interior
reference maximum. No distinguished-boundary maximum principle
is substituted for (6).

## 2. Uniform scalar target curvature

For \(x\in I\), \(|h|\le3/25\), \(\lambda\ge1\), put
\[
               f(x)=\Re\{g(x+\ell+ih)-\lambda g(x+ih)\}.
 \tag{7}
\]
Let \(C=\cos(3\pi/20)\), \(S=\sin(3\pi/20)\),
\(K=\cosh(2\pi h)\) and \(T=\cos(2\pi x+3\pi/20)\).
Then
\[
 -1\le T\le0,\quad 1\le K<4/3,\quad
                 7/8<C<9/10,\quad S>9/20.
 \tag{8}
\]
For example \(\pi<22/7\) and \(\cos v>1-v^2/2\)
give \(C>7/8\). At \(v=471/1000<3\pi/20\),
the inequalities
\(\cos v<1-v^2/2+v^4/24<9/10\) and
\(\sin v>v-v^3/6>9/20\) prove the other two bounds.
The hyperbolic estimate is the existing outer-strip bound.

The same exact cotangent subtraction as in the
[own-four support proof](research_mixed_four_left_cut_support.md)
gives
\[
 \Re\{\cot\pi(x+ih)-\cot\pi(x+\ell+ih)\}
 =\frac{2S(C-KT)}{T^2-2CKT+C^2+K^2-1}
 \ge\frac{2S}{C+K}.
 \tag{9}
\]
The denominator is a product of positive cotangent denominators.
After multiplying by positive quantities, the last comparison is
\((1+T)\{1-T-K(K-C)\}\ge0\), valid because
\(K(K-C)<11/18<1\). Since the extra
\((\lambda-1)\pi\Re\cot\pi(x+ih)\) is nonnegative,
\[
                      -f''(x)>\frac{27\pi}{67}>\frac65 .
 \tag{10}
\]
The last comparison already follows from \(\pi>3\).
Consequently the two-target Hessian of \(D\) is diagonal and at
most \(-c_*I_2\), where \(c_*=6/5-2\kappa>0\).

## 3. Correlated whole-cell acceptance

Each face in (6) is covered by the full cube
\((\theta,\rho,\psi)\in[0,1]^3\), with circle variable
\(c+r e^{2\pi i\theta}\) and other disk variable
\(c+\rho r e^{2\pi i\psi}\). This includes the disk center.
The exact derivatives are \(2\pi i(z-c)\) for the circle,
and \(r e^{2\pi i\psi},2\pi i\rho r e^{2\pi i\psi}\)
for the disk.

The original interval affine-root self-map, tiny midpoint
original-log lift and weighted Neumann response are invoked with
own flag zero throughout. In particular the Jacobian and nonlinear
remainder use own coefficient two, not three.
For a fixed rational trial \(\widehat X\in I^2\), write
\(\delta=\widehat X-U\), \(P=\phi'(Z)\),
\(P_c=F_X(\ell;\widehat X+iH)\) and \(H_\phi=\phi''(Z)\).
Then
\[
 D_U=(-\Re H_\phi-2\kappa I)\delta,\qquad
 D_H=\Im\{P-P_c+H_\phi\delta\}.
 \tag{11}
\]
The Hessian is the exact complex Schur complement
\[
 H_\phi=F_{XX}-F_{Xs}F_{ss}^{-1}F_{sX}.
 \tag{12}
\]
Here \(F_{ss}=g''(s_*+a)+g''(s_*+b)-2g''(s_*)\);
the mixed vector is
\((g''(s_*+a)+2\pi i,g''(s_*+b))\), and the two
outer diagonal entries are
\(g''(s_*+a)-(1+\eta/2)g''(a)\) and
\(g''(s_*+b)-g''(b)\).
Both the asymmetric chirp and all reference cancellations in (11)
are retained.

The original root response and the polar derivatives give the
three real parameter derivatives \(D_{\xi_j}\).
The target slope interval at the trial is
\(\beta=\Re P_c-\Re P+2\kappa\delta\).
By (10), a rigorous upper bound on the full target square is
\[
 D_0+\sum_{j=1}^3 h_j\sup|D_{\xi_j}|
  +\sum_{i=1}^2
    \max_{d\in[11/50-\widehat X_i,\,9/20-\widehat X_i]}
           \{\beta_i d-\tfrac12c_*d^2\}<-1/2000 .
 \tag{13}
\]
Here \(D_0\) is the direct interval phase value on the tiny
original-log midpoint disk and \(h_j\) are parameter halfwidths.
Each one-sided quadratic maximum uses zero, its clipped stationary
point or its endpoint. Interval slopes are maximized according to
the sign of \(d\). Floating target optimizers propose rational
trials only. Every term deciding acceptance is evaluated outward.

## 4. Pilot, full coverage and replay

The certifier is
[certify_mixed_three_left_cut_support.py](../experiments/certify_mixed_three_left_cut_support.py).
It binds the complete old source author and saved replay, their
current dependencies, this proof and its own code, together with
the analytic reference-boundary, contour and target-optimization
inputs. It does not rerun the old root cover.

The pilot checks only the external-three/three circle-first face,
with both orientations, at a cap of 511 visited nodes or 60 seconds.
This family has the weakest recorded matched left-cut floor among
the three own-three families. The pilot has no universal scope:
accepted leaves and every pending box are retained explicitly.

For a full run, all three unordered external type pairs and both
ordinary boundary faces must pass. The code cyclically splits the
three parameter axes at exact rational midpoints. It appends left
then right and pops right first. Every saved leaf contains the
original affine root witness and both rational target pairs.
A complete face exhausts its stack with \(2L-1\) nodes for \(L\)
leaves; a complete six-face record has \(2L_{\rm total}-6\) nodes.
The swapped orientation covers the exchanged ordered type case
by the exact symmetry of (2). No equal-type face is skipped.

Saved replay reconstructs the identical trees and must accept every
saved leaf without a root proposal, a target proposal or refinement.
All source hashes and the author input hash are checked again at
completion. Displayed decimal extrema do not decide acceptance.
An interrupted or failed run preserves completed faces and the
current tree with all pending cells and proves no missing coverage.

After a complete acceptance of (13), the boundary principle proves
(5) on all reduced products. For actual ordinary references, the
[half-index contour theorem](research_mixed_half_index_contour.md)
and the actual-height right-tail endpoint theorem then reduce the
finite upper maximum to
\[
              C_\tau N^A
                   \exp N\{\max(B,R(1/2),R(1))+\tau\}.
 \tag{14}
\]
This deduction retains all original rows, current orientations,
halfweights and both level parities. The half row, revived last
row and different terminal graphs remain separate; no full-source
dominance, moving-root packet or transverse derivative claim is
made by this certificate.
