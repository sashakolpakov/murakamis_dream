# The complete incoming-height connector on the following disks

Research deduction, 7 November 2026. The completed saved-only connector
comparison proves a uniform positive gap on both full reduced following
disks. No new evaluation or minimum computation is performed in this
deduction. The source is the full vertical
join from a new following-reference height to the unchanged original
complementary path.

## 1. Original action, path and finite source

Retain the two full reduced disks
\[
 P_3=\{|c-(7/20-i/100)|\le83/1000\},\qquad
 P_4=\{|c-(3/10-13i/250)|\le3/50\}.
 \tag{1}
\]
On their original holomorphic half-chain sheet let \(a(c)\) be the
first attached leg, \(q(c)\) the last leg, and
\[
 \mathscr P(c)=H_{34}(c)-G(q(c),c),\qquad
 G(z,c)=g(z+c)-2g(z)-2g(c)+2\pi izc.
 \tag{2}
\]
These are the absolute pre-Gram action and original branches of
[the critical-curve theorem](research_mixed_three_four_following_critical_curve.md).
In particular \(q(c)\in O_4\) and
\(1/2<e^{2\pi\Im q(c)}<1\) throughout both disks.
No final Gram factor or new phase constant is introduced.

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\), use exactly
\[
 U_{0,N}(w,X)=\sum_{j<N}H_N(w,r^{-j})p_j(X)/P_j,
 \qquad
 C_{1,N}(X,Y)=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3.
 \tag{3}
\]
The coefficients \(H_N\) remain whole. Both parities, every
\(0\le j<N\), revived numerator rows and all zeros are retained.
There is no \(\kappa_N\), halfweight, \(d_N\), or Fourier
selection in (3).

The original complementary path is fixed:
\[
 \Gamma_+:[1/2+ih_{\rm pair},1/2]\cup[1/2,1],
 \qquad -7/200<h_{\rm pair}<0.
 \tag{4}
\]
For each base reference \(c_0\), define the oriented join
\[
 \gamma_{c_0}:[1/2+i\Im a(c_0),1/2+ih_{\rm pair}],
 \qquad
 \mathcal J_N^{c_0}(w,z)=N\int_{\gamma_{c_0}}
 U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},e^{-2\pi iz})\,da.
 \tag{5}
\]
The path in (5) is held fixed when differentiating in \(w,z\),
or after substituting \(z=q(c)\). No derivative of its
reference-dependent endpoints is taken.

Write \(\mathcal V_d(R)\) for the explicit whole-source ceiling
in [the vertical-connector theorem](research_mixed_transformed_vertical_connector.md),
equation (3). Set
\[
 d(c)=\max\{11/50,-2\pi\Im a(c)\},\qquad
 R(c)=e^{2\pi\Im q(c)}.
 \tag{6}
\]
Since \(-2\pi h_{\rm pair}<11/50\), the conditions
\(\Im a(c)<0\), \(d(c)<1/2\) put both endpoints of (5)
in the admitted nonpositive-height interval of that theorem.

## 2. The fixed certificate and its precise implication

**Certificate C.** The sole saved-only result prescribed by
[the reviewed connector protocol](research_mixed_three_four_following_saved_connector_protocol.md)
completed with all 1,024 prescribed cells positive, all guards
passed, and no provenance invalidation. Its output is
`repro/results/research-mixed-three-four-following-saved-connector-attempt01.json`.
Its SHA is
`9a9678c6dd85654bc3acf4c7e7a1e1418118eb97882bab4439c6ead188f0e07c`.
Its frozen manifest is
`repro/protocols/research-mixed-three-four-following-saved-connector.json`,
SHA `3d8a3ef687e446756340edd1a919f9558065893ed9364de4079704e730664424`.
The reviewed protocol and checker have hashes
`6be2872b0a1974ee91141f6159ea0a50186e0a43b36e19c7488aab50e00c52c8` and
`84bbeedb0f558d82be40791615de565f86084c27d87e980ae4762c3ef9c180ee`.

This certificate only decodes the whole-cell boxes and action bounds
of the completed saved-response result, SHA
`5bc3e5ff76ab5371e76bddb8d8fc32512ef16d9571d1991fb0c5f57dd39867c3`.
The earlier failed interval-inverse result, SHA
`e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b`,
remains unchanged. No roots, inclusions, Hessians, inverses, response
derivatives, actions or dilogarithms are recomputed.

The complete record contains 1,024 positive connector comparisons and
17 passed checks per cell. Its only new mathematical operations are
4,096 saved-interval decodes, 1,024 elementary ceiling evaluations and
1,024 comparisons. All forbidden-evaluation counters are zero; no cell,
failure or input was removed, and no refinement or retry occurred.
Read-only audits checked every identifier, guard, saved rational margin
sign and current hash: all 54 bindings, 11 inherited records and 189
dependency edges match. The earlier failed artifact and the completed
saved-response artifact remain unchanged. No checker was replayed and
no numerical minimum was extracted in these audits.

For each circle cell, Certificate C supplies outward bounds
\[
 \Im a<0,\qquad d(c)\le\Delta_k<1/2,\qquad
 R(c)\le R_k<1,
 \qquad
 \Re\mathscr P(c)-\mathcal V_{\Delta_k}(R_k)\ge m_k>0.
 \tag{7}
\]
The action lower bound is the saved full-cell real-initial margin
plus \(7/4\). Both maxima in \(\mathcal V\) are retained.
The certificate evaluates no new action or response and makes no
choice of a better height, radius, subdivision, or retry.

Define only symbolically
\[
                       \mu_J=\min_{k=1}^{1024}m_k>0.
 \tag{8}
\]
No numerical value of this finite minimum is asserted or computed.

**Proposition.** Throughout both full disks,
\[
 \Im a(c)<0,\qquad d(c)<1/2,\qquad
 \Re\mathscr P(c)-\mathcal V_{d(c)}(R(c))\ge\mu_J.
 \tag{9}
\]

*Proof.* The boundary height guards extend to each disk by the
harmonic maximum and minimum principles for \(\Im a\).
The ceiling is increasing in both \(d\) and \(R\), so (7)
gives the last inequality on the two complete circles.
Section 2 of the reviewed protocol proves, on this exact sheet and
height range, that
\[
                \mathcal V_{d(c)}(R(c))-\Re\mathscr P(c)
 \tag{10}
\]
is subharmonic. It keeps the maximum defining \(d\), the decreasing
concave radius primitive, and both branches of the convex increasing
quadratic maximum. Thus the maximum principle proves (9). Compactness
and the strict guards give an open collar of the two disks on which
the height conditions persist and the margin is at least \(\mu_J/2\).
No independent containing box is substituted for the actual sheet.
\(\square\)

## 3. Complete finite connector and fixed-base holomorphic jets

**Theorem.** There is a fixed
\(\varepsilon>0\) such that for each base \(c_0\in P_3\cup P_4\),
all \(|c-c_0|<\varepsilon\), every real ordinary color
\(w\in[-2,2]\), and every pair of fixed nonnegative integers
\(k,\ell\),
\[
 \left|\partial_w^k\partial_c^\ell
 \left[e^{-N\mathscr P(c)}
             \mathcal J_N^{c_0}(w,q(c))\right]\right|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{-\mu_JN/4}.
 \tag{11}
\]
The constants and neighborhoods are uniform over the compact base
family. The same bound holds on a sufficiently small fixed complex
ordinary-color disk about \(-2\), with a smaller disk for derivatives.
It includes both level parities.

For bases \(c_0\) in any original clipped domain
\(K=A_3,O_3,A_4,O_4\), let \(\mathcal P(w,z)\) be the original
local holomorphic pre-Gram action of
[the following plateau theorem](research_mixed_three_four_following_plateau_source.md),
so \(\mathcal P(-2,q(c_0))=\mathscr P(c_0)\).
On sufficiently small fixed bidisks about \((-2,q(c_0))\),
\[
 \left|\partial_w^k\partial_z^\ell
       [e^{-N\mathcal P(w,z)}\mathcal J_N^{c_0}(w,z)]\right|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{-\mu_JN/4}.
 \tag{12}
\]
Again the base path is fixed and the constants are uniform on each
compact \(K\).

*Proof.* For a fixed base, all heights of (5) are bounded by
\(d(c_0)\). At \(c=c_0\), (9) pays the exact ceiling
\(\mathcal V_{d(c_0)}(R(c_0))\). Uniform continuity on the compact
base set permits the same fixed path, with nearby outgoing radius,
while keeping at least half this reserve below \(\Re\mathscr P(c)\).
Use the complete-source theorem with an aggregate tolerance less than
\(\mu_J/8\). Its all-real-color bound and polynomially bounded
path length, including the original prefactor \(N\), give a
normalized rate at most \(-3\mu_J/8\) before fixed derivatives.
The same theorem provides a small complex-color disk with an arbitrarily
small prescribed tolerance. Whole-interval Markov bounds apply to the
ordinary color before normalization; Cauchy bounds apply to the fixed-path
holomorphic function in \(c\), or in the small complex color disk.
Weakening to \(-\mu_J/4\) proves (11).

For (12), use continuity of the original local action and of the
outgoing-radius ceiling on a small fixed bidisk about its base.
The value gap again exceeds \(\mu_J/2\) before source tolerances.
The exact finite source (5) is holomorphic on that bidisk. Cauchy
applied to the normalized holomorphic function, on a smaller bidisk,
gives all fixed mixed derivatives with the same weakened exponent.
There is no division by a possibly vanishing cap or conditional sum.
\(\square\)

The normalization in (11) is the complete-left-color action even when
bounding other real colors. It does not assign those colors a new
critical action. The angular loss required by a subsequent ordinary
observation is not inferred solely from this normalization.

The join (5) now connects the new right-horizontal endpoint to the
unchanged \(\Gamma_+\) of (4). An exact full-prefix assembly may use
it together with the separately proved initial, left-taper, plateau,
right-horizontal, and complementary sources, preserving their
orientations and common normalization. This note does not itself
perform that assembly or evaluate either sector of the next Fourier
transfer. Its final Gram contraction, selected-sector comparison,
and arbitrary short-filling closure remain separate obligations.
