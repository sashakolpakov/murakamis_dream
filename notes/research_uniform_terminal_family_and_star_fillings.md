# Uniform terminal estimates and stars with arbitrary fixed powers

The complete terminal-source theorem holds for every fixed signed power
of magnitude at least two. Its existing research statement allows all
constants to depend on that power. The composition theorem needs less
uniformity than a simultaneous limit: only its source charts, phase
curvature and exponential angular bounds must have common constants.
The polynomial prefactors, starting levels and \(O(N^{-1})\) errors may
still depend on the fixed power.

This note proves that weaker uniformity for all \(|p|\ge2\). Combined
with the proved common-circle composition theorem, it removes the
finite-set restriction on terminal powers. There is one finite threshold
on the number of leaves, valid for all fixed assignments of terminal
powers \(|p_\ell|\ge2\) and every fixed signed central power.

## 1. What must be uniform

Use the exact original terminal polynomial
\[
 H_{p,N}(u)=\phi_N^{(t)}\bigl(R^pK_N(t,u)\bigr),\qquad
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u).       \tag{1}
\]
No index or first normal is removed in (1). Let \(W_p\) be the
calibrated geometric boundary action and \(\epsilon_{p,N}\) its
known unit scalar. The desired estimates are
\[
 H_{p,N}(u)=\epsilon_{p,N}A_p(u)e^{NW_p(u)}
                           (1+O_p(N^{-1})),             \tag{2}
\]
on one common disk, and
\[
 |H_{p,N}(x+iy)|
 \le C_pN^{d_p}
       \exp N\{M_p-c(1-\cos x)+C_1y^2\},\qquad
 M_p=\Re W_p(0),                                        \tag{3}
\]
on one common whole-period strip. The positive constants \(c,C_1\)
and its width are to be independent of \(p\).

We also require a common holomorphic bound on the phase derivatives,
a lower bound
\[
                    -\Re W_p''(0)\ge a_{\min}>0,        \tag{4}
\]
and a common disk on which \(A_p\) is nonzero. A positive common
lower bound for \(|A_p(0)|\) is unnecessary and in fact false:
that amplitude is of order \(|p|^{-3/2}\) for large \(|p|\).

## 2. Compactifying the large powers in the original local phase

First let \(p\ge64\), \(s=1/p\), and use the exact local edge action
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                  \bigl(\tan(t/2)\cos(u/2)\bigr).
\]
The selected terminal equation is
\(\psi_t(t,u)+ipt/(2\pi)=i\).
Writing \(t=s\zeta\) gives
\[
                  \zeta=2\pi+2\pi i\,\psi_t(s\zeta,u).   \tag{5}
\]
This equation is holomorphic at \(s=0\).

For clarity, it admits a uniform elementary contraction. On
\(|t|,|u|\le1/4\), differentiating the displayed formula and bounding
\(\tan,\sec,\cos\) by their hyperbolic majorants gives
\[
 |\psi_{tt}(t,u)|<1/5,\qquad |\psi_t(t,u)|\le |t|/5.       \tag{6}
\]
For example \(|\tan(t/2)|<0.127\), \(|\cos(u/2)|<1.008\),
\(|\sec(t/2)|^2<1.017\), and
\(|1+\tan^2(t/2)\cos^2(u/2)|^{1/2}>0.991\);
these bounds give (6) directly. They also keep the continued square
root away from zero.

For \(|s|\le1/64\), \(|\zeta|\le7\), the right side of (5) has
modulus at most \(2\pi+14\pi/320<7\), and its derivative in
\(\zeta\) has modulus less than \(2\pi/320<1/50\).
Thus (5) has a unique jointly holomorphic solution on a neighborhood
of this closed parameter set, with
\[
 \zeta(0,u)=2\pi,\qquad |t_s(u)|\le7/64.
\]
It is the same selected branch as in
[the large terminal-power theorem](research_terminal_large_fixed_powers.md),
by its uniqueness near zero.

The exact stationary action becomes
\[
 W_s(u)=\psi(s\zeta(s,u),u)
                 +\frac{is}{4\pi}\zeta(s,u)^2-is\zeta(s,u). \tag{7}
\]
It is jointly holomorphic including \(s=0\), where
\(W_0(u)=\psi(0,u)\). In particular all its fixed derivatives are
uniformly bounded on smaller common disks. At completeness,
\[
 W_s''(0)=-\frac{\cos(t_s(0)/2)}{2\pi}.                   \tag{8}
\]
Hence \(-\Re W_s''(0)>1/(4\pi)\) for real \(0\le s\le1/64\).
Shrinking the common \(u\)-disk makes the corresponding real Hessian
bound uniform throughout it.

The leading amplitude from the original trace is
\[
 A_p(u)=i\sqrt{\frac2\pi}\,
 \frac{a_e(t_p(u),u)\sin t_p(u)}
 {\sqrt{-\psi_{tt}(t_p(u),u)-ip/(2\pi)}} .
\]
Its rescaling is the holomorphic function
\[
 s^{-3/2}A_{1/s}(u)
 =i\sqrt{\frac2\pi}\,a_e(s\zeta,u)
 \frac{\sin(s\zeta)/s}
      {\sqrt{-s\psi_{tt}(s\zeta,u)-i/(2\pi)}}.            \tag{9}
\]
The quotient in the numerator takes value \(\zeta(0,u)=2\pi\)
at \(s=0\). Its denominator is nonzero by (6), and the known edge
amplitude has no zero in this chart. Also \(|s\zeta|<1/4\), so
\(\sin(s\zeta)\ne0\) for \(s\ne0\). Thus (9) has no zero on a
common disk, with a common upper and lower modulus bound after
shrinking it. Only the removed scalar factor \(s^{3/2}\) tends
to zero.

Negative powers are covered by the exact conjugacy of the original
terminal coefficients:
\(W_{-p}(u)=\overline{W_p(\overline u)}\), with the correspondingly
conjugate amplitude and original unit scalar. All modulus, derivative
and real-curvature bounds are unchanged. The physical internal
critical angle is \(-\overline{t_p(\overline u)}\); it remains below
the real axis.

## 3. A common source disk, with all trace currents retained

Holomorphy of the classical expressions alone is not the source
assertion (2). The proof of the source expansion must use a common
boundary disk. We check that point directly in the large-power
contour argument.

Set \(a_0=6/25\). The proved complete-parent estimates for \(p\ge64\)
are
\[
\begin{split}
 0<M_\infty-M_p&\le\Delta,\qquad
                 \Delta=\pi\sec(\pi/32)/64^2,\\
 M_\infty-\psi(a_0,0)&\ge a_0^2/(4\pi),\\
 \text{omitted original wire rate}&\le M_\infty-\pi/100 .
\end{split}                                             \tag{10}
\]
Both gaps
\[
 \delta_{\rm wire}=\pi/100-\Delta,\qquad
 \delta_{\rm outer}=a_0^2/(4\pi)-\Delta
                                                               \tag{11}
\]
are strictly positive and independent of \(p\). The Hermite estimates
include \(R^p\) and the full trace; only their polynomial prefactors
may depend on \(p\).

The selected angle satisfies \(|t_p(u)|\le7/64\). Near \(u=0\),
put \(Q_e(t,u)=\psi_t(t,u)/t\). It is holomorphic, and on a sufficiently
small common chart \(\Re Q_e<-c_e<0\). The exact critical identity
\[
 t_p(u)=\frac{2\pi/p}{1-2\pi iQ_e(t_p(u),u)/p},\qquad
 \Im t_p(u)=
 \frac{4\pi^2\Re Q_e(t_p(u),u)}
      {p^2|1-2\pi iQ_e(t_p(u),u)/p|^2}                  \tag{12}
\]
shows that the lower contour depth is positive and comparable to
\(p^{-2}\) throughout the common complex boundary disk.
No fixed positive lower depth independent of \(p\) is asserted.

On the complete central rectangle, after reducing the common boundary
radius if necessary, one has \(\Re\psi_{tt}<-c'_e<0\).
The signed quadratic chirp does not change that real Hessian.
The lower horizontal endpoint is separated from the selected real
coordinate by at least \(a_0-7/64>0\), up to the harmless
\(O(N^{-1})\) midpoint adjustment. Its action loss therefore has a
positive common lower bound. The real endpoint loss follows from
(10)--(11). Convexity in the vertical depth controls the complete
endpoint current between them, exactly as in the large-power proof.

The omitted-wire and outer-angle estimates extend to a small common
complex boundary disk by the separate polynomial degree bound and
the fixed gaps (11). The selected actions (7) have uniform derivative
bounds, so that same disk can be made small enough to preserve the
comparison with the selected action. The local edge expansion already
holds on a fixed complex chart. These are every region used in the
original contour proof.

The rational trace denominator still contains all its charges. At
depth \(h_p>0\), its nonleading terms lose \(h_p\), which is not a
uniform positive constant in \(p\). For each fixed \(p\), however,
this is an exponential loss and eventually gives \(O_p(N^{-1})\).
Thus the whole proof yields (2) on a common boundary disk, with the
error constant and starting level allowed to depend on \(p\).
This is exactly the uniformity needed here.

## 4. Uniform whole-period exponential bounds

On the retained wire contours the detailed
[weighted edge estimate](research_weighted_edge_contour_bound.md)
has angular constant \(1/20\), independent of \(p\).
It inserts the loss \((1-\cos x)/20\) into the entire lower
horizontal integral and its vertical current. The remaining original
terms have the uniform gaps (11). Consequently one may take, for
all \(p\ge64\),
\[
 c_{\rm large}=
       \min\{1/20,\delta_{\rm wire}/2,\delta_{\rm outer}/2\}>0
\]
in the real-boundary estimate
\[
 |H_{p,N}(x)|\le C_pN^{d_p}
                  e^{N\{M_p-c_{\rm large}(1-\cos x)\}}. \tag{13}
\]
The factor \(1/2\) suffices because \(1-\cos x\le2\).

Near zero, the common source disk, (7)--(9) and uniform phase Hessian
bounds give a common quadratic complex estimate. Away from a small
fixed zero neighborhood, (13) has a common strict gap. Cover that
fixed real spectral set by finitely many enlarged intervals which
preserve half the gap. The Bernstein--Walsh Green functions and the
separate degree \(N-1\) are independent of \(p\). One common thin
complex neighborhood therefore preserves a fixed fraction of the
gap for every \(p\). Combining the near and far regions proves
(3) with common \(c,C_1\) and strip width.

For the finitely many signed powers \(2\le|p|<64\), use their already
proved whole-source theorems listed in
[the verified terminal assembly](research_verified_terminal_fillings_and_long_remainder.md),
Section 2. Take the minimum of their positive radii, angular constants
and real curvatures, and the maximum of their finite derivative and
imaginary-quadratic constants, together with the large-power constants.
All are positive or finite as appropriate. The exceptional powers
\(2,-2\) use their calibrated actions; the exact scalar
\(e^{\pm i\pi N/2}\) remains separate.

**Proposition 1.** Estimates (2)--(4), the common phase derivative
bounds and the common nonvanishing amplitude disk hold simultaneously
for every signed integer \(|p|\ge2\). Their exponential and chart
constants are uniform. The prefactor \(C_pN^{d_p}\), the source error,
and the starting level may depend on the fixed \(p\).

The family of geometric charts is uniform as well. For large
\(|p|\), the actual original edge shapes lie in the fixed positive
chart because \(t_p(u)\) and \(u\) are small. Formula (12) gives the
correct positive core orientation even as its length tends to zero.
The remaining finitely many powers have their previously proved
positive charts. Taking their finite minimum proves the common chart
assertion, with every original filling curve retained. The details of
the marked geometry are in
[the common-block geometry](research_amplified_marked_block_geometry.md).

## 5. Bare edges and a fixed collection of zero blocks

One may add the full unfilled edge \(K_N(t,u)\) to this uniformly
controlled family. It has \(q=1\), local exponent \(-3/2\), and
phase \(\psi(t,u)\), with both diagonal curvatures \(1/(2\pi)\).
This is a full-source statement, not a declaration that its retained
wire approximation is exact.

Indeed the finite Hermite and interval bounds give a strict gap for
all omitted indices on the whole real boundary square. The retained
kernel has the whole-angle Gaussian bound proved in
[the edge packet proof](../papers/circle-tree-volume/edge-packet.tex).
Since the sum of the two angular losses is bounded on that square,
reducing their coefficient absorbs the omitted-index gap. The local
full expansion follows by comparing that same gap with
\(\Re\psi(0,0)\), then shrinking the complex chart. Polynomial
Bernstein--Walsh continuation extends the real global gap, while the
local expansion supplies the quadratic imaginary bound. Its original
positive edge geometry and boundary markings are unchanged.

Finally one may add any fixed finite collection of actual zero subtrees
from the all-zero theorem. Taking the minimum of the uniform terminal
constants and the finitely many extra positive constants again gives a
uniform family. The permitted types are therefore
\[
 \{\text{all terminal powers }|p|\ge2\}
 \ \cup\ \{\text{one unfilled edge}\}
 \ \cup\ \{\text{a prescribed finite list of zero subtrees}\}.   \tag{14}
\]
Every member has the full estimates used by the composition theorem,
a common positive chart, and exponent \(-3q/2\).

## 6. A volume theorem with no long coefficient

**Theorem 2.** There is a finite integer \(m_*\) such that the
following holds. Let an original star have \(m\ge m_*\) terminal
vertices, with independently chosen fixed signed powers
\[
                      |p_1|,\ldots,|p_m|\ge2 .
\]
Give its central original circle any fixed signed power \(n\).
For every carrier and component pattern giving a knot, the resulting
knot is hyperbolic and satisfies
\[
 \boxed{\displaystyle
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                         =\operatorname{Vol}(S^3\setminus K).}
                                                               \tag{15}
\]
The full original source has a nonzero asymptotic
\[
        \Omega_N N^{3/2}D\,e^{NS}(1+O(N^{-1})),\qquad
        |\Omega_N|=1,\quad D\ne0,\quad
        2\pi\Re S=\operatorname{Vol}(S^3\setminus K).     \tag{16}
\]
The threshold \(m_*\) is independent of every power in the assignment.
The powers are fixed before \(N\to\infty\); no error uniform in
level-dependent powers is claimed.

**Proof.** The proof of
[the common-circle source theorem](research_amplified_finite_block_source.md)
uses finiteness of its collection only to obtain the constants
(10)--(12) there and a common nonvanishing source disk. Proposition 1
establishes exactly those properties for all terminal powers.
Its entire proof therefore applies with this uniformly controlled
family. More explicitly, the aggregate real curvature is at least
\(ma_{\min}\), the aggregate imaginary curvature has modulus at
most \(mb_{\max}\), and its original-\(n\) completed-square estimate
is bounded by \(K/m\), with one constant \(K\) for every assignment.
Taking \(m_*\) to satisfy its explicit threshold inequalities proves
the scalar source theorem, since terminals have no other boundary
variables. The original \(m\) terminal carriers and central carrier
remain as their known unit scalars, each once.

The marked common-chart geometry proves the actual primitive central
cone filling and calibrates its absolute action, after the terminal
fillings. Once the center is filled, only the original main cusps
remain. There is no remaining long-filling argument or unverified
boundary assembly in this case. The original knot normalization has
only the known unit framing factors. This proves (15)--(16).
\(\square\)

With the enlarged family (14), the same argument gives a whole-boundary
packet after the arbitrary fixed central power, provided its number of
incidences exceeds the threshold for that fixed enlarged family.
Independently sufficiently long fixed fillings at its remaining circles
then give the volume identity as before.

This is a uniform theorem for stars and the stated substituted pieces.
It does not say that every tree or every short-filled connected region
has this form. Low-valence cores, terminal powers \(0,\pm1\), and
uncontrolled adjacent nonzero regions still matter for the full
cofinite-assignment goal.

## 7. Finite original-source normalization checks

The script
[check_amplified_mixed_block_composition.py](../experiments/check_amplified_mixed_block_composition.py)
compares original Newton crossing/multiplication matrices with nested
full physical derivative traces. Its pieces include terminal powers
\(2,-3,64\), a second star with powers \(-2,7,-65,3\), and a mixed
configuration containing a trivalent zero vertex, a bare edge with a
complex free angle, and terminals \(-2,5\). The zero block keeps both
of its distinct complex outside angles.

Run
~~~sh
python3 experiments/check_amplified_mixed_block_composition.py \
  --precision 100 \
  --output repro/results/research-amplified-mixed-block-composition.json
~~~

The [saved results](../repro/results/research-amplified-mixed-block-composition.json)
contain 48 comparisons at levels \(3,4,5,6\) and central powers
\(-2,0,1,3\). All passed at 100 decimal digits; the largest relative
difference is below \(1.84\cdot10^{-98}\). These calculations test
the exact source normalization, every normal derivative and the
placement of the original signed crossings. They do not measure
the sufficient multiplicity threshold or assert convergence uniform
in level-dependent powers.


