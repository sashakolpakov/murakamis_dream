# Coherent radial capacity of the original augmented pretzel source

29 October 2026. These diagnostics evaluate the exact polynomial and
original source in
[the complete-base theorem](actual_pretzel_complete_base_casimir_polynomial.md).
They retain all nodal derivatives and all true winding channels.
They do not prove an asymptotic limit, a global circle supremum, or
geometric survival.

## 1. A genuine full-source finite Cauchy bound

Let \(z_N\) be that explicit half-degree polynomial and let \(R>1\).
The exact enclosing residue, with the original source normal terms,
immediately gives

\[
 |\mathcal A_{s,N}|
 \leq N^2\frac{R+R^{-1}}{(1-R^{-N})^2}
       R^{-N}\max_{|w|=R}|z_N(w+w^{-1})|^s.             \tag{1}
\]

No inner factorial sum is replaced by absolute values. Its only
maximum is the coherent actual polynomial on the specified circle.
For each fixed \(R,s\) the prefactor is polynomial in \(N\).

The classical candidate circle for the primitive winding is

\[
 c_s=2-4\sec^2(\pi/s),\qquad
 R_s=\frac{-c_s+\sqrt{c_s^2-4}}2.
\]

The compared classical action rate is

\[
 V_s/(2\pi)=\frac{4s}{\pi}
 \left[\Lambda\left(\frac\pi4+\frac\pi{2s}\right)
       +\Lambda\left(\frac\pi4-\frac\pi{2s}\right)\right].
\]

The identification and accessibility of that classical critical point
are separate from the finite inequality (1).

## 2. Coherent values, with precision replay

The capacity column below is
\(s\log\max_{|w|=R_s}|z_N(w+w^{-1})|/N-\log R_s\),
before the polynomial prefactor of (1). The period column is the
FULL original \(\log|\mathcal A_{s,N}|/N\), calculated with the
source derivative terms, not only the largest spectral value.

| Boxes | N | Coherent capacity rate | Original period rate | Candidate action rate |
|---:|---:|---:|---:|---:|
| 3 | 128 | 2.282542848771 | 2.358391191770 | 2.332487232247 |
| 3 | 256 | 2.307490060173 | 2.349466791768 | 2.332487232247 |
| 5 | 128 | 5.113656771500 | 5.175096842135 | 5.180738545635 |
| 5 | 256 | 5.147131188299 | 5.181900345453 | 5.180738545635 |
| 7 | 128 | 7.617877073877 | 7.673538626889 | 7.707108672092 |
| 7 | 256 | 7.662390577692 | 7.694267916927 | 7.707108672092 |
| 9 | 128 | 10.031081747751 | 10.083088667235 | 10.143508359858 |
| 9 | 256 | 10.087158750074 | 10.117206848457 | 10.143508359858 |

The apparent circle maximum is near the negative real axis, with a
finite-level angular shift of order \(1/N\). At \(N=256\), its angles
divided by \(\pi\) are respectively 0.998640430, 0.999300037,
0.999527662, 0.999641617. Evaluation exactly on the negative axis
changes the reported rates by less than \(2.2\cdot10^{-6}\).

The grid used \(\max(256,4N)\) angles followed by local golden-section
refinement at every sampled local maximum. This is a numerical search,
not a certified global bound. The \(N=128\) calculation was repeated
at 128 and 256 decimal digits; \(N=256\) was repeated at 256 and
512 digits. All rates reproduce the displayed twelve decimal places.
The finite Cauchy prefactor is included when checking (1); its omission
from the capacity column explains why finite capacity rates can lie
below finite period rates.

## 3. Exact remaining analytic step

These values support trying to prove a uniform coherent circle bound
at \(R_s\), including all competing branches and boundary currents.
The original period then still needs a selected saddle with a nonzero
coefficient for a LOWER/survival theorem. Formal stationary values,
convergence of these samples and positivity of the coefficient
\(b_v\) do not prove either assertion.

[Diagnostic program](../experiments/diagnose_pretzel_coherent_radial_capacity.py).
Its four JSON outputs record the base levels, two precision replays,
and the high level independently. All diagnostic processes completed;
no background calculations remain.
