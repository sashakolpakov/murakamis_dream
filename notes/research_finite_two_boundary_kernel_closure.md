# Composing a finite collection of two-boundary pieces

Research note, 3 November 2026. The bare edge is not the only kernel
that can be used in the long-power recursion. A proved two-boundary
source with the same analytic properties can replace it. This matters
for short crossing powers: the degree-two sources of powers \(2\)
and \(-2\) have already been estimated on their entire original
boundary. Summing such a vertex first avoids extending a local edge
formula to the difficult contour of that vertex.

The theorem below is an induction for the full finite sources. Its
hypotheses include global bounds and all first normals. Local
convergence of critical actions alone is not a substitute for them.

## 1. Two exact orders of contraction

Use the original Newton algebra, crossing \(R\), turn \(T\), and
full trace \(\phi_N\). The complete edge kernel is
\[
 K_N(s,t)=\sum_{j=0}^{N-1}e_j(-2\cos s)e_j(-2\cos t),
 \qquad (Tf)(u)=\phi_N^{(t)}[f(t)K_N(t,u)].
 \tag{1}
\]
For a fixed signed power \(b\), put
\[
 P_{b,N}(s,u)=\phi_N^{(t)}[R^bK_N(t,s)K_N(t,u)].
 \tag{2}
\]
At every level and for every input polynomial \(f\),
\[
 \boxed{\displaystyle
 T\bigl(R^bT(R^af)\bigr)(u)
       =\phi_N^{(s)}[R^af(s)P_{b,N}(s,u)].}
 \tag{3}
\]
Indeed, substitute (1) and interchange the two finite linear
functionals. This interchanges finite sums and derivatives, not
asymptotic expansions. Every first normal at a repeated root remains.
All products are formed in the original quotient algebra.

For \(H_{a,N}=T(R^a)\), the special case is
\[
            T(R^bH_{a,N})(u)=\phi_N^{(s)}[R^aP_{b,N}(s,u)].
 \tag{4}
\]
Thus an outer short power \(b\) can be summed before a long inner
power \(a\). No contour identity is needed to justify this reordering.

## 2. The kernel hypotheses and two consequences

Consider a finite collection \(E_{j,N}(s,u)\). Each is a polynomial
of degree at most \(N-1\) separately in \(-2\cos s\) and
\(-2\cos u\). Suppose its full source has the expansion
\[
 E_{j,N}(s,u)=\epsilon_{j,N}N^{-3/2}
 a_j(s,u)e^{N\Phi_j(s,u)}(1+O(N^{-1})),
 \qquad |\epsilon_{j,N}|=1,
 \tag{5}
\]
on a neighborhood of one closed bidisk about zero. The amplitudes
are holomorphic and zero-free there, the errors are holomorphic,
and the phases are separately even. Assume that on a smaller
common bidisk
\[
                    -\Re\Phi_j''\succeq\kappa I_2
                    \quad(\kappa>0).
 \tag{6}
\]
Here the real part is the Hermitian part of the complex symmetric
matrix. Suppose also that the entire boundary polynomial satisfies
\[
 |E_{j,N}(x+iy,v+iw)|\le C_jN^{d_j}
 e^{N\{M_j-c_j(1-\cos x)-c_j(1-\cos v)+B_j(y^2+w^2)\}},
 \quad M_j=\Re\Phi_j(0,0),
 \tag{7}
\]
for all real \(x,v\in[-\pi,\pi]\) and a fixed positive strip.
Finiteness permits common positive constants after decreasing the
losses and widths and increasing the other constants.

These hypotheses imply both estimates used in the fixed-domain
long-power proof. There are positive radii \(r_o,r_i\) and constants
\(\gamma_o,\gamma_i\), common to the collection, such that
\[
\begin{split}
 |E_{j,N}(x,u)|&\le C_j'N^{d_j'}
  e^{N\{\Re\Phi_j(0,u)-\gamma_o(1-\cos x)\}},
       &&x\in[-\pi,\pi],\quad |u|\le r_o,\\
 |E_{j,N}(s,v)|&\le C_j'N^{d_j'}
  e^{N\{\Re\Phi_j(s,0)-\gamma_i(1-\cos v)\}},
       &&|s|\le r_i,\quad v\in[-\pi,\pi].
\end{split}
 \tag{8}
\]
Both radii include neighborhoods of the displayed closed disks.
The first estimate gives first spectral derivatives on any fixed
outer real spectral interval at polynomial cost.

Here is the proof, which is useful because no additional wire formula
is required. Fix a small \(a>0\) inside the bidisk of (5). For real
\(|x|\le a\), separate evenness and (6) give
\[
 \Re\Phi_j(x,u)\le\Re\Phi_j(0,u)-\kappa x^2/2.
 \tag{9}
\]
The full expansion (5) gives the first bound in this region. On
\(|x|\ge a\), (7), together with
\[
 |\Phi_j(0,u)-\Phi_j(0,0)|\le L|u|^2,
 \tag{10}
\]
gives a possible error of at most \((B+L)|u|^2\) relative to
\(\Re\Phi_j(0,u)\). Choose \(r_o\) so this error is less than
half of \(c(1-\cos a)\). The remaining half of the angular loss
proves the first line of (8). The second follows by exchanging the
roles of the variables: use (5)--(6) for small real \(v\), and (7)
for \(|v|\ge a\), absorbing
\((B+L)|s|^2\) by a common choice of \(r_i\).
Markov's inequality on an outer spectral interval proves the
first-normal assertion, including complex \(u\); rotating the value
of a derivative reduces the complex-coefficient estimate to the real
one. The polynomial degree is at most \(N-1\).

## 3. The invariant class and the long-power operation

Start with any family of original one-boundary sources having the
common terminal properties used in
[the fixed-domain theorem](research_fixed_domain_long_power_turns.md):
a zero-free holomorphic packet on a common disk, a bounded normalized
even phase with positive real curvature, and a whole-boundary
Gaussian strip bound. The original terminal family \(H_{a,N}\),
\(|a|\ge2\), is such a family.

Choose \(R>0\) so \(|u|\le2R\) lies inside all initial disks, the
kernel bidisks, their marked charts when geometry is asserted, and
the disk \(|u|<r_o\) of (8). Let \(a_T>0\) be the initial curvature
bound and choose
\[
\begin{split}
 a_0&\le\min(a_T,\kappa),\\
 H&\ge\max\left\{H_T,\,
       2R^2\max_j\sup_{|s|,|u|\le2R}
                       \left|\frac{\Phi_{j,u}(s,u)}u\right|\right\}.
\end{split}
 \tag{11}
\]
The removable values at \(u=0\) are understood. The invariant
phase bounds are
\[
 |W(u)-W(0)|\le H,\qquad -\Re W''(u)\ge a_0
                       \quad(|u|\le2R).
 \tag{12}
\]
Choose positive common angular and strip constants for the initial
family and for the output reset described below. They are fixed
before choosing a power threshold.

For a source \(F_N\) in this class, define the exact operation
\[
 \mathcal U_{j,n}F_N(u)
       =\phi_N^{(s)}[R^nF_N(s)E_{j,N}(s,u)].
 \tag{13}
\]
There is one integer \(B_*\), independent of \(F_N\), \(j\), and
the number of previous operations, such that every fixed signed
\(|n|\ge B_*\) gives another source in the same class.

To verify the uniformity explicitly, choose
\[
 0<r<\min(R/2,r_i/2),\qquad
 L\ge 2H/R^2+\max_j\sup|\Phi_{j,ss}|,\qquad
 C_h=8\pi^2L.
 \tag{14}
\]
Let \(\delta>0\) be smaller than the common outer angular losses
at the midpoint cutoff \(r\), supplied by (7)--(8) and the input
real bound. Require, for example,
\[
\begin{gathered}
 |n|>8\pi L,\qquad |n|>16\pi/r,\\
 \frac{C_h}{2n^2}<\min(\delta/4,a_0r^2/8),\qquad
 \frac{C_h}{n^2}<r/4.
\end{gathered}
 \tag{15}
\]
Increasing one integer \(B_*\) makes these inequalities hold for
every eligible signed \(n\).

Put \(P(s,u)=W(s)+\Phi_j(s,u)\). The contraction
\[
 s_\lambda(u)=\frac{2\pi}{n}
                  \{\lambda+iP_s(s_\lambda(u),u)\}
                    \quad(0\le\lambda\le1)
 \tag{16}
\]
has a unique solution throughout the unchanged output disk. It obeys
\[
 |s_\lambda(u)|\le4\pi\lambda/|n|,\qquad
 0<-\Im s_\lambda(u)\le C_h\lambda/n^2
                       \quad(\lambda>0),
 \tag{17}
\]
with a positive lower bound of order \(\lambda/n^2\). The estimates
follow from (6), (12), and the contraction calculation in the
fixed-domain proof. The action
\[
 S(u)=P(s_*(u),u)+\frac{in}{4\pi}s_*(u)^2-is_*(u),
                    \qquad s_*=s_1,
 \tag{18}
\]
loses at most \(C_h/(2n^2)\) in real part from \(P(0,u)\).

### The full trace and its nonzero coefficient

The first line of (8) bounds every original outer trace node, with
its first normal, at rate
\(\Re W(0)+\Re\Phi_j(0,u)-\delta\). This is below (18) by
(15), uniformly on the unchanged disk. In the central midpoint
rectangle use the full packet (5) and the full packet for \(F_N\).
The exact midpoint trace identity retains its endpoint current and
the rational kernel containing every Fourier charge.

Its lower horizontal side passes through \(s_*(u)\). Strict
horizontal concavity follows from (6), (12). The endpoint gaps,
their preservation under the small shift (17), and vertical
convexity after folding the upper endpoint are precisely the
argument in Section 4 of the fixed-domain proof, now with
\(\psi\) replaced by \(\Phi_j\). Its proof uses these stated
inequalities and the exact trace identity, not the bare edge's
factorial formula. Higher charges have a strictly smaller rate at
the positive depth in (17). That gap may shrink with \(n\), which
only changes the starting level for a fixed operation.

If \(F_N=\varepsilon_N A e^{NW}(1+O(N^{-1}))\), the result is
\[
 \mathcal U_{j,n}F_N
   =\varepsilon_N\epsilon_{j,N}C_{N,n}
       A_{\rm new}(u)e^{NS(u)}(1+O_{F,j,n}(N^{-1})),
 \qquad C_{N,n}=e^{\pi in(N-1)^2/(4N)},
 \tag{19}
\]
where
\[
 A_{\rm new}(u)=i\sqrt{\frac2\pi}\,
 \frac{\sin s_*\,A(s_*)a_j(s_*,u)}
 {\sqrt{-W''(s_*)-\Phi_{j,ss}(s_*,u)-in/(2\pi)}}.
 \tag{20}
\]
Every factor is nonzero on the common disk. The powers of \(N\)
are \(N^{-3/2}N^2N^{-1/2}=1\). The coefficient and Gaussian branch
are those of the original midpoint trace.

### Why no constant deteriorates under iteration

The envelope identity is
\[
                        S'(u)=\Phi_{j,u}(s_*(u),u).
 \tag{21}
\]
It restores the normalized bound \(H\) in (11). The matrix
\[
 -\begin{pmatrix}
 W''+\Phi_{j,ss}+in/(2\pi)&\Phi_{j,su}\\
 \Phi_{j,us}&\Phi_{j,uu}
 \end{pmatrix}
 \tag{22}
\]
has Hermitian real part at least
\(\operatorname{diag}(a_0,0)+\kappa I_2\).
The exact Schur-complement identity therefore gives
\(-\Re S''\ge\kappa\ge a_0\) on the same disk.

For arbitrary real outside angle \(u\), use the second line of
(8) on the complete central contour chosen at \(u=0\). It supplies
the loss \(\gamma_i(1-\cos u)\) on every horizontal and endpoint
piece; the remaining phase is exactly the central phase already
bounded at \(u=0\). Outer physical nodes use (7), retaining its
output loss and a fixed central loss. The latter absorbs the small
selected-action decrease in (18). Consequently the whole real
output has angular loss at least
\[
                         \gamma=\min(\gamma_i,c_{\rm ker})>0,
 \tag{23}
\]
after harmless common decreases, independently of the input's
previous loss and the number of operations. Here \(c_{\rm ker}\)
is a common constant in (7).

The output is again a polynomial of spectral degree at most
\(N-1\). Combine (23) with the uniform local phase bounds (12),
(21)--(22), and apply the polynomial maximum-principle strip reset
of Section 5 of the fixed-domain proof. This gives common positive
constants \(c,C,h\) in
\[
 |F_N(x+iy)|\le C_FN^{d_F}
 e^{N\{\Re W(0)-c(1-\cos x)+Cy^2\}}.
 \tag{24}
\]
For an explicit order of choices, first choose \(R,H,a_0\); next
choose \(c\) below the initial loss and the output loss (23), and
choose \(C\) from the common local derivative bounds. Choose \(h\)
from the initial strip and the Green-function bound on the fixed
outer spectral interval. Only then choose \(r,L,\delta,B_*\) in
(14)--(15). This is the same noncircular order as in the
fixed-domain proof. Prefactors and starting levels may depend on
the whole fixed word, but eligibility, the zero-free disk, and the
exponential constants do not.

## 4. The available finite collection

Take
\[
                       E_0=K,\qquad E_+=P_2,\qquad E_-=P_{-2}.
 \tag{25}
\]
The bare edge satisfies (5)--(7), as used in the fixed-domain
theorem. For the other two kernels these are the proved conclusions
of [the two-boundary theorem](research_degree_two_power_two_boundary_theorem.md)
and [its marked phase comparison](research_degree_two_power_two_geometric_phase.md):
\[
\begin{split}
 \epsilon_{\sigma,N}&=e^{\sigma i\pi N/2},\\
 \Phi_\sigma&=G_\sigma,\qquad
 \Phi_\sigma''(0,0)
             =-\frac{e^{\sigma i\pi/6}}{2\pi}I_2,
                      \quad \sigma=\pm1.
\end{split}
 \tag{26}
\]
Thus (6) holds on a common bidisk after shrinking once. The exact
imaginary constants are retained in (26).

Equation (13) with \(E_0\) is the ordinary long-power turn
\(T(R^nF)\). With \(E_\sigma\), equation (3) identifies it with
\[
                        T\bigl(R^{2\sigma}T(R^nF)\bigr).
 \tag{27}
\]
It follows that any finite sequence of these operations, starting
from any terminal \(T(R^a)\), \(|a|\ge2\), has the full nonzero
packet and the same domains and constants, provided every variable
power \(n\) has magnitude at least \(B_*\). The short powers \(2\)
and \(-2\) may occur arbitrarily often. In the literal word they are
separated by at least one eligible long power.

There is also a useful additional seed. Apply the same proof once
with \(F=1\). The input then has \(W=0\), so its positive curvature
and angular loss are absent; the kernel itself supplies both in
(6)--(8). Use \(\kappa\) in place of \(a_0\) when selecting the
threshold for this first step. The output resets to (11)--(12) and
(24), exactly as above. After one common enlargement of \(B_*\),
(4) therefore gives a controlled family
\[
 T(R^{2\sigma}H_{a,N})(u)
   =e^{\sigma i\pi N/2}C_{N,a}
       D_{a,\sigma}(u)e^{NS_{a,\sigma}(u)}
                         (1+O_a(N^{-1})),
             \qquad |a|\ge B_* .
 \tag{28}
\]
The phase is the stationary value of
\(G_\sigma(s,u)+ia s^2/(4\pi)-is\); its amplitude is (20)
with \(A=1\). This proves the long-inner/short-outer assertion
using only the already proved two-boundary source, on its existing
small bidisk. It requires no extension of the bare-edge packet to
the old central-angle saddle of the two-crossing vertex.

## 5. Markings, closing, and the volume limit

For the collection (25), every kernel is an actual original marked
piece: either a bare edge, or two edges with their middle degree-two
circle already filled at power \(2\sigma\). Their interface maps,
primitive periods and absolute phases are those proved in the
referenced geometric constructions. Choose the common disk above
inside these positive marked charts.

Attach a controlled child to the input circle of one of these
pieces. The original annular sectors glue with their common primitive
longitude, and the new carrier is inserted once. If \(n=\eta-2p\),
the new primitive filling period is
\[
 U+pV=-2\pi\left(W'(s)+\Phi_{j,s}(s,u)
                         +\frac{in}{2\pi}s\right)
                =-2\pi i\lambda .
 \tag{29}
\]
The charge path (17) stays in the inner child and kernel charts.
Consequently every earlier filled slope stays fixed and every
earlier core stays positive. The new core is positive because
\(-2\Im s_\lambda>0\). The output periods are
\(U_{\rm out}=-2\pi S'(u)\), \(V_{\rm out}=2iu\).
This is the same full-map annular composition as in
[the recursive marked construction](research_recursive_marked_block_geometry.md);
a kernel \(P_{2\sigma}\) simply retains its already completed
interior circle throughout that composition.

At charge zero and complete outer boundary, the child and kernel
volumes add. Their absolute anchor is
\(2\pi\Re[W(0)+\Phi_j(0,0)]\). Schläfli's formula along (29)
therefore gives complete-boundary volume \(2\pi\Re S(0)\).
The phase constants in (26) remain in their exact unit factors and
do not change this real anchor.

Finally close the last original circle by \(\phi_N(R^{c_0}F_N)\).
The scalar-closing proof in Section 7 of the fixed-domain theorem
uses only the restored invariant class, so one additional common
threshold for \(|c_0|\) suffices. The result has a nonzero
\(N^{3/2}D e^{NS}\) asymptotic, times the recorded unit scalars.
If the original disk frames, half-twist parities and literal strand
tracing give one knot and no internal closed component, the original
reduced zero-framed Kashaev invariant therefore satisfies
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                       =\operatorname{Vol}(S^3\setminus K).
 \tag{30}
\]
The size of every long-power threshold is independent of the fixed
word length and of the number of short \(2\) or \(-2\) insertions.
All powers and the whole word remain fixed before \(N\to\infty\).
This result does not treat arbitrary adjacent short clusters, nor
does it imply finitely many excluded assignments for a fixed
template.

## 6. Any prescribed finite set of nonzero short powers

The restriction to the two short powers in (25) can now be removed.
Let \(\mathcal B\subset\mathbb Z\setminus\{0\}\) be any fixed finite
set. By
[the all-power degree-two theorem](research_all_nonzero_degree_two_fillings.md),
every \(P_{b,N}\), \(b\in\mathcal B\), satisfies the full two-boundary
hypotheses (5)--(7). Since the set is finite, choose a common bidisk,
a common positive curvature lower bound, and common angular and strip
constants. There is no claim that these choices are uniform over all
nonzero integers.

Applying Sections 1--3 to the finite collection
\[
                  \{K_N\}\cup\{P_{b,N}:b\in\mathcal B\}
 \tag{31}
\]
gives one threshold \(B_*(\mathcal B)\) for the operations
\[
 F\longmapsto T(R^nF),\qquad
 F\longmapsto T\bigl(R^bT(R^nF)\bigr),
 \quad b\in\mathcal B,\quad |n|\geq B_*(\mathcal B).
 \tag{32}
\]
The exact trace interchange (3) proves the second equality with
the kernel operation; it is not an asymptotic replacement. Starting
with any terminal \(T(R^a)\), \(|a|\ge2\), one may perform any
fixed finite sequence of (32). The full boundary estimate, nonzero
leading coefficient, and common domains survive every step. The
threshold is independent of sequence length, the order of elements
of \(\mathcal B\), and the signs of the long powers. Constants in
the remainder and its starting level may depend on the entire fixed
sequence. The seed \(F=1\) described above is available after the
same type of common threshold enlargement.

Each kernel in (31) also has its original marked geometric meaning.
For \(|b|\ge2\), it is the isolated filled degree-two piece, with
the positive geometric germ and absolute action supplied by the
all-power theorem and its referenced geometric proofs. For
\(b=\pm1\), the
[direct boundary-action comparison](research_degree_two_unit_power_geometry.md)
gives the original primitive derivatives and absolute real volume
anchor of the filled piece itself. Its core and both boundary labels
remain present. A drawing reduced by the marked unit-power move is
also available, but then the actual half-turn and both crossing
shifts must be carried on the attached tangle. With these original
interface maps retained,
the annular composition and scalar-closing argument of Section 5
apply without alteration. Thus (30) holds for the resulting knots
after an independently sufficiently long final power.

This treats any finite allowed collection of isolated short powers,
repeated arbitrarily often with sufficiently long powers between
successive insertions. It does not permit two arbitrary short powers
to be composed without the intervening long step. That distinction
remains essential to the finite-exception problem.
