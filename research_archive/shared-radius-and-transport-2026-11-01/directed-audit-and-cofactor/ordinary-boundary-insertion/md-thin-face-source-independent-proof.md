# Independent source proof for thin triangular attachments

Private research, 1 November 2026. This note independently checks the source argument in sections 3–7 of `md-thin-face-source-certificate-extension.md`. No public file is changed. The actual local source estimates and finite-Hermite/Morse-period interfaces are those currently published at commit `4a72b9f966633aca68765c9f412960b058a3b076`.

The source argument closes, subject to the precise geometric disk lemma stated below. In particular, no additional certificate for the newly positive boundary variables is being assumed. The explicit zigzag cores admit one complete-vector witness for **every** locally allowed noncentral string, not only a complete central minimum. The checks below are algebraic and uniform in every fixed finite chain length. The numerical inequalities used in the construction are only three fixed constants with explicit Fourier-series remainder bounds.

## 1. Exact hypotheses and the geometric input kept separate

For a triangle write
\[
 Q(w_1,w_2,w_3)=\max_{\alpha_i\ge0,\ \sum\alpha_i=1/2}
 \left(\sum_i f(\alpha_i)+\sum_{w_i>0}\alpha_i\log w_i\right),
 \qquad f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
\]
with zero loads at zero weights. At an ordered quartet \((x,b,c,y)\), the actual phase-uniform, real-spectral upper rates are
\[
 X=Q(x,b,y)+Q(x,c,y),\quad
 A_L=\max\{\log c,Q(x,b,y)+\tfrac12\log c\},\quad
 A_R=\max\{\log b,Q(x,c,y)+\tfrac12\log b\}.
 \tag{1}
\]
A side overloading a zero protected coordinate is absent. These estimates apply to the actual cleared Casimir source, including the unused spectral factors at both parities; they are not claims about a positive replacement of that source.

Let B be a fixed marked simple matched sphere whose protected edge is uv. Choose the oriented root quartet \((u,a,v,b)\), with removed triangle \((u,b,v)\). The fresh block interior is
\[
 I_B=V(B)\setminus\{u,v,b\},\qquad |I_B|=R_B-1.
\]
It has an unabridged certificate: at \(u=v=0,b=1\), every locally allowed noncentral string has a finite positive interior witness with rate at most \(\Phi_B-\gamma_B\), for one \(\gamma_B>0\). A cover that omitted strings only because their old shared coefficient was zero would not suffice.

The geometric input is the following particular disk statement, rather than an exact quantum star–triangle identity. For all positive boundary weights, and continuously at the supported corner \(u=v=0,b>0\),
\[
 \inf_{q_{I_B}}\left\{\sum_{t\subset P_B}Q_t-\sum_{i\in I_B}q_i\right\}
       =Q(u,v,b)+\Phi_B.
 \tag{2}
\]
At the corner the infimum has a unique finite positive minimizer after b is fixed; the interior objective is coercive. Its conditional minimizers converge to that corner minimizer as \(u/b,v/b\to0\). Geometry is checking this statement from strict supported loads and development. Positive Hessian alone would not prove its coercivity; no such inference is used below.

For the closed block expression, still with no target at u or v, define
\[
 \widehat G_{B,\omega}=
 \sum_{e\subset B}A_{e,\omega_e}-\sum_{i\in I_B}q_i-\log b,
 \quad T=Q(u,v,b),\quad \Delta=2T-\log b.
 \tag{3}
\]
The simplex vertex at b gives \(\Delta\ge0\). Restoring the removed triangle in (2) gives
\[
 \inf\widehat G_{B,C}=\Phi_B+\Delta.
 \tag{4}
\]
All these expressions are invariant under simultaneously scaling the entire boundary and interior vector: there are \(R_B\) degree-one rates and exactly \(R_B\) subtracted targets. Thus the normalization b=1 causes no change of the source demands.

## 2. All newly allowed strings are controlled

There is a fixed \(\eta_B>0\) such that every noncentral string locally allowed at a boundary triple with
\[
 0\le u/b,\ v/b\le\eta_B
 \tag{5}
\]
has a positive interior witness for
\[
 \widehat G_{B,\omega}\le\Phi_B-\gamma_B/2.
 \tag{6}
\]
For the central string take the minimizer in (4). All these choices can satisfy \(a\ge v\).

To prove this, set b=1. For the finitely many strings already allowed at the old protected corner, retain one of their certified interior vectors. Every old triangle contains a positive ordinary weight, since its vertices are distinct and only u and v were zero. Q is continuous on this supported compact boundary square. Every overloaded ordinary middle remains positive and fixed, so the finite maximum in (1) is also continuous. Hence all old inequalities persist with half their margin on one common sufficiently small square.

A newly allowed string has a side overloading u or v. Use one fixed positive interior vector, for example the central corner minimizer. If w denotes one of these overloaded coordinates, then that factor is at most
\[
 \max\{\log\eta,\ C+\tfrac12\log\eta\}\longrightarrow-\infty
 \quad (0<w\le\eta\to0).
 \tag{7}
\]
Every other local rate has a uniform upper bound on the same square: positive interior coordinates are fixed, Q remains finite and continuous, and small middle logarithms can only decrease their terms. There is no compensating positive infinity. This proves (6) uniformly in the relative rates at which u and v approach zero. At an exactly zero overloaded coordinate the string is absent, so no evaluation of a nonexistent finite term is required.

The old witness list and the extra chosen vector are finite, with positive a-coordinates. The central minimizer has the same property by (2). Reducing \(\eta_B\) again makes \(a\ge v\) for all of them. This proves the claimed uniform extension rather than presuming certificates for a different mark.

The uniformity here concerns a finite-dimensional **rate inequality**. Later quantum estimates need only the finitely many fixed weight vectors of the final diagram; no uniform-in-N theorem through a changing zero-pattern is assumed.

## 3. The bridge map and every target

Let a core have selected quartet \((u,v,c,b)\) and removed triangle \((u,v,b)\). The opposite boundary orientation of the block gives new quartet \((u,a,c,b)\). Put
\[
 Q_a=Q(u,a,b),\qquad Q_c=Q(u,c,b),\qquad T=Q(u,v,b).
\]
Assume \(a,c\ge v\); then monotonicity of Q gives \(Q_a,Q_c\ge T\). The label map is
\[
 C\mapsto(C,C),\qquad L\mapsto(L,C),\qquad R\mapsto(C,R).
 \tag{8}
\]
In particular, the new right side overloads a and maps to the block's actual right side; it is not mapped to a reflected left sector with different original faces.

The central equality is
\[
 X_{\rm new}=Q_a+Q_c=X_D+X_B-2T.
\]
For the left side,
\[
 A_{D,L}+X_B-2T
 =\max\{q_c+Q_a-T,Q_a+q_c/2\}
 \ge\max\{q_c,Q_a+q_c/2\}=A_{{\rm new},L}.
 \tag{9}
\]
For the right side,
\[
 X_D+A_{B,R}-2T
 =\max\{q_a+Q_c-T,Q_c+q_a/2\}\ge A_{{\rm new},R}.
 \tag{10}
\]
These are exact inequalities between the rate functions, with no reassignment of shared radii. Every noncentral output string has at least one noncentral induced input string.

The number of matching regions is \(R_D+R_B-1\): the two old root matching edges become one. The vertex count is \(V_D+V_B-3\), also giving \(R_D+R_B-1\) ordinary targets. The core already pays once for each of its ordinary u,v,b. The block expression pays nothing at u,v and pays once at b. Thus adding the two input functions pays for b twice but for u and v only once. All block interior vertices are fresh. Consequently
\[
 G_{{\rm new},\omega}
 \le G_{D,\omega_D}+\widehat G_{B,\omega_B}-2T+\log b
 =G_{D,\omega_D}+\widehat G_{B,\omega_B}-\Delta.
 \tag{11}
\]
The sign and coefficient of \(\Delta\) are essential. Subtracting just T, or adding targets at the newly positive u,v inside the block, would be wrong.

Using (4) for the central string, conditional minimization in every fresh block interior cancels \(\Delta\) exactly. Hence the completed source potential satisfies
\[
 \Phi_{\rm new}=\Phi_D+\Phi_B.
 \tag{12}
\]
It also follows that the complete core coordinates are unchanged by the attachment. Neither statement is an equality of finite quantum polynomials.

## 4. Finite witnesses, including multiple attachments

Suppose one witness has been chosen for every locally allowed noncentral core string, with gap \(\gamma_D>0\); choose the complete vector for its central string. Require each selected vector at every intended attachment to satisfy (5) and \(c\ge v\). Then use the corresponding block witness from section 2 at those **same** core boundary coordinates.

If the block string is central, (4) cancels \(\Delta\) in (11), preserving the core gap. If the block string is noncentral, (6) and \(\Delta\ge0\) preserve at least \(\gamma_B/2\). The central core witness has value exactly \(\Phi_D\). Thus every noncentral assembled string has a witness of rate at most
\[
 \Phi_D+\Phi_B-\min\{\gamma_D,\gamma_B/2\}.
 \tag{13}
\]
No coefficient-support omission is needed anywhere in this argument.

For k attachments at distinct core matching regions, retain one induced core string and choose **one** of its witnesses, then choose each block witness at its boundary triple. Fresh block interiors are disjoint. Boundary vertices may coincide, even with different roles in different attachments: every block still has no targets at its own u,v and exactly one extra target at its own b. Therefore the added correction is precisely \(-\sum_i\Delta_i\), including repeated occurrences of the same b. Cancellation is occurrence-by-occurrence in the auxiliary sum; the final diagram still has only one target for that core face.

The resulting gap is at least \(\min\{\gamma_D,\gamma_{B_1}/2,\ldots,\gamma_{B_k}/2\}\), and
\[
 R_{\rm new}=R_D+\sum_i(R_{B_i}-1),\qquad
 \Phi_{\rm new}=\Phi_D+\sum_i\Phi_{B_i}.
 \tag{14}
\]
The distinct-region requirement prevents replacing the same original partner twice. Coincident boundary vertices do not cause a problem. The geometric gluing must of course keep the stated original oriented sphere and matching; this is a separate combinatorial construction, not an inference from (14).

## 5. The explicit zigzag core certifies every induced sector

Use the octahedral sphere and orientations in the candidate note. The matched complete weights are
\[
 P=S=1,\quad v_2=v_3=2,\quad v_0=v_1=0.
\]
The pole star equation follows from
\(2\arctan(1/\sqrt2)+\arctan(1/(2\sqrt2))=\pi/2\); the complementary corner equations give the rim stars. Set \(u=v_2=2,v=P=1,b_0=v_3=2,c=S=1\).

In the oriented triangle \((u,v,b_{j-1})\), stellar insertion gives exactly
\[
 F_j=(u,v,b_j),\quad A_j=(u,b_j,b_{j-1}),\quad
 B_j=(v,b_{j-1},b_j).
 \tag{15}
\]
The second triangle is the cyclic version of \((b_{j-1},u,b_j)\); thus every internal edge has opposite induced orientations. The unchanged outer partner is \((u,b_0,c)\). For positive even n, the matching consists of the root pair \((A_1,(u,b_0,c))\), the terminal pair \((F_n,A_n)\), the pairs \((B_j,B_{j+1})\) for odd j, and \((A_j,A_{j+1})\) for even j with \(1\le j<n\). A1 and An are used at the endpoints; A2 through A(n−1) pair consecutively; all B's pair consecutively. Every triangle occurs once, and the shared matching edges have opposite orientations. There are n+1 pairs in this replaced region, as required after n stellar insertions.

The exact inserted curvatures are
\[
 b_j=3j^2+4\sqrt2j+2=3(j+\sqrt2)(j+\sqrt2/3).
 \tag{16}
\]
They obey the displayed Descartes recurrence and leave the exterior weights unchanged. In particular the positive ratios \(r_j=b_j/b_{j-1}\) decrease strictly: each factor \((j+\alpha)/(j-1+\alpha)\) decreases for \(\alpha>0\).

Here is the full local source test, not just stationarity. At any surviving left side,
\[
 X-A_L=\min\{X-\log c,\ Q(x,c,y)-\tfrac12\log c\}.
 \tag{17}
\]
The analogous formula holds on the right. The second quantity is strictly positive whenever the overloaded triangle contains a further positive corner. To see this directly, move a small positive load from the overloaded simplex vertex to that corner. The entropy gain has positive leading order \(\varepsilon\log(1/\varepsilon)\), which dominates the finite linear change in the two logarithmic weights. Thus strict balance at both positive middles, together with this support fact, makes the **same complete vector** a strict witness for every noncentral string.

All matching regions satisfy these conditions:

* The two unchanged protected caps have outer weights 1,0 and middle weights 0,2. The surviving overloaded triangle is (1,2,0), with two positive entries. A quarter-quarter allocation gives
  \(X-\log2\ge2f(1/4)-(3/4)\log2>0.06\).
* The other unchanged pair has outer weights 2,0 and middle weights 1,1. Already the outer vertex allocations give \(X\ge\log2>0\).
* The new root has outer weights 2,2 and middles \(b_1,1\). The two stated allocations give exactly
  \(X-\log b_1\ge2f(1/12)+f(1/3)+2f(1/5)+f(1/10)+(17/30)\log2-(2/3)\log b_1>0.25\).
* An internal pair has outer weights \(s_j,b_j\), with \(s_j\in\{1,2\}\), and middles \(b_{j-1},b_{j+1}\), possibly in reversed order. Quarter-quarter allocations at \((b_j,b_{j-1})\) and \((b_j,b_{j+1})\) give
  \[
  X-\log b_{j+1}\ge4f(1/4)-\tfrac14\log(r_{j+1}^3r_j)
       \ge4f(1/4)-\tfrac14\log\frac{b_2^3}{2b_1^2}>0.09.
  \]
  This is an all-j proof, not a finite chain check.
* The terminal pair has outer weights \(2,b_n\) and middles \(1,b_{n-1}\). Its vertex/quarter-quarter allocations give
  \(X-\log b_{n-1}\ge2f(1/4)+(3/4)\log(b_n/b_{n-1})>0\).

Every surviving overloaded triangle in this list has another positive corner. For a fixed n take the minimum of the finitely many strictly positive quantities in (17) and their right versions. This is a positive \(\gamma_D(n)\), and the complete vector witnesses every locally allowed noncentral core string, including those with zero global coefficient. No unseen per-sector optimization or certificate is required. There is no assertion that \(\gamma_D(n)\) has a positive lower bound as n grows.

The three numerical constants used above have a rigorous elementary verification: \(\Lambda(x)=\sum_{k\ge1}\sin(2kx)/(2k^2)\) has truncation remainder at most \(1/(2K)\). The supplied interval script uses K=2048 and outward Arb arithmetic; its lower bounds exceed 0.06, 0.25 and 0.09 respectively. I inspected that remainder and the expressions, rather than treating sampled n-values as a proof. I have not rerun that script in this audit.

At the terminal face the ordered core quartet is exactly
\[
 (u,v,c_{\rm tip},b_n)=(2,1,b_{n-1},b_n).
\]
Hence \(c_{\rm tip}\ge v\), \(u/b_n=2/b_n\to0\), and \(v/b_n=1/b_n\to0\). Since **all** core strings use this same complete vector, choosing one sufficiently long even chain meets section 4's thinness condition for every induced core sector simultaneously.

## 6. Many interfaces and retained failure of weak balance

A finite number of strictly balanced octahedral cores can first be joined by the published protected operation while retaining each positive T2/Z2 pair. Their interior complete weights are unchanged after the common boundary scale is matched. The newly merged crossing is also strictly balanced: its rate is the sum of the old rates minus the singleton boundary term, and the remaining nontrivial triangle contributes strictly more than that singleton term. All surviving overloaded triangles retain a second positive corner. Thus the complete vector remains a witness for every noncentral string.

Build one even chain in each of these untouched positive disks. The separate source comparisons above apply at each root and internally; every other old comparison is unchanged. After a fixed finite choice of chain lengths this supplies one finite strictly balanced core with arbitrarily many distinct thin interfaces. Shared boundary vertices keep their single inherited weights. Attach any fixed finite list of unabridged certified blocks using section 4.

For the seventeen-region input, the public restricted dual certificate gives
\[
 A_{12,R}+\sum_{e\in\{2,4,7\}}H_e+
 \sum_{e\notin\{2,4,7,12\}}X_e-\sum_fq_f>\Phi_{17}+0.025.
\]
At its complete vector set \(\delta_e=\max(0,\log b_e-X_e,\log c_e-X_e)\), omitting protected logarithms. Then \(H_e-X_e=\delta_e\), and \(A_{12,R}-X_{12}\le\delta_{12}\), because the mixed branch differs by \(q_b/2-Q_b\le0\). Thus \(\sum_{e\in\{2,4,7,12\}}\delta_e>0.025\), so at least one defect exceeds 1/160. This quantitatively justifies the continuity argument; failure is not merely non-strict.

The input root is crossing 15 with quartet \((16,14,0,17)\) and removed triangle \((16,17,0)\), so the four possible failed comparisons are not changed by root merging. The overloaded face of the failed comparison is ordinary. By the conditional minimizer convergence in (2), sufficiently thin positive boundary data preserve this strict defect in the new complete packing. Consequently the resulting marked diagrams need not be weak-balanced, although this is not an assertion about every alternative mark or presentation of the resulting knots.

## 7. Transfer to the actual full invariant

Compile the new oriented matched sphere afresh by the exact general Morse source theorem. No finite polynomial factorization into the old blocks is used. At level N, every spectral degree is at most d=N−1, every new ordinary face has one degree-d target, and the protected mark and actual cup/cap, even coset and framing factors are those of that new diagram.

For each genuine noncentral string, take the assembled witness from section 4. The phase-uniform local estimates (1), followed by Cauchy coefficient extraction with those shared weights, give a rate below \(\Phi_{\rm new}\) by a fixed positive margin. Targets d rather than N and polynomial factors change the rate by o(1). There are finitely many strings for the fixed diagram, so
\[
 \limsup_{N\to\infty}\frac1N\log
 \|S_{N,\mathrm{full}}-S_{N,C}\|_{[-2,2]^{R_{\rm new}}}
 <\Phi_{\rm new}
 \tag{18}
\]
at both parities. No exchange of an N-limit with growing chain or block size occurs.

The exact finite-Hermite bound multiplies this by at most
\(\prod_e(1+|n_e|/2)\), retaining all repeated-node normal data and the original signed crossing multipliers. For fixed powers this has zero exponential cost. The independently proved general Morse theorem supplies the nonzero entire central period for the actual new simple sphere. Its selected action approaches \(\Phi_{\rm new}\) as every fixed signed filling becomes sufficiently long, and its primitive completion identifies \(2\pi\Re S\) with the actual filled knot-complement volume. Choose the threshold after the gap in (18). The complementary contribution then cannot cancel the central term, yielding
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
 =\operatorname{Vol}(S^3\setminus K).
 \tag{19}
\]
The half-twist pattern must pass the new diagram's original knot/no-extra-component test. The invariant is the reduced zero-framed complete-color invariant; the recorded unit-modulus character and the optional one-cut factor \(i^{N+3}/N\) remain of zero exponential rate. Thresholds may depend on the entire fixed construction and its certificate. No N-growing data, arbitrary stable-polynomial replacement, or uniform theorem for every undecorated sphere is asserted.

## 8. Status and dependencies

The new source implications proved here are sections 2–7 conditional on the geometric statement (2) and the literal oriented simple-sphere gluing. The independently audited local rates, exact Morse compiler, finite Hermite norm, and central-period/metric-volume theorem are used at their published scopes. The conditional disk geometry is being independently proved in the geometry lane and is not replaced by an assumed quantum contraction.

Dependencies checked at statement and normalization level:

- `actual_global_left_weighted_spectral_envelope.md`, especially sections 1 and 4: original unused rows, all face phases, both parities, whole real spectral interval; the reflected right sector retains its literal order.
- `actual_cross_cofactor_factorization.md`, section 8, and the global central cofactor proofs: the actual central source and its complete upper rate.
- `research_matched_sphere_morse_source.md`, sections 5–6: exact source at the original mark with all physical factors.
- `actual_uniform_filling_supremum_bound.md`, sections 1, 4–7: actual weighted Hermite functional, canonical spectral multidegree and no exponential filling cost for fixed powers.
- `actual_morse_cross_filling_period.md` and `actual_morse_geometric_contribution.md`: nonzero all-charge central contribution, fixed diagram, independent long signed slopes, actual primitive metric completion and absolute volume.
- `general_protected_triangular_sum_volume.md`, sections 2, 6–7: the protected preliminary core joins and the existing seventeen-region unabridged certificate/strict failure localization.

No public files or scientific artifacts were modified. No finite tests are used to infer the all-chain or all-level statements.
