# Uniform support at the smaller own-four left cutoff

Research certificate, 5 November 2026. This is an ordinary-reference
comparison for the own-type-four conditional factor. It compares
the complete row at index \(1/8\) with its original horizontal
supporting plane, for every horizontal target in the plateau.
The reference inputs range over the entire reduced bidisks, not
just their two-circle distinguished boundary. Terminal endpoint
graphs and the other two remaining real rows are separate.

The arithmetic part is the six-face certificate described below.
Only a complete record with status “passed” establishes that part;
an interrupted record with pending cells establishes no universal
sign.

## 1. The original reference and the allocated deficit

Let the external type flags be
\((\alpha,\beta)\in\{(0,0),(0,1),(1,1)\}\). The flag zero
means type three. The two reduced closed disks are
\[
 \begin{split}
 P_3&=\{z:|z-(7/20-i/100)|\le83/1000\},\\
 P_4&=\{z:|z-(3/10-13i/250)|\le3/50\}.
 \end{split}
 \tag{1}
\]
For \((A,C)\in P_{3+\alpha}\times P_{3+\beta}\), use the
unique original two-leg root \((s,t)\) of
\[
 \begin{split}
 g'(s+t)+g'(s+A)-3g'(s)+2\pi i A&=0,\\
 g'(s+t)+g'(t+C)-3g'(t)+2\pi i C&=0.
 \end{split}
 \tag{2}
\]
Existence, uniqueness, original zero lifts and the parameter response
are those of the
[reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md).
All four arguments in (2) lie in its regular rectangle
\(Q=[.23,.45]+i[-.12,.12]\). No exponentiated equation
replaces (2).

There are two conditional orientations:
\[
 (s_*,a,b,\eta)=(s,A,t,\alpha)
       \quad\hbox{or}\quad(t,C,s,\beta).
 \tag{3}
\]
For either, set
\[
 \begin{split}
 F(v;a,b)={}&g(v+a)+g(v+b)-3g(v)
       -(1+\eta/2)g(a)-\tfrac32g(b)+2\pi iav,\\
 \phi(a,b)&=F(s_*;a,b),\qquad Z=(a,b)=U+iH,\\
 I&=[11/50,9/20],\qquad
 \ell=1/8,\qquad \kappa=1/2500000 .
 \end{split}
 \tag{4}
\]
The branch of \(\phi\) is the original critical branch. It is
locally a holomorphic function of its retained variables, as in the
[reference-boundary principle](research_mixed_horizontal_tail_reference_boundary.md).
For \(X\in I^2\), define
\[
 \begin{split}
 B_Z(X)&=\Re\phi(Z)+\Re\phi'(Z)\cdot(X-U)
                              -\kappa\|X-U\|^2,\\
 D(Z,X)&=\Re F(\ell;X+iH)-B_Z(X).
 \end{split}
 \tag{5}
\]
At this cut every shifted real argument lies strictly between zero
and one. Thus the first term in (5) is exactly the allocated
complete real-row rate, with its asymmetric chirp and both outer
halfweights. It is not a sum in which revived rows have been removed.

**Theorem 1.** For every reference in (1)--(3) and every \(X\in I^2\),
the complete certificate specified in Sections 3--5 proves
\[
                         D(Z,X)<-1/2000 .
 \tag{6}
\]
Both orientations are required. Swapping \((A,s)\) with \((C,t)\)
preserves (2), so the three unordered type pairs together with these
two orientations cover all ordered ordinary conditional families.
Both boundary faces are checked even when the external types agree.

On the full auxiliary domain the displayed outer factorial
allocations are formal phase functions. Their physical interpretation
as unselected Fourier upper rates retains the actual negative
type-four reference heights. In particular (6) does not assign that
physical branch at a positive auxiliary type-four height.

## 2. Reduction to six ordinary boundary faces

The allocated original critical phase satisfies
\[
                       -D_U^2\Re\phi\succ(\pi/8)I_2
                                      \succ2\kappa I_2 .
 \tag{7}
\]
This is the original pair estimate followed by the complex Schur
complement, as explained in the reference-boundary principle.
The map \((A,C)\mapsto(A,t(A,C))\) is locally invertible
because \(t_C\ne0\); the same holds in the other orientation.

At matched targets \(X=U\), the old source theorem has
left-cut gap greater than \(1/1000\) at index \(3/20\), throughout
the full reduced product. The full-real-row derivative is greater
than \(1/2\) on \((0,3/20]\), on the full outer-height domain
\([-.12,.12]\); see Section 6 of the
[asymmetric-contour proof](research_mixed_horizontal_asymmetric_contour.md).
Moving the cut from \(3/20\) to \(1/8\) therefore saves more
than \(1/80\), and gives
\[
             D(Z,U)<-\frac1{1000}-\frac1{80}
                              =-\frac{27}{2000}.
 \tag{8}
\]
Only this single-row deduction is used on the auxiliary height
domain. No right-tail theorem restricted to heights at most
\(.108\) is extended to this domain.

The reference-boundary principle, using (7)--(8), reduces (6) to
\[
 (\partial P_{3+\alpha}\times P_{3+\beta})
       \ \cup\ (P_{3+\alpha}\times\partial P_{3+\beta}).
 \tag{9}
\]
These are ordinary boundary faces. The second factor in each face
is a whole disk, not just its circle. With three unordered type
pairs there are six three-real-dimensional faces.

For each face use the full cube
\((\theta,\rho,\psi)\in[0,1]^3\): its circle variable is
\(c+r e^{2\pi i\theta}\), and its disk variable is
\(c+\rho r e^{2\pi i\psi}\). The derivatives are
\(2\pi i(z-c)\) on the circle and
\(r e^{2\pi i\psi},\,2\pi i\rho r e^{2\pi i\psi}\)
on the disk. The center \(\rho=0\) and all boundary points are
included. Repeated polar images do not leave any point uncovered.

## 3. Eliminating the horizontal target grid

The target curvature at the new cut is stronger than needed. Put
\[
 f(x)=\Re\{g(x+\ell+ih)-\lambda g(x+ih)\},
 \quad x\in I,\quad |h|\le3/25,\quad \lambda\ge1.
 \tag{10}
\]
Write \(C=\cos(\pi/8)\), \(S=\sin(\pi/8)\),
\(K=\cosh(2\pi h)\) and \(T=\cos(2\pi x+\pi/8)\).
Then \(-1\le T\le0\), \(1\le K<4/3\),
\(9/10<C<15/16\), and \(S>3/8\). Direct subtraction gives
\[
 \Re\{\cot\pi(x+ih)-\cot\pi(x+\ell+ih)\}
 =\frac{2S(C-KT)}{T^2-2CKT+C^2+K^2-1}
 \ge\frac{2S}{C+K}.
 \tag{11}
\]
The denominator is the product of two strictly positive cotangent
denominators. After multiplication by the positive denominators,
the last inequality is
\((1+T)\{1-T-K(K-C)\}\ge0\).
It follows from \(K(K-C)<26/45<1\) and \(T\le0\).
Since \(g''(z)=\pi\cot\pi z-\pi i\), the nonnegative
extra term \((\lambda-1)\pi\Re\cot\pi(x+ih)\) gives
\[
                          -f''(x)>\frac{36\pi}{109}>1.
 \tag{12}
\]
The last strict inequality follows already from \(\pi>157/50\).
The hyperbolic bound is the same elementary bound used on the outer
strip in the smaller-cut proof.

The dependence on the two real targets is separated in (4).
Consequently the target Hessian of \(D\) is diagonal and at most
\(-c_*I_2\), where \(c_*=1-2\kappa>0\).
Fix any rational trial \(\widehat X\in I^2\).
For a target slope interval \(\beta_i\) containing
\(\partial_{X_i}D(Z,\widehat X)\), every target is bounded by
the trial value plus the two clipped quadratic gains
\[
 G_i=\max_{d\in[11/50-\widehat X_i,\,9/20-\widehat X_i]}
                  \{\beta_i d-\tfrac12c_*d^2\}.
 \tag{13}
\]
Here the interval coefficient is maximized in the appropriate sign
of \(d\). On either one-sided interval the exact maximum is at
zero, the stationary point, or the outer endpoint. This is the
formula implemented by the checker; stable endpoint slopes may
give zero gain. Floating scalar stationary points merely propose
the rational trials. They never decide acceptance, and no target
grid is used.

## 4. A whole-cell bound preserving the reference cancellations

Let \(P=\phi'(Z)\), \(H_\phi=\phi''(Z)\),
\(\delta=\widehat X-U\), and
\(P_c=F_X(\ell;\widehat X+iH)\).
At fixed rational trial the exact reference derivatives are
\[
 \begin{split}
 D_U&=(-\Re H_\phi-2\kappa I)\delta,\\
 D_H&=\Im\{P-P_c+H_\phi\delta\}.
 \end{split}
 \tag{14}
\]
The first line is precisely the cancellation used in the
reference-boundary principle. The second keeps the complete
height response and both allocated outer terms.

The checker evaluates the complex Schur complement
\[
 H_\phi=F_{XX}-F_{Xs}F_{ss}^{-1}F_{sX}.
 \tag{15}
\]
Explicitly, \(F_{ss}=g''(s_*+a)+g''(s_*+b)-3g''(s_*)\),
the mixed vector is
\((g''(s_*+a)+2\pi i,\ g''(s_*+b))\), and the two
outer diagonal entries before elimination are
\(g''(s_*+a)-(1+\eta/2)g''(a)\) and
\(g''(s_*+b)-3g''(b)/2\).
The chirp in the first mixed entry is retained.

On each parameter cell the original affine two-root witness is
validated by the unchanged interval self-map and original-log
midpoint test from the reduced-disk certifier. Its interval inverse
response, with its weighted Neumann tail, encloses the derivatives
of both roots with respect to both external arguments. Combining
that response with the polar derivatives after (9) gives the
derivative of \(Z\) with respect to all three real parameters.
Equation (14), by the real chain rule, gives interval derivatives
\(D_{\xi_j}\) throughout the whole cell.

If the cell midpoint is \(\xi_0\), with halfwidths \(h_j\),
the direct original-log phase evaluation on the tiny midpoint root
disk gives \(D_0\). The accepted upper bound is
\[
                 D_0+\sum_{j=1}^3 h_j\sup|D_{\xi_j}|
                             +G_1+G_2<-1/2000 .
 \tag{16}
\]
Every quantity in this inequality is outward evaluated. The root
disk is not clipped to improve the phase bound. The full correlated
root response is used; neither retained reference argument is
replaced by an independent range for differentiating the phase.
Both orientations in (3) must pass (16) on every accepted leaf.

## 5. Complete coverage, bounded author run and saved replay

The certifier is
[certify_mixed_four_left_cut_support.py](../experiments/certify_mixed_four_left_cut_support.py).
The canonical output is
[research-mixed-four-left-cut-support.json](../repro/results/research-mixed-four-left-cut-support.json).
It binds this proof, its own script, the complete original
reduced-disk author and saved replay, and all inherited current
dependencies, together with the analytic supporting-plane,
reference-boundary, curvature and contour deductions used here.
The original source records are not modified or recomputed.

For each of the six cases the root cube is split at exact rational
midpoints, cycling the three parameter axes. The stack appends the
left child and then the right child, and pops the right child first.
Every split and accepted leaf is saved in that precise traversal
order. A leaf stores its rational affine root witness and the two
rational target pairs. A complete face must exhaust its stack and
has exactly \(2L-1\) visited nodes if it has \(L\) leaves.
The complete six-face run therefore has \(2L_{\rm total}-6\)
nodes. These identities supplement the actual tree reconstruction;
they do not replace it.

The author run is bounded by 600,000 visited nodes and 600 seconds.
If either limit or the explicit depth limit stops it, the record
has status “incomplete”, preserves completed faces, the partial
current tree and every pending cell, and proves no omitted-cell
claim. A failed strict-gap test is subdivided or reported as
unresolved; no display-rounded maximum is used for acceptance.

A saved replay uses the same six cases and exact tree traversal.
It may neither propose a root nor propose a target, and it may not
refine a saved leaf. Every saved self-map, original-log lift,
response and inequality (16) is checked again at the requested
precision. Both proof/script hashes and every input/dependency
hash are rechecked after completion. Reporting decimals are
diagnostic; the acceptance test is the direct strict interval
comparison in (16).

Once all six faces pass, (7)--(9) and the boundary principle prove
Theorem 1 on the entire reduced input products. No old
four-dimensional root cover is rerun.

## 6. Consequence and remaining scope

For actual ordinary own-four references to which the
[smaller-cut contour theorem](research_mixed_four_left_cut_extension.md)
applies, the left row in that theorem's finite upper maximum is
strictly below the original plane. Thus its upper bound simplifies
to
\[
 C_\tau N^A
       \exp N\{\max(B,R(1/2),R(1))+\tau\},\qquad \tau>0 .
 \tag{17}
\]
The actual outer allocation, fixed original reference heights,
all original contour currents and both level parities are
unchanged. This is an upper bound; it asserts no new moving
critical point, relative finite packet, or transverse derivative
estimate.

The half row and last row remain calibrated comparison problems.
The theorem also makes no claim for the different terminal
endpoint graphs merely from their inclusion in a rectangle.
Neither actual-word realization of arbitrary independent inputs
nor full open-source dominance is needed or concluded.
