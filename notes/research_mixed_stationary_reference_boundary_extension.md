# Boundary extension along a stationary reference curve

Research deduction, 6 November 2026. Internal stationarity reduces the
reference-response cost in the selected-height maximum principle to
the retained boundary coordinates. The original canonical prefix gives
a one-complex-dimensional application, with a possible direct
external-coordinate cover using original-gradient residuals. No boundary
gap, response bound or new numerical evaluation is supplied here.

## 1. Only the boundary responses remain

Let \(r(p)\in\mathbb C^n\) be holomorphic near a closed complex
rectangle \(R\), and let \(F\) be holomorphic near its image.
Partition the coordinate indices into internal indices \(I\) and
retained boundary indices \(B\). Suppose throughout this neighborhood
that
\[
 F_i(r(p))=0\quad(i\in I),\qquad
 p_j(p)=F_j(r(p))\quad(j\in B).
 \tag{1}
\]
The letter \(p_j\) denotes a marginal, while \(p\) is the
single complex reference parameter. Differentiation gives the exact
vector identity
\[
 F''(r)r'=(w_i)_{i=1}^n,\qquad
 w_i=0\ (i\in I),\quad w_j=p_j'\ (j\in B).
 \tag{2}
\]

Fix a real target vector \(x\), a real height vector \(h\), and
a nonnegative real diagonal matrix \(\Lambda=\operatorname{diag}\lambda_i\).
These are held fixed while differentiating \(p\). Set
\[
 w=x+ih+\tfrac12\Lambda(r-\bar r),\qquad
 D=\Re\{\Psi(w)-F(r)-F'(r)\cdot(w-r)\},
 \tag{3}
\]
where \(\Psi\) is holomorphic near the entire target image and
\(-\Re\Psi''(w)\succeq0\) there. All branches and domains are
required on the whole parameter rectangle, before applying a maximum
principle. The
[selected-height extension identity](research_mixed_selected_height_reference_extension.md),
equation (4), and symmetry of \(F''\) give
\[
 \Delta_pD=
 -\Re\{(\Lambda r')^T\Psi''(w)\Lambda\bar r'\}
 +2\Re\sum_{j\in B}\lambda_jp_j'\overline{r_j'}.
 \tag{4}
\]
Indeed the second term before reduction is
\(2\Re\{r'^TF''(r)\Lambda\bar r'\}\), and (2) gives
precisely (4). No derivative of a target optimizer, second derivative
of the reference map or omission of a boundary marginal is involved.

The first term in (4) is nonnegative. Consequently, with
\[
 \mathcal B(p)=\sum_{j\in B}\lambda_j|p_j'r_j'|,
 \qquad \Delta_pD\ge-2\mathcal B(p),
 \tag{5}
\]
only boundary responses must be charged. Each summand in
\(\mathcal B\) is the modulus of a holomorphic function, so
\(\mathcal B\) is subharmonic. This does not make \(D\)
subharmonic.

**Proposition 1.** Suppose \(D\le-\gamma\) and
\(\mathcal B\le B_0\) on all of \(\partial R\), uniformly
over the fixed target parameters under consideration. If the imaginary
width of \(R\) is \(L\), then
\[
                 D\le-\gamma+B_0L^2/4\quad\hbox{on }R.
 \tag{6}
\]
The smaller real width can replace \(L\). For a closed disk of
radius \(R_0\), the corresponding bound is
\(D\le-\gamma+B_0R_0^2/2\), provided the same holomorphic and
target hypotheses hold near that disk.

To prove (6), first extend the boundary bound for \(\mathcal B\)
by subharmonicity. For an imaginary interval \([y_-,y_+]\),
subtract \(B_0(y-y_-)(y_+-y)\) from \(D\). The result is
subharmonic and is at most \(-\gamma\) on the boundary, including
the vertical sides. The barrier is at most \(B_0L^2/4\).
For a disk use \(B_0(R_0^2-|p-p_0|^2)/2\). Apply this argument
separately for every target before taking any supremum.
There is no deformation of the target contour in this argument.

The disk barrier also works on a clipped disk. More generally, let
\(K=\overline\Omega\) be a compact planar domain contained in
\(\{|p-p_0|\le R_0\}\), and assume the holomorphic hypotheses
on a neighborhood of \(K\). If both boundary bounds hold on the
entire \(\partial\Omega\), then the same loss
\(B_0R_0^2/2\) holds on \(K\). The barrier is nonnegative on
\(K\), so subtracting it preserves the boundary upper bound on
every clipping segment as well as on the circular arcs. No comparison
outside \(K\) is required. The clipped disks used below are convex
and have nonempty interiors, so this version applies directly.

## 2. The original second-selection comparison

Use the [canonical prefix](research_mixed_second_selected_reference_curve.md)
for flags \((\alpha,1,\beta)\), with its next external coordinate
now denoted \(c\). Let
\[
 r(c)=(a,u,z,v,b),\qquad
 F=V(u,a)+V(u,z)+V(v,z)+V(v,b)
       -g(u)-\beta g(v)-g(z)
       -\tfrac\alpha2g(a)-\tfrac\beta2g(b)
       +2\pi iau+2\pi izv,
 \quad V(s,t)=g(s+t)-g(s)-g(t).
 \tag{7}
\]
This is exactly the allocated original phase in the
[central budget](research_mixed_second_selected_central_budget.md),
equation (3). Its canonical references satisfy the full complex
identities \(F_u=F_z=F_v=0\), with
\[
 p_L=F_a=g'(a+u)-(1+\alpha/2)g'(a)+2\pi iu,
 \qquad
 p_R=F_b=g'(v+b)-(1+\beta/2)g'(b).
 \tag{8}
\]
They are the same original incoming and outgoing tangents; in
particular the outgoing allocated halfweight remains in \(p_R\).

For the factorial branch \(\nu=1\) and forced branch \(\nu=0\),
take
\[
 \Psi_\nu=F+(1-\nu)g(z)+2\nu\pi iz,
 \quad
 \Lambda=\operatorname{diag}(1,1,0,1,1),\quad
 h=(0,0,H,0,0).
 \tag{9}
\]
At the target, \(\Re(2\nu\pi iz)=-2\nu\pi H\), exactly
the frequency debit of the full selected polynomial. With
\(x=(x_a,x_u,x_z,x_v,x_b)\), (3) is precisely
\[
 D_\nu(c;x)=\Re\{\Psi_\nu(w)-F(r)
                -p_L(w_a-a)-p_R(w_b-b)\}.
 \tag{10}
\]
Thus it is the central objective minus its original reference value,
with both complex affine terms retained.

Here is an explicit sufficient domain for Proposition 1. Let the
closed external-coordinate rectangle, disk or clipped disk lie in \(D_3\cup D_4\)
with a holomorphic canonical prefix on a neighborhood, and require
its whole image to have
\[
\begin{gathered}
 -.102<\Im u<-.001,\qquad -.078<\Im a<.021,\\
 (\Im v,\Im b)\in
 \begin{cases}(-.065,.068)^2,&\beta=0,\\
               (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{11}
\]
Take \(0\le H\le.014\), \(P=[.22,.45]\), and the full
original target product
\[
 x\in P\times[.125,.5]\times P\times[\ell_\beta,.5]\times P,
 \qquad \ell_0=.15,\quad\ell_1=.125.
 \tag{12}
\]
Every single argument and every pair argument of \(g\) then has
real part strictly between zero and one, uniformly on the closed
target. In particular the smallest pair sum is at least \(.345\)
and the largest is at most \(.95\). The original primitive is
holomorphic on a neighborhood of this full image. Proposition 1 of
[horizontal concavity](research_mixed_second_selected_horizontal_concavity.md)
gives \(-\Re\Psi_\nu''\succ0\) throughout (11)--(12).
The already proved index barriers can restrict (12) afterwards;
they are not needed to establish the extension's target regularity.
Likewise a fixed branch-domain restriction in \(x_z\) is allowed.

For this application, the entire reference response cost is
\[
              \mathcal B(c)=|p_L'(c)a'(c)|+|p_R'(c)b'(c)|.
 \tag{13}
\]
The same \(\mathcal B\) applies to both Fourier alternatives
and every target in (12). Hence boundary gaps for (10) extend with
the explicit cost (6), if the whole-image conditions (11) and a
boundary upper bound on (13) are proved. In particular the actual
typed external domains are
\[
\begin{split}
 K_3&=\{|c-(.35-.01i)|\le.083\}
        \cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4&=\{|c-(.30-.052i)|\le.060\}
        \cap\{-.108\le\Im c\le-.001\}.
\end{split}
 \tag{13a}
\]
The respective extension costs are at most
\(6889B_0/2000000\) and \(9B_0/5000\). Both the circular arcs
and the straight clipping segments must be covered by the boundary
comparison and the response bound. This avoids adding invalid corners
of enclosing rectangles. Canonical existence on the
larger disks alone is not a proof of all these quantitative hypotheses.
No whole-disk bound, raw-defect subharmonicity, or comparison for the
clipped scalar majorants is inferred. The identity applies to the
original phase defect before its target optimization.

## 3. Direct external-coordinate enclosures

The frozen [residual-localization theorem](research_mixed_prefix_residual_localization.md)
provides a way to enclose this same curve without the high-degree
rational transport. Write its seven original gradient components as
\(f(q;c)\), with \(q=(e,\xi,a,u,z,v,b)\), and
\(\mu=6\pi/49\). Existence is already proved for every
\(c\in D_3\cup D_4\), independently of a proposed approximation.
At a fixed center \(q_0\), changing \(c\) changes only the last
gradient row:
\[
 f(q_0;c)-f(q_0;c_0)
 =e_b\{j(b_0+c)-j(b_0+c_0)+i\pi(c-c_0)\},
 \qquad j=J'.
 \tag{14}
\]
Thus the first derivative forcing is rank one. For the exact
canonical solution,
\[
 q_*'(c)=-f_q(q_*;c)^{-1}e_b
             \{\pi\cot\pi(b_*+c)+i\pi\}.
 \tag{15}
\]
The inverse norm is at most \(1/\mu\). A deliberately coarse
global bound follows directly on the common product: for
\(\Re(b+c)\in[.46,.90]\), positive-radius minimization gives
\(|1-e^{-2\pi i(b+c)}|>1/2\), since where its cosine is
positive the sine modulus is at least \(\sin(\pi/5)>1/2\).
Using
\(\pi\cot\pi w+i\pi=2\pi i/(1-e^{-2\pi iw})\) gives
\(\|q_*'(c)\|_2<98/3\). This finite bound explains the
regularity of the coordinate chart; it is too coarse by itself to
promise an efficient scalar-gap cover.

A rational affine predictor gives a sharper validated option. Fix
exact \(q_0,c_0\) and an arbitrary rational complex column \(T\),
and set \(q_{\rm aff}(c)=q_0+T\delta\), \(\delta=c-c_0\).
Require the whole affine image to remain in the common convex product,
and the whole parameter cell to lie in the domain of existing canonical
solutions. With \(r_0=f(q_0;c_0)\), \(H_0=f_q(q_0;c_0)\),
and \(s_0=f_c(q_0;c_0)\), Taylor's formula gives
\[
 \|f(q_{\rm aff}(c);c)\|_2
 \le \|r_0\|_2+\|H_0T+s_0\|_2|\delta|
                         +\tfrac12\|\rho\|_2|\delta|^2.
 \tag{16}
\]
All quantities on the right require outward bounds. To define an
explicit admissible remainder, express each gradient row as
\(\sum_k a_{ik}j(L_{ik}(q,c))\) plus an affine term, using
\(f_\xi=2j(1/2-\xi)-3j(\xi)+j(e-\xi)+i\pi e\).
Each \(L_{ik}\) is affine, and one may take
\[
 \rho_i=\sum_k |a_{ik}|
       \sup|J'''(L_{ik}(q_{\rm aff}(c),c))|
       |dL_{ik}(T,1)|^2,
 \qquad J'''(w)=-\pi^2\csc^2\pi w,
 \tag{17}
\]
where the supremum includes every segment from \(c_0\) to the
cell. The regular-strip checks precede (17). The affine chirps have
zero remainder. No certified inverse is required to choose \(T\):
its unsatisfied linear equation is explicitly charged in (16).

Dividing (16) by \(\mu\) bounds
\(\|q_*(c)-q_{\rm aff}(c)\|_2\) for every parameter in
the cell. Good rational predictors therefore leave a quadratic
parameter remainder, rather than propagating nested degree-97
quotients. Both (13) and scalar comparisons still need actual
enclosures before this route becomes a certificate. Nothing here
authorizes replacing those calculations with a claim that the full
defect attains its maximum on the parameter boundary.

## 4. Matching boundary responses cancel before taking absolute values

The signed form (4) is also useful for a finite collection of clusters.
Let each cluster \(k\) have holomorphic reference and target phases
\(F^{(k)},\Psi^{(k)}\), and let its reference coordinates be drawn
from one holomorphic global coordinate vector \(r(p)\). Assume that
the phases have no additional explicit dependence on \(p\); all
parameter dependence passes through those reference and target
coordinates. Each cluster satisfies the internal stationarity and
target-curvature hypotheses of Section 1. Any shared coordinate has
the same \(x_j,h_j,\lambda_j\) in every occurrence, so that the
cluster targets are restrictions of one global target.

Let \(p_j^{(k)}\) be the boundary marginal of cluster \(k\) at
an occurrence of coordinate \(r_j\). Count every occurrence with
its literal multiplicity. Partition the global boundary coordinates
into glued internal coordinates \(G\) and external coordinates
\(E_{\rm out}\). Require the full complex matching equations
\[
       \sum_{k:\,j\in B_k}p_j^{(k)}(p)=0\quad(j\in G)
 \tag{18}
\]
throughout the parameter neighborhood, not merely at one reference
point. All own terms and Fourier allocations must already have been
assigned to the cluster phases so that (18) is their actual original
stationarity equation. Define the total external marginal
\(P_j=\sum_{k:\,j\in B_k}p_j^{(k)}\).

**Corollary 2.** For the sum of the cluster defects (3), the only
possibly negative response term is
\[
 \Delta_p\sum_kD^{(k)}
 =\sum_k\mathcal A_k
       +2\Re\sum_{j\in E_{\rm out}}\lambda_jP_j'\bar r_j',
 \qquad \mathcal A_k\ge0.
 \tag{19}
\]
Consequently Proposition 1 applies with the single external cost
\[
            \mathcal B_{\rm out}
             =\sum_{j\in E_{\rm out}}\lambda_j|P_j'r_j'|.
 \tag{20}
\]

To prove this, sum the exact identities (4). At a shared coordinate
the factor \(\lambda_j\bar r_j'\) is common to every occurrence.
Differentiating (18) makes their signed response sum zero. Only then
take absolute values at the external coordinates. Each
\(P_j'r_j'\) is holomorphic, so the boundary control of (20)
extends by subharmonicity just as in (5). The terms
\(\mathcal A_k\) are the nonnegative target-Hessian forms from
(4); their sum remains nonnegative on the glued coordinate space.
The affine tangent contributions at glued coordinates also cancel
already in \(\sum_kD^{(k)}\), by (18) and the common target.

Thus no response charge is paid at an exactly matched internal
interface. The cost is indexed by the external boundary, rather than
by the number of constituent clusters. This is not a numerical bound
on external responses uniform in cluster count: the functions
\(P_j'\) and \(r_j'\) may still depend on the whole composition.
If the two target-height factors at an interface differ, or matching
holds only at an isolated point, the stated cancellation does not
follow. Nor does the lemma itself establish a boundary comparison,
a finite-source contour estimate or a nonzero coefficient.
