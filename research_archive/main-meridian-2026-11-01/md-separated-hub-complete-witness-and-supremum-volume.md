# The complete-color witness for the separated-hub supremum

Private source check, 1 November 2026. No repository statement is changed here.

The uniform moving-meridian upper bound for a separated-bare-hub source has a matching witness already supplied by the original complete-color source theorem. This yields equality for the supremum containing completeness; it does not establish a lower bound at any fixed nonzero meridian displacement.

Keep the hypotheses of `notes/actual_conway_all_strict_tree_long_twist_volume.md`: a fixed strict ordered cylindrical expression, its original loop-free one-main-component pairing, the corresponding retained half-twist pattern, and the prescribed reduced cut and framing. For at least three physical leaves, the complete core packet applies directly. For two leaves, retain the separate knot-pattern condition: its packet has a pure leaf; the both-odd two-main-component pattern is not covered by that lower theorem.

Section 6, equations (24)--(25), of that note states the exact physical complementary-color identity
\[
 h_j^\epsilon=C_j^\epsilon+(-1)^Nh_{N-j}^\epsilon,
 \qquad h_0^\epsilon=0.
\]
At every auxiliary color \(j_i=N\), the full source is therefore exactly its all-core contraction. There is no nonempty alias contribution at that color tuple. The all-core theorem bounds the complement of its fixed complete window exponentially below the complete action. Its local window, including the original lattice, chirp, offsets, and half-twist phases, satisfies
\[
 Z_N^\epsilon(N,\ldots,N)
 =\eta_N N^{3/2}a_\epsilon(0)e^{NF_0}
       \bigl(1+O(N^{-1})\bigr)
       +O\!\left(N^Ce^{N(F_0-\gamma)}\right),
 \qquad a_\epsilon(0)\ne0,
\]
where
\[
 \eta_N=\exp\!\left(\frac{i\pi(N-1)}4\sum_i\epsilon_i\right),
 \qquad |\eta_N|=1.
\]
These are precisely the all-parity packet and nonzero amplitude asserted in equation (25), backed by `notes/actual_conway_general_core_packet_and_gap.md`, section 6. In particular,
\[
 \frac1N\log|Z_N^\epsilon(N,\ldots,N)|\longrightarrow F_0.
\]
The direct complete source normalization in `notes/actual_complete_augmented_source_normalization.md`, equations (3)--(5), confirms that the prescribed reduced framing differs only by its retained unit phase. The full modified evaluation would have the additional factor \(i^{N+3}/N\); that is not included in the reduced scalar under consideration.

The new moving compiler gives
\[
 \mathcal F_{N,\mathbf j}^\epsilon(q^s)=H_N(s)Z_{N,\mathbf j}^\epsilon(s),
 \qquad H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},
 \qquad H_N(0)=1.
\]
All typed root-transfer scalars are also one at \(s=0\). Thus the preceding complete-color witness applies to the same reduced scalar used in the uniform source upper bound.

For every fixed \(0\le R<1\), the supremum over \(|s|\le R\) and all auxiliary colors contains \(s=0\), \(\mathbf j=(N,\ldots,N)\). Combining the witness with the new upper bound proves
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
  \log\sup_{\substack{|s|\le R\\1\le j_i\le N}}
       |\mathcal F_{N,\mathbf j}^\epsilon(q^s)|
       =2\pi F_0=\operatorname{Vol}(Y^\epsilon).
\]
The final identification is the existing geometry of the complete augmented exterior, with all its auxiliary crossing circles retained. No independently long filling slopes are required for this unsummed source statement. Conversely, the argument supplies no lower bound at a specified nonzero \(s\), no deformed far-color gap, and no replacement of the augmented volume by a smaller filled-knot volume.
