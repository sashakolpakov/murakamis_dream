# A fixed source sector beyond the shared-radius envelope criterion

The local source polynomial splits into its central, left and right recurrence-path pieces, conventionally labeled CROSS, LEFT and RIGHT (C, L and R). This note gives an obstruction to a sufficient coefficient-estimation method, not to the volume conjecture. It uses one actual fixed marked simple-sphere source, one genuine left label, and central at every other crossing region. There are no unrestricted spectator labels and no mixtures between different genuine spectator sectors.

## 1. The precise disproved statement

For a fixed original source, retain its two protected zero variables and every ordinary target \(d=N-1\). At each crossing region \(e=(x,b,c,y)\), put
\[
 X_e(L)=Q(L_x,L_b,L_y)+Q(L_x,L_c,L_y),\qquad
 A_{e,L}(L)=\max\{\log L_c,Q(L_x,L_b,L_y)+\tfrac12\log L_c\}.
                                                        \tag{1}
\]
Here the triangle action, including its absolute source normalization, is
\[
 Q(w_1,w_2,w_3)=\max_{\substack{a_i\ge0\ (w_i>0)\\\sum a_i=1/2}}
       \sum_{i:w_i>0}\{f(a_i)+a_i\log w_i\},\qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
\]
where \(\Lambda(t)=-\int_0^t\log|2\sin u|\,du\). Zero-weight corners are omitted; a triangle with one positive weight \(w\) has action \(\frac12\log w\). A left label with protected overloaded middle \(c\) is absent. The analogous right rate overloads \(b\).

For a genuine fixed label string \(\sigma\), the convex weighted-envelope capacity is
\[
 \mathcal C_\sigma=\inf_{L_f>0\ (f\text{ ordinary})}
 \left[\sum_e A_{e,\sigma_e}(L)-\sum_{f\text{ ordinary}}\log L_f\right],
 \qquad A_{e,C}=X_e.                                   \tag{2}
\]
All face coordinates in (2) are shared, and the protected variables remain zero. Write \(\Phi=\operatorname{Vol}(Y)/(2\pi)\) for the actual complete augmented action.

**Theorem.** There is an actual connected marked simple-sphere source with \(54\) crossing regions and a genuine string consisting of left at region \(32\), central at all other \(53\) regions, for which
\[
                    \mathcal C_\sigma>\Phi+\frac15.     \tag{3}
\]
The source admits a parity pattern whose original main strands form a knot. Thus restricting the conjectured method to original knot-producing diagrams does not remove this example.

Consequently the universal assertion \(\mathcal C_\sigma<\Phi\) for every genuine non-central string is false. Further subdivision only by the C/L/R labels cannot repair this particular singleton. The theorem does **not** assert an exponential lower bound for the signed shared coefficient, the full-minus-central spectral supremum, the filled period, or a knot invariant. It does not contradict any volume equality.

## 2. The original oriented source

The white sphere has vertices \(0,\ldots,55\), \(108\) oriented triangles, and \(162\) edges. Its exact construction starts with the oriented tetrahedral boundary
\[
 (0,1,2),\ (0,3,1),\ (1,3,2),\ (0,2,3),
                                                        \tag{4}
\]
then performs \(52\) stellar subdivisions and \(487\) legal diagonal flips. The full move list is in `actual_singleton_sector_obstruction_certificate.json`. The verifier checks each old face or oriented adjacent pair before the move, forbids an already existing new diagonal, and checks the resulting oriented incidence. Each operation preserves a simple triangulated oriented sphere.

The same certificate records a perfect matching of its dual triangles. For each ordered quartet \((x,b,c,y)\), the two actual oriented faces are \((x,b,y)\) and \((x,y,c)\); the source polynomial reads \(H(x,b,c,y)\). The complete list below fixes all source incidences. The mark is the nonmatching edge \(29\text{--}50\). Thus precisely \(29,50\) are protected, and all other \(54\) face targets are \(d\).

| Crossing | Ordered quartet | Crossing | Ordered quartet |
|---:|:---|---:|:---|
| 0 | \((26, 28, 38, 12)\) | 27 | \((27, 39, 29, 51)\) |
| 1 | \((7, 29, 26, 51)\) | 28 | \((29, 50, 45, 22)\) |
| 2 | \((15, 13, 8, 0)\) | 29 | \((51, 39, 3, 31)\) |
| 3 | \((8, 0, 5, 6)\) | 30 | \((1, 25, 3, 28)\) |
| 4 | \((15, 8, 13, 5)\) | 31 | \((3, 28, 51, 46)\) |
| 5 | \((2, 25, 33, 35)\) | 32 | \((0, 50, 16, 29)\) |
| 6 | \((52, 54, 48, 24)\) | 33 | \((22, 50, 32, 17)\) |
| 7 | \((3, 9, 11, 25)\) | 34 | \((10, 30, 45, 29)\) |
| 8 | \((47, 11, 34, 53)\) | 35 | \((29, 41, 16, 44)\) |
| 9 | \((9, 3, 55, 54)\) | 36 | \((24, 31, 27, 39)\) |
| 10 | \((18, 37, 13, 0)\) | 37 | \((27, 29, 24, 48)\) |
| 11 | \((54, 52, 12, 48)\) | 38 | \((42, 37, 40, 23)\) |
| 12 | \((36, 5, 18, 6)\) | 39 | \((23, 45, 40, 0)\) |
| 13 | \((18, 13, 36, 5)\) | 40 | \((28, 26, 46, 51)\) |
| 14 | \((4, 33, 25, 35)\) | 41 | \((11, 25, 53, 1)\) |
| 15 | \((10, 45, 6, 23)\) | 42 | \((34, 53, 47, 1)\) |
| 16 | \((18, 6, 37, 43)\) | 43 | \((2, 33, 25, 28)\) |
| 17 | \((21, 41, 7, 29)\) | 44 | \((31, 24, 3, 54)\) |
| 18 | \((41, 0, 44, 16)\) | 45 | \((14, 32, 45, 0)\) |
| 19 | \((7, 26, 0, 49)\) | 46 | \((40, 0, 42, 37)\) |
| 20 | \((38, 12, 26, 49)\) | 47 | \((43, 6, 37, 19)\) |
| 21 | \((17, 50, 32, 0)\) | 48 | \((6, 23, 19, 37)\) |
| 22 | \((30, 10, 29, 48)\) | 49 | \((4, 20, 12, 54)\) |
| 23 | \((14, 45, 32, 22)\) | 50 | \((28, 33, 12, 4)\) |
| 24 | \((6, 12, 10, 48)\) | 51 | \((3, 11, 1, 47)\) |
| 25 | \((9, 20, 25, 4)\) | 52 | \((12, 6, 49, 0)\) |
| 26 | \((0, 41, 7, 21)\) | 53 | \((20, 9, 54, 55)\) |

In particular the selected quartet is
\[
 (x,b,c,y)=(0,50,16,29),\qquad (L_b,L_y)=(0,0).
                                                        \tag{5}
\]
It follows that its retained triangle is the singleton \(\{0\}\), while its overloaded middle \(16\) is ordinary. The selected local left polynomial is therefore not killed by the protected substitutions. Section 3 also proves that its shared coefficient, with all other regions central, is nonzero at every sufficiently large even level. Its exact envelope is especially simple:
\[
 A_{32,L}(L)=\max\{q_{16},(q_0+q_{16})/2\},
       \qquad q_f=\log L_f.                            \tag{6}
\]
This is one genuine left envelope with its two internal comparison branches. It is not an unrestricted \(H=\max(A_C,A_L,A_R)\) spectator.

The actual-source identification is the general-Morse inverse cut and coefficient theorem in [the exact source for a matched spherical diagram](research_matched_sphere_morse_source.md), §§1–6, and [the geometric contribution and original filled complement](actual_morse_geometric_contribution.md), §§1–3. The legal sphere construction, dual matching, cyclic quartets and nonmatching mark satisfy those inputs. The complete positive cut exists by the simple-sphere construction in the latter note; no terminal tangles have been inserted.

The literal terminal-pairing calculation gives one main component when exactly the following zero-based crossing regions have odd powers:
\[
 \{1,2,5,14,15,16,17,21,22,23,25,27,28\}.               \tag{7}
\]
All other powers are even. This test uses the physical untwisted pairing \((C_0,C_1),(C_2,C_3)\), the actual odd pairing, and the original outside edges. It does not identify the shaded pairing with the physical strand pairing. The topology verifier below checks all outside connections and local pairings, and gives this explicit parity pattern. The convex-envelope conclusion itself is independent of this choice of powers.

## 3. The exact feasible lower witness

For an ordinary supported triangle \(t\), let
\[
 F_t(a)=\sum_{f\in t\text{ ordinary}}f(a_f),\qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \quad a_f\ge0,\quad\sum_fa_f=\frac12 .                 \tag{8}
\]
The triangle Fenchel inequality, with its original source normalization, is
\[
 Q_t(q)\ge F_t(a)+\sum_f a_fq_f.                        \tag{9}
\]
It holds at every positive shared vector and at the exact protected specialization. See [the triangle entropy and balance formulas](actual_triangle_entropy_algebraic_balance.md), §1.

At every central spectator there are two such full rows. At crossing \(32\), choose the rational number
\[
             \lambda=\frac{548219162717}{10^{12}}.
                                                        \tag{10}
\]
Since \(0<\lambda<1\), equation (6) gives for all real \(q\)
\[
 A_{32,L}(q)
  \ge (1-\lambda)q_{16}
          +\lambda(q_0+q_{16})/2
  =\frac\lambda2q_0+(1-\lambda/2)q_{16}.                \tag{11}
\]
The selected retained singleton carries load \(\lambda/2\) on face \(0\), with zero entropy. No other triangle mass is scaled: all \(106\) spectator rows have mass one and total corner load \(1/2\).

The certificate contains \(305\) rational variables, including \(\lambda\), with their full row/corner incidence. It satisfies exactly
\[
 \begin{split}
 &a_{tf}\ge0,\qquad \sum_{f\in t}a_{tf}=1/2
                    &&\text{for every spectator row},\\
 &\sum_{t\text{ spectator}}a_{tf}
       +\frac\lambda2\mathbf1_{f=0}
       +(1-\lambda/2)\mathbf1_{f=16}=1
                    &&\text{for every ordinary face }f.
 \end{split}                                           \tag{12}
\]
The vertex labels in each row are checked against the original quartet list, not an independently assembled transportation graph. Protected loads are zero. All rational target equations are verified by exact fractions.

Sum (9) over the spectator rows and add (11). Every logarithmic term cancels the original unit face targets in (2), by (12). Hence, for every shared vector,
\[
  G_\sigma(L)\ge E_{\mathrm{dual}},\qquad
  E_{\mathrm{dual}}=
      \sum_{t\text{ spectator}}F_t(a_t),
  \qquad \mathcal C_\sigma\ge E_{\mathrm{dual}}.          \tag{13}
\]
This is weak duality. It requires no existence of a minimizing radius vector, no strong-duality theorem, and no interpretation of a failed solver as a lower bound.

### The chosen shared sector is not identically zero

The preceding dual witness concerns an envelope. We separately verify that it belongs to an actual nonzero source sector, rather than a string that could be removed for lack of shared coefficient support. This verification gives no exponential lower bound.

Take an even level \(N=2m\), and set \(d=2m-1\). At the common real spectral value \(-2\), put
\[
 \begin{aligned}
 a_j&=2+2\cos((2j+1)\pi/N)>0 &&(0\le j\le d),\\
 s_j&=2\sin(j\pi/N)>0 &&(1\le j\le d).
\end{aligned}
 \tag{13a}
\]
Set \(s_0=0\). After the common sign \((-1)^d\) is removed from each actual numerator, every path coefficient is nonnegative. This follows directly from the unused-row path formula in [the exact cofactor factorization](actual_cross_cofactor_factorization.md), §§1–2. In particular, the lower cleared cofactor on a triangle satisfies
\[
 R_0=1,\qquad
 R_j(b)=b^j\prod_{r<j}a_r+s_j^2(x+y)R_{j-1}(b)
             +s_js_{j-1}a_{j-1}xyR_{j-2}(b),\qquad D(b)=R_{m-1}(b),
 \tag{13b}
\]
where the recurrence is used for \(1\le j\le m-1\), with absent negative-index terms zero. Induction shows that \(R_j\) contains every homogeneous monomial of degree \(j\) in its surviving triangle variables with a strictly positive coefficient. The pure \(b^j\) term is present, and multiplication by \(x+y\) supplies every remaining monomial from the previous degree. Setting a protected variable to zero preserves this statement on the remaining variables.

The exact even central factorization contains the positive summand
\[
                  s_m^2(x+y)D(b)D(c).
 \tag{13c}
\]
At each of the \(53\) central regions, choose one ordinary outer face from \(x,y\) for this displayed linear factor. Such a face exists: the matched outer diagonal cannot be the nonmatching protected edge. Let \(c_f\) count these choices, so \(\sum_f c_f=53\). The certificate checker verifies this incidence directly. At the selected left region \((0,50,16,29)\), the substitutions at \(50,29\) force the lower endpoint row to zero and leave only one-step paths. For every \(0\le j\le m-1\), the local polynomial consequently contains
\[
                         L_0^jL_{16}^{d-j}
 \tag{13d}
\]
with a strictly positive coefficient.

Choose \(j=\lfloor(m-1)\lambda\rfloor\). The \(106\) central triangle factors in (13c) must have row degrees \(m-1\) and face totals
\[
 b_f=d-c_f-j\mathbf1_{f=0}-(d-j)\mathbf1_{f=16}.
 \tag{13e}
\]
Scale the strictly positive rational corner loads from (12) by \(2(m-1)\). They already have the required row degrees. Put \(e=(m-1)\lambda-j\in[0,1)\). The correction needed in the column sums is
\[
 \delta_f=\begin{cases}
  1-c_0+e,&f=0,\\
  -c_{16}-e,&f=16,\\
  1-c_f,&f\ne0,16.
 \end{cases}
 \qquad \sum_f\delta_f=0,\qquad\sum_f|\delta_f|<110.
 \tag{13f}
\]
The graph on the \(54\) ordinary faces that joins two faces when they occur in the same central triangle is connected. This is an exact finite incidence check recorded by the verifier. Choose a spanning tree in this graph and, for each tree edge, one triangle containing its endpoints. Route the column correction \(\delta\) along this tree. A transfer across a tree edge subtracts from one corner of the chosen row and adds to its other corner, so it preserves every row degree. Each transfer has magnitude at most \(\sum|\delta_f|\); there are \(53\) tree edges. Thus no individual corner load changes by more than \(53\cdot110=5830\).

The minimum original central corner load is the positive rational number
\[
                  a_*=\frac{29141577}{40000000000}.
 \tag{13g}
\]
For \(2(m-1)a_*>5830\), all corrected loads are nonnegative. The resulting real transportation table has integer row and column sums. It has an integer table with the same supported entries: to see this, perturb alternating entries around a cycle of fractional entries until one becomes integral. This preserves margins and nonnegativity. If the remaining fractional graph were a forest, its leaf would have an integer sum and exactly one fractional incident entry, which is impossible. Repetition therefore removes all fractional entries.

The integer row allocations select monomials present in the full-support factors \(D\). Equations (13c)–(13e) then give exactly degree \(d\) at every ordinary face, and zero at the protected faces. All contributions have the same original overall sign, so there is no cancellation at this even-level point. In particular the actual shared singleton coefficient is nonzero for every even \(N=2m\) with \(m\ge4001158\). This deliberately coarse threshold is only a support certificate; it is not an asymptotic rate estimate.

## 4. An upper bound for the actual complete action

The complete action function is
\[
 P(L)=\sum_e\{Q(L_x,L_b,L_y)+Q(L_x,L_c,L_y)\}
                                  -\sum_f\log L_f.      \tag{14}
\]
The actual complete marked circle packing is stationary for this convex function. Its source-calibrated value is \(\Phi\), so
\[
                         \Phi\le P(L^{\mathrm{up}})     \tag{15}
\]
for any positive shared ordinary vector. This is a consequence of the geometric face-star equations and the normalized triangle action in [the complete geometric filling period](actual_morse_cross_filling_period.md), §§2–4, and [the geometric contribution and original filled complement](actual_morse_geometric_contribution.md), §§2,4–6. It does not invoke a full-positive-source endpoint theorem or a middle-forest restriction.

The certificate contains one positive rational vector \(L^{\mathrm{up}}\), with the two protected coordinates still zero. It need not be the exact packing. The proof uses it only in the upper bound (15).

## 5. Rational interval certification

`verify_actual_singleton_sector_obstruction.py` uses the established integer outward-rounded interval engine in `experiments/verify_conway_two_leaf_block_alias_certificate.py`. It does not import NumPy, SciPy, an optimizer, or floating-point approximations. Its extra square-root enclosures use integer square roots; arctangents use exact half-angle reduction and an alternating series with an explicit remainder.

For \(0<t<1/2\), it evaluates
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds
 =t\log(2\pi t)-t-
   \sum_{n=1}^{20}\frac{\zeta(2n)t^{2n+1}}{n(2n+1)}+R,
                                                        \tag{16}
\]
with
\[
 -\frac{2t^{43}}{21\cdot43(1-t^2)}\le R\le0,
 \qquad f(t)=-J(t)-J(1/2-t).                            \tag{17}
\]
At \(0,1/2\), \(f\) is exactly zero. The zeta intervals use exact finite sums and integral-tail bounds. The same interval engine evaluates the rational weighted triangle upper witness using its explicit maximizing angles. All intervals are outward rounded before addition or subtraction.

The completed run certifies the conservative decimal bounds
\[
 \begin{split}
 E_{\mathrm{dual}}&>67.8938190642,\\
 P(L^{\mathrm{up}})&<67.6882466366,\\
 E_{\mathrm{dual}}-P(L^{\mathrm{up}})&>0.2055724276>1/5.
 \end{split}                                           \tag{18}
\]
The JSON output stores the actual rational interval endpoints, not rounded decimal evidence. Combining (13), (15) and (18) proves (3).

The diagnostic optimizer was used only to locate the source and seed the rational loads and radii. Exact row reduction produced a rational feasible flow before verification. The verification reads only that saved rational object and checks all identities independently of the locating calculation. Repeating the numerical optimization is unnecessary to reproduce the proof.

## 6. What this changes, and what it leaves open

The earlier 17-crossing marked source in [the separation between anchored and refined certificates](actual_shared_radius_certificate_separation.md) is a useful sanity test. Its anchored obstruction mixes genuine labels at spectators, while a rigorous 40-branch cover certifies every singleton there. The present search reproduces the expected negative singleton diagnostic for that source and then uses a different simple sphere. No conclusion here contradicts the 40-branch certificate.

For the present \(54\)-crossing source, every finite cover whose branch costs are formed only by maxima of the same local C/L/R envelopes must include this singleton somewhere. A containing branch has pointwise cost at least \(G_\sigma\), so it also cannot have a strict witness below \(\Phi\). Thus arbitrary refinement **only among these genuine labels** is insufficient on this fixed source and mark.

The obstruction does not exclude another original mark or another presentation of the knot. Nor does it exclude an estimate which keeps additional shared coefficient cancellation, couples the spectral variables, refines the actual finite polynomial by more structure than these three envelopes, or estimates the filled period directly. In particular (3) is not a lower bound for
\(\|S_{N,\mathrm{full}}-S_{N,\mathrm C}\|\). Cauchy's bound and the local weighted envelopes can be strictly larger than the shared signed coefficient. No new quantum-volume theorem or counterexample follows.

## 7. Reproducing the certificate

From the repository root run

```sh
python3 repro/run_research_checks.py singleton-envelope
```

The runner executes both checks and saves their logs. The individual scripts also accept `--certificate` and `--output`. The capacity verifier also accepts `--repo` to locate its rational interval engine. Their defaults resolve from the script location, so the working directory is immaterial. Only the Python standard library is required. Assertions are part of verification; optimized Python execution is rejected.

The [certificate](https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/actual_singleton_sector_obstruction_certificate.json) contains the exact oriented moves, matching, protected mark, label string, rational corner loads and upper radius vector. The [capacity verifier](https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/verify_actual_singleton_sector_obstruction.py) checks those inputs and the entropy inequality; its [saved output](https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/actual_singleton_sector_obstruction_results.json) records rational interval endpoints and hashes. The [topology verifier](https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/verify_actual_singleton_sector_obstruction_topology.py) separately checks the oriented sphere, matching frames and original knot pairing; its [saved output](https://github.com/sashakolpakov/murakamis_dream/blob/main/experiments/actual_singleton_sector_obstruction_topology_results.json) records the explicit odd crossing set.

These are finite certificates for the theorem proved here. They do not numerically evaluate a quantum invariant, infer its asymptotics from sampled levels, or establish a volume equality for this knot family.
