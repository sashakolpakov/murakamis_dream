# A mixed-rule half-row certificate design

Research implementation design, 5 November 2026. This note accompanies
[certify_mixed_optimized_half_row_support.py](../experiments/certify_mixed_optimized_half_row_support.py).
It implements the
[optimized-envelope rule](research_mixed_half_row_optimized_envelope.md)
and preserves the completed part of the
[original design](research_mixed_half_row_support.md).
No numerical result is asserted here. A pilot is not a uniform
certificate; a full attempt follows review of the pilot.

## 1. Unchanged mathematical target

Use the original phase, primitive and logarithmic lifts:
\[
\begin{split}
 F(v;a,b)={}&g(v+a)+g(v+b)-(2+\epsilon)g(v)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi iav,\\
 \phi(a,b)&=F(s_*;a,b),\qquad Z=(a,b)=U+iH,\\
 I&=[11/50,9/20],\qquad \kappa=1/2500000,\\
 D(Z,X)&=\Re F(1/2;X+iH)-\Re\phi(Z)
          -\Re\phi'(Z)\cdot(X-U)+\kappa\|X-U\|^2.
\end{split}
\tag{1}
\]
For own flag \(\epsilon\in\{0,1\}\), external flags
\((\alpha,\beta)\in\{(0,0),(0,1),(1,1)\}\), and the original
coupled roots \((s,t)\), the two orientations remain
\[
       (s_*;a,b;\eta)=(s;A,t;\alpha),\qquad(t;C,s;\beta).
\tag{2}
\]
The disks are \(P_3=\{|z-(.35-.01i)|\le.083\}\) and
\(P_4=\{|z-(.30-.052i)|\le.060\}\). The requested bound is
\[
                         D(Z,X)<-1/2000,\qquad X\in I^2.
\tag{3}
\]
The original ordinary-boundary reduction is unchanged. Its matched
gap at row \(1/2\) uses the old entire right-tail entropy theorem
on the full reduced products, followed by the two fixed-row
subharmonic transfers. It does not extend the later \(.108\)
height theorem to the auxiliary range. All twelve faces, both own
flags and both orientations remain. Formal auxiliary halfweights
retain their original physical-height qualification.

## 2. Optimized-envelope leaves

Set \(V(Z)=\max_{X\in I^2}D(Z,X)\). The method proves separable
target curvature
\[
          D_{X_iX_i}<-c,\qquad c=14/5-2\kappa>0.
\tag{4}
\]
For a rational trial \(\widehat X\in I^2\), enclose the whole-cell
slopes by \([\underline\beta_i,\overline\beta_i]\). Every clipped
optimizer lies in
\[
 {\cal X}_i=I\cap
 \left[\widehat X_i-\frac{[-\underline\beta_i]_+}{c},
       \widehat X_i+\frac{[\overline\beta_i]_+}{c}\right].
\tag{5}
\]
The code constructs outward endpoints and intersects their enclosure
with \(I\). No floating sign, clipping or bound decision is used.

The tiny original-log midpoint root disk gives a direct deficit
interval and midpoint slopes
\([\underline\beta_i^0,\overline\beta_i^0]\). Put
\[
\begin{split}
 G_i^0=\max\Bigl\{&0,\
 \max_{0\le d\le9/20-\widehat X_i}
       (\overline\beta_i^0d-cd^2/2),\\
 &\max_{0\le d\le\widehat X_i-11/50}
       (-\underline\beta_i^0d-cd^2/2)\Bigr\},\\
 M_0&=\overline{D(Z_0,\widehat X)}+G_1^0+G_2^0.
\end{split}
\tag{6}
\]
Outward clipping of the scalar stationary point evaluates these
gains, giving \(M_0\ge V(Z_0)\) even at endpoint optimizers.

For \(P=\phi'\), \(H_\phi=\phi''\), \(d=X-U\) and
\(P_c=F_X(1/2;X+iH)\), the envelope derivative is
\[
\begin{split}
 D_U&=-\Re(H_\phi d)-2\kappa d,\qquad
 D_H=\Im(P-P_c+H_\phi d),\\
 V_{\xi_j}&=D_U\cdot\Re Z_{\xi_j}+D_H\cdot\Im Z_{\xi_j}
                          \quad\text{at }X=X^*(Z).
\end{split}
\tag{7}
\]
The value \(V\) is \(C^1\) on the admitted domain, including
clipping transitions, by the method's compactness/sandwich proof.
No optimizer derivative is used. The original two-root response
and complex Schur Hessian are unchanged.

Evaluate (7) over the original whole-cell reference/root boxes and
\(X\in{\cal X}\), obtaining intervals \({\cal G}_j\). For exact
parameter halfwidths \(h_j\), accept a leaf only if
\[
                   M_0+\sum_jh_j\sup|{\cal G}_j|<-1/2000.
\tag{8}
\]
There is no additional whole-cell target gain. A direct trial
deficit rigorously above the requested threshold stops the
attempt; an inconclusive upper interval permits only bounded
subdivision. Floating calculations propose rational witnesses and
trials but cannot accept a leaf.

## 3. The pinned face and exact exchange

The old bounded author attempt stopped at its time cap. Its
[partial record](../repro/results/research-mixed-half-row-support-partial.json)
has SHA256
f326bde32741e73dee5b9f8475d31b897d16569cdc002d970f4cfa49219f0686.
Only its complete case
\[
              (\epsilon,\alpha,\beta,\mathrm{face})=(0,0,0,0)
\tag{9}
\]
is imported: 96,199 leaves and the complete exact tree. The
unfinished opposite face is not promoted. The new program binds
that record, old proof, old checker and every old dependency.
It reconstructs the complete tree and revalidates every imported
root and source test with the old fixed-trial rule, without search.

For equal external types write
\(S=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).
The original equations have the exact exchange
\[
                         (s,t,A,C)\longmapsto(t,s,C,A).
\tag{10}
\]
The two conditional orientations interchange with unchanged own
flag and matching first-halfweight flag. At identical polar
parameters, face one is face zero with its inputs swapped.
An affine-root witness therefore transforms by
\[
 \mathrm{center}\mapsto S\,\mathrm{center},\quad
 \mathrm{radius}\mapsto S\,\mathrm{radius},\quad
 Y\mapsto SYS,\quad D_{\rm affine}\mapsto SD_{\rm affine}S.
\tag{11}
\]
The two saved target pairs exchange orientation slots; coordinates
within each pair do not exchange. These transformations give the
corresponding original-log witness and the same mathematical
inequality. Every transformed root and bound is nevertheless
rechecked outward.

The exchange applies to every equal-type face pair in a future
complete run. Case (9) and its opposite use the old rule; new
independent faces use (8), and their equal-type opposites use the
new rule after exchange. No equal-type opposite face is searched.
Both unequal-type ordinary faces remain independent.

## 4. Acceptance labels and replay

Each domain has the explicit label “fixed_trial_v1” or
“optimized_envelope_v1”. The former invokes the unchanged original
checker, with its original curvature and whole-cell target gain.
The latter invokes (4)--(8). A stronger available bound does not
silently change the acceptance rule of an imported leaf.

An independent tree stores exact split axes, rational original
witnesses and both rational target pairs. A transported domain
stores its earlier equal-type face-zero “source_case”, its rule
and its leaf count. Its entire tree is reconstructed by (11).
The source pointer always goes to an earlier independently stored
tree; there is no cyclic or nested pointer.

Saved replay checks every exact tree and transformed leaf using
its specified rule. The pinned tree must equal the one in the old
partial record. A transported domain must be its prescribed
exchange. All other saved trees are traversed without root/target
proposals or subdivision. Original roots, midpoint log lifts,
responses, gains or optimizer boxes, and strict source bounds are
recalculated at replay precision. Displayed decimal bounds may
change with precision; exact trees, rational witnesses, target
pairs, rules and provenance may not.

## 5. Bounded execution

The first pilot, after proof/code review, is only
\[
                   (\epsilon,\alpha,\beta,\mathrm{face})=(0,1,1,0).
\tag{12}
\]
It has at most 511 visited nodes and 60 seconds including setup.
Both conditional orientations and every target are checked.
Setup binds the old partial and reconstructs its complete tree,
but does not numerically replay its leaves in this weak-face
pilot. Pilot success has status “pilot_complete”, never “passed”.

A full attempt following pilot review has the existing caps of
600,000 visited nodes, 600 seconds and depth 45. Imported and
exchanged nodes count toward visit/time limits; setup counts
toward time. The driver checks limits between node evaluations,
then saves completed domains and the exact unfinished frontier.
Artifact serialization and final hash checks do not restart the
search. Point or depth stops also preserve an incomplete record.
There is no automatic extension or restart.

Only a complete non-pilot record proves (3). This design does not
prove completion within the limits or settle the remaining
last-row, terminal-graph or ordinary-source comparisons. The
original partial proof, checker and result remain unchanged.
