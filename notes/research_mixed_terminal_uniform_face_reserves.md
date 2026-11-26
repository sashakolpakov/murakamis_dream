# Real-face bounds over the canonical terminal families

Research deduction and fixed extraction protocol, 6 November 2026.

The terminal source certificates already bound eight real boundary
faces and the physical right-triangle majorant on their original
parameter cells. The earlier
[canonical extraction](research_mixed_terminal_canonical_face_reserve.md)
used only four central references. Here the reference input is allowed
to vary over its entire certified disk. We extract the source bounds
on every cell meeting the resulting enclosure of the terminal input.
No source estimate or root is recomputed.

## 1. The family being bounded

Let \(\beta,\epsilon\in\{0,1\}\). The external input has type
\(\beta\), the last ordinary block has type four, and the terminal
block has type \(\epsilon\). For \(b\in D_\beta\), let
\(q_*(b)=(e_*,\xi_*,t_*,a_*,s_*)\) be the canonical critical
point constructed in the
[all-input theorem](research_mixed_terminal_all_input_affine_enclosures.md).
Here the subscript on the disks is a flag: \(D_0\) is the type-three
disk and \(D_1\) is the type-four disk. Explicitly,
\[
 D_0=\{|b-(.35-.01i)|\le.09\},\qquad
 D_1=\{|b-(.30-.052i)|\le.064\}.
 \tag{1}
\]
This flag notation is used only in this note. Elsewhere these same
disks are denoted \(D_3,D_4\).

The [quadratic residual refinement](research_mixed_terminal_quadratic_residual_refinement.md)
gives a closed Cartesian rectangle \(A_{\beta,\epsilon}\)
containing \(a_*(D_\beta)\). Its exact rational endpoints are the
`coordinate_enclosures.a` entries of the immutable result with SHA256
2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331.
The extraction uses those complete rectangles. It does not replace
them by their centers or impose their correlation on the independent
real target variables.

The terminal input \(a_*\) has type four in all four cases, regardless
of \(\beta\). The relevant original endpoint trees therefore have
own flag \(\epsilon\) and neighbor flag one. The canonical endpoint
and the endpoint in those trees solve the same original zero-lift
equations. Their uniqueness in the original open product identifies
the two, whenever the source hypotheses below hold.

For terminal type three, the bare certificates apply on the whole
original terminal input disk. For terminal type four they apply only
to the original oriented, inverse-feasible source set. Define
\(\mathcal A_{\beta,1}\) to be those parameters in \(D_\beta\)
whose canonical terminal reference satisfies these original hypotheses
of [the coupled source continuation](research_mixed_terminal_four_coupled_source_continuation.md).
In particular the preceding ordinary and external inverse legs retain
their stipulated types, regions and equations. For type three put
\(\mathcal A_{\beta,0}=D_\beta\), subject to the same original
endpoint convention.

This definition does not prove
\(\mathcal A_{\beta,1}=D_\beta\). The coordinate rectangle is used
to select containing source cells; it is not a proof that independent
points of that rectangle satisfy the inverse constraints. Any use for
an actual word must also establish that its reference lies in the
original source set.

## 2. Covering the image by the original cells

The original normalized endpoint square is \([-1,1]^2\), with
physical coordinates
\[
 a=.30-.052i+.064(X+iY).
 \tag{2}
\]
Reconstruct its complete closed binary partition in the original
right-child-first order, with alternating split axes. Include every
neighbor-one source leaf meeting \(A_{\beta,\epsilon}\), including
an intersection along an edge or at a corner. The own-type indexing
continues to count the preceding neighbor-zero leaves. Thus none of
the saved source-job numbers changes.

The checker verifies that every rectangle lies strictly inside the
type-four input disk, has positive widths and negative imaginary
part, and is disjoint from all original geometric exclusion cells.
It verifies that the sum of its intersection areas equals its area.
The reconstructed partition has disjoint interiors and covers the
closed square; retaining every closed intersection also covers the
boundary of the rectangle. Consequently the selected leaves cover
the whole canonical image.

## 3. The nine source families and their bounds

Use exactly the same families as the canonical extraction:

* For terminal type three, the eight real-cut families in the mixed-face
  replay and its one raw half-transform family.
* For terminal type four, families zero through seven and family twenty
  of the coupled source replay. These are the eight real-cut families
  and the raw half-transform family with both private real variables
  retained.

The complete target intervals, penalties, original reference action
and bare supporting plane are unchanged. Write \(B_0\) for that bare
plane. For each selected original cell \(C\) and required family
\(f\), let \(u_{C,f}\) be its saved upper bound for the defect from
\(B_0\). It is decoded from the displayed interval
\([m\mathbin{+/-}r]\) as the exact rational \(m+r\). A rounded
decimal without an enclosing radius is not accepted.

The earlier saved extraction, SHA256
c85ef62dd25724f6bed335dc16982c2133e4f991a5badcd68e038a57b1a513aa,
already checked all 70,254 original jobs, their source trees, target
trials, summary order, author/replay identity and source/exclusion
counts. The present calculation binds that result and its checker,
and checks that the same source records and all inherited dependencies
have exactly their saved hashes. These facts are reused; no source
tree or analytic bound is evaluated again. The endpoint partition is
reconstructed because the new rectangles select different cells.

If every selected job has a finite maximum, put
\[
 U_{\beta,\epsilon,f}
    =\max_{C\cap A_{\beta,\epsilon}\ne\varnothing}u_{C,f}.
 \tag{3}
\]
A null maximum means that the source job was wholly excluded, rather
than bounded by a finite number. This extraction conservatively marks
the family unresolved if any selected job has a null maximum. It
retains all null jobs and any observed finite maximum without treating
that partial maximum as a bound for the full rectangle.

**Proposition.** Whenever (3) is defined, the bare source defect of
family \(f\) is at most \(U_{\beta,\epsilon,f}\), uniformly for
\(b\in\mathcal A_{\beta,\epsilon}\) and all of its original real
targets.

Indeed \(a_*(b)\) belongs to a selected cell. The original source
certificate for that cell applies to the reference, with its original
inverse conditions in type four, and bounds the defect by \(u_{C,f}\).
Taking the maximum proves the assertion. Geometric exclusions within
a source job remove no admissible reference by the original certificate.
The argument does not assume that every point of an enclosing box is
a realized critical point.

## 4. Passing to the joined comparison

The height-transport argument in Section 3 of the
[canonical extraction](research_mixed_terminal_canonical_face_reserve.md)
applies pointwise on the same original source domains. For each of
these nine families it carries the bare reserve to the allocated
terminal plane \(B_T\) at the common selected height \(H=.01\),
with no additional height debit. Let \(E_{\beta,\epsilon,\nu}\)
be any valid uniform upper bound for the joined-plane defect, with
the original incoming tangent and either complete weight alternative
\(\nu=0,1\). Then
\[
 \sup D_{\beta,\epsilon,\nu,f}
       \le E_{\beta,\epsilon,\nu}+U_{\beta,\epsilon,f}.
 \tag{4}
\]
The previous values of \(E\) were established only at four central
references. They are not substituted into (4) for the varying family.
A uniform plane estimate must be proved separately. The extraction
also records comparison with the earlier reserve \(11/200\), solely
to make its strength readable; passing or failing that threshold does
not by itself establish or refute the joined inequality.

## 5. Fixed saved-data calculation

The checker is
[check_mixed_terminal_uniform_face_reserves.py](../experiments/check_mixed_terminal_uniform_face_reserves.py).
It processes all four original canonical cases and nine source
families per case, in their fixed order. It binds the refinement
proof/checker/result, its preceding enclosure result, the canonical
extraction proof/checker/result and all their recorded inputs. Every
input binding is checked before and after the calculation.

For each case it saves the complete image rectangle, every intersecting
source cell, exact area coverage, all contributing job numbers and
outward upper bounds, attaining jobs, null jobs and the maximum (3)
when defined. It records the original source scope explicitly.
No new parameter partition, target trial, source replay, analytic
function, root, optimizer, or changed reference is permitted. A failed
reserve or unresolved family is retained without an automatic retry.

The proposed fresh output is
repro/results/research-mixed-terminal-uniform-face-reserves.json.
At the time this protocol is frozen, it has not been executed. The
uniform-source and joined conclusions remain conditional on the
stated checks and source hypotheses; no complete finite-source or
knot-volume theorem follows from this extraction alone.
