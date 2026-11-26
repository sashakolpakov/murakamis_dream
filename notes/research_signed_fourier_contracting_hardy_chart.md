# A phase-sensitive Hardy chart for the signed Conway block

Written research proof, 22 November 2026.

The forced finite recurrence for the signed Fourier block has a
contracting region of fixed positive width in the input index. In this
region every output entry has a uniform relative approximation by an
explicit Cauchy kernel. The approximation is zero-free on a fixed complex
disk, and the actual rectangular crossing operator is uniformly bounded.
An exact polynomial Hardy Gram retains all output channels and both
original closing rows.

This is one universal signed-block estimate. It does not assert that
turns or branching preserve its input band, or evaluate a closed source.

## 1. The exact normalized polynomials

Use the complete Hermite algebra and centered orthonormal basis of the
[Fourier compiler](research_centered_fourier_conway_compiler.md). Put
\[
 d=N-1,\quad N\ge2,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{d^2/2},\quad
 F_c=(Q;Q)_c,\quad
 \gamma_b=e^{-\pi i(b-d/2)d/N}.
 \tag{1}
\]
All displayed fractional powers mean these exponentials. Let
\[
 \mathcal S_c(x)=\sum_{r=c}^dF_rx^r,\qquad 0\le c\le d.
\]
The [signed-slice proof](research_centered_fourier_signed_slice.md)
gives, with its original phases,
\[
 \begin{split}
 (1-x)\mathcal S_c(x)+Qx\mathcal S_c(Qx)&=F_cx^c,\\
 C_{0bc}
 &=\kappa\overline{\gamma_c}\gamma_b N^{-5/2}
 F_{d-c}q^{-c^2}(-qQ^b)^cQ^{bd}\mathcal S_c(Q^{-b}),\\
 F_cF_{d-c}&=N(-1)^cQ^{c(c+1)/2}.
 \end{split}
 \tag{2}
\]
Here \(C_{abc}=\phi(f_af_bf_c)\) and multiplication by the actual
\(R^+=\sqrt N f_0\) has matrix \(\sqrt N C_{0bc}\), with input
index \(b\) and output index \(c\).

Define polynomials independent of \(c\) by
\[
 A_1(z)=1,\qquad
 A_{m+1}(z)=1+z(1-Q^{-m})A_m(z),\qquad 1\le m<N.
 \tag{3}
\]
Here \(z\) is an auxiliary Hardy coordinate, not the original Casimir
generator. The realization below is a linear isometry, not an algebra
homomorphism.
They have the exact coefficients
\[
 A_m(z)=\sum_{j=0}^{m-1}a_{m,j}z^j,\qquad
 a_{m,j}=\prod_{\ell=m-j}^{m-1}(1-Q^{-\ell}).
 \tag{4}
\]
The coefficient at \(j=0\) is one. Iteration of (3) proves (4)
without an infinite extension.

For \(1\le m\le N\), the first equation of (2) implies
\[
 \mathcal S_c(Q^m)
       =F_cQ^{(m-1)c-m}A_m(Q^{-c}).
 \tag{5}
\]
Indeed at \(x=1\) it gives \(\mathcal S_c(Q)=F_c/Q\).
Substitution at \(x=Q^m\), followed by division by the nonzero
factor in (5), gives exactly (3) at \(z=Q^{-c}\).

Write \(b=N-m\). Substitution of (5) into (2) gives the simple
phase-preserving identity
\[
 \boxed{\qquad
 C_{0,N-m,c}
   =\kappa\overline{\gamma_c}\gamma_{N-m}N^{-3/2}
                           A_m(Q^{-c}).
 \qquad}
 \tag{6}
\]
For clarity, \(Q^{bd}=Q^m\) and
\((-qQ^b)^c=(-q)^cQ^{-mc}\). Their product with the power
in (5) leaves \((-q)^cQ^{-c}\); the last equation of (2),
together with \(q^{-c^2}\), cancels this factor exactly.
There is no parity-dependent residual phase. Formula (6) is exact
also at \(m=1,N\) and \(c=0,d\).

## 2. A uniform zero-free complex chart

Fix
\[
 0<\alpha<1/6,\qquad R\ge1,\qquad
 \rho=2R\sin(\pi\alpha)<1,\qquad
 M_N=\lfloor\alpha N\rfloor+1.
 \tag{7}
\]
Put
\[
 w_m=1-Q^{-(m-1)},\qquad D_m(z)=\frac1{1-w_mz}.
 \tag{8}
\]
For every \(1\le m\le M_N\), \(D_m\) is holomorphic on
\(|z|\le R\). The actual polynomial satisfies
\[
 \boxed{\quad
 \sup_{\substack{m\le M_N\\|z|\le R}}
 |A_m(z)-D_m(z)|
 \le \frac{2\pi R\rho}{N(1-\rho)^3}.
 \quad}
 \tag{9}
\]

Here is a direct error proof with the forcing retained. Set
\(B_j(z)=z(1-Q^{-j})\), so that
\[
 |B_j|\le\rho,\qquad |B_j-B_{j-1}|\le2\pi R/N
       \quad(1\le j\le M_N-1).
\]
Let \(e_m=A_m-D_m\). Since \(D_1=A_1=1\), \(e_1=0\).
Equations (3) and (8) give
\[
 e_{m+1}=B_m e_m+B_m(D_m-D_{m+1}).
 \tag{10}
\]
The last difference has modulus at most
\(2\pi R/[N(1-\rho)^2]\). Summing the resulting geometric
error recurrence proves (9).

Since \(|D_m|\ge(1+\rho)^{-1}\), this is also a uniform relative
estimate,
\[
 A_m(z)=\frac{1+O_{\alpha,R}(N^{-1})}{1-w_mz}.
 \tag{11}
\]
Consequently all these polynomials are zero-free on the whole closed
disk for sufficiently large \(N\). If \(R>1\), fixed \(z\)-derivatives
of the error are \(O(N^{-1})\) on every smaller disk, by the Cauchy
formula. No derivative in the discrete index or in a meridian parameter
is asserted.

There is also an all-level bound, requiring no asymptotic argument:
\[
 |A_m(z)|\le\sum_{j=0}^{m-1}\rho^j\le(1-\rho)^{-1}.
 \tag{12}
\]
If \(\rho<1/2\), the same sum gives
\(|A_m(z)|\ge(1-2\rho)/(1-\rho)>0\) at every level.

Combining (6) and (11), uniformly for every output index \(c\),
\[
 C_{0,N-m,c}
  =\frac{\kappa\overline{\gamma_c}\gamma_{N-m}}{N^{3/2}}\,
    \frac{1+O_\alpha(N^{-1})}
         {1-Q^{-c}(1-Q^{-(m-1)})},
 \qquad 1\le m\le M_N.
 \tag{13}
\]
Thus an entire positive fraction of the signed block has an individual
complex-entry estimate, with all \(N\) output channels retained.

## 3. Exact Hardy realization and the rectangular operator

Give polynomials of degree below \(N\) their coefficient Hardy norm,
\[
 \langle p,r\rangle_{H^2}
       =\sum_{j=0}^d\overline{p_j}r_j.
\]
Define their centered coefficient vector by
\[
 (\mathcal I_Np)_c
       =N^{-1/2}\overline{\gamma_c}\,p(Q^{-c}).
 \tag{14}
\]
Finite Fourier orthogonality makes \(\mathcal I_N\) an isometry.
More explicitly, in the original algebra,
\[
                  \mathcal I_N(z^j)=(-q)^je_j.
 \tag{15}
\]
To check this, multiply (14) by the centered compiler's
\(U_{rc}=N^{-1/2}\gamma_c(-qQ^c)^r\).
The root sum is zero unless \(r=j\), and then equals one.
Thus the Hardy realization is the original positive Newton norm with
known unit phases; it is not a new geometric metric.

Let \(\Pi_{\alpha,N}\) be the orthogonal projection onto the input
span of \(f_{N-m}\), \(1\le m\le M_N\). Write
\(T_{\alpha,N}:\mathbb C^{M_N}\to\mathcal H_N\) for the restriction
of \(M_{R^+}\) in this ordered orthonormal input basis.
Equation (6) is equivalently
\[
       M_{R^+}f_{N-m}
           =\frac{\kappa\gamma_{N-m}}{\sqrt N}
                                      \mathcal I_N A_m.
 \tag{16}
\]
In particular its exact Gram is
\[
 \left\langle M_{R^+}f_{N-m},M_{R^+}f_{N-n}\right\rangle
   =\frac{\overline{\gamma_{N-m}}\gamma_{N-n}}{N}
       \sum_{j=0}^{\min(m,n)-1}
                    \overline{a_{m,j}}a_{n,j}.
 \tag{17}
\]
There are no Fourier aliases in this identity.

Write \(\rho_0=2\sin(\pi\alpha)<1\). On the band,
\(|a_{m,j}|\le\rho_0^j\); hence
\[
 \boxed{\qquad
 \|M_{R^+}\Pi_{\alpha,N}\|_{\rm op}
     \le\|M_{R^+}\Pi_{\alpha,N}\|_{\rm HS}
     \le\sqrt{\frac{M_N}{N(1-\rho_0^2)}}.
 \qquad}
 \tag{18}
\]
This is an all-\(N\) bound on the actual full-output operator, not a
bound after projecting its output to a few values. It follows by
summing the squared norms in (16). Every Hermite direction remains.

Replace \(A_m(Q^{-c})\) in (16) by \(D_m(Q^{-c})\), retaining the same
scalar phases, and call the resulting rectangular matrix
\(\widetilde T_{\alpha,N}\). Formula (9) at \(R=1\) gives
\[
 \|T_{\alpha,N}-\widetilde T_{\alpha,N}\|_{\rm op}
 \le\|\cdot\|_{\rm HS}=O_\alpha(N^{-1}).
 \tag{19}
\]
Indeed every entry error is \(O(N^{-2})\), and there are \(NM_N\)
entries. This also gives an \(O(N^{-1})\) operator error for the
two corresponding input Grams, since both operators are bounded.

## 4. The Szegő kernel and the original caps

The exact Gram in (17) has the uniform approximation
\[
 \langle A_m,A_n\rangle_{H^2}
     =\frac1{1-\overline{w_m}w_n}+O_\alpha(N^{-1}).
 \tag{20}
\]
For proof, (9) bounds \(A_m-D_m\) also in Hardy norm on the unit
circle. Both Hardy norms are uniformly bounded, while
\(\langle D_m,D_n\rangle=(1-\overline{w_m}w_n)^{-1}\)
by their convergent geometric series.

Sampling the rational kernels has an exact finite correction:
\[
 \frac1N\sum_{c=0}^d
 \frac1{(1-Q^c\overline{w_m})(1-Q^{-c}w_n)}
 =\frac{1-(\overline{w_m}w_n)^N}
 {(1-\overline{w_m}w_n)(1-\overline{w_m}^{\,N})(1-w_n^N)}.
 \tag{21}
\]
Expand both geometric series and keep precisely the terms whose
degrees agree modulo \(N\). This proves (21), with absolute
convergence. Its difference from the Szegő kernel is
\(O_\alpha(\rho_0^N)\), uniformly in both band indices.
Neither (20) nor (21) gives a lower condition-number bound for a
growing family of these kernel vectors.

The original closures remain exact and may not be reconstructed from
a norm approximation. For \(p(z)=\sum_{j=0}^dp_jz^j\), (15) gives
\[
       m(\mathcal I_Np)=p_0,\qquad
       \phi(\mathcal I_Np)=(-q)^dp_d=\kappa^{-2}p_d.
 \tag{22}
\]
The compiler supplies \(m(e_j)=\delta_{j0}\) and
\(\phi(e_j)=\delta_{jd}\). Since \(M_N-1<d\), equations
(16) and (22) imply on this entire band
\[
 \phi(M_{R^+}f_{N-m})=0,\qquad
 m(M_{R^+}f_{N-m})=\kappa\gamma_{N-m}/\sqrt N.
 \tag{23}
\]
This is consistent with the exact Frobenius identity
\(\phi(R^+f_b)=\sqrt N\,\delta_{0b}\).

For comparison, the polynomial represented by sampling \(D_m\) is
\[
 \frac1{1-w_m^N}\sum_{j=0}^dw_m^jz^j.
\]
Its \(\phi\)-value is
\(\kappa^{-2}w_m^d/(1-w_m^N)\), generally nonzero. It is
exponentially small on this band, but cannot replace the exact zero
in (23) when proving a source lower bound.

Turns also remain literal. For the genuine \(Je_j=e_{d-j}\),
\[
 J\mathcal I_Np
    =\mathcal I_N\!\left[\kappa^2z^dp(Q/z)\right].
 \tag{24}
\]
The right side is a polynomial of degree at most \(d\). Low Hardy
degrees become high degrees, so the chart is not asserted invariant
under a turn or under a general branching multiplication.

## 5. Scope, sources and coverage

The negative signed block has the corresponding chart by the exact
compiler identity \(C_{dbc}=\overline{C_{0,d-b,d-c}}\). It requires
the reflected input band and retains the same original normal data.
The proof supplies no estimate for the intervening growing region or
for the full three-index tensor at a branching vertex. In particular
it constructs neither a compatible geometric Gram for an arbitrary
short component nor a nonzero original closing coefficient.

The complete proof directs are:

| Source | SHA-256 |
|---|---|
| [Signed Fourier slice, 319 lines](research_centered_fourier_signed_slice.md) | 71abfe35c8c005589762b9a5dc672dfa4c5ce95d0c7a12fddae8ad2f1586336d |
| [Centered compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

Both entire matching texts were read. For coverage, the entire
[one-head finite Euler flow](research_actual_one_head_euler_coherent_flow.md)
at a18a31a9b338a936b1a03a112b091c0da7588e6b88baa502b1378bb004cf3e65
and [physical geometric-input kernel](research_physical_crossing_qexponential_section_kernel.md)
at a935669d6c534f3c1f572abefcc1687f1e6150d85218cfc6c5e398de0a13a404
were read. They already establish exact finite Euler kernels,
small-activity zero-free charts and recovery of finite endpoint terms.
The estimate here concerns the actual centered Fourier entries on a
fixed fraction of their input indices, with every output retained.
The elementary contracting-recurrence and Hardy-kernel methods are
not claimed as general novelties.

Only written mathematics and text operations were used. Earlier finals
and public manuscripts remain unchanged.
