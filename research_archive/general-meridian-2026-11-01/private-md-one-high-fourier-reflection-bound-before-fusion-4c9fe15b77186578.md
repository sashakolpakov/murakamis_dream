# A reflected complete trace bounds the one-high deformation

Private derivation, 1 November 2026. All products and traces below use the fixed complete Newton polynomials. The comparison changes the high index in the *difference* of two traces. It does not compare the full moving trace with the complete trace at the same indices.

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
The last step is the established all-low whole-trace comparison, valid at both parities for every tuple of low indices. That theorem is proved in Section 2 of notes/actual_main_meridian_source_bounds.md by the finite Fourier identity, adjacent odd level, interval-tail comparison and original positive slack-path map. Only its all-low case is used here. The number of interpolation values is fixed independently of \(N\); no unknown state or growing inverse matrix enters (20).

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
The first complete tensor is nonnegative and is zero outside its old support. Equation (22) does not assert polynomial domination by that first term. In the valence-nine obstruction the second term is precisely allowed to be exponentially larger than it.

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

## 5. One high physical interface and the precise scope of a global use

Consider one moving whole junction with exactly one high physical interface. Replace every other moving tensor by an already justified complete positive majorant, and retain all old complete tensors and all actual boundary profiles. Removing the high interface separates two genuine old unturned regions, with ordinary-output profiles \(f_A\) and \(f_B\). Suppose their boundary inputs are the original rigid profiles \(g+c\), so the proved old product response gives \(f_A'\ge f_2'\) and \(f_B'\ge f_2'\) on their full ordinary-output intervals. The constants stay in these profiles. A physical quarter-turn identifies equal covariant labels, so at covariant label \(z\) the original action is \(f_A(1-z)+f_B(1-z)\).

Only the correction in (21) reflects the moving endpoint to \(1-z\). Its positive comparison action is therefore bounded by
\[
 f_A(1-z)+f_B(z),\qquad z\ge1/2.
 \tag{29}
\]
Because \(f_2\) is symmetric and \(f_A'-f_2'\ge0\),
\[
 f_A(z)-f_A(1-z)
 =\int_{1-z}^z(f_A'(t)-f_2'(t))\,dt\ge0.
 \tag{30}
\]
Hence (29) is at most \(f_A(z)+f_B(z)\), which is bounded by the maximum of the same original complete action. This comparison preserves the neighboring region; it does not replace it by a free cap or by a uniform J-norm budget.

For a single such interface, a strict source gap follows by a local-to-global argument when the possible equality set in (29) lies in a regular window satisfying (23). Outside a fixed neighborhood of that equality set, strict compact separation of the old action gives a loss. Inside it, (28) supplies the missing loss. If \(A\) is not the isolated two-leaf product, its response inequality is strict and already separates (29) away from half. If it is that two-leaf product, its symmetry can make (30) an equality; (28) is then essential. Regularity in this case comes from the original strict conditional optimizer, with all junction-incident low factors bounded away from zero and half. For a genuinely higher-valence moving junction, the old physical-edge half theorem excludes the exceptional two-trivalent-hub half optimizer. These are geometric hypotheses to verify in the original tree, not conclusions of Fourier coefficient positivity alone.

This note does not establish simultaneous reflection at several interfaces. Multiple reflected edges change how the conditional old regions are coupled. Applying the one-interface inequality while silently resetting the other interfaces would not be a proof. The exact finite estimate (21), its regular refinement (28), and the conditional single-interface argument (29)–(30) are the established reductions.

## 6. Inputs and boundaries of the result

The finite Fourier trace, complete positive multiplication, and all-low comparison are in notes/actual_main_meridian_source_bounds.md, Section 2. The full high Newton and polynomial Hermite bounds are in its Section 1.4 and notes/actual_conway_root_star_full_jet_localization.md. The neighboring derivative comparison is in notes/actual_conway_unflagged_probe_geometry.md, Appendix A. The private old whole-hub simultaneous-half and complete-edge-half proofs retain the original physical-turn and hidden-unturned conventions used in Section 5.

No topological move, geometric filling assertion, or invariant equality follows merely by replacing an index in (21). The replacement is an upper comparison for an exact trace difference in the fixed basis. Actual mixed carriers, scalar framings, and paired edge weights remain those of the original typed contraction. Their boundedness on fixed pre-resonance disks can be used separately; they have not been absorbed into a new trace definition.
