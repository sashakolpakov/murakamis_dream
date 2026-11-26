# Uniform ordinary-label reduction on the actual terminal input domains

Research completion, 6 November 2026. Every nonmain ordinary profile
is strictly dominated by the ordinary main maximum on the entire height
range needed by the actual typed terminal inputs. The real targets remain
independent and range over the whole plateau. This is a uniform
pointwise theorem, not a collection of sampled word references.
It proves no new terminal-profile sign or whole-invariant asymptotic.

## 1. The full containing rectangle

Retain the original own-four phase and its chirp:
\[
 Q(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs.
 \tag{1}
\]
Here
\[
 \begin{gathered}
 b=x+ik,\quad a=y+i/100,\quad x,y\in P=[11/50,9/20],\\
 -223/2000\le k\le17/250,\qquad
 -51/500\le h\le-1/1000.
 \end{gathered}
 \tag{2}
\]
Define the ordinary main and real-cut profiles by
\[
 \begin{split}
 R_0&=\max_{1/8\le s_R\le1/2}\Re Q(s_R+ih;b,a),\\
 R_L&=\Re Q(1/8;b,a),\qquad R_R=\Re Q(1/2;b,a),\\
 R_1&=2\pi(-k)_++2\pi/100.
 \end{split}
 \tag{3}
\]
The last-row envelope \(R_1\) is the maximum of the four original
affine carriers \(0,-2\pi k,2\pi/100,2\pi(1/100-k)\).

**Theorem 1.** Throughout (2),
\[
       R_L<R_0-1/500,\qquad
       R_R<R_0-1/500,\qquad
       R_1<R_0-1/400.
 \tag{4}
\]
Thus each of the six nonmain labels in the original seven-label
ordinary envelope is below \(R_0\) with common strict gap \(1/500\).

## 2. Completed upper strip and its assembly with the older bounds

The [height-extension theorem](research_mixed_terminal_ordinary_label_height_extension.md)
already proves the half-row inequality on \([-.116,.08]\), the
left-cut inequality on \([-.116,.03]\), and the last-row inequality
on \([-.1115,.08]\). Its exact inherited starting bounds are
\(49/2000,163/10000,23/625\), respectively, for the three
completed last-row, left-cut and half-row records.

For the remaining incoming strip \([.03,.068]\), the
[new fixed-trial protocol](research_mixed_terminal_upper_input_left_cut_protocol.md)
uses \(s=1/4+ih\), without optimizing or moving a source root.
Separate real concavity reduces the difference
\(\Re\{Q(1/4+ih)-Q(1/8)\}\) to the four pairs
\((x,y)\in\{.22,.45\}^2\). At these corners its exact incoming
height derivative, including the chirp, is negative. Thus the largest
incoming height \(k=.068\) is the only one that must be evaluated.
The derivative in \(h\) has absolute value below \(3\pi/4\).

The [sole fixed evaluation](../repro/results/research-mixed-terminal-upper-input-left-cut.json),
SHA256
f55e7101f558c44f11f59798e54dbf6f5250617831a7f899fd1a5513ef6342d2,
completed all 128 comparisons at 160-bit precision: four corners on
each of 32 equal closed height intervals covering \([-.102,-.001]\).
Each saved bound is its outward midpoint lower endpoint minus the
upper endpoint of its proved Lipschitz correction. The exact minimum is
\[
 \frac{321523598565176372593575865896782689064112233199}
      {93536104789177786765035829293842113257979682750464}
                       >\frac1{300}>\frac1{500}.
 \tag{5}
\]
There were 768 original-primitive evaluations and no source root,
finite sum, optimizer, adaptive subdivision or retry. This proves the
left-cut inequality on the upper strip. Its shared endpoint \(.03\)
overlaps the old lower strip, with no missing boundary. Combining the
three height ranges gives (4) on all of (2).

The [saved-only assembly checker](../experiments/check_mixed_terminal_ordinary_label_completion.py)
checks every exact height cell, midpoint, real corner, corrected
endpoint and count in this record. It also checks the 128, 128 and 32
old lower endpoints against the three stronger starting bounds above,
their exact partitions and every inherited input hash. It performs
no primitive or source replay. Its
[compact result](../repro/results/research-mixed-terminal-ordinary-label-completion.json)
records the four minima, the exact interval union, and the common gap.
The saved analytic enclosures remain inputs; the checker does not
recompute their primitive values or the constant \(\pi\).

## 3. All actual typed inputs, with independent real targets

The [typed actual-reference envelopes](research_mixed_typed_last_row_envelopes.md)
are
\[
 \begin{split}
 K_3={}&\{|b_*-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im b_*\le.068,\ 
                   \Re b_*-3\Im b_*\le.608\},\\
 K_4={}&\{|b_*-(.30-.052i)|\le.060\}
       \cap\{-.108\le\Im b_*\le-.001\}.
 \end{split}
 \tag{6}
\]
They contain all required ordinary and attached incoming references.
Both height projections lie inside (2). Consequently (4) applies to
every such reference with \(k=\Im b_*\). Importantly, its horizontal
target \(x\) is still any point of \(P\); it is not set equal to
\(\Re b_*\) or restricted by the disk equation.

**Corollary 2.** Whenever the original seven-label finite ordinary
envelope applies, at a reference in \(K_3\cup K_4\), every nonmain
ordinary label may be replaced by the main ordinary profile, with
the same terminal profile and the same complete selected-weight
alternative. The full terminal/ordinary profile maximum therefore
reduces from \(7\cdot27\cdot2=378\) entries to \(27\cdot2=54\).

Indeed the terminal factor, incoming modulus halfweight, selected
Fourier weight, and original affine marginal are independent of the
ordinary index. Adding them to (4) preserves each comparison.
The four affine periodic carriers are each bounded by \(R_1\).
The original complete-weight branch restriction, when used, is
pointwise and at the same height, so it commutes with this replacement.
The finite envelope uses one total arbitrary positive tolerance.
No Fourier summand, ordinary alias join or physical row is deleted.

This finishes the ordinary-label reduction on the full actual typed
input domains. The separately required source hypotheses are retained,
including the narrower coupled terminal-four source domain when it is
used. The 54 remaining terminal/Fourier signs are not proved uniformly
by this corollary. It does not extend the four-reference terminal-kernel
theorem to all \(K_3,K_4\), nor assert a complete open-word or new
knot-family volume theorem.
