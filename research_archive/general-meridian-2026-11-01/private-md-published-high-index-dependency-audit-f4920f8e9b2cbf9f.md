# Dependency check after the one-high whole-trace obstruction

1 November 2026. Read-only check of the publication checkout
/private/tmp/murakamis_dream-publication. No repository or checkout edits.

The three checked publication files are byte-identical to their workspace copies:

| File under notes/ | SHA256 |
| --- | --- |
| actual_main_meridian_source_bounds.md | 153abbbdaac292c763c787a3de235ec123194d4aae944d6f10f111fc17a967d7 |
| actual_main_meridian_component_extension.md | a75f9fbca9a0c6ea1302ed229826e16110f773b600195b453d8348b6659dae66 |
| actual_main_meridian_regular_bare_trace.md | bb545421973876c313e33c32d4fb7e171846fc1978d6b4070941071ccbc27663 |

## 1. Singleton hubs

The pointwise comparison in source_bounds Section 2.1, (F3), assumes that every incident Newton index is at most \(m_N=\lfloor(N-1)/2\rfloor\). Its arbitrary-array version in Section 2.5, (F19), assumes low support in every input array. The output application (F20) also explicitly restricts the inserted probe to \(k\le m_N\). The paragraph following (F20) states that this comparison does not cover a high input or high output.

Section 3.3 uses precisely those hypotheses: (H14) has low input projections and a low output probe. The reference replacement (H15) is coefficientwise in the complete positive algebra. It does not introduce a moving high-index factor into (H14).

All other sectors are estimated differently in Section 3.4. The exact Chebyshev folding bounds of Section 1.2, (D8)–(D10), give polynomial quotient-multiplication cost in the full value-and-normal norm. A low input with coefficient profile \(c+g\) has norm rate at most \(c+2G_0\). A high input with coefficient profile \(c\) has norm rate at most \(c\), since each high Newton basis element has polynomial full-normal norm.

For \(B\) inputs, of which \(h\) are high, (H18) consequently gives raw rate
\[
 \sum c_b+2(B-h)G_0.
\]
A high output uses a polynomial-norm probe and polynomial-norm reconstruction, giving (H19) at that same rate. A low output costs at most \(G_0\) for its probe and another \(G_0\) for reconstruction, giving (H20). These are absolute norm estimates; they are not ratios to the complete trace of the same index tuple.

For \(B\ge3\), the independently proved geometric inequality (H6) gives
\(\widehat\omega_B>2BG_0\). Thus every high-input contribution and the high output of the all-low input product lie strictly below the original turned pressure. The new one-high obstruction is consistent with this: its positive complete scalar may be much smaller than this absolute coupled budget.

The \(B=2\) exceptions are also safe. Two low input indices have sum at most \(d\), so their raw polynomial product is canonical and unchanged. One high input and low output produce a cubic trace with two low incident factors; its degree is at most \(2d<2N-1\), equivalently the exact return support is empty because those two low indices have sum below \(N\). The old high-input/probe gap is applied only after this exact equality. Cases with high output and/or two high inputs are covered by the strict norm savings in (H19)–(H20). No one-high moving-versus-complete pointwise inequality is used.

## 2. Adjacent path-admissible components

In component_extension Section 3, the clean branch in (15) has low coefficient support. Equation (20) defines its next clean output by projecting the product of clean children onto low output indices. Every factor in the trace to which source_bounds (F19) is applied is therefore low, including the output probe.

The positive reference polynomial may have additional complete high coefficients. Enlarging the complete comparison from the low projection to that full positive reference uses positivity of the old multiplication only. It does not extend the moving trace comparison to high factors.

The remainder estimate (21) is instead a full norm estimate. An input error saves its maintained \(\gamma_i\) in the raw product. High extraction costs a power of \(N\); low extraction and reconstruction can cost \(2G_0\). This cost is written explicitly in
\[
 \gamma_{\mathrm{out}}
 \ge\min(\Delta_v,\Delta_v+\gamma_*-2G_0).
\]
Sections 4–5 then prove and use the coupled pressure lower bound
\(\Delta_v\ge2G_0-\varepsilon_k\). The path condition pays the possible repeated deficit; no one-high scalar ratio is substituted for it.

The witness in Section 4, (23)–(27), selects only low Newton indices in a complete positive trace. The odd Fourier positivity and interval-tail lower bound used there are within their stated all-low range.

Section 6 distinguishes inherited full-cone losses from newly generated high outputs. Equation (16) converts a full-norm deficit through a physical decorated turn into a deficit in both coefficient ranges. The whole-component pressure is affine in these constants, as stated in (36). This homogeneity avoids a further unnecessary charge across a flagged separator; it does not assert a high-index pointwise trace comparison.

## 3. The regular bare trace

regular_bare_trace Section 1 begins with low factors \(n_i\le M\) in (1). Its regular window (4) strengthens that to
\[
 \delta\le n_i/N\le1/2-\delta,\qquad \sum_i n_i/N\ge1+\delta.
\]
The positive sine-binomial coefficients, convolution concavity, and tail differences in Sections 2–3 all retain these assumptions. The ratio theorem (18) in Section 4 is explicitly proved on this same window. The exact statement for at most four factors, (19), is also stated for low indices.

Section 5 applies the result to signed arrays only on a common window satisfying (4), and first bounds the error by a positive absolute majorant. It does not claim a relative result for an arbitrary signed contraction or a high-index tuple.

The trivalent extension requires a different local argument for its internal labels: on strict old cubic support the raw degree is below \(2N-1\), so the moving trace is exactly complete. The global extension draft makes that replacement explicitly. It does not invoke the regular all-low lemma across a high bare–bare edge.

## 4. Conclusion

The refuted comparison is absent from these published dependencies. The existing singleton theorem uses an all-low trace comparison plus a separate full-norm/geometric-surplus estimate. The path theorem retains the explicit turn cost and pays it with its stated pressure criterion. The local regular trace remains all-low. The counterexample therefore does not invalidate these estimates.

This conclusion checks the actual logical branches and their hypotheses, rather than inferring safety from the stated theorem scopes alone.
