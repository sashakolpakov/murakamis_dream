# A stable exterior controls the whole protected spectral interval

This note proves a strict bound for one left contribution of the original
finite source. All the neighboring crossing regions retain their actual
central numerators at spectrum \(-2\), while the selected spectrum ranges
over the entire real interval \([-2,2]\). The application to the original
54-region example holds along odd levels. It retains every original face
coefficient and gives the strict inequality (31). It does not estimate all
source sectors or prove a new knot-volume limit.

Here a *source* is the polynomial obtained from the literal finite crossing
operators before its original face coefficients and filling functionals are
applied. The central contribution contains paths through the middle degree;
the left contribution contains paths below it. The original main mark sets
two adjacent face variables to zero. These are called the *protected*
variables. At the selected crossing the ordered arguments are
\((C,0,A,0)\). Removing this one crossing and extracting every other
ordinary face coefficient leaves a homogeneous polynomial in the two
remaining face variables \(A,C\). This polynomial is the *exterior* of
the selected crossing; no additional tangle or manifold is inserted.

The proof has two parts. A sine-Cauchy Gram matrix bounds the exact protected
spectral functional. Log-concavity then controls the alternating truncated
exterior on an unbounded integration interval. The original cutoff leaves
enough room for its squared moment to exist. The full polynomial squared
would exceed that moment range, and is never substituted for the truncation.

## 1. The original protected functional and its spectral metric

Fix an integer level \(N\ge2\), corresponding to the original root
\(q_N=e^{\pi i/N}\). Write
\[
 d=N-1,\qquad M=\lfloor N/2\rfloor-1,\qquad
 \theta=\pi/N,\qquad c_j=2\cos((2j+1)\theta),\qquad
 s_j=2\sin(j\theta),\qquad S_j=\prod_{r=1}^j s_r.
 \tag{1}
\]
The real variable \(\sigma\) is the Casimir spectral parameter of the
selected crossing. Its protected left numerator has the following exact
coefficients, including all spectral factors from unused matrix rows:
\[
 v_j(\sigma)=(-1)^j S_j^2\prod_{r=j+1}^{d}(\sigma-c_r),
 \qquad 0\le j\le M.
 \tag{2}
\]
Thus every spectral row, repeated node, and parity endpoint remains present.
Put \(U_0=\csc^2(\theta/2)\) and
\[
 g_j(\sigma)=(-1)^jv_j(\sigma)/U_0,\qquad
 C_{ij}=\frac{\sin\theta}{\sin((i+j+1)\theta)}
 =\alpha_N\int_0^\infty\frac{t^{i+j}}{1+t^N}\,dt,
 \qquad \alpha_N=\frac{N\sin\theta}{\pi}\le1.
 \tag{3}
\]
All the integrals used here have degree at most
\[
 2M=N-2\quad(N\text{ even}),\qquad
 2M=N-3\quad(N\text{ odd}).
 \tag{4}
\]
In particular \(C\) is a positive-definite Gram matrix. Its last diagonal
entry is especially useful:
\[
 C_{MM}=
 \begin{cases}1,&N\text{ even},\\
 (2\cos\theta)^{-1},&N\text{ odd},\end{cases}
 \qquad C_{MM}\le1.
 \tag{5}
\]

The exact sine-Cauchy spectral calculation gives
\[
 \sup_{-2\le\sigma\le2}g(\sigma)^T C^{-1}g(\sigma)
 \le\frac{\pi^5}{16}(M+1)^2.
 \tag{6}
\]
For completeness, take the lower bidiagonal matrix \(A\) with diagonal
\(c_j\) and subdiagonal \(s_j^2\). The sine subtraction identities give
\(AC=CA^T\), so \(A\) is self-adjoint in the \(C^{-1}\) metric. Here
\(T_N\) is the Chebyshev polynomial defined by
\(T_N(\cos u)=\cos(Nu)\), and \(e_0\) is the first coordinate vector.
With \(\chi_N(z)=2(T_N(z/2)+1)\), the original recurrence in (2) gives
\[
 g(\sigma)=U_0^{-1}
 \frac{\chi_N(\sigma)-\chi_N(A)}{\sigma I-A}\,e_0.
 \tag{7}
\]
The quotient denotes a polynomial divided difference, including at every
spectral node. Since \(\chi_N(A)=0\), \(|\chi_N'|\le N^2\) on the real
interval, and \((C^{-1})_{00}\le\pi(M+1)^2\), its spectral theorem proves
(6), using \(U_0\ge4N^2/\pi^2\). The last evaluation bound follows by
expanding degree-\(M\) polynomials in shifted Legendre polynomials on
\([0,1]\), where the density in (3) is at least \(1/\pi\).

The matrix notation in (7) is local to this spectral calculation. In the
binary polynomial below, \(A,C\) denote the two remaining face variables.
If the original extracted exterior is
\[
 P(A,C)=\sum_{j=0}^{d}p_j A^jC^{d-j},\qquad
 Q_M(t)=\sum_{j=0}^{M}(-1)^j p_jt^j,
 \tag{8}
\]
then the original remaining targets give precisely
\[
 S_N(\sigma)=\sum_{j=0}^{M}v_j(\sigma)p_j.
 \tag{9}
\]
There is no extra degree target. Cauchy--Schwarz in (3), followed by (6),
therefore proves
\[
 \sup_{\sigma\in[-2,2]}|S_N(\sigma)|
 \le \frac{\pi^{5/2}}4\,U_0(M+1)\,\|Q_M\|_C,
 \qquad
 \|Q_M\|_C^2=\alpha_N\int_0^\infty
                   \frac{|Q_M(t)|^2}{1+t^N}\,dt.
 \tag{10}
\]
The prefactor is polynomial in \(N\). Both parities are included in this
finite spectral statement.

## 2. A finite alternating-section estimate

A real polynomial is called *real stable* when it does not vanish if every
variable has positive imaginary part. A homogeneous binary real-stable
polynomial with nonnegative coefficients factors into positive linear
factors. For the finite estimate we use that explicit factorization:
suppose the nonzero exterior has
\[
 P(A,C)=P(1,1)\prod_{r=1}^{d}[(1-\lambda_r)C+\lambda_r A],
 \qquad 0\le\lambda_r\le1,\qquad P(1,1)>0.
 \tag{11}
\]
Write \(P(t)=P(t,1)\), and define
\[
 \nu=\frac1d\sum_r\lambda_r,\qquad
 k=\frac1d\sum_r\lambda_r(1-\lambda_r),\qquad
 a=1-\nu-k,\qquad b=\nu-k.
 \tag{12}
\]
Here \(k\) is a finite polynomial response, not the protected spectral
dual norm. For any fixed \(T\ge1\), put
\[
 R_T=\max\{a,b,1-4k,a/T+bT-2k\}.
 \tag{13}
\]
The following inequality is completely finite:
\[
 \boxed{\quad
 \|Q_M\|_C\le
 \sqrt{1+\log T}\,P(1,1)R_T^{d/2}
 +\max\{P(T)/T^M,(d+1)p_M\}+p_M.
 \quad}
 \tag{14}
\]
It requires no lower bound for any coefficient, no bound for a coefficient
ratio, and no moment of the full squared polynomial.

First, the coefficients in (11) have contiguous support and are
log-concave. This follows directly by multiplying successively by positive
linear factors. If \((c_j)\) is log-concave and \(q_j=u c_j+v c_{j-1}\),
then
\[
 \begin{aligned}
 q_j^2-q_{j-1}q_{j+1}
 ={}&u^2(c_j^2-c_{j-1}c_{j+1})
   +v^2(c_{j-1}^2-c_{j-2}c_j)\\
 &+uv(c_jc_{j-1}-c_{j-2}c_{j+1})\ge0.
 \end{aligned}
 \tag{15}
\]
The last inequality follows from the ordering of consecutive ratios;
endpoint zeros follow by continuity. Monomial factors merely shift the
support.

Assume first \(p_Mp_{M+1}>0\), and let
\[
                       t_0=p_M/p_{M+1}.
 \tag{16}
\]
For \(t\le t_0\), the terms \(p_jt^j\) decrease from \(j=M+1\) onwards.
The alternating omitted tail is therefore bounded by its first term,
which is at most \(p_Mt^M\). For \(t\ge t_0\), the terms up to \(M\)
increase, and pairing successive terms from the last term bounds the
alternating prefix by its last term. Thus
\[
 |Q_M(t)|\le
 \begin{cases}
 |P(-t)|+p_Mt^M,&0\le t\le t_0,\\
 p_Mt^M,&t\ge t_0.
 \end{cases}
 \tag{17}
\]
At \(t=t_0\), the terms of index \(M,M+1\) are largest in the entire
coefficient sequence, so
\[
                         P(t_0)/t_0^M\le(d+1)p_M.
 \tag{18}
\]

The function \(\log P(e^z)-Mz\) is convex: its second derivative is the
variance of the exponent under the positive coefficient weights. If
\(t_0>T\), its maximum on \([\log T,\log t_0]\) is at an endpoint.
Consequently (17)--(18) give, on the whole unbounded interval \(t\ge T\),
\[
 |Q_M(t)|\le(K_T+p_M)t^M,
 \qquad K_T=\max\{P(T)/T^M,(d+1)p_M\}.
 \tag{19}
\]
If \(t_0\le T\), this follows directly from the second line of (17).
If the support lies above \(M\), the section is zero. If the support ends
at or below \(M\), the section is the full polynomial and
\(P(t)/t^M\) is nonincreasing for \(t>0\), proving (19) with the first
term in \(K_T\). These cases include every zero coefficient possibility.
In particular no division by a zero coefficient has occurred.

It remains to estimate \(P(-t)\) only on the bounded interval \([0,T]\).
The arithmetic-geometric mean inequality applied to the squared factors
in (11) gives, for \(0\le t\le1\),
\[
 |P(-t)|\le P(1,1)\max\{a,1-4k\}^{d/2}.
 \tag{20}
\]
Indeed the average square is
\(1-2(1+t)\nu+(1+t)^2(\nu-k)\), a convex quadratic whose two
endpoint values are \(a\) and \(1-4k\). For \(1\le t\le T\), divide
each squared factor by \(t\). This gives
\[
 \frac{|P(-t)|^2}{t^d}
 \le P(1,1)^2\bigl(a/t+bt-2k\bigr)^d
 \le P(1,1)^2 R_T^d.
 \tag{21}
\]
The final step uses convexity of \(a/t+bt-2k\) on \((0,\infty)\).
All factors are squared before averaging, so real zeros cause no exception.

By (17), (20), and (21), the contribution on \([0,T]\) is bounded
pointwise by the sum of \(p_Mt^M\) and the function
\[
 P(1,1)R_T^{d/2}
 \begin{cases}1,&0\le t\le1,\\t^{d/2},&1\le t\le T.\end{cases}
 \tag{22}
\]
The squared \(C\) norm of the latter function, restricted to this bounded
interval, is at most
\(P(1,1)^2R_T^d(1+\log T)\): use \(\alpha_N\le1\) and
\(t^d/(1+t^N)\le1/t\) for \(t\ge1\).
Combine (19) with Minkowski's inequality and
\(\|t^M\|_C=\sqrt{C_{MM}}\le1\). This proves (14).

The use of \(t^M\), rather than \(t^{d/2}\), on the unbounded interval
is essential. It retains the original one-row cutoff margin and makes
the tail integrable with a norm at most one. No estimate for
\(\log t_0\) is needed.

## 3. A general original-target rate criterion

Consider a fixed original source and a sequence of levels on which its
extracted exterior satisfies (11). Let \(\Phi\) denote its complete
augmented action, so that \(2\pi\Phi\) is the original augmented volume.
Suppose, for one fixed \(T\ge1\),
\[
 \begin{aligned}
 \limsup_N N^{-1}\log P_N(1,1)&\le F_0,\\
 \limsup_N N^{-1}\log\bigl(P_N(T,1)/T^{d/2}\bigr)&\le F_T,\\
 \limsup_N N^{-1}\log p_{N,M}&\le\Phi-\gamma,
                 \qquad\gamma>0,\\
 \nu_N\longrightarrow\nu,\qquad k_N&\longrightarrow k.
 \end{aligned}
 \tag{23}
\]
All coefficients and limits in (23) concern the same original extracted
polynomial. Since \(d/2-M\) is \(1/2\) or \(1\), replacing
\(T^{d/2}\) by \(T^M\) changes only a bounded factor. Equations (10)
and (14) prove
\[
 \boxed{\quad
 \limsup_N\frac1N\log\sup_{\sigma\in[-2,2]}|S_N(\sigma)|
 \le\max\{F_0+\tfrac12\log R_T,\ F_T,\ \Phi-\gamma\}.
 \quad}
 \tag{24}
\]
In particular, if the first two entries are strictly below \(\Phi\),
this is a strict source gap on the entire real cap spectral interval.
Polynomial prefactors may depend on the fixed diagram; none changes (24).

For the original odd central exterior, stability is not an additional
comparison assumption. At \(N=2m+1\), each actual central endpoint
numerator is
\[
 N^2D_m(x,b,y)D_m(x,c,y),\qquad
 D_m(x,b,y)=\det\bigl(bI+xH_-/2+yH_+/2\bigr),
 \tag{25}
\]
with the actual positive-definite Hermitian matrices \(H_-,H_+\).
Each determinant in (25) is nonzero when its surviving arguments have
positive imaginary parts: the imaginary part of its matrix is positive
definite. Products and identification of shared variables preserve this
property. For differentiation, fix the other variables in the upper
half-plane and apply the one-variable Gauss--Lucas argument; specialization
at a real boundary value follows by taking a limit from the upper
half-plane. These operations preserve stability or give the zero
polynomial. Coefficient extraction is differentiation followed by such a
specialization. Thus the nonzero extracted binary polynomial has exactly
(11), with all original factors \(N^2\) retained. If it is zero, the bound
is automatic. Borcea and Brändén's
[study of stability-preserving operators](https://arxiv.org/abs/0809.0401)
provides general background for these closure operations. The quantitative
finite inequalities used here are proved in sections 1--2.

The cutoff coefficient in (23) comes from the same omitted-tail capacity
as in the original fixed-cap argument. Let \(R(s)\) be the residual
complete triangle capacity with the two unextracted loads \(s,1-s\).
The strict complete optimizer gives
\[
 \max_{1/2\le s\le1}R(s)\le\Phi-\gamma_D,
 \qquad
 \limsup_N N^{-1}\log p_{N,j_N}\le R(s)
       \quad\text{if }j_N/d\longrightarrow s.
 \tag{26}
\]
The second assertion is the closed coefficient upper bound, including
boundary loads. Since \(M/d\to1/2\), it proves the third line of (23)
with \(\gamma=\gamma_D\), even though \(M\) lies just below the first
omitted index. This uses no lower estimate and no asymptotic rounding.

## 4. The unchanged 54-region source

The selected region is \(32\), with ordered quartet \((0,50,16,29)\);
the protected faces are \(29,50\). In (8)--(9),
\(A=L_{16}\) and \(C=L_0\), so the cap is literally
\((C,0,A,0)\). Every other ordinary face target is extracted at degree
\(d\) before forming \(P_N\). The other \(53\) original regions use
their actual central endpoint numerators at \(-2\).

The exact response and complete-flow certificates give
\[
 F_0\le\frac{33947}{500},\qquad
 \frac{27}{100}\le\nu\le\frac{11}{40},\qquad
 k\ge\frac{11}{125},\qquad
 \Phi\ge\frac{67687}{1000}.
 \tag{27}
\]
Take \(T=17/5\). Direct rational arithmetic gives
\[
 a-Tb=1-(1+T)\nu+(T-1)k\ge\frac3{2500}>0.
 \tag{28}
\]
Thus the last entry in (13) is at most \(1-4k\); the other entries
give \(R_T\le81/125\). The elementary positive artanh series proves
\[
 -\tfrac12\log(81/125)>\frac{27}{125},\qquad
 F_0+\tfrac12\log R_T<\Phi-\frac9{1000}.
 \tag{29}
\]

The additional tilted certificate is a positive rational trial vector
with \(A=17/5,C=1\). It retains all \(106\) original exterior
triangle rows and the \(52\) other ordinary targets. Evaluating the
ordinary positive Cauchy upper at that vector gives
\[
 \limsup_{\substack{N\to\infty\\N\text{ odd}}}
 \frac1N\log\frac{P_N(17/5,1)}{(17/5)^{d/2}}
 <\frac{16921}{250}=67.684\le\Phi-\frac3{1000}.
 \tag{30}
\]
No stationarity of the trial vector is required for this upper bound.
Its interval evaluation uses positive rational weights, outward integer
fixed-point arithmetic, bounded arctangent and log-sine series, and the
original entropy normalization. The displayed pressure is not a different
source or a reweighted final face target.

Combining (24), (26), (29), and (30) proves the concrete conclusion
\[
 \boxed{\quad
 \limsup_{\substack{N\to\infty\\N\text{ odd}}}
 \frac1N\log\sup_{\sigma\in[-2,2]}|S_N(\sigma)|
 \le\Phi-\min\{3/1000,\gamma_D\}<\Phi.
 \quad}
 \tag{31}
\]
Every fixed smaller positive gap holds for all sufficiently large odd
levels. This is a bound for the signed original singleton coefficient,
not for its sum of absolute local arrays.

## 5. Normals, exact scope, and proof inputs

The scalar in (9) is a polynomial of degree at most \(d\) in \(\sigma\).
The complex-coefficient Markov inequality on \([-2,2]\) therefore gives
\[
 \|S_N'\|_{[-2,2]}\le\frac{d^2}{2}\|S_N\|_{[-2,2]}.
 \tag{32}
\]
To see that complex coefficients cause no problem, rotate the derivative
at a point to a positive real number and apply the real Markov inequality
to the real part of the rotated polynomial. Consequently the normalized
first normal \(N^{-2}S_N'\) has the same strict rate. Alternatively the
exact finite full-Hermite filling functional in this one cap variable
has norm at most \(1+|n|/2\) for fixed signed \(n\), so it too preserves
the strict rate. All other spectra remain fixed at \(-2\) in these
statements. Applying their filling functionals would require estimates
not supplied here.

The actual even central exterior is not known to satisfy (11), and its
positive stable comparator cannot replace it in a signed estimate.
Accordingly (31) is odd-level only. The finite theorem (14), the local
spectral metric (6), and the parity cutoff (5) themselves hold at both
parities. The proof does not bound the beta-square spectator energy by
\(e^{2N\Phi}\); it proves the desired spectral functional bound using
the separate valid sine-Cauchy norm. It makes no assertion about multiple
noncentral regions, varying neighboring spectra, an all-sector remainder,
or a new actual knot-volume equality.

The proof uses the following exact source results.

- [The coupled protected spectral functional](research_protected_cap_coupled_norm.md),
  sections 1--2, gives the unused-row vector, sine-Cauchy metric, and
  spectral divided difference. Its subsequent comparison with the
  beta-square measure is not needed here.
- [The original cap and its two negative-axis intervals](research_global_cap_negative_axis_and_mahler_bound.md),
  sections 1--4, gives the original exterior targets and the closed
  boundary capacity (26).
- [Factorization of the central cofactor](actual_cross_cofactor_factorization.md),
  section 3, and [the boundary model and its curvature](actual_q_hahn_boundary_model_curvature.md)
  give the actual odd central determinant pencils and their scalar
  normalization.
- [The exterior response criterion](research_global_cap_effective_response_criterion.md),
  sections 1--3, and [the common-axis mean and response bound](research_cap_common_axis_bound.md),
  sections 3--7, give the positive coefficient packet, its differentiated
  pressure, and the original complete-flow normalization. Only the response
  at zero is differentiated in the 54-region application here.
- [Restoring the omitted cap triangles](research_cap_dirichlet_response_region.md)
  gives a geometric sufficient response region, independent of the
  54-region certificate. Its final section combines that region with the
  finite section estimate proved here; all neighboring spectra stay fixed.
- [The finite filling supremum bound](actual_uniform_filling_supremum_bound.md)
  gives the optional one-variable full-Hermite consequence following (32).

The exact rational data for (27)--(30) are the
[exterior response certificate](../experiments/r54_response_certificate.json),
[complete feasible-flow lower certificate](../experiments/r54_complete_flow_lower_certificate.json),
and [tilted-pressure certificate](../experiments/r54_tilted_pressure_certificate.json).
From the repository root, their portable verification command is

```sh
python3 repro/check_cap_response.py
```

The verifier encloses the displayed finite classical quantities by rational
arithmetic. The analytic coefficient and spectral arguments are the proofs
above and in the linked source results; they are not consequences of
sampling quantum levels. The conclusion remains the odd-level, one-cap
bound (31), with the neighboring spectra fixed as stated.
