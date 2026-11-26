# Read-only integration audit of the cap response certificates

This report concerns the current publication checkout and the four requested
interfaces: the portable runner, the three response/entropy verifiers, section
7 of the common-axis proof, and the Methods subsection on extracting the
exterior before estimating the cap. No verifier, reproduction suite, quantum
sample, or build was run for this audit. No public file was edited.

No mathematical defect in the certificate chain or its stated source scope
was found. One malformed Methods TeX fragment was reported and has been
corrected in the subsequently read source. A small edge-counting clarification
is recorded below.

## 1. Fresh reports and the dependency chain

`repro/check_cap_response.py` executes the topology, response, complete-flow,
tilted-pressure, and stable-section checks in that order. Each target report
is removed before its subprocess starts; a nonzero exit or absent output
aborts the run. The tilted verifier receives the exact `response.json` path
produced earlier in this invocation. Thus an old checked-in result cannot
replace the fresh response computation. Each subprocess uses the same Python
executable with `-I`, and the verifiers reject disabled assertions.

The standalone tilted verifier reads a separately supplied response report;
it does not independently redo the response localization. Its text and output
scope say this. The default integrated command supplies that missing freshness
guarantee. It checks that the response refers to the same original source
certificate and retains the response file hash in its result. The final runner
also records the exact script, certificate, interval-engine, and written-proof
hashes.

The runner distinguishes written proof inputs from finite tests. Its listed
unproved-by-the-checks inputs include the odd determinant stability, limiting
coefficient estimates, strict omitted-coefficient gap, and original complete
geometric volume identity. Its exclusions retain the even exterior, varying
neighboring spectra, and full filled-knot remainder. This is the correct
semantic separation.

## 2. Outward interval arithmetic

The imported interval engine uses integer endpoints at scale \(10^{40}\).
Addition and negation are exact at that scale. Multiplication takes the four
endpoint products with outward floor/ceiling division; division takes the four
endpoint quotients and excludes a denominator interval containing zero. The
integer-square-root wrappers correctly round the lower endpoint down and the
upper endpoint up.

The arctangent wrapper applies the exact positive half-angle identity until
the entire interval lies below \(1/2\), then includes the next-term remainder
after 80 alternating terms. Interval dependence can widen this enclosure but
cannot reverse containment. The logarithm uses the positive artanh series
after power-of-two scaling, with its geometric tail included. The Machin
formula encloses \(\pi\) by rational alternating series.

For the log-sine integral, the Euler product gives the negative remainder
after the twentieth zeta term. Bounding each later zeta value by two and each
denominator below by \(21\cdot43\) gives exactly
\(-2t^{43}/(21\cdot43(1-t^2))\). The rational-flow verifier uses the
engine's exact endpoint values at \(0,1/2\); the response and tilted
wrappers use interval angles strictly between these endpoints. Zeta values
are enclosed by positive sums and integral tails. There is no hidden
floating-point function in the acceptance arithmetic.

## 3. The response localization and its constants

`experiments/verify_r54_response.py` uses the original ordered quartet
\((0,50,16,29)\), protected set \(\{29,50\}\), and boundary faces
\(A=16,C=0\). It removes only region 32, leaving 106 original triangle
rows and 52 free ordinary coordinates. The singleton rows have value
\(\tfrac12\log L\), derivative \(1/2\), and zero Hessian. Every
nontrivial triangle contributes its exact original entropy, angle loads,
and unordered-pair conductances.

The graph calculation gives the grounded Hessian lower bound by paths to
\(\{A,C\}\); parallel triangle contributions only improve it. The
test \(8g_{\max}<(1-4r)\lambda r\) has the correct Euclidean factor
since \(\sqrt{52}<8\). Together with the written conductance variation
bound, it gives an interior stationary point in the stated log-coordinate
ball. Existence, uniqueness, and identification with the exterior pressure
are consequences of this written argument, not assertions inferred from a
small numerical residual.

The electrical correction is subtracted in the correct direction:
\(E_0-r_I^TH_{II}^{-1}r_I\). Replacing the inverse quadratic term by
\(52r_{\max}^2/\lambda\) gives a lower bound for the response. The
subsequent factor \(1-4r\) and the boundary-load error
\(rD_A/(4\pi)\) match equations (38)--(39) of the common-axis note.
The calculation checks the response lower bound \(11/125\), the
pressure upper bound \(33947/500\), and a rational enclosure of the
load. The tilted verifier subsequently extracts the stronger load upper
bound \(11/40\) from this same computed enclosure.

## 4. Complete-flow and tilted-pressure normalization

The complete-flow verifier checks all 108 rows in their original oriented
order. Every supported row has mass \(1/2\), every ordinary column has
mass one, and the protected variables have no supported load. Its entropy is
therefore a feasible lower bound for the complete action. The upper endpoint
of the entropy enclosure is an upper bound for this one feasible entropy,
not an upper bound for the optimized action. The script and note retain
this distinction. The conversion \(2\pi\Phi=\operatorname{Vol}\) is
an explicitly named geometric theorem, not a conclusion of the rational
arithmetic.

The tilted verifier retains the same 106 exterior triangles and all 52
extracted demands, with \(A=17/5,C=1\). It subtracts
\(\tfrac12\log(17/5)\) only after evaluating the original positive
trial pressure. A trial positive vector is sufficient for this upper bound;
no stationary-point assertion is made there. The accepted upper bound
\(16921/250=67.684\) lies below the complete lower bound
\(67687/1000=67.687\) by \(0.003\).

The tightened response values give
\(a-(17/5)b\ge3/2500\). This reduces the tilted squared-factor term
to the same bound \(81/125\) used at zero. The loss exceeds
\(27/125=0.216\), so the zero-tilt pressure margin is \(0.009\).
The strict omitted-boundary gap remains a separate written input and is
not assigned a numerical value by any verifier.

## 5. Methods prose and the remaining scope

The new subsection correctly extracts all other original face coefficients
before forming the binary exterior. It retains the actual odd determinant
factorization, distinguishes Bernoulli response from the variance of the
root parameters, and explains the common negative-axis argument. Its
truncation, sine-Cauchy cutoff, and subsequent R54 inequality have the
correct normalization. The displayed volume is that of the original
augmented complement divided by \(2\pi\), not the filled knot volume.

The response criterion retains \(0<\nu\le1/2\), strict feasibility,
and connected support. The prose expressly leaves neighboring spectra
fixed and separates the even source and the complete remainder. No new
full volume theorem is implied.

The initially read odd-level subscript contained a broken `\rm` fragment.
The current source at Methods line 386 now has `N\text{ odd}`, which is
correct. For the later Dirichlet display, the convention should be explicit:
the edge sum is over unordered incidences, once per triangle contribution,
with multiplicity retained. With that convention the displayed minimum is
exactly \(F''(z)\), with no missing factor of two.

The scope of this report is the finite certificate integration and the
specified explanatory passage. It is not a new independent proof of all
source, geometric, or asymptotic dependencies cited by these notes.
