# Continuing the first-cap plateau certificate on actual reference domains

Research design, 5 November 2026. This is a separate second stage of
the [four-current first-cap certificate](research_mixed_first_cap_plateau_certificate.md).
Its proof, driver and incomplete first author record remain immutable.
The numerical source test, target sets, curvature and requested gap
are unchanged. Only an unnecessary portion of the auxiliary type-four
input disk is removed. No second-stage author or replay has been run;
the requested signs are still unproved.

## 1. The sufficient domain for every actual word

Keep the original endpoint input disks
\[
 D_3=\{|b-(.35-.01i)|\le.09\},\qquad
 D_4=\{|b-(.30-.052i)|\le.064\},
 \qquad
 \widehat D_3=D_3,\quad
 \widehat D_4=D_4\cap\{\Im b\ge-27/250\}.
 \tag{1}
\]
Both own endpoint types are retained on both of these input domains.
The outgoing target remains the entire plateau \([.22,.45]\), at
the attached output's reference height; the private cuts and alias
heights are exactly those of the first-stage certificate.

**Lemma 1.** For every actual open word in three and four of length
\(m\ge2\), the first endpoint's external parameter belongs to the
interior of its corresponding domain in (1).

*Proof.* In the original coordinates \((s_j,t_j)\), the first
endpoint's private and attached legs are \(s_1,t_1\), and its
external input is \(b=s_2\). When \(m\ge3\), this is a leg
of the ordinary second vertex. The whole ordinary-block image
estimate in Proposition 1 of the
[critical height bounds](research_mixed_cyclic_critical_height_bounds.md),
as inherited in Section 1 of
[local factor coverage](research_mixed_open_local_factor_coverage.md),
puts every such type-four leg at height
\[
                       -51/500<\Im s_2<-1/1000.
 \tag{2}
\]
It also puts the leg strictly in the smaller typed disk and hence
strictly in its original input disk. This invokes the full ordinary
map image bound, not a cyclic refinement about a periodic reference.

For \(m=2\), the right endpoint's attached leg is \(s_2\),
whereas its private leg is \(t_2\). The
[all-length localization proof](research_mixed_open_word_critical_localization.md),
Section 3, explicitly constructs the two endpoint maps using one
another's attached legs. The
[complete endpoint image extraction](research_mixed_open_word_endpoint_rectangles.md)
therefore gives, when that endpoint is type four,
\[
                   s_2\in(.246,.350)+i(-.108,-.020).
 \tag{3}
\]
This proves the lower bound in (1) also at length two. No private
endpoint coordinate is substituted for this input. Type-three
inputs already lie strictly in \(D_3\). The statements do not
depend on the first endpoint's own type. Reversal gives the same
input-domain conclusion at the other end, without asserting a
symmetry of the chirped finite kernel. \(\square\)

Thus (1) preserves the intended theorem for **all** actual words
of length at least two. It does not retain the stronger proposed
claim over the entire auxiliary \(D_4\). The one-vertex case
remains excluded exactly as in stage one. This domain deduction
alone proves no current inequality on the retained set.

## 2. What the first attempt establishes and leaves unresolved

The immutable first attempt is
[research-mixed-first-cap-plateau-attempt01.json](../repro/results/research-mixed-first-cap-plateau-attempt01.json),
with SHA256
`a403b6999d00a41d0fdcdb0dd826767b61b3d430cf296a77ff25d3a546471321`.
It ended with status `incomplete` at the added-depth cap 20,
without an arithmetic or inherited-root error. It contains 18,912
completed job trees, followed by the exact active tree of job 18,912
(259 nodes) and its two pending rectangles. Its 689 refinements and
all accepted nodes are retained; an incomplete record is not a
certificate of the full first-stage claim.

The unresolved box is in the own-four, neighbor-four left-cut job.
In the original normalized input coordinates its vertical interval is
\[
           [-15359/16384,-7679/8192].
 \tag{4}
\]
Since \(\Im b=-13/250+(8/125)\eta\), it corresponds to
\[
 \Im b\in[-28671/256000,-14335/128000]
                       \subset(-\infty,-27/250).
 \tag{5}
\]
The requested comparison missed the margin \(-1/20000\) there;
that noncertification is not a counterexample to the larger-domain
inequality. Equations (4)--(5) show only that this particular pending
box is outside every needed actual reference domain. All remaining
admitted boxes still require the same complete proof test.

## 3. Exact continuation with one additional exclusion rule

The new driver is
[certify_mixed_first_cap_actual_plateau.py](../experiments/certify_mixed_first_cap_actual_plateau.py).
Its first author invocation requires `--bootstrap-stage1` with the
exact immutable record above. It checks that record's hash, original
proof and script hashes, every original dependency, incomplete status,
absence of arithmetic error, all four family descriptions, both own
types, 5,258 original endpoint leaves and 21,032 jobs. The requested
constants remain
\[
           \kappa=1/2500000,\qquad
           \mu=3/200,\qquad \delta=1/20000.
 \tag{6}
\]
The stage-one numerical helpers, from the phase definitions through
root enclosures, response, target proposals, strict acceptance and
original-tree reconstruction, are copied literally. The driver
compares this source block against the hash-bound original script
before any continuation. There is no changed acceptance criterion.

For a normalized input box \(B\), retain the old strict
outside-disk exclusion `X`. The only new terminal node is `H`,
which is permitted precisely when the neighbor is type four,
the box is not already outside the original disk, and
\[
                         \sup\Im B<-7/8.
 \tag{7}
\]
Indeed \(\Im b\ge-.108\) is exactly \(\eta\ge-7/8\).
Equality boxes and boxes crossing that height are retained. The
whole original box may still be used for a source estimate; this
overestimates the required intersection and is safe. No discarded
point belongs to (1).

Each author continuation imports the 18,912 completed trees and the
active tree prefix verbatim, checks their complete right-first
partitions structurally, reconstructs their exact pending frontier,
and performs no arithmetic replay of accepted leaves. Existing
accepted leaves outside the new domain remain valid, stronger
comparisons and are not replaced by exclusions. New source failures
may subdivide the parameter box with the unchanged rule, but never
the target set. The inherited original root witness is retained on
every subcell. No complex-root proposal is allowed.

The active box remains pending throughout fallible arithmetic.
Signal-masked commits and atomic publication preserve the frontier
at the node/time/depth caps or on an unresolved failure. The limits
remain at most 600,000 additional nodes, 600 seconds, and added depth
45 (default 20). Resuming a second-stage incomplete record requires
an immutable input and a different output. The original completed
trees and active prefix must still agree literally with stage one;
all later accepted prefixes, trials, split axes and pending boxes
are reconstructed without alteration.

## 4. Complete replay and source conclusion

The final saved replay checks **every** accepted source leaf,
including all imported stage-one leaves, with its saved rational
target and original root witness. No target proposal, root proposal
or refinement is allowed. Disk exclusions and height exclusions are
validated and reported separately. The completed trees must cover
all 21,032 original jobs after the exclusions justified above.

The output binds the new proof and script, the exact stage-one
record/proof/script, all of their dependencies, and the geometric
inputs proving Lemma 1. Bootstrap, resume and replay input hashes
are distinguished. Final publication rechecks every binding. The
original first-stage proof, script and record are never rewritten.

Only after a complete author and an independent complete saved
replay may this stage assert the four comparisons on (1). The
[unchanged phase and full-source reduction](research_mixed_first_cap_plateau_phase.md)
then supplies the first-cap supporting plane on the entire outgoing
plateau at every actual endpoint reference for every \(m\ge2\),
with both own types, the original halfweight, all finite rows and
ordinary-color dependence retained. This is a first-cap theorem;
it does not by itself establish the whole ordinary open-word sum.
