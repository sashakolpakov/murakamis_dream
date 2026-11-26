# Actual-reference coverage of the deeper-radius three-block estimate

Private source audit, 8 November 2026. The complete lower-left source
theorem for an ordinary next type three is proved under
\(|Y_*|\le7/10\). No eligible actual reference or knot is certified
by this audit. Whether the cap-initialized actual family has any
such references remains undecided; in particular its eligible
subfamily has not been proved nonempty.

Only written source statements and checker code were inspected.
No root, radius, action, saved-value comparison, or replay was evaluated.
The frozen source estimates and public manuscripts are unchanged.

## 1. The exact condition and the actual family

Keep the original ordinary-next family of
[the local next-source theorem, Section 2](research_mixed_three_four_next_local_source.md).
The prefix is \(34\), the next vertex is an **ordinary** three,
and its following external leg is \(b=s_4^*\). Write
\[
 y_*=q_{34}(s_*),\qquad
 (s_*,z_*)=F_3(y_*,b),\qquad
 Y_*=e^{-2\pi i y_*}.
 \tag{1}
\]
Here \(q_{34}\) is the cap-initialized following map, and \(F_3\)
is the original two-leg zero-logarithm-lift map. The original
complete left cap belongs to the definition of \(q_{34}\).
No independent choice of \(y_*\) or \(s_*\) is made.

The new source theorem's additional hypothesis is exactly
\[
 \boxed{\quad
 |e^{-2\pi i q_{34}(s_*)}|^2\le\frac{49}{100}.
 \quad}
 \tag{2}
\]
Equivalently,
\(\Im y_*\le-\log(10/7)/(2\pi)\). The remaining actual-family
conditions and all original weights are still required.

For a length-four open word, \(b\) has its attached role
\(b\in A_{n_4}\). For a longer word it has its ordinary role
\(b\in O_{n_4}\), where \(n_4\in\{3,4\}\). These are the clipped
domains in
[actual reference domains, Sections 1--2](research_mixed_actual_last_row_reference_domains.md).
The corresponding sufficient independent domains for the
ordinary half-chain are
\[
                    K\in\{A_3,A_4,O_3,O_4\}.
 \tag{3}
\]
An arbitrary point of one of these containing domains need not
be realized by a complete open word. In particular the
complete-ended word \(343\) has a terminal third vertex and is
not an ordinary-next instance of (1).

[Cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md)
already gives a unique original-log critical half-chain on every
full typed input disk. Thus the seven-coordinate system for the
prefix \(343\), with the final Gram input \(b\), has the required
branch before any proposed boundary calculation. Its literal
action is
\[
\begin{split}
\mathcal A_{343}
={}&E(s_1,u)+V_0(s_1,t_1)+V_1(s_2,t_2)+V_0(s_3,t_3)\\
 &+G(t_1,s_2)+G(t_2,s_3)+G(t_3,b),
\end{split}
\tag{4}
\]
with the original \(E,V,G\) of that lemma. In (1),
\((y_*,s_*,z_*)=(t_2,s_3,t_3)\).

## 2. What the existing image theorems do and do not imply

The
[following-curve theorem, equation (7)](research_mixed_three_four_following_critical_curve.md)
and the whole ordinary map give only the sufficient enclosure
\[
 y_*\in O_4,\qquad
 .24<\Re y_*<.36,\qquad -.102<\Im y_*<-.001 .
 \tag{5}
\]
This interval does not imply (2). The global sheet, uniqueness,
nonvanishing denominators and original logarithmic lifts in that
theorem do not supply a radius sign on a subregion of (3).
The existing following boundary protocols address different
action inequalities; their successful source conclusions do not
assert (2).

There is a useful exact distinction for the *interior* \(343\)
geometry. Theorem 1, row \(010\), of
[the conditioned critical-coordinate table](research_mixed_neighbor_conditioned_critical_boxes.md)
gives
\[
                 -49/1000<\Im t_j<-30/1000
 \tag{6}
\]
when \(j\) is the middle four of that eligible three-vertex
window. It follows that this coordinate has radius **greater**
than \(7/10\). Indeed,
\[
 -2\pi\Im t_j
 <\frac{49\pi}{500}
 <\frac{77}{250}
 <\frac6{17}
 <\log\frac{10}{7}.
 \tag{7}
\]
The first rational comparison uses \(\pi<22/7\);
\(77\cdot17=1309<1500=6\cdot250\).
For the final comparison, the elementary identity
\[
 \frac{d}{dx}\left(\log x-\frac{2(x-1)}{x+1}\right)
       =\frac{(x-1)^2}{x(x+1)^2}>0\qquad(x>1)
\]
gives \(\log(10/7)>6/17\). Exponentiating (7) proves the
strict radius exclusion.

This is not an exclusion of (2) for the cap-initialized prefix.
[Open-window inheritance, Theorem 1](research_mixed_open_word_window_inheritance.md)
licenses the conditioned table only for
\(7\le j\le m-6\). The four here is at \(j=2\), with an actual
attached left input. Repeating an open word cyclically would
change that cap equation. The cyclic table and its stronger
interior height refinements therefore cannot decide its radius.

Consequently the existing written bounds establish neither
coverage of all of (1) by (2), a nonempty eligible actual
subfamily, nor emptiness of that subfamily.

## 3. The rational eligibility locus retains both coupled maps

The rational representation can be used without discarding the
condition in (1). Use the auxiliary convention
\(U=e^{-2\pi i u}\) and the rational functions \(Z,T,P,Q,\mathcal C\)
in
[the following-curve theorem, equations (3)--(5)](research_mixed_three_four_following_critical_curve.md).
On its selected sheet they satisfy
\[
 Q(U)=e^{-2\pi i y_*},\qquad C(U):=\mathcal C(U)=e^{-2\pi i s_*}.
\]
Append the own-three instance of
[rational critical transport, equation (8)](research_mixed_rational_critical_transport.md):
\[
\begin{split}
 W(U)&=\frac{1-Q(U)(1-C(U))^2/(1-Q(U)C(U))}{C(U)},\\
 B(U)&=\frac{1-C(U)W(U)}
 {W(U)(1-C(U)W(U))+(1-W(U))^2}.
\end{split}
\tag{8}
\]
Then \(W=e^{-2\pi iz_*}\) and \(B=e^{-2\pi ib}\).
Every denominator is nonzero at an original admitted root.
The regular primitive strips and the original zero lifts in
(1) and (4) remain mandatory; an arbitrary preimage of \(B\)
is not an admitted reference.

The eligibility locus on this selected sheet is
\[
                         100|Q(U)|^2\le49.
 \tag{9}
\]
For a polynomial representation \(Q=A_Q/D_Q\) on the
nonvanishing chart it is the explicit real algebraic inequality
\(100|A_Q(U)|^2-49|D_Q(U)|^2\le0\).
Equations (8)--(9) retain the original cap and next-block
correlations. They identify a test, not a signed partition of
the typed input domains: no portion of their image has yet
been certified to satisfy (9).

## 4. Existing verification entry points and the missing test

The following are existing mathematical and code inputs, not
instructions to execute their old protocols.

* The existence, uniqueness and original branch of (4) are
  [cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md)
  and [the arbitrary-prefix theorem, Section 1](research_mixed_arbitrary_prefix_pregram_curve.md).
  A full typed-domain proof can bound the harmonic coordinate
  \(\Im t_2(b)\) on the boundary of the chosen compact domain
  in (3), since the branch is already holomorphic on a
  neighborhood of that domain. Every clipping chord as well
  as the circular pieces must be retained.
* The original cap-\(34\) five-variable equations, Jacobian,
  chamber tests and strict inclusion test are implemented in
  [the fixed center checker](../experiments/check_mixed_three_four_following_action_centers.py);
  the parameter-cell version and provenance checks are in
  [the fixed boundary checker](../experiments/check_mixed_three_four_following_boundary_cover.py).
  They solve the \(34\) prefix with \(s_3\) held external.
  Their existing case lists and outputs do **not** certify
  the coupled ordinary \(343\) eligibility condition.
* The original own-three two-leg primitives are the function
  named evalf in
  [the block certifier](../experiments/certify_mixed_cyclic_block_localization.py)
  and the independent sine/cotangent function fg in
  [its replay](../experiments/replay_mixed_cyclic_block_localization.py).
  Appending those two equations to the first five yields
  exactly (4), with \(b\) held external. This requires a new
  reviewed specification and checker; it is not an existing
  completed seven-variable certificate.
* For one **actual complete open word**, the endpoint equation,
  Jacobian, and test functions in
  [open-word localization](../experiments/certify_mixed_open_word_critical_localization.py)
  and those ordinary block primitives supply the original
  finite system. The right cap or actual suffix must be
  included. Certifying (9) for an arbitrary permitted external
  value \(b\) would prove a half-chain reference instance,
  not by itself a knot instance.

The missing extra comparison is simply (2), or its equivalent
height inequality, on certified original root enclosures.
No action or dilogarithm value is needed for that radius test.
Strict inclusion in the deep region would also certify a
neighborhood; an interval crossing the threshold is inconclusive.

Any evaluation must first receive its own complete written
protocol, separate source/code review, frozen input manifest
and declared case inventory. Its record must retain every
failure and inconclusive case, the original cap/ordinary
roles, branches, and all prescribed coverage. The old
following-action or saved-response protocols do not authorize
this new comparison. Nothing in this audit executes or
authorizes a numerical test.

Until such coverage is established, the deeper-radius source
theorem is a restricted-domain theorem. It supplies no
additional knot-family coverage merely from its \(R\le7/10\)
hypothesis.
