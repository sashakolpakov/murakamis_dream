# Bounded conclusion of the even endpoint stability inquiry

The requested all-level assertion remains **unproved and unrefuted**:
no general separate real-stability proof or positive-semidefinite
determinant representation has emerged for the actual even
\(D=R_{m-1}\) and \(T=R_m\). In particular, no even negative-axis
estimate, parity bridge, source gap, or filling theorem is claimed.
All work in this pass is private; no repository file was changed.

## What is proved

1. **An exact all-real-face check at level eight.** The note
   `md-even-dt-separate-stability-n8-and-open-interface.md` gives
   the complete discriminants after \(A=x+y\), \(B=x-y\).
   They are positive combinations of powers of \(A^2\) and
   \(B^2\), with rationally certified radical coefficients.
   A base point has three/four real simple roots, and connectedness
   proves strict \(b\)-hyperbolicity for every real outer-face pair.
   The usual hyperbolicity-cone characterization gives separate real
   stability; the direct calculation itself proves the all-real-face
   statement. This is a finite-level result only and supplies no PSD
   matrix or extrapolation in \(N\).
2. **A uniform obstruction for proper odd lower cofactors.** The note
   `md-odd-lower-cofactor-hard-edge-obstruction.md` extends the
   earlier even hard-edge proof. For odd \(N=2m+1\) and every fixed
   \(s\ge1\), the reversed normalized \(R_{m-s}(b;1,1)\), with
   \(b=(2N^2/\pi^2)/t\), tends locally uniformly on the whole
   complex plane to
   \(f_{s+1}(t)=\sum_{r\ge0}t^r/(s+1)_r^2\).
   The limit is strictly positive on the real axis and is a
   nonpolynomial entire function of order at most one half.
   It has infinitely many nonreal zeros. Therefore, for every fixed
   requested number of nonreal roots, all sufficiently large odd
   levels have at least that many in the original cofactor.
   This excludes stable-minor and uniformly bounded-negative-index
   interpretations of the individual endpoint skipping cofactor.
   It does not decide the combined spectral derivative containing
   that cofactor.
3. **The five-term identity remains exact.** The already frozen note
   `md-even-central-five-term-decomposition-and-formalization.md`
   retains all original scalars and target shifts. Its stability
   hypotheses are still missing. The exact \(N=6\) noninterlacing
   obstruction is recorded with its discriminant in the new note;
   it rules out a common principal-minor construction, not separate
   stability or a signed decomposition using different pencils.

## Quantitative limitations

The nonreal roots detected by either hard-edge theorem have size
proportional to \(N^2\) for each fixed limiting zero. Their
Bernoulli coordinates are \(O(N^{-2})\). Thus the proof does not
show a positive fraction of bad roots, an exponential spectral cost,
or failure of a coherent source bound. A defect of size \(o(N)\),
a subexponential correction, or a bounded signed sum of stable
pieces remains possible.

The separate odd-neighborhood coefficient estimate remains valid:
the exact cost is
\((1+\epsilon/(2s_m^2))[\sinh(N\alpha)/(N\sinh\alpha)]^2\),
with \(\alpha=\operatorname{arsinh}(\sqrt\epsilon/2)\).
It does not preserve negative-axis cancellation. Neither it nor the
stable nearest-node coefficient comparison can be substituted for
the missing coherent estimate.

## Exact check and dependencies

`md-even-dt-n8-exact-certificate.py` reconstructs the original
recurrence in its exact algebraic number field, checks every
discriminant coefficient against the displayed table, and verifies
the rational radical bounds and the real base-point roots. Its JSON
contains no floating-point root samples. The script completed
successfully. Both new mathematical notes render to native MathML
without warnings and contain no control bytes.

`md-even-dt-inquiry-final-record.json` records the exact hashes of
these artifacts, the frozen companion proofs, and the source notes
actually used. The old five-term and even-obstruction files were not
changed in this pass. The mathematical inquiry stops here pending a
new all-level idea; these bounded results are not promoted to public
parity theorems.
