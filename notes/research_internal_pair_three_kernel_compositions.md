# Repeated internal pairs separated by long fillings

Research corollaries, updated 4 November 2026. Frozen manuscripts are unchanged.

The full two-boundary theorems permit repeated internal pairs in an
original path, separated by sufficiently long signed fillings.
Sections 1–4 retain the first case, the pair \(3,3\) and its mirror.
Section 5 first treats a prescribed finite collection. Sections 6–8
prove one common separator and closing threshold for all ordered
pairs \(n,p\ge7\), their mirrors, and the original \(3,3\) pair.
The threshold is independent of the powers, number and order of the
blocks. It need not be small, and each word is fixed before the level
tends to infinity. Section 9 also gives an exact zero-separator
reduction when the merged neighboring power is sufficiently long.
None of these statements removes every separating-power restriction.

## 1. The original operation

Use the original crossing \(R\), full Hermite trace \(\phi_N\),
and edge kernel \(K_N\). Thus
\[
 (TF)(u)=\phi_N^{(s)}[F(s)K_N(s,u)].
 \tag{1}
\]
All products are taken before the trace; in particular, the first
normal derivatives at double spectral roots are retained.
For \(\sigma\in\{1,-1\}\), let
\[
 E_{\sigma,N}(s,u)=
 \phi_N^{(t)}\phi_N^{(r)}
 [R(t)^{3\sigma}R(r)^{3\sigma}
          K_N(s,t)K_N(t,r)K_N(r,u)].
 \tag{2}
\]
This is a path with two selected interior vertices and two free
endpoints. Both selected vertices have original degree two.
Interchanging finite traces gives the exact identity
\[
 \begin{split}
 \phi_N^{(s)}[R(s)^n F(s)E_{\sigma,N}(s,u)]
   &=T\!\left(R^{3\sigma}
           T\!\left(R^{3\sigma}T(R^nF)\right)\right)(u).
 \end{split}
 \tag{3}
\]
No boundary variable is specialized in this identity. Hence its
derivatives are also those of the original source. The factor
\(R^n\) belongs to the input circle; the two factors \(R^{3\sigma}\)
belong to the two different interior circles in (2).

## 2. Checking the composition hypotheses

Theorem 1 of
[the internal-pair packet](research_internal_pair_three_full_boundary_packet.md)
proves that \(E_{\sigma,N}\) is a polynomial of degree at most
\(N-1\) in each boundary spectral variable and has the expansion
\[
 E_{\sigma,N}(s,u)=
 C_{N,3\sigma}^{\,2}N^{-3/2}
       a_\sigma(s,u)e^{N\Phi_\sigma(s,u)}(1+O(N^{-1})),
 \qquad
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)}.
 \tag{4}
\]
The amplitude is holomorphic and nonzero on a fixed bidisk. The
normalized error is holomorphic there, and the phase is separately
even. At the origin,
\[
 \Phi_+''(0,0)
      =-\frac{\cos(t_*/2)}{2\pi}I_2,\qquad
 \Phi_-''(0,0)=\overline{\Phi_+''(0,0)},\qquad
                         \Re\cos(t_*/2)>0 .
 \tag{5}
\]
Continuity therefore gives a common smaller closed bidisk and
\(\kappa>0\) on which
\(-\Re\Phi_\sigma''\succeq\kappa I_2\).
Here \(\Re\) denotes the Hermitian part of the symmetric Hessian.
The same theorem proves the full two-boundary estimate
\[
 |E_{\sigma,N}(x+iy,v+iw)|
 \le C_\sigma N^{d_\sigma}
 e^{N\{M_\sigma-c_\sigma(1-\cos x)
                    -c_\sigma(1-\cos v)+B_\sigma(y^2+w^2)\}}
 \tag{6}
\]
on the entire real boundary square and a fixed complex strip.
It includes both level parities and the original first normals.

Thus (4)--(6) verify all hypotheses (5)--(7) of
[the finite two-boundary composition theorem](research_finite_two_boundary_kernel_closure.md).
There is no additional analytic hypothesis for this insertion.
The marked stationary action in the internal-pair theorem retains
the original primitive meridians, disk longitudes, carriers and
all three edge constants. Its positive boundary germ and absolute
volume anchor supply the geometric hypotheses used in Section 5
of the composition theorem.

## 3. The resulting family of paths

**Corollary 1.** There is a finite integer \(B\) with the following
property. Start with \(F_0=T(R^a)\), where \(|a|\ge2\).
Apply any fixed finite sequence of the operations
\[
 \begin{split}
 F&\longmapsto T(R^nF),\\
 F&\longmapsto
       T\!\left(R^{3\sigma}
          T\!\left(R^{3\sigma}T(R^nF)\right)\right),
       \qquad \sigma=\pm1 ,
 \end{split}
 \qquad |n|\ge B .
 \tag{7}
\]
Every resulting source has a nonzero holomorphic boundary
asymptotic and a whole-boundary quadratic strip bound on common
domains. One may then close the last original circle by
\(\phi_N(R^cF)\) for any fixed \(|c|\ge B\), after enlarging \(B\)
once to include the scalar-closing threshold.

Keep the original half-twist carriers and require, at every circle,
\[
                  n_v=\eta_v-2p_v,\qquad p_v\in\mathbb Z .
 \tag{8}
\]
If the resulting literal strand closure has one knot component
and no internal closed component, its original reduced
zero-framed Kashaev invariant has a nonzero leading term and
satisfies
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
                  \log|\langle K\rangle_N|
                    =\operatorname{Vol}(S^3\setminus K).
 \tag{9}
\]
The integer \(B\) is independent of the sequence length, the order
and signs of the short pairs, and the signs or magnitudes of the
eligible long powers. Every power and the entire sequence are
fixed before \(N\) tends to infinity.

**Proof.** Enlarge the finite kernel collection by the two
polynomials (2). Section 2 verifies its hypotheses on common
smaller domains. Sections 2--3 of the finite-kernel theorem give
one long-power threshold and restore the same phase, curvature
and boundary bounds after each operation. Equation (3) identifies
each operation with the original word (7). Its exact scalar is
the incoming scalar multiplied by
\(C_{N,n}C_{N,3\sigma}^{\,2}\); no scalar is discarded.

The original positive interface charts in Section 2 allow the
marked annular composition of Section 5 of that theorem. The
long filling moves only its own primitive meridian period.
Both interior fillings of each short pair remain fixed and
positive throughout the small input deformation. A sufficiently
long final trace has a nonzero \(N^{3/2}\) leading coefficient.
The original writhe and framing factors have modulus one.
The marked volume identity and the literal knot-component
hypothesis therefore give (9). \(\square\)

For example, when every stage uses a pair, the original path word
is
\[
 (a,n_1,3\sigma_1,3\sigma_1,n_2,3\sigma_2,3\sigma_2,
                       \ldots,n_k,3\sigma_k,3\sigma_k,c).
 \tag{10}
\]
Equation (8) is imposed on this original word. In particular,
the odd powers in a short pair require the corresponding odd
carrier parity. No change of peripheral basis or quotient of
the original filling assignments is used.

## 4. What the corollary does and does not cover

One may add any other fixed finite collection of kernels already
satisfying the same hypotheses. This includes isolated nonzero
short powers from Section 6 of the finite-kernel theorem, and
fixed long runs from Corollary 3 of
[the uniform path theorem](research_uniform_path_trace_assembly.md).
The latter theorem supplies their \(N^{-3/2}\) normalization,
nonzero coefficient and full boundary bounds. Its real angular
loss and separate evenness imply negative definite boundary
Hessian at zero, so shrinking their finitely many neighborhoods
supplies the remaining curvature hypothesis.

The numerical threshold \(64\) in the uniform path theorem is
not a proved separator threshold for the enlarged collection.
The present deduction gives a finite common \(B\) from the
composition theorem. Constants in error terms and their starting
levels may depend on the entire fixed word.

In particular, the corollary does not join two short pairs without
an intervening long power, does not treat an arbitrary adjacent
short word, and does not imply finitely many excluded original
assignments for a fixed template. It proves a new repeated-block
family within the existing composition theorem.


## 5. Any fixed finite collection of positive internal pairs

Let \(\mathcal F\) be any finite set of ordered integer pairs
\((n,p)\) with \(n,p\ge7\), and put
\[
                  \mathcal J=\{(3,3)\}\cup\mathcal F.
 \tag{11}
\]
For \((n,p)\in\mathcal J\) and \(\sigma\in\{1,-1\}\), retain
the literal marked kernel
\[
 E_{\sigma;n,p,N}(s,u)=
 \phi_N^{(t)}\phi_N^{(r)}
 [R(t)^{\sigma n}R(r)^{\sigma p}
                       K_N(s,t)K_N(t,r)K_N(r,u)] .
 \tag{12}
\]
The order of \(n,p\) is part of this definition. Its exact
contraction against an incoming original source is
\[
 \begin{split}
 &\phi_N^{(s)}[R(s)^b F(s)E_{\sigma;n,p,N}(s,u)]\\
 &\hspace{8mm}=
 T\!\left(R^{\sigma p}
     T\!\left(R^{\sigma n}T(R^bF)\right)\right)(u).
 \end{split}
 \tag{13}
\]
This follows by interchanging the original finite Hermite traces.
All three crossing factors belong to distinct original circles;
none is absorbed into a new peripheral convention.

Theorems 6–7 of the
[full pair source theorem](research_internal_pair_combined_contour_reduction.md)
prove, for each member of \(\mathcal F\), the zero-free local
expansion and whole-period quadratic-strip bound required by
(5)–(7) of the
[finite-kernel composition theorem](research_finite_two_boundary_kernel_closure.md).
The leading unit through both parities is exactly
\(C_{N,\sigma n}C_{N,\sigma p}\). Each kernel has degree at
most \(N-1\) in each ordinary boundary color. Its normalized
remainder is holomorphic, with all fixed ordinary boundary
normals retained. The existing pair-three theorem supplies the
same statements for the pair \(3,3\) and its mirror.

For clarity, the boundary curvature for a positive general pair
is explicit. If \(t_*,r_*\) are its selected angles at complete
outside colors, its critical boundary action satisfies
\[
 \mathcal S''(0,0)=
 -\frac1{2\pi}
 \begin{pmatrix}
      \cos(t_*/2)&0\\0&\cos(r_*/2)
 \end{pmatrix}.
 \tag{14}
\]
The first derivative of the unsummed phase in either outside
angle vanishes identically at that angle zero. Consequently
the derivative of its internal critical point also vanishes
there, so no Schur correction occurs in (14).
Equivalently, separate evenness gives the mixed entry zero,
and the original edge derivative supplies the two diagonal
entries. Their real parts are positive after the displayed
minus sign is removed. The mirror pair has the conjugate
Hessian. Continuity on a smaller common closed bidisk therefore
gives \(-\Re\mathcal S''\succeq\kappa I_2\) for some
\(\kappa>0\), common to this finite collection.

All the hypotheses are hypotheses on full finite sources.
In particular the whole-period estimate in Theorem 7 is not
inferred from a local Gaussian or a formal positive critical
point. Taking minima of the finitely many strip widths and
angular losses, and maxima of their remaining constants,
provides the common domains used in the composition theorem.
Their positive marked boundary germs persist on these domains:
the already filled interior circles retain their original
slopes and positive core lengths. Their complete anchors are
the volumes of their three original edges, including the
internal filling corrections.

**Corollary 2.** For every finite collection \(\mathcal F\) above,
there is a finite integer \(B_{\mathcal F}\) with the following
property. Start with \(F_0=T(R^a)\), \(|a|\ge2\). Apply any
fixed finite sequence of the operations
\[
 \begin{split}
 F&\longmapsto T(R^bF),\\
 F&\longmapsto
 T\!\left(R^{\sigma p}
     T\!\left(R^{\sigma n}T(R^bF)\right)\right),
 \quad (n,p)\in\mathcal J,\quad \sigma=\pm1,
 \end{split}
 \qquad |b|\ge B_{\mathcal F}.
 \tag{15}
\]
The resulting original source has a nonzero holomorphic packet
and a whole-boundary quadratic-strip bound on common domains.
It may be closed by \(\phi_N(R^cF)\) whenever
\(|c|\ge B_{\mathcal F}\), after increasing this same threshold
once to include scalar closing.

Retain every original carrier and impose
\(n_v=\eta_v-2p_v\), \(p_v\in\mathbb Z\), at every original
circle, including both interior circles of each pair. If the
literal strand closure has one knot component and no internal
closed component, its original reduced zero-framed Kashaev
invariant has a nonzero leading term and obeys
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                          =\operatorname{Vol}(S^3\setminus K).
 \tag{16}
\]
The limit is through all integer levels, including both parities.
The threshold is independent of the number of pair insertions,
their order, their choices of mirror, and the signs or magnitudes
of the eligible long powers. The entire word and all its powers
are fixed before the level tends to infinity.

*Proof.* Enlarge the finite kernel collection in the composition
theorem by (12). The preceding expansion, curvature and global
bounds verify its analytic assumptions on common smaller domains.
That theorem supplies a single long-power threshold and restores
the same invariant phase and boundary estimates after every
operation. Equation (13) identifies the operation with the original
word and retains its incoming scalar multiplied by
\(C_{N,b}C_{N,\sigma n}C_{N,\sigma p}\).
The original bare-edge step in (15) is already part of the same
induction. Constants in a final error bound and its starting level
may depend on the resulting fixed word.

The marked annular composition and scalar closing are those of
Section 5 of the composition theorem. The long filling changes
only its own primitive meridian period. Both previously filled
interior circles remain in their positive marked charts. At a
complete interface the child and pair volume anchors add; the
original Schläfli calculation supplies the new filling correction.
After the final scalar trace, the literal knot-component condition
identifies the source with its reduced zero-framed Kashaev
invariant, up to the already retained unit framing and carrier
factors. This proves (16). \(\square\)

For a sequence in which every step inserts a pair, the original
path word is
\[
 (a,b_1,\sigma_1n_1,\sigma_1p_1,b_2,
       \sigma_2n_2,\sigma_2p_2,\ldots,
       b_k,\sigma_kn_k,\sigma_kp_k,c),
       \qquad (n_i,p_i)\in\mathcal J.
 \tag{17}
\]
Thus every finite choice of additional pairs yields an actual
family of original assignments. The argument up to this point does
not supply a threshold common to the infinite pair family; Section 8
proves that stronger statement. Both results still require eligible
separating powers and do not give finitely many excluded assignments
in an arbitrary fixed template.

## 6. Uniform estimates for the isolated-vertex family

The uniformity needed for a separator threshold concerns exponential
rates and domains. It does not concern a simultaneous limit in the
crossing powers and the level. In this section a **uniform kernel
family** means that (5)–(7) of the
[finite-kernel theorem](research_finite_two_boundary_kernel_closure.md)
hold on common disks and strips, with common phase derivative bounds,
positive real Hessian bound, angular loss and imaginary quadratic
constant. The amplitude is nonzero on the common disk. Its size,
the polynomial upper prefactor, the normalized asymptotic error and
the first valid level may depend on the member. No positive common
lower bound on the amplitudes is required.

**Lemma 3.** The exact isolated-vertex kernels
\[
 P_{n,N}(u,v)=\phi_N^{(t)}
       [R(t)^nK_N(t,u)K_N(t,v)],\qquad n\ge7,
 \tag{18}
\]
form a uniform kernel family. Their mirrors do also. One can include
the bare kernel in the same family.

*Proof.* For the finitely many powers \(7\le n<64\), use
[the all-power isolated-vertex theorem](research_all_nonzero_degree_two_fillings.md).
We give the required uniform source estimates for \(n\ge64\),
rather than infer them from holomorphy of the geometric equations.
Put \(s=1/n\), and write the selected angle as \(t=s\zeta\).
The original stationary equation becomes
\[
 \zeta=2\pi+2\pi i\{\psi_t(s\zeta,u)+\psi_t(s\zeta,v)\}.
 \tag{19}
\]
On \(|t|,|u|,|v|\le1/4\), the elementary edge derivative bound
\(|\psi_{tt}|<1/5\) proved in Section 2 of
[the uniform terminal theorem](research_uniform_terminal_family_and_star_fillings.md)
gives \(|\psi_t(t,u)|\le|t|/5\). For
\(|s|\le1/64\), \(|\zeta|\le7\), the right side of (19)
has modulus at most \(2\pi+(4\pi/5)(7/64)<7\), and
its derivative in \(\zeta\) has modulus less than
\(4\pi/(5\cdot64)<1/25\). Thus (19) has a unique jointly
holomorphic solution on a neighborhood of a smaller closed parameter
polydisk, including \(s=0\). At that endpoint \(\zeta=2\pi\).
The stationary phase is
\[
 S_s(u,v)=\psi(s\zeta,u)+\psi(s\zeta,v)
             +\frac{is\zeta^2}{4\pi}-is\zeta,
 \qquad S_0(u,v)=\psi(0,u)+\psi(0,v).
 \tag{20}
\]
Consequently its normalized values and all fixed derivatives have
common bounds on smaller disks. Separate evenness and differentiation
of the stationary equation give
\[
 S_s''(0,0)=-\frac{\cos(t_s(0,0)/2)}{2\pi}I_2.
 \tag{21}
\]
Since \(|t_s|\le7/64\), its negative real part exceeds
\(I_2/(4\pi)\) for real \(0\le s\le1/64\).
Compactness and the common derivative bounds extend a smaller positive
bound to one common closed complex bidisk.

The actual degree-two trace amplitude in the
[degree-and-power theorem](research_high_degree_short_internal_vertex.md),
equation (18), has the rescaling
\[
 s^{-3/2}A_{1/s}(u,v)=i\sqrt{\frac2\pi}\,
 \frac{[\sin(s\zeta)/s]a_e(s\zeta,u)a_e(s\zeta,v)}
 {\sqrt{-s\{\psi_{tt}(s\zeta,u)+\psi_{tt}(s\zeta,v)\}
                                      -i/(2\pi)}}.
 \tag{22}
\]
The numerator quotient equals \(2\pi\) at \(s=0\).
The denominator stays nonzero by the preceding derivative bound;
the edge amplitudes are nonzero on this chart. Shrinking the common
bidisk once makes (22) holomorphic and nonzero there, uniformly
including \(s=0\). The factor \(s^{3/2}\) explains why a
uniform positive amplitude lower bound would be false.

Here is the source-domain check. Apply the degree-and-power proof
with \(d=2\), retained wire interval \([1/5,3/10]\), and
outer angle cutoff \(a_0=6/25\). Its complete-boundary action loss
obeys
\[
 0<2M_\infty-\Re S_{1/n}(0,0)
       \le\Delta:=\frac7{4100}.
 \tag{23}
\]
The omitted original wire assignments, after the full first-normal
trace, have rate at most \(2M_\infty-\pi/100\).
The outer trace rows have rate at most \(2\psi(a_0,0)\).
Thus the two common gaps are
\[
 \delta_w=\frac\pi{100}-\Delta>0,
 \qquad
 \delta_o=\frac{a_0^2}{2\pi}-\Delta>0.
 \tag{24}
\]
The geometric point satisfies \(|t_s|\le7/64<a_0\).
Set \(Q(t,u,v)=[\psi_t(t,u)+\psi_t(t,v)]/t\), with its
removable value at zero. On a smaller common chart
\(\Re Q<-q_0<0\). For real \(n\ge64\), (19) gives
\[
 t=\frac{2\pi/n}{1-2\pi iQ(t,u,v)/n},\qquad
 -\Im t=\frac{-4\pi^2\Re Q(t,u,v)}
 {n^2|1-2\pi iQ(t,u,v)/n|^2}>0.
 \tag{25}
\]
This identity holds for complex \(u,v\) as well. The depth is
comparable to \(n^{-2}\) throughout the common boundary disk.

On the central trace rectangle, \(\Re(\psi_{tt}(t,u)+
\psi_{tt}(t,v))\) has a common strictly negative upper bound.
The chirp adds a purely imaginary second derivative. The horizontal
endpoint is a fixed distance from \(\Re t\); horizontal concavity
therefore gives a common endpoint gap. At height zero the gap follows
from (24). Convexity in the vertical height bounds the complete
folded endpoint current by those two endpoint bounds. All omitted
wire and outer-row estimates extend to a common complex boundary
bidisk by their separate degree bounds, the fixed gaps (24), and the
common derivative bounds for (20). These are precisely the regions
in the original midpoint-trace proof. Its higher Fourier charges
lose the positive depth in (25). That loss may tend to zero with
\(n\), but for each fixed \(n\) it yields the required exponentially
small error. It affects the starting level, not the common source
domain or any separator threshold.

For arbitrary real outside angles, the retained weighted edge bound
in Section 6 of the degree-and-power theorem inserts
\([(1-\cos u)+(1-\cos v)]/20\) in every central horizontal
and vertical estimate. The omitted terms have the gaps (24),
uniformly for those angles. Since the sum of the two angular losses
is at most four, the real-period bound holds with the common constant
\[
 c_*=\min\{1/20,\delta_w/4,\delta_o/4\}>0.
 \tag{26}
\]
Near zero the common source disk and phase derivative bounds give
a common quadratic complex estimate. Away from that neighborhood,
the real-period bound has a common strict gap. The separate degree
\(N-1\) and polynomial Bernstein–Walsh continuation preserve half
that gap on a common thin strip. This proves the required uniform
strip estimate. Polynomial prefactors and starting levels may still
depend on \(n\).

Take the finite minimum with the powers \(7\le n<64\).
Exact conjugation gives the mirrored family, with the original unit
scalars retained. The bare kernel has the same estimates on its
fixed complete-boundary chart. The large-power geometric charts
are common because \(t_s\) and both free angles remain in the
fixed positive edge chart; (25) retains the correct core orientation.
The remaining finitely many members use their proved marked charts.
No filling curve is changed. \(\square\)

## 7. One long trace with two free endpoints

**Lemma 4.** Let \(\mathcal E\) and \(\mathcal F\) be two
uniform kernel families in the sense of Section 6. There is one
finite integer \(B_0\) such that the exact kernels
\[
 G_{E,F,b,N}(u,v)=\phi_N^{(t)}
                 [R(t)^bE_N(u,t)F_N(t,v)],
                 \qquad |b|\ge B_0,
 \tag{27}
\]
form a uniform kernel family. Every member and \(b\) are fixed
before \(N\) tends to infinity. The output constants can depend
on the two input families, but not on their members or \(b\).
This is a single gluing statement; it does not assert that all its
constants are unchanged under arbitrary repeated gluing.

*Proof.* Write the two input phases as \(\Phi(u,t)\) and
\(\Theta(t,v)\), and put \(P(t;u,v)=\Phi(u,t)+\Theta(t,v)\).
The proof of the centered estimates (8) in the finite-kernel theorem
uses only common phase derivatives, curvature and strip constants.
It therefore supplies common centered estimates for these families,
even if they are infinite. Its prefactors may depend on the members.

On common small disks, the exact stationary equation is
\[
 t_\lambda=\frac{2\pi}{b}
        \{\lambda+iP_t(t_\lambda;u,v)\},\qquad 0\le\lambda\le1.
 \tag{28}
\]
Separate evenness gives \(P_t(0;u,v)=0\).
The common derivative and real-curvature bounds give a contraction
for all sufficiently large \(|b|\), with
\(|t_\lambda|\le4\pi\lambda/|b|\) and positive lower depth
comparable to \(\lambda/b^2\). The depth assertion follows
exactly as in (25), with \(Q=P_t/t\): its real part is uniformly
negative. The selected action
\[
 \Gamma(u,v)=P(t_*;u,v)+\frac{ib}{4\pi}t_*^2-it_*,
               \qquad t_*=t_1,
 \tag{29}
\]
loses at most \(C/(2b^2)\) in real part from \(P(0;u,v)\).
Indeed its derivative in \(\lambda\) has real part \(\Im t_\lambda\).

Choose a fixed midpoint angle cutoff inside the common packet disks.
The centered estimates bound all original outer trace nodes, including
their first normals, at a fixed common loss relative to
\(P(0;u,v)\). Increase \(B_0\) until \(C/(2b^2)\) is smaller
than a quarter of this loss and the central horizontal endpoint loss.
On the central rectangle the exact midpoint trace is applied to the
product of the two full input packets. Horizontal concavity, folded
vertical convexity and the positive depth in (28) control respectively
the central maximum, both endpoint currents and every higher rational
Fourier charge. This is the proof of Section 3 of the finite-kernel
theorem with \((u,v)\) as parameters; each inequality is uniform
because the phase bounds and outer-node gaps just used are common.
In particular the conclusion concerns the original full trace, not
only its stationary integral.

If the input unit scalars and amplitudes are \(\epsilon_E,a_E\)
and \(\epsilon_F,a_F\), the output is
\[
 G_{E,F,b,N}=
 \epsilon_E\epsilon_F C_{N,b}N^{-3/2}
 a_G(u,v)e^{N\Gamma(u,v)}(1+O_{E,F,b}(N^{-1})),
 \tag{30}
\]
with the original Gaussian branch and
\[
 a_G=i\sqrt{\frac2\pi}\,
 \frac{\sin t_*\,a_E(u,t_*)a_F(t_*,v)}
 {\sqrt{-\Phi_{tt}(u,t_*)-\Theta_{tt}(t_*,v)-ib/(2\pi)}}.
 \tag{31}
\]
The power is \(N^{-3}N^2N^{-1/2}=N^{-3/2}\).
Every factor in (31) is nonzero on one common bidisk: the two input
amplitudes have that property, the stationary equation excludes
\(t_*=0\), and the denominator has positive real part before
taking its square root. Derivatives of the normalized remainder
retain their order on smaller common disks.

The full negative Hessian in variables \((u,t,v)\) has Hermitian
real part at least \(\kappa\operatorname{diag}(1,2,1)\),
after choosing a common input lower bound \(\kappa>0\).
The chirp contributes only a purely imaginary entry. Taking its
Schur complement in \(t\) proves
\[
                         -\Re\Gamma''\succeq\kappa I_2.
 \tag{32}
\]
For completeness, apply the full quadratic form to
\((z,-A^{-1}Bz)\), where \(A\) is the internal block and
\(B\) its boundary row. The internal row vanishes, so the
quadratic form is exactly that of the boundary Schur complement;
its real part is bounded below by \(\kappa|z|^2\).
The envelope identities
\(\Gamma_u=\Phi_u(u,t_*)\) and
\(\Gamma_v=\Theta_v(t_*,v)\) give common normalized phase
bounds. Cauchy estimates on smaller disks give the other fixed
derivative bounds.

For the whole real outside square, choose the central trace contour
at \(u=v=0\). The centered estimates give, throughout that contour,
\[
 |E_N(u,t)F_N(t,v)|\le C_{E,F}N^{d_{E,F}}
 e^{N\{\Re\Phi(0,t)+\Re\Theta(t,0)
                         -\gamma[(1-\cos u)+(1-\cos v)]\}}.
 \tag{33}
\]
The central and vertical comparisons are thus the complete-boundary
ones already proved, with both outside losses retained. Outer physical
trace nodes use the two full global estimates, which retain these
losses and a fixed internal loss. The latter pays the small action
change in (29). This proves a common positive real-period loss for
(27). The local common packet, derivative bounds and separate
spectral degrees at most \(N-1\) then give a common quadratic
strip by the same near/far polynomial continuation argument as in
Lemma 3. All original first normals are retained throughout.
When the inputs have common marked positive charts, the small selected
angle lies in both; the usual marked gluing and original period
equation identify the stationary action and its additive complete
volume anchor. \(\square\)

## 8. One separator threshold for all positive pairs of powers at least seven

**Corollary 3.** The full kernels of all ordered pairs
\(n,p\ge7\), their mirrors \((-n,-p)\), and the two
pairs \((3,3),(-3,-3)\) form one uniform kernel family.
Consequently there is one finite separator and closing threshold
\(B\) in Corollary 2, valid for arbitrary fixed choices of these
pairs. It is independent of their powers, the number of blocks,
their order, and their mirror choices. Every word and every power
are still fixed before taking the level limit.

*Proof.* Apply Lemma 4 to the uniform singleton family of Lemma 3
and the bare edge. The exact identity is
\[
 \phi_N^{(t)}[R(t)^pP_{n,N}(u,t)K_N(t,v)]
       =E_{+;n,p,N}(u,v).
 \tag{34}
\]
Thus all \(n\ge7,p\ge B_0\) have common kernel estimates.
Interchanging the two selected traces gives
\[
 E_{+;n,p,N}(u,v)=E_{+;p,n,N}(v,u),
 \tag{35}
\]
so the same estimates cover \(n\ge B_0,p\ge7\).
Increase \(B_0\) to at least eight if necessary. The uncovered
square \(7\le n,p<B_0\) is finite. Theorems 6–7 of the
[full pair-source proof](research_internal_pair_combined_contour_reduction.md)
provide its actual packets, ordinary boundary derivatives,
whole-period estimates, and original marked volume phases. Taking
the finite minimum with the common large-power constants fills this
square. Exact conjugation supplies the mirrors. Adding the two
already proved three-crossing pairs makes another finite enlargement.
This proves the first assertion, including the common marked charts.

The induction of Section 3 of the finite-kernel theorem uses the
kernel collection only through its common radii, curvature,
normalized phase bounds and exponential strip estimates. Lemmas
3–4 and the preceding finite enlargement supply exactly those
constants for the present infinite family. The actual original
terminal sources \(T(R^a)\), \(|a|\ge2\), already have the
required uniform initial constants by the uniform terminal theorem.
Choose the invariant class and then its separator and closing
thresholds in the same order as that induction. Their finite
maximum is one \(B\) independent of every pair in the family.
The amplitudes, error constants and first valid levels of a fixed
output word may depend on all its powers; they do not enter this
threshold selection. This proves the second assertion.

All annular boundary markings, original carrier powers and component
tests in Corollary 2 remain in force. For each resulting literal knot
closure, its full-level Kashaev asymptotic and volume identity are
therefore still (16), now with this single \(B\). \(\square\)

This conclusion removes the finite-list restriction on allowed pair
powers. It supplies no explicit small value of \(B\), and does not
allow adjacent blocks with an ineligible separating power. In
particular it is not an all-but-finitely-many theorem for an arbitrary
original template.

## 9. What an exact zero-power join does

There is an exact simplification at separator zero, but its output
is a different block. To specify it without losing a marked rotation,
first distinguish the quantum transform \(\mathsf T\) from the
physical quarter-turn \(T\). The full original Frobenius algebra
has \(\mathsf T^2=I\). Define the kernel operator
\(\mathsf E_{n,p}F=\phi_N[F E_{+;n,p,N}]\). Then
\[
 \mathsf E_{n,p}=\mathsf T R^p\mathsf T R^n\mathsf T,
 \qquad
 \mathsf E_{r,s}\mathsf E_{n,p}
 =\mathsf T R^s\mathsf T R^{r+p}\mathsf T R^n\mathsf T.
 \tag{36}
\]
This identity holds in the entire original algebra, so it includes
all first-normal data and every parity. In kernel form it says
\[
 \begin{aligned}
 &\phi_N^{(z)}
      [E_{+;n,p,N}(u,z)E_{+;r,s,N}(z,v)]\\
 &\quad=\phi_N^{(t_1)}\phi_N^{(t_2)}\phi_N^{(t_3)}
   [R(t_1)^nR(t_2)^{p+r}R(t_3)^s
     K_N(u,t_1)K_N(t_1,t_2)K_N(t_2,t_3)K_N(t_3,v)].
 \end{aligned}
 \tag{37}
\]
Indeed expand the left side, interchange its five finite traces,
and use \(\mathsf T^2=I\) at the zero-power middle vertex.
The neighboring multiplication operators combine as
\(R^rR^p=R^{r+p}\). Equivalently the original path word
\((n,p,0,r,s)\) reduces to \((n,p+r,s)\).
It does not become an arbitrary four-vertex adjacent word, and
(37) does not estimate either side asymptotically.

For the actual marked tangle, the corresponding local rule is
\[
                   T(R^0T(F))=T^2(F)=\tau(F),
 \tag{38}
\]
where \(\tau\) is the physical half-turn with endpoint permutation
\((02)(13)\). It carries all branches, crossings, ribbons and
peripheral marks. Section 4 of
[the marked degree-two moves](research_marked_degree_two_tangle_moves.md)
proves the merge \(p+r\) with precisely this transported rotation,
the reversed child order and the required branch rotations.
One must not replace \(\tau\) by the identity on an arbitrary
attached tangle merely because \(\mathsf T^2=I\) in the quantum
algebra. Closing components and the original carrier are checked
after this marked move.

**Corollary 4.** There is one finite \(B_{\rm zero}\) such that
all the zero joins (37) with \(n,p,r,s\ge7\) and
\(p+r\ge B_{\rm zero}\) form a uniform kernel family.
Their mirrors have the same assertion. They may be added to the
uniform library of Corollary 3, with a single enlarged separator
and closing threshold.

*Proof.* The right side of (37) is exactly
\[
 \phi_N^{(z)}[R(z)^{p+r}P_{n,N}(u,z)P_{s,N}(z,v)].
 \tag{39}
\]
Apply Lemma 4 with both input families equal to the singleton
family of Lemma 3. Its common long-power threshold is
\(B_{\rm zero}\). This proves the complete packet and boundary
estimates, including every original normal, not merely a formal
reduction. The marked zero move identifies its geometry with the
original zero join after carrying the half-turn and restoring the
neighboring fillings. The original component and carrier conditions
remain required. A union of two uniform kernel families is again
uniform by taking minima of their positive constants and maxima of
the finite upper bounds; the same invariant-class induction then
applies. \(\square\)

For positive powers at least seven the merged power is at least
fourteen. No bound \(B_{\rm zero}\le14\) has been proved, so
Corollary 4 does not settle every such zero join. More generally,
the map \((p,r)\mapsto p+r\) has infinite fibers when the original
powers are allowed both signs. Zero reduction cannot turn a finite
list of reduced exceptions into a finite list of original assignments;
see [the original-parameter obstruction](research_redundant_filling_parameters.md).

## 10. Checking the scalar margins

The proof of the uniform family is analytic. The focused checker
[check_uniform_pair_kernel_library.py](../experiments/check_uniform_pair_kernel_library.py)
reproduces its seven displayed scalar margins with exact fractions,
using \(25/8<\pi<22/7\). Its
[record](../repro/results/research-uniform-pair-kernel-library.json)
includes the proof and input-note hashes. These checks concern the
contraction, common discarded-region gaps and amplitude denominator.
They do not substitute for the exact trace, Schur-complement or
marked-topology arguments, and do not compute either threshold.
