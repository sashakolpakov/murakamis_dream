# A correlated quadratic residual from the saved terminal center data

Research protocol, 6 November 2026. All four canonical terminal
families already have complete input-disk enclosures. This note
improves the residual majorant used for their posterior errors by
summing the complex quadratic Taylor coefficients before taking
absolute values. It uses only existing saved center values and
curvature bounds. It changes no predictor, input disk, error tube,
or original root.

## 1. The second-order cancellation

Use the eleven-term decomposition
\[
 f(q;b)=\sum_\ell\sigma_\ell v_\ell j(z_\ell)
                       +i\pi(Mq+nb+c),
 \qquad j(z)=\Log(2\sin\pi z),
 \tag{1}
\]
from [the correlated affine certificate](research_mixed_terminal_correlated_affine_family_certificate.md).
Along the same original predictor,
\[
 b=b_0+\delta,\quad q^{\rm aff}=q^0+u\delta,\quad
 z_\ell=z_\ell^0+\lambda_\ell\delta,\quad |\delta|\le r,
 \tag{2}
\]
all coefficients \(q^0,u,B,\lambda_\ell\) are the unchanged exact
saved Gaussian rationals. The original strips and logarithmic
branches are unchanged.

Write \(j_{\ell,1}=j'(z_\ell^0)\). The elementary derivative
identities give
\[
 j_{\ell,2}:=j''(z_\ell^0)=-\pi^2-j_{\ell,1}^{\,2},
 \qquad j'''(z)=-2j'(z)j''(z).
 \tag{3}
\]
Thus the complex second derivative at the center requires no new
analytic evaluation: it is computed from the saved cotangent
interval and saved certified interval for \(\pi\).

Let \(a_\ell=r|\lambda_\ell|\) and retain the original bound
\(|j''|\le m_\ell^{\rm aff}\) on the complete affine argument
disk. Integration along its radial segments gives
\[
 |j'(z)|\le |j_{\ell,1}|+m_\ell^{\rm aff}a_\ell,\qquad
 |j'''(z)|\le
 M_{\ell,3}:=
       2\bigl(|j_{\ell,1}|+m_\ell^{\rm aff}a_\ell\bigr)
                    m_\ell^{\rm aff}.
 \tag{4}
\]
Every derivative and connecting segment stays on that same regular
disk. Taylor's formula with integral remainder now yields
\[
 Bf(q^{\rm aff};b)
   =c+v\delta+\frac12 S\delta^2+\mathcal R_3(\delta),
 \tag{5}
\]
where
\[
 \begin{split}
 c&=Bf(q^0;b_0),\\
 v&=B(J_0u+L_0{\bf e}_s),\\
 S_i&=\sum_\ell \sigma_\ell(Bv_\ell)_i
                             j_{\ell,2}\lambda_\ell^{\,2},\\
 |(\mathcal R_3)_i|
  &\le\frac{|\delta|^3}{6}
           \sum_\ell|\sigma_\ell(Bv_\ell)_i|
                         M_{\ell,3}|\lambda_\ell|^3 .
 \end{split}
 \tag{6}
\]
The original chirp is exactly linear along (2), so it contributes
only to \(c,v\). There is no omitted quadratic chirp or mixed
external term. The square \(\lambda_\ell^2\) in \(S_i\) is a
complex square without conjugation. Its factors and the signs
\(\sigma_\ell\) must be combined before applying a modulus.

Consequently a valid residual vector is
\[
 R_i^{(2)}=
 |c_i|+r|v_i|+\frac{r^2}{2}|S_i|
   +\frac{r^3}{6}\sum_\ell|\sigma_\ell(Bv_\ell)_i|
                           M_{\ell,3}|\lambda_\ell|^3 .
 \tag{7}
\]
The last factor may use the exact rational
\(|\lambda_\ell|^2\) multiplied by its outward modulus upper
bound. This formula may improve the old sum of absolute quadratic
terms; no improvement is presumed. Since both residual vectors
are valid, the componentwise choice
\[
             \widehat R_i=\min(R_i^{\rm old},R_i^{(2)})
 \tag{8}
\]
is also valid throughout the whole input disk. Choosing the smaller
of two proved bounds does not alter any source or radius candidate.

## 2. Posterior error transport without a new root certificate

For each of the four already certified families, keep its chosen
tube: multiplier 2 for \(D_3\), multiplier 1 for \(D_4\), as in
[the all-input enclosure theorem](research_mixed_terminal_all_input_affine_enclosures.md).
Retain the same nonnegative error-cost matrix \(C\) of that theorem.
The old certificate proved
\[
 R^{\rm old}+C\rho<\rho,\qquad \rho(C)<1,\qquad
 (I-C)^{-1}\ge0 .
 \tag{9}
\]
Here \(\rho(C)\) denotes spectral radius, while the vector \(\rho\)
is the fixed error radius. The matrix \(C\) is an error-cost
majorant for the already located root, not a full Jacobian
contraction matrix.

The actual error \(w_i=|q_{*,i}-q_i^0-u_i(b-b_0)|\) therefore
satisfies, by the same error-path Taylor argument,
\[
 w\le\widehat R+Cw,\qquad
 w\le\widehat z:=(I-C)^{-1}\widehat R
       \le (I-C)^{-1}R^{\rm old}<\rho .
 \tag{10}
\]
All existence, uniqueness, log-branch identification and analytic
continuation statements remain supplied by the old certificates.
The new calculation only sharpens a bound on their same root.
Exact rational elimination and the identity
\[
                (I-C)\widehat z=\widehat R
 \tag{11}
\]
verify the posterior vector. Its shared affine form is retained;
independent coordinate rectangles may be enlarged from it only
afterward.

## 3. One fixed saved-only protocol

Use all four cases, in their original order, of the immutable
[correlated record](../repro/results/research-mixed-terminal-correlated-affine-family.json),
SHA256 51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1,
and the four posterior entries of the completed
[split Taylor record](../repro/results/research-mixed-terminal-split-taylor-completion.json),
SHA256 e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617.
Bind the intermediate split-inclusion record and its saved source
associations as well. The selected candidate and center/response
fields must agree through this complete chain.

Reconstruct \(c,v\) conservatively from the already saved original
logs, cotangents, chirp and exact \(B,u\), using the same outward-hull
serialized-endpoint convention as the previous saved checker.
For (3), (6), and (7), use exact rational complex interval arithmetic
and integer-square-root modulus upper bounds. The existing affine
sine witness supplies \(m_\ell^{\rm aff}\); (4) supplies \(M_{\ell,3}\)
without a new sine or cotangent call. Retain every complex
quadratic summand, its sum before modulus, each positive cubic
remainder, both candidate residual bounds, and the componentwise
choice (8).

The fixed calculation has four residual comparisons and four exact
posterior solves. It uses the old parameter disks, old affine
predictors, old certified tubes and old error-cost matrices. It
does not test new radii or retry a failed bound. Every non-improved
component remains visible. All inherited identities are checked
before and after exclusive output.

The proposed fresh output is
repro/results/research-mixed-terminal-quadratic-residual-refinement.json.
No analytic library, root or optimizer is invoked. No source,
reference, height integral, or scalar phase is reevaluated.
Improved root enclosures alone do not certify the still-unproved
uniform phase inequality: any later use of sharper force or value
bounds requires its own justified calculation on those enclosures.
