# A reflected trace bound for one high Newton index

The finite tangle algebra is written in a Newton polynomial basis \(e_0,\ldots,e_{N-1}\). In this note an index is **high** when it exceeds \(\lfloor(N-1)/2\rfloor\). This is an internal basis index, not an auxiliary crossing-circle color. Its distinction from a low index matters because the high polynomial has signed Fourier coefficients and vanishes at the complete spectral nodes, while its derivatives at repeated roots need not vanish.

When one high basis polynomial is multiplied by several low ones, moving the main meridian can make the trace exponentially larger than its complete value. The useful comparison concerns the difference of the two traces. Its first Fourier alias cancels exactly. The remaining difference is bounded by a positive complete trace in which the high index \(h\) is replaced by \(N-1-h\). In a regular low-index window there is a further strict exponential loss.

The proof below retains both level parities, all Fourier aliases, and the coefficient trace at repeated roots. Section 5 explains how the reflected index is used in a whole ordered tree through the [component-pressure comparison](actual_main_meridian_component_pressure.md). The [general component theorem](actual_main_meridian_general_component_comparison.md) combines this bound with the other index sectors. The comparison does not identify the two diagrams produced by deleting a turn, and it does not assert a bound by the same-index complete trace.

## 1. Exact Fourier coefficients of a high Newton polynomial

Fix an integer \(N\ge2\), and put
\[
 q=e^{\pi i/N},\quad d=N-1,\quad m=\lfloor d/2\rfloor,
 \quad S_j=\prod_{v=1}^j2\sin(\pi v/N),\quad S_0=1,
 \qquad c_j=2\cos((2j+1)\pi/N).
 \tag{1}
\]
The fixed polynomial and the coefficient trace are
\[
 e_j(z)=S_j^{-2}\prod_{v=0}^{j-1}(c_v-z),\qquad
 P_s(z)=\mathsf T_N(z)+2\cos(2\pi s),\qquad
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \tag{2}
\]
Here \(\mathsf T_N(u+u^{-1})=u^N+u^{-N}\). The remainder is a polynomial of degree less than \(N\); it retains both the value and first normal at a repeated root. Write \(\eta=(-1)^{N+1}\).

Suppose \(m<h\le d\), and set \(a=N-h\) and \(v=2h-N\ge0\). The Fourier expansion has a central gap:
\[
 e_h(-u-u^{-1})=\sum_{k=-h}^{h}A_k u^k,
 \qquad A_k=0\quad (|k|<a).
 \tag{3}
\]
For the two remaining tails its coefficients are exactly
\[
 \boxed{\quad
 A_k=(-1)^{h-|k|}
 \frac{S_{2h-N}}{S_h^2S_{|k|-a}S_{h-|k|}},
 \qquad a\le |k|\le h.
 \quad}
 \tag{4}
\]
Every factorial in (4) has index between zero and \(N-1\). In particular (4) includes the even-level endpoint \(h=N/2\): then \(v=0\), and the only coefficients are \(A_h=A_{-h}=S_h^{-2}\).

To prove this directly, factor the numerator as a string of consecutive odd powers:
\[
 e_h(-u-u^{-1})=
 \frac{u^{-h}}{S_h^2}
 \prod_{j=0}^{h-1}(1+q^{2j+1}u)(1+q^{-2j-1}u).
 \tag{5}
\]
The \(2h\) factors have exponents \(-2h+1,-2h+3,\ldots,2h-1\). Removing one complete cycle of \(N\) factors leaves the exact identity
\[
 \prod_{j=0}^{h-1}(1+q^{2j+1}u)(1+q^{-2j-1}u)
   =(1-\eta u^N)\prod_{j=0}^{v-1}(1-q^{2j-v+1}u).
 \tag{6}
\]
The last product is one when \(v=0\). Its finite binomial expansion is
\[
 \prod_{j=0}^{v-1}(1-q^{2j-v+1}u)
  =\sum_{l=0}^v(-1)^l\frac{S_v}{S_lS_{v-l}}u^l.
 \tag{7}
\]
This follows by the two-term coefficient recurrence for a finite geometric product; no root-of-unity factorial is divided by a zero factor. Multiplication by \(1-\eta u^N\) gives the negative-frequency interval \([-h,-a]\) and the positive-frequency interval \([a,h]\). In the latter interval \(k=a+l\), and
\(-\eta(-1)^l=(-1)^{h-k}\). Symmetry under \(u\mapsto u^{-1}\) gives the other interval. This proves (3)–(4), including their signs.

There is a useful interpretation of its closed coefficient rate. Define
\[
 J(t)=\int_0^t\log(2\sin\pi y)\,dy,
 \quad g(t)=J(2t)-4J(t),
 \quad b_t(w)=J(2t)-2J(t)-J(t+w)-J(t-w).
 \tag{8}
\]
For \(\alpha=(N-h)/N\) and \(w=k/N>0\), the uniform sine-factorial estimate gives
\[
 \frac1N\log|A_k|
  =H_\alpha(w)+O(\log N/N),
 \quad
 H_\alpha(w)=-J(2\alpha)+2J(\alpha)
              -J(w-\alpha)+J(w+\alpha).
 \tag{9}
\]
The error is uniform on the closed coefficient support. Reflection \(J(1-t)=-J(t)\) and duplication \(J(2t)=2J(t)-2J(1/2-t)\) yield
\[
 H_\alpha(w)=b_{1/2-\alpha}(w-1/2)-g(1/2-\alpha).
 \tag{10}
\]
Thus the absolute coefficient rates are those of a low finite packet centered at frequency \(1/2\), normalized to have maximum rate zero. The signs in (4) still alternate. Formula (10) is not a positive expansion of the actual high polynomial.

For later use, the full coefficient norm has a polynomial bound
\[
 \sum_{k=-h}^h|A_k|\le C N^C,
 \qquad m<h<N.
 \tag{11}
\]
One proof applies the uniform factorial estimate in (9): strict concavity of \(b_t\) gives \(b_t(w)\le b_t(0)=g(t)\), also by continuity at the endpoints. There are at most \(2N\) coefficients. Alternatively, the established high Newton spectral-jet bound and complete Hermite interpolation give a polynomial sup norm on \([-2,2]\); each Fourier coefficient is bounded by that sup norm. Both arguments concern the actual fixed polynomial, including its normals.

## 2. The first alias cancels in the trace difference

Let \(F=\prod_{j=1}^B e_{n_j}\), where \(B\) is fixed and \(0\le n_j\le m\). Write
\[
 F(-u-u^{-1})=\sum_{k=-D}^D f_k u^k,
 \qquad D=\sum_j n_j.
 \tag{12}
\]
These coefficients are nonnegative, symmetric and unimodal. Indeed each low factor has coefficients
\[
 [u^{k-n}]e_n(-u-u^{-1})
    =\frac{S_{2n}}{S_n^2S_kS_{2n-k}},
 \qquad 0\le k\le2n<N;
 \tag{13}
\]
the successive ratio proves unimodality. Decomposing each factor as a nonnegative sum of centered interval indicators shows that convolution preserves it. We set \(f_k=0\) outside the support.

For any polynomial \(G\), if \(G(-u-u^{-1})=\sum g_k u^k\), the exact finite Fourier trace is
\[
 \phi_s(G)=N^2\sum_{l\ge1}\eta^{l+1}
      (g_{lN-1}-g_{lN+1})U_{l-1}(\cos2\pi s).
 \tag{14}
\]
Only finitely many terms occur. This identity is a polynomial quotient identity and therefore includes the collision values of \(s\). It follows either from the generic simple-root residue sum followed by polynomial continuation, or from the exact monic Chebyshev reduction. At \(s=0\), \(U_{l-1}(1)=l\).

Apply (14) to \(G=e_hF\). Since \(U_0=1\), its first alias cancels exactly in \(\phi_s(G)-\phi_0(G)\). Every remaining Fourier coefficient is evaluated at an absolute frequency at least \(2N-1\). Equations (11)–(12) and unimodality give
\[
 |g_{lN\pm1}|\le C N^C f_{lN-1-h}
       \le C N^C f_{2N-1-h},\qquad l\ge2.
 \tag{15}
\]
The number of aliases is bounded in terms of \(B\). Moreover
\(U_{l-1}(\cos2\pi s)-l\) is divisible by
\(\Delta_s=2\cos2\pi s-2\), with a quotient bounded on any fixed disk. Therefore, for every fixed \(R<\infty\),
\[
 \sup_{|s|\le R}\frac{|(\phi_s-\phi_0)(e_hF)|}{|\Delta_s|}
       \le C_{B,R}N^{C_B} f_{2N-1-h}.
 \tag{16}
\]
At zeros of \(\Delta_s\), the quotient is understood as its polynomial continuation. No estimate in this section assumes a sign for the high coefficients or an absence of higher aliases.

## 3. Recovering a positive complete comparison at both parities

Set \(r=d-h\), so \(0\le r\le m\), and put \(C=e_rF\). Its Laurent coefficients \(c_k\) are nonnegative, symmetric and unimodal. The positive endpoint coefficient of the extra low factor is \([u^r]e_r=S_r^{-2}\); hence
\[
 c_{N-1}\ge S_r^{-2}f_{N-1-r}
       \ge N^{-1}f_{N+r}
       =N^{-1}f_{2N-1-h}.
 \tag{17}
\]
Here \(S_r^2\le N\): the successive sine factors first decrease the partial products and then increase them up to the midpoint product, whose square is \(N\) at odd levels and \(N/2\) at even levels. The two frequencies in (17) satisfy \(N-1-r\ge0\) and \(N-1-r\le N+r\).

The interval-tail lemma gives
\[
 c_{N-1}\le(2m+1)^{B+1}(c_{N-1}-c_{N+1}).
 \tag{18}
\]
For clarity, that lemma states that a convolution of \(B+1\) nonnegative symmetric unimodal sequences supported on \([-m,m]\) satisfies \(c_k\le(2m+1)^{B+1}(c_k-c_{k+2})\) for \(k\ge m\). After the interval-indicator decomposition, a nonzero integer convolution strictly decreases in its upper tail, so its positive two-step difference is at least one while its value is at most the product of the interval lengths. This includes zero radii and support endpoints.

At even levels the complete trace itself has alternating alias signs, so (18) cannot simply be summed into it. A fixed-dimensional interpolation recovers the first difference instead. Put
\[
 d_l=c_{lN-1}-c_{lN+1},\qquad
 Q_N(X)=\sum_{l=1}^{B+1}\eta^{l+1}d_lU_{l-1}(X).
 \tag{19}
\]
Absent aliases are assigned coefficient zero. Formula (14) gives
\(Q_N(\cos2\pi s)=N^{-2}\phi_s(C)\). Choose once and for all \(B+1\) distinct real parameters in \([0,1/8)\). Their cosine values are distinct, so evaluation in the basis \(U_0,\ldots,U_B\) is an invertible matrix depending only on \(B\). In particular
\[
 d_1\le C_BN^{-2}\max_j|\phi_{s_j}(C)|
       \le C_BN^{C_B}\phi_0(C).
 \tag{20}
\]
The last step is the established all-low whole-trace comparison, valid at both parities for every tuple of low indices. That theorem is proved in Section 2 of [the source-bound theorem](actual_main_meridian_source_bounds.md) by the finite Fourier identity, adjacent odd level, interval-tail comparison and original positive slack-path map. Only its all-low case is used here. The number of interpolation values is fixed independently of \(N\); no unknown state or growing inverse matrix enters (20).

Combining (16)–(20) proves the finite reflected-index bound
\[
 \boxed{\quad
 |(\phi_s-\phi_0)(e_hF)|
 \le C_{B,R}N^{C_B}|\Delta_s|\,
          \phi_0(e_{d-h}F),
 \quad h>m,\quad n_j\le m,\quad |s|\le R.
 \quad}
 \tag{21}
\]
Both traces on the right are at the original level. A zero right side forces the left side to vanish. For \(B=0\) this also follows immediately by degree. The trace estimate allows any fixed finite \(R\); an application to physical turns retains its separate pre-resonance restriction \(R<1\) and its bounded typed factors.

The full moving trace consequently has the positive majorant
\[
 |\phi_s(e_hF)|\le \phi_0(e_hF)
       +C_{B,R}N^{C_B}|\Delta_s|\phi_0(e_{d-h}F).
 \tag{22}
\]
The first complete tensor is nonnegative and is zero outside its old support. Equation (22) does not assert polynomial domination by that first term. The [nine-factor counterexample](actual_main_meridian_same_index_obstruction.md) shows why the second term must be allowed to be exponentially larger than the first.

## 4. Strict loss on a regular low-factor window

The reflected estimate can be sharpened where \(r/N\) stays positive and every \(n_j/N\) stays in a fixed compact subinterval of \((0,1/2)\). This uses the two different frequencies in (17), rather than replacing both by the coarser tail bound.

Fix \(\delta>0\), and suppose
\[
 \delta\le n_j/N\le1/2-\delta\quad(1\le j\le B),
 \qquad r/N\ge\delta.
 \tag{23}
\]
For \(u\) in that low interval, the individual coefficient action from (13) is \(b_u(t)\) in (8), and
\[
 b_u''(t)=-\frac{\pi\sin(2\pi u)}
                    {\sin\pi(u+t)\sin\pi(u-t)}
             \le-\lambda_\delta<0,
 \qquad |t|<u.
 \tag{24}
\]
For example \(\lambda_\delta=\pi\min_{u\in[\delta,1/2-\delta]}\sin2\pi u\) works. The convolution rate
\[
 B_{\mathbf u}(t)=\max\left\{\sum_{j=1}^B b_{u_j}(v_j):
                    |v_j|\le u_j,\ \sum_jv_j=t\right\}
 \tag{25}
\]
is even and strongly concave with modulus \(\lambda_\delta/B\). To prove the modulus directly, use strong concavity for each summand and
\(\sum_j(v_j-w_j)^2\ge B^{-1}(\sum_jv_j-\sum_jw_j)^2\), then maximize. Thus, for \(0\le t_1\le t_2\) in its support,
\[
 B_{\mathbf u}(t_2)-B_{\mathbf u}(t_1)
       \le-\frac{\lambda_\delta}{2B}(t_2^2-t_1^2).
 \tag{26}
\]
This includes support endpoints by continuity. Uniform factorial estimates and the fixed number of convolution variables give
\(\log f_k=N B_{\mathbf u}(k/N)+O_B(\log N)\) whenever \(f_k>0\). The lower bound follows by rounding a constrained maximizing tuple to integer indices with the same integer sum; each index changes by \(O_B(1)\), and the endpoint logarithmic modulus of \(J\) costs only \(O_B(\log N)\). The upper bound is the same factorial estimate summed over at most \(N^{B-1}\) tuples.

Take
\(t_1=(N-1-r)/N\) and \(t_2=(N+r)/N\). If \(f_{N+r}=0\), (16) is zero and there is nothing to prove. Otherwise both frequencies lie in the support, and (26) gives
\[
 f_{N+r}\le C N^C
       \exp\left\{-\frac{2\lambda_\delta r}{B}+O(1)\right\}
       f_{N-1-r}.
 \tag{27}
\]
Use the first inequality of (17), then (18)–(20). For some \(\kappa_{B,\delta}>0\), and all sufficiently large levels,
\[
 \boxed{\quad
 |(\phi_s-\phi_0)(e_hF)|
   \le C_{B,R,\delta}N^C|\Delta_s|e^{-\kappa_{B,\delta}N}
                  \phi_0(e_{d-h}F).
 \quad}
 \tag{28}
\]
The loss can be fixed before \(R\); only the prefactor and eventual threshold depend on the disk. This is a relative loss against the reflected complete tensor, not against the same-index complete tensor.

## 5. Several reflected interfaces and the strict old window

The finite estimates above now have a precise whole-tree interface. The required positive-pressure comparison is proved separately in [the component-pressure theorem](actual_main_meridian_component_pressure.md). It applies to an original ordered tree of whole bare junctions, all of valence at least three, whose internal edges are physical quarter-turns and whose external profiles are the original rigid functions \(g+c_j\). The constants are retained. Write \(F(\mathcal G)\) for its complete positive maximum.

### 5.1. Reflection removes a turn in the positive comparison

The exact complete metric and turn are \(\phi_0(e_i e_j)=\delta_{i+j,d}\) and \(T_0(e_i)=e_{d-i}\). Consequently
\[
 \sum_{i=0}^d\phi_0(Ae_i)\phi_0(e_{d-i}B)=\phi_0(AB).
 \tag{29}
\]
Reflecting exactly one endpoint of an equal-label physical-turn edge therefore changes it into the complementary pairing (29). Removing that turn and fusing the two ordered old products is an exact positive tensor operation, with the induced boundary order. It is not an assertion that the physical links before and after deletion are isotopic.

The pressure comparison retains the neighboring profiles. At a cut physical edge they are unturned product profiles \(f_A,f_B\), and the original and deleted pressures are
\[
 F_T=\max_b\{f_A(b)+f_B(b)\},\qquad
 F_I=\max_b\{f_A(b)+f_B(1-b)\}.
 \tag{30}
\]
The product-response theorem gives \(f_X'\ge f_2'\), and \(f_2\) is symmetric. Hence \(f_X(b)\ge f_X(1-b)\) for \(b\ge1/2\). Applying this to the smaller of the two arguments in the deleted summand gives \(F_I\le F_T\). After fusion the new hub still has valence at least three, and its original ordered positive resolution has a unique strict maximizing state. The same argument can therefore be applied successively to the *current* fused tree. For any finite set \(S\) of deleted edges,
\[
                      F(\mathcal G/S)\le F(\mathcal G).
 \tag{31}
\]
This does not hold the old multi-boundary responses fixed while changing their couplings. Each stage uses the actual profiles of that fused tree. The cited geometric proof establishes the induced cyclic order, exact fusion and strictness hypotheses.

For moving-source applications, expand each one-high tensor as its complete tensor plus its difference. Replace a selected difference by (21). Actual typing makes moving equal-color vertices nonadjacent. A selected internal high edge meets a constant old tensor, whose complete support permits at most one high incidence. Thus the selected internal edges form a matching. Each selected moving endpoint has all other indices low, and its old neighbor also has all other indices low. Every fused hub therefore has an all-low exterior in that band sector. The other physical edges are retained.

After positive fusion, summing all complementary hidden labels gives the old tensor of \(\mathcal G/S\). The original band restrictions can be kept in its positive resolution or discarded for an upper bound. They do not change its lattice spacing: reflection is the exact integer substitution \(h\mapsto d-h\).

### 5.2. The strict fused optimizer supplies the Fourier window

First note an elementary degree restriction that needs no old-support assumption. A cubic tensor with one high index and two low indices has degree at most \(d+2m\le2N-2\). Its trace difference vanishes, because the first possible changing alias has degree \(2N-1\). Therefore every nonzero selected one-high difference has valence at least four. It need not have valence at least five: off the complete support a valence-four difference can be nonzero.

Fix a nonempty set of selected internal differences, and keep the complementary labels of the deleted edges as hidden variables in a fixed old positive resolution of \(\mathcal G/S\). Let \(w_S\) be its unique strict complete optimizer. An internal fusion of a valence-at-least-four selected vertex with a valence-at-least-three neighbor creates valence at least five. In particular the fused tree cannot be the exceptional tree consisting of two trivalent hubs, each carrying two rigid external leaves.

The old physical-edge half theorem now puts every remaining physical internal label of \(w_S\) strictly inside \((0,1/2)\); the external rigid labels also lie strictly in that interval. Hidden unturned labels remain in their original strict interval \((0,1)\). For a selected difference, each of its other incidences is a remaining physical edge or an original rigid leaf: the matching has removed only its unique high edge. Thus all the low factors entering that difference lie in a fixed compact low-index window near \(w_S\).

Let \(r\) be the hidden complementary index of that selected edge, and let \(x_r\) be its normalized value at \(w_S\). Strictness gives \(x_r>0\). If \(x_r>1/2\), the closed limiting sector \(r/N\le1/2\) excludes \(w_S\), and the whole sector has a compact old-action gap. Otherwise \(r/N\) is bounded below by a fixed positive constant in a sufficiently small neighborhood of \(w_S\). The value \(x_r=1/2\) is allowed: (23) requires a positive lower bound on \(r/N\), not separation of that particular probe from half. All *other* factors are strictly below half. Hence the precise hypotheses of (28) hold near every fused optimizer that can contribute to the reflected sector. The finite restriction \(r\le m\) can only reduce this sum.

This argument uses the unconstrained strict optimizer of the same fused old action, followed by restriction to the band sector. It does not assume that an arbitrary band-constrained optimizer is strict. Values \(r\) near zero are in the compact complement of this optimizer, rather than being inserted into a false uniform interior Fourier estimate.

### 5.3. Combining the local Fourier loss and compact separation

Use the coarse inequality (21) on all selected differences. Resolve every resulting complete tensor positively. This gives a polynomial multiple of the original positive state sum of \(\mathcal G/S\), with its exact rigid boundary profiles and constants. Its closed factorial errors and the number of states are subexponential uniformly up to support faces.

Outside a fixed neighborhood of \(w_S\), uniqueness and strictness give a rate at most \(F(\mathcal G/S)-\eta_S\), with \(\eta_S>0\). Inside that neighborhood, apply (28) at one selected difference and use (21) at the others. The resulting bound has a further fixed loss \(\kappa_S>0\). If the band sector excludes \(w_S\), only the first case is needed. Thus the sum of this selected correction sector has rate
\[
 F(\mathcal G/S)-\min(\eta_S,\kappa_S)+o(1)
                  \le F(\mathcal G)-\min(\eta_S,\kappa_S)+o(1),
 \tag{32}
\]
with the irrelevant minimum omitted when only the compact-complement case occurs. One may shrink either positive constant to absorb polynomial factors. The structural loss is fixed before the parameter disk; \(R\) affects constants and the eventual level threshold. There are only finitely many selected sets for a fixed component.

No division by a complete tensor is used when that tensor vanishes. Equation (21) already forces the corresponding exact difference to be zero. Similarly, the argument never assigns a relative asymptotic to an old-support boundary tensor. It uses its positive closed upper envelope and the compact separation of the *whole* old action.

### 5.4. A reflected original external index

If the unique high incidence is an original external leaf, there is no internal turn to delete. Its actual high coefficient cone contributes the rate \(c_j\). After reflection to \(r=d-h\), the old comparison leaf contributes \(g(r/N)+c_j\). Thus the missing quantity
\[
                                  g(r/N)\ge0
 \tag{33}
\]
is a loss, and must be retained rather than silently supplied to the original source. At the strict old optimizer the reflected leaf is inside \((0,1/2)\), where this loss is strictly positive. Away from a neighborhood of that optimizer, old compact separation applies. This handles the two endpoints without pretending that \(g\) is uniformly positive on the closed interval.

If internal corrections are present as well, first perform their fusions and retain (33) in that same positive tree. If there are only external corrections, the nonzero selected vertex already has valence at least four by the cubic degree argument, so the exceptional two-trivalent geometry cannot arise. One external loss or one internal Fourier loss is enough; the other differences may retain their coarse reflected bounds. The boundary constants and all unchanged input profiles are counted once.

### 5.5. What this interface supplies

Equations (29)–(33), with the separately proved old fusion theorem, close the strict-window requirement for a finite family of one-high trace differences. Several reflected incidences are not treated as independent caps: their positive contraction is the same fused tree, and the sequential pressure theorem controls that tree as a whole.

The [general component comparison](actual_main_meridian_general_component_comparison.md) organizes the other sectors, including vertices with several high incidences, external high coefficient cones and inherited errors. Its half-cardinal comparison is compatible with the matching: every fused exterior is low, so it creates no additional high mark, and the remaining several-high moving vertices stay nonadjacent. That component proof retains the actual typed edge factors and the required output-norm interfaces. The [filled-volume theorem](actual_main_meridian_filled_volume.md) then uses the original finite wire packet and marked filling action; its geometric conclusion is not inferred from the reflected trace bound alone.

## 6. Proof inputs, finite checks and scope

The finite Fourier trace, complete positive multiplication and all-low comparison are proved in [Source growth near the complete main meridian](actual_main_meridian_source_bounds.md), Section 2. Its Section 1.4 and the [full-jet localization theorem](actual_conway_root_star_full_jet_localization.md) give the high Newton and polynomial Hermite bounds. The neighboring derivative comparison is proved in [the unflagged probe geometry](actual_conway_unflagged_probe_geometry.md), Appendix A. The [component-pressure theorem](actual_main_meridian_component_pressure.md) supplies the ordered fusion, simultaneous pressure comparison and complete physical-edge half bound used in Section 5.

The finite identities have a standalone reproduction through the research-check runner:

```bash
python3 repro/run_research_checks.py general-components
```

The high-Fourier check constructs the Newton polynomials directly over exact cyclotomic number fields, performs an independent monic quotient division with a formal parameter \(\Delta\), and compares the result with the Fourier formula. It also checks the full Frobenius fusion identity with an input that vanishes at repeated-node values but has nonzero first-normal trace. The recorded levels include both parities. These finite algebra checks test the identities and their signs; the uniform inequalities, strict exponential loss and pressure comparison are established by the arguments above.

No topological move or invariant equality follows merely by replacing an index in (21). The replacement is an upper comparison for an exact trace difference in the fixed basis. Actual mixed carriers, scalar framings and paired edge weights remain those of the original typed contraction. Their boundedness on fixed pre-resonance disks can be used separately; they have not been absorbed into a new trace definition.
