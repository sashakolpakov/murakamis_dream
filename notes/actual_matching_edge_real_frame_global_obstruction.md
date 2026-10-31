# A real exceptional target cannot preserve the selected global complement

30 October 2026. The
[real-target classification](actual_matching_edge_real_target_frames.md)
constructs local real cross-central frames for every strict geometric
target c<1. They cannot also preserve the selected physical ordinary
complement in the present one-matching-edge reduction of a certified
right-angled link. This is a precise frame obstruction for that route,
not a rate gap or a contradiction to the source invariant or conjecture.

## 1. Statement and retained hypotheses

Fix an actual labeled right-angled matching-polyhedron certificate,
its literal Morse prefixes, retained half twists, primitive markings,
and original source. Choose one matching edge as the exceptional
four-port block. Assume its actual rectangle satisfies 0<c<1; the
parabolic case c=1 is not treated here.

There is NO common regular frame with all the following properties:

* Every original input/output factor outside this edge lies in the
  strict physical domain on its source-selected complete geometric
  sheet, as in the selected-factor localization theorem.
* After the ACTUAL inverse pivotal turn, both target magnetic rows
  and the normalized total are real and strictly physical, in either
  degree adapter. The two limiting target rows are distinct.
* The limiting target row distance is positive and at most 1/2, the folded
  polynomial bandwidth. In particular this includes any strict
  candidate for a nonzero real exceptional matrix entry.

The real-target classification shows that such rows must be on its
minus anti-diagonal branch. The key additional fact proved below is
that undoing the turn puts BOTH original factors at this edge in the
strict physical domain on their selected sheets as well. The geometric
white-normal argument then excludes the resulting all-factor frame.

## 2. Undo the actual turn before testing the disk strips

Retain the original incoming pair and transport

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]], P=BA,
    C=I+b(P+I), b=-i/(2c),
    A_o=C A C^-1, B_o=C B C^-1.

The target input/output pair is (A_o^-1,A) and (B_o,B^-1), with
target product T=B^-1 B_o=A A_o^-1. Let Pi be the original frame,
and Pi_t its inverse-turn frame. The actual basepath change is

    Pi_t=A_o Pi/Tr(A_o Pi).                        (1)

Here Pi is the prefix-normalized local projector
`W Pi_global/Tr(W Pi_global)`, followed by the common local
normalizing conjugacy. Its flags are the actual prefix image Wv
and the same global kernel w. This notation does not choose a new
independent frame at the edge.

In the target notation, let E=e^2, e=exp(+/-pi i tau), and

    q=rho+i sqrt(1-rho^2), q_out=conjugate(q),
    rho=rho_-<0, k=sinh^2 eta, c=sech eta.

First use the displayed ordering; exchanging q and its conjugate
will be included below. Since q is unit, the target prefix equations
and (1) give the EXACT original prefix diagonals

    Tr(A Pi)=e/q,
    Tr(A_o Pi)=e^-1/q,
    Tr(P Pi)=q^-2.                                (2)

Indeed Tr(A_o^-1 Pi_t)=1/Tr(A_o Pi), while T A_o=A and
B_o A_o=P. These identities fix the basepoint and all ratios; (2)
is not obtained by identifying Pi with Pi_t.

Write the original image and kernel flags in the disk coordinate
eta(s)=1/(2s+1) as z and w. Put H=1/c=sqrt(1+k). In this coordinate

    A=[[-1,0],[-2,-1]], P=[[-1,-2],[0,-1]],
    C acts by eta -> eta+iH,
    A_o=[[-1-2iH,-2H^2],[-2,-1+2iH]].             (3)

For Pi represented by these flags,

    Pi=[[z,-zw],[1,-w]]/(z-w).

Direct traces in (3) give

    Tr(P Pi)=-1-2/(z-w),
    Tr(A Pi)=-1+2zw/(z-w),
    Tr(A_o Pi)-Tr(A Pi)
                =[-2H^2-2iH(z+w)]/(z-w).          (4)

Use q+q^-1=2rho and (2) in (4). It follows that

    z-w=-q/rho,
    z+w=iH+(e^-1-e)/(2iH rho).                    (5)

The second term in the sum is REAL for both target adapters. Hence

    Im z=[H-sqrt(1-rho^2)/rho]/2,
    Im w=[H+sqrt(1-rho^2)/rho]/2.                  (6)

Exchanging the trace signs exchanges these heights. They are finite:
rho_- is strictly negative. Both flags lie strictly in the ACTUAL
original disk strip 0<Im eta<H precisely when

    |rho|>1/sqrt(k+2).                            (7)

For rho_-=(-sqrt(k+2)-c0)/(1+k), inequality (7) is equivalent to
c0>-1/sqrt(k+2). This is exactly the lower inequality in the
strict physical interval already required by the real-target
classification. Thus every viable real minus-branch target satisfies
its original disk's selected strip test, including when tau<1/2.

The real plus branch fails (7), but it is already excluded from a
direct nonzero folded entry by its exact row distance greater than
1/2. No source support is discarded in this argument.

## 3. Both original factors are also strictly physical

Let q=exp(i alpha), pi/2<alpha<pi, and set

    delta=1-alpha/pi in (0,1/2),
    u=(tau-delta)/2, v=(tau+delta)/2,
    0<u<tau/2<v<tau<1.

These are the target low and high rows. The original physical
coordinate dictionary applied to (2) is

    U_in=-q/e, U_out=-q e, T_original=q^2.         (8)

For q in the upper half-plane, the original two factors have total
degree

    tau_original=alpha/pi=1-delta in (1/2,1),

and their magnetic rows are u and 1-v, in one order or the other
depending on the target adapter. Their physical wire pairs are
(u,1-v) and (1-v,u). Every entry is strictly between zero and one,
and their sum is tau_original. Thus both factors lie strictly in
the ordinary complete-channel physical domain.

For q in the lower half-plane, the actual physical total is instead
1+delta, with physical magnetic rows v and 1-u. Applying the
original high-degree adapter subtracts delta from those rows and
reverses the total. The normalized total and rows are again

    1-delta,  u and 1-v.                          (9)

This explicitly covers both trace orderings and both target adapters.
There is no implicit assumption that the normalized target total tau
itself exceeds 1/2.

Combine (6),(7) with (9). The selected-sheet continuation throughout
the full strict physical domain, proved in
[the selected-factor theorem](actual_augmented_plat_selected_factor_localization.md),
identifies these strip tests with the actual source-selected input
and output sheets. Therefore BOTH original factors at the chosen
edge are now physical and selected, in the same original frame Pi.

## 4. Why the geometric global obstruction applies beyond its old headline

The original
[white-normal obstruction](actual_right_angled_selected_framing_obstruction.md)
was initially stated for an all-central source frame. Its geometric
sections 4--5 prove a stronger conditional assertion: simultaneous
STRICT physical support and the oriented disk-strip tests are
impossible in one common frame for the literal certified cut.

Here is the precise use, with no extension of an unproved source
sheet outside its domain. Write Pi_global=v ell, let w=ker ell and
w_0=r_(F_0)(v). The literal prefixes are Q_i=r_(F_i)r_(F_0).
Each adjacent white reflection preserves the two disk halfspaces.
Consequently all input/output strip tests imply w,w_0 belong to
the common shaded exterior K. In the white-normal polyhedron C,
K lies strictly inside C on its unit sphere.

Actual prefix diagonals are positive normal rescalings of the
polarized real-linear forms L_n(w,w_0). Their real kernel meets
int C. Following a line in that kernel to a triangular boundary
facet gives a nonnegative relation among the three actual prefix
diagonals of that facet. Thus zero lies in their real convex hull.
This contradicts that original factor's strict physical-support
criterion. The proof includes coincident flags and nongeneric
facet-edge intersections; it does not require exactly two generic
failures or an all-central hypothesis.

By assumption every factor outside the selected matching edge is
physical and source-selected; the full-domain theorem supplies its
strip test. Sections 2--3 supply both properties on the edge as well.
The preceding geometric contradiction proves the stated obstruction.

## 5. What must change in the proposed method

The exact real-row Green action and real exceptional operator packets
remain valid local theorems. The new conclusion is that this real
slice cannot contain the complete geometric point while retaining the
currently selected physical ordinary complement in a single common
frame. Within that one-block setup, a geometric contraction must use
complex target coordinates or change which grouping or complementary
source description is controlled.

No numerical exponential gap, vanishing of the invariant, absence of
a geometric contribution on another cycle, or impossibility of a
different source-preserving resummation is inferred. The parabolic
target c=1, boundary support, and exact limiting row coincidences
remain outside the strict local classification used here.

Focused audit: [actual inverse-turn flags and both physical adapters](../experiments/audit_actual_matching_edge_real_frame_global_obstruction.py).

Distinct limiting target rows are required.

The argument uses the explicit local-prefix projector. It makes no conclusion about a different global source route.