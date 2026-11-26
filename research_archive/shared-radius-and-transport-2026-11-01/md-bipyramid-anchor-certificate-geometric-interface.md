# Shared-radius certificates and the original bipyramid filling

This records an independent verification of the three finite certificates
\(m=6,8,10\), and a component rule valid for every even \(m\ge6\).
It asserts no shared-radius certificate for other sizes.

## 1. Ordered diagrams and their main components

The oriented white triangles are
\[
 (N,v_j,v_{j+1}),\qquad (S,v_{j+1},v_j),\qquad j\in\mathbb Z/m.
\]
Match north triangles across \(Nv_j\) for odd \(j\), and south
triangles across \(Sv_j\) for even \(j\). In source argument order
\((x,b,c,y)\), the coupons are
\[
 (N,v_{j-1},v_{j+1},v_j)\quad(j\ \mathrm{odd}),\qquad
 (S,v_{j+1},v_{j-1},v_j)\quad(j\ \mathrm{even}).           \tag{1}
\]
The south middle order is reversed. Mark the unmatched edge \(v_0v_1\).

For cyclic quadrilateral \((x,b,y,c)\), number boundary terminals by
\[
 0=xb,\quad 1=by,\quad 2=yc,\quad 3=cx.                \tag{2}
\]
These are native corners \((C_1,C_2,C_3,C_0)\) in that order.
The literal shaded map \(C_1\mapsto C_0,\ C_2\mapsto C_3\) therefore
gives untwisted pairs \((0,3),(1,2)\). Either signed half twist gives
\((0,2),(1,3)\). This is the corner indexing of
general_augmented_plat_matching_geometry.md §4, without a changed frame.

With every box even these pairings give exactly three main circles:
all unmatched north spokes, all unmatched south spokes, and the
entire equator. At a north box the strands belong to north and
equator; at a south box they belong to south and equator. Make exactly
one north box and exactly one south box odd, for instance \(j=1,0\).
The first switch merges north and equator; the second merges that
circle with south. Thus this is a knot parity for every even \(m\ge6\).
Both odd signs are independently allowed. Any fixed powers of these
parities, including independently long positive or negative powers,
preserve the component test.

This uses physical endpoint maps, not cycles of the dual graph after
removing its matching. It does not identify a named knot class or
exclude alternative Conway presentations.

## 2. What the finite certificate proves

For ordinary positive shared curvatures \(L_f\), with
\(L_{v_0}=L_{v_1}=0\), put
\[
 X_e=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),\quad
 H_e=\max(X_e,\{\log b_e:b_e>0\},\{\log c_e:c_e>0\}).
\]
The surviving anchor rates are
\[
 A_{e,L}=\max(\log c_e,Q(x_e,b_e,y_e)+\tfrac12\log c_e),
 \qquad
 A_{e,R}=\max(\log b_e,Q(x_e,c_e,y_e)+\tfrac12\log b_e).
\]
Omit an anchor exactly when its overloaded middle is protected.
Each surviving anchor has a rational positive whole shared vector
satisfying
\[
 A_{e,s}+\sum_{f\ne e}H_f-\sum_{a\ \mathrm{ordinary}}\log L_a
 <L_m-\frac3{10}\le\Phi_m-\frac3{10}.                  \tag{3}
\]
Here \(L_m\) is the entropy of a rational feasible complete triangle
flow; \(\Phi_m\) is the maximum complete positive action.

The verifier checks exactly: each triangle supplies \(1/2\), each
ordinary face demands \(1\), and every arc appears once. Hence
\(L_m\le\Phi_m\), without solving for the complete saddle. It also
checks all \(2m\) triangles, \(3m\) edges, \(m\) ordered coupons and
the protected nonmatching edge.

For a triangle with weights \(w_i\), it evaluates
\[
 D=\sqrt{w_1w_2+w_2w_3+w_3w_1},\quad a_i=\arctan(w_i/D),\quad
 Q(w)=\frac1\pi\sum_{w_i>0}
 [\Lambda(a_i)+\Lambda(\pi/2-a_i)+a_i\log w_i].
\]
One positive entry uses \(Q=\tfrac12\log w_i\) exactly. The
Lobachevsky Fourier sum through \(K\) terms has absolute tail
\(1/(2K)\), because
\(\Lambda(t)=\frac12\sum_{n\ge1}\sin(2nt)/n^2\).
Here \(K=2048\), with 192-bit Arb enclosures through every operation.
For a maximum, the maximum of the lower endpoints and maximum of the
upper endpoints form a containing interval. The smallest gap bounds are
\[
 0.4307260153\ldots,\quad0.3815006381\ldots,\quad
 0.3570485090\ldots                                  \tag{4}
\]
for \(m=6,8,10\). The proof uses \(3/10\), not these decimal abbreviations.

The independent run of /private/tmp/md-bipyramid-mark-verify-certificate.py
wrote /private/tmp/md-bipyramid-mark-peer-verified-results.json.
No optimizer is imported by the verifier.

## 3. Passage to the original full long-filling limit

The global weighted LEFT theorem and reflected RIGHT theorem apply
to each literal local numerator on all face phases and real spectra.
CROSS has its coefficientwise polynomial-cost positive endpoint
bound. These local identities require no flat plat.

For each non-CROSS sector choose a surviving one-sided anchor and
use its entire shared vector from (3) in the original coefficient
extraction. Other coupons are bounded by \(H_f\). There are finitely
many sectors. Replacing \(d/N=(N-1)/N\) by \(1\) at fixed curvatures
costs \(O(1/N)\). For every \(0<\eta<3/10\),
\[
 \|S_{N,\mathrm{full}}-S_{N,\mathrm{CROSS}}\|_{[-2,2]^m}
 \le \exp\{N(\Phi_m-\eta)+o(N)\}.                    \tag{5}
\]
Every shared variable retains all its occurrences.

The finite Hermite theorem in actual_uniform_filling_supremum_bound.md,
§§1,5,7, applies to this general Morse source. Spectral degree is at
most \(d\) in each variable; repeated-root normals remain; full and
CROSS polynomials coincide on the product node grid. Formula (4)
there bounds insertion of fixed signed powers by a constant independent
of \(N\). Thus the filled complement still has rate at most
\(\Phi_m-\eta\). This step needs no Fourier tail or complex strip.

The simple-sphere packing theorem supplies the labeled positive
certificate. actual_morse_cross_filling_period.md gives the nonzero
relative asymptotic for the entire original CROSS term, including
both parities and every charge. actual_morse_geometric_contribution.md
identifies its rate with
\(\operatorname{Vol}(S^3\setminus K_{\boldsymbol p})/(2\pi)\)
for the knot pattern of §1. The rate approaches \(\Phi_m\) as all
fixed signed powers become independently long.

Choose the common lower length threshold so that the volume drop
is below \(\eta/2\), and satisfy the analytic and metric filling
thresholds. Equation (5) is exponentially smaller than the nonzero
CROSS asymptotic. Therefore the full invariant has that same limit.
The original framing character has unit modulus; the prescribed
one-cut full conversion is polynomial in \(N\).

Thresholds depend on the fixed diagram and its witnesses. Nothing here
is uniform in growing \(m\) or in powers growing with \(N\), and no
moving-color or geometric-longitude extension is inferred.
