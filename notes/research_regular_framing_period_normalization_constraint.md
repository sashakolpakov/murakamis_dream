# A normalization constraint on a regular framing-period reduction

Private written proof, 18 November 2026.

A uniformly bounded compact framing chain, with uniformly controlled
descending normal collars, contributes at most \(N^{1/2}\) times the
geometric exponential in the literal soft-cut braid presentation.
It cannot be declared the entire original framing period: the exact
normalization of an already known source forces a larger polynomial
coefficient. This is a consistency test on a proposed general source
map, not a new knot case or a defect in the local density theorem.

The complete proof directs are E, the literal Morse–Bott density;
A, the literal factorial amplitudes; and G, the exact whole-source
normalization and its written asymptotic. Their pins are below.

## 1. What a bounded regular source reduction would imply

Keep E's \(c\)-crossing braid, \(m=c+1\) occupation coordinates,
\(c_0=2\pi i\), and \(h=c_0/N\). Write
\[
 \sigma_*=\Phi_\theta(\zeta_*)/c_0,\qquad
 \Lambda=\operatorname{Re}\sigma_* .
 \tag{1}
\]
All original scalar factors are retained. For the canonical reduced
source at complete color, the occupation-independent factors in
\(E_N\) are unit root phases. They come from the common Cartan,
framing and pivotal scalar lines. A's exact signed formulas have
no additional uncancelled quantum-dimension or \((q-q^{-1})^{-1}\)
factor. The trace-one binomial multiplies the unnormalized diagonal
partial-trace summand; restoring an old cut-average \(N\) would
count it twice. An explicitly different convention containing the
whole modified dimension retains its \(N^{-1}\) at completeness
and is a different normalization.

Consider a proposed contribution obtained by integrating normal
collars over a piecewise smooth relative \(r\)-chain \(\gamma_N\).
Assume the following concrete local bounds.

* The chains lie in a fixed compact subset of finitely many regular
  marked source charts. Their mass includes absolute multiplicities,
  and satisfies \(\operatorname{mass}(\gamma_N)\le C\).
* The normal collars use uniformly controlled descending Gaussian
  coordinates for the actual phase, with bounded multiplicities and
  volume Jacobians. Their outer normal boundaries have a fixed
  strictly smaller real phase. All charts have the same marked
  critical phase \(\sigma_*\), up to recorded unit phases.
* The actual source on those collars is A's literal amplitude,
  including its binomial weight and E's original scalar line.
  Any other relative currents are retained separately.

The first two bullets are hypotheses on the proposed source map;
they are not consequences of a nonzero Hessian or of passing
through a geometric point.

Under these hypotheses the collar contribution \(J_N\) obeys
\[
                         |J_N|\le C' N^{1/2}e^{N\Lambda}.
 \tag{2}
\]
Here and below constants may depend on the fixed diagram and compact
charts, but not on \(N\).

To prove (2), use E's holomorphic Morse–Bott coordinates. On a
descending real normal ball, A's uniformly bounded amplitude gives
an integrable bound \(C e^{-aN|y|^2}\) after factoring out
\(e^{N\Lambda}\). The \(c\) normal variables therefore cost
\(O(N^{-c/2})\); the uniform strict phase loss treats their outer
boundary. The actual lattice measure and the \(c\) crossing plus
one binomial amplitudes contribute \(N^mN^{-m/2}\).
Thus their product is
\[
                N^{m/2}N^{-c/2}=N^{1/2}.
 \tag{3}
\]
Integrating over the bounded-mass \(r\)-chain proves (2), including
finite sums of these collars and unit-phase aliases.

Equivalently E computes their leading normal one-form as
\[
 E_N N^{1/2}(2\pi)^{c/2}c_0^{c/2-m}
 e^{N\sigma_*}\left(\omega_0+O(N^{-1})\right),\qquad
 \omega_0=C_\beta\,\frac{dr}{s_\theta},\quad C_\beta\ne0,
 \tag{4}
\]
with a uniform one-form error on these compact charts. Equation
(2) uses the mass bound, not only the signed endpoints of
\(\gamma_N\).

## 2. The original normalization rules out an exhaustive bounded model

G proves as a whole Laurent-polynomial identity that its original
reduced source has the specialization
\[
 K_N(4_1)=\sum_{k=0}^{N-1}
                  \prod_{j=1}^k4\sin^2(\pi j/N).
 \tag{5}
\]
Its proof keeps all cups, caps, Cartan scalars and the original
index-zero cut: the cup and cap powers of \(N\) cancel exactly.
Thus (5) has no hidden external normalization.

For clarity, the leading power in that same proof is explicit.
Put
\[
 V(x)=\int_0^x\log(4\sin^2\pi t)\,dt,\qquad x_*=5/6 .
\]
G's uniform factorial expansion near \(x_*\) gives
\[
 \prod_{j=1}^k4\sin^2(\pi j/N)
  =2N\sin(\pi k/N)e^{NV(k/N)}(1+O(N^{-1})).
 \tag{6}
\]
The endpoint-regularized remainder is uniform, and outside a fixed
neighborhood of \(x_*\) there is a strict exponential loss.
Moreover \(V''(x_*)=-2\pi\sqrt3\).
The sum supplies \(N\), the factor in (6) supplies \(N\), and
the one-dimensional Laplace integral supplies \(N^{-1/2}\).
With its exact positive coefficient, G obtains
\[
 K_N(4_1)=3^{-1/4}N^{3/2}e^{NV(x_*)}(1+O(N^{-1})).
 \tag{7}
\]
This invokes G's complete written normalization argument, not a
numerical fit or an imported new asymptotic claim.

Consequently a proposed general source reduction with the bounds
of Section 1 cannot exhaust the leading term of this same invariant.
Indeed, if
\[
 K_N(4_1)=J_N+R_N,\qquad
 R_N=o\!\left(N^{3/2}e^{NV(x_*)}\right),
 \tag{8}
\]
and \(J_N\) satisfies (2) at \(\Lambda=V(x_*)\), division by
\(N^{3/2}e^{NV(x_*)}\) makes the right side tend to zero.
Equation (7) makes the left side tend to \(3^{-1/4}\), a contradiction.
This tests the normalization of a universal proposed framing-period
map. It neither contradicts E's local statement nor changes the
volume exponential.

## 3. The precise requirement on an effective framing pairing

More generally suppose an actual source comparison, with its
remainder proved rather than suppressed, gives
\[
 K_N=u_N C\,N^{1/2}e^{N\sigma_*}
                          \bigl(P_N+\epsilon_N\bigr),
 \qquad |u_N|=1,\quad C\ne0,\quad \epsilon_N=o(N).
 \tag{9}
\]
If the same scalar has the normalization
\[
 |K_N|=C_*\,N^{3/2}e^{N\operatorname{Re}\sigma_*}(1+o(1)),
                       \qquad C_*>0,
 \tag{10}
\]
then
\[
                         |P_N|\sim \frac{C_*}{|C|}N .
 \tag{11}
\]
Indeed (9)--(10) determine
\(|P_N+\epsilon_N|=(C_*/|C|)N(1+o(1))\), and the difference
between this modulus and \(|P_N|\) is at most
\(|\epsilon_N|=o(N)\). No phase alignment beyond the recorded
unit \(u_N\) is needed for this conclusion.

The leading form in (4) has primitive \(C_\beta r/s_\theta\).
For a specified finite-endpoint chain its leading integral is
therefore its signed endpoint sum times \(C_\beta/s_\theta\).
That algebraic equality alone does not control the full source:
if the chain mass grows, its \(O(N^{-1})\) error can accumulate;
if it escapes, the compact-chart uniform bounds no longer apply.
A bounded signed endpoint sum is not a substitute for either bound.

Thus a global source comparison must determine which data provide
the missing polynomial scale: growing multiplicity or extent,
nonuniform endpoint/infinity layers, or other same-action relative
currents. This note selects none of these mechanisms and asserts no
actual framing pushforward. In particular it does not normalize the
remaining period to one or infer it from the local torsion coefficient.

## Complete proof-source pins

* E: notes/research_soft_cut_morse_bott_density.md, SHA256
  e411f25c7b66b61d865427db1e1f789aeb09b9c76471a303dfdb8d7673fe6f9a.
* A: notes/research_literal_crossing_slit_chart_amplitude.md, SHA256
  c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.
* G: notes/figure_eight_whole_source_identity.md, SHA256
  63738069644ac40aa05fcb860e2de8edbb09c06ac2976f522cc1c3acc94e3951.

All three complete directs were read nontruncated in the active
author sequence, their used implications checked and unchanged
whole reads explicitly retained where applicable. Only written
mathematics and text/hash operations were used. Frozen/public
files are unchanged.
