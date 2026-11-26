# Reduction of the original Fourier cap to one horizontal integral

Research deduction, 7 November 2026. The completed outgoing-boundary
estimates now remove the vertical current and both endpoint portions
of the bent main contour. What remains is one explicitly normalized
horizontal integral of the original low retained polynomial. No
estimate for its unpaid retained corrections is assumed here.

Use the actual correlated reference family and incoming allocation
of [the left-taper source theorem](research_mixed_fourier_left_taper_source_completion.md).
Write \(h_q=\Im q_*\), \(c=11/50\),
\(\alpha_N=-1/(2N)\), \(\beta_N=\alpha_N+1\), and retain
\(S_N^<(q)\), \(B_\eta(x)\), and \(d_N(X)\) from that theorem.
Let \(V_N^{\mathrm F}\) be the original complete Fourier cap.
Its low retained part is the exact physical sum of \(S_N^<\);
the remaining physical retained indices satisfy
\(j\ge\lceil N/2\rceil\).

Define
\[
 I_N^{\mathrm{hor}}
       =N\int_c^{\beta_N}S_N^<(u+i h_q)\,du,
 \qquad
 \delta_c=\frac{\kappa}{2500},\quad
 \kappa=\frac1{2500000}.
 \tag{1}
\]
The normalization \(+N\) in (1) is the zero-mode coefficient
of the original finite residue formula. The cardinal factor
\(1/N\) is already inside \(S_N^<\).

**Proposition.** Uniformly on the stated actual family, for all
sufficiently large \(N\) of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}
       |V_N^{\mathrm F}-I_N^{\mathrm{hor}}|
        \le e^{N(B_\eta(x)-\delta_c/8)}.
 \quad}
 \tag{2}
\]

*Proof.* Choose the exact outgoing path consisting, in order, of
the real segment \(\alpha_N\to0\), the taper
\(t\mapsto t+i h_qt/c\) from zero to \(c+i h_q\), the
horizontal segment in (1), and the vertical return
\(\beta_N+i h_q\to\beta_N\). The global factorial source is
holomorphic throughout the intervening half-plane, so its exact
real-endpoint contour identity applies without adding residues.

Subtracting (1) from that identity leaves four low-source terms.
The real endpoint segment has finite gap \(1/1000\) by
[the seam theorem with its premise discharged](research_mixed_fourier_left_taper_completion.md).
The taper integral has finite gap \(\delta_c/4\) by
the left-taper source theorem, equation (21). The entire signed
outgoing vertical current has gap \(1/2000\), and the unweighted
right return has gap \(1/200\), by
[the vertical-current completion](research_mixed_fourier_right_cap_vertical_current_completion.md),
equations (22) and (27). Each statement already retains its exact
summation or integration scalar and the original incoming weight.

Finally the original high retained part has finite gap
\(1/70000\), after its outgoing rows have been summed coherently,
by [the high-index source theorem](research_mixed_fourier_right_cap_coherent_high_tail_payment.md).
This bound concerns precisely the physical difference between
the complete cap and its low retained part; no off-grid high-index
estimate is substituted.

All five gaps are at least \(\delta_c/4\). The triangle inequality
therefore bounds the left side of (2) by
\(5e^{N(B_\eta-\delta_c/4)}\). Absorbing the fixed factor five
gives (2). The incoming finite weight was not divided out, so
its zeros remain allowed. \(\square\)

Equation (2) is a reduction of the actual finite source, not its
asymptotic evaluation. The joint main sheet and several retained
correction groups inside (1) have already been bounded. The
positive-height retained corrections on its right portion still
require control. One must also preserve and estimate the selected
geometric contribution before extracting a lower bound for the
whole cap. The full attachment and arbitrary short partial-filling
problems remain outside this proposition.
