# Chapters 5 and 6: signed remainder and nonzero packet

This bounded read concerns the public manuscript at
c5d9c851c672b941bdbbec51da50d8f1a5c2cf12.
No public file was edited and no certificate or numerical audit was rerun.
The accompanying JSON records the exact files and hashes read.

## 1. Conclusion and limits of the read

I found no mathematical defect in the stated signed remainder estimates
or in the nonzero local packet theorem, under their fixed
completed-root grammar. In particular I found no substitution of a
positive complete-source estimate for a signed-source estimate, no
interpolation from tested levels, and no use of a formal saddle as a
definition of the actual finite source.

This conclusion covers the chain from the displayed finite leaf
identities through the global recurrence envelope, tangent induction,
finite holomorphic window, and nonzero lattice Gaussian. It is not a
new audit of all physical crossing conventions, all hyperbolic
completion arguments, or the full charge comparison in Chapter 8.
The source identities in Appendix A remain explicit dependencies.
Their relevant polynomial/normal identities were read; their entire
quantum-group derivation was not independently reconstructed here.

There is no essential correction to recommend in Chapters 5 or 6.
The choice order for the finite contour estimates could be made more
explicit in a formal proof, as detailed in Section 5 below.

## 2. Scope and exact source inputs

The actual scope is fixed by
01-introduction.tex:132–144, Definition def:grammar:
every completed box starts with two elementary pieces, the final
closure has two completed children, the word and signs are fixed, and
the knot/no-internal-component test is separate. Lines 142 and 154
explicitly prevent extrapolating this proof to arbitrary tangle syntax
or an \(N\)-growing family.

The final two-child condition is used, rather than ornamental.
03-entropy.tex:150–168, lem:port-bounds, places the selected leaves in
a compact subset of \((1/4,1/2)\) for each fixed word. This is precisely
the strict dominance interval of B1-high-index-packet.tex:4–16.
There is no asserted common interval over all trees.

The exact local source inputs are:

* A-finite-identities.tex:96–128, eq:A-Cheb-newton and the
  high-color identity: the core/alias split is a polynomial identity
  in the full root quotient, including repeated-node derivatives.
  It is not inferred from values at distinct nodes.
* A-finite-identities.tex:130–134: the triangular half-twist
  transport retains the selected crossing scalar and full normal data.
* A-finite-identities.tex:76–94: the physical turn reverses the
  normalized Newton index, and the closing pairing is the exact
  anti-diagonal relation \(i+j=d\).
* 03-entropy.tex:49–58, eq:lattice-dimension: solving the original
  closing relation with coefficient one gives a primitive
  \(K=2H-3\) integer lattice at both parities.

These inputs account for the original finite support, rather than
using the limiting action to guess an admissible lattice.

## 3. The global signed remainder is a separate theorem

05-alias.tex:10–31, eq:leaf-envelopes, uses a uniform
exponential-rate core bound and a polynomial-times-exponential alias
bound. It does not assert a polynomial core prefactor at recurrence
collisions. Its actual global core proof is Appendix B2, not the local
asymptotic in B1.

The decisive points in B2 are as follows.

1. B2:15–70 derives the exact normalized recurrence from the literal
   finite sum, including physical \(r<h\), its zero terminal
   coefficient, and the actual terminal modulus at both parities.
   The global normalization uses the nonzero complete diagonal,
   so no negative factorial or vanishing normalization is divided out.
2. B2:82–123 locates both limiting characteristic roots inside the
   appropriate ellipse. The strict bound on a fixed interval above
   \(1/4\) includes the maximal-color collision.
3. B2:153–191 bounds fixed-length matrix products by
   Cayley--Hamilton before allowing the block length to grow.
   This avoids a singular eigenvector basis. The order is: fix an
   error budget, choose a finite block length, then take \(N\) large.
   The resulting estimates are uniform in the physical color.
4. B2:193–221 treats small indices separately by a factorial product.
   Its rate tends to zero with the lower cutoff. In the strict
   far-color estimate this cutoff is chosen after the negative
   budget on an interior interval has been fixed.
5. B2:225–318 converts these statements to the actual normalized
   Newton coefficients, proves the pure-color loss, and bounds the
   entire alias transport support.

Thus eq:b2-global-rate and eq:b2-far-color have the uniformity needed
by Chapter 5. In particular a local selected-branch expansion is not
being used across a root collision.

For the supporting-plane induction, the continuous gate domain is
the full tetrahedron in 05:27–31, including high aliased inputs.
The two-leaf and attachment certificates cover full slope intervals
or rectangles and full gate polytopes. I read the interval arithmetic
and coverage logic in Appendix C and the two verifier programs,
but did not rerun their rational data this turn. Their logical inputs
are feasibility, global concavity, and outward bounds for the
transcendental functions; numerical optimizer output is not an input
to verification.

The inherited-child step in 05:80–136 retains the child's affine
output tangent on its entire output range. It does not replace the
child by another leaf. The exact split in 05:156–161 applies the
attachment gap to a new alias and transports any old loss unchanged.
Completed/completed products add the two tangent bounds and the gate
tangent; the internal linear terms cancel at the original stationary
state. Turns alter only the fixed affine offset.

The all-core majorant has its maximum at the complete strict point:
near that point \(\widetilde g=g\), so the point is stationary for
the concave majorant. If another maximum existed, their segment
would contradict the negative Hessian in that neighborhood.
This supplies the compact off-window gap used in 05:170–176.
Inside the window the independent macroscopic-color loss from B2
applies.

There is no circular dependence between this global estimate and the
packet. B2:320–331 imports the already established positive
variational/alias margins, not the complex packet theorem. B1:675–728
then imports the global envelope from B2. Uniform \(o(N)\) errors
are absorbed only after those fixed positive margins are chosen.
The number of states is polynomial and the number of alias subsets
is fixed with the tree. This proves eq:whole-alias-gap and
eq:physical-color-gap without assuming the filled contribution
dominates.

## 4. The exact local source selects the branch and amplitude

06-packet.tex:14–20 defines the packet from a finite wire sum.
B1:30–56 fixes the canonical Gamma-product continuation and its
exact shift identity. B1:79–115 continues only the color factors in
the original finite signed sum. Thus the object is separately even
and holomorphic before any saddle estimate.

The key branch-selection argument is B1:117–274:

* The Ward relation is obtained by a displayed finite telescoping
  certificate, with both endpoint terms accounted for.
* The exact upper wall
  \(q_N(M-1,t)=0,\ U_M=1\) holds at both parities.
* A selected-root contraction is constructed on a larger fixed
  complex interval. At every physical index its continued fraction
  encounters that exact wall and forgets its artificial tail.
* Consequently eq:b1-exact-ratio is an equality with the original
  finite source, and also establishes its local nonvanishing.

The amplitude is therefore not an arbitrary matching constant.
Summing these exact ratios from the true upper endpoint fixes the
action and first transport correction; see B1:276–336.
The \(O(N^{-1})\) displacement of the parity-dependent endpoint
does not create an order-one constant because the selected logarithm
vanishes at \(x=1/2\).

The leading local expansion alone is not used on a deformed contour.
B1:338–393 first constructs a holomorphic index interpolant by
optimally truncated Euler--Maclaurin. Its error on the physical
index grid is exponentially small, uniformly in the complex color
disk. Cauchy derivative bounds come from the fixed larger tube,
not from estimates only at integer indices.

B1:399–480 retains the continuous quadratic phase and the original
external unit phase. Its exact chirp cancellation at completeness
fixes the lattice-frequency convention. Positive and negative signs
are related by Schwarz reflection, not by conjugating a free
holomorphic variable. Equations eq:b1-local-amplitudes and
eq:b1-amplitude-at-zero explicitly give a nonzero multiplier.

The action shear is identified with this source-selected action in
B1:482–519. Matching the algebraic derivative equation is followed
by the endpoint \(x\to1/2\), which removes the possible function of
color left undetermined by an \(x\)-derivative comparison.
Hence the shear is not merely a formal phase with the right Hessian.

## 5. Finite contours and the nonzero packet

B1:533–576 fixes a rectangular window with strict gate support and
color-independent integer summation set. The source-to-interpolant
error is bounded absolutely before any oscillatory cancellation.
Only afterward is the color disk shrunk so that this error is below
the selected critical action.

The finite cotangent proof at B1:611–645 has the required normalizations:
the kernel \(\pi N\cot(\pi Nz)\) has residue one, a vertical
half-grid face has bounded cotangent, and the constant horizontal
terms contribute \(N^K\) times the ordinary integral.
The determinant square root is continued from the positive
complete Gaussian. The leaf, gate and lattice powers combine to
\[
 N^{H/2}\,N^{-3(H-2)/2}\,N^{K/2}=N^{3/2}.
\]
The integer offsets are retained in the amplitude at the changed
critical point; no parity lattice-density factor is inserted.

For a completely explicit formal choice order in this contour
argument, one should record:

1. Fix the strict real rectangle and its positive boundary gap.
2. Choose a fixed imaginary height small enough both to preserve
   that boundary gap and to make the quadratic imaginary phase
   growth smaller than the cotangent decay.
3. Shrink the complex color disk to preserve the side gaps and
   place the critical point inside the translated contour.
4. Compare every absolute connector/interpolation error with the
   real part of the selected critical action on that smaller disk.

All four choices are available from the bounds stated in B1; this
is an expansion of its argument, not an additional hypothesis or a
found gap.

At completeness the leading density is the positive pure density
times a product of explicitly nonzero signed factors. The Hessian
is the original negative-definite one. Thus the leading coefficient
is nonzero at zero color, and remains nowhere zero after shrinking
the disk. Separate evenness removes the wire--color Schur
correction at zero and gives the displayed negative real color
Hessian. This proves the exact finite packet and its complex
Gaussian bound, not merely an expansion on the real color grid.

This nonzero contribution is the local all-core packet of
eq:packet. It should not be confused with a separately projected
central sector of the general matched-sphere source in Appendix O.
Nor is nonzero local amplitude by itself a proof of noncancellation
after auxiliary filling.

## 6. Interface with filling and a formal dependency order

B1:717–728 uses the exact Fourier--Hermite coefficient bound from
A-finite-identities.tex:138–168,
\(\sum_j|\beta_j^{-p}|\le2N(1+|p|)\).
For a fixed number of leaves and fixed signed powers, multiplying
these bounds preserves the global exponential remainder.
The argument does not claim a common error bound for powers
growing with \(N\), or that a bound at the augmented rate proves
the smaller filled rate.

The subsequent filling proof still needs a nonzero selected-charge
contribution, tails/connectors, and its action sufficiently close to
the augmented action. Those are the explicit Chapter 8 inputs and
were not audited in full in this read. Chapters 5 and 6 supply the
required source error, holomorphic packet, normalization, evenness,
nonzero amplitude, and Hessian without presupposing those filling
conclusions.

A suitable dependency order for internal formalization is:

1. Full root-algebra Newton, turn, trace, and core/alias identities.
2. True gate support and primitive integer-lattice elimination.
3. Uniform sine-factorial estimates, concavity, strict maximum,
   and the fixed-tree high leaf interval.
4. Exact rational supporting certificates and their analytic
   interval soundness.
5. Finite alias-sector affine-tangent induction.
6. Global recurrence ellipse and fixed-block matrix estimate,
   including the singular endpoint and far-color loss.
7. Global source restoration and high physical-color gap.
8. Exact local recurrence, terminal wall, selected contraction,
   and source-exact ratio interpolation.
9. Exponential Euler--Maclaurin interpolation, fixed chirp,
   action shear, and normalized nonzero local amplitudes.
10. Exact finite lattice contour, complex Gaussian, and nonzero
    packet.
11. Polynomial finite-Hermite transfer of the discarded source;
    the separate filling-charge and geometry theorems follow.

Modules 4 and parts of 5–6 have finite algebraic kernels suitable
for a small formal verifier. Their successful compilation would
not by itself prove the analytic enclosure rules, the global
recurrence estimates, or the complex saddle theorem. Those
dependencies should remain visible in any human description of
the formal work.
