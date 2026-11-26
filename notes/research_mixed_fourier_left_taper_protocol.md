# A fixed certificate for the remaining left-contour derivative

Protocol written before execution, 7 November 2026. This certificate
tests the two functions in equations (10)--(13) of
[the derivative reduction](research_mixed_fourier_left_taper_reduction.md).
It does not evaluate a quantum sum, solve a critical equation, choose
a contour from sampled values, or assert a complete source bound.

The analytic proof already treats \(0<x\le1/100\). The sole numerical
question is whether both minimized derivatives are positive on
\[
 [1/100,11/50]\times[0,51/110].
\]
The first coordinate is divided into exactly 512 equal closed
intervals, and the second into exactly 256 equal closed intervals.
Every one of these 131072 rectangles is evaluated once at 256-bit
Arb precision, using the complete previously saved rectangle for
\(Y\). There is no subdivision, retry, change of precision, alternate
branch, or preliminary point evaluation. An inconclusive rectangle
is recorded as such; it does not authorize a replacement run.

## Original geometric parameter

The parameter is the full `K` enclosure in
`repro/results/research-mixed-fourier-boundary-update.json`, inherited
unchanged through the successful Wall degree certificate. Its canonical
hash is
`00f030c9a079403c2811e9b1c0dcca898ca8d912f4c11c0e338b3cc655a89591`.
This rectangle contains the image of the full original algebraic-root
square, not just its center. The checker binds both saved certificates,
their writers, their inherited input files, and the original root
certificate. It verifies the saved associations and unchanged input
hashes before importing an analytic library. No earlier certificate
is executed again.

## Interval formula and branch guards

For each first-coordinate interval, evaluate the three unit-circle
enclosures
\[
 E=e^{-2\pi ix},\qquad
 E_-=e^{-2\pi i(x+1/8)},\qquad
 E_+=e^{-2\pi i(x+1/2)}.
\]
For each rectangle, compute
\[
 r=e^{-2\pi\lambda x},\quad Q=rE,
 \quad t^0_\nu=\Re E_\nu+\lambda\Im E_\nu.
\]
The minimizing radius is
\(t_\nu=\min(r,\max(r/2,t^0_\nu))\). This function is
nondecreasing in each of its two arguments. Therefore if the exact
outward rational endpoints of their Arb enclosures are
\([r_-,r_+]\) and \([b_-,b_+]\), a containing interval is
\[
 [\min(r_-,\max(r_-/2,b_-)),
   \min(r_+,\max(r_+/2,b_+))].
\]
The checker encloses this interval outward again before using it.
This preserves the minimizing-radius uncertainty and does not select
the midpoint of a cell.

Evaluate
\[
 D_\nu=\Log Y-\Log(1-Q)-\Log(1-YQ)+\Log(1-t_\nu E_\nu),
 \qquad H_\nu=\Re D_\nu+\lambda\Im D_\nu.
\]
All four logarithms must have arguments with strictly positive real
part, verified on their full input enclosures before evaluation.
These guards fix the original disk determinations; in particular
\(\Log Y=\log\rho+i\phi\). No argument is obtained by reducing an
angle modulo a period after evaluation.

## Fixed inventory and output

The complete analytic-call inventory is one evaluation of \(\pi\),
one logarithm of \(Y\), 1536 complex exponentials, 131072 real
exponentials, and 524288 further complex logarithms. All other
operations are interval arithmetic, exact rational conversion, or
hash and schema checks. There are zero root solves, source evaluations,
optimizations, adaptive refinements and retries.

For each cell and each sign, save outward integer endpoints in units
of \(2^{-40}\). Rounding down the lower rational endpoint and up the
upper rational endpoint preserves inclusion. A cell passes only if
both saved lower endpoints are strictly positive. The grid formulas
and integer cell indices specify all closed rectangles exactly.

The sole output is
`repro/results/research-mixed-fourier-left-taper.json`, opened with
exclusive creation before any analytic operation. The writer records
its own hash, receives the reviewed expected hash as a required
command-line argument, and verifies every input hash again at the
end. Success requires the complete fixed inventory, all grid cells,
all branch guards, positive saved lower bounds, and unchanged inputs.
An error or interruption leaves a non-success record. Only the root
agent may execute the frozen checker, once, after reviewing its full
source and receiving a separate full proof-and-code review.

If successful, this proves the directional phase inequality on the
compact rectangle. Together with Lemma 2 of the reduction it proves
the phase comparison along the proposed left taper. Uniform finite
factorial estimates at the half-grid endpoint, retained-index
corrections, the remaining vertical integral and coupled attachments
are additional requirements; none is certified by this calculation.
